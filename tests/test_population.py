"""Tests de la gestion de la population (src/ga/population.py) — étape 8, Tristan.

Tests écrits par Claude (règle des tests par agent, CLAUDE.md), à faire passer sur la branche ``etape-8-population``.
Ils traduisent D4 (TODO.md) : (μ+λ) sans doublons, peine de mort complétée par les infaisables, stagnation du
meilleur, restart avec élite. Sans MiniZinc. Validés le 2026-11-16 contre une implémentation de référence jetable
(39 tests verts), qui n'est pas dans le dépôt : à toi d'écrire la tienne.

Conventions des tests :
    - les individus sont construits à la main (``evaluated_individual`` pour un individu faisable de coût choisi,
      ``infeasible_individual`` ci-dessous pour un infaisable) ; leur génome est une étiquette (une chaîne), et deux
      individus de même étiquette ont des génomes identiques ;
    - l'ordre des survivants rendus n'est pas imposé : les tests comparent des ensembles ou des multiensembles ;
    - les propriétés sont vérifiées avec un vrai ``random.Random`` à graine fixée, sur beaucoup de populations.
"""

import random
import unittest
from collections import Counter
from collections.abc import Sequence

from src.ga.chromosome import BlockEncoding, BlockGenome
from src.ga.individual import Individu
from src.ga.initialization import PopulationInitializer, RandomBlockInitializer
from src.ga.population import (
    ConvergenceCriterion,
    DeathPenaltySurvivorSelector,
    EliteRestart,
    InvalidPopulationParameterError,
    PlusSurvivorSelector,
    PopulationDefaults,
    PopulationError,
    RestartPolicy,
    StagnationCriterion,
    SurvivorSelector,
)
from src.ga.selection import EmptyPopulationError, InvalidSelectionParameterError, UnevaluatedIndividualError
from src.model.evaluation import CostBreakdown, CostEvaluator
from tests.fixtures import evaluated_individual, reference_genome, synthetic_instance
from tests.test_feasibility import REFERENCE_SHIFT, single

INVALID_COUNT: int = 0
SEED: int = 23
PROPERTY_TRIALS: int = 200
MAX_POPULATION: int = 12
MAX_TOTAL: int = 50
LABEL_POOL: tuple[str, ...] = tuple("ABCDEFGH")
STAGNATION_GENERATIONS: int = 3
IMPROVING_STEPS: int = 10
ELITE_COUNT: int = 2


# ---------------------------------------------------------------------------------------------------------------------
# Outils
# ---------------------------------------------------------------------------------------------------------------------

def infeasible_individual(genome: str, total: int) -> Individu[str]:
    """Individu évalué infaisable (une violation « au moins 1 »), dont ``cost.total`` vaut ``total``."""
    cost = CostBreakdown(
        under_coverage_cost=0,
        over_coverage_cost=0,
        quasi_hard_cells=0,
        coverage_violations=1,
        structural_violations=0,
        penalty_cost=total,
    )
    return Individu(genome=genome, horaire=single(REFERENCE_SHIFT), cost=cost)


def unevaluated_individual(genome: str) -> Individu[str]:
    return Individu(genome=genome, horaire=single(REFERENCE_SHIFT))


def genomes(population: Sequence[Individu]) -> Counter:
    """Multiensemble des génomes d'une population."""
    return Counter(individual.genome for individual in population)


def totals(population: Sequence[Individu]) -> list[int]:
    """Coûts triés d'une population."""
    return sorted(individual.cost.total for individual in population)


def random_population(rng: random.Random) -> list[Individu[str]]:
    """Population aléatoire, avec des doublons : un même génome a toujours le même coût."""
    size = rng.randint(1, MAX_POPULATION)
    cost_of = {label: rng.randint(0, MAX_TOTAL) for label in LABEL_POOL}
    labels = [rng.choice(LABEL_POOL) for _ in range(size)]
    return [evaluated_individual(label, cost_of[label]) for label in labels]


def population_with_best(best_total: int, size: int) -> tuple[Individu[str], ...]:
    """Population de ``size`` individus distincts dont le meilleur coût vaut ``best_total``."""
    return tuple(evaluated_individual(str(index), best_total + index) for index in range(size))


class RecordingInitializer(PopulationInitializer[BlockGenome]):
    """Faux initialiseur : des individus non évalués du génome de référence ; note les tailles demandées."""

    def __init__(self) -> None:
        self.requested_sizes: list[int] = []

    def initialize(self, size: int, rng: random.Random) -> tuple[Individu[BlockGenome], ...]:
        self.requested_sizes.append(size)
        return tuple(Individu.from_genome(reference_genome(), BlockEncoding()) for _ in range(size))


def elite_restart(elite_count: int = PopulationDefaults.RESTART_ELITE_COUNT) -> EliteRestart:
    instance = synthetic_instance()
    return EliteRestart(RandomBlockInitializer(instance, BlockEncoding()), CostEvaluator(instance), elite_count)


# ---------------------------------------------------------------------------------------------------------------------
# Contrat du scaffold
# ---------------------------------------------------------------------------------------------------------------------

class TestScaffoldContract(unittest.TestCase):

    def test_givenInterfaces_whenInstantiated_thenRaiseTypeError(self) -> None:
        for interface in (SurvivorSelector, ConvergenceCriterion, RestartPolicy):
            with self.subTest(interface=interface.__name__):
                with self.assertRaises(TypeError):
                    interface()  # type: ignore[abstract]

    def test_givenConcreteStrategies_whenChecked_thenImplementTheirInterface(self) -> None:
        self.assertTrue(issubclass(PlusSurvivorSelector, SurvivorSelector))
        self.assertTrue(issubclass(DeathPenaltySurvivorSelector, SurvivorSelector))
        self.assertTrue(issubclass(StagnationCriterion, ConvergenceCriterion))
        self.assertTrue(issubclass(EliteRestart, RestartPolicy))

    def test_givenNoArgument_whenStagnationCriterion_thenDefaultGenerations(self) -> None:
        self.assertEqual(StagnationCriterion().generations, PopulationDefaults.STAGNATION_GENERATIONS)

    def test_givenInvalidGenerations_whenStagnationCriterion_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidPopulationParameterError) as context:
            StagnationCriterion(generations=INVALID_COUNT)
        self.assertIn(str(INVALID_COUNT), str(context.exception))

    def test_givenNoEliteCount_whenEliteRestart_thenDefaultEliteCount(self) -> None:
        self.assertEqual(elite_restart().elite_count, PopulationDefaults.RESTART_ELITE_COUNT)

    def test_givenInvalidEliteCount_whenEliteRestart_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidPopulationParameterError) as context:
            elite_restart(elite_count=INVALID_COUNT)
        self.assertIn(str(INVALID_COUNT), str(context.exception))

    def test_givenPopulationErrors_whenCheckingHierarchy_thenEveryErrorIsAPopulationError(self) -> None:
        self.assertTrue(issubclass(InvalidPopulationParameterError, PopulationError))


# ---------------------------------------------------------------------------------------------------------------------
# Contrat commun aux deux sélecteurs de survivants
# ---------------------------------------------------------------------------------------------------------------------

def survivor_selectors() -> tuple[SurvivorSelector, ...]:
    return PlusSurvivorSelector(), DeathPenaltySurvivorSelector()


class TestSurvivorSelectorContract(unittest.TestCase):

    def test_givenAnySelector_whenSelect_thenReturnsATupleOfExactlySizeIndividuals(self) -> None:
        population = [evaluated_individual(label, total) for label, total in zip("ABCDE", (50, 10, 30, 20, 40))]
        for selector in survivor_selectors():
            for size in range(1, len(population) + 1):
                with self.subTest(selector=type(selector).__name__, size=size):
                    survivors = selector.select(population, size, random.Random(SEED))
                    self.assertIsInstance(survivors, tuple)
                    self.assertEqual(len(survivors), size)

    def test_givenAnySelector_whenSelect_thenSurvivorsAreObjectsOfThePopulation(self) -> None:
        population = [evaluated_individual(label, total) for label, total in zip("ABCD", (4, 3, 2, 1))]
        for selector in survivor_selectors():
            with self.subTest(selector=type(selector).__name__):
                for survivor in selector.select(population, 2, random.Random(SEED)):
                    self.assertTrue(any(survivor is individual for individual in population))

    def test_givenListPopulation_whenSelect_thenPopulationIsNotModified(self) -> None:
        for selector in survivor_selectors():
            with self.subTest(selector=type(selector).__name__):
                population = [evaluated_individual(label, total) for label, total in zip("ABCD", (4, 3, 2, 1))]
                snapshot = list(population)
                selector.select(population, 2, random.Random(SEED))
                self.assertEqual(len(population), len(snapshot))
                for before, after in zip(snapshot, population):
                    self.assertIs(before, after)

    def test_givenEmptyPopulation_whenSelect_thenRaisesEmptyPopulationError(self) -> None:
        for selector in survivor_selectors():
            with self.subTest(selector=type(selector).__name__):
                with self.assertRaises(EmptyPopulationError):
                    selector.select((), 1, random.Random(SEED))

    def test_givenUnevaluatedIndividual_whenSelect_thenRaisesUnevaluatedIndividualError(self) -> None:
        population = (evaluated_individual("A", 1), unevaluated_individual("B"))
        for selector in survivor_selectors():
            with self.subTest(selector=type(selector).__name__):
                with self.assertRaises(UnevaluatedIndividualError):
                    selector.select(population, 1, random.Random(SEED))

    def test_givenInvalidSize_whenSelect_thenRaisesInvalidSelectionParameterError(self) -> None:
        population = (evaluated_individual("A", 1),)
        for selector in survivor_selectors():
            with self.subTest(selector=type(selector).__name__):
                with self.assertRaises(InvalidSelectionParameterError):
                    selector.select(population, INVALID_COUNT, random.Random(SEED))

    def test_givenSameSeed_whenSelect_thenSameSurvivors(self) -> None:
        rng = random.Random(SEED)
        population = random_population(rng)
        size = max(1, len(population) // 2)
        for selector in survivor_selectors():
            with self.subTest(selector=type(selector).__name__):
                first = selector.select(population, size, random.Random(SEED))
                second = selector.select(population, size, random.Random(SEED))
                self.assertEqual([s.genome for s in first], [s.genome for s in second])


# ---------------------------------------------------------------------------------------------------------------------
# (μ+λ) sans doublons
# ---------------------------------------------------------------------------------------------------------------------

class TestPlusSurvivorSelector(unittest.TestCase):

    def test_givenDistinctGenomes_whenSelect_thenKeepsTheSizeBestByTotal(self) -> None:
        population = [evaluated_individual(label, total) for label, total in zip("ABCDE", (50, 10, 30, 20, 40))]
        survivors = PlusSurvivorSelector().select(population, 3, random.Random(SEED))
        self.assertEqual(totals(survivors), [10, 20, 30])
        self.assertEqual(genomes(survivors), Counter("BDC"))

    def test_givenDuplicateGenomes_whenEnoughDistinct_thenKeepsOneCopyOfEachGenome(self) -> None:
        population = [
            evaluated_individual("A", 10), evaluated_individual("A", 10),
            evaluated_individual("B", 20), evaluated_individual("C", 30), evaluated_individual("D", 40),
        ]
        survivors = PlusSurvivorSelector().select(population, 3, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter("ABC"))

    def test_givenFewerDistinctGenomesThanSize_whenSelect_thenCompletesWithDuplicatesInCostOrder(self) -> None:
        # Distincts : A (10), B (20). Il manque un survivant : le doublon le moins coûteux, A.
        population = [
            evaluated_individual("B", 20), evaluated_individual("A", 10),
            evaluated_individual("B", 20), evaluated_individual("A", 10),
        ]
        survivors = PlusSurvivorSelector().select(population, 3, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter({"A": 2, "B": 1}))

    def test_givenSingleGenomeRepeated_whenSelect_thenReturnsSizeCopies(self) -> None:
        population = [evaluated_individual("A", 10) for _ in range(4)]
        survivors = PlusSurvivorSelector().select(population, 3, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter({"A": 3}))

    def test_givenEqualCosts_whenSelect_thenEarlierIndividualInInputWins(self) -> None:
        # X et Y ont le même coût ; X vient avant Y : tri stable.
        population = [evaluated_individual("Z", 5), evaluated_individual("X", 10), evaluated_individual("Y", 10)]
        survivors = PlusSurvivorSelector().select(population, 2, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter("ZX"))

    def test_givenRandomPopulations_whenSelect_thenBestIsNeverLostAndSurvivorsAreDistinctWhenPossible(self) -> None:
        rng = random.Random(SEED)
        selector = PlusSurvivorSelector()
        for trial in range(PROPERTY_TRIALS):
            population = random_population(rng)
            size = rng.randint(1, len(population))
            with self.subTest(trial=trial):
                survivors = selector.select(population, size, rng)
                self.assertEqual(len(survivors), size)
                self.assertEqual(min(totals(survivors)), min(totals(population)), "le meilleur n'est jamais perdu")
                distinct_count = len(genomes(population))
                expected_distinct = min(size, distinct_count)
                self.assertEqual(len(genomes(survivors)), expected_distinct)

    def test_givenRandomPopulations_whenSelect_thenDistinctSurvivorsAreTheBestDistinctGenomes(self) -> None:
        rng = random.Random(SEED)
        selector = PlusSurvivorSelector()
        for trial in range(PROPERTY_TRIALS):
            population = random_population(rng)
            size = rng.randint(1, len(population))
            with self.subTest(trial=trial):
                survivors = selector.select(population, size, rng)
                best_cost_of = {}
                for individual in population:
                    best_cost_of.setdefault(individual.genome, individual.cost.total)
                distinct_costs = sorted(best_cost_of.values())
                kept_distinct_costs = sorted(
                    {survivor.genome: survivor.cost.total for survivor in survivors}.values()
                )
                expected = distinct_costs[:min(size, len(distinct_costs))]
                self.assertEqual(kept_distinct_costs, expected)


# ---------------------------------------------------------------------------------------------------------------------
# Peine de mort
# ---------------------------------------------------------------------------------------------------------------------

class TestDeathPenaltySurvivorSelector(unittest.TestCase):

    def test_givenEnoughFeasible_whenSelect_thenFeasiblePassBeforeCheaperInfeasible(self) -> None:
        population = [
            infeasible_individual("I1", 5), evaluated_individual("F1", 100),
            infeasible_individual("I2", 6), evaluated_individual("F2", 200),
        ]
        survivors = DeathPenaltySurvivorSelector().select(population, 2, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter(["F1", "F2"]))

    def test_givenMoreFeasibleThanSize_whenSelect_thenKeepsTheBestFeasible(self) -> None:
        population = [evaluated_individual(label, total) for label, total in zip("ABC", (30, 10, 20))]
        population.append(infeasible_individual("I", 1))
        survivors = DeathPenaltySurvivorSelector().select(population, 2, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter("BC"))

    def test_givenTooFewFeasible_whenSelect_thenCompletesWithTheBestInfeasible(self) -> None:
        population = [
            evaluated_individual("F1", 100),
            infeasible_individual("I1", 7), infeasible_individual("I2", 5), infeasible_individual("I3", 6),
        ]
        survivors = DeathPenaltySurvivorSelector().select(population, 3, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter(["F1", "I2", "I3"]))

    def test_givenNoFeasible_whenSelect_thenKeepsTheBestInfeasible(self) -> None:
        population = [infeasible_individual(label, total) for label, total in zip("ABC", (9, 7, 8))]
        survivors = DeathPenaltySurvivorSelector().select(population, 2, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter("BC"))

    def test_givenDuplicateFeasibleGenomes_whenSelect_thenKeepsOneCopyOfEachFeasibleGenome(self) -> None:
        population = [
            evaluated_individual("A", 10), evaluated_individual("A", 10), evaluated_individual("B", 20),
            infeasible_individual("I", 1),
        ]
        survivors = DeathPenaltySurvivorSelector().select(population, 2, random.Random(SEED))
        self.assertEqual(genomes(survivors), Counter("AB"))

    def test_givenRandomMixedPopulations_whenSelect_thenNoInfeasibleSurvivesWhileAFeasibleGenomeIsLeftOut(self) -> None:
        rng = random.Random(SEED)
        selector = DeathPenaltySurvivorSelector()
        for trial in range(PROPERTY_TRIALS):
            size = rng.randint(1, MAX_POPULATION)
            population = [
                evaluated_individual("F" + rng.choice(LABEL_POOL), 0) if rng.random() < 0.5
                else infeasible_individual("I" + rng.choice(LABEL_POOL), 0)
                for _ in range(size)
            ]
            survivor_count = rng.randint(1, len(population))
            with self.subTest(trial=trial):
                survivors = selector.select(population, survivor_count, rng)
                self.assertEqual(len(survivors), survivor_count)
                feasible_genomes = {i.genome for i in population if i.cost.is_feasible}
                kept_feasible = {s.genome for s in survivors if s.cost.is_feasible}
                some_infeasible_kept = any(not s.cost.is_feasible for s in survivors)
                if some_infeasible_kept:
                    self.assertEqual(kept_feasible, feasible_genomes, "un infaisable ne passe qu'après tous les faisables")


# ---------------------------------------------------------------------------------------------------------------------
# Stagnation du meilleur
# ---------------------------------------------------------------------------------------------------------------------

class TestStagnationCriterion(unittest.TestCase):

    def test_givenConstantBest_whenCalledEachGeneration_thenConvergesAfterExactlyGGenerationsWithoutDecrease(self) -> None:
        criterion = StagnationCriterion(generations=STAGNATION_GENERATIONS)
        population = population_with_best(10, 3)
        verdicts = [criterion.has_converged(population) for _ in range(STAGNATION_GENERATIONS + 1)]
        expected = [False] * STAGNATION_GENERATIONS + [True]
        self.assertEqual(verdicts, expected)

    def test_givenDecreasingBest_whenCalledEachGeneration_thenNeverConverges(self) -> None:
        criterion = StagnationCriterion(generations=STAGNATION_GENERATIONS)
        for step in range(IMPROVING_STEPS):
            population = population_with_best(IMPROVING_STEPS - step, 3)
            self.assertFalse(criterion.has_converged(population))

    def test_givenDecreaseDuringStagnation_whenCalled_thenCounterRestarts(self) -> None:
        criterion = StagnationCriterion(generations=STAGNATION_GENERATIONS)
        stagnant = population_with_best(10, 3)
        better = population_with_best(5, 3)
        for _ in range(STAGNATION_GENERATIONS):
            self.assertFalse(criterion.has_converged(stagnant))
        self.assertFalse(criterion.has_converged(better), "une baisse remet le compteur à zéro")
        verdicts = [criterion.has_converged(better) for _ in range(STAGNATION_GENERATIONS)]
        self.assertEqual(verdicts, [False] * (STAGNATION_GENERATIONS - 1) + [True])

    def test_givenConverged_whenReset_thenNeedsGStagnantGenerationsAgain(self) -> None:
        criterion = StagnationCriterion(generations=STAGNATION_GENERATIONS)
        population = population_with_best(10, 3)
        for _ in range(STAGNATION_GENERATIONS + 1):
            criterion.has_converged(population)
        criterion.reset()
        verdicts = [criterion.has_converged(population) for _ in range(STAGNATION_GENERATIONS + 1)]
        self.assertEqual(verdicts, [False] * STAGNATION_GENERATIONS + [True])

    def test_givenOneGeneration_whenSecondCallHasSameBest_thenConverges(self) -> None:
        criterion = StagnationCriterion(generations=1)
        population = population_with_best(10, 2)
        self.assertFalse(criterion.has_converged(population))
        self.assertTrue(criterion.has_converged(population))


# ---------------------------------------------------------------------------------------------------------------------
# Restart avec élite
# ---------------------------------------------------------------------------------------------------------------------

class TestEliteRestart(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = synthetic_instance()
        self.evaluator = CostEvaluator(self.instance)
        self.population = (
            evaluated_individual("worst", 40), evaluated_individual("best", 10),
            evaluated_individual("second", 20), evaluated_individual("third", 30),
        )

    def test_givenPopulation_whenRestart_thenSizeIsConserved(self) -> None:
        restart = EliteRestart(RecordingInitializer(), self.evaluator, ELITE_COUNT)
        self.assertEqual(len(restart.restart(self.population, random.Random(SEED))), len(self.population))

    def test_givenEliteCount_whenRestart_thenTheEliteCountBestIndividualsAreKept(self) -> None:
        restart = EliteRestart(RecordingInitializer(), self.evaluator, ELITE_COUNT)
        restarted = restart.restart(self.population, random.Random(SEED))
        for elite in (self.population[1], self.population[2]):
            self.assertTrue(any(individual is elite for individual in restarted))
        for left_out in (self.population[0], self.population[3]):
            self.assertFalse(any(individual is left_out for individual in restarted))

    def test_givenEliteCount_whenRestart_thenTheRestComesFromTheInitializerAndIsEvaluated(self) -> None:
        initializer = RecordingInitializer()
        restart = EliteRestart(initializer, self.evaluator, ELITE_COUNT)
        restarted = restart.restart(self.population, random.Random(SEED))
        self.assertEqual(initializer.requested_sizes, [len(self.population) - ELITE_COUNT])
        newcomers = [individual for individual in restarted if individual.genome == reference_genome()]
        self.assertEqual(len(newcomers), len(self.population) - ELITE_COUNT)
        for newcomer in newcomers:
            self.assertTrue(newcomer.is_evaluated())
            self.assertEqual(newcomer.cost, self.evaluator.evaluate(newcomer.horaire))

    def test_givenEliteAsLargeAsPopulation_whenRestart_thenNoNewIndividualIsRequested(self) -> None:
        initializer = RecordingInitializer()
        restart = EliteRestart(initializer, self.evaluator, len(self.population))
        restarted = restart.restart(self.population, random.Random(SEED))
        self.assertNotIn(0, initializer.requested_sizes)
        self.assertEqual(genomes(restarted), genomes(self.population))

    def test_givenEliteLargerThanPopulation_whenRestart_thenRaisesWithBothNumbersInMessage(self) -> None:
        too_large = len(self.population) + 1
        restart = EliteRestart(RecordingInitializer(), self.evaluator, too_large)
        with self.assertRaises(InvalidPopulationParameterError) as context:
            restart.restart(self.population, random.Random(SEED))
        self.assertIn(str(too_large), str(context.exception))
        self.assertIn(str(len(self.population)), str(context.exception))

    def test_givenListPopulation_whenRestart_thenPopulationIsNotModified(self) -> None:
        population = list(self.population)
        snapshot = list(population)
        EliteRestart(RecordingInitializer(), self.evaluator, ELITE_COUNT).restart(population, random.Random(SEED))
        self.assertEqual(len(population), len(snapshot))
        for before, after in zip(snapshot, population):
            self.assertIs(before, after)

    def test_givenRealInitializer_whenRestartWithSameSeed_thenSameNewcomers(self) -> None:
        restart = elite_restart(ELITE_COUNT)
        first = restart.restart(self.population, random.Random(SEED))
        second = restart.restart(self.population, random.Random(SEED))
        self.assertEqual([i.genome for i in first], [i.genome for i in second])


if __name__ == "__main__":
    unittest.main()
