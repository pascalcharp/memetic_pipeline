"""Tests des opérateurs de variation (src/ga/operators.py) — étape 7b, Xavier.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche
``etape-7b-variation`` (voir TODO.md, 7b), sans MiniZinc :
    - faisabilité préservée : un opérateur appliqué à des génomes faisables (``reference_genome``, ou des génomes
      variés construits à la main) rend des génomes faisables (``FeasibilityChecker`` sur le décodage) ;
    - entrées jamais modifiées (comparer avec une copie prise avant l'appel) ;
    - reproductibilité : même graine ⇒ même résultat ;
    - croisement : chaque gène d'un enfant vient de l'un des parents, au même indice ; les deux enfants sont
      complémentaires ; deux parents identiques ⇒ enfants identiques aux parents ; nombre de parents ou longueurs
      différentes ⇒ exception ;
    - ``BlockBoundaryMutation`` : Σd conservée, durées ≥ 4, blocs déjà à la durée minimale ;
    - ``ShiftStartMutation`` : quart en bordure de la plage utile (début le plus tôt, fin la plus tardive) ;
    - ``ActivityMutation`` : activité différente et valide ; instance à une seule activité ⇒ génome inchangé.
"""

import unittest

from src.ga.chromosome import BlockEncoding, Encoding
from src.ga.operators import (
    ActivityMutation,
    BlockBoundaryMutation,
    Crossover,
    Mutation,
    OperatorDefaults,
    ShiftStartMutation,
    UniformGeneCrossover,
    VariationOperator,
)
from src.model.horaire import Horaire
from tests.fixtures import synthetic_instance


class OtherEncoding(Encoding[str]):
    """Encodage factice, incompatible avec les opérateurs de BlockEncoding."""

    def encode(self, horaire: Horaire) -> str:
        raise NotImplementedError

    def decode(self, genome: str) -> Horaire:
        raise NotImplementedError


class TestScaffoldContract(unittest.TestCase):

    def setUp(self) -> None:
        instance = synthetic_instance()
        self.block_operators = (
            UniformGeneCrossover(),
            ShiftStartMutation(instance),
            BlockBoundaryMutation(),
            ActivityMutation(instance),
        )

    def test_interfaces_are_abstract(self) -> None:
        for interface in (VariationOperator, Crossover, Mutation):
            with self.subTest(interface=interface.__name__):
                with self.assertRaises(TypeError):
                    interface()  # type: ignore[abstract]

    def test_block_operators_are_compatible_with_block_encoding_only(self) -> None:
        for operator in self.block_operators:
            with self.subTest(operator=type(operator).__name__):
                self.assertTrue(operator.is_compatible_with(BlockEncoding()))
                self.assertFalse(operator.is_compatible_with(OtherEncoding()))

    def test_crossover_takes_two_parents(self) -> None:
        self.assertEqual(UniformGeneCrossover().parent_count(), OperatorDefaults.CROSSOVER_PARENT_COUNT)


if __name__ == "__main__":
    unittest.main()
