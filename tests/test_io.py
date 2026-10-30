"""Tests de la lecture et de la validation des instances (src/utils/io.py)."""

import copy
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

import numpy as np

from src.config import ProjectPaths
from src.model.shift_rules import ModelIndexing, ShiftStructure
from src.utils.io import (
    InstanceDimensionError,
    InstanceError,
    InstanceFields,
    InstanceFileNotFoundError,
    InstanceFormatError,
    InstanceValueError,
    MilestoneWindow,
    NoShiftFitsError,
    ProblemInstance,
    load_instance,
    parse_instance,
)
from tests.minizinc_probe import MiniZincModelProbe

# (nom, employés, activités, périodes) des instances fournies.
BENCHMARKS: tuple[tuple[str, int, int, int], ...] = (
    ("bench_1", 3, 1, 32),
    ("bench_2", 4, 2, 28),
    ("bench_3", 6, 3, 48),
    ("bench_4", 8, 4, 44),
    ("bench_5", 8, 5, 48),
)

REFERENCE_BENCHMARK: str = "bench_1"
INSTANCE_EXTENSION: str = ".json"
TEST_SOURCE_NAME: str = "instance_de_test"


def benchmark_path(name: str) -> Path:
    return ProjectPaths.DATA_DIR / f"{name}{INSTANCE_EXTENSION}"


def reference_data() -> dict[str, Any]:
    """Copie modifiable des données JSON de l'instance de référence (bench_1 : 3 employés, 1 activité, 32 périodes)."""
    with benchmark_path(REFERENCE_BENCHMARK).open() as instance_file:
        return json.load(instance_file)


def zero_row(activity_count: int) -> list[int]:
    return [0] * activity_count


def pad_with_empty_periods(data: dict[str, Any], before: int, after: int) -> dict[str, Any]:
    """Ajoute des périodes entièrement nulles au début et à la fin de la journée."""
    padded = copy.deepcopy(data)
    activity_count = data[InstanceFields.ACTIVITY_COUNT]
    for field in InstanceFields.MATRICES:
        padded[field] = (
            [zero_row(activity_count) for _ in range(before)]
            + padded[field]
            + [zero_row(activity_count) for _ in range(after)]
        )
    padded[InstanceFields.PERIOD_COUNT] += before + after
    return padded


def keep_first_periods(data: dict[str, Any], period_count: int) -> dict[str, Any]:
    """Tronque la journée à ses ``period_count`` premières périodes."""
    truncated = copy.deepcopy(data)
    for field in InstanceFields.MATRICES:
        truncated[field] = truncated[field][:period_count]
    truncated[InstanceFields.PERIOD_COUNT] = period_count
    return truncated


class TestBenchmarksLoad(unittest.TestCase):
    """Les cinq instances fournies se chargent avec les bonnes dimensions."""

    def test_every_benchmark_loads_with_expected_dimensions(self) -> None:
        for name, employees, activities, periods in BENCHMARKS:
            with self.subTest(instance=name):
                instance = load_instance(benchmark_path(name))
                self.assertIsInstance(instance, ProblemInstance)
                self.assertEqual(instance.name, name)
                self.assertEqual(instance.employee_count, employees)
                self.assertEqual(instance.activity_count, activities)
                self.assertEqual(instance.period_count, periods)
                for matrix in (instance.demand, instance.over_cost, instance.under_cost):
                    self.assertEqual(matrix.shape, (periods, activities))

    def test_matrices_match_json_content(self) -> None:
        data = reference_data()
        instance = parse_instance(data, TEST_SOURCE_NAME)
        np.testing.assert_array_equal(instance.demand, np.array(data[InstanceFields.DEMAND]))
        np.testing.assert_array_equal(instance.over_cost, np.array(data[InstanceFields.OVER_COST]))
        np.testing.assert_array_equal(instance.under_cost, np.array(data[InstanceFields.UNDER_COST]))

    def test_matrices_are_read_only(self) -> None:
        instance = load_instance(benchmark_path(REFERENCE_BENCHMARK))
        for matrix in (instance.demand, instance.over_cost, instance.under_cost):
            with self.assertRaises(ValueError):
                matrix[0, 0] = 1

    def test_instance_is_frozen(self) -> None:
        instance = load_instance(benchmark_path(REFERENCE_BENCHMARK))
        with self.assertRaises(AttributeError):
            instance.employee_count = 1  # type: ignore[misc]

    def test_unknown_fields_are_ignored(self) -> None:
        data = reference_data()
        data["champ_inconnu"] = "ignoré"
        parse_instance(data, TEST_SOURCE_NAME)


# Périodes vides ajoutées avant et après la journée de référence pour tester le rognage de la plage utile.
PERIODS_BEFORE: int = 3
PERIODS_AFTER: int = 2


class TestUsefulRangeAndWindows(unittest.TestCase):
    """Plage utile (MIN_PERIODES..MAX_PERIODES) et fenêtres des jalons."""

    def test_full_day_is_useful_in_every_benchmark(self) -> None:
        for name, _, _, periods in BENCHMARKS:
            with self.subTest(instance=name):
                instance = load_instance(benchmark_path(name))
                self.assertEqual(instance.first_useful_period, ModelIndexing.FIRST_INDEX)
                self.assertEqual(instance.last_useful_period, periods)

    def test_empty_periods_at_both_ends_are_trimmed(self) -> None:
        data = pad_with_empty_periods(reference_data(), PERIODS_BEFORE, PERIODS_AFTER)
        instance = parse_instance(data, TEST_SOURCE_NAME)
        original_period_count = reference_data()[InstanceFields.PERIOD_COUNT]
        self.assertEqual(instance.first_useful_period, ModelIndexing.FIRST_INDEX + PERIODS_BEFORE)
        self.assertEqual(instance.last_useful_period, PERIODS_BEFORE + original_period_count)

    def test_period_with_only_a_cost_is_useful(self) -> None:
        # Une période sans demande mais avec un coût non nul fait partie de la plage utile.
        data = pad_with_empty_periods(reference_data(), PERIODS_BEFORE, 0)
        data[InstanceFields.OVER_COST][0] = [1]
        instance = parse_instance(data, TEST_SOURCE_NAME)
        self.assertEqual(instance.first_useful_period, ModelIndexing.FIRST_INDEX)

    def test_shortest_possible_day_fits_exactly_one_start(self) -> None:
        # bench_2 a exactement MIN_SHIFT_SPAN + 1 périodes : un seul début possible, une seule fin possible.
        instance = load_instance(benchmark_path("bench_2"))
        self.assertEqual(instance.period_count, ShiftStructure.MIN_SHIFT_SPAN + ShiftStructure.INCLUSIVE_BOUNDS_CORRECTION)
        self.assertEqual(instance.windows.start, MilestoneWindow(1, 1))
        self.assertEqual(instance.windows.end, MilestoneWindow(28, 28))

    def test_day_one_period_too_short_is_rejected(self) -> None:
        too_short = ShiftStructure.MIN_SHIFT_SPAN
        data = keep_first_periods(reference_data(), too_short)
        with self.assertRaises(NoShiftFitsError) as context:
            parse_instance(data, TEST_SOURCE_NAME)
        self.assertIn(TEST_SOURCE_NAME, str(context.exception))

    def test_long_day_with_too_short_useful_range_is_rejected(self) -> None:
        # La journée est longue, mais seules quelques périodes portent des données.
        useful_periods = ShiftStructure.MIN_SHIFT_SPAN
        data = pad_with_empty_periods(keep_first_periods(reference_data(), useful_periods), PERIODS_BEFORE, PERIODS_AFTER)
        with self.assertRaises(NoShiftFitsError):
            parse_instance(data, TEST_SOURCE_NAME)

    def test_all_zero_instance_is_rejected(self) -> None:
        data = reference_data()
        period_count = data[InstanceFields.PERIOD_COUNT]
        for field in InstanceFields.MATRICES:
            data[field] = [zero_row(data[InstanceFields.ACTIVITY_COUNT]) for _ in range(period_count)]
        with self.assertRaises(NoShiftFitsError):
            parse_instance(data, TEST_SOURCE_NAME)


class TestMilestoneWindowContains(unittest.TestCase):
    """Appartenance d'une période à une fenêtre, bornes incluses."""

    def test_bounds_are_included(self) -> None:
        window = MilestoneWindow(5, 15)
        for period, expected in ((4, False), (5, True), (10, True), (15, True), (16, False)):
            with self.subTest(period=period):
                self.assertEqual(window.contains(period), expected)

    def test_single_period_window(self) -> None:
        window = MilestoneWindow(7, 7)
        self.assertTrue(window.contains(7))
        self.assertFalse(window.contains(6))
        self.assertFalse(window.contains(8))

    def test_empty_window_contains_nothing(self) -> None:
        window = MilestoneWindow(9, 8)
        for period in (7, 8, 9, 10):
            with self.subTest(period=period):
                self.assertFalse(window.contains(period))


class TestConsistencyWithMiniZinc(unittest.TestCase):
    """La plage utile et les fenêtres calculées en Python sont celles de horaire.mzn, y compris avec des périodes vides."""

    WINDOW_PARAMETERS: dict[str, tuple[str, str]] = {
        "debut": ("MIN_DEBUT", "MAX_DEBUT"),
        "pause1": ("MIN_P1", "MAX_P1"),
        "diner": ("MIN_DINER", "MAX_DINER"),
        "pause2": ("MIN_P2", "MAX_P2"),
        "fin": ("MIN_FIN", "MAX_FIN"),
    }

    def assert_matches_minizinc(self, instance: ProblemInstance, instance_path: Path) -> None:
        parameter_names = ["MIN_PERIODES", "MAX_PERIODES"]
        for minimum_name, maximum_name in self.WINDOW_PARAMETERS.values():
            parameter_names += [minimum_name, maximum_name]
        values = MiniZincModelProbe(instance_path).evaluate(parameter_names)

        self.assertEqual(instance.first_useful_period, values["MIN_PERIODES"])
        self.assertEqual(instance.last_useful_period, values["MAX_PERIODES"])
        for milestone, window in instance.windows.by_milestone().items():
            minimum_name, maximum_name = self.WINDOW_PARAMETERS[milestone]
            with self.subTest(milestone=milestone):
                self.assertEqual(window, MilestoneWindow(values[minimum_name], values[maximum_name]))

    def test_padded_instance_matches_minizinc(self) -> None:
        data = pad_with_empty_periods(reference_data(), PERIODS_BEFORE, PERIODS_AFTER)
        with tempfile.TemporaryDirectory() as directory:
            instance_path = Path(directory) / f"padded{INSTANCE_EXTENSION}"
            instance_path.write_text(json.dumps(data))
            self.assert_matches_minizinc(load_instance(instance_path), instance_path)

    def test_shortest_benchmark_matches_minizinc(self) -> None:
        instance_path = benchmark_path("bench_2")
        self.assert_matches_minizinc(load_instance(instance_path), instance_path)


class TestDisplay(unittest.TestCase):
    """repr concis sur une ligne, str lisible sur plusieurs lignes."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = load_instance(benchmark_path(REFERENCE_BENCHMARK))

    def test_repr_is_a_single_line_with_name_and_dimensions(self) -> None:
        text = repr(self.instance)
        self.assertNotIn("\n", text)
        self.assertTrue(text.startswith(ProblemInstance.__name__))
        for fragment in (repr(REFERENCE_BENCHMARK), "employee_count=3", "activity_count=1", "period_count=32", "1..32"):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, text)

    def test_repr_does_not_dump_matrices(self) -> None:
        # Le repr généré par dataclass afficherait les tableaux numpy en entier.
        self.assertNotIn("array", repr(self.instance))
        self.assertNotIn("demand", repr(self.instance))

    def test_str_summarizes_dimensions_range_windows_and_demand(self) -> None:
        text = str(self.instance)
        self.assertGreater(len(text.splitlines()), 1)
        self.assertIn(REFERENCE_BENCHMARK, text)
        self.assertIn(str(int(self.instance.demand.sum())), text)
        for milestone, window in self.instance.windows.by_milestone().items():
            with self.subTest(milestone=milestone):
                self.assertIn(milestone, text)
                self.assertIn(str(window), text)

    def test_str_reflects_trimmed_useful_range(self) -> None:
        data = pad_with_empty_periods(reference_data(), PERIODS_BEFORE, PERIODS_AFTER)
        instance = parse_instance(data, TEST_SOURCE_NAME)
        first = ModelIndexing.FIRST_INDEX + PERIODS_BEFORE
        self.assertIn(f"{first}..{instance.last_useful_period}", repr(instance))
        self.assertIn(f"périodes {first} à {instance.last_useful_period}", str(instance))

    def test_window_str_shows_inclusive_bounds(self) -> None:
        self.assertEqual(str(MilestoneWindow(5, 15)), "5..15")


class TestFileErrors(unittest.TestCase):
    """Erreurs liées au fichier lui-même."""

    def test_missing_file_raises(self) -> None:
        missing_path = ProjectPaths.DATA_DIR / f"inexistante{INSTANCE_EXTENSION}"
        with self.assertRaises(InstanceFileNotFoundError) as context:
            load_instance(missing_path)
        self.assertIn(str(missing_path), str(context.exception))

    def test_directory_instead_of_file_raises(self) -> None:
        with self.assertRaises(InstanceFileNotFoundError):
            load_instance(ProjectPaths.DATA_DIR)

    def test_invalid_json_raises(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            broken_path = Path(directory) / f"cassee{INSTANCE_EXTENSION}"
            broken_path.write_text('{"NB_EMPLOYES": 3,')
            with self.assertRaises(InstanceFormatError) as context:
                load_instance(broken_path)
        self.assertIn(broken_path.name, str(context.exception))
        self.assertIsNotNone(context.exception.__cause__)

    def test_json_root_must_be_an_object(self) -> None:
        with self.assertRaises(InstanceFormatError):
            parse_instance([1, 2, 3], TEST_SOURCE_NAME)


class TestStructureErrors(unittest.TestCase):
    """Champs manquants, types et dimensions."""

    def assert_rejected(self, data: Any, error_type: type[InstanceError], *expected_fragments: str) -> None:
        with self.assertRaises(error_type) as context:
            parse_instance(data, TEST_SOURCE_NAME)
        message = str(context.exception)
        for fragment in (TEST_SOURCE_NAME,) + expected_fragments:
            self.assertIn(fragment, message)

    def test_every_missing_field_is_reported(self) -> None:
        for field in InstanceFields.COUNTS + InstanceFields.MATRICES:
            with self.subTest(field=field):
                data = reference_data()
                del data[field]
                self.assert_rejected(data, InstanceFormatError, field)

    def test_count_must_be_an_integer(self) -> None:
        for invalid_value in (3.0, "3", True, None, [3]):
            with self.subTest(value=invalid_value):
                data = reference_data()
                data[InstanceFields.EMPLOYEE_COUNT] = invalid_value
                self.assert_rejected(data, InstanceFormatError, InstanceFields.EMPLOYEE_COUNT)

    def test_count_must_be_positive(self) -> None:
        for field in InstanceFields.COUNTS:
            for invalid_value in (0, -1):
                with self.subTest(field=field, value=invalid_value):
                    data = reference_data()
                    data[field] = invalid_value
                    self.assert_rejected(data, InstanceValueError, field)

    def test_matrix_must_be_a_list(self) -> None:
        data = reference_data()
        data[InstanceFields.DEMAND] = {"1": [1]}
        self.assert_rejected(data, InstanceFormatError, InstanceFields.DEMAND)

    def test_matrix_row_must_be_a_list(self) -> None:
        data = reference_data()
        data[InstanceFields.OVER_COST][4] = 7
        self.assert_rejected(data, InstanceFormatError, InstanceFields.OVER_COST, "ligne 5")

    def test_too_few_rows_raises(self) -> None:
        data = reference_data()
        data[InstanceFields.UNDER_COST].pop()
        self.assert_rejected(data, InstanceDimensionError, InstanceFields.UNDER_COST, InstanceFields.PERIOD_COUNT)

    def test_too_many_rows_raises(self) -> None:
        data = reference_data()
        data[InstanceFields.DEMAND].append([1])
        self.assert_rejected(data, InstanceDimensionError, InstanceFields.DEMAND)

    def test_wrong_column_count_raises(self) -> None:
        data = reference_data()
        data[InstanceFields.DEMAND][9] = [1, 1]
        self.assert_rejected(
            data, InstanceDimensionError, InstanceFields.DEMAND, "ligne 10", InstanceFields.ACTIVITY_COUNT
        )

    def test_empty_row_raises(self) -> None:
        data = reference_data()
        data[InstanceFields.DEMAND][0] = []
        self.assert_rejected(data, InstanceDimensionError, InstanceFields.DEMAND, "ligne 1")

    def test_cell_must_be_an_integer(self) -> None:
        for invalid_value in (1.5, 1.0, "1", True, None):
            with self.subTest(value=invalid_value):
                data = reference_data()
                data[InstanceFields.OVER_COST][2][0] = invalid_value
                self.assert_rejected(data, InstanceFormatError, InstanceFields.OVER_COST, "ligne 3, colonne 1")


class TestValueErrors(unittest.TestCase):
    """Valeurs hors domaine."""

    def test_negative_value_in_any_matrix_raises(self) -> None:
        for field in InstanceFields.MATRICES:
            with self.subTest(field=field):
                data = reference_data()
                data[field][6][0] = -1
                with self.assertRaises(InstanceValueError) as context:
                    parse_instance(data, TEST_SOURCE_NAME)
                message = str(context.exception)
                self.assertIn(field, message)
                self.assertIn("période 7", message)

    def test_demand_equal_to_employee_count_is_accepted(self) -> None:
        data = reference_data()
        data[InstanceFields.DEMAND][0][0] = data[InstanceFields.EMPLOYEE_COUNT]
        parse_instance(data, TEST_SOURCE_NAME)

    def test_demand_above_employee_count_raises(self) -> None:
        data = reference_data()
        data[InstanceFields.DEMAND][0][0] = data[InstanceFields.EMPLOYEE_COUNT] + 1
        with self.assertRaises(InstanceValueError) as context:
            parse_instance(data, TEST_SOURCE_NAME)
        self.assertIn("période 1", str(context.exception))

    def test_every_specific_error_is_an_instance_error(self) -> None:
        for error_type in (
            InstanceFileNotFoundError,
            InstanceFormatError,
            InstanceDimensionError,
            InstanceValueError,
            NoShiftFitsError,
        ):
            with self.subTest(error=error_type.__name__):
                self.assertTrue(issubclass(error_type, InstanceError))


if __name__ == "__main__":
    unittest.main()
