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
import unittest
from collections import Counter

from src.ga.chromosome import BlockEncoding, Encoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.operators import Crossover, Mutation, ShiftStartMutation, UniformGeneCrossover
from src.ga.population import ConvergenceCriterion, RestartPolicy, SurvivorSelector
from src.ga.registry import IncompatibleOperatorError
from src.ga.selection import MutableSelector, ParentSelector, TournamentSelector, UniformMutableSelector
from src.memetic import engine
from src.memetic.config import InvalidMemeticConfigError, MemeticConfig, MemeticError
from src.memetic.engine import Memetic, MemeticResult, MemeticCrossoverArgs, MemeticMutationArgs
from src.memetic.executor import SequentialExecutor
from src.memetic.local_search import LocalSearchResult, LocalSolver
from src.memetic.seeds import SeedStreams, derive_task_seeds
from src.memetic.solver import SolveOutcome, SolverStatistics
from src.memetic.termination import (
    GenerationLimit,
    InvalidTerminationParameterError,
    TerminationCriterion,
)
from src.model.evaluation import CostEvaluator
from src.model.horaire import Horaire
from src.observability.hub import ObservationHub
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
from unittest import mock

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

def fake_config_with_mock(
        dispatcher: ObservationHub = mock.Mock(),
        local_solver: LocalSolver = mock.Mock(),
        parent_selector: ParentSelector = mock.MagicMock(TournamentSelector),
        crossover: Crossover = mock.MagicMock(FakeCrossover),
        mutable_selector: MutableSelector = mock.MagicMock(MutableSelector),
        mutation: Mutation = mock.MagicMock(FakeMutation),
        evaluator: CostEvaluator = mock.MagicMock(CostEvaluator),
        survivor_selector: SurvivorSelector = mock.MagicMock(FakeSurvivorSelector),
        convergence: ConvergenceCriterion = mock.MagicMock(FakeConvergenceCriterion),
        restart: RestartPolicy = mock.MagicMock(FakeRestartPolicy),
        termination: TerminationCriterion = mock.MagicMock(GenerationLimit),
) -> MemeticConfig:
    """Configuration complète avec les faux objets, sans MiniZinc."""
    instance = synthetic_instance()
    encoding = BlockEncoding()
    return MemeticConfig(
        encoding=encoding,
        initializer=RandomBlockInitializer(instance, encoding),
        parent_selector=parent_selector,
        crossover=crossover,
        mutable_selector=mutable_selector,
        mutation=mutation,
        local_solver=local_solver,
        evaluator=evaluator,
        survivor_selector=survivor_selector,
        convergence=convergence,
        restart=restart,
        termination=termination,
        population_size=POPULATION_SIZE,
        crossover_count=CROSSOVER_COUNT,
        mutation_count=MUTATION_COUNT,
        master_seed=MASTER_SEED,
        dispatcher=dispatcher
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
    )


def observed_run(config: MemeticConfig) -> tuple[MemeticResult, list]:
    """Exécute ``config`` avec un ``RecordingCollector`` et rend le résultat et les événements reçus."""
    collector = RecordingCollector()
    result = Memetic(dataclasses.replace(config, collectors=(collector,))).run()
    return result, collector.events


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
        self.assertEqual(GenerationLimit(GENERATIONS).generations, GENERATIONS)

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
        streams = [value for name, value in vars(SeedStreams).items() if name.isupper()]
        self.assertEqual(len(streams), len(set(streams)))

    def test_givenMemeticErrors_whenCheckingHierarchy_thenConfigErrorIsAMemeticError(self) -> None:
        self.assertTrue(issubclass(InvalidMemeticConfigError, MemeticError))

class TestEngine(unittest.TestCase):
    def test_engine_seed_collection_generate_seeds(self):
        engine = Memetic(fake_config())
        seeds = engine._generate_seed()

        self.assertIsNotNone(next(seeds.INITIALIZATION))
        self.assertIsNotNone(next(seeds.PARENT_SELECTION))
        self.assertIsNotNone(next(seeds.CROSSOVER))
        self.assertIsNotNone(next(seeds.MUTABLE_SELECTION))
        self.assertIsNotNone(next(seeds.MUTATION))
        self.assertIsNotNone(next(seeds.LOCAL_SEARCH))
        self.assertIsNotNone(next(seeds.SURVIVOR_SELECTION))
        self.assertIsNotNone(next(seeds.RESTART))

    def test_engine_each_seed_generated_increment_generation(self):
        engine = Memetic(fake_config())
        for _ in range(100):
            old_generation = engine.generation
            engine._generate_seed()
            self.assertEqual(engine.generation, old_generation + 1)


    def test_engine_seed_collection_generate_same_seeds_each_time(self):
        engine = Memetic(fake_config())

        seeds1 = engine._generate_seed()
        engine.generation = 0
        seeds2 = engine._generate_seed()

        self.assertEqual(next(seeds1.INITIALIZATION), next(seeds2.INITIALIZATION))
        self.assertEqual(next(seeds1.PARENT_SELECTION), next(seeds2.PARENT_SELECTION))
        self.assertEqual(next(seeds1.CROSSOVER), next(seeds2.CROSSOVER))
        self.assertEqual(next(seeds1.MUTABLE_SELECTION), next(seeds2.MUTABLE_SELECTION))
        self.assertEqual(next(seeds1.MUTATION), next(seeds2.MUTATION))
        self.assertEqual(next(seeds1.LOCAL_SEARCH), next(seeds2.LOCAL_SEARCH))
        self.assertEqual(next(seeds1.SURVIVOR_SELECTION), next(seeds2.SURVIVOR_SELECTION))
        self.assertEqual(next(seeds1.RESTART), next(seeds2.RESTART))

    def test_engine_seed_random_is_the_same(self):
        engine = Memetic(fake_config())
        rng1 = engine._generate_rng(engine._generate_seed().INITIALIZATION)
        engine.generation = 0
        rng2 = engine._generate_rng(engine._generate_seed().INITIALIZATION)
        for _ in range(100):
            self.assertEqual(rng1.random(), rng2.random())

    def test_engine_init_population_correct_size(self):
        engine = Memetic(fake_config())
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)
        engine._init_population(rng)
        self.assertEqual(len(engine.population), engine.config.population_size)

    def test_engine_init_population_caclulate_cost(self):
        engine = Memetic(fake_config())
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)
        engine._init_population(rng)
        for i in engine.population:
            self.assertTrue(i.is_evaluated())

    def test_engine_init_population_send_event(self):
        dispatcher = mock.Mock()
        engine = Memetic(fake_config_with_mock(dispatcher=dispatcher))
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)
        engine._init_population(rng)
        self.assertEqual(dispatcher.emit.call_count, engine.config.population_size + 1)

    def test_engine_crossover_send_to_local_solver(self):
        local_solver = mock.MagicMock(LocalSolver)
        default_config = fake_config()
        engine = Memetic(fake_config_with_mock(
            local_solver=local_solver,
            parent_selector=default_config.parent_selector,
            evaluator=default_config.evaluator,
            crossover=default_config.crossover
        ))
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)
        engine._init_population(rng)
        local_solver.improve.return_value = LocalSearchResult(engine.population[0].horaire, engine.population[0].horaire, SolveOutcome("no_solution"), frozenset([1]), SolverStatistics())
        engine._crossover_loop(MemeticCrossoverArgs(rng, rng, rng))
        self.assertEqual(local_solver.improve.call_count, engine.config.crossover_count)

    def test_engine_crossover_event_are_sent(self):
        local_solver = mock.MagicMock(LocalSolver)
        dispatcher = mock.Mock()
        default_config = fake_config()
        engine = Memetic(fake_config_with_mock(
            local_solver=local_solver,
            parent_selector=default_config.parent_selector,
            evaluator=default_config.evaluator,
            crossover=default_config.crossover,
            dispatcher=dispatcher,
        ))
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)

        engine._init_population(rng)
        local_solver.improve.return_value = LocalSearchResult(engine.population[0].horaire, engine.population[0].horaire, SolveOutcome("no_solution"), frozenset([1]), SolverStatistics())
        dispatcher.reset_mock()

        engine._crossover_loop(MemeticCrossoverArgs(rng, rng, rng))

        self.assertEqual(dispatcher.emit.call_count, 2 * engine.config.crossover_count)

    def test_engine_mutation_send_to_local_solver(self):
        local_solver = mock.MagicMock(LocalSolver)
        default_config = fake_config()
        engine = Memetic(fake_config_with_mock(
            local_solver=local_solver,
            mutable_selector=default_config.mutable_selector,
            mutation=default_config.mutation,
            evaluator=default_config.evaluator,
        ))
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)
        engine._init_population(rng)
        local_solver.improve.return_value = LocalSearchResult(engine.population[0].horaire, engine.population[0].horaire, SolveOutcome("no_solution"), frozenset([1]), SolverStatistics())
        engine._mutation_loop(MemeticMutationArgs(rng, rng, rng))

        self.assertEqual(local_solver.improve.call_count, engine.config.mutation_count)

    def test_engine_mutation_event_are_sent(self):
        local_solver = mock.MagicMock(LocalSolver)
        dispatcher = mock.Mock()
        default_config = fake_config()
        engine = Memetic(fake_config_with_mock(
            dispatcher=dispatcher,
            local_solver=local_solver,
            mutable_selector=default_config.mutable_selector,
            mutation=default_config.mutation,
            evaluator=default_config.evaluator,
        ))
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)

        engine._init_population(rng)
        local_solver.improve.return_value = LocalSearchResult(engine.population[0].horaire, engine.population[0].horaire, SolveOutcome("no_solution"), frozenset([1]), SolverStatistics())
        dispatcher.reset_mock()

        engine._mutation_loop(MemeticMutationArgs(rng, rng, rng))

        self.assertEqual(dispatcher.emit.call_count, 2 * engine.config.mutation_count)

    def test_engine_process_result(self):
        engine = Memetic(fake_config_with_mock())
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)
        engine._init_population(rng)

        _process = engine._process_result("")

        i = _process(LocalSearchResult(engine.population[0].horaire, engine.population[0].horaire, SolveOutcome("no_solution"), frozenset([1]), SolverStatistics()))

        self.assertTrue(i.is_evaluated())

    def test_engine_process_result_send_origin_with_operator(self):
        origin = "tomate"
        operator = "cerise"

        dispacther = mock.Mock()
        emit = mock.Mock()
        dispacther.emit = emit
        engine = Memetic(fake_config_with_mock(dispatcher=dispacther))
        collection = engine._generate_seed()
        rng = engine._generate_rng(collection.INITIALIZATION)
        engine._init_population(rng)
        emit.reset_mock()

        _process = engine._process_result(origin, operator)
        _process(LocalSearchResult(engine.population[0].horaire, engine.population[0].horaire, SolveOutcome("no_solution"), frozenset([1]), SolverStatistics()))

        for c in emit.call_args_list:
            event = c.args[0]
            self.assertIsNotNone(event.origin)
            self.assertEqual(event.origin, origin)

            self.assertIsNotNone(event.operator)
            self.assertEqual(event.operator, operator)

# ---------------------------------------------------------------------------------------------------------------------
# Graines dérivées (D7)
# ---------------------------------------------------------------------------------------------------------------------

class TestDeriveTaskSeeds(unittest.TestCase):

    def test_givenSameArguments_whenDerive_thenSameSeeds(self) -> None:
        first = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_BATCH)
        second = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_BATCH)
        self.assertEqual(first, second)

    def test_givenTaskCount_whenDerive_thenOneIntegerSeedPerTask(self) -> None:
        seeds = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_BATCH)
        self.assertIsInstance(seeds, tuple)
        self.assertEqual(len(seeds), SEED_BATCH)
        for seed in seeds:
            self.assertIsInstance(seed, int)

    def test_givenZeroTasks_whenDerive_thenEmptyTuple(self) -> None:
        self.assertEqual(derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, 0), ())

    def test_givenOneBatch_whenDerive_thenSeedsWithinTheBatchAreDistinct(self) -> None:
        seeds = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_BATCH)
        self.assertEqual(len(set(seeds)), SEED_BATCH)

    def test_givenOtherGenerationStreamOrMasterSeed_whenDerive_thenSeedsDiffer(self) -> None:
        reference = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_BATCH)
        variants = {
            "génération": derive_task_seeds(MASTER_SEED, SEED_GENERATION + 1, SeedStreams.CROSSOVER, SEED_BATCH),
            "lot": derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.MUTATION, SEED_BATCH),
            "graine maître": derive_task_seeds(OTHER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_BATCH),
        }
        for name, variant in variants.items():
            with self.subTest(change=name):
                self.assertTrue(set(variant).isdisjoint(reference))

    def test_givenLargerBatch_whenDerive_thenSeedsOfTheFirstTasksAreUnchanged(self) -> None:
        short = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_PREFIX)
        long = derive_task_seeds(MASTER_SEED, SEED_GENERATION, SeedStreams.CROSSOVER, SEED_BATCH)
        self.assertEqual(long[:SEED_PREFIX], short)


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
        config = dataclasses.replace(fake_config(), population_size=0, collectors=(collector,))
        with self.assertRaises(InvalidMemeticConfigError):
            Memetic(config).run()
        self.assertEqual(collector.events, [])


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
            self.assertEqual(event.origin, Origins.INITIALIZATION)
            self.assertIsNone(event.operator)
            self.assertTrue(event.individual.is_evaluated())
        origins = Counter((event.origin, event.operator) for event in searches)
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
        convergence = FakeConvergenceCriterion(frozenset({CONVERGENCE_CALL}))
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

    def test_engine_each_loop_increment_generation(self):
        is_done = mock.Mock()
        run = [False, False, True]
        is_done.side_effect = run
        terminated = mock.Mock()
        terminated.is_done = is_done
        default_config = fake_config()
        engine = Memetic(
            fake_config_with_mock(
                termination=terminated,

                local_solver=default_config.local_solver,
            )
         )
        engine.run()

        self.assertEqual(engine.generation, len(run))

if __name__ == "__main__":
    unittest.main()
