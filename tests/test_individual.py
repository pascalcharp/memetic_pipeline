"""Tests de l'individu (src/ga/individual.py), avec un encodage factice indépendant de BlockEncoding."""

import dataclasses
import unittest

from src.ga.chromosome import Encoding
from src.ga.individual import Individu
from src.model.horaire import Horaire, HoraireEmploye

# Génome factice : le numéro de début de chaque employé ; le reste du quart est fixé.
type StartGenome = tuple[int, ...]

FIXED_ACTIVITIES: tuple[int, ...] = (1, 1, 1, 1)
GENOME: StartGenome = (1, 4, 5)
COST: int = 94


class StartOnlyEncoding(Encoding[StartGenome]):
    """Encodage factice : un quart de forme fixe, décalé selon le début. Compte les appels à ``decode``."""

    def __init__(self) -> None:
        self.decode_calls = 0

    def encode(self, horaire: Horaire) -> StartGenome:
        return tuple(shift.start for shift in horaire.employees)

    def decode(self, genome: StartGenome) -> Horaire:
        self.decode_calls += 1
        return Horaire(
            employees=tuple(
                HoraireEmploye(
                    start=start,
                    break1=start + 4,
                    lunch=start + 9,
                    break2=start + 19,
                    end=start + 27,
                    activities=FIXED_ACTIVITIES,
                )
                for start in genome
            )
        )


class TestFromGenome(unittest.TestCase):
    """Construction d'un individu à partir d'un génome."""

    def setUp(self) -> None:
        self.encoding = StartOnlyEncoding()
        self.individual = Individu.from_genome(GENOME, self.encoding)

    def test_horaire_is_the_decoded_genome(self) -> None:
        self.assertEqual(self.individual.genome, GENOME)
        self.assertEqual(self.individual.horaire, self.encoding.decode(GENOME))

    def test_genome_is_decoded_once_at_construction(self) -> None:
        self.assertEqual(self.encoding.decode_calls, 1)
        _ = self.individual.horaire
        _ = self.individual.horaire
        self.assertEqual(self.encoding.decode_calls, 1)

    def test_new_individual_is_not_evaluated(self) -> None:
        self.assertIsNone(self.individual.cost)
        self.assertFalse(self.individual.is_evaluated())


class TestWithCost(unittest.TestCase):
    """L'évaluation retourne un nouvel individu ; l'original n'est jamais modifié (D7)."""

    def setUp(self) -> None:
        self.individual = Individu.from_genome(GENOME, StartOnlyEncoding())

    def test_with_cost_returns_an_evaluated_copy(self) -> None:
        evaluated = self.individual.with_cost(COST)
        self.assertEqual(evaluated.cost, COST)
        self.assertTrue(evaluated.is_evaluated())
        self.assertEqual(evaluated.genome, self.individual.genome)
        self.assertEqual(evaluated.horaire, self.individual.horaire)

    def test_original_is_unchanged(self) -> None:
        self.individual.with_cost(COST)
        self.assertIsNone(self.individual.cost)

    def test_zero_cost_counts_as_evaluated(self) -> None:
        # Un coût nul est un vrai coût (solution parfaite), pas l'absence d'évaluation.
        self.assertTrue(self.individual.with_cost(0).is_evaluated())

    def test_is_frozen(self) -> None:
        with self.assertRaises(dataclasses.FrozenInstanceError):
            self.individual.cost = COST  # type: ignore[misc]


class TestEquality(unittest.TestCase):
    """Deux individus se comparent par valeur : génome, horaire et coût."""

    def test_same_genome_and_cost_are_equal(self) -> None:
        first = Individu.from_genome(GENOME, StartOnlyEncoding())
        second = Individu.from_genome(GENOME, StartOnlyEncoding())
        self.assertEqual(first, second)
        self.assertEqual(hash(first), hash(second))

    def test_different_costs_are_not_equal(self) -> None:
        individual = Individu.from_genome(GENOME, StartOnlyEncoding())
        self.assertNotEqual(individual.with_cost(COST), individual.with_cost(COST + 1))


if __name__ == "__main__":
    unittest.main()
