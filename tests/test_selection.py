"""Tests de la sélection (src/ga/selection.py) — étape 7a, Tristan.

Sur ``main`` : tests du scaffold (verts), dont la vérification commune ``check_selectable``. Cas à couvrir sur la
branche ``etape-7a-selection`` (voir TODO.md, 7a), sans MiniZinc, avec ``evaluated_individual`` (tests/fixtures.py) :
    - ``select(population, count, rng)`` rend exactement ``count`` individus, tous issus de la population ;
    - tournoi : le meilleur gagne un tournoi qui couvre toute la population (taille grande, graine fixée) ;
      sur beaucoup de tirages, un individu meilleur est tiré plus souvent qu'un moins bon ;
    - tournoi de taille 1 et ``UniformMutableSelector`` : chaque individu finit par être tiré ;
    - population d'un seul individu ; individus de même coût ;
    - population vide, non évaluée, ``count`` invalide ⇒ exception (via ``check_selectable``) ;
    - reproductibilité : même graine ⇒ mêmes tirages ; la population n'est jamais modifiée.
"""

import unittest
import random
from collections.abc import Sequence
from collections import Counter
from src.ga.individual import Individu
from src.ga.selection import (
    EmptyPopulationError,
    InvalidSelectionParameterError,
    MutableSelector,
    ParentSelector,
    SelectionDefaults,
    TournamentSelector,
    UnevaluatedIndividualError,
    check_selectable,
    UniformMutableSelector
)
from tests.fixtures import evaluated_individual
from tests.test_feasibility import REFERENCE_SHIFT, single

POPULATION_TOTALS: tuple[int, ...] = (30, 10, 20)
SEED: int = 42
DRAW_COUNT: int = 3000
LARGE_TOURNAMENT_SIZE: int = 100
BEST_GENOME: int = POPULATION_TOTALS.index(min(POPULATION_TOTALS))
MIDDLE_GENOME: int = POPULATION_TOTALS.index(20)
WORST_GENOME: int = POPULATION_TOTALS.index(max(POPULATION_TOTALS))
UNEVALUATED_GENOME: int = 99
TIED_TOTAL: int = 10
TIED_COUNT: int = 3


def population() -> tuple[Individu[int], ...]:
    """Trois individus évalués ; le génome est l'indice de l'individu, pour le reconnaître."""
    return tuple(evaluated_individual(index, total) for index, total in enumerate(POPULATION_TOTALS))


def unevaluated_individual() -> Individu[int]:
    """Individu sans coût, qui doit faire lever ``UnevaluatedIndividualError``."""
    return Individu(genome=UNEVALUATED_GENOME, horaire=single(REFERENCE_SHIFT))


def tied_population() -> tuple[Individu[int], ...]:
    """Individus de même coût ; le génome est l'indice de l'individu, pour le reconnaître."""
    return tuple(evaluated_individual(index, TIED_TOTAL) for index in range(TIED_COUNT))


class TestCheckSelectable(unittest.TestCase):

    def test_valid_population(self) -> None:
        check_selectable(population(), count=1)

    def test_invalid_count(self) -> None:
        with self.assertRaises(InvalidSelectionParameterError) as context:
            check_selectable(population(), count=0)
        self.assertIn("0", str(context.exception))

    def test_empty_population(self) -> None:
        with self.assertRaises(EmptyPopulationError):
            check_selectable((), count=1)

    def test_unevaluated_individual_is_located(self) -> None:
        unevaluated = unevaluated_individual()
        with self.assertRaises(UnevaluatedIndividualError) as context:
            check_selectable(population() + (unevaluated,), count=1)
        self.assertIn(str(len(POPULATION_TOTALS)), str(context.exception))


class TestScaffoldContract(unittest.TestCase):

    def test_interfaces_are_abstract(self) -> None:
        for interface in (ParentSelector, MutableSelector):
            with self.subTest(interface=interface.__name__):
                with self.assertRaises(TypeError):
                    interface()  # type: ignore[abstract]

    def test_tournament_default_size(self) -> None:
        self.assertEqual(TournamentSelector().size, SelectionDefaults.TOURNAMENT_SIZE)

    def test_tournament_size_must_be_positive(self) -> None:
        with self.assertRaises(InvalidSelectionParameterError) as context:
            TournamentSelector(size=0)
        self.assertIn("0", str(context.exception))


def genomes(selection: tuple[Individu[int], ...]) -> list[int]:
    return [individual.genome for individual in selection]


def selectors() -> tuple[ParentSelector[int] | MutableSelector[int], ...]:
    return TournamentSelector(), UniformMutableSelector()


class TestSelectionContract(unittest.TestCase):

    def test_givenAnySelector_whenSelect_thenReturnsExactlyCountIndividualsInATuple(self) -> None:
        for selector in selectors():
            with self.subTest(selector=type(selector).__name__):
                selection = selector.select(population(), 5, random.Random(SEED))
                self.assertIsInstance(selection, tuple)
                self.assertEqual(len(selection), 5)

    def test_givenAnySelector_whenSelect_thenAllIndividualsComeFromPopulation(self) -> None:
        source = population()
        for selector in selectors():
            with self.subTest(selector=type(selector).__name__):
                selection = selector.select(source, DRAW_COUNT, random.Random(SEED))
                for individual in selection:
                    self.assertTrue(any(individual is candidate for candidate in source))

    def test_givenCountLargerThanPopulation_whenSelect_thenSelectsWithReplacement(self) -> None:
        for selector in selectors():
            with self.subTest(selector=type(selector).__name__):
                selection = selector.select(population(), DRAW_COUNT, random.Random(SEED))
                self.assertEqual(len(selection), DRAW_COUNT)

    def test_givenSingleIndividualPopulation_whenSelect_thenAlwaysReturnsThatIndividual(self) -> None:
        only = evaluated_individual(0, 10)
        for selector in selectors():
            with self.subTest(selector=type(selector).__name__):
                selection = selector.select((only,), 4, random.Random(SEED))
                self.assertEqual(len(selection), 4)
                for individual in selection:
                    self.assertIs(individual, only)

    def test_givenListPopulation_whenSelect_thenPopulationIsNotModified(self) -> None:
        for selector in selectors():
            with self.subTest(selector=type(selector).__name__):
                source = list(population())
                snapshot = list(source)
                selector.select(source, 10, random.Random(SEED))
                self.assertEqual(len(source), len(snapshot))
                for before, after in zip(snapshot, source):
                    self.assertIs(before, after)
                self.assertEqual([i.cost.total for i in source], list(POPULATION_TOTALS))


class TestSelectionErrors(unittest.TestCase):

    def test_givenEmptyPopulation_whenSelect_thenRaisesEmptyPopulationError(self) -> None:
        for selector in selectors():
            with self.subTest(selector=type(selector).__name__):
                with self.assertRaises(EmptyPopulationError):
                    selector.select((), 1, random.Random(SEED))

    def test_givenUnevaluatedIndividual_whenSelect_thenRaisesUnevaluatedIndividualError(self) -> None:
        unevaluated = unevaluated_individual()
        for selector in selectors():
            with self.subTest(selector=type(selector).__name__):
                with self.assertRaises(UnevaluatedIndividualError):
                    selector.select(population() + (unevaluated,), 1, random.Random(SEED))

    def test_givenInvalidCount_whenSelect_thenRaisesInvalidSelectionParameterError(self) -> None:
        for selector in selectors():
            for count in (0, -1):
                with self.subTest(selector=type(selector).__name__, count=count):
                    with self.assertRaises(InvalidSelectionParameterError):
                        selector.select(population(), count, random.Random(SEED))


class TestTournamentSelector(unittest.TestCase):

    def test_givenTournamentCoveringWholePopulation_whenSelect_thenBestAlwaysWins(self) -> None:
        selector = TournamentSelector(size=LARGE_TOURNAMENT_SIZE)
        selection = selector.select(population(), 20, random.Random(SEED))
        self.assertEqual(genomes(selection), [BEST_GENOME] * 20)

    def test_givenTournamentOfSizeTwo_whenManyDraws_thenBetterIndividualsAreDrawnMoreOften(self) -> None:
        selection = TournamentSelector(size=2).select(population(), DRAW_COUNT, random.Random(SEED))
        drawn = Counter(genomes(selection))
        self.assertGreater(drawn[BEST_GENOME], drawn[MIDDLE_GENOME])
        self.assertGreater(drawn[MIDDLE_GENOME], drawn[WORST_GENOME])
        self.assertGreater(drawn[WORST_GENOME], 0)

    def test_givenTournamentOfSizeOne_whenManyDraws_thenEveryIndividualIsDrawn(self) -> None:
        selection = TournamentSelector(size=1).select(population(), DRAW_COUNT, random.Random(SEED))
        self.assertEqual(set(genomes(selection)), set(range(len(POPULATION_TOTALS))))

    def test_givenEqualCosts_whenSelect_thenSelectsFromPopulationWithoutError(self) -> None:
        tied = tied_population()
        selection = TournamentSelector(size=2).select(tied, DRAW_COUNT, random.Random(SEED))
        self.assertEqual(len(selection), DRAW_COUNT)
        self.assertEqual(set(genomes(selection)), set(range(TIED_COUNT)))

    def test_givenFixedSeed_whenSelect_thenMatchesHandRecordedWinners(self) -> None:
        # Valeur calculée une fois avec random.Random(SEED), tournois de taille 2, coûts (30, 10, 20).
        expected = [1, 0, 2, 2, 1, 1, 0, 1, 1, 2]
        selection = TournamentSelector(size=2).select(population(), 10, random.Random(SEED))
        self.assertEqual(genomes(selection), expected)

    def test_givenTournamentOfSizeOne_whenSelect_thenMatchesIndependentUniformDraw(self) -> None:
        expected = random.Random(SEED).choices(range(len(POPULATION_TOTALS)), k=10)
        selection = TournamentSelector(size=1).select(population(), 10, random.Random(SEED))
        self.assertEqual(genomes(selection), expected)


class TestUniformMutableSelector(unittest.TestCase):

    def test_givenManyDraws_whenSelect_thenEveryIndividualIsDrawn(self) -> None:
        selection = UniformMutableSelector().select(population(), DRAW_COUNT, random.Random(SEED))
        self.assertEqual(set(genomes(selection)), set(range(len(POPULATION_TOTALS))))

    def test_givenManyDraws_whenSelect_thenCostIsIgnored(self) -> None:
        selection = UniformMutableSelector().select(population(), DRAW_COUNT, random.Random(SEED))
        drawn = Counter(genomes(selection))
        expected_share = DRAW_COUNT / len(POPULATION_TOTALS)
        for genome in range(len(POPULATION_TOTALS)):
            self.assertAlmostEqual(drawn[genome], expected_share, delta=expected_share * 0.15)

    def test_givenFixedSeed_whenSelect_thenMatchesIndependentUniformDraw(self) -> None:
        expected = random.Random(SEED).choices(range(len(POPULATION_TOTALS)), k=10)
        selection = UniformMutableSelector().select(population(), 10, random.Random(SEED))
        self.assertEqual(genomes(selection), expected)


class ScriptedRandom(random.Random):
    """RNG dont chaque appel à ``choices`` rend le tirage écrit d'avance (indices dans la population)."""

    def __init__(self, *draws: Sequence[int]) -> None:
        super().__init__()
        self.draws: list[Sequence[int]] = list(draws)
        self.requested_sizes: list[int] = []

    def choices(self, population, weights=None, *, cum_weights=None, k=1):  # type: ignore[override]
        indices = self.draws.pop(0)
        assert len(indices) == k, f"tirage écrit de taille {len(indices)}, mais k={k} demandé"
        self.requested_sizes.append(k)
        return [population[index] for index in indices]


# Coûts de population() : génome 0 -> 30, génome 1 -> 10 (meilleur), génome 2 -> 20.
ALL_ORDERED_PAIRS: tuple[tuple[int, int], ...] = tuple((i, j) for i in range(3) for j in range(3))
WINNERS_OF_ALL_ORDERED_PAIRS: list[int] = [0, 1, 2, 1, 1, 1, 2, 1, 2]


class TestTournamentHandCrafted(unittest.TestCase):

    def test_givenDrawnCandidates_whenSelect_thenLowestCostAmongDrawnWins(self) -> None:
        rng = ScriptedRandom((0, 2))
        selection = TournamentSelector(size=2).select(population(), 1, rng)
        self.assertEqual(genomes(selection), [2])  # 20 < 30

    def test_givenBestIndividualNotDrawn_whenSelect_thenItCannotWin(self) -> None:
        rng = ScriptedRandom((0, 2))  # le génome 1 (coût 10) n'est pas dans le tournoi
        selection = TournamentSelector(size=2).select(population(), 1, rng)
        self.assertNotIn(BEST_GENOME, genomes(selection))

    def test_givenBestIndividualDrawnAmongOthers_whenSelect_thenBestWins(self) -> None:
        rng = ScriptedRandom((0, 1, 2))
        selection = TournamentSelector(size=3).select(population(), 1, rng)
        self.assertEqual(genomes(selection), [BEST_GENOME])

    def test_givenSeveralParents_whenSelect_thenEachParentHasItsOwnTournament(self) -> None:
        rng = ScriptedRandom((0, 2), (0, 1), (2, 2))
        selection = TournamentSelector(size=2).select(population(), 3, rng)
        self.assertEqual(genomes(selection), [2, 1, 2])

    def test_givenSameIndividualDrawnTwice_whenSelect_thenItWinsItsOwnTournament(self) -> None:
        rng = ScriptedRandom((0, 0))
        selection = TournamentSelector(size=2).select(population(), 1, rng)
        self.assertEqual(genomes(selection), [0])

    def test_givenEqualCosts_whenSelect_thenFirstDrawnCandidateWins(self) -> None:
        tied = tied_population()
        rng = ScriptedRandom((2, 0, 1))  # suppose TIED_COUNT >= 3
        selection = TournamentSelector(size=3).select(tied, 1, rng)
        self.assertEqual(genomes(selection), [2])

    def test_givenSizeAndCount_whenSelect_thenOneTournamentOfSizeCandidatesPerParent(self) -> None:
        rng = ScriptedRandom((0, 1, 2), (2, 1, 0))
        TournamentSelector(size=3).select(population(), 2, rng)
        self.assertEqual(rng.requested_sizes, [3, 3])

    def test_givenEveryOrderedPairDrawnOnce_whenSelectSizeTwo_thenWinnersMatchHandComputedTable(self) -> None:
        rng = ScriptedRandom(*ALL_ORDERED_PAIRS)
        selection = TournamentSelector(size=2).select(population(), len(ALL_ORDERED_PAIRS), rng)
        self.assertEqual(genomes(selection), WINNERS_OF_ALL_ORDERED_PAIRS)

    def test_givenEveryOrderedPairDrawnOnce_whenSelectSizeTwo_thenWinCountsAreFiveThreeOne(self) -> None:
        rng = ScriptedRandom(*ALL_ORDERED_PAIRS)
        selection = TournamentSelector(size=2).select(population(), len(ALL_ORDERED_PAIRS), rng)
        drawn = Counter(genomes(selection))
        self.assertEqual((drawn[BEST_GENOME], drawn[MIDDLE_GENOME], drawn[WORST_GENOME]), (5, 3, 1))


class TestUniformMutableSelectorHandCrafted(unittest.TestCase):

    def test_givenScriptedDraw_whenSelect_thenReturnsDrawnIndividualsInOrder(self) -> None:
        rng = ScriptedRandom((2, 2, 0, 1))
        selection = UniformMutableSelector().select(population(), 4, rng)
        self.assertEqual(genomes(selection), [2, 2, 0, 1])

    def test_givenWorstIndividualDrawn_whenSelect_thenItIsKeptDespiteItsCost(self) -> None:
        rng = ScriptedRandom((WORST_GENOME, WORST_GENOME))
        selection = UniformMutableSelector().select(population(), 2, rng)
        self.assertEqual(genomes(selection), [WORST_GENOME, WORST_GENOME])

    def test_givenScriptedDraw_whenSelect_thenReturnsTheSamePopulationObjects(self) -> None:
        source = population()
        selection = UniformMutableSelector().select(source, 2, ScriptedRandom((1, 0)))
        self.assertIs(selection[0], source[1])
        self.assertIs(selection[1], source[0])


if __name__ == "__main__":
    unittest.main()