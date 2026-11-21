"""Moteur mémétique : la boucle ``Memetic(NR, NM)`` du pseudo-code de CLAUDE.md (étape 9).

Le moteur ne dépend que des interfaces (D5) : toutes les stratégies viennent de ``MemeticConfig``.

Déroulement d'une exécution (``run``) :
    1. valider la configuration ; émettre ``RunStarted`` ;
    2. génération 0 : ``initializer.initialize``, puis évaluer chaque individu ; émettre ``IndividualCreated``
       pour chacun et ``GenerationEnded`` ;
    3. tant que ``termination.is_done`` est faux, une génération :
        a. boucle NR, **par lot** (D7) : tirer tous les parents (``parent_selector``), produire tous les enfants
           (``crossover.recombine``), puis pour chaque enfant : décoder, évaluer (coût avant), ``local_solver``,
           ré-encoder l'horaire rendu (``encoding.encode``), évaluer ; émettre ``LocalSearchDone`` et
           ``IndividualCreated`` ;
        b. boucle NM, par lot : tirer les individus à muter (``mutable_selector``), ``mutation.mutate`` sur leur
           génome, puis comme en a. ;
        c. ``survivor_selector.select`` sur parents + nouveaux, ramenée à ``population_size`` ; émettre
           ``GenerationEnded`` ;
        d. si ``convergence.has_converged`` : émettre ``Converged``, ``restart.restart``, ``convergence.reset()``,
           émettre ``Restarted`` ;
    4. émettre ``RunEnded`` avec le meilleur individu ; fermer les destinations ; rendre ``MemeticResult``.

Chaque tâche d'un lot reçoit son propre ``random.Random`` (``derive_task_seeds``, D7) et passe par
``config.executor.map``. Les événements passent par ``ObservationHub`` (D8), depuis le fil principal, après chaque lot.
"""

from dataclasses import dataclass
import random
from typing import Generator, Iterable, Sequence, Tuple

from numpy.random import rand

from src.ga import population
from src.ga.chromosome import Encoding
from src.ga.individual import Individu
from src.ga.initialization import PopulationInitializer
from src.ga.operators import Crossover
from src.ga.population import ConvergenceCriterion, SurvivorSelector
from src.ga.selection import MutableSelector, ParentSelector
from src.memetic import local_search
from src.memetic.config import MemeticConfig
from src.memetic.local_search import LocalSolver, LocalSearchResult
from src.memetic.seeds import SeedStreams, SeedsCollection, derive_task_seeds
from src.memetic.termination import TerminationCriterion
from src.model.evaluation import CostEvaluator
from src.model.horaire import Horaire
from src.observability.events import GenerationEnded, IndividualCreated, LocalSearchDone, RunStarted
from src.observability.hub import ObservationHub
from src.observability.sinks import RecordSink


@dataclass(frozen=True)
class MemeticResult[G]:
    """Résultat d'une exécution : meilleur individu, population finale, nombre de générations et de restarts."""

    best: Individu[G]
    population: tuple[Individu[G], ...]
    generations: int
    restarts: int

@dataclass(frozen=True)
class MemeticCrossoverArgs:
    PARENT_SELECTION: random.Random
    CROSSOVER: random.Random
    LOCAL_SEARCH: random.Random

@dataclass(frozen=True)
class MemeticMutationArgs:
    MUTABLE_SELECTION: random.Random
    MUTATION: random.Random
    LOCAL_SEARCH: random.Random

class Memetic[G]:
    """Moteur mémétique, configuré par ``config``."""

    config: MemeticConfig[G]

    dispatcher: ObservationHub
    rng: random.Random

    initializer: PopulationInitializer[G]
    crossover: Crossover[G]
    termination: TerminationCriterion[G]
    encoding: Encoding[G]
    parents_selector: ParentSelector[G]
    mutable_selector: MutableSelector[G]
    survivors_selector: SurvivorSelector[G]
    solver: LocalSolver
    convergence: ConvergenceCriterion[G]

    population: tuple[Individu[G], ...]
    generation: int = 0


    def __init__(self, config: MemeticConfig[G]) -> None:
        config.validate()

        self.config = config
        self.dispatcher = self.config.dispatcher

        self.rng = random.Random()
        self.rng.seed(self.config.master_seed)

        self.initializer = self.config.initializer
        self.crossover = self.config.crossover
        self.termination = self.config.termination
        self.encoding = self.config.encoding
        self.parents_selector = self.config.parent_selector
        self.mutable_selector = self.config.mutable_selector
        self.survivors_selector = self.config.survivor_selector
        self.solver = self.config.local_solver
        self.convergence = self.config.convergence
        self.executor = self.config.executor

    def run(self) -> MemeticResult[G]:
        """Exécute l'algorithme jusqu'au critère d'arrêt et rend le résultat.

        Raises:
            InvalidMemeticConfigError, IncompatibleOperatorError: si la configuration est invalide
                (``MemeticConfig.validate``).
        """
        self.dispatcher.emit(RunStarted(self.config.master_seed, self.config.population_size, self.config.crossover_count, self.config.mutation_count))

        seeds_collection = self._generate_seed()

        self._init_population(self._generate_rng(seeds_collection.INITIALIZATION))

        while not self.termination.is_done(0, self.population):
            self.executor.map(self._crossover_loop, self._NR(seeds_collection.PARENT_SELECTION, seeds_collection.CROSSOVER, seeds_collection.LOCAL_SEARCH))
            self.executor.map(self._mutation_loop, self._NM(seeds_collection.MUTABLE_SELECTION, seeds_collection.MUTATION, seeds_collection.LOCAL_SEARCH))

        raise NotImplementedError  # Étape 9 (Xavier)

    def _init_population(self, rng: random.Random):
        def _evaluate(individual: Individu[G]):
            cost = self.config.evaluator.evaluate(individual.horaire)
            individual = individual.with_cost(cost)
            self.dispatcher.emit(
                IndividualCreated(
                    generation=self.generation,
                    origin="tomate",
                    operator=None,
                    individual=individual
                )
            )
            return individual

        self.population = self.initializer.initialize(self.config.population_size, self.rng)
        self.population = tuple([
            _evaluate(i)
            for i in self.population
        ])
        self.dispatcher.emit(
            GenerationEnded(
                generation=self.generation,
                population=self.population,
            )
        )

    def _crossover_loop(self, args: MemeticCrossoverArgs):
        """
        The crossover loop:
            Parents = SelectParent(P)
            Enfants = Recombine(Parents)
            Enfants = SolveurLocal(Enfants)
            Evaluer(Enfants)
            P = P + Enfants
        """
        _process = self._process_result("NR", "recombine")
        parents = self.parents_selector.select(self.population, self.config.crossover_count, args.PARENT_SELECTION)
        children_to_crossover = self.crossover.recombine([x.genome for x in parents], args.CROSSOVER)
        childrens = [
            _process(
                self.solver.improve(
                    self.encoding.decode(x),
                    args.LOCAL_SEARCH
                )
            )
            for x in children_to_crossover
        ]
        self.population = tuple(list(self.population) + childrens)

    def _mutation_loop(self, args: MemeticMutationArgs):
        """
        The mutation loop:
            i = SelectMutable(P)
            Mute(i)
            i = SolveurLocal(i)
            Evaluer(i)
            P = P + {i}
        """
        _process = self._process_result("NM", "mutation")
        population_subset = self.mutable_selector.select(self.population, self.config.mutation_count, args.MUTABLE_SELECTION)
        mutated = [
            self.encoding.decode(
                self.config.mutation.mutate(x.genome, args.MUTATION)
            )
            for x in population_subset
        ]
        children = [
            _process(self.solver.improve(x, args.MUTABLE_SELECTION))
            for x in mutated
        ]
        self.population = tuple(list(self.population) + children)

    def _process_result(self, origin: str, operator: str | None = None):
        def _process(result: LocalSearchResult) -> Individu[G]:
            old_cost = self.config.evaluator.evaluate(result.seed_horraire)
            new_cost = self.config.evaluator.evaluate(result.horaire)
            self.dispatcher.emit(
                LocalSearchDone(
                    generation=self.generation,
                    origin=origin,
                    operator=operator,
                    cost_before=old_cost,
                    cost_after=new_cost,
                    result=result
                )
            )

            individual = Individu.from_genome(self.encoding.encode(result.horaire), self.encoding)
            individual = individual.with_cost(new_cost)
            self.dispatcher.emit(
                IndividualCreated(
                    generation=self.generation,
                    origin=origin,
                    operator=operator,
                    individual=individual
                )
            )
            return individual
        return _process

    def _NR(self, select_parents_seed: Iterable[int], recombine_seed: Iterable[int], local_solver_seed: Iterable[int]) -> Generator[MemeticCrossoverArgs]:
        """
        Generator creating NR new random number generator to be use by the crossover loop
        The number generator is created with the help of the master seed.
        """
        for i in range(self.config.crossover_count):
            yield MemeticCrossoverArgs(
                self._generate_rng(select_parents_seed),
                self._generate_rng(recombine_seed),
                self._generate_rng(local_solver_seed)
            )

    def _NM(self, select_mutation_seed: Iterable[int], mutation_seeds: Iterable[int], local_solver_seed: Iterable[int]) -> Generator[MemeticMutationArgs]:
        """
        Generator creating NM new random number generator to be use by the mutation loop.
        The number generator is created with the help of the master seed.
        """
        for i in range(self.config.mutation_count):
            yield MemeticMutationArgs(
                self._generate_rng(select_mutation_seed),
                self._generate_rng(mutation_seeds),
                self._generate_rng(local_solver_seed)
            )

    def _generate_seed(self):
        def _seeds(streams: SeedStreams, task_count: int):
            master_seed = self.config.master_seed
            generation = self.generation
            return derive_task_seeds(master_seed, generation, SeedStreams.INITIALIZATION, self.config.crossover_count)

        collections = SeedsCollection(
            INITIALIZATION=_seeds(SeedStreams.INITIALIZATION, 1),

            PARENT_SELECTION=_seeds(SeedStreams.PARENT_SELECTION, self.config.crossover_count),
            CROSSOVER=_seeds(SeedStreams.CROSSOVER, self.config.crossover_count),

            MUTABLE_SELECTION=_seeds(SeedStreams.MUTABLE_SELECTION, self.config.mutation_count),
            MUTATION=_seeds(SeedStreams.MUTATION, self.config.mutation_count),

            LOCAL_SEARCH=_seeds(SeedStreams.LOCAL_SEARCH, self.config.mutation_count + self.config.crossover_count),

            SURVIVOR_SELECTION=_seeds(SeedStreams.SURVIVOR_SELECTION, 1),
            RESTART=_seeds(SeedStreams.RESTART, 1),
        )
        self.generation += 1
        return collections

    def _generate_rng(self, seed: Iterable[int]):
        rng = random.Random()
        rng.seed(next(iter(seed)))
        return rng

