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
)
from tests.fixtures import evaluated_individual
from tests.test_feasibility import REFERENCE_SHIFT, single

POPULATION_TOTALS: tuple[int, ...] = (30, 10, 20)


def population() -> tuple[Individu[int], ...]:
    """Trois individus évalués ; le génome est l'indice de l'individu, pour le reconnaître."""
    return tuple(evaluated_individual(index, total) for index, total in enumerate(POPULATION_TOTALS))


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
        unevaluated = Individu(genome=99, horaire=single(REFERENCE_SHIFT))
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


if __name__ == "__main__":
    unittest.main()
