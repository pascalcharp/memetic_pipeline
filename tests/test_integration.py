"""Tests de la sous-étape 9-intégration : le moteur mémétique avec les vrais composants (Pascal).

Tests écrits par Claude (règle des tests par agent, CLAUDE.md), à faire passer en écrivant
``build_block_memetic_config`` (``src/memetic/assembly.py``). Validés le 2026-11-22 contre un assemblage de référence
jetable, qui n'est pas dans le dépôt.

Deux parties :
    - ``TestAssembly`` (sans MiniZinc) : la configuration contient les composants attendus, reçoit les paramètres de
      ``AssemblySettings`` et partage ce qui doit l'être ;
    - ``TestMemeticOnBench1`` (MiniZinc et CP-SAT, quelques secondes) : deux exécutions complètes sur bench_1, avec la
      même graine, l'une sans mesure et l'autre avec les quatre collecteurs de 8b, un ``RecordingCollector``, un
      ``MemorySink`` et un ``JsonlSink``. On vérifie : taille et nombre de générations, coût du meilleur qui ne
      remonte jamais, faisabilité structurelle de chaque individu, borne de la recherche locale, appels réels à
      CP-SAT, reproductibilité avec et sans collecteurs, ordre des événements et enregistrements des collecteurs.
"""

import json
import tempfile
import unittest
import warnings
from pathlib import Path

from minizinc.error import MiniZincWarning

from src.config import ProjectPaths
from src.ga.chromosome import BlockEncoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.operators import (
    ActivityMutation,
    RandomGenomeCrossover,
    RandomGenomeMutation,
    ShiftStartMutation,
    UniformGeneCrossover,
)
from src.ga.population import EliteRestart, PlusSurvivorSelector, StagnationCriterion
from src.ga.selection import TournamentSelector, UniformMutableSelector
from src.memetic.assembly import AssemblyDefaults, AssemblySettings, build_block_memetic_config
from src.memetic.catalog import StrategyChoice, StrategyChoices, StrategyNames
from src.memetic.config import MemeticConfig
from src.memetic.engine import Memetic, MemeticResult
from src.memetic.local_search import MiniZincLocalSolver, RandomEmployeesNeighborhood
from src.memetic.solver import CpSatAdapter, DeterministicTimeLimit, ModelVariants, SolverDefaults
from src.memetic.termination import GenerationLimit
from src.model.evaluation import CostEvaluator
from src.model.feasibility import FeasibilityChecker
from src.observability.collectors import (
    CostStatisticsCollector,
    DiversityCollector,
    FeasibilityRateCollector,
    RecordNames,
    SolverEffortCollector,
)
from src.observability.events import (
    Converged,
    Event,
    GenerationEnded,
    IndividualCreated,
    LocalSearchDone,
    Origins,
    Restarted,
    RunEnded,
    RecordSchema,
    RunStarted,
)
from src.observability.hub import ObservationHub
from src.observability.sinks import JsonlSink, MemorySink
from src.utils.io import ProblemInstance, load_instance
from tests.fixtures import RecordingCollector

BENCH_1: str = "bench_1.json"
EVENTS_FILE: str = "events.jsonl"

# Paramètres des tests sans MiniZinc : tous différents des valeurs par défaut, pour vérifier qu'ils sont transmis.
CUSTOM_SETTINGS = AssemblySettings(
    population_size=7,
    crossover_count=3,
    mutation_count=4,
    generations=9,
    master_seed=11,
    tournament_size=3,
    stagnation_generations=4,
    elite_count=2,
    neighborhood_size=2,
    deterministic_time_units=1.5,
    initial_local_search=True,
)

# Exécution réelle sur bench_1 : courte, et une stagnation d'une seule génération pour exercer le restart. Avec la
# graine 7, l'exécution atteint l'optimum de bench_1 (94, docs/PROBLEME.md) et fait un restart (mesuré le 2026-11-22,
# CP-SAT monothread sous limite déterministe : reproductible).
INTEGRATION_SETTINGS = AssemblySettings(
    population_size=6,
    crossover_count=2,
    mutation_count=2,
    generations=4,
    master_seed=7,
    stagnation_generations=1,
)
CHILDREN_PER_CROSSOVER: int = 2
MIN_EXPECTED_RESTARTS: int = 1


def bench_1() -> ProblemInstance:
    return load_instance(ProjectPaths.DATA_DIR / BENCH_1)


# ---------------------------------------------------------------------------------------------------------------------
# Assemblage, sans MiniZinc
# ---------------------------------------------------------------------------------------------------------------------

class TestAssembly(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = bench_1()
        self.config = build_block_memetic_config(self.instance, CUSTOM_SETTINGS)

    def test_givenSettings_whenBuilding_thenEngineParametersArePassed(self) -> None:
        self.assertIsInstance(self.config, MemeticConfig)
        self.assertEqual(self.config.population_size, CUSTOM_SETTINGS.population_size)
        self.assertEqual(self.config.crossover_count, CUSTOM_SETTINGS.crossover_count)
        self.assertEqual(self.config.mutation_count, CUSTOM_SETTINGS.mutation_count)
        self.assertEqual(self.config.master_seed, CUSTOM_SETTINGS.master_seed)

    def test_givenSettings_whenBuilding_thenConfigIsValid(self) -> None:
        self.config.validate()

    def test_givenSettings_whenBuilding_thenExpectedComponentTypes(self) -> None:
        expected = {
            "encoding": BlockEncoding,
            "initializer": RandomBlockInitializer,
            "parent_selector": TournamentSelector,
            "crossover": UniformGeneCrossover,
            "mutable_selector": UniformMutableSelector,
            "mutation": ShiftStartMutation,
            "local_solver": MiniZincLocalSolver,
            "evaluator": CostEvaluator,
            "survivor_selector": PlusSurvivorSelector,
            "convergence": StagnationCriterion,
            "restart": EliteRestart,
            "termination": GenerationLimit,
        }
        for field_name, expected_type in expected.items():
            with self.subTest(field=field_name):
                self.assertIsInstance(getattr(self.config, field_name), expected_type)

    def test_givenSettings_whenBuilding_thenComponentParametersArePassed(self) -> None:
        self.assertEqual(self.config.parent_selector.size, CUSTOM_SETTINGS.tournament_size)
        self.assertEqual(self.config.convergence.generations, CUSTOM_SETTINGS.stagnation_generations)
        self.assertEqual(self.config.restart.elite_count, CUSTOM_SETTINGS.elite_count)
        self.assertEqual(self.config.termination.maximum_generations, CUSTOM_SETTINGS.generations)

    def test_givenSettings_whenBuilding_thenLocalSolverUsesCpSatOnTheRelaxedModelUnderADeterministicLimit(self) -> None:
        local_solver = self.config.local_solver
        self.assertIsInstance(local_solver.adapter, CpSatAdapter)
        self.assertEqual(local_solver.adapter.model, ModelVariants.RELAXED)
        options = local_solver.adapter.options
        self.assertEqual(options.limit, DeterministicTimeLimit(CUSTOM_SETTINGS.deterministic_time_units))
        self.assertEqual(options.threads, SolverDefaults.THREADS)
        self.assertEqual(options.seed, SolverDefaults.SEED)
        self.assertIsInstance(local_solver.neighborhood, RandomEmployeesNeighborhood)
        self.assertEqual(local_solver.neighborhood.size, CUSTOM_SETTINGS.neighborhood_size)

    def test_givenSettings_whenBuilding_thenEvaluatorAndInitializerAreShared(self) -> None:
        self.assertIs(self.config.local_solver.evaluator, self.config.evaluator)
        self.assertIs(self.config.restart.evaluator, self.config.evaluator)
        self.assertIs(self.config.restart.initializer, self.config.initializer)

    def test_givenInitialLocalSearch_whenBuilding_thenInitializerUsesTheLocalSolverOrNot(self) -> None:
        self.assertIs(self.config.initializer.local_solver, self.config.local_solver)
        without = build_block_memetic_config(
            self.instance, AssemblySettings(initial_local_search=False)
        )
        self.assertIsNone(without.initializer.local_solver)

    def test_givenChosenMutation_whenBuilding_thenTheCatalogCreatesItAndTheConfigIsValid(self) -> None:
        strategies = StrategyChoices(mutation=StrategyChoice(StrategyNames.ACTIVITY))
        config = build_block_memetic_config(self.instance, CUSTOM_SETTINGS, strategies=strategies)
        self.assertIsInstance(config.mutation, ActivityMutation)
        self.assertIs(config.mutation.instance, self.instance)
        self.assertIsInstance(config.crossover, UniformGeneCrossover)
        config.validate()

    def test_givenDefaultStrategies_whenBuilding_thenSameOperatorsAsWithoutStrategies(self) -> None:
        config = build_block_memetic_config(self.instance, CUSTOM_SETTINGS, strategies=StrategyChoices())
        self.assertIsInstance(config.crossover, type(self.config.crossover))
        self.assertIsInstance(config.mutation, type(self.config.mutation))

    def test_givenSurvivorSelectorChoice_whenBuilding_thenTheCatalogCreatesItWithItsParameter(self) -> None:
        # Étape 10e : par défaut, la sélection des survivants de référence ; avec prefer_newest, l'enfant à coût égal.
        self.assertFalse(self.config.survivor_selector.prefer_newest)
        strategies = StrategyChoices(survivor_selector=StrategyChoice(StrategyNames.PLUS, {"prefer_newest": True}))
        config = build_block_memetic_config(self.instance, CUSTOM_SETTINGS, strategies=strategies)
        self.assertIsInstance(config.survivor_selector, PlusSurvivorSelector)
        self.assertTrue(config.survivor_selector.prefer_newest)

    def test_givenNoDispatcher_whenBuilding_thenEachConfigHasItsOwnHub(self) -> None:
        first = build_block_memetic_config(self.instance)
        second = build_block_memetic_config(self.instance)
        self.assertIsInstance(first.dispatcher, ObservationHub)
        self.assertIsNot(first.dispatcher, second.dispatcher)

    def test_givenDispatcher_whenBuilding_thenItIsUsed(self) -> None:
        hub = ObservationHub()
        self.assertIs(build_block_memetic_config(self.instance, dispatcher=hub).dispatcher, hub)

    def test_givenTwoBuilds_whenComparing_thenStatefulComponentsAreNew(self) -> None:
        other = build_block_memetic_config(self.instance, CUSTOM_SETTINGS)
        self.assertIsNot(other.convergence, self.config.convergence)
        self.assertIsNot(other.local_solver, self.config.local_solver)

    def test_givenNoSettings_whenBuilding_thenDefaultsAreUsed(self) -> None:
        config = build_block_memetic_config(self.instance)
        self.assertEqual(config.population_size, AssemblyDefaults.POPULATION_SIZE)
        self.assertEqual(config.crossover_count, AssemblyDefaults.CROSSOVER_COUNT)
        self.assertEqual(config.mutation_count, AssemblyDefaults.MUTATION_COUNT)
        self.assertEqual(config.termination.maximum_generations, AssemblyDefaults.GENERATIONS)


# ---------------------------------------------------------------------------------------------------------------------
# Exécution complète sur bench_1, avec MiniZinc et CP-SAT
# ---------------------------------------------------------------------------------------------------------------------

def run_engine(instance: ProblemInstance, dispatcher: ObservationHub) -> MemeticResult:
    config = build_block_memetic_config(instance, INTEGRATION_SETTINGS, dispatcher)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", MiniZincWarning)
        return Memetic(config).run()


def history(events: list[Event]) -> list[list]:
    """Génomes de la population à chaque ``GenerationEnded``."""
    return [[individual.genome for individual in event.population]
            for event in events if isinstance(event, GenerationEnded)]


class TestMemeticOnBench1(unittest.TestCase):
    """Deux exécutions de même graine : ``plain`` sans mesure, ``observed`` avec collecteurs et destinations.

    Les deux exécutions sont faites une seule fois, dans ``setUpClass`` (environ 30 s, une quarantaine d'appels à
    CP-SAT) ; les tests ne font ensuite que lire leurs résultats. Le temps est attribué à un autre test que celui qui
    le consomme : en console (``unittest -v``), la pause suit la ligne du dernier test de ``TestAssembly`` ; dans
    PyCharm, elle est comptée dans le premier test de cette classe.
    """

    instance: ProblemInstance
    plain: MemeticResult
    observed: MemeticResult
    events: list[Event]
    memory: MemorySink
    jsonl_lines: list[dict]

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = bench_1()
        cls.plain = run_engine(cls.instance, ObservationHub())

        recorder = RecordingCollector()
        cls.memory = MemorySink()
        collectors = (
            recorder,
            CostStatisticsCollector(),
            DiversityCollector(cls.instance.period_count),
            FeasibilityRateCollector(),
            SolverEffortCollector(),
        )
        with tempfile.TemporaryDirectory() as directory:
            jsonl_path = Path(directory) / EVENTS_FILE
            hub = ObservationHub(collectors, (cls.memory, JsonlSink(jsonl_path)))
            cls.observed = run_engine(cls.instance, hub)
            cls.jsonl_lines = [json.loads(line) for line in jsonl_path.read_text().splitlines()]
        cls.events = recorder.events

    def events_of(self, event_type: type) -> list:
        return [event for event in self.events if isinstance(event, event_type)]

    # --- Déroulement -------------------------------------------------------------------------------------------------

    def test_givenRun_whenFinished_thenGenerationCountAndPopulationSizeAreKept(self) -> None:
        self.assertEqual(self.observed.generations, INTEGRATION_SETTINGS.generations)
        self.assertEqual(len(self.observed.population), INTEGRATION_SETTINGS.population_size)
        ends = self.events_of(GenerationEnded)
        self.assertEqual([event.generation for event in ends], list(range(INTEGRATION_SETTINGS.generations + 1)))
        for event in ends + self.events_of(Restarted):
            with self.subTest(event=type(event).__name__, generation=event.generation):
                self.assertEqual(len(event.population), INTEGRATION_SETTINGS.population_size)

    def test_givenRun_whenFinished_thenBestCostNeverIncreases(self) -> None:
        populations = [event.population for event in self.events if isinstance(event, (GenerationEnded, Restarted))]
        bests = [min(individual.cost.total for individual in population) for population in populations]
        for previous, current in zip(bests, bests[1:]):
            self.assertLessEqual(current, previous)

    def test_givenRun_whenFinished_thenBestIsTheCheapestAndStructurallyFeasible(self) -> None:
        best = self.observed.best
        self.assertEqual(best.cost.total, min(individual.cost.total for individual in self.observed.population))
        self.assertEqual(FeasibilityChecker(self.instance).violations(best.horaire), [])
        self.assertEqual(self.events[-1].best.genome, best.genome)

    def test_givenRun_whenFinished_thenEveryIndividualIsStructurallyFeasible(self) -> None:
        checker = FeasibilityChecker(self.instance)
        populations = [event.population for event in self.events if isinstance(event, (GenerationEnded, Restarted))]
        individuals = [event.individual for event in self.events_of(IndividualCreated)]
        individuals += [individual for population in populations for individual in population]
        for index, individual in enumerate(individuals):
            with self.subTest(individual=index):
                self.assertEqual(checker.violations(individual.horaire), [])

    def test_givenShortStagnation_whenRun_thenTheRestartPathIsExercised(self) -> None:
        self.assertGreaterEqual(self.observed.restarts, MIN_EXPECTED_RESTARTS)

    def test_givenRun_whenFinished_thenRestartsMatchConvergedEvents(self) -> None:
        self.assertEqual(len(self.events_of(Converged)), self.observed.restarts)
        self.assertEqual(len(self.events_of(Restarted)), self.observed.restarts)

    # --- Recherche locale réelle -------------------------------------------------------------------------------------

    def test_givenRun_whenFinished_thenOneLocalSearchPerNewIndividualWhateverItsOrigin(self) -> None:
        searches = self.events_of(LocalSearchDone)
        created = self.events_of(IndividualCreated)
        self.assertEqual(len(searches), len(created), "chaque nouvel individu passe par le LocalSolver")
        by_origin = {origin.value: 0 for origin in Origins}
        for event in searches:
            by_origin[event.origin] += 1
        per_generation = INTEGRATION_SETTINGS.crossover_count * CHILDREN_PER_CROSSOVER
        self.assertEqual(by_origin[Origins.INITIALIZATION.value], INTEGRATION_SETTINGS.population_size)
        self.assertEqual(by_origin[Origins.CROSSOVER.value], per_generation * INTEGRATION_SETTINGS.generations)
        self.assertEqual(by_origin[Origins.MUTATION.value],
                         INTEGRATION_SETTINGS.mutation_count * INTEGRATION_SETTINGS.generations)
        restart_newcomers = sum(1 for event in created if event.origin == Origins.RESTART.value)
        self.assertEqual(by_origin[Origins.RESTART.value], restart_newcomers)
        self.assertGreater(restart_newcomers, 0)

    def test_givenFeasibleInput_whenLocalSearchDone_thenCostDoesNotIncrease(self) -> None:
        for index, event in enumerate(self.events_of(LocalSearchDone)):
            if event.cost_before.is_feasible:
                with self.subTest(search=index, outcome=event.result.outcome):
                    self.assertLessEqual(event.cost_after.total, event.cost_before.total)

    def test_givenRun_whenFinished_thenCpSatReallySolvedTheSubproblems(self) -> None:
        searches = self.events_of(LocalSearchDone)
        self.assertTrue(any(event.result.outcome.has_solution for event in searches))
        self.assertTrue(any(event.result.statistics.failures is not None for event in searches))

    # --- Reproductibilité ----------------------------------------------------------------------------------------------

    def test_givenSameSeed_whenRunWithAndWithoutCollectors_thenSameResult(self) -> None:
        self.assertEqual([i.genome for i in self.plain.population], [i.genome for i in self.observed.population])
        self.assertEqual(self.plain.best.genome, self.observed.best.genome)
        self.assertEqual(self.plain.best.cost, self.observed.best.cost)
        self.assertEqual(self.plain.restarts, self.observed.restarts)

    # --- Événements et enregistrements ------------------------------------------------------------------------------

    def test_givenObservedRun_whenListingEvents_thenTheyComeInTheExpectedOrder(self) -> None:
        """Génération 0 : recherches de l'initialiseur, puis individus, puis ``GenerationEnded(0)``. Génération g :
        paires (``LocalSearchDone``, ``IndividualCreated``) des lots NR et NM, puis ``GenerationEnded(g)``, puis, en
        cas de restart, ``Converged(g)``, les recherches et les nouveaux individus du restart, ``Restarted(g)``."""
        self.assertIsInstance(self.events[0], RunStarted)
        self.assertIsInstance(self.events[-1], RunEnded)
        population_size = INTEGRATION_SETTINGS.population_size
        initial_searches = self.events[1:1 + population_size]
        initial_created = self.events[1 + population_size:1 + 2 * population_size]
        for event in initial_searches:
            self.assertIsInstance(event, LocalSearchDone)
            self.assertEqual(event.origin, Origins.INITIALIZATION.value)
        for event in initial_created:
            self.assertIsInstance(event, IndividualCreated)
            self.assertEqual(event.origin, Origins.INITIALIZATION.value)
        self.assertIsInstance(self.events[1 + 2 * population_size], GenerationEnded)

        generation = 0
        restarting = False
        expecting_search_result = False
        for event in self.events[2 + 2 * population_size:-1]:
            with self.subTest(event=type(event).__name__, generation=generation):
                if isinstance(event, Converged):
                    self.assertEqual(event.generation, generation)
                    restarting = True
                elif isinstance(event, Restarted):
                    self.assertTrue(restarting)
                    self.assertEqual(event.generation, generation)
                    restarting = False
                elif restarting:
                    self.assertIsInstance(event, (LocalSearchDone, IndividualCreated))
                    self.assertEqual(event.origin, Origins.RESTART.value)
                    self.assertEqual(event.generation, generation)
                elif isinstance(event, LocalSearchDone):
                    self.assertFalse(expecting_search_result, "deux LocalSearchDone de suite")
                    self.assertEqual(event.generation, generation + 1)
                    expecting_search_result = True
                elif isinstance(event, IndividualCreated):
                    self.assertTrue(expecting_search_result, "IndividualCreated sans LocalSearchDone avant")
                    self.assertEqual(event.generation, generation + 1)
                    expecting_search_result = False
                else:
                    self.assertIsInstance(event, GenerationEnded)
                    self.assertFalse(expecting_search_result)
                    generation += 1
                    self.assertEqual(event.generation, generation)
        self.assertEqual(generation, INTEGRATION_SETTINGS.generations)

    def test_givenObservedRun_whenReadingRecords_thenEachCollectorProducedSome(self) -> None:
        for record_name in (RecordNames.COST_STATISTICS, RecordNames.DIVERSITY,
                            RecordNames.FEASIBILITY_RATES, RecordNames.SOLVER_EFFORT):
            with self.subTest(record=record_name):
                self.assertTrue(self.memory.of_event(record_name))

    def test_givenObservedRun_whenReadingTheJsonlFile_thenSameRecordsAsInMemory(self) -> None:
        self.assertEqual(len(self.jsonl_lines), len(self.memory.records))
        field = RecordSchema.EVENT_FIELD
        self.assertEqual([line[field] for line in self.jsonl_lines], [record[field] for record in self.memory.records])



# ---------------------------------------------------------------------------------------------------------------------
# Témoin « individus aléatoires + LocalSolver » (étape 10d), avec MiniZinc et CP-SAT
# ---------------------------------------------------------------------------------------------------------------------

RANDOM_GENOME_WITNESS = StrategyChoices(
    crossover=StrategyChoice(StrategyNames.RANDOM_GENOME),
    mutation=StrategyChoice(StrategyNames.RANDOM_GENOME),
)


class TestRandomGenomeWitnessOnBench1(unittest.TestCase):
    """Le moteur, assemblé avec les stratégies ``random_genome``, fait une exécution complète sur bench_1.

    On vérifie ce dont le témoin a besoin pour être comparable au mémétique : mêmes réglages, même nombre de
    recherches locales par génération (2 × NR enfants de croisement, NM mutants), individus structurellement
    faisables, reproductibilité. Une exécution, faite une seule fois dans ``setUpClass``.
    """

    instance: ProblemInstance
    result: MemeticResult
    events: list[Event]

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = bench_1()
        recorder = RecordingCollector()
        config = build_block_memetic_config(
            cls.instance, INTEGRATION_SETTINGS, ObservationHub((recorder,)), strategies=RANDOM_GENOME_WITNESS
        )
        cls.config = config
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", MiniZincWarning)
            cls.result = Memetic(config).run()
        cls.events = recorder.events

    def test_givenWitnessStrategies_whenBuilding_thenRandomOperatorsReceiveTheInstance(self) -> None:
        self.assertIsInstance(self.config.crossover, RandomGenomeCrossover)
        self.assertIsInstance(self.config.mutation, RandomGenomeMutation)
        self.assertIs(self.config.crossover.instance, self.instance)
        self.assertIs(self.config.mutation.instance, self.instance)

    def test_givenWitnessRun_whenFinished_thenGenerationCountAndPopulationSizeAreKept(self) -> None:
        self.assertEqual(self.result.generations, INTEGRATION_SETTINGS.generations)
        self.assertEqual(len(self.result.population), INTEGRATION_SETTINGS.population_size)

    def test_givenWitnessRun_whenCountingLocalSearches_thenSameBudgetPerGenerationAsTheMemetic(self) -> None:
        expected = {
            Origins.CROSSOVER.value: CHILDREN_PER_CROSSOVER * INTEGRATION_SETTINGS.crossover_count,
            Origins.MUTATION.value: INTEGRATION_SETTINGS.mutation_count,
        }
        searches = [event for event in self.events if isinstance(event, LocalSearchDone)]
        for generation in range(1, INTEGRATION_SETTINGS.generations + 1):
            for origin, count in expected.items():
                with self.subTest(generation=generation, origin=origin):
                    found = [event for event in searches if event.generation == generation and event.origin == origin]
                    self.assertEqual(len(found), count)

    def test_givenWitnessRun_whenFinished_thenEveryIndividualIsStructurallyFeasible(self) -> None:
        checker = FeasibilityChecker(self.instance)
        created = [event.individual for event in self.events if isinstance(event, IndividualCreated)]
        for index, individual in enumerate(created):
            with self.subTest(index=index):
                self.assertTrue(checker.is_feasible(individual.horaire))

    def test_givenSameSeed_whenWitnessRunsTwice_thenSameResult(self) -> None:
        config = build_block_memetic_config(self.instance, INTEGRATION_SETTINGS, strategies=RANDOM_GENOME_WITNESS)
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", MiniZincWarning)
            again = Memetic(config).run()
        self.assertEqual(again.best.genome, self.result.best.genome)
        self.assertEqual(
            [individual.genome for individual in again.population],
            [individual.genome for individual in self.result.population],
        )

# ---------------------------------------------------------------------------------------------------------------------
# Témoin fort : recherche locale itérée (1+1) (étape 10e), avec MiniZinc et CP-SAT
# ---------------------------------------------------------------------------------------------------------------------

ITERATED_LOCAL_SEARCH_SETTINGS = AssemblySettings(
    population_size=1, crossover_count=0, mutation_count=1, generations=6, master_seed=5,
    stagnation_generations=1000,
)
ITERATED_LOCAL_SEARCH = StrategyChoices(survivor_selector=StrategyChoice(StrategyNames.PLUS, {"prefer_newest": True}))


class TestIteratedLocalSearchOnBench1(unittest.TestCase):
    """Le moteur en recherche locale itérée (1+1) : population 1, NR = 0, NM = 1, l'enfant gardé s'il n'est pas pire,
    pas de restart. Une seule exécution, dans ``setUpClass``."""

    result: MemeticResult
    events: list[Event]

    @classmethod
    def setUpClass(cls) -> None:
        recorder = RecordingCollector()
        config = build_block_memetic_config(
            bench_1(), ITERATED_LOCAL_SEARCH_SETTINGS, ObservationHub((recorder,)), strategies=ITERATED_LOCAL_SEARCH
        )
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", MiniZincWarning)
            cls.result = Memetic(config).run()
        cls.events = recorder.events

    def test_givenRun_whenCountingLocalSearches_thenOnePerGenerationPlusTheInitialOne(self) -> None:
        searches = [event for event in self.events if isinstance(event, LocalSearchDone)]
        self.assertEqual(len(searches), 1 + ITERATED_LOCAL_SEARCH_SETTINGS.generations)
        self.assertEqual({event.origin for event in searches if event.generation > 0}, {Origins.MUTATION.value})

    def test_givenRun_whenFinished_thenASingleIndividualAndNoRestart(self) -> None:
        self.assertEqual(self.result.restarts, 0)
        for event in self.events:
            if isinstance(event, GenerationEnded):
                self.assertEqual(len(event.population), 1)

    def test_givenRun_whenFollowingTheCurrentIndividual_thenItIsTheChildUnlessTheChildIsWorse(self) -> None:
        current = None
        for event in self.events:
            if isinstance(event, IndividualCreated) and event.generation > 0:
                child = event.individual
            if isinstance(event, GenerationEnded):
                (survivor,) = event.population
                if current is not None:
                    expected = child if child.cost.total <= current.cost.total else current
                    with self.subTest(generation=event.generation):
                        self.assertEqual(survivor.genome, expected.genome)
                        self.assertLessEqual(survivor.cost.total, current.cost.total)
                current = survivor


if __name__ == "__main__":
    unittest.main()
