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
from typing import Literal, Sequence
import unittest
from unittest import mock

from src.ga.chromosome import ActivityBlock, BlockEncoding, BlockGene, BlockGenome, Encoding
from src.ga.operators import (
    ActivityMutation,
    BlockBoundaryMutation,
    Crossover,
    GeneCannotMutateBoundryError,
    GenomeCannotMutate,
    GenomeNoGeneToMutateError,
    Mutation,
    OperatorDefaults,
    ParentLengthMismatchError,
    ShiftStartMutation,
    UniformGeneCrossover,
    VariationOperator,
    WrongParentCountError,
)
from src.model.horaire import Horaire
from src.model.shift_rules import ShiftStructure
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

    CROSSOVER = 0
    SHIFT_MUTAION = 1
    BLOCK_MUTAION = 2

    def setUp(self) -> None:
        instance = self.instance = synthetic_instance()
        gene_1 = BlockGene(instance.windows.start.earliest, (ActivityBlock(1, 8), ActivityBlock(1, 8), ActivityBlock(1, 8), ActivityBlock(1, 8), ))
        gene_2 = BlockGene(instance.windows.start.earliest + 1, (ActivityBlock(1, 4), ActivityBlock(1, 4), ActivityBlock(1, 4), ActivityBlock(1, 4), ))
        gene_3 = BlockGene(instance.windows.start.earliest + 2, (ActivityBlock(2, 5), ActivityBlock(2, 5), ActivityBlock(2, 5), ActivityBlock(2, 5), ))
        self.rng = Random()
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
            self.block_operators[self.CROSSOVER].recombine(zero_parents, self.rng)

    def test_crossover_throw_when_one_parent_is_sent(self) -> None:
        one_parents: Sequence[BlockGenome] = tuple(tuple())
        with self.assertRaises(WrongParentCountError):
            self.block_operators[self.CROSSOVER].recombine(one_parents, self.rng)

    def test_crossover_throw_when_three_parent_is_sent(self) -> None:
        three_parents: Sequence[BlockGenome] = (tuple(), tuple(), tuple())
        with self.assertRaises(WrongParentCountError):
            self.block_operators[self.CROSSOVER].recombine(three_parents, self.rng)

    def test_crossover_throw_when_two_parent_not_same_gene_number_from_parent_1(self) -> None:
        two_parents: Sequence[BlockGenome] = (self.parent_1, tuple())
        with self.assertRaises(ParentLengthMismatchError):
            self.block_operators[self.CROSSOVER].recombine(two_parents, self.rng)

    def test_crossover_throw_when_two_parent_not_same_gene_number_from_parent_2(self) -> None:
        two_parents: Sequence[BlockGenome] = (tuple(), self.parent_2)
        with self.assertRaises(ParentLengthMismatchError):
            self.block_operators[self.CROSSOVER].recombine(two_parents, self.rng)

    @mock.patch('random.choice')
    def test_crossover_when_mask_is_zero_take_default_parent_of_the_child(self, rnd: mock.Mock) -> None:
        rnd.choice.return_value = 0
        parents: Sequence[BlockGenome] = (self.parent_1, self.parent_2)
        child_1, child_2 = self.block_operators[self.CROSSOVER].recombine(parents, rnd)
        self.assertEqual(parents[0], child_1)
        self.assertEqual(parents[1], child_2)

    @mock.patch('random.choice')
    def test_crossover_when_mask_is_zero_take_other_parent_of_the_child(self, rnd: mock.Mock) -> None:
        rnd.choice.return_value = 1
        parents: Sequence[BlockGenome] = (self.parent_1, self.parent_2)
        child_1, child_2 = self.block_operators[self.CROSSOVER].recombine(parents, rnd)
        self.assertEqual(parents[0], child_2)
        self.assertEqual(parents[1], child_1)

    @mock.patch('random.choice')
    def test_crossover_when_mask_is_more_than_one_mask_is_respected(self, rnd: mock.Mock) -> None:
        rnd.choice.return_value = 0
        parents: Sequence[BlockGenome] = (self.parent_3, self.parent_4)
        child_1, child_2 = self.block_operators[self.CROSSOVER].recombine(parents, rnd)
        self.assertEqual(parents[0], child_1)
        self.assertEqual(parents[1], child_2)

    def test_shift_should_throw_when_genome_does_not_have_gen(self):
        with self.assertRaises(GenomeNoGeneToMutateError):
            self.block_operators[self.SHIFT_MUTAION].mutate(tuple(), self.rng)

    def test_shift_clamp(self):
        def _test(value: int):
            clamped = self.block_operators[self.SHIFT_MUTAION]._clamp(value)
            self.assertTrue(self.instance.windows.start.earliest <= clamped <= self.instance.windows.start.latest)
        _test(-10000)
        _test(self.instance.windows.start.earliest)
        _test(self.instance.windows.start.latest)
        _test(10000)

    def test_shift_mutation_should_add_day(self):
        self._test_for_shift_mutation(
            index=0,
            sign=1,
            add_or_remove=1,
            genome=self.parent_1
        )

    def test_shift_mutation_should_remove_day(self):
        self._test_for_shift_mutation(
            index=0,
            sign=-1,
            add_or_remove=1,
            genome=self.parent_2
        )

    def _test_for_shift_mutation(self, index: int, sign: Literal[1] | Literal[-1], add_or_remove: int, genome: BlockGenome):
        rng = mock.Mock()
        rng.randrange.side_effect = [index, add_or_remove]
        rng.choice.return_value = sign
        mutated = self.block_operators[self.SHIFT_MUTAION].mutate(genome, rng)
        self.assertNotEqual(
            mutated[index].start,
            genome[index].start
        )
        self.assertEqual(
            mutated[index].start,
            max(genome[index].start + (sign * add_or_remove), 0)
        )

    def test_block_mutation_throw_when_gene_is_not_valid(self) -> None:
        block1 = ActivityBlock(2, 4)
        block2 = ActivityBlock(2, 5)
        block3 = ActivityBlock(2, 6)
        gene1 = BlockGene(self.instance.windows.start.earliest + 2, (block1, block1, block1, block1))
        gene2 = BlockGene(self.instance.windows.start.earliest + 2, (block1, block1, block1, block2))
        gene3 = BlockGene(self.instance.windows.start.earliest + 2, (block1, block1, block1, block3))

        with self.assertRaises(GeneCannotMutateBoundryError):
            self.block_operators[self.BLOCK_MUTAION]._get_2_valid_block_to_mutate(gene1, 2, self.rng)

        with self.assertRaises(GeneCannotMutateBoundryError):
            self.block_operators[self.BLOCK_MUTAION]._get_2_valid_block_to_mutate(gene2, 2, self.rng)

        with self.assertRaises(GeneCannotMutateBoundryError):
            self.block_operators[self.BLOCK_MUTAION]._get_2_valid_block_to_mutate(gene3, 3, self.rng)

    def test_block_mutation_get_random_block_does_not_select_itself(self) -> None:
        rng = mock.Mock()
        rng.randrange.side_effect = [3, 0, 0, 0]
        block1 = ActivityBlock(2, 4)
        block2 = ActivityBlock(2, ShiftStructure.MIN_ACTIVITY_DURATION + 2)
        gene = BlockGene(self.instance.windows.start.earliest + 2, (block1, block1, block1, block2))
        first, second = self.block_operators[self.BLOCK_MUTAION]._get_2_valid_block_to_mutate(gene, 2, rng)
        self.assertNotEqual(first, second)

    def test_block_boundary_mutate_throw_when_no_in_genome(self):
        rng = mock.Mock()
        rng.randint.return_value = 0

        with self.assertRaises(GenomeCannotMutate):
            self.block_operators[self.BLOCK_MUTAION].mutate(tuple(), rng)

    def test_block_boundary_mutate_throw_when_no_can_mutate_when_adding_one(self):
        rng = mock.Mock()
        rng.randint.side_effect = [1]
        rng.randrange.side_effect = [0, 0]

        block1 = ActivityBlock(2, 4)
        gene1 = BlockGene(self.instance.windows.start.earliest, (block1, block1, block1, block1))

        with self.assertRaises(GenomeCannotMutate):
            self.block_operators[self.BLOCK_MUTAION].mutate(tuple([gene1]), rng)

    def test_block_boundary_mutate_throw_when_no_can_mutate_when_adding_two(self):
        rng = mock.Mock()
        rng.randint.side_effect =   [1, 2]
        rng.randrange.side_effect = [0, 0, 0, 0]

        block1 = ActivityBlock(2, 4)
        block2 = ActivityBlock(2, 5)
        gene1 = BlockGene(self.instance.windows.start.earliest, (block1, block1, block1, block2))

        self.block_operators[self.BLOCK_MUTAION].mutate(tuple([gene1]), rng)
        with self.assertRaises(GenomeCannotMutate):
            self.block_operators[self.BLOCK_MUTAION].mutate(tuple([gene1]), rng)

    def test_bblock_boundary_mutate_transfer_right_amount_from_block_1_and_2_only(self):
        rng = mock.Mock()
        gene_index = 0
        rng.randint.side_effect =   [1]
        rng.randrange.side_effect = [gene_index, 0, 0]

        block1 = ActivityBlock(2, 4)
        block2 = ActivityBlock(2, 5)
        gene1 = BlockGene(self.instance.windows.start.earliest, (block1, block1, block1, block2))

        mutated = self.block_operators[self.BLOCK_MUTAION].mutate(tuple([gene1]), rng)
        self.assertEqual(mutated[gene_index].blocks[0].duration, block1.duration + 1)
        self.assertEqual(mutated[gene_index].blocks[1].duration, block1.duration)
        self.assertEqual(mutated[gene_index].blocks[2].duration, block1.duration)
        self.assertEqual(mutated[gene_index].blocks[3].duration, block2.duration - 1)



if __name__ == "__main__":
    unittest.main()
