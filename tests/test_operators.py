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

from random import Random
from typing import Sequence
import unittest
from unittest import mock

from src.ga.chromosome import ActivityBlock, BlockEncoding, BlockGene, BlockGenome, Encoding
from src.ga.operators import (
    ActivityMutation,
    BlockBoundaryMutation,
    Crossover,
    Mutation,
    OperatorDefaults,
    ParentLengthMismatchError,
    ShiftStartMutation,
    UniformGeneCrossover,
    VariationOperator,
    WrongParentCountError,
)
from src.model.horaire import Horaire
from tests.fixtures import synthetic_instance


class OtherEncoding(Encoding[str]):
    """Encodage factice, incompatible avec les opérateurs de BlockEncoding."""

    def encode(self, horaire: Horaire) -> str:
        raise NotImplementedError

    def decode(self, genome: str) -> Horaire:
        raise NotImplementedError

    def clone(self, genome: str) -> str:
        raise NotImplementedError


class TestScaffoldContract(unittest.TestCase):

    def setUp(self) -> None:
        gene_1 = BlockGene(0, (ActivityBlock(1, 8), ActivityBlock(1, 8), ActivityBlock(1, 8), ActivityBlock(1, 8), ))
        gene_2 = BlockGene(1, (ActivityBlock(1, 4), ActivityBlock(1, 4), ActivityBlock(1, 4), ActivityBlock(1, 4), ))
        gene_3 = BlockGene(2, (ActivityBlock(2, 5), ActivityBlock(2, 5), ActivityBlock(2, 5), ActivityBlock(2, 5), ))
        instance = synthetic_instance()
        self.rnd = Random()
        self.crossover = UniformGeneCrossover()
        self.parent_1 = tuple([gene_1])
        self.parent_2 = tuple([gene_2])
        self.parent_3 = tuple([gene_1, gene_3])
        self.parent_4 = tuple([gene_2, gene_1])
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

    def test_crossover_throw_when_zero_parent_is_sent(self) -> None:
        zero_parents: Sequence[BlockGenome] = tuple()
        with self.assertRaises(WrongParentCountError):
            self.crossover.recombine(zero_parents, self.rnd)

    def test_crossover_throw_when_one_parent_is_sent(self) -> None:
        one_parents: Sequence[BlockGenome] = tuple(tuple())
        with self.assertRaises(WrongParentCountError):
            self.crossover.recombine(one_parents, self.rnd)

    def test_crossover_throw_when_three_parent_is_sent(self) -> None:
        three_parents: Sequence[BlockGenome] = (tuple(), tuple(), tuple())
        with self.assertRaises(WrongParentCountError):
            self.crossover.recombine(three_parents, self.rnd)

    def test_crossover_throw_when_two_parent_not_same_gene_number_from_parent_1(self) -> None:
        two_parents: Sequence[BlockGenome] = (self.parent_1, tuple())
        with self.assertRaises(ParentLengthMismatchError):
            self.crossover.recombine(two_parents, self.rnd)

    def test_crossover_throw_when_two_parent_not_same_gene_number_from_parent_2(self) -> None:
        two_parents: Sequence[BlockGenome] = (tuple(), self.parent_2)
        with self.assertRaises(ParentLengthMismatchError):
            self.crossover.recombine(two_parents, self.rnd)


    @mock.patch('random.choice')
    def test_crossover_when_mask_is_zero_take_default_parent_of_the_child(self, rnd: mock.Mock) -> None:
        rnd.choice.return_value = 0
        parents: Sequence[BlockGenome] = (self.parent_1, self.parent_2)
        child_1, child_2 = self.crossover.recombine(parents, rnd)
        self.assertEqual(parents[0], child_1)
        self.assertEqual(parents[1], child_2)

    @mock.patch('random.choice')
    def test_crossover_when_mask_is_zero_take_other_parent_of_the_child(self, rnd: mock.Mock) -> None:
        rnd.choice.return_value = 1
        parents: Sequence[BlockGenome] = (self.parent_1, self.parent_2)
        child_1, child_2 = self.crossover.recombine(parents, rnd)
        self.assertEqual(parents[0], child_2)
        self.assertEqual(parents[1], child_1)

    @mock.patch('random.choice')
    def test_crossover_when_mask_is_more_than_one_mask_is_respected(self, rnd: mock.Mock) -> None:
        rnd.choice.return_value = 0
        parents: Sequence[BlockGenome] = (self.parent_3, self.parent_4)
        child_1, child_2 = self.crossover.recombine(parents, rnd)
        self.assertEqual(parents[0], child_1)
        self.assertEqual(parents[1], child_2)


if __name__ == "__main__":
    unittest.main()
