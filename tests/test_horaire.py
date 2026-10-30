"""Tests du phénotype Horaire (src/model/horaire.py) : construction, forme, grille « employé × période »."""

import dataclasses
import unittest

import numpy as np

from src.config import ProjectPaths
from src.model.horaire import Horaire, HoraireEmploye, MalformedHoraireError
from src.model.shift_rules import ModelIndexing, ModelVariableNames
from tests.minizinc_probe import MiniZincModelProbe

# Solution optimale de bench_1 documentée dans docs/PROBLEME.md (32 périodes, 1 activité).
BENCH_1_PERIOD_COUNT: int = 32
BENCH_1_OPTIMUM_VARIABLES: dict[str, list] = {
    ModelVariableNames.START: [1, 4, 5],
    ModelVariableNames.BREAK1: [5, 8, 9],
    ModelVariableNames.LUNCH: [10, 13, 16],
    ModelVariableNames.BREAK2: [20, 25, 26],
    ModelVariableNames.END: [28, 31, 32],
    ModelVariableNames.ACTIVITIES: [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
}
# Même grille que dans docs/PROBLEME.md, où P (pause), D (dîner) et . (hors quart) valent tous 0.
BENCH_1_OPTIMUM_GRID: tuple[str, ...] = (
    "11110111100001111110111111110000",
    "00011110111100001111111101111110",
    "00001111011111100001111110111111",
)

# Employé 1 de l'optimum, avec une activité différente par bloc pour repérer toute confusion entre blocs.
DISTINCT_ACTIVITIES: tuple[int, ...] = (1, 2, 3, 4)


def bench_1_employee_1(activities: tuple[int, ...] = DISTINCT_ACTIVITIES) -> HoraireEmploye:
    return HoraireEmploye(start=1, break1=5, lunch=10, break2=20, end=28, activities=activities)


def grid_from_digits(rows: tuple[str, ...]) -> np.ndarray:
    return np.array([[int(digit) for digit in row] for row in rows], dtype=np.int64)


class TestHoraireEmploye(unittest.TestCase):
    """Construction et forme d'un quart."""

    def test_fields_keep_given_values(self) -> None:
        shift = bench_1_employee_1()
        self.assertEqual((shift.start, shift.break1, shift.lunch, shift.break2, shift.end), (1, 5, 10, 20, 28))
        self.assertEqual(shift.activities, DISTINCT_ACTIVITIES)

    def test_is_frozen(self) -> None:
        shift = bench_1_employee_1()
        with self.assertRaises(dataclasses.FrozenInstanceError):
            shift.start = 2  # type: ignore[misc]

    def test_wrong_activity_count_is_rejected(self) -> None:
        for activities in ((1, 1, 1), (1, 1, 1, 1, 1), ()):
            with self.subTest(activities=activities):
                with self.assertRaises(MalformedHoraireError) as context:
                    bench_1_employee_1(activities)
                self.assertIn(str(len(activities)), str(context.exception))

    def test_structurally_infeasible_shift_is_representable(self) -> None:
        # Jalons dans le désordre : c'est une donnée valide, la faisabilité est vérifiée ailleurs (D6).
        shift = HoraireEmploye(start=20, break1=5, lunch=3, break2=1, end=0, activities=(1, 1, 1, 1))
        self.assertEqual(shift.start, 20)


class TestActivityAt(unittest.TestCase):
    """Activité exercée à chaque période, aux bornes de chaque bloc (employé 1 : 1, 5, 10, 20, 28)."""

    def test_activity_at_block_boundaries(self) -> None:
        expected_by_period = {
            0: ModelIndexing.NO_ACTIVITY,
            1: 1,  # debut : première période de l'activité 1
            4: 1,
            5: ModelIndexing.NO_ACTIVITY,  # pause1
            6: 2,
            9: 2,
            10: ModelIndexing.NO_ACTIVITY,  # diner, 4 périodes
            13: ModelIndexing.NO_ACTIVITY,
            14: 3,
            19: 3,
            20: ModelIndexing.NO_ACTIVITY,  # pause2
            21: 4,
            28: 4,  # fin : incluse
            29: ModelIndexing.NO_ACTIVITY,
        }
        shift = bench_1_employee_1()
        for period, expected in expected_by_period.items():
            with self.subTest(period=period):
                self.assertEqual(shift.activity_at(period), expected)


class TestHoraire(unittest.TestCase):
    """Construction, égalité par valeur et construction depuis les variables MiniZinc."""

    def test_equal_by_value_and_hashable(self) -> None:
        first = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)
        second = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)
        self.assertEqual(first, second)
        self.assertEqual(hash(first), hash(second))

    def test_different_horaires_are_not_equal(self) -> None:
        first = Horaire(employees=(bench_1_employee_1(),))
        second = Horaire(employees=(dataclasses.replace(bench_1_employee_1(), end=29),))
        self.assertNotEqual(first, second)

    def test_no_employee_is_rejected(self) -> None:
        with self.assertRaises(MalformedHoraireError):
            Horaire(employees=())

    def test_from_model_variables(self) -> None:
        horaire = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)
        self.assertEqual(horaire.employee_count, 3)
        self.assertEqual(
            horaire.employees[1],
            HoraireEmploye(start=4, break1=8, lunch=13, break2=25, end=31, activities=(1, 1, 1, 1)),
        )

    def test_activities_become_tuples(self) -> None:
        # minizinc-python rend des listes ; le phénotype doit rester hachable.
        horaire = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)
        self.assertIsInstance(horaire.employees[0].activities, tuple)

    def test_missing_variable_is_named(self) -> None:
        for missing in BENCH_1_OPTIMUM_VARIABLES:
            with self.subTest(missing=missing):
                values = {name: value for name, value in BENCH_1_OPTIMUM_VARIABLES.items() if name != missing}
                with self.assertRaises(MalformedHoraireError) as context:
                    Horaire.from_model_variables(values)
                self.assertIn(missing, str(context.exception))

    def test_wrong_variable_length_is_named(self) -> None:
        values = dict(BENCH_1_OPTIMUM_VARIABLES)
        values[ModelVariableNames.LUNCH] = [10, 13]
        with self.assertRaises(MalformedHoraireError) as context:
            Horaire.from_model_variables(values)
        self.assertIn(ModelVariableNames.LUNCH, str(context.exception))

    def test_wrong_activity_count_from_model_variables(self) -> None:
        values = dict(BENCH_1_OPTIMUM_VARIABLES)
        values[ModelVariableNames.ACTIVITIES] = [[1, 1, 1, 1], [1, 1, 1], [1, 1, 1, 1]]
        with self.assertRaises(MalformedHoraireError):
            Horaire.from_model_variables(values)


class TestGrid(unittest.TestCase):
    """Grille « employé × période → activité ou 0 »."""

    def test_documented_bench_1_optimum(self) -> None:
        grid = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES).to_grid(BENCH_1_PERIOD_COUNT)
        np.testing.assert_array_equal(grid, grid_from_digits(BENCH_1_OPTIMUM_GRID))

    def test_shape_and_type(self) -> None:
        grid = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES).to_grid(BENCH_1_PERIOD_COUNT)
        self.assertEqual(grid.shape, (3, BENCH_1_PERIOD_COUNT))
        self.assertTrue(np.issubdtype(grid.dtype, np.integer))

    def test_each_block_keeps_its_own_activity(self) -> None:
        grid = Horaire(employees=(bench_1_employee_1(),)).to_grid(BENCH_1_PERIOD_COUNT)
        np.testing.assert_array_equal(grid, grid_from_digits(("11110222200003333330444444440000",)))

    def test_periods_after_the_day_are_ignored(self) -> None:
        horaire = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)
        full_grid = horaire.to_grid(BENCH_1_PERIOD_COUNT)
        shorter_period_count = 20
        np.testing.assert_array_equal(horaire.to_grid(shorter_period_count), full_grid[:, :shorter_period_count])

    def test_shift_starting_before_the_day_is_clipped(self) -> None:
        # Quart infaisable qui commence avant la période 1 : la grille ne garde que les périodes 1..N.
        shift = HoraireEmploye(start=-2, break1=2, lunch=7, break2=17, end=25, activities=(1, 1, 1, 1))
        grid = Horaire(employees=(shift,)).to_grid(BENCH_1_PERIOD_COUNT)
        np.testing.assert_array_equal(grid, grid_from_digits(("10111100001111110111111110000000",)))

    def test_grid_does_not_depend_on_previous_calls(self) -> None:
        horaire = Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)
        first_grid = horaire.to_grid(BENCH_1_PERIOD_COUNT)
        first_grid[0, 0] = 9
        np.testing.assert_array_equal(horaire.to_grid(BENCH_1_PERIOD_COUNT), grid_from_digits(BENCH_1_OPTIMUM_GRID))


class TestGridMatchesMiniZinc(unittest.TestCase):
    """Validation croisée : la grille Python est identique à la 2ᵉ sortie de horaire.mzn."""

    BENCHMARKS: tuple[str, ...] = ("bench_1", "bench_2", "bench_3")
    INSTANCE_EXTENSION: str = ".json"

    # Lignes de la 2ᵉ sortie : « Employé e<TAB>chiffres », un chiffre par période (activités < 10 dans les bench).
    GRID_LINE_PREFIX: str = "Employé"
    GRID_LINE_SEPARATOR: str = "\t"

    EMPLOYEE_VARIABLES: tuple[str, ...] = (
        ModelVariableNames.START,
        ModelVariableNames.BREAK1,
        ModelVariableNames.LUNCH,
        ModelVariableNames.BREAK2,
        ModelVariableNames.END,
        ModelVariableNames.ACTIVITIES,
    )

    def minizinc_grid(self, output_text: str) -> np.ndarray:
        rows = [
            line.split(self.GRID_LINE_SEPARATOR)[1]
            for line in output_text.splitlines()
            if line.startswith(self.GRID_LINE_PREFIX)
        ]
        return grid_from_digits(tuple(rows))

    def test_grid_matches_model_output(self) -> None:
        for benchmark in self.BENCHMARKS:
            with self.subTest(benchmark=benchmark):
                result = MiniZincModelProbe(ProjectPaths.DATA_DIR / f"{benchmark}{self.INSTANCE_EXTENSION}").first_solution()
                self.assertTrue(result.status.has_solution())

                values = {name: result[name] for name in self.EMPLOYEE_VARIABLES}
                horaire = Horaire.from_model_variables(values)
                expected_grid = self.minizinc_grid(result.solution._output_item)

                period_count = expected_grid.shape[1]
                np.testing.assert_array_equal(horaire.to_grid(period_count), expected_grid)


if __name__ == "__main__":
    unittest.main()
