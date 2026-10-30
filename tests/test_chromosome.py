"""Tests du génotype (src/ga/chromosome.py) : forme du gène, interface Encoding, encodage par blocs."""

import dataclasses
import random
import unittest

from src.config import ProjectPaths
from src.ga.chromosome import ActivityBlock, BlockEncoding, BlockGene, Encoding, MalformedGenomeError
from src.model.feasibility import FeasibilityChecker, StructuralRule
from src.model.horaire import Horaire, HoraireEmploye
from src.model.shift_rules import ModelIndexing, ModelVariableNames, ShiftStructure
from src.utils.io import ProblemInstance, load_instance
from tests.minizinc_probe import MiniZincModelProbe
from tests.test_feasibility import SYNTHETIC_ACTIVITY_COUNT, synthetic_instance
from tests.test_horaire import BENCH_1_OPTIMUM_VARIABLES

INSTANCE_EXTENSION: str = ".json"

# Écart fixe d'un quart en plus des blocs d'activité : le quart compte Σd + 2 pauses + dîner périodes,
# et ses bornes sont incluses, d'où fin - debut = Σd + 5.
NON_ACTIVITY_SPAN: int = (
    2 * ShiftStructure.BREAK_DURATION + ShiftStructure.LUNCH_DURATION - ShiftStructure.INCLUSIVE_BOUNDS_CORRECTION
)


def gene(start: int, *blocks: tuple[int, int]) -> BlockGene:
    """Gène écrit de façon compacte : ``gene(1, (activité, durée), ...)``."""
    return BlockGene(start=start, blocks=tuple(ActivityBlock(activity, duration) for activity, duration in blocks))


def uniform_gene(start: int, durations: tuple[int, ...], activity: int = 1) -> BlockGene:
    return gene(start, *((activity, duration) for duration in durations))


def satisfies_d1_conditions(block_gene: BlockGene, instance: ProblemInstance) -> bool:
    """Conditions de faisabilité d'un gène selon D1 : domaines des durées et des activités, couplages linéaires."""
    durations = [block.duration for block in block_gene.blocks]
    span = sum(durations) + NON_ACTIVITY_SPAN
    return (
        all(duration >= ShiftStructure.MIN_ACTIVITY_DURATION for duration in durations)
        and ShiftStructure.MIN_SHIFT_SPAN <= span <= ShiftStructure.MAX_SHIFT_SPAN
        and instance.first_useful_period <= block_gene.start
        and block_gene.start + span <= instance.last_useful_period
        and all(ModelIndexing.FIRST_INDEX <= block.activity <= instance.activity_count for block in block_gene.blocks)
    )


# Optimum de bench_1 (docs/PROBLEME.md) et son génome, calculé à la main avec les formules de D1.
BENCH_1_OPTIMUM: Horaire = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)
BENCH_1_OPTIMUM_GENOME: tuple[BlockGene, ...] = (
    uniform_gene(1, (4, 4, 6, 8)),  # (1, 5, 10, 20, 28)
    uniform_gene(4, (4, 4, 8, 6)),  # (4, 8, 13, 25, 31)
    uniform_gene(5, (4, 6, 6, 6)),  # (5, 9, 16, 26, 32)
)

# Quart de l'exemple de D1 avec une activité distincte par bloc, pour repérer toute confusion entre blocs.
D1_EXAMPLE_SHIFT: HoraireEmploye = HoraireEmploye(start=1, break1=5, lunch=10, break2=20, end=28, activities=(1, 2, 3, 4))
D1_EXAMPLE_GENE: BlockGene = gene(1, (1, 4), (2, 4), (3, 6), (4, 8))


class TestBlockGene(unittest.TestCase):
    """Forme d'un gène."""

    def test_wrong_block_count_is_rejected(self) -> None:
        for block_count in (0, 3, 5):
            with self.subTest(block_count=block_count):
                with self.assertRaises(MalformedGenomeError) as context:
                    uniform_gene(1, (4,) * block_count)
                self.assertIn(str(block_count), str(context.exception))

    def test_is_frozen_and_hashable(self) -> None:
        with self.assertRaises(dataclasses.FrozenInstanceError):
            D1_EXAMPLE_GENE.start = 2  # type: ignore[misc]
        self.assertEqual(hash(D1_EXAMPLE_GENE), hash(gene(1, (1, 4), (2, 4), (3, 6), (4, 8))))

    def test_infeasible_durations_are_representable(self) -> None:
        # Durées nulles ou négatives : c'est une donnée valide, la faisabilité est vérifiée ailleurs (D6).
        negative = uniform_gene(1, (0, -3, 4, 4))
        self.assertEqual(negative.blocks[1].duration, -3)


class TestEncodingInterface(unittest.TestCase):
    """``Encoding`` est abstraite ; ``BlockEncoding`` la réalise."""

    def test_encoding_cannot_be_instantiated(self) -> None:
        with self.assertRaises(TypeError):
            Encoding()  # type: ignore[abstract]

    def test_block_encoding_is_an_encoding(self) -> None:
        self.assertIsInstance(BlockEncoding(), Encoding)


class TestBlockEncodingOneEmployee(unittest.TestCase):
    """Traduction d'un seul quart : exemple de D1."""

    def setUp(self) -> None:
        self.encoding = BlockEncoding()

    def test_encode_shift_d1_example(self) -> None:
        self.assertEqual(self.encoding.encode_shift(D1_EXAMPLE_SHIFT), D1_EXAMPLE_GENE)

    def test_decode_gene_d1_example(self) -> None:
        self.assertEqual(self.encoding.decode_gene(D1_EXAMPLE_GENE), D1_EXAMPLE_SHIFT)

    def test_durations_are_activity_lengths_in_the_grid(self) -> None:
        # Chaque durée du gène est le nombre de périodes de son bloc dans la grille : D1 et grille s'accordent.
        grid_row = Horaire(employees=(D1_EXAMPLE_SHIFT,)).to_grid(D1_EXAMPLE_SHIFT.end)[0]
        for block in self.encoding.encode_shift(D1_EXAMPLE_SHIFT).blocks:
            with self.subTest(activity=block.activity):
                self.assertEqual(int((grid_row == block.activity).sum()), block.duration)


class TestBlockEncodingHoraire(unittest.TestCase):
    """Traduction d'un horaire complet et allers-retours."""

    def setUp(self) -> None:
        self.encoding = BlockEncoding()

    def test_encode_bench_1_optimum(self) -> None:
        self.assertEqual(self.encoding.encode(BENCH_1_OPTIMUM), BENCH_1_OPTIMUM_GENOME)

    def test_decode_bench_1_optimum(self) -> None:
        self.assertEqual(self.encoding.decode(BENCH_1_OPTIMUM_GENOME), BENCH_1_OPTIMUM)

    def test_genome_is_a_tuple(self) -> None:
        # Un tuple de gènes figés : le génome est immuable (D7) et hachable (D8).
        genome = self.encoding.encode(BENCH_1_OPTIMUM)
        self.assertIsInstance(genome, tuple)
        self.assertEqual(hash(genome), hash(BENCH_1_OPTIMUM_GENOME))

    def test_employee_order_is_kept(self) -> None:
        reversed_horaire = Horaire(employees=tuple(reversed(BENCH_1_OPTIMUM.employees)))
        self.assertEqual(self.encoding.encode(reversed_horaire), tuple(reversed(BENCH_1_OPTIMUM_GENOME)))

    def test_round_trip_from_infeasible_horaire(self) -> None:
        # Jalons dans le désordre : durées négatives, mais la traduction reste une bijection.
        disordered = HoraireEmploye(start=20, break1=5, lunch=3, break2=1, end=0, activities=(1, 2, 3, 4))
        horaire = Horaire(employees=(disordered, D1_EXAMPLE_SHIFT))
        genome = self.encoding.encode(horaire)
        self.assertLess(genome[0].blocks[0].duration, 0)
        self.assertEqual(self.encoding.decode(genome), horaire)

    def test_round_trip_from_random_genomes(self) -> None:
        # encode(decode(g)) == g pour des gènes quelconques, y compris absurdes (durées négatives, activité 0).
        rng = random.Random(20261030)
        for _ in range(200):
            genome = tuple(
                gene(rng.randint(-5, 50), *((rng.randint(0, 6), rng.randint(-3, 12)) for _ in range(4)))
                for _ in range(rng.randint(1, 8))
            )
            with self.subTest(genome=genome):
                self.assertEqual(self.encoding.encode(self.encoding.decode(genome)), genome)


class TestDecodingInfeasibleGenomes(unittest.TestCase):
    """Un génome infaisable se décode sans exception ; l'infaisabilité est constatée par le vérificateur.

    Instance synthétique de test_feasibility : 1 employé, plage utile 4..43.
    """

    def setUp(self) -> None:
        self.encoding = BlockEncoding()
        self.checker = FeasibilityChecker(synthetic_instance())

    def rules_violated_by(self, block_gene: BlockGene) -> set[StructuralRule]:
        horaire = self.encoding.decode((block_gene,))
        return {violation.rule for violation in self.checker.violations(horaire)}

    def test_cases(self) -> None:
        cases = {
            "Σd = 21, quart trop court": (uniform_gene(10, (4, 4, 4, 9)), StructuralRule.SHIFT_SPAN),
            "Σd = 31, quart trop long": (uniform_gene(5, (4, 4, 4, 19)), StructuralRule.SHIFT_SPAN),
            "quart qui déborde après la plage utile": (uniform_gene(16, (4, 4, 4, 13)), StructuralRule.END_WINDOW),
            "quart qui commence avant la plage utile": (uniform_gene(3, (5, 5, 6, 7)), StructuralRule.START_WINDOW),
            "bloc 1 trop court": (uniform_gene(10, (3, 5, 7, 7)), StructuralRule.START_TO_BREAK1_GAP),
        }
        for case, (block_gene, expected_rule) in cases.items():
            with self.subTest(case=case):
                self.assertEqual(self.rules_violated_by(block_gene), {expected_rule})


class TestFeasibilityConditionsOfD1(unittest.TestCase):
    """Propriété annoncée par D1 : sur un gène, la faisabilité se réduit à des conditions simples.

    L'horaire décodé est faisable si et seulement si chaque durée est au moins l'activité minimale,
    la durée totale donne 6 à 8 h rémunérées, le quart tient dans la plage utile et les activités
    sont dans leur domaine.
    """

    SAMPLE_SIZE: int = 3000
    SEED: int = 3
    MIN_CASES_OF_EACH_VERDICT: int = 50


    def test_decoded_feasibility_matches_d1_conditions(self) -> None:
        encoding = BlockEncoding()
        instance = synthetic_instance()
        checker = FeasibilityChecker(instance)
        rng = random.Random(self.SEED)
        # Activités tirées surtout dans le domaine, parfois juste en dehors (0 et NB_ACTIVITES + 1).
        activity_choices = (0, 1, 1, 1, 2, 2, 2, SYNTHETIC_ACTIVITY_COUNT + 1)

        verdict_counts = {True: 0, False: 0}
        for _ in range(self.SAMPLE_SIZE):
            block_gene = gene(
                rng.randint(1, 18), *((rng.choice(activity_choices), rng.randint(3, 10)) for _ in range(4))
            )
            expected = satisfies_d1_conditions(block_gene, instance)
            verdict_counts[expected] += 1
            with self.subTest(gene=block_gene):
                self.assertEqual(checker.is_feasible(encoding.decode((block_gene,))), expected)

        # L'échantillon doit exercer les deux verdicts, sinon la propriété n'est pas vraiment testée.
        self.assertGreaterEqual(verdict_counts[True], self.MIN_CASES_OF_EACH_VERDICT)
        self.assertGreaterEqual(verdict_counts[False], self.MIN_CASES_OF_EACH_VERDICT)


class TestRoundTripOnMiniZincSolutions(unittest.TestCase):
    """Validation croisée : aller-retour sur des solutions de horaire.mzn, dont les gènes respectent D1."""

    BENCHMARKS: tuple[str, ...] = ("bench_1", "bench_2", "bench_3")
    EMPLOYEE_VARIABLES: tuple[str, ...] = (
        ModelVariableNames.START,
        ModelVariableNames.BREAK1,
        ModelVariableNames.LUNCH,
        ModelVariableNames.BREAK2,
        ModelVariableNames.END,
        ModelVariableNames.ACTIVITIES,
    )

    def test_round_trip_and_gene_domains(self) -> None:
        encoding = BlockEncoding()
        for benchmark in self.BENCHMARKS:
            with self.subTest(benchmark=benchmark):
                path = ProjectPaths.DATA_DIR / f"{benchmark}{INSTANCE_EXTENSION}"
                result = MiniZincModelProbe(path).first_solution()
                horaire = Horaire.from_model_variables({name: result[name] for name in self.EMPLOYEE_VARIABLES})
                instance = load_instance(path)

                genome = encoding.encode(horaire)
                self.assertEqual(encoding.decode(genome), horaire)
                for block_gene in genome:
                    self.assertTrue(satisfies_d1_conditions(block_gene, instance))


if __name__ == "__main__":
    unittest.main()
