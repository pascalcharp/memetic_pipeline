"""Tests du moteur mémétique (src/memetic/engine.py, config.py, seeds.py, termination.py) — étape 9, Xavier.

Tests écrits par Claude (règle des tests par agent, CLAUDE.md), à faire passer sur la branche ``etape-9-boucle``.
Ils suivent le déroulement décrit dans la docstring de ``engine.py``. Sans MiniZinc : faux objets de
``tests/fixtures.py``, vrais sélecteurs (7a), vrais opérateurs (7b), ``RandomBlockInitializer`` (6) et
``CostEvaluator`` (4) sur l'instance synthétique. L'exécution avec les vrais composants et MiniZinc est la
sous-étape 9-intégration (Pascal). Validés le 2026-11-16 contre un moteur de référence jetable (35 tests verts),
qui n'est pas dans le dépôt : à toi d'écrire le tien.

Déroulement attendu, tel que les tests le vérifient :
    - ``run`` valide la configuration avant tout (aucun événement si elle est invalide) ;
    - événements : ``RunStarted`` en premier, ``RunEnded`` en dernier ; génération 0 : un ``IndividualCreated``
      (origine ``Origins.INITIALIZATION``, opérateur ``None``) par individu initial, puis ``GenerationEnded(0)`` ;
      génération g ≥ 1 : pour chaque nouvel individu, ``LocalSearchDone`` puis ``IndividualCreated`` (origine
      ``CROSSOVER`` ou ``MUTATION``, opérateur = nom de la classe de l'opérateur), puis ``GenerationEnded(g)``, puis,
      si le critère converge, ``Converged(g)`` et ``Restarted(g)`` ;
    - par génération : NR appels à ``crossover.recombine``, NM appels à ``mutation.mutate``, un appel au
      ``LocalSolver`` par nouvel individu ; pas de ``LocalSolver`` à l'initialisation (l'initialiseur a son option) ;
    - ``termination.is_done(g, population)`` est consulté après chaque génération, à partir de la génération 0 :
      avec ``GenerationLimit(G)``, il y a exactement G générations après l'initialisation.
"""

import dataclasses
import random
from collections.abc import Iterator, Sequence
import unittest
from unittest import mock
from collections import Counter

from src.ga.chromosome import BlockEncoding, Encoding
from src.ga.chromosome import BlockGenome
from src.ga.initialization import PopulationInitializer, RandomBlockInitializer
from src.ga.operators import ShiftStartMutation, UniformGeneCrossover
from src.ga.population import EliteRestart, SurvivorSelector
from src.ga.registry import IncompatibleOperatorError
from src.ga.selection import TournamentSelector, UniformMutableSelector
from src.memetic.config import InvalidMemeticConfigError, MemeticConfig, MemeticError
from src.memetic.engine import Memetic, MemeticResult
from src.memetic.executor import Executor, SequentialExecutor
from src.memetic.local_search import LocalSearchResult
from src.memetic.seeds import SeedStreams, derive_task_seeds
from src.memetic.termination import (
    GenerationLimit,
    InvalidTerminationParameterError,
    TerminationCriterion,
)
from src.model.evaluation import CostEvaluator
from src.model.horaire import Horaire
from src.observability.hub import ObservationHub
from src.ga.individual import Individu
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
from tests.fixtures import (
    FakeConvergenceCriterion,
    FakeCrossover,
    FakeLocalSolver,
    FakeMutation,
    FakeRestartPolicy,
    FakeSurvivorSelector,
    RecordingCollector,
    synthetic_instance,
)

POPULATION_SIZE: int = 4
CROSSOVER_COUNT: int = 2
MUTATION_COUNT: int = 1
MASTER_SEED: int = 42
OTHER_SEED: int = 43
GENERATIONS: int = 3
INVALID_GENERATIONS: int = 0
CONVERGENCE_CALL: int = 2
EMPLOYEE_COUNT: int = 3
REAL_RUN_GENERATIONS: int = 5
REAL_RUN_POPULATION: int = 6
SEED_BATCH: int = 100
SEED_PREFIX: int = 3
SEED_GENERATION: int = 7
CHILDREN_PER_CROSSOVER: int = FakeCrossover.PARENT_COUNT
# NR et NM différents du nombre de parents et de 1 : un moteur qui confondrait NR et le nombre de parents, ou
# qui ferait NM mutations par tâche, est alors détecté.
LARGE_CROSSOVER_COUNT: int = 3
LARGE_MUTATION_COUNT: int = 3
ONE_GENERATION: int = 1


def fake_config() -> MemeticConfig:
    """Configuration complète avec les faux objets, sans MiniZinc. Une configuration neuve par exécution."""
    instance = synthetic_instance()
    encoding = BlockEncoding()
    return MemeticConfig(
        encoding=encoding,
        initializer=RandomBlockInitializer(instance, encoding),
        parent_selector=TournamentSelector(),
        crossover=FakeCrossover(),
        mutable_selector=UniformMutableSelector(),
        mutation=FakeMutation(),
        local_solver=FakeLocalSolver(),
        evaluator=CostEvaluator(instance),
        survivor_selector=FakeSurvivorSelector(),
        convergence=FakeConvergenceCriterion(),
        restart=FakeRestartPolicy(),
        termination=GenerationLimit(GENERATIONS),
        population_size=POPULATION_SIZE,
        crossover_count=CROSSOVER_COUNT,
        mutation_count=MUTATION_COUNT,
        master_seed=MASTER_SEED,
        dispatcher=mock.MagicMock(ObservationHub)
    )

def real_operators_config(master_seed: int = MASTER_SEED, with_collector: bool = False) -> MemeticConfig:
    """Vrais opérateurs de 7b et vrai initialiseur, sur 3 employés ; seul le ``LocalSolver`` est factice."""
    instance = synthetic_instance(EMPLOYEE_COUNT)
    encoding = BlockEncoding()
    return MemeticConfig(
        encoding=encoding,
        initializer=RandomBlockInitializer(instance, encoding),
        parent_selector=TournamentSelector(),
        crossover=UniformGeneCrossover(),
        mutable_selector=UniformMutableSelector(),
        mutation=ShiftStartMutation(instance),
        local_solver=FakeLocalSolver(),
        evaluator=CostEvaluator(instance),
        survivor_selector=FakeSurvivorSelector(),
        convergence=FakeConvergenceCriterion(),
        restart=FakeRestartPolicy(),
        termination=GenerationLimit(REAL_RUN_GENERATIONS),
        population_size=REAL_RUN_POPULATION,
        crossover_count=CROSSOVER_COUNT,
        mutation_count=MUTATION_COUNT,
        master_seed=master_seed,
        dispatcher=ObservationHub((RecordingCollector(),)) if with_collector else ObservationHub(),
    )


def observed_run(config: MemeticConfig) -> tuple[MemeticResult, list]:
    """Exécute ``config`` avec un ``RecordingCollector`` et rend le résultat et les événements reçus."""
    dispatcher = mock.Mock()
    result = Memetic(dataclasses.replace(config, dispatcher=dispatcher)).run()
    return result, [x.args[0] for x in dispatcher.emit.call_args_list]


def history(events: list) -> list[list]:
    """Génomes de la population à chaque ``GenerationEnded`` : l'historique d'une exécution."""
    return [[individual.genome for individual in event.population]
            for event in events if isinstance(event, GenerationEnded)]


class OtherEncoding(Encoding[str]):
    """Encodage factice, incompatible avec les opérateurs de ``BlockEncoding``."""

    def encode(self, horaire: Horaire) -> str:
        raise NotImplementedError

    def decode(self, genome: str) -> Horaire:
        raise NotImplementedError


class IncompatibleCrossover(FakeCrossover):
    @classmethod
    def encoding_type(cls) -> type[Encoding]:
        return OtherEncoding


class IncompatibleMutation(FakeMutation):
    @classmethod
    def encoding_type(cls) -> type[Encoding]:
        return OtherEncoding


# ---------------------------------------------------------------------------------------------------------------------
# Contrat du scaffold
# ---------------------------------------------------------------------------------------------------------------------

class TestScaffoldContract(unittest.TestCase):

    def test_givenInterface_whenInstantiated_thenRaisesTypeError(self) -> None:
        with self.assertRaises(TypeError):
            TerminationCriterion()  # type: ignore[abstract]

    def test_givenGenerationLimit_whenConstructed_thenKeepsItsLimit(self) -> None:
        self.assertEqual(GenerationLimit(GENERATIONS).maximum_generations, GENERATIONS)

    def test_givenInvalidGenerations_whenGenerationLimit_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidTerminationParameterError) as context:
            GenerationLimit(INVALID_GENERATIONS)
        self.assertIn(str(INVALID_GENERATIONS), str(context.exception))

    def test_givenFakeObjects_whenBuildingConfig_thenDefaultsAreSequentialAndNoObservation(self) -> None:
        config = fake_config()
        self.assertIsInstance(config.executor, SequentialExecutor)
        self.assertIsInstance(config.dispatcher, ObservationHub)

    def test_givenConfig_whenBuildingEngine_thenEngineKeepsIt(self) -> None:
        config = fake_config()
        self.assertIs(Memetic(config).config, config)

    def test_givenSeedStreams_whenListed_thenAllDistinct(self) -> None:
        streams = [stream.value for stream in SeedStreams]
        self.assertEqual(len(streams), len(set(streams)))

    def test_givenMemeticErrors_whenCheckingHierarchy_thenConfigErrorIsAMemeticError(self) -> None:
        self.assertTrue(issubclass(InvalidMemeticConfigError, MemeticError))

# ---------------------------------------------------------------------------------------------------------------------
# Graines dérivées (D7)
# ---------------------------------------------------------------------------------------------------------------------

class TestDeriveTaskSeeds(unittest.TestCase):

    @staticmethod
    def _first_seeds(seeds: Iterator[int], count: int) -> list[int]:
        return [next(seeds) for _ in range(count)]

    def test_givenSameArguments_whenDerive_thenSameSeeds(self) -> None:
        first = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER)
        second = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER)
        self.assertEqual(self._first_seeds(first, SEED_BATCH), self._first_seeds(second, SEED_BATCH))

    def test_givenTaskCount_whenDerive_thenOneIntegerSeedPerTask(self) -> None:
        seeds = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER)
        for seed in self._first_seeds(seeds, SEED_BATCH):
            self.assertIsInstance(seed, int)

    def test_givenOneBatch_whenDerive_thenSeedsWithinTheBatchAreDistinct(self) -> None:
        seeds = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER)
        self.assertEqual(len(set(self._first_seeds(seeds, SEED_BATCH))), SEED_BATCH)

    def test_givenOtherGenerationStreamOrMasterSeed_whenDerive_thenSeedsDiffer(self) -> None:
        reference = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER)
        variants = {
            "génération": derive_task_seeds(MASTER_SEED, SEED_GENERATION + 1, SeedStreams.CROSSOVER),
            "lot": derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.MUTATION),
            "graine maître": derive_task_seeds(OTHER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER),
        }
        reference_seeds = set(self._first_seeds(reference, SEED_BATCH))
        for name, variant in variants.items():
            with self.subTest(change=name):
                self.assertTrue(reference_seeds.isdisjoint(self._first_seeds(variant, SEED_BATCH)))

    def test_givenLargerBatch_whenDerive_thenSeedsOfTheFirstTasksAreUnchanged(self) -> None:
        short = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER)
        long = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER)
        long_seeds = self._first_seeds(long, SEED_BATCH)
        self.assertEqual(self._first_seeds(short, SEED_PREFIX), long_seeds[:SEED_PREFIX])


# ---------------------------------------------------------------------------------------------------------------------
# Critère d'arrêt
# ---------------------------------------------------------------------------------------------------------------------

class TestGenerationLimit(unittest.TestCase):

    def test_givenLimit_whenIsDone_thenFalseBeforeAndTrueFromTheLimit(self) -> None:
        criterion = GenerationLimit(GENERATIONS)
        verdicts = [criterion.is_done(generation, ()) for generation in range(GENERATIONS + 2)]
        self.assertEqual(verdicts, [False] * GENERATIONS + [True, True])


# ---------------------------------------------------------------------------------------------------------------------
# Validation de la configuration
# ---------------------------------------------------------------------------------------------------------------------

class TestMemeticConfigValidate(unittest.TestCase):

    def test_givenValidConfig_whenValidate_thenNoException(self) -> None:
        fake_config().validate()

    def test_givenOutOfDomainScalar_whenValidate_thenRaisesWithValueInMessage(self) -> None:
        cases = {"population_size": 0, "crossover_count": -1, "mutation_count": -2}
        for field_name, value in cases.items():
            with self.subTest(field=field_name):
                config = dataclasses.replace(fake_config(), **{field_name: value})
                with self.assertRaises(InvalidMemeticConfigError) as context:
                    config.validate()
                self.assertIn(str(value), str(context.exception))

    def test_givenNoVariationAtAll_whenValidate_thenRaisesInvalidMemeticConfigError(self) -> None:
        config = dataclasses.replace(fake_config(), crossover_count=0, mutation_count=0)
        with self.assertRaises(InvalidMemeticConfigError):
            config.validate()

    def test_givenOnlyCrossoverOrOnlyMutation_whenValidate_thenNoException(self) -> None:
        dataclasses.replace(fake_config(), crossover_count=0).validate()
        dataclasses.replace(fake_config(), mutation_count=0).validate()

    def test_givenIncompatibleOperator_whenValidate_thenRaisesIncompatibleOperatorError(self) -> None:
        for field_name, operator in (("crossover", IncompatibleCrossover()), ("mutation", IncompatibleMutation())):
            with self.subTest(field=field_name):
                config = dataclasses.replace(fake_config(), **{field_name: operator})
                with self.assertRaises(IncompatibleOperatorError):
                    config.validate()

    def test_givenInvalidConfig_whenRun_thenRaisesBeforeAnyEvent(self) -> None:
        collector = RecordingCollector()
        dispatcher = mock.Mock()
        config = dataclasses.replace(fake_config(), population_size=0, dispatcher=dispatcher)
        with self.assertRaises(InvalidMemeticConfigError):
            Memetic(config).run()
        dispatcher.assert_not_called()


# ---------------------------------------------------------------------------------------------------------------------
# Boucle, avec les faux objets
# ---------------------------------------------------------------------------------------------------------------------

class TestMemeticRunWithFakes(unittest.TestCase):

    def test_givenGenerationLimit_whenRun_thenExactlyThatManyGenerationsAndPopulationSize(self) -> None:
        result, events = observed_run(fake_config())
        self.assertEqual(result.generations, GENERATIONS)
        self.assertEqual(len(result.population), POPULATION_SIZE)
        generation_ends = [event for event in events if isinstance(event, GenerationEnded)]
        self.assertEqual([event.generation for event in generation_ends], list(range(GENERATIONS + 1)))
        for event in generation_ends:
            self.assertEqual(len(event.population), POPULATION_SIZE)

    def test_givenNrAndNm_whenRun_thenOperatorsAndLocalSolverAreCalledTheExpectedNumberOfTimes(self) -> None:
        config = fake_config()
        Memetic(config).run()
        self.assertEqual(len(config.crossover.received), CROSSOVER_COUNT * GENERATIONS)
        self.assertEqual(len(config.mutation.received), MUTATION_COUNT * GENERATIONS)
        new_per_generation = CROSSOVER_COUNT * CHILDREN_PER_CROSSOVER + MUTATION_COUNT
        self.assertEqual(len(config.local_solver.received), new_per_generation * GENERATIONS)

    def test_givenRun_whenObserved_thenRunStartedFirstAndRunEndedLastWithTheBest(self) -> None:
        result, events = observed_run(fake_config())
        self.assertIsInstance(events[0], RunStarted)
        self.assertEqual(events[0].master_seed, MASTER_SEED)
        self.assertEqual(events[0].population_size, POPULATION_SIZE)
        self.assertIsInstance(events[-1], RunEnded)
        self.assertEqual(events[-1].generations, GENERATIONS)
        self.assertEqual(events[-1].best.cost.total, result.best.cost.total)
        self.assertEqual(result.best.cost.total, min(individual.cost.total for individual in result.population))

    def test_givenRun_whenObserved_thenIndividualCreatedAndLocalSearchDoneCountsAndOrigins(self) -> None:
        _, events = observed_run(fake_config())
        created = [event for event in events if isinstance(event, IndividualCreated)]
        searches = [event for event in events if isinstance(event, LocalSearchDone)]
        new_per_generation = CROSSOVER_COUNT * CHILDREN_PER_CROSSOVER + MUTATION_COUNT
        self.assertEqual(len(created), POPULATION_SIZE + new_per_generation * GENERATIONS)
        self.assertEqual(len(searches), new_per_generation * GENERATIONS)
        initial = [event for event in created if event.generation == 0]
        self.assertEqual(len(initial), POPULATION_SIZE)
        for event in initial:
            self.assertEqual(event.origin, Origins.INITIALIZATION.value)
            self.assertIsNone(event.operator)
            self.assertTrue(event.individual.is_evaluated())
        origins = Counter((Origins(event.origin), event.operator) for event in searches)
        self.assertEqual(origins, Counter({
            (Origins.CROSSOVER, FakeCrossover.__name__): CROSSOVER_COUNT * CHILDREN_PER_CROSSOVER * GENERATIONS,
            (Origins.MUTATION, FakeMutation.__name__): MUTATION_COUNT * GENERATIONS,
        }))

    def test_givenRun_whenObserved_thenEventsOfAGenerationComeBeforeItsGenerationEnded(self) -> None:
        _, events = observed_run(fake_config())
        current_generation = 0
        for event in events:
            if isinstance(event, (IndividualCreated, LocalSearchDone)):
                self.assertEqual(event.generation, current_generation)
            if isinstance(event, GenerationEnded):
                self.assertEqual(event.generation, current_generation)
                current_generation += 1

    def test_givenLocalSearchDone_whenObserved_thenCostsBeforeAndAfterAreEvaluations(self) -> None:
        config = fake_config()
        _, events = observed_run(config)
        for event in [e for e in events if isinstance(e, LocalSearchDone)]:
            self.assertEqual(event.cost_after, config.evaluator.evaluate(event.result.horaire))
            self.assertIsNotNone(event.cost_before)

    def test_givenConvergence_whenRun_thenRestartThenResetAndEventsFollowGenerationEnded(self) -> None:
        convergence = FakeConvergenceCriterion(frozenset([CONVERGENCE_CALL]))
        restart = FakeRestartPolicy()
        config = dataclasses.replace(fake_config(), convergence=convergence, restart=restart)
        result, events = observed_run(config)
        self.assertEqual(result.restarts, 1)
        self.assertEqual(len(restart.received), 1)
        self.assertEqual(convergence.reset_count, 1)
        self.assertEqual(convergence.calls, GENERATIONS, "le critère est consulté une fois par génération g ≥ 1")
        names = [type(event) for event in events]
        converged_index = names.index(Converged)
        self.assertIsInstance(events[converged_index - 1], GenerationEnded)
        self.assertEqual(events[converged_index - 1].generation, CONVERGENCE_CALL)
        self.assertEqual(events[converged_index].generation, CONVERGENCE_CALL)
        self.assertIsInstance(events[converged_index + 1], Restarted)
        self.assertEqual(events[converged_index + 1].generation, CONVERGENCE_CALL)

    def test_givenNoConvergence_whenRun_thenNoRestart(self) -> None:
        config = fake_config()
        result, events = observed_run(config)
        self.assertEqual(result.restarts, 0)
        self.assertEqual(config.restart.received, [])
        self.assertFalse(any(isinstance(event, (Converged, Restarted)) for event in events))

    def test_givenOnlyMutation_whenRun_thenNoCrossover(self) -> None:
        config = dataclasses.replace(fake_config(), crossover_count=0)
        result = Memetic(config).run()
        self.assertEqual(config.crossover.received, [])
        self.assertEqual(len(config.mutation.received), MUTATION_COUNT * GENERATIONS)
        self.assertEqual(len(result.population), POPULATION_SIZE)

    def test_givenOnlyCrossover_whenRun_thenNoMutation(self) -> None:
        config = dataclasses.replace(fake_config(), mutation_count=0)
        Memetic(config).run()
        self.assertEqual(config.mutation.received, [])
        self.assertEqual(len(config.crossover.received), CROSSOVER_COUNT * GENERATIONS)


# ---------------------------------------------------------------------------------------------------------------------
# Boucle, avec les vrais opérateurs (seul le LocalSolver est factice)
# ---------------------------------------------------------------------------------------------------------------------

class TestMemeticRunWithRealOperators(unittest.TestCase):

    def test_givenRealOperators_whenRun_thenBestCostNeverIncreases(self) -> None:
        _, events = observed_run(real_operators_config())
        bests = [min(i.cost.total for i in event.population) for event in events if isinstance(event, GenerationEnded)]
        self.assertEqual(len(bests), REAL_RUN_GENERATIONS + 1)
        for previous, current in zip(bests, bests[1:]):
            self.assertLessEqual(current, previous)

    def test_givenSameSeed_whenRunTwice_thenSameHistoryAndResult(self) -> None:
        first_result, first_events = observed_run(real_operators_config())
        second_result, second_events = observed_run(real_operators_config())
        self.assertEqual(history(first_events), history(second_events))
        self.assertEqual(first_result.best.genome, second_result.best.genome)

    def test_givenOtherSeed_whenRun_thenHistoryDiffers(self) -> None:
        _, first_events = observed_run(real_operators_config(MASTER_SEED))
        _, other_events = observed_run(real_operators_config(OTHER_SEED))
        self.assertNotEqual(history(first_events), history(other_events))

    def test_givenCollectorOrNot_whenRun_thenSameResult(self) -> None:
        without = Memetic(real_operators_config(with_collector=False)).run()
        with_collector = Memetic(real_operators_config(with_collector=True)).run()
        self.assertEqual([i.genome for i in without.population], [i.genome for i in with_collector.population])
        self.assertEqual(without.best.genome, with_collector.best.genome)

    def test_givenGlobalRandomState_whenRun_thenItIsNotUsed(self) -> None:
        random.seed(MASTER_SEED)
        state_before = random.getstate()
        Memetic(real_operators_config()).run()
        self.assertEqual(random.getstate(), state_before, "chaque tâche a son propre random.Random (D7)")


# ---------------------------------------------------------------------------------------------------------------------
# Lots NR et NM (D7) : nombre d'appels, parents tirés dans P, indépendance des tâches
# ---------------------------------------------------------------------------------------------------------------------

class WorstFirstSurvivorSelector[G](SurvivorSelector[G]):
    """``SelectPop`` factice qui garde les ``size`` meilleurs, mais rangés du pire au meilleur."""

    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        ranked = sorted(population, key=lambda individual: individual.cost.total)[:size]
        return tuple(reversed(ranked))


class ReversedOrderExecutor(Executor):
    """Exécuteur factice qui exécute les tâches dans l'ordre inverse, mais rend les résultats dans l'ordre du lot."""

    def map(self, task, items):
        batch = list(items)
        results = [task(item) for item in reversed(batch)]
        return list(reversed(results))


class TestMemeticBatches(unittest.TestCase):

    def test_givenLargeNr_whenRun_thenEachCrossoverReceivesParentCountParents(self) -> None:
        config = dataclasses.replace(fake_config(), crossover_count=LARGE_CROSSOVER_COUNT)
        Memetic(config).run()
        self.assertEqual(len(config.crossover.received), LARGE_CROSSOVER_COUNT * GENERATIONS)
        for parents in config.crossover.received:
            self.assertEqual(len(parents), FakeCrossover.PARENT_COUNT)

    def test_givenLargeNrAndRealCrossover_whenRun_thenNoWrongParentCount(self) -> None:
        config = dataclasses.replace(real_operators_config(), crossover_count=LARGE_CROSSOVER_COUNT)
        result = Memetic(config).run()
        self.assertEqual(result.generations, REAL_RUN_GENERATIONS)

    def test_givenLargeNm_whenRun_thenExactlyNmMutationsPerGeneration(self) -> None:
        config = dataclasses.replace(fake_config(), mutation_count=LARGE_MUTATION_COUNT)
        Memetic(config).run()
        self.assertEqual(len(config.mutation.received), LARGE_MUTATION_COUNT * GENERATIONS)
        new_per_generation = CROSSOVER_COUNT * CHILDREN_PER_CROSSOVER + LARGE_MUTATION_COUNT
        self.assertEqual(len(config.local_solver.received), new_per_generation * GENERATIONS)

    def test_givenCrossoverBatch_whenRun_thenParentsComeFromThePopulationBeforeTheBatch(self) -> None:
        config = dataclasses.replace(
            fake_config(), crossover_count=LARGE_CROSSOVER_COUNT, termination=GenerationLimit(ONE_GENERATION)
        )
        _, events = observed_run(config)
        initial_genomes = history(events)[0]
        for parents in config.crossover.received:
            for parent in parents:
                self.assertIn(parent, initial_genomes)

    def test_givenSurvivorsNotSortedByCost_whenRun_thenBestIsTheCheapest(self) -> None:
        config = dataclasses.replace(fake_config(), survivor_selector=WorstFirstSurvivorSelector())
        result, events = observed_run(config)
        cheapest = min(individual.cost.total for individual in result.population)
        self.assertEqual(result.best.cost.total, cheapest)
        self.assertEqual(events[-1].best.cost.total, cheapest)

    def test_givenTasksRunInAnotherOrder_whenRun_thenSameHistory(self) -> None:
        _, sequential_events = observed_run(real_operators_config())
        reordered = dataclasses.replace(real_operators_config(), executor=ReversedOrderExecutor())
        _, reordered_events = observed_run(reordered)
        self.assertEqual(history(sequential_events), history(reordered_events))

    def test_givenRun_whenFinished_thenTheHubIsClosed(self) -> None:
        dispatcher = mock.Mock()
        Memetic(dataclasses.replace(fake_config(), dispatcher=dispatcher)).run()
        dispatcher.close.assert_called_once()

    def test_givenTwoConfigs_whenBuiltWithDefaultHub_thenEachHasItsOwnHub(self) -> None:
        instance = synthetic_instance()
        encoding = BlockEncoding()
        arguments = dict(
            encoding=encoding, initializer=RandomBlockInitializer(instance, encoding),
            parent_selector=TournamentSelector(), crossover=FakeCrossover(), mutable_selector=UniformMutableSelector(),
            mutation=FakeMutation(), local_solver=FakeLocalSolver(), evaluator=CostEvaluator(instance),
            survivor_selector=FakeSurvivorSelector(), convergence=FakeConvergenceCriterion(),
            restart=FakeRestartPolicy(), termination=GenerationLimit(GENERATIONS), population_size=POPULATION_SIZE,
            crossover_count=CROSSOVER_COUNT, mutation_count=MUTATION_COUNT, master_seed=MASTER_SEED,
        )
        self.assertIsNot(MemeticConfig(**arguments).dispatcher, MemeticConfig(**arguments).dispatcher)


# ---------------------------------------------------------------------------------------------------------------------
# Graines du moteur (D7) : chaque lot a son stream, et une tâche ne dépend que de sa position dans son lot
# ---------------------------------------------------------------------------------------------------------------------

RngState = tuple


def expected_state(generation: int, stream: SeedStreams, position: int = 0) -> RngState:
    """État du ``random.Random`` que doit recevoir la tâche ``position`` du lot ``stream`` de ``generation``."""
    seeds = derive_task_seeds(MASTER_SEED, generation, stream)
    seed = [next(seeds) for _ in range(position + 1)][position]
    return random.Random(seed).getstate()


class RngRecordingMutation(FakeMutation):
    """``FakeMutation`` qui note l'état du générateur reçu, sans le consommer."""

    def __init__(self) -> None:
        super().__init__()
        self.states: list[RngState] = []

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        self.states.append(rng.getstate())
        return super().mutate(genome, rng)


class RngRecordingLocalSolver(FakeLocalSolver):
    """``FakeLocalSolver`` qui note l'état du générateur reçu, sans le consommer."""

    def __init__(self) -> None:
        super().__init__()
        self.states: list[RngState] = []

    def improve(self, horaire: Horaire, rng: random.Random) -> LocalSearchResult:
        self.states.append(rng.getstate())
        return super().improve(horaire, rng)


class RngRecordingInitializer[G](PopulationInitializer[G]):
    """Initialiseur qui note l'état du générateur reçu, puis délègue à ``delegate``."""

    def __init__(self, delegate: PopulationInitializer[G]) -> None:
        self.delegate = delegate
        self.states: list[RngState] = []

    def initialize(self, size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        self.states.append(rng.getstate())
        return self.delegate.initialize(size, rng)


class RngRecordingRestartPolicy(FakeRestartPolicy):
    """``FakeRestartPolicy`` qui note l'état du générateur reçu, sans le consommer."""

    def __init__(self) -> None:
        super().__init__()
        self.states: list[RngState] = []

    def restart(self, population, rng: random.Random):
        self.states.append(rng.getstate())
        return super().restart(population, rng)


class TestEngineSeeds(unittest.TestCase):

    def mutation_task_states(self, crossover_count: int) -> tuple[list[RngState], list[RngState]]:
        """États reçus par les tâches de mutation (par ``mutate`` et par le ``LocalSolver``), pour un NR donné."""
        mutation = RngRecordingMutation()
        local_solver = RngRecordingLocalSolver()
        config = dataclasses.replace(
            fake_config(),
            crossover_count=crossover_count,
            mutation_count=LARGE_MUTATION_COUNT,
            mutation=mutation,
            local_solver=local_solver,
        )
        Memetic(config).run()
        crossover_children = crossover_count * CHILDREN_PER_CROSSOVER
        calls_per_generation = crossover_children + LARGE_MUTATION_COUNT
        mutation_local_search_states = [
            state
            for generation_start in range(0, calls_per_generation * GENERATIONS, calls_per_generation)
            for state in local_solver.states[generation_start + crossover_children:generation_start + calls_per_generation]
        ]
        return mutation.states, mutation_local_search_states

    def test_givenOtherNr_whenRun_thenMutationTasksReceiveTheSameGenerators(self) -> None:
        reference_mutate, reference_search = self.mutation_task_states(CROSSOVER_COUNT)
        other_mutate, other_search = self.mutation_task_states(LARGE_CROSSOVER_COUNT)
        self.assertEqual(len(reference_mutate), LARGE_MUTATION_COUNT * GENERATIONS)
        self.assertEqual(reference_mutate, other_mutate, "le générateur d'une mutation ne dépend pas de NR")
        self.assertEqual(reference_search, other_search, "la recherche locale d'une mutation ne dépend pas de NR")

    def test_givenMutationTask_whenRun_thenOperatorAndLocalSolverShareTheTaskGenerator(self) -> None:
        mutate_states, search_states = self.mutation_task_states(CROSSOVER_COUNT)
        expected = [
            expected_state(generation, SeedStreams.MUTATION, position)
            for generation in range(ONE_GENERATION, GENERATIONS + 1)
            for position in range(LARGE_MUTATION_COUNT)
        ]
        self.assertEqual(mutate_states, expected)
        self.assertEqual(search_states, expected, "pas le générateur de la sélection des individus à muter")

    def test_givenRun_whenInitializing_thenInitializerReceivesTheInitializationGenerator(self) -> None:
        initializer = RngRecordingInitializer(fake_config().initializer)
        Memetic(dataclasses.replace(fake_config(), initializer=initializer)).run()
        self.assertEqual(initializer.states, [expected_state(0, SeedStreams.INITIALIZATION)])

    def test_givenConvergence_whenRestarting_thenRestartReceivesTheRestartGenerator(self) -> None:
        restart = RngRecordingRestartPolicy()
        convergence = FakeConvergenceCriterion(frozenset([CONVERGENCE_CALL]))
        Memetic(dataclasses.replace(fake_config(), restart=restart, convergence=convergence)).run()
        self.assertEqual(restart.states, [expected_state(CONVERGENCE_CALL, SeedStreams.RESTART)])


# ---------------------------------------------------------------------------------------------------------------------
# Recherches locales hors du moteur : initialisation et restart (D8, D10)
# ---------------------------------------------------------------------------------------------------------------------

ELITE_COUNT: int = 1


def config_with_outside_searches(converge_at: frozenset[int] = frozenset()) -> MemeticConfig:
    """``fake_config`` dont l'initialiseur passe par un ``FakeLocalSolver`` et dont le restart est un vrai
    ``EliteRestart`` qui réutilise cet initialiseur."""
    instance = synthetic_instance()
    encoding = BlockEncoding()
    evaluator = CostEvaluator(instance)
    initializer = RandomBlockInitializer(instance, encoding, local_solver=FakeLocalSolver())
    return dataclasses.replace(
        fake_config(),
        initializer=initializer,
        evaluator=evaluator,
        restart=EliteRestart(initializer, evaluator, ELITE_COUNT),
        convergence=FakeConvergenceCriterion(converge_at),
    )


class TestOutsideSearches(unittest.TestCase):

    def test_givenInitializerWithLocalSolver_whenRun_thenGenerationZeroPublishesItsSearches(self) -> None:
        _, events = observed_run(config_with_outside_searches())
        generation_zero = events[1:events.index(next(e for e in events if isinstance(e, GenerationEnded)))]
        searches = [event for event in generation_zero if isinstance(event, LocalSearchDone)]
        created = [event for event in generation_zero if isinstance(event, IndividualCreated)]
        self.assertEqual(len(searches), POPULATION_SIZE)
        self.assertEqual(len(created), POPULATION_SIZE)
        self.assertEqual(generation_zero, searches + created, "les recherches d'abord, puis les individus")
        for event in searches:
            self.assertEqual(event.origin, Origins.INITIALIZATION.value)
            self.assertIsNone(event.operator)
            self.assertEqual(event.generation, 0)
            self.assertEqual(event.cost_after, CostEvaluator(synthetic_instance()).evaluate(event.result.horaire))

    def test_givenRestart_whenRun_thenNewcomersAndTheirSearchesArePublishedBetweenConvergedAndRestarted(self) -> None:
        result, events = observed_run(config_with_outside_searches(frozenset([CONVERGENCE_CALL])))
        self.assertEqual(result.restarts, 1)
        converged = next(index for index, event in enumerate(events) if isinstance(event, Converged))
        restarted = next(index for index, event in enumerate(events) if isinstance(event, Restarted))
        between = events[converged + 1:restarted]
        newcomer_count = POPULATION_SIZE - ELITE_COUNT
        searches = [event for event in between if isinstance(event, LocalSearchDone)]
        created = [event for event in between if isinstance(event, IndividualCreated)]
        self.assertEqual(between, searches + created)
        self.assertEqual(len(searches), newcomer_count)
        self.assertEqual(len(created), newcomer_count)
        for event in searches + created:
            self.assertEqual(event.origin, Origins.RESTART.value)
            self.assertIsNone(event.operator)
            self.assertEqual(event.generation, CONVERGENCE_CALL)
        restarted_population = events[restarted].population
        self.assertEqual(len(restarted_population), POPULATION_SIZE)
        self.assertEqual([event.individual for event in created], list(restarted_population[ELITE_COUNT:]))
        for event in created:
            self.assertTrue(event.individual.is_evaluated())


if __name__ == "__main__":
    unittest.main()
