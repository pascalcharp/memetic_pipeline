"""Tests des collecteurs (src/observability/collectors.py) — étape 8b, Mély.

Tests écrits par Claude (règle des tests par agent, CLAUDE.md), à faire passer sur la branche
``etape-8b-observabilite``. Ils suivent les contrats écrits dans les docstrings des collecteurs et les noms de
champs de ``collectors.py`` (``CostStatisticsFields``, ``DiversityFields``, ``FeasibilityFields``,
``SolverEffortFields``, ``RecordFields``, ``Scopes``). Sans MiniZinc. Validés le 2026-11-16 contre une
implémentation de référence jetable (24 tests verts), qui n'est pas dans le dépôt : à toi d'écrire la tienne.

Les événements sont construits à la main et passent par ``ObservationHub`` ; les enregistrements sont lus dans un
``MemorySink``. Les valeurs attendues sont calculées à la main dans chaque test.
"""

import json
import math
import random
import unittest
from collections.abc import Sequence
from datetime import timedelta

from src.ga.chromosome import BlockEncoding, BlockGene, BlockGenome
from src.ga.individual import Individu
from src.memetic.local_search import LocalSearchResult
from src.memetic.solver import SolveOutcome, SolverStatistics
from src.model.evaluation import CostBreakdown
from src.observability.collectors import (
    CollectorDefaults,
    CollectorError,
    CostStatisticsCollector,
    CostStatisticsFields,
    DiversityCollector,
    DiversityFields,
    FeasibilityFields,
    FeasibilityRateCollector,
    InvalidCollectorParameterError,
    InvalidPopulationError,
    MetricCollector,
    RecordFields,
    RecordNames,
    Scopes,
    SolverEffortCollector,
    SolverEffortFields,
)
from src.observability.events import (
    Converged,
    Event,
    GenerationEnded,
    LocalSearchDone,
    Origins,
    RecordSchema,
    RunEnded,
    RunStarted,
)
from src.observability.hub import ObservationHub
from src.observability.sinks import MemorySink
from tests.fixtures import REFERENCE_GENE, synthetic_instance
from tests.test_feasibility import REFERENCE_SHIFT, single

INVALID_EVERY: int = 0
SEED: int = 31
EMPLOYEE_COUNT: int = 2
CROSSOVER_NAME: str = "UniformGeneCrossover"
MUTATION_NAME: str = "ShiftStartMutation"
PLACES: int = 9

# Deux gènes faisables différents sur l'instance synthétique : le quart de référence, et le même décalé d'une période.
GENE_A: BlockGene = REFERENCE_GENE
GENE_B: BlockGene = BlockGene(REFERENCE_GENE.start + 1, REFERENCE_GENE.blocks)


# ---------------------------------------------------------------------------------------------------------------------
# Outils
# ---------------------------------------------------------------------------------------------------------------------

def cost(under: int = 0, over: int = 0, violations: int = 0, quasi_hard: int = 0, penalty: int = 0) -> CostBreakdown:
    """Coût décomposé écrit à la main ; ``total`` = ``under + over + penalty``."""
    return CostBreakdown(
        under_coverage_cost=under,
        over_coverage_cost=over,
        quasi_hard_cells=quasi_hard,
        coverage_violations=violations,
        structural_violations=0,
        penalty_cost=penalty,
    )


FEASIBLE_COST: CostBreakdown = cost(over=10)
INFEASIBLE_COST: CostBreakdown = cost(violations=1, penalty=1_000_000)


def labeled_individual(label: str, individual_cost: CostBreakdown) -> Individu[str]:
    """Individu évalué de coût choisi ; l'horaire est celui de référence (les statistiques de coût l'ignorent)."""
    return Individu(genome=label, horaire=single(REFERENCE_SHIFT), cost=individual_cost)


def genome_individual(genome: BlockGenome, total: int) -> Individu[BlockGenome]:
    """Individu évalué décodé de ``genome`` (vraie grille), de coût ``total`` (sur-couverture)."""
    return Individu.from_genome(genome, BlockEncoding()).with_cost(cost(over=total))


def local_search_done(
        generation: int,
        origin: str,
        operator: str | None,
        feasible_before: bool = True,
        feasible_after: bool = True,
        statistics: SolverStatistics = SolverStatistics(),
) -> LocalSearchDone:
    result = LocalSearchResult(
        horaire=single(REFERENCE_SHIFT),
        outcome=SolveOutcome.FEASIBLE,
        freed_employees=frozenset(),
        statistics=statistics,
    )
    return LocalSearchDone(
        generation=generation,
        origin=origin,
        operator=operator,
        cost_before=FEASIBLE_COST if feasible_before else INFEASIBLE_COST,
        cost_after=FEASIBLE_COST if feasible_after else INFEASIBLE_COST,
        result=result,
    )


def records_of(collector: MetricCollector, events: Sequence[Event]) -> list[dict]:
    """Enregistrements produits par ``collector`` sur ``events``, lus dans un ``MemorySink``."""
    sink = MemorySink()
    hub = ObservationHub([collector], [sink])
    for event in events:
        hub.emit(event)
    return sink.records


def by_group(records: Sequence[dict]) -> dict[tuple[str, str | None], dict]:
    """Enregistrements de taux de faisabilité indexés par (origine, opérateur)."""
    return {(r[FeasibilityFields.ORIGIN], r[FeasibilityFields.OPERATOR]): r for r in records}


def scenario_events() -> list[Event]:
    """Une petite exécution complète, avec tous les types d'événements, pour les tests communs."""
    population = (genome_individual((GENE_A, GENE_B), 10), genome_individual((GENE_B, GENE_A), 20))
    return [
        RunStarted(master_seed=SEED, population_size=len(population), crossover_count=1, mutation_count=1),
        GenerationEnded(generation=0, population=population),
        local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME, False, True,
                          SolverStatistics(failures=2, propagations=10, solve_time=timedelta(seconds=1))),
        local_search_done(1, Origins.MUTATION, MUTATION_NAME),
        GenerationEnded(generation=1, population=population),
        Converged(generation=1),
        RunEnded(generations=1, best=population[0]),
    ]


def all_collectors() -> list[MetricCollector]:
    period_count = synthetic_instance(EMPLOYEE_COUNT).period_count
    return [CostStatisticsCollector(), DiversityCollector(period_count), FeasibilityRateCollector(),
            SolverEffortCollector()]


# ---------------------------------------------------------------------------------------------------------------------
# Contrat du scaffold
# ---------------------------------------------------------------------------------------------------------------------

class TestScaffoldContract(unittest.TestCase):

    def test_givenInterface_whenInstantiated_thenRaisesTypeError(self) -> None:
        with self.assertRaises(TypeError):
            MetricCollector()  # type: ignore[abstract]

    def test_givenCollectors_whenChecked_thenImplementMetricCollector(self) -> None:
        for collector in (CostStatisticsCollector, DiversityCollector, FeasibilityRateCollector, SolverEffortCollector):
            with self.subTest(collector=collector.__name__):
                self.assertTrue(issubclass(collector, MetricCollector))

    def test_givenNoEvery_whenDiversityCollector_thenDefaultFrequency(self) -> None:
        collector = DiversityCollector(synthetic_instance().period_count)
        self.assertEqual(collector.every, CollectorDefaults.DIVERSITY_EVERY_GENERATIONS)

    def test_givenInvalidEvery_whenDiversityCollector_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidCollectorParameterError) as context:
            DiversityCollector(synthetic_instance().period_count, every=INVALID_EVERY)
        self.assertIn(str(INVALID_EVERY), str(context.exception))
        self.assertIsInstance(context.exception, CollectorError)


# ---------------------------------------------------------------------------------------------------------------------
# Règles communes à tous les collecteurs (D8)
# ---------------------------------------------------------------------------------------------------------------------

class TestCommonRules(unittest.TestCase):

    def test_givenScenario_whenEveryCollectorObserves_thenRecordsHaveSchemaAndAreJsonSerializable(self) -> None:
        for collector in all_collectors():
            with self.subTest(collector=type(collector).__name__):
                records = records_of(collector, scenario_events())
                self.assertTrue(records, "chaque collecteur produit au moins un enregistrement sur ce scénario")
                for record in records:
                    self.assertEqual(record[RecordSchema.VERSION_FIELD], RecordSchema.VERSION)
                    json.dumps(record)

    def test_givenScenario_whenEveryCollectorObserves_thenGlobalRandomStateIsUnchanged(self) -> None:
        random.seed(SEED)
        state_before = random.getstate()
        for collector in all_collectors():
            records_of(collector, scenario_events())
        self.assertEqual(random.getstate(), state_before)

    def test_givenScenario_whenEveryCollectorObserves_thenEachProducesOnlyItsOwnRecordType(self) -> None:
        expected_types = {
            CostStatisticsCollector: RecordNames.COST_STATISTICS,
            DiversityCollector: RecordNames.DIVERSITY,
            FeasibilityRateCollector: RecordNames.FEASIBILITY_RATES,
            SolverEffortCollector: RecordNames.SOLVER_EFFORT,
        }
        for collector in all_collectors():
            with self.subTest(collector=type(collector).__name__):
                types = {record[RecordSchema.EVENT_FIELD] for record in records_of(collector, scenario_events())}
                self.assertEqual(types, {expected_types[type(collector)]})


# ---------------------------------------------------------------------------------------------------------------------
# Statistiques de coût
# ---------------------------------------------------------------------------------------------------------------------

class TestCostStatisticsCollector(unittest.TestCase):

    def test_givenPopulation_whenGenerationEnded_thenTotalStatisticsAreComputed(self) -> None:
        population = tuple(labeled_individual(label, cost(over=total)) for label, total in zip("ABCD", (10, 20, 30, 40)))
        records = records_of(CostStatisticsCollector(), [GenerationEnded(generation=2, population=population)])
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record[RecordSchema.EVENT_FIELD], RecordNames.COST_STATISTICS)
        self.assertEqual(record[RecordFields.GENERATION], 2)
        self.assertEqual(record[CostStatisticsFields.SIZE], 4)
        self.assertEqual(record[CostStatisticsFields.TOTAL_MIN], 10)
        self.assertEqual(record[CostStatisticsFields.TOTAL_MAX], 40)
        self.assertIs(type(record[CostStatisticsFields.TOTAL_MIN]), int)
        self.assertIs(type(record[CostStatisticsFields.TOTAL_MAX]), int)
        self.assertAlmostEqual(record[CostStatisticsFields.TOTAL_MEAN], 25.0, places=PLACES)
        self.assertAlmostEqual(record[CostStatisticsFields.TOTAL_MEDIAN], 25.0, places=PLACES)
        self.assertAlmostEqual(record[CostStatisticsFields.TOTAL_STDEV], math.sqrt(125.0), places=PLACES)

    def test_givenDecomposedCosts_whenGenerationEnded_thenMeansAndFeasibleCountAreComputed(self) -> None:
        population = (
            labeled_individual("A", cost(under=4, over=2, quasi_hard=1)),
            labeled_individual("B", cost(under=0, over=6, violations=2, quasi_hard=0, penalty=2_000_000)),
        )
        record = records_of(CostStatisticsCollector(), [GenerationEnded(generation=0, population=population)])[0]
        self.assertAlmostEqual(record[CostStatisticsFields.UNDER_COVERAGE_MEAN], 2.0, places=PLACES)
        self.assertAlmostEqual(record[CostStatisticsFields.OVER_COVERAGE_MEAN], 4.0, places=PLACES)
        self.assertAlmostEqual(record[CostStatisticsFields.COVERAGE_VIOLATIONS_MEAN], 1.0, places=PLACES)
        self.assertAlmostEqual(record[CostStatisticsFields.QUASI_HARD_CELLS_MEAN], 0.5, places=PLACES)
        self.assertEqual(record[CostStatisticsFields.FEASIBLE_COUNT], 1)

    def test_givenSingleIndividual_whenGenerationEnded_thenStandardDeviationIsZero(self) -> None:
        population = (labeled_individual("A", cost(over=7)),)
        record = records_of(CostStatisticsCollector(), [GenerationEnded(generation=0, population=population)])[0]
        self.assertEqual(record[CostStatisticsFields.TOTAL_STDEV], 0)
        self.assertEqual(record[CostStatisticsFields.TOTAL_MIN], record[CostStatisticsFields.TOTAL_MAX])

    def test_givenOtherEvents_whenObserved_thenNoRecord(self) -> None:
        events = [RunStarted(master_seed=SEED, population_size=1, crossover_count=1, mutation_count=1),
                  Converged(generation=1), local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME)]
        self.assertEqual(records_of(CostStatisticsCollector(), events), [])


# ---------------------------------------------------------------------------------------------------------------------
# Diversité
# ---------------------------------------------------------------------------------------------------------------------

class TestDiversityCollector(unittest.TestCase):

    def setUp(self) -> None:
        self.period_count = synthetic_instance(EMPLOYEE_COUNT).period_count

    def test_givenPermutedGenomes_whenGenerationEnded_thenGenotypicDiversityIgnoresPermutation(self) -> None:
        # (A, B) et (B, A) : même génotype à une permutation près, mais grilles différentes.
        population = (
            genome_individual((GENE_A, GENE_B), 10),
            genome_individual((GENE_B, GENE_A), 10),
            genome_individual((GENE_A, GENE_B), 20),
        )
        records = records_of(DiversityCollector(self.period_count), [GenerationEnded(generation=0, population=population)])
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record[RecordFields.GENERATION], 0)
        self.assertAlmostEqual(record[DiversityFields.GENOTYPIC], 1 / 3, places=PLACES)
        self.assertAlmostEqual(record[DiversityFields.PHENOTYPIC], 2 / 3, places=PLACES)
        self.assertEqual(record[DiversityFields.DISTINCT_COSTS], 2)

    def test_givenAllDistinct_whenGenerationEnded_thenDiversitiesAreOne(self) -> None:
        population = (genome_individual((GENE_A, GENE_A), 10), genome_individual((GENE_A, GENE_B), 20))
        record = records_of(DiversityCollector(self.period_count),
                            [GenerationEnded(generation=0, population=population)])[0]
        self.assertAlmostEqual(record[DiversityFields.GENOTYPIC], 1.0, places=PLACES)
        self.assertAlmostEqual(record[DiversityFields.PHENOTYPIC], 1.0, places=PLACES)

    def test_givenEvery_whenSeveralGenerations_thenMeasuresOnlyMultiplesOfEvery(self) -> None:
        population = (genome_individual((GENE_A, GENE_B), 10),)
        events = [GenerationEnded(generation=generation, population=population) for generation in range(5)]
        records = records_of(DiversityCollector(self.period_count, every=2), events)
        self.assertEqual([r[RecordFields.GENERATION] for r in records], [0, 2, 4])

    def test_givenOtherEvents_whenObserved_thenNoRecord(self) -> None:
        events = [Converged(generation=1), local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME)]
        self.assertEqual(records_of(DiversityCollector(self.period_count), events), [])


# ---------------------------------------------------------------------------------------------------------------------
# Taux de faisabilité
# ---------------------------------------------------------------------------------------------------------------------

class TestFeasibilityRateCollector(unittest.TestCase):

    def events(self) -> list[Event]:
        population = (labeled_individual("A", FEASIBLE_COST),)
        return [
            GenerationEnded(generation=0, population=population),
            # Génération 1 : 3 croisements (avant : F, I, I ; après : F, F, I), 2 mutations (toujours faisables).
            local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME, True, True),
            local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME, False, True),
            local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME, False, False),
            local_search_done(1, Origins.MUTATION, MUTATION_NAME, True, True),
            local_search_done(1, Origins.MUTATION, MUTATION_NAME, True, True),
            GenerationEnded(generation=1, population=population),
            # Génération 2 : 1 croisement (avant : I ; après : F).
            local_search_done(2, Origins.CROSSOVER, CROSSOVER_NAME, False, True),
            GenerationEnded(generation=2, population=population),
            RunEnded(generations=2, best=population[0]),
        ]

    def test_givenGenerationWithoutCalls_whenGenerationEnded_thenNoRecord(self) -> None:
        records = records_of(FeasibilityRateCollector(), self.events())
        self.assertNotIn(0, [r[RecordFields.GENERATION] for r in records])

    def test_givenCallsOfTwoOperators_whenGenerationEnded_thenOneRecordPerGroupWithRates(self) -> None:
        records = records_of(FeasibilityRateCollector(), self.events())
        generation_one = by_group([r for r in records if r[RecordFields.GENERATION] == 1
                                   and r[RecordFields.SCOPE] == Scopes.GENERATION])
        self.assertEqual(set(generation_one), {(Origins.CROSSOVER, CROSSOVER_NAME), (Origins.MUTATION, MUTATION_NAME)})
        crossover = generation_one[(Origins.CROSSOVER, CROSSOVER_NAME)]
        self.assertEqual(crossover[FeasibilityFields.COUNT], 3)
        self.assertEqual(crossover[FeasibilityFields.FEASIBLE_BEFORE], 1)
        self.assertEqual(crossover[FeasibilityFields.FEASIBLE_AFTER], 2)
        self.assertAlmostEqual(crossover[FeasibilityFields.RATE_BEFORE], 1 / 3, places=PLACES)
        self.assertAlmostEqual(crossover[FeasibilityFields.RATE_AFTER], 2 / 3, places=PLACES)
        mutation = generation_one[(Origins.MUTATION, MUTATION_NAME)]
        self.assertEqual(mutation[FeasibilityFields.COUNT], 2)
        self.assertAlmostEqual(mutation[FeasibilityFields.RATE_BEFORE], 1.0, places=PLACES)

    def test_givenNewGeneration_whenGenerationEnded_thenOnlyCallsOfThatGenerationAreCounted(self) -> None:
        records = records_of(FeasibilityRateCollector(), self.events())
        generation_two = by_group([r for r in records if r[RecordFields.GENERATION] == 2
                                   and r[RecordFields.SCOPE] == Scopes.GENERATION])
        self.assertEqual(set(generation_two), {(Origins.CROSSOVER, CROSSOVER_NAME)})
        crossover = generation_two[(Origins.CROSSOVER, CROSSOVER_NAME)]
        self.assertEqual(crossover[FeasibilityFields.COUNT], 1)
        self.assertEqual(crossover[FeasibilityFields.FEASIBLE_BEFORE], 0)
        self.assertEqual(crossover[FeasibilityFields.FEASIBLE_AFTER], 1)

    def test_givenRunEnded_whenObserved_thenCumulativeRecordsCoverTheWholeRun(self) -> None:
        records = records_of(FeasibilityRateCollector(), self.events())
        cumulative = by_group([r for r in records if r[RecordFields.SCOPE] == Scopes.CUMULATIVE])
        self.assertEqual(set(cumulative), {(Origins.CROSSOVER, CROSSOVER_NAME), (Origins.MUTATION, MUTATION_NAME)})
        crossover = cumulative[(Origins.CROSSOVER, CROSSOVER_NAME)]
        self.assertEqual(crossover[RecordFields.GENERATION], 2)
        self.assertEqual(crossover[FeasibilityFields.COUNT], 4)
        self.assertEqual(crossover[FeasibilityFields.FEASIBLE_BEFORE], 1)
        self.assertEqual(crossover[FeasibilityFields.FEASIBLE_AFTER], 3)
        self.assertAlmostEqual(crossover[FeasibilityFields.RATE_AFTER], 3 / 4, places=PLACES)
        self.assertEqual(cumulative[(Origins.MUTATION, MUTATION_NAME)][FeasibilityFields.COUNT], 2)

    def test_givenInitializationCalls_whenGenerationEnded_thenOperatorIsNone(self) -> None:
        population = (labeled_individual("A", FEASIBLE_COST),)
        events = [local_search_done(0, Origins.INITIALIZATION, None, False, True),
                  GenerationEnded(generation=0, population=population)]
        records = records_of(FeasibilityRateCollector(), events)
        self.assertEqual(len(records), 1)
        self.assertIsNone(records[0][FeasibilityFields.OPERATOR])
        self.assertEqual(records[0][FeasibilityFields.ORIGIN], Origins.INITIALIZATION)

    def test_givenRunStarted_whenNewRunBegins_thenFeasibilityCountsAreReset(self) -> None:
        collector = FeasibilityRateCollector()
        population = (labeled_individual("A", FEASIBLE_COST),)

        # Première exécution : un croisement infaisable devient faisable.
        collector.on_event(
            local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME, False, True)
        )
        collector.on_event(GenerationEnded(generation=1, population=population))

        # Début d'une nouvelle exécution avec le même collecteur.
        collector.on_event(
            RunStarted(
                master_seed=42,
                population_size=1,
                crossover_count=1,
                mutation_count=0,
            )
        )

        # Deuxième exécution : une mutation faisable reste faisable.
        collector.on_event(
            local_search_done(1, Origins.MUTATION, MUTATION_NAME, True, True)
        )
        collector.on_event(GenerationEnded(generation=1, population=population))
        records = collector.on_event(RunEnded(generations=1, best=population[0]))

        # Le cumul ne doit contenir que la deuxième exécution.
        self.assertEqual(len(records), 1)
        record = records[0]
        self.assertEqual(record[RecordFields.SCOPE], Scopes.CUMULATIVE)
        self.assertEqual(record[FeasibilityFields.ORIGIN], Origins.MUTATION)
        self.assertEqual(record[FeasibilityFields.COUNT], 1)
        self.assertEqual(record[FeasibilityFields.FEASIBLE_BEFORE], 1)
        self.assertEqual(record[FeasibilityFields.FEASIBLE_AFTER], 1)


# ---------------------------------------------------------------------------------------------------------------------
# Charge du solveur
# ---------------------------------------------------------------------------------------------------------------------

class TestSolverEffortCollector(unittest.TestCase):

    def events(self) -> list[Event]:
        population = (labeled_individual("A", FEASIBLE_COST),)
        return [
            GenerationEnded(generation=0, population=population),
            local_search_done(1, Origins.CROSSOVER, CROSSOVER_NAME, statistics=SolverStatistics(
                nodes=None, failures=5, propagations=100, solve_time=timedelta(seconds=0.5), deterministic_time=0.2)),
            local_search_done(1, Origins.MUTATION, MUTATION_NAME, statistics=SolverStatistics(
                nodes=None, failures=3, propagations=None, solve_time=timedelta(seconds=0.25))),
            GenerationEnded(generation=1, population=population),
            local_search_done(2, Origins.CROSSOVER, CROSSOVER_NAME, statistics=SolverStatistics(
                nodes=None, failures=1, propagations=50, solve_time=None, deterministic_time=0.05)),
            GenerationEnded(generation=2, population=population),
            RunEnded(generations=2, best=population[0]),
        ]

    def records(self, scope: str) -> list[dict]:
        return [r for r in records_of(SolverEffortCollector(), self.events()) if r[RecordFields.SCOPE] == scope]

    def test_givenGenerationWithoutCalls_whenGenerationEnded_thenZeroCallsAndNoStatistics(self) -> None:
        generation_zero = [r for r in self.records(Scopes.GENERATION) if r[RecordFields.GENERATION] == 0]
        self.assertEqual(len(generation_zero), 1)
        record = generation_zero[0]
        self.assertEqual(record[SolverEffortFields.CALLS], 0)
        for field in (SolverEffortFields.NODES, SolverEffortFields.FAILURES, SolverEffortFields.PROPAGATIONS,
                      SolverEffortFields.SOLVE_TIME_SECONDS, SolverEffortFields.DETERMINISTIC_TIME):
            self.assertIsNone(record[field])

    def test_givenCalls_whenGenerationEnded_thenSumsOnlyReportedStatisticsOfThatGeneration(self) -> None:
        record = [r for r in self.records(Scopes.GENERATION) if r[RecordFields.GENERATION] == 1][0]
        self.assertEqual(record[SolverEffortFields.CALLS], 2)
        self.assertIsNone(record[SolverEffortFields.NODES])
        self.assertEqual(record[SolverEffortFields.FAILURES], 8)
        self.assertEqual(record[SolverEffortFields.PROPAGATIONS], 100)
        self.assertAlmostEqual(record[SolverEffortFields.SOLVE_TIME_SECONDS], 0.75, places=PLACES)

    def test_givenNewGeneration_whenGenerationEnded_thenCountsRestartFromZero(self) -> None:
        record = [r for r in self.records(Scopes.GENERATION) if r[RecordFields.GENERATION] == 2][0]
        self.assertEqual(record[SolverEffortFields.CALLS], 1)
        self.assertEqual(record[SolverEffortFields.FAILURES], 1)
        self.assertIsNone(record[SolverEffortFields.SOLVE_TIME_SECONDS])

    def test_givenRunEnded_whenObserved_thenCumulativeEffortOfTheWholeRun(self) -> None:
        cumulative = self.records(Scopes.CUMULATIVE)
        self.assertEqual(len(cumulative), 1)
        record = cumulative[0]
        self.assertEqual(record[RecordFields.GENERATION], 2)
        self.assertEqual(record[SolverEffortFields.CALLS], 3)
        self.assertIsNone(record[SolverEffortFields.NODES])
        self.assertEqual(record[SolverEffortFields.FAILURES], 9)
        self.assertEqual(record[SolverEffortFields.PROPAGATIONS], 150)
        self.assertAlmostEqual(record[SolverEffortFields.SOLVE_TIME_SECONDS], 0.75, places=PLACES)


    def test_givenDeterministicTimes_whenObserved_thenSummedPerGenerationAndForTheRunIgnoringNone(self) -> None:
        # Étape 10d : la mutation de la génération 1 ne rapporte pas de temps déterministe.
        by_generation = {r[RecordFields.GENERATION]: r for r in self.records(Scopes.GENERATION)}
        self.assertAlmostEqual(by_generation[1][SolverEffortFields.DETERMINISTIC_TIME], 0.2, places=PLACES)
        self.assertAlmostEqual(by_generation[2][SolverEffortFields.DETERMINISTIC_TIME], 0.05, places=PLACES)
        (cumulative,) = self.records(Scopes.CUMULATIVE)
        self.assertAlmostEqual(cumulative[SolverEffortFields.DETERMINISTIC_TIME], 0.25, places=PLACES)

    def test_givenRunStarted_whenNewRunBegins_thenSolverEffortIsReset(self) -> None:
        collector = SolverEffortCollector()
        population = (labeled_individual("A", FEASIBLE_COST),)

        # Première exécution : 5 échecs rapportés.
        collector.on_event(
            local_search_done(
                1,
                Origins.CROSSOVER,
                CROSSOVER_NAME,
                statistics=SolverStatistics(
                    failures=5,
                    propagations=100,
                    solve_time=timedelta(seconds=0.5),
                ),
            )
        )

        # Début d'une nouvelle exécution.
        collector.on_event(
            RunStarted(
                master_seed=42,
                population_size=1,
                crossover_count=1,
                mutation_count=0,
            )
        )

        # Deuxième exécution : seulement 2 échecs.
        collector.on_event(
            local_search_done(
                1,
                Origins.MUTATION,
                MUTATION_NAME,
                statistics=SolverStatistics(
                    failures=2,
                    propagations=20,
                    solve_time=timedelta(seconds=0.25),
                ),
            )
        )

        generation_records = collector.on_event(
            GenerationEnded(generation=1, population=population)
        )
        cumulative_records = collector.on_event(
            RunEnded(generations=1, best=population[0])
        )

        # Les statistiques de la première exécution doivent être oubliées.
        self.assertEqual(len(generation_records), 1)
        self.assertEqual(len(cumulative_records), 1)

        for record in generation_records + cumulative_records:
            self.assertEqual(record[SolverEffortFields.CALLS], 1)
            self.assertEqual(record[SolverEffortFields.FAILURES], 2)
            self.assertEqual(record[SolverEffortFields.PROPAGATIONS], 20)
            self.assertAlmostEqual(
                record[SolverEffortFields.SOLVE_TIME_SECONDS],
                0.25,
                places=PLACES,
            )

class TestInvalidCollectorPopulation(unittest.TestCase):
    """Vérifie que les collecteurs refusent les populations invalides."""

    def test_givenEmptyPopulation_whenGenerationEnded_thenBothCollectorsRaise(self):
        event = GenerationEnded(generation=0, population=[])

        collectors = [
            CostStatisticsCollector(),
            DiversityCollector(period_count=96),
        ]

        for collector in collectors:
            with self.subTest(collector=type(collector).__name__):
                with self.assertRaises(InvalidPopulationError):
                    collector.on_event(event)

    def test_givenUnevaluatedPopulation_whenGenerationEnded_thenBothCollectorsRaise(self):
        individual = Individu.from_genome((GENE_A,), BlockEncoding())
        event = GenerationEnded(generation=0, population=[individual])

        collectors = [
            CostStatisticsCollector(),
            DiversityCollector(period_count=96),
        ]

        for collector in collectors:
            with self.subTest(collector=type(collector).__name__):
                with self.assertRaises(InvalidPopulationError):
                    collector.on_event(event)


if __name__ == "__main__":
    unittest.main()
