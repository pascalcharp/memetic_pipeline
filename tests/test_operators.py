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

import numpy

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
from src.config import ProjectPaths
from src.ga.initialization import RandomBlockInitializer
from src.model.shift_rules import ModelIndexing, ShiftStructure
from src.utils.io import MilestoneWindow, ProblemInstance, ShiftWindows, load_instance
from tests.fixtures import REFERENCE_GENE, reference_genome, synthetic_instance


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
    ACTIVITY_MUTAION = 3

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

    def test_block_boundary_mutate_transfer_right_amount_from_block_1_and_2_only(self):
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

    def test_activity_mutation_does_nothing_when_only_a_single_activity(self):
        rng = mock.Mock()
        block1 = ActivityBlock(1, 4)
        gene1 = BlockGene(self.instance.windows.start.earliest, (block1, block1, block1, block1))
        test_instance_with_a_single_activity = ProblemInstance(
            name="test",
            employee_count=1,
            activity_count=1,
            period_count=20000,
            demand=numpy.array(list()),
            over_cost=numpy.array(list()),
            under_cost=numpy.array(list()),
            first_useful_period=0,
            last_useful_period=100,
            windows=ShiftWindows(
                MilestoneWindow(0, 0),
                MilestoneWindow(5, 5),
                MilestoneWindow(10, 10),
                MilestoneWindow(20, 20),
                MilestoneWindow(30, 30),
            )
        )
        mutation = ActivityMutation(test_instance_with_a_single_activity)
        mutated = mutation.mutate(tuple([gene1]), rng)

        for i in mutated[0].blocks:
            self.assertEqual(i.activity, block1.activity)


# Propriétés de ActivityMutation vérifiées avec un vrai générateur aléatoire (pas de mock) : un mock rend la valeur
# que le test attend et peut masquer un indice pris pour une activité.
ACTIVITY_SEED: int = 7
ACTIVITY_DRAW_COUNT: int = 300
ACTIVITY_GENOME_COUNT: int = 50
ACTIVITY_BENCH_FILE: str = "bench_5.json"  # 5 activités : plusieurs activités de remplacement possibles
SYNTHETIC_EMPLOYEE_COUNT: int = 3


def changed_blocks(original: BlockGenome, mutated: BlockGenome) -> list[tuple[ActivityBlock, ActivityBlock]]:
    """Paires (bloc d'origine, bloc muté) qui diffèrent, tous gènes confondus."""
    return [
        (original_block, mutated_block)
        for original_gene, mutated_gene in zip(original, mutated)
        for original_block, mutated_block in zip(original_gene.blocks, mutated_gene.blocks)
        if original_block != mutated_block
    ]


class TestActivityMutationWithRealRandom(unittest.TestCase):
    """``ActivityMutation`` : activité de remplacement valide et différente, tirée parmi toutes les autres."""

    def assert_single_valid_activity_change(
            self, instance: ProblemInstance, original: BlockGenome, mutated: BlockGenome
    ) -> ActivityBlock:
        """Vérifie qu'un seul bloc a changé, seulement d'activité, vers une activité valide et différente ;
        rend le bloc muté."""
        self.assertEqual(len(mutated), len(original))
        for original_gene, mutated_gene in zip(original, mutated):
            self.assertEqual(mutated_gene.start, original_gene.start)
        changes = changed_blocks(original, mutated)
        self.assertEqual(len(changes), 1, "un seul bloc doit changer")
        original_block, mutated_block = changes[0]
        self.assertEqual(mutated_block.duration, original_block.duration)
        self.assertNotEqual(mutated_block.activity, original_block.activity)
        self.assertGreaterEqual(mutated_block.activity, ModelIndexing.FIRST_INDEX)
        self.assertLessEqual(mutated_block.activity, instance.activity_count)
        return mutated_block

    def test_givenSyntheticInstance_whenMutateManyTimes_thenEachMutationChangesOneBlockToAnotherValidActivity(
            self) -> None:
        instance = synthetic_instance(SYNTHETIC_EMPLOYEE_COUNT)
        genome = reference_genome(SYNTHETIC_EMPLOYEE_COUNT)
        mutation = ActivityMutation(instance)
        rng = Random(ACTIVITY_SEED)
        for draw in range(ACTIVITY_DRAW_COUNT):
            with self.subTest(draw=draw):
                self.assert_single_valid_activity_change(instance, genome, mutation.mutate(genome, rng))

    def test_givenBenchGenomes_whenMutateManyTimes_thenEveryOtherActivityIsEventuallyDrawn(self) -> None:
        instance = load_instance(ProjectPaths.DATA_DIR / ACTIVITY_BENCH_FILE)
        population = RandomBlockInitializer(instance, BlockEncoding()).initialize(
            ACTIVITY_GENOME_COUNT, Random(ACTIVITY_SEED)
        )
        mutation = ActivityMutation(instance)
        rng = Random(ACTIVITY_SEED)
        drawn_activities: set[int] = set()
        for index, individual in enumerate(population):
            with self.subTest(genome_index=index):
                mutated_block = self.assert_single_valid_activity_change(
                    instance, individual.genome, mutation.mutate(individual.genome, rng)
                )
                drawn_activities.add(mutated_block.activity)
        all_activities = set(range(ModelIndexing.FIRST_INDEX, instance.activity_count + ModelIndexing.FIRST_INDEX))
        self.assertEqual(drawn_activities, all_activities)

    def test_givenGenome_whenMutate_thenInputIsNotModified(self) -> None:
        instance = synthetic_instance(SYNTHETIC_EMPLOYEE_COUNT)
        genome = reference_genome(SYNTHETIC_EMPLOYEE_COUNT)
        snapshot = tuple(genome)
        ActivityMutation(instance).mutate(genome, Random(ACTIVITY_SEED))
        self.assertEqual(genome, snapshot)

    def test_givenSameSeed_whenMutate_thenSameResult(self) -> None:
        instance = synthetic_instance(SYNTHETIC_EMPLOYEE_COUNT)
        genome = reference_genome(SYNTHETIC_EMPLOYEE_COUNT)
        mutation = ActivityMutation(instance)
        first = mutation.mutate(genome, Random(ACTIVITY_SEED))
        second = mutation.mutate(genome, Random(ACTIVITY_SEED))
        self.assertEqual(first, second)


# Propriétés de BlockBoundaryMutation vérifiées avec un vrai générateur aléatoire (pas de mock).
BOUNDARY_SEED: int = 11
BOUNDARY_DRAW_COUNT: int = 300
BOUNDARY_GENOME_COUNT: int = 50
BOUNDARY_BENCH_FILE: str = "bench_5.json"
# Gène dont tous les blocs sont à la durée minimale : aucun bloc ne peut céder de périodes, le gène doit être écarté.
MINIMAL_BLOCK_COUNT: int = 4
MINIMAL_GENE: BlockGene = BlockGene(
    REFERENCE_GENE.start,
    tuple(ActivityBlock(block.activity, ShiftStructure.MIN_ACTIVITY_DURATION) for block in REFERENCE_GENE.blocks),
)
# Gène faisable aux blocs courts : durées 6, 6, 5, 5 (Σd = 22, minimum de 6 heures rémunérées). Aucun bloc ne peut
# céder plus de SHORT_BLOCKS_MAX_DURATION - MIN_ACTIVITY_DURATION périodes.
SHORT_BLOCKS_DURATIONS: tuple[int, ...] = (6, 6, 5, 5)
SHORT_BLOCKS_MAX_DURATION: int = max(SHORT_BLOCKS_DURATIONS)
SHORT_BLOCKS_GENE: BlockGene = BlockGene(
    REFERENCE_GENE.start,
    tuple(
        ActivityBlock(block.activity, duration)
        for block, duration in zip(REFERENCE_GENE.blocks, SHORT_BLOCKS_DURATIONS)
    ),
)


def total_duration(gene: BlockGene) -> int:
    """Σd d'un gène."""
    return sum(block.duration for block in gene.blocks)


class TestBlockBoundaryMutationWithRealRandom(unittest.TestCase):
    """``BlockBoundaryMutation`` : un seul gène change, Σd est conservée et chaque durée reste au moins minimale."""

    def assert_valid_boundary_move(self, original: BlockGenome, mutated: BlockGenome) -> None:
        """Vérifie qu'un seul gène a changé, seulement par ses durées, avec Σd conservée et des durées valides."""
        self.assertEqual(len(mutated), len(original))
        changed_genes = [index for index in range(len(original)) if original[index] != mutated[index]]
        self.assertEqual(len(changed_genes), 1, "un seul gène doit changer")
        original_gene = original[changed_genes[0]]
        mutated_gene = mutated[changed_genes[0]]
        self.assertEqual(mutated_gene.start, original_gene.start)
        self.assertEqual(
            [block.activity for block in mutated_gene.blocks],
            [block.activity for block in original_gene.blocks],
        )
        self.assertEqual(total_duration(mutated_gene), total_duration(original_gene))
        for block in mutated_gene.blocks:
            self.assertGreaterEqual(block.duration, ShiftStructure.MIN_ACTIVITY_DURATION)

    def test_givenMinimalGeneBeforeMutableGene_whenMutateManyTimes_thenOnlyTheMutableGeneChanges(self) -> None:
        # Le gène minimal (indice 0) est écarté quand il est tiré ; la mutation doit alors porter sur le gène
        # de référence (indice 1), jamais sur le gène minimal.
        genome: BlockGenome = (MINIMAL_GENE, REFERENCE_GENE)
        mutation = BlockBoundaryMutation()
        rng = Random(BOUNDARY_SEED)
        for draw in range(BOUNDARY_DRAW_COUNT):
            with self.subTest(draw=draw):
                mutated = mutation.mutate(genome, rng)
                self.assertEqual(mutated[0], MINIMAL_GENE, "le gène minimal ne peut pas muter")
                self.assert_valid_boundary_move(genome, mutated)

    def test_givenBenchGenomes_whenMutate_thenEachMutationIsAValidBoundaryMove(self) -> None:
        instance = load_instance(ProjectPaths.DATA_DIR / BOUNDARY_BENCH_FILE)
        population = RandomBlockInitializer(instance, BlockEncoding()).initialize(
            BOUNDARY_GENOME_COUNT, Random(BOUNDARY_SEED)
        )
        mutation = BlockBoundaryMutation()
        rng = Random(BOUNDARY_SEED)
        for index, individual in enumerate(population):
            with self.subTest(genome_index=index):
                self.assert_valid_boundary_move(individual.genome, mutation.mutate(individual.genome, rng))

    def test_givenGenome_whenMutate_thenInputIsNotModified(self) -> None:
        genome: BlockGenome = (MINIMAL_GENE, REFERENCE_GENE)
        snapshot = tuple(genome)
        BlockBoundaryMutation().mutate(genome, Random(BOUNDARY_SEED))
        self.assertEqual(genome, snapshot)

    def test_givenSameSeed_whenMutate_thenSameResult(self) -> None:
        genome: BlockGenome = (MINIMAL_GENE, REFERENCE_GENE)
        mutation = BlockBoundaryMutation()
        first = mutation.mutate(genome, Random(BOUNDARY_SEED))
        second = mutation.mutate(genome, Random(BOUNDARY_SEED))
        self.assertEqual(first, second)

    # Bogue 3 : quand aucun gène ne peut céder le transfert tiré, la mutation ne doit pas lever d'exception en pleine
    # exécution ; elle rend le génome inchangé (même convention que ActivityMutation sur une instance à une activité).

    def test_givenOnlyMinimalGenes_whenMutateManyTimes_thenGenomeIsReturnedUnchanged(self) -> None:
        genome: BlockGenome = (MINIMAL_GENE, MINIMAL_GENE)
        mutation = BlockBoundaryMutation()
        rng = Random(BOUNDARY_SEED)
        for draw in range(BOUNDARY_DRAW_COUNT):
            with self.subTest(draw=draw):
                self.assertEqual(mutation.mutate(genome, rng), genome)

    def test_givenFeasibleGeneWithShortBlocks_whenMutateManyTimes_thenNeverRaisesAndMoveIsValidOrNone(self) -> None:
        # Σd = 22 (6 heures rémunérées, quart faisable) et aucun bloc ne dépasse SHORT_BLOCKS_MAX_DURATION : certains
        # transferts tirés sont trop grands pour tous les blocs, d'autres sont possibles.
        genome: BlockGenome = (SHORT_BLOCKS_GENE, SHORT_BLOCKS_GENE)
        mutation = BlockBoundaryMutation()
        rng = Random(BOUNDARY_SEED)
        unchanged_count = 0
        for draw in range(BOUNDARY_DRAW_COUNT):
            with self.subTest(draw=draw):
                mutated = mutation.mutate(genome, rng)
                if mutated == genome:
                    unchanged_count += 1
                else:
                    self.assert_valid_boundary_move(genome, mutated)
        self.assertGreater(unchanged_count, 0, "certains transferts tirés doivent être impossibles")
        self.assertLess(unchanged_count, BOUNDARY_DRAW_COUNT, "certains transferts tirés doivent être possibles")


if __name__ == "__main__":
    unittest.main()
