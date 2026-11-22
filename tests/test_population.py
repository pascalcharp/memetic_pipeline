"""Tests de la gestion de la population (src/ga/population.py) — étape 8, Tristan.

Lancer : ``python -m unittest tests.test_population`` (sans MiniZinc).

Les individus sont construits à la main avec des coûts choisis (vrais ``Horaire`` et ``CostBreakdown``), le restart
utilise un faux ``PopulationInitializer`` et un faux évaluateur. Un vrai ``random.Random`` à graine fixée est préféré
à un mock du générateur.

Les valeurs des tests sont nommées : ``ID_*`` identifie un génome (même identifiant => même horaire => doublons),
``COST_*`` est un coût total (``COST_LOWEST`` < ... < ``COST_HIGHEST``). Les tailles attendues se déduisent des
résultats attendus plutôt que d'être écrites en dur.
"""

import random
import unittest

from src.ga.population import (
    ConvergenceCriterion,
    DeathPenaltySurvivorSelector,
    EliteRestart,
    EmptyPopulationForConvergenceError,
    InvalidPopulationParameterError,
    PlusSurvivorSelector,
    PopulationDefaults,
    PopulationError,
    RestartPolicy,
    RestartResult,
    StagnationCriterion,
    SurvivorSelector,
)
from src.ga.chromosome import BlockEncoding
from src.ga.individual import Individu
from src.ga.initialization import InitializationResult, RandomBlockInitializer
from src.memetic.local_search import LocalSearchRecord, LocalSearchResult
from src.memetic.solver import SolveOutcome, SolverStatistics
from src.ga.selection import EmptyPopulationError, InvalidSelectionParameterError, UnevaluatedIndividualError
from src.model.evaluation import CostBreakdown, CostEvaluator
from src.model.horaire import Horaire, HoraireEmploye
from tests.fixtures import cost_with_total, synthetic_instance

INVALID_COUNT: int = 0
SEED: int = 42

# Génomes (un identifiant = un horaire distinct).
ID_A: int = 1
ID_B: int = 2
ID_C: int = 3
ID_D: int = 4
ID_E: int = 5

# Coûts totaux, du meilleur au pire.
COST_LOWEST: int = 10
COST_LOW: int = 20
COST_MEDIUM: int = 30
COST_HIGH: int = 40
COST_HIGHEST: int = 50

# Population type : identifiants triés du meilleur au pire coût (voir ``mixed_population``).
IDS_BY_COST: tuple[int, ...] = (ID_B, ID_D, ID_C, ID_E, ID_A)
BEST_INDEX: int = 0
BEST_ID: int = IDS_BY_COST[BEST_INDEX]
TOP_COUNT: int = 3
SINGLE_SURVIVOR: int = 1

# Nombre de copies d'un même génome dans les populations de doublons.
DUPLICATE_COUNT: int = 3

# Les individus créés par le faux initialiseur ont des identifiants >= NEW_ID_BASE : on les distingue ainsi
# des individus de la population de départ.
NEW_ID_BASE: int = 1_000_000
NEW_ID_SPAN: int = 1_000_000
EVALUATED_TOTAL: int = 100

# Paramètres du restart.
SINGLE_ELITE: int = PopulationDefaults.MIN_RESTART_ELITE_COUNT
MULTIPLE_ELITES: int = 2
EXCESS_ELITES: int = 1
SINGLE_DISTINCT: int = 1
FIRST_CALL: int = 0

# Paramètres de la stagnation.
GENERATIONS: int = 3
ONE_GENERATION: int = PopulationDefaults.MIN_STAGNATION_GENERATIONS
REFERENCE_GENERATION: int = 1  # la 1re génération fixe la référence : elle ne compte pas comme une stagnation
DROP_GENERATION: int = 1  # une génération dont le meilleur coût baisse remet le compteur à zéro

# Décalages de l'horaire synthétique d'un génome (jalons à la suite du début).
BREAK1_OFFSET: int = 1
LUNCH_OFFSET: int = 2
BREAK2_OFFSET: int = 3
END_OFFSET: int = 4
SYNTHETIC_ACTIVITIES: tuple[int, ...] = (1, 2, 1, 2)


# ---------------------------------------------------------------------------------------------------------------------
# Faux objets et aides
# ---------------------------------------------------------------------------------------------------------------------

def distinct_horaire(genome_id: int) -> Horaire:
    """Horaire propre à ``genome_id`` (début = identifiant). Même identifiant => horaires égaux.

    ``evaluated_individual`` (fixtures) ne convient pas ici : tous ses individus ont le même horaire de référence,
    donc seraient tous des doublons pour les sélecteurs, qui dédupliquent via ``Individu.__eq__`` (horaire).
    Un ``Horaire`` ne vérifie aucune règle structurelle : celui-ci peut être infaisable, sans importance ici.
    """
    shift = HoraireEmploye(
        start=genome_id,
        break1=genome_id + BREAK1_OFFSET,
        lunch=genome_id + LUNCH_OFFSET,
        break2=genome_id + BREAK2_OFFSET,
        end=genome_id + END_OFFSET,
        activities=SYNTHETIC_ACTIVITIES,
    )
    return Horaire(employees=(shift,))


def cost_of(total: int, feasible: bool = True) -> CostBreakdown:
    """Coût de total ``total`` ; infaisable (une violation structurelle, sans pénalité) si ``feasible`` est faux."""
    if feasible:
        return cost_with_total(total)
    return CostBreakdown(
        under_coverage_cost=0,
        over_coverage_cost=total,
        quasi_hard_cells=0,
        coverage_violations=0,
        structural_violations=1,
        penalty_cost=0,
    )


def individual(genome_id: int, total: int, feasible: bool = True) -> Individu[int]:
    """Individu évalué. Même ``genome_id`` => même horaire => individus égaux (doublons)."""
    return Individu(genome=genome_id, horaire=distinct_horaire(genome_id), cost=cost_of(total, feasible))


def unevaluated_individual(genome_id: int) -> Individu[int]:
    """Individu sans coût (non évalué)."""
    return Individu(genome=genome_id, horaire=distinct_horaire(genome_id))


def mixed_population() -> list[Individu[int]]:
    """Cinq génomes distincts, dans le désordre ; triés par coût croissant : ``IDS_BY_COST``."""
    return [
        individual(ID_A, COST_HIGHEST),
        individual(ID_B, COST_LOWEST),
        individual(ID_C, COST_MEDIUM),
        individual(ID_D, COST_LOW),
        individual(ID_E, COST_HIGH),
    ]


def copies_of(genome_id: int, total: int, count: int = DUPLICATE_COUNT) -> list[Individu[int]]:
    """``count`` exemplaires du même génome (donc des doublons)."""
    return [individual(genome_id, total) for _ in range(count)]


def ids(individus) -> list[int]:
    return [individu.genome for individu in individus]


class FakeInitializer:
    """Génère ``count`` individus non évalués dont l'identifiant est tiré de ``rng`` (la consommation du
    générateur est donc observable), et une recherche locale factice par individu."""

    def __init__(self) -> None:
        self.calls: list[tuple[int, random.Random]] = []
        self.searches: list[LocalSearchRecord] = []

    def initialize(self, count: int, rng: random.Random) -> InitializationResult[int]:
        self.calls.append((count, rng))
        new_ids = [rng.randrange(NEW_ID_BASE, NEW_ID_BASE + NEW_ID_SPAN) for _ in range(count)]
        individuals = tuple(Individu(genome=i, horaire=distinct_horaire(i)) for i in new_ids)
        searches = tuple(fake_search(individu.horaire) for individu in individuals)
        self.searches.extend(searches)
        return InitializationResult(individuals=individuals, searches=searches)


def fake_search(horaire: Horaire) -> LocalSearchRecord:
    """Recherche locale factice : rend l'horaire reçu."""
    result = LocalSearchResult(
        horaire=horaire, outcome=SolveOutcome.FEASIBLE, freed_employees=frozenset(), statistics=SolverStatistics()
    )
    return LocalSearchRecord(input_horaire=horaire, result=result)


class FakeEvaluator:
    def __init__(self) -> None:
        self.evaluated: list[Horaire] = []

    def evaluate(self, horaire: Horaire) -> CostBreakdown:
        self.evaluated.append(horaire)
        return cost_with_total(EVALUATED_TOTAL)


def elite_restart(elite_count: int = PopulationDefaults.RESTART_ELITE_COUNT) -> EliteRestart:
    instance = synthetic_instance()
    return EliteRestart(RandomBlockInitializer(instance, BlockEncoding()), CostEvaluator(instance), elite_count)


def fake_elite_restart(elite_count: int) -> tuple[EliteRestart, FakeInitializer, FakeEvaluator]:
    initializer, evaluator = FakeInitializer(), FakeEvaluator()
    return EliteRestart(initializer, evaluator, elite_count), initializer, evaluator  # type: ignore[arg-type]


def feed(criterion: StagnationCriterion, totals: list[int]) -> list[bool]:
    """Une génération par coût : le meilleur de la population a ce coût. Rend le résultat de chaque génération."""
    return [criterion.has_converged([individual(ID_A, total)]) for total in totals]


def stagnation_pattern(generations: int) -> list[bool]:
    """Résultats attendus pour un coût constant : la 1re génération fixe la référence, puis la convergence arrive
    à la ``generations``-ième génération sans baisse."""
    return [False] * generations + [True]


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
        self.assertTrue(issubclass(EmptyPopulationForConvergenceError, PopulationError))


# ---------------------------------------------------------------------------------------------------------------------
# Propriétés communes aux deux sélecteurs
# ---------------------------------------------------------------------------------------------------------------------

class TestCommonSurvivorSelectors(unittest.TestCase):
    SELECTORS = (PlusSurvivorSelector, DeathPenaltySurvivorSelector)

    def setUp(self) -> None:
        self.rng = random.Random(SEED)

    def test_givenMoreIndividualsThanSize_whenSelect_thenExactlySizeReturned(self) -> None:
        population = mixed_population()
        size = len(population) - SINGLE_SURVIVOR
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                self.assertEqual(len(selector_class().select(population, size, self.rng)), size)

    def test_givenSingleSurvivor_whenSelect_thenOnlyTheBestReturned(self) -> None:
        population = mixed_population()
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                result = selector_class().select(population, SINGLE_SURVIVOR, self.rng)
                self.assertEqual(ids(result), [BEST_ID])

    def test_givenBestIsLastInInput_whenSelect_thenBestIsNeverLost(self) -> None:
        worst_first = sorted(mixed_population(), key=lambda individu: individu.cost.total, reverse=True)
        size = len(worst_first) - SINGLE_SURVIVOR
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                self.assertEqual(ids(selector_class().select(worst_first, size, self.rng))[BEST_INDEX], BEST_ID)

    def test_givenFewerDistinctGenomesThanSize_whenSelect_thenCompletedWithDuplicatesInCostOrder(self) -> None:
        # B n'existe qu'en un exemplaire : la complétion ne le répète pas (pas de cycle A, B, A, B) ; elle prend
        # les doublons écartés de A, dans l'ordre.
        population = [individual(ID_B, COST_LOW)] + copies_of(ID_A, COST_LOWEST)
        expected = [ID_A, ID_B] + [ID_A] * (DUPLICATE_COUNT - SINGLE_SURVIVOR)
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                self.assertEqual(ids(selector_class().select(population, len(expected), self.rng)), expected)

    def test_givenSingleDistinctGenome_whenSelect_thenSizeReachedWithCopiesOfIt(self) -> None:
        population = copies_of(ID_A, COST_LOWEST)
        expected = [ID_A] * DUPLICATE_COUNT
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                self.assertEqual(ids(selector_class().select(population, len(expected), self.rng)), expected)

    def test_givenSizeZero_whenSelect_thenRaisesInvalidSelectionParameterError(self) -> None:
        population = mixed_population()
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                with self.assertRaises(InvalidSelectionParameterError):
                    selector_class().select(population, INVALID_COUNT, self.rng)

    def test_givenEmptyPopulation_whenSelect_thenRaisesEmptyPopulationError(self) -> None:
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                with self.assertRaises(EmptyPopulationError):
                    selector_class().select([], SINGLE_SURVIVOR, self.rng)

    def test_givenUnevaluatedIndividual_whenSelect_thenRaisesUnevaluatedIndividualError(self) -> None:
        population = mixed_population() + [unevaluated_individual(NEW_ID_BASE)]
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                with self.assertRaises(UnevaluatedIndividualError):
                    selector_class().select(population, SINGLE_SURVIVOR, self.rng)

    def test_givenPopulation_whenSelect_thenInputIsNotModified(self) -> None:
        population = [
            individual(ID_C, COST_MEDIUM),
            individual(ID_A, COST_LOWEST),
            individual(ID_A, COST_LOWEST),
            individual(ID_B, COST_LOW),
        ]
        snapshot = list(population)
        size = len(population) - SINGLE_SURVIVOR
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                selector_class().select(population, size, self.rng)
                self.assertEqual(population, snapshot)

    def test_givenSelector_whenSelect_thenResultIsATuple(self) -> None:
        population = mixed_population()
        for selector_class in self.SELECTORS:
            with self.subTest(selector=selector_class.__name__):
                self.assertIsInstance(selector_class().select(population, TOP_COUNT, self.rng), tuple)


# ---------------------------------------------------------------------------------------------------------------------
# PlusSurvivorSelector
# ---------------------------------------------------------------------------------------------------------------------

class TestPlusSurvivorSelector(unittest.TestCase):

    def setUp(self) -> None:
        self.selector = PlusSurvivorSelector()
        self.rng = random.Random(SEED)

    def select_ids(self, population: list[Individu[int]], expected: list[int]) -> list[int]:
        """Ids des survivants quand on en demande autant que de résultats attendus."""
        return ids(self.selector.select(population, len(expected), self.rng))

    def test_givenUnorderedPopulation_whenSelect_thenKeepsBestInAscendingCostOrder(self) -> None:
        expected = list(IDS_BY_COST[:TOP_COUNT])
        self.assertEqual(self.select_ids(mixed_population(), expected), expected)

    def test_givenAdjacentDuplicates_whenSelect_thenOneCopyOfEachGenome(self) -> None:
        population = [
            individual(ID_A, COST_LOWEST),
            individual(ID_A, COST_LOWEST),
            individual(ID_B, COST_LOW),
            individual(ID_C, COST_MEDIUM),
        ]
        expected = [ID_A, ID_B, ID_C]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenNonAdjacentDuplicates_whenSelect_thenOneCopyOfEachGenome(self) -> None:
        # Mêmes coûts : le tri stable garde l'ordre d'entrée A, B, A ; le doublon n'est pas adjacent.
        population = [individual(ID_A, COST_LOWEST), individual(ID_B, COST_LOWEST), individual(ID_A, COST_LOWEST)]
        expected = [ID_A, ID_B]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenEqualCosts_whenSelect_thenTiesBrokenByInputOrder(self) -> None:
        population = [individual(ID_C, COST_MEDIUM), individual(ID_A, COST_MEDIUM), individual(ID_B, COST_MEDIUM)]
        expected = [ID_C, ID_A]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenInfeasibleIndividuals_whenSelect_thenFeasibilityIsIgnored(self) -> None:
        population = [
            individual(ID_A, COST_HIGH),
            individual(ID_B, COST_LOWEST, feasible=False),
            individual(ID_C, COST_MEDIUM),
        ]
        expected = [ID_B, ID_C]
        self.assertEqual(self.select_ids(population, expected), expected)


# ---------------------------------------------------------------------------------------------------------------------
# DeathPenaltySurvivorSelector
# ---------------------------------------------------------------------------------------------------------------------

class TestDeathPenaltySurvivorSelector(unittest.TestCase):

    def setUp(self) -> None:
        self.selector = DeathPenaltySurvivorSelector()
        self.rng = random.Random(SEED)

    def select_ids(self, population: list[Individu[int]], expected: list[int]) -> list[int]:
        """Ids des survivants quand on en demande autant que de résultats attendus."""
        return ids(self.selector.select(population, len(expected), self.rng))

    def test_givenCheaperInfeasible_whenSelect_thenAllFeasibleComeFirst(self) -> None:
        population = [
            individual(ID_A, COST_LOWEST, feasible=False),
            individual(ID_B, COST_HIGHEST),
            individual(ID_C, COST_HIGH),
        ]
        expected = [ID_C, ID_B]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenEnoughFeasible_whenSelect_thenNoInfeasibleSelected(self) -> None:
        population = [
            individual(ID_A, COST_LOWEST, feasible=False),
            individual(ID_B, COST_HIGHEST),
            individual(ID_C, COST_HIGH),
            individual(ID_D, COST_MEDIUM),
        ]
        expected = [ID_D, ID_C, ID_B]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenTooFewFeasible_whenSelect_thenCompletedWithBestInfeasible(self) -> None:
        population = [
            individual(ID_A, COST_HIGHEST),
            individual(ID_B, COST_MEDIUM, feasible=False),
            individual(ID_C, COST_LOWEST, feasible=False),
            individual(ID_D, COST_LOW, feasible=False),
        ]
        expected = [ID_A, ID_C, ID_D]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenNoFeasible_whenSelect_thenBestInfeasibleSelected(self) -> None:
        population = [
            individual(ID_A, COST_MEDIUM, feasible=False),
            individual(ID_B, COST_LOWEST, feasible=False),
            individual(ID_C, COST_LOW, feasible=False),
        ]
        expected = [ID_B, ID_C]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenFeasibleDuplicates_whenSelect_thenOneCopyOfEachGenome(self) -> None:
        population = [
            individual(ID_A, COST_LOWEST),
            individual(ID_B, COST_LOW),
            individual(ID_A, COST_LOWEST),
            individual(ID_C, COST_MEDIUM),
        ]
        expected = [ID_A, ID_B, ID_C]
        self.assertEqual(self.select_ids(population, expected), expected)

    def test_givenFewerDistinctGenomes_whenSelect_thenInfeasibleDistinctBeforeFeasibleDuplicate(self) -> None:
        # Ordre de complétion : faisables distincts, infaisables distincts, puis doublons.
        population = [
            individual(ID_A, COST_LOWEST),
            individual(ID_B, COST_LOW, feasible=False),
            individual(ID_A, COST_LOWEST),
        ]
        expected = [ID_A, ID_B, ID_A]
        self.assertEqual(self.select_ids(population, expected), expected)


# ---------------------------------------------------------------------------------------------------------------------
# StagnationCriterion
# ---------------------------------------------------------------------------------------------------------------------

class TestStagnationCriterion(unittest.TestCase):

    def test_givenCostKeepsDecreasing_whenHasConverged_thenAlwaysFalse(self) -> None:
        totals = [COST_HIGHEST, COST_HIGH, COST_MEDIUM, COST_LOW, COST_LOWEST]
        results = feed(StagnationCriterion(generations=ONE_GENERATION), totals)
        self.assertEqual(results, [False] * len(totals))

    def test_givenCostStagnates_whenHasConverged_thenTrueAfterExactlyGenerationsWithoutDrop(self) -> None:
        totals = [COST_MEDIUM] * (GENERATIONS + REFERENCE_GENERATION)
        self.assertEqual(feed(StagnationCriterion(generations=GENERATIONS), totals), stagnation_pattern(GENERATIONS))

    def test_givenMinimumGenerations_whenNextGenerationDoesNotDrop_thenConverged(self) -> None:
        totals = [COST_MEDIUM] * (ONE_GENERATION + REFERENCE_GENERATION)
        self.assertEqual(
            feed(StagnationCriterion(generations=ONE_GENERATION), totals), stagnation_pattern(ONE_GENERATION)
        )

    def test_givenDropAfterStagnation_whenHasConverged_thenCounterRestartsFromZero(self) -> None:
        # GENERATIONS générations au coût élevé (aucune ne converge), puis une baisse remet le compteur à zéro :
        # il faut encore GENERATIONS générations sans baisse pour converger.
        totals = [COST_HIGH] * GENERATIONS + [COST_MEDIUM] * (DROP_GENERATION + GENERATIONS)
        *earlier_results, last_result = feed(StagnationCriterion(generations=GENERATIONS), totals)
        self.assertFalse(any(earlier_results))
        self.assertTrue(last_result)

    def test_givenCostIncreases_whenHasConverged_thenCountsAsNoDrop(self) -> None:
        totals = [COST_LOW, COST_MEDIUM, COST_HIGH]
        generations = len(totals) - REFERENCE_GENERATION
        self.assertEqual(feed(StagnationCriterion(generations=generations), totals), stagnation_pattern(generations))

    def test_givenPopulationWithSeveralIndividuals_whenHasConverged_thenBestCostIsTracked(self) -> None:
        criterion = StagnationCriterion(generations=ONE_GENERATION)
        criterion.has_converged([individual(ID_A, COST_HIGH), individual(ID_B, COST_LOW)])
        # Le meilleur passe de COST_LOW à COST_LOWEST : baisse, donc pas de convergence
        # (le 1er individu seul resterait à COST_HIGH).
        self.assertFalse(criterion.has_converged([individual(ID_A, COST_HIGH), individual(ID_B, COST_LOWEST)]))

    def test_givenEmptyPopulation_whenHasConverged_thenRaisesEmptyPopulationForConvergenceError(self) -> None:
        with self.assertRaises(EmptyPopulationForConvergenceError):
            StagnationCriterion().has_converged([])

    def test_givenConverged_whenReset_thenCounterStartsOverFromZero(self) -> None:
        criterion = StagnationCriterion(generations=GENERATIONS)
        totals = [COST_MEDIUM] * (GENERATIONS + REFERENCE_GENERATION)
        self.assertEqual(feed(criterion, totals), stagnation_pattern(GENERATIONS))
        criterion.reset()
        self.assertEqual(feed(criterion, totals), stagnation_pattern(GENERATIONS))

    def test_givenReset_whenCostIsHigherThanBefore_thenNewReferenceIsUsed(self) -> None:
        criterion = StagnationCriterion(generations=GENERATIONS)
        feed(criterion, [COST_LOWEST])
        criterion.reset()
        # Sans reset, COST_HIGHEST compterait comme une non-baisse ; après reset, c'est la nouvelle référence.
        # Séquence : référence, baisse (compteur à zéro), puis GENERATIONS générations sans baisse.
        totals = [COST_HIGHEST] + [COST_HIGH] * (DROP_GENERATION + GENERATIONS)
        self.assertEqual(feed(criterion, totals), stagnation_pattern(DROP_GENERATION + GENERATIONS))


# ---------------------------------------------------------------------------------------------------------------------
# EliteRestart
# ---------------------------------------------------------------------------------------------------------------------

class TestEliteRestart(unittest.TestCase):

    def setUp(self) -> None:
        self.rng = random.Random(SEED)
        self.population = mixed_population()

    def test_givenPopulation_whenRestart_thenSizeIsKept(self) -> None:
        restart, _, _ = fake_elite_restart(MULTIPLE_ELITES)
        self.assertEqual(len(restart.restart(self.population, self.rng).population), len(self.population))

    def test_givenSingleElite_whenRestart_thenBestIndividualIsKept(self) -> None:
        restart, _, _ = fake_elite_restart(SINGLE_ELITE)
        self.assertEqual(ids(restart.restart(self.population, self.rng).population)[:SINGLE_ELITE], list(IDS_BY_COST[:SINGLE_ELITE]))

    def test_givenMultipleElites_whenRestart_thenBestAreKeptInCostOrder(self) -> None:
        restart, _, _ = fake_elite_restart(MULTIPLE_ELITES)
        result = restart.restart(self.population, self.rng).population
        self.assertEqual(ids(result)[:MULTIPLE_ELITES], list(IDS_BY_COST[:MULTIPLE_ELITES]))

    def test_givenEliteInPopulation_whenRestart_thenElitesKeepTheirCost(self) -> None:
        restart, _, _ = fake_elite_restart(SINGLE_ELITE)
        best = restart.restart(self.population, self.rng).population[BEST_INDEX]
        self.assertEqual(best.cost.total, COST_LOWEST)

    def test_givenDuplicateElites_whenRestart_thenOneCopyKeptAndSizeIsKept(self) -> None:
        # Pas de complément de l'élite par des doublons : A n'est gardé qu'une fois, le reste est régénéré.
        population = [
            individual(ID_A, COST_LOWEST),
            individual(ID_A, COST_LOWEST),
            individual(ID_B, COST_LOW),
            individual(ID_C, COST_MEDIUM),
        ]
        restart, _, _ = fake_elite_restart(MULTIPLE_ELITES)
        result = restart.restart(population, self.rng).population
        self.assertEqual(ids(result)[:MULTIPLE_ELITES], [ID_A, ID_B])
        self.assertEqual(len(result), len(population))

    def test_givenFewerDistinctGenomesThanEliteCount_whenRestart_thenRestRegenerated(self) -> None:
        population = copies_of(ID_A, COST_LOWEST)
        restart, initializer, _ = fake_elite_restart(len(population))
        result = restart.restart(population, self.rng).population
        self.assertEqual(ids(result)[:SINGLE_DISTINCT], [ID_A])
        self.assertEqual([count for count, _ in initializer.calls], [len(population) - SINGLE_DISTINCT])
        self.assertEqual(len(result), len(population))

    def test_givenRestart_whenCalled_thenInitializerGeneratesTheRest(self) -> None:
        restart, initializer, _ = fake_elite_restart(MULTIPLE_ELITES)
        result = restart.restart(self.population, self.rng).population
        self.assertEqual([count for count, _ in initializer.calls], [len(self.population) - MULTIPLE_ELITES])
        self.assertTrue(all(genome_id >= NEW_ID_BASE for genome_id in ids(result[MULTIPLE_ELITES:])))

    def test_givenRestart_whenCalled_thenNewIndividualsAreEvaluated(self) -> None:
        restart, _, evaluator = fake_elite_restart(MULTIPLE_ELITES)
        new_individuals = restart.restart(self.population, self.rng).population[MULTIPLE_ELITES:]
        self.assertTrue(all(individu.is_evaluated() for individu in new_individuals))
        self.assertEqual(
            [individu.cost.total for individu in new_individuals], [EVALUATED_TOTAL] * len(new_individuals)
        )
        self.assertEqual(evaluator.evaluated, [individu.horaire for individu in new_individuals])

    def test_givenSeededRng_whenRestart_thenInitializerConsumesThatGenerator(self) -> None:
        restart, initializer, _ = fake_elite_restart(SINGLE_ELITE)
        result = restart.restart(self.population, self.rng).population
        expected_rng = random.Random(SEED)
        expected_ids = [
            expected_rng.randrange(NEW_ID_BASE, NEW_ID_BASE + NEW_ID_SPAN)
            for _ in range(len(self.population) - SINGLE_ELITE)
        ]
        self.assertEqual(ids(result)[SINGLE_ELITE:], expected_ids)
        _, used_rng = initializer.calls[FIRST_CALL]
        self.assertIs(used_rng, self.rng)

    def test_givenEliteEqualToPopulationSize_whenRestart_thenNothingIsRegenerated(self) -> None:
        restart, initializer, _ = fake_elite_restart(len(self.population))
        result = restart.restart(self.population, self.rng).population
        # Le restart rend l'élite triée par coût croissant, pas dans l'ordre d'entrée.
        self.assertEqual(ids(result), list(IDS_BY_COST))
        self.assertEqual(initializer.calls, [])

    def test_givenEliteLargerThanPopulation_whenRestart_thenRaisesWithSizesInMessage(self) -> None:
        elite_count = len(self.population) + EXCESS_ELITES
        restart, _, _ = fake_elite_restart(elite_count)
        with self.assertRaises(InvalidPopulationParameterError) as context:
            restart.restart(self.population, self.rng)
        self.assertIn(str(elite_count), str(context.exception))
        self.assertIn(str(len(self.population)), str(context.exception))

    def test_givenEmptyPopulation_whenRestart_thenRaisesInvalidPopulationParameterError(self) -> None:
        # elite_count vaut au moins 1 : il dépasse toujours la taille d'une population vide.
        restart, _, _ = fake_elite_restart(SINGLE_ELITE)
        with self.assertRaises(InvalidPopulationParameterError):
            restart.restart([], self.rng)

    def test_givenPopulation_whenRestart_thenInputIsNotModified(self) -> None:
        restart, _, _ = fake_elite_restart(MULTIPLE_ELITES)
        snapshot = list(self.population)
        totals_before = [individu.cost.total for individu in self.population]
        restart.restart(self.population, self.rng)
        self.assertEqual(self.population, snapshot)
        self.assertEqual([individu.cost.total for individu in self.population], totals_before)

    def test_givenRestart_whenCalled_thenResultSeparatesEliteAndNewcomers(self) -> None:
        restart, _, _ = fake_elite_restart(MULTIPLE_ELITES)
        result = restart.restart(self.population, self.rng)
        self.assertIsInstance(result, RestartResult)
        self.assertEqual(ids(result.elite), list(IDS_BY_COST[:MULTIPLE_ELITES]))
        self.assertEqual(len(result.newcomers), len(self.population) - MULTIPLE_ELITES)
        self.assertEqual(result.population, result.elite + result.newcomers)
        self.assertIsInstance(result.population, tuple)

    def test_givenInitializerWithSearches_whenRestart_thenSearchesArePassedOn(self) -> None:
        restart, initializer, _ = fake_elite_restart(MULTIPLE_ELITES)
        result = restart.restart(self.population, self.rng)
        self.assertEqual(result.searches, tuple(initializer.searches))
        self.assertEqual(len(result.searches), len(result.newcomers))

    def test_givenEliteEqualToPopulationSize_whenRestart_thenNoNewcomerAndNoSearch(self) -> None:
        restart, _, _ = fake_elite_restart(len(self.population))
        result = restart.restart(self.population, self.rng)
        self.assertEqual(result.newcomers, ())
        self.assertEqual(result.searches, ())


if __name__ == "__main__":
    unittest.main()