"""Tests des opérateurs de variation (src/ga/operators.py) — étape 7b, Xavier.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche
``etape-7b-variation`` (voir docs/archive/TODO.md, 7b), sans MiniZinc :
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
    EmptyGenomeError,
    GeneCannotMutateBoundaryError,
    Mutation,
    OperatorDefaults,
    ParentLengthMismatchError,
    RandomGenomeCrossover,
    RandomGenomeMutation,
    ShiftStartMutation,
    UniformGeneCrossover,
    VariationOperator,
    WrongParentCountError,
)
from src.model.feasibility import FeasibilityChecker
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


class TestScaffoldContract(unittest.TestCase):

    CROSSOVER = 0
    SHIFT_MUTATION = 1
    BLOCK_MUTATION = 2
    ACTIVITY_MUTATION = 3

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

    def test_crossover_throw_when_zero_parents_are_sent(self) -> None:
        zero_parents: Sequence[BlockGenome] = tuple()
        with self.assertRaises(WrongParentCountError):
            self.block_operators[self.CROSSOVER].recombine(zero_parents, self.rng)

    def test_crossover_throw_when_one_parent_is_sent(self) -> None:
        one_parents: Sequence[BlockGenome] = tuple(tuple())
        with self.assertRaises(WrongParentCountError):
            self.block_operators[self.CROSSOVER].recombine(one_parents, self.rng)

    def test_crossover_throw_when_three_parents_are_sent(self) -> None:
        three_parents: Sequence[BlockGenome] = (tuple(), tuple(), tuple())
        with self.assertRaises(WrongParentCountError):
            self.block_operators[self.CROSSOVER].recombine(three_parents, self.rng)

    def test_crossover_throw_when_two_parents_not_same_gene_number_from_parent_1(self) -> None:
        two_parents: Sequence[BlockGenome] = (self.parent_1, tuple())
        with self.assertRaises(ParentLengthMismatchError):
            self.block_operators[self.CROSSOVER].recombine(two_parents, self.rng)

    def test_crossover_throw_when_two_parents_not_same_gene_number_from_parent_2(self) -> None:
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
    def test_crossover_when_mask_is_one_take_other_parent_of_the_child(self, rnd: mock.Mock) -> None:
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

    def test_shift_should_throw_when_genome_does_not_have_gene(self):
        with self.assertRaises(EmptyGenomeError):
            self.block_operators[self.SHIFT_MUTATION].mutate(tuple(), self.rng)

    def test_shift_mutation_should_add_periods(self):
        self._test_for_shift_mutation(
            index=0,
            sign=1,
            add_or_remove=1,
            genome=self.parent_1
        )

    def test_shift_mutation_should_remove_periods(self):
        self._test_for_shift_mutation(
            index=0,
            sign=-1,
            add_or_remove=1,
            genome=self.parent_2
        )

    def _test_for_shift_mutation(self, index: int, sign: Literal[1] | Literal[-1], add_or_remove: int, genome: BlockGenome):
        rng = mock.Mock()
        rng.randrange.return_value = index
        rng.randint.return_value = add_or_remove
        rng.choice.return_value = sign
        mutated = self.block_operators[self.SHIFT_MUTATION].mutate(genome, rng)
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

        with self.assertRaises(GeneCannotMutateBoundaryError):
            self.block_operators[self.BLOCK_MUTATION]._get_2_valid_block_to_mutate(gene1, 2, self.rng)

        with self.assertRaises(GeneCannotMutateBoundaryError):
            self.block_operators[self.BLOCK_MUTATION]._get_2_valid_block_to_mutate(gene2, 2, self.rng)

        with self.assertRaises(GeneCannotMutateBoundaryError):
            self.block_operators[self.BLOCK_MUTATION]._get_2_valid_block_to_mutate(gene3, 3, self.rng)

    def test_block_boundary_mutate_throw_when_genome_is_empty(self):
        rng = mock.Mock()
        rng.randint.return_value = 0

        with self.assertRaises(EmptyGenomeError):
            self.block_operators[self.BLOCK_MUTATION].mutate(tuple(), rng)

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
        ).individuals
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
# Un déplacement de frontière change exactement deux blocs, d'indices consécutifs.
BOUNDARY_CHANGED_BLOCK_COUNT: int = 2
NEIGHBOR_INDEX_GAP: int = 1
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
        ).individuals
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

    def test_givenAnyGenome_whenGetTransferBounds_thenReturnsTheFixedDefaultBounds(self) -> None:
        for genome in ((REFERENCE_GENE,), (MINIMAL_GENE, SHORT_BLOCKS_GENE)):
            with self.subTest(genome=genome):
                self.assertEqual(
                    BlockBoundaryMutation().get_transfer_bounds(genome),
                    (OperatorDefaults.MIN_BOUNDARY_TRANSFER, OperatorDefaults.MAX_BOUNDARY_TRANSFER),
                )

    # Bogue 4 : la mutation déplace la frontière entre deux blocs VOISINS (docstring, docs/archive/TODO.md 7b). Les deux blocs
    # dont la durée change doivent donc avoir des indices consécutifs.

    def test_givenReferenceGenome_whenMutateManyTimes_thenTheTwoChangedBlocksAreNeighbors(self) -> None:
        genome: BlockGenome = reference_genome(SYNTHETIC_EMPLOYEE_COUNT)
        mutation = BlockBoundaryMutation()
        rng = Random(BOUNDARY_SEED)
        for draw in range(BOUNDARY_DRAW_COUNT):
            with self.subTest(draw=draw):
                mutated = mutation.mutate(genome, rng)
                changed_indices = [
                    block_index
                    for original_gene, mutated_gene in zip(genome, mutated)
                    for block_index, (original_block, mutated_block)
                    in enumerate(zip(original_gene.blocks, mutated_gene.blocks))
                    if original_block != mutated_block
                ]
                self.assertEqual(len(changed_indices), BOUNDARY_CHANGED_BLOCK_COUNT)
                first_index, second_index = changed_indices
                self.assertEqual(second_index - first_index, NEIGHBOR_INDEX_GAP,
                                 "les deux blocs modifiés doivent être voisins")


# Messages d'erreur des opérateurs.
ERRORS_SEED: int = 17
THREE_PARENTS: int = 3
SHORT_PARENT_LENGTH: int = 2
LONG_PARENT_LENGTH: int = 5
REFERENCE_GENOME_FOR_ERRORS: BlockGenome = reference_genome(SHORT_PARENT_LENGTH)

# Propriétés de ShiftStartMutation vérifiées avec un vrai générateur aléatoire (pas de mock). La faisabilité est
# jugée par FeasibilityChecker, qui sert d'oracle : les tests ne recalculent pas eux-mêmes les fenêtres des jalons.
SHIFT_SEED: int = 13
SHIFT_DRAW_COUNT: int = 300
SHIFT_GENOME_COUNT: int = 50
SHIFT_BENCH_FILE: str = "bench_5.json"
# Quart le plus long : Σd = 30 (8 heures rémunérées). Ses jalons tardifs (fin, pause 2) le bornent bien avant
# la fin de la fenêtre de début.
LONG_SHIFT_DURATIONS: tuple[int, ...] = (8, 8, 7, 7)
LONG_SHIFT_BLOCKS: tuple[ActivityBlock, ...] = tuple(
    ActivityBlock(block.activity, duration) for block, duration in zip(REFERENCE_GENE.blocks, LONG_SHIFT_DURATIONS)
)


def feasible_starts(instance: ProblemInstance, blocks: tuple[ActivityBlock, ...]) -> list[int]:
    """Débuts pour lesquels un quart de ces blocs est structurellement faisable, selon FeasibilityChecker.

    Le génome testé donne ce quart à chacun des employés de l'instance (le vérificateur exige le bon nombre).
    """
    checker = FeasibilityChecker(instance)
    encoding = BlockEncoding()
    candidate_starts = range(instance.first_useful_period, instance.last_useful_period + ModelIndexing.FIRST_INDEX)
    return [
        start for start in candidate_starts
        if not checker.violations(encoding.decode(tuple(BlockGene(start, blocks) for _ in range(instance.employee_count))))
    ]


class TestShiftStartMutationWithRealRandom(unittest.TestCase):
    """``ShiftStartMutation`` : un seul début change, les blocs non, et le quart décalé reste faisable."""

    def assert_valid_shift(self, instance: ProblemInstance, original: BlockGenome, mutated: BlockGenome) -> None:
        """Vérifie qu'au plus un gène a changé, seulement par son début, et que le génome muté est faisable."""
        self.assertEqual(len(mutated), len(original))
        changed_genes = [index for index in range(len(original)) if original[index] != mutated[index]]
        self.assertLessEqual(len(changed_genes), 1, "un seul gène peut changer")
        for index in changed_genes:
            self.assertEqual(mutated[index].blocks, original[index].blocks)
        violations = FeasibilityChecker(instance).violations(BlockEncoding().decode(mutated))
        self.assertEqual(violations, [], "le quart décalé doit rester faisable")

    def test_givenGeneWithRoomOnBothSides_whenMutateManyTimes_thenStartAlwaysMoves(self) -> None:
        instance = synthetic_instance(SYNTHETIC_EMPLOYEE_COUNT)
        genome = reference_genome(SYNTHETIC_EMPLOYEE_COUNT)
        starts = feasible_starts(instance, REFERENCE_GENE.blocks)
        room = min(REFERENCE_GENE.start - starts[0], starts[-1] - REFERENCE_GENE.start)
        self.assertGreaterEqual(room, OperatorDefaults.MAX_SHIFT_AMPLITUDE, "cas utile : le gène peut bouger dans les deux sens")
        mutation = ShiftStartMutation(instance)
        rng = Random(SHIFT_SEED)
        for draw in range(SHIFT_DRAW_COUNT):
            with self.subTest(draw=draw):
                mutated = mutation.mutate(genome, rng)
                self.assertNotEqual(mutated, genome, "un décalage nul n'est pas une mutation")
                self.assert_valid_shift(instance, genome, mutated)

    def test_givenLongShiftAtLatestFeasibleStart_whenMutateManyTimes_thenAlwaysFeasible(self) -> None:
        instance = synthetic_instance()
        latest_start = feasible_starts(instance, LONG_SHIFT_BLOCKS)[-1]
        self.assertLess(latest_start, instance.windows.start.latest, "cas utile : borne plus serrée que la fenêtre")
        genome: BlockGenome = (BlockGene(latest_start, LONG_SHIFT_BLOCKS),)
        mutation = ShiftStartMutation(instance)
        rng = Random(SHIFT_SEED)
        for draw in range(SHIFT_DRAW_COUNT):
            with self.subTest(draw=draw):
                self.assert_valid_shift(instance, genome, mutation.mutate(genome, rng))

    def test_givenGeneAtEarliestFeasibleStart_whenMutateManyTimes_thenAlwaysFeasible(self) -> None:
        instance = synthetic_instance()
        earliest_start = feasible_starts(instance, REFERENCE_GENE.blocks)[0]
        genome: BlockGenome = (BlockGene(earliest_start, REFERENCE_GENE.blocks),)
        mutation = ShiftStartMutation(instance)
        rng = Random(SHIFT_SEED)
        for draw in range(SHIFT_DRAW_COUNT):
            with self.subTest(draw=draw):
                self.assert_valid_shift(instance, genome, mutation.mutate(genome, rng))

    def test_givenBenchGenomes_whenMutate_thenEachMutationIsAValidShift(self) -> None:
        instance = load_instance(ProjectPaths.DATA_DIR / SHIFT_BENCH_FILE)
        population = RandomBlockInitializer(instance, BlockEncoding()).initialize(
            SHIFT_GENOME_COUNT, Random(SHIFT_SEED)
        ).individuals
        mutation = ShiftStartMutation(instance)
        rng = Random(SHIFT_SEED)
        for index, individual in enumerate(population):
            with self.subTest(genome_index=index):
                self.assert_valid_shift(instance, individual.genome, mutation.mutate(individual.genome, rng))

    def test_givenGenome_whenMutate_thenInputIsNotModified(self) -> None:
        instance = synthetic_instance(SYNTHETIC_EMPLOYEE_COUNT)
        genome = reference_genome(SYNTHETIC_EMPLOYEE_COUNT)
        snapshot = tuple(genome)
        ShiftStartMutation(instance).mutate(genome, Random(SHIFT_SEED))
        self.assertEqual(genome, snapshot)

    def test_givenSameSeed_whenMutate_thenSameResult(self) -> None:
        instance = synthetic_instance(SYNTHETIC_EMPLOYEE_COUNT)
        genome = reference_genome(SYNTHETIC_EMPLOYEE_COUNT)
        mutation = ShiftStartMutation(instance)
        first = mutation.mutate(genome, Random(SHIFT_SEED))
        second = mutation.mutate(genome, Random(SHIFT_SEED))
        self.assertEqual(first, second)



class TestOperatorErrorMessages(unittest.TestCase):
    """Les exceptions des opérateurs portent un message utile au diagnostic (nom de l'opérateur, valeurs reçues)."""

    def test_givenThreeParents_whenRecombine_thenMessageNamesOperatorAndCounts(self) -> None:
        crossover = UniformGeneCrossover()
        parents = (REFERENCE_GENOME_FOR_ERRORS,) * THREE_PARENTS
        with self.assertRaises(WrongParentCountError) as context:
            crossover.recombine(parents, Random(ERRORS_SEED))
        message = str(context.exception)
        self.assertIn(UniformGeneCrossover.__name__, message)
        self.assertIn(str(crossover.parent_count()), message)
        self.assertIn(str(THREE_PARENTS), message)

    def test_givenParentsOfDifferentLengths_whenRecombine_thenMessageGivesBothLengths(self) -> None:
        short_parent = reference_genome(SHORT_PARENT_LENGTH)
        long_parent = reference_genome(LONG_PARENT_LENGTH)
        with self.assertRaises(ParentLengthMismatchError) as context:
            UniformGeneCrossover().recombine((short_parent, long_parent), Random(ERRORS_SEED))
        message = str(context.exception)
        self.assertIn(UniformGeneCrossover.__name__, message)
        self.assertIn(str(SHORT_PARENT_LENGTH), message)
        self.assertIn(str(LONG_PARENT_LENGTH), message)

    def test_givenEmptyGenome_whenShiftStartMutate_thenMessageNamesOperator(self) -> None:
        with self.assertRaises(EmptyGenomeError) as context:
            ShiftStartMutation(synthetic_instance()).mutate((), Random(ERRORS_SEED))
        self.assertIn(ShiftStartMutation.__name__, str(context.exception))

    def test_givenEmptyGenome_whenBlockBoundaryMutate_thenMessageNamesOperator(self) -> None:
        with self.assertRaises(EmptyGenomeError) as context:
            BlockBoundaryMutation().mutate((), Random(ERRORS_SEED))
        self.assertIn(BlockBoundaryMutation.__name__, str(context.exception))

    def test_givenEmptyGenome_whenActivityMutate_thenMessageNamesOperator(self) -> None:
        with self.assertRaises(EmptyGenomeError) as context:
            ActivityMutation(synthetic_instance()).mutate((), Random(ERRORS_SEED))
        self.assertIn(ActivityMutation.__name__, str(context.exception))

    def test_givenMinimalGene_whenLookingForBlocksToMove_thenMessageGivesTransferAndMinimum(self) -> None:
        transfer = OperatorDefaults.MAX_BOUNDARY_TRANSFER
        with self.assertRaises(GeneCannotMutateBoundaryError) as context:
            BlockBoundaryMutation()._get_2_valid_block_to_mutate(MINIMAL_GENE, transfer, Random(ERRORS_SEED))
        message = str(context.exception)
        self.assertIn(str(transfer), message)
        self.assertIn(str(ShiftStructure.MIN_ACTIVITY_DURATION), message)



# ---------------------------------------------------------------------------------------------------------------------
# Opérateurs témoins (étape 10d) : RandomGenomeCrossover et RandomGenomeMutation
# ---------------------------------------------------------------------------------------------------------------------

RANDOM_GENOME_SEED: int = 23
RANDOM_GENOME_DRAW_COUNT: int = 200
RANDOM_GENOME_BENCH_FILES: tuple[str, ...] = ("bench_2.json", "bench_5.json")
RANDOM_GENOME_REFERENCE_BENCH: str = "bench_2.json"
# Assez de graines pour qu'au moins deux tirages diffèrent, sur une instance où les génomes possibles se comptent
# par milliards.
RANDOM_GENOME_DISTINCT_SEEDS: tuple[int, ...] = tuple(range(10))


def bench_instance(file_name: str) -> ProblemInstance:
    return load_instance(ProjectPaths.DATA_DIR / file_name)


class TestRandomGenomeOperators(unittest.TestCase):
    """Contrat des opérateurs témoins : la loi de l'initialisation, des entrées jamais lues, aucun autre tirage.

    La référence est ``RandomBlockInitializer.random_genome`` : avec un ``rng`` dans le même état, l'opérateur doit
    rendre les mêmes génomes, et laisser ``rng`` dans le même état.
    """

    def setUp(self) -> None:
        self.instance = bench_instance(RANDOM_GENOME_REFERENCE_BENCH)
        self.reference = RandomBlockInitializer(self.instance, BlockEncoding())
        self.crossover = RandomGenomeCrossover(self.instance)
        self.mutation = RandomGenomeMutation(self.instance)
        sampler = Random(RANDOM_GENOME_SEED)
        self.parents = (self.reference.random_genome(sampler), self.reference.random_genome(sampler))
        self.other_parents = (self.reference.random_genome(sampler), self.reference.random_genome(sampler))

    # --- Interface ---------------------------------------------------------------------------------------------------

    def test_givenRandomOperators_whenCheckingEncoding_thenCompatibleWithBlockEncodingOnly(self) -> None:
        for operator in (self.crossover, self.mutation):
            with self.subTest(operator=type(operator).__name__):
                self.assertTrue(operator.is_compatible_with(BlockEncoding()))
                self.assertFalse(operator.is_compatible_with(OtherEncoding()))

    def test_givenRandomCrossover_whenAskingParentCount_thenSameAsUniformGeneCrossover(self) -> None:
        self.assertEqual(self.crossover.parent_count(), UniformGeneCrossover().parent_count())

    # --- Croisement --------------------------------------------------------------------------------------------------

    def test_givenSeed_whenRandomRecombine_thenTwoSuccessiveInitializerDraws(self) -> None:
        reference_rng = Random(RANDOM_GENOME_SEED)
        expected = (self.reference.random_genome(reference_rng), self.reference.random_genome(reference_rng))
        children = self.crossover.recombine(self.parents, Random(RANDOM_GENOME_SEED))
        self.assertEqual(len(children), OperatorDefaults.RANDOM_CROSSOVER_CHILD_COUNT)
        self.assertEqual(children, expected)

    def test_givenRandomRecombine_whenFinished_thenRngStateAsAfterTwoInitializerDraws(self) -> None:
        reference_rng = Random(RANDOM_GENOME_SEED)
        self.reference.random_genome(reference_rng)
        self.reference.random_genome(reference_rng)
        rng = Random(RANDOM_GENOME_SEED)
        self.crossover.recombine(self.parents, rng)
        self.assertEqual(rng.getstate(), reference_rng.getstate())

    def test_givenDifferentParents_whenRandomRecombineWithSameSeed_thenSameChildren(self) -> None:
        first = self.crossover.recombine(self.parents, Random(RANDOM_GENOME_SEED))
        second = self.crossover.recombine(self.other_parents, Random(RANDOM_GENOME_SEED))
        self.assertEqual(first, second)

    def test_givenParentsWhoseGenesMustNotBeRead_whenRandomRecombine_thenGenesAreNotAccessed(self) -> None:
        # Des « parents » qui échouent dès qu'on lit un gène : seul leur nombre peut être consulté.
        unreadable = mock.MagicMock()
        unreadable.__getitem__.side_effect = AssertionError
        unreadable.__iter__.side_effect = AssertionError
        self.crossover.recombine([unreadable, unreadable], Random(RANDOM_GENOME_SEED))

    def test_givenWrongParentCount_whenRandomRecombine_thenRaisesNamingOperatorAndCounts(self) -> None:
        for parents in ((self.parents[0],), self.parents + (self.parents[0],)):
            with self.subTest(parent_count=len(parents)):
                with self.assertRaises(WrongParentCountError) as context:
                    self.crossover.recombine(parents, Random(RANDOM_GENOME_SEED))
                message = str(context.exception)
                self.assertIn(RandomGenomeCrossover.__name__, message)
                self.assertIn(str(OperatorDefaults.CROSSOVER_PARENT_COUNT), message)
                self.assertIn(str(len(parents)), message)

    def test_givenSameSeed_whenRandomRecombineTwice_thenSameChildren(self) -> None:
        first = self.crossover.recombine(self.parents, Random(RANDOM_GENOME_SEED))
        second = self.crossover.recombine(self.parents, Random(RANDOM_GENOME_SEED))
        self.assertEqual(first, second)

    def test_givenSeveralSeeds_whenRandomRecombine_thenChildrenDiffer(self) -> None:
        children = {self.crossover.recombine(self.parents, Random(seed)) for seed in RANDOM_GENOME_DISTINCT_SEEDS}
        self.assertGreater(len(children), 1)

    # --- Mutation ----------------------------------------------------------------------------------------------------

    def test_givenSeed_whenRandomMutate_thenInitializerDraw(self) -> None:
        expected = self.reference.random_genome(Random(RANDOM_GENOME_SEED))
        self.assertEqual(self.mutation.mutate(self.parents[0], Random(RANDOM_GENOME_SEED)), expected)

    def test_givenRandomMutate_whenFinished_thenRngStateAsAfterOneInitializerDraw(self) -> None:
        reference_rng = Random(RANDOM_GENOME_SEED)
        self.reference.random_genome(reference_rng)
        rng = Random(RANDOM_GENOME_SEED)
        self.mutation.mutate(self.parents[0], rng)
        self.assertEqual(rng.getstate(), reference_rng.getstate())

    def test_givenDifferentGenomes_whenRandomMutateWithSameSeed_thenSameResult(self) -> None:
        first = self.mutation.mutate(self.parents[0], Random(RANDOM_GENOME_SEED))
        second = self.mutation.mutate(self.other_parents[1], Random(RANDOM_GENOME_SEED))
        self.assertEqual(first, second)

    def test_givenEmptyGenome_whenRandomMutate_thenRandomGenomeWithoutError(self) -> None:
        expected = self.reference.random_genome(Random(RANDOM_GENOME_SEED))
        self.assertEqual(self.mutation.mutate((), Random(RANDOM_GENOME_SEED)), expected)

    def test_givenSeveralSeeds_whenRandomMutate_thenResultsDiffer(self) -> None:
        results = {self.mutation.mutate(self.parents[0], Random(seed)) for seed in RANDOM_GENOME_DISTINCT_SEEDS}
        self.assertGreater(len(results), 1)

    # --- Faisabilité structurelle, sur plusieurs instances ------------------------------------------------------------

    def test_givenManyDraws_whenRandomOperators_thenEveryGenomeIsStructurallyFeasibleForTheInstance(self) -> None:
        encoding = BlockEncoding()
        for file_name in RANDOM_GENOME_BENCH_FILES:
            instance = bench_instance(file_name)
            checker = FeasibilityChecker(instance)
            crossover = RandomGenomeCrossover(instance)
            mutation = RandomGenomeMutation(instance)
            rng = Random(RANDOM_GENOME_SEED)
            parents = (reference_genome(instance.employee_count), reference_genome(instance.employee_count))
            for draw in range(RANDOM_GENOME_DRAW_COUNT):
                genomes = crossover.recombine(parents, rng) + (mutation.mutate(parents[0], rng),)
                for genome in genomes:
                    with self.subTest(instance=file_name, draw=draw):
                        self.assertEqual(len(genome), instance.employee_count)
                        self.assertTrue(checker.is_feasible(encoding.decode(genome)))

if __name__ == "__main__":
    unittest.main()
