"""Moteur mémétique : la boucle ``Memetic(NR, NM)`` du pseudo-code de CLAUDE.md (étape 9).

Le moteur ne dépend que des interfaces (D5) : toutes les stratégies viennent de ``MemeticConfig``.

Déroulement d'une exécution (``run``) :
    1. valider la configuration ; émettre ``RunStarted`` ;
    2. génération 0 : ``initializer.initialize``, puis évaluer chaque individu ; émettre un ``LocalSearchDone`` par
       recherche locale faite par l'initialiseur, puis un ``IndividualCreated`` par individu, puis ``GenerationEnded`` ;
    3. tant que ``termination.is_done`` est faux, une génération :
        a. lot NR (D7) : tirer d'un coup les ``NR × parent_count`` parents dans P (``parent_selector``), puis NR
           tâches indépendantes, chacune : ``crossover.recombine``, et pour chaque enfant : décoder, évaluer (coût
           avant), ``local_solver``, ré-encoder l'horaire rendu (``encoding.encode``), évaluer. Après le lot :
           émettre ``LocalSearchDone`` et ``IndividualCreated`` pour chaque enfant, puis P = P + enfants ;
        b. lot NM : tirer d'un coup les NM individus à muter dans P (``mutable_selector``), puis NM tâches, chacune :
           ``mutation.mutate`` sur le génome, puis comme en a. ;
        c. ``survivor_selector.select`` sur parents + nouveaux, ramenée à ``population_size`` ; émettre
           ``GenerationEnded`` ;
        d. si ``convergence.has_converged`` : émettre ``Converged`` ; ``restart.restart`` ; émettre un
           ``LocalSearchDone`` par recherche locale du restart, puis un ``IndividualCreated`` par nouvel individu
           (origine ``RESTART``) ; ``convergence.reset()`` ; émettre ``Restarted`` ;
    4. émettre ``RunEnded`` avec le meilleur individu ; fermer le hub ; rendre ``MemeticResult``.

Les tâches d'un lot passent par ``config.executor.map``. Elles ne lisent que leurs propres entrées (parents ou
génome déjà tirés, graine) et rendent leurs enfants sans rien modifier ni émettre : chaque tâche a son propre
``random.Random`` (``derive_task_seeds``, D7), et les événements sont émis depuis le fil principal, après chaque lot
(D8). Le résultat ne dépend donc pas de l'ordre d'exécution des tâches.
"""

import random
from collections.abc import Iterator, Sequence
from dataclasses import dataclass

from src.ga.individual import Individu
from src.memetic.config import MemeticConfig
from src.memetic.local_search import LocalSearchRecord, LocalSearchResult
from src.memetic.seeds import SeedStreams, derive_task_seeds
from src.model.evaluation import CostBreakdown
from src.observability.events import (
    Converged,
    GenerationEnded,
    IndividualCreated,
    LocalSearchDone,
    Origins,
    Restarted,
    RunEnded,
    RunStarted,
)


class EngineConstants:
    """Constantes du déroulement d'une exécution."""

    # La génération 0 est l'initialisation (D8).
    INITIAL_GENERATION: int = 0


@dataclass(frozen=True)
class MemeticResult[G]:
    """Résultat d'une exécution : meilleur individu, population finale, nombre de générations et de restarts."""

    best: Individu[G]
    population: tuple[Individu[G], ...]
    generations: int
    restarts: int


@dataclass(frozen=True)
class CrossoverTask[G]:
    """Une tâche du lot NR : les génomes des parents, déjà tirés, et la graine de la tâche."""

    parents: tuple[G, ...]
    seed: int


@dataclass(frozen=True)
class MutationTask[G]:
    """Une tâche du lot NM : le génome à muter, déjà tiré, et la graine de la tâche."""

    genome: G
    seed: int


@dataclass(frozen=True)
class ImprovedChild[G]:
    """Un nouvel individu produit par une tâche : résultat du ``LocalSolver``, coût avant la recherche locale, et
    individu ré-encodé et évalué (son coût est le coût après)."""

    search: LocalSearchResult
    cost_before: CostBreakdown
    individual: Individu[G]


class Memetic[G]:
    """Moteur mémétique, configuré par ``config``. Une instance (et une configuration) par exécution."""

    def __init__(self, config: MemeticConfig[G]) -> None:
        self.config = config

    def run(self) -> MemeticResult[G]:
        """Exécute l'algorithme jusqu'au critère d'arrêt et rend le résultat.

        Raises:
            InvalidMemeticConfigError, IncompatibleOperatorError: si la configuration est invalide
                (``MemeticConfig.validate``), avant tout événement.
        """
        self.config.validate()
        hub = self.config.dispatcher
        hub.emit(RunStarted(
            master_seed=self.config.master_seed,
            population_size=self.config.population_size,
            crossover_count=self.config.crossover_count,
            mutation_count=self.config.mutation_count,
        ))

        generation = EngineConstants.INITIAL_GENERATION
        restarts = 0
        population = self.initial_population()

        while not self.config.termination.is_done(generation, population):
            generation += 1
            population = population + self.crossover_batch(population, generation)
            population = population + self.mutation_batch(population, generation)
            population = self.config.survivor_selector.select(
                population, self.config.population_size, self.single_task_rng(generation, SeedStreams.SURVIVOR_SELECTION)
            )
            hub.emit(GenerationEnded(generation=generation, population=population))

            if self.config.convergence.has_converged(population):
                hub.emit(Converged(generation=generation))
                restart = self.config.restart.restart(population, self.single_task_rng(generation, SeedStreams.RESTART))
                self.publish_outside_searches(restart.searches, generation, Origins.RESTART)
                for individual in restart.newcomers:
                    hub.emit(IndividualCreated(
                        generation=generation, origin=Origins.RESTART.value, operator=None, individual=individual
                    ))
                population = restart.population
                self.config.convergence.reset()
                restarts += 1
                hub.emit(Restarted(generation=generation, population=population))

        best = self.best_of(population)
        hub.emit(RunEnded(generations=generation, best=best))
        hub.close()
        return MemeticResult(best=best, population=population, generations=generation, restarts=restarts)

    # -----------------------------------------------------------------------------------------------------------------
    # Étapes d'une génération (fil principal)
    # -----------------------------------------------------------------------------------------------------------------

    def initial_population(self) -> tuple[Individu[G], ...]:
        """Génération 0 : population initiale évaluée ; émet un ``LocalSearchDone`` par recherche locale de
        l'initialiseur, puis ``IndividualCreated`` pour chaque individu, puis ``GenerationEnded(0)``."""
        generation = EngineConstants.INITIAL_GENERATION
        rng = self.single_task_rng(generation, SeedStreams.INITIALIZATION)
        initialization = self.config.initializer.initialize(self.config.population_size, rng)
        population = tuple(
            individual.with_cost(self.config.evaluator.evaluate(individual.horaire))
            for individual in initialization.individuals
        )
        self.publish_outside_searches(initialization.searches, generation, Origins.INITIALIZATION)
        for individual in population:
            self.config.dispatcher.emit(IndividualCreated(
                generation=generation, origin=Origins.INITIALIZATION.value, operator=None, individual=individual
            ))
        self.config.dispatcher.emit(GenerationEnded(generation=generation, population=population))
        return population

    def crossover_batch(self, population: Sequence[Individu[G]], generation: int) -> tuple[Individu[G], ...]:
        """Lot NR : les enfants des NR croisements, réparés et évalués (événements émis après le lot)."""
        crossover_count = self.config.crossover_count
        if crossover_count == 0:
            return ()
        parent_count = self.config.crossover.parent_count()
        parents = self.config.parent_selector.select(
            population,
            crossover_count * parent_count,
            self.single_task_rng(generation, SeedStreams.PARENT_SELECTION),
        )
        parent_genomes = [parent.genome for parent in parents]
        seeds = derive_task_seeds(self.config.master_seed, generation, SeedStreams.CROSSOVER)
        tasks = [
            CrossoverTask(parents=tuple(parent_genomes[start:start + parent_count]), seed=next(seeds))
            for start in range(0, crossover_count * parent_count, parent_count)
        ]
        children_by_task = self.config.executor.map(self.run_crossover_task, tasks)
        children = [child for task_children in children_by_task for child in task_children]
        return self.publish(children, generation, Origins.CROSSOVER, type(self.config.crossover).__name__)

    def mutation_batch(self, population: Sequence[Individu[G]], generation: int) -> tuple[Individu[G], ...]:
        """Lot NM : les NM individus mutés, réparés et évalués (événements émis après le lot)."""
        mutation_count = self.config.mutation_count
        if mutation_count == 0:
            return ()
        selected = self.config.mutable_selector.select(
            population, mutation_count, self.single_task_rng(generation, SeedStreams.MUTABLE_SELECTION)
        )
        seeds = derive_task_seeds(self.config.master_seed, generation, SeedStreams.MUTATION)
        tasks = [MutationTask(genome=individual.genome, seed=next(seeds)) for individual in selected]
        children = self.config.executor.map(self.run_mutation_task, tasks)
        return self.publish(children, generation, Origins.MUTATION, type(self.config.mutation).__name__)

    def publish(
            self, children: Sequence[ImprovedChild[G]], generation: int, origin: Origins, operator: str
    ) -> tuple[Individu[G], ...]:
        """Émet ``LocalSearchDone`` puis ``IndividualCreated`` pour chaque enfant, dans l'ordre ; rend les individus."""
        for child in children:
            self.config.dispatcher.emit(LocalSearchDone(
                generation=generation,
                origin=origin.value,
                operator=operator,
                cost_before=child.cost_before,
                cost_after=child.individual.cost,
                result=child.search,
            ))
            self.config.dispatcher.emit(IndividualCreated(
                generation=generation, origin=origin.value, operator=operator, individual=child.individual
            ))
        return tuple(child.individual for child in children)

    def publish_outside_searches(
            self, searches: Sequence[LocalSearchRecord], generation: int, origin: Origins
    ) -> None:
        """Émet un ``LocalSearchDone`` (opérateur ``None``) pour chaque recherche locale faite hors du moteur, par
        l'initialiseur ou le restart : la charge du solveur est ainsi mesurée partout (D10)."""
        evaluator = self.config.evaluator
        for search in searches:
            self.config.dispatcher.emit(LocalSearchDone(
                generation=generation,
                origin=origin.value,
                operator=None,
                cost_before=evaluator.evaluate(search.input_horaire),
                cost_after=evaluator.evaluate(search.result.horaire),
                result=search.result,
            ))

    # -----------------------------------------------------------------------------------------------------------------
    # Tâches (indépendantes : ni état modifié, ni événement)
    # -----------------------------------------------------------------------------------------------------------------

    def run_crossover_task(self, task: CrossoverTask[G]) -> tuple[ImprovedChild[G], ...]:
        """Un croisement, puis la recherche locale de chaque enfant, avec le générateur de la tâche."""
        rng = random.Random(task.seed)
        child_genomes = self.config.crossover.recombine(task.parents, rng)
        return tuple(self.improve(genome, rng) for genome in child_genomes)

    def run_mutation_task(self, task: MutationTask[G]) -> ImprovedChild[G]:
        """Une mutation, puis la recherche locale du mutant, avec le générateur de la tâche."""
        rng = random.Random(task.seed)
        mutant = self.config.mutation.mutate(task.genome, rng)
        return self.improve(mutant, rng)

    def improve(self, genome: G, rng: random.Random) -> ImprovedChild[G]:
        """Décode ``genome``, l'évalue (coût avant), le passe au ``LocalSolver``, ré-encode l'horaire rendu et
        l'évalue (coût après)."""
        encoding = self.config.encoding
        evaluator = self.config.evaluator
        horaire = encoding.decode(genome)
        cost_before = evaluator.evaluate(horaire)
        search = self.config.local_solver.improve(horaire, rng)
        individual = Individu.from_genome(encoding.encode(search.horaire), encoding)
        individual = individual.with_cost(evaluator.evaluate(individual.horaire))
        return ImprovedChild(search=search, cost_before=cost_before, individual=individual)

    # -----------------------------------------------------------------------------------------------------------------
    # Utilitaires
    # -----------------------------------------------------------------------------------------------------------------

    def single_task_rng(self, generation: int, stream: SeedStreams) -> random.Random:
        """Générateur d'un lot d'une seule tâche (sélection, initialisation, restart) : la première graine du lot."""
        seeds: Iterator[int] = derive_task_seeds(self.config.master_seed, generation, stream)
        return random.Random(next(seeds))

    @staticmethod
    def best_of(population: Sequence[Individu[G]]) -> Individu[G]:
        """L'individu de plus petit ``cost.total`` (le premier rencontré en cas d'égalité)."""
        return min(population, key=lambda individual: individual.cost.total)
