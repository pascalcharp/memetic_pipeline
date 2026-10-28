"""Tests des règles structurelles d'un quart (src/model/shift_rules.py) et de leur cohérence avec horaire.mzn."""

import asyncio
import unittest
import warnings
from datetime import timedelta

import minizinc
from minizinc.error import MiniZincWarning

from src.config import MiniZincConfig, ProjectPaths
from src.model.shift_rules import ModelIndexing, ShiftGaps, ShiftStructure, WindowOffsets
from src.utils.minizinc_env import locate_minizinc_driver, lookup_solver


class TestValuesReadInModel(unittest.TestCase):
    """Les valeurs dérivées sont celles écrites en dur dans horaire.mzn (valeurs attendues lues dans le modèle)."""

    def test_shift_span_bounds(self) -> None:
        self.assertEqual(ShiftStructure.MIN_SHIFT_SPAN, 27)
        self.assertEqual(ShiftStructure.MAX_SHIFT_SPAN, 35)

    def test_gaps_between_milestones(self) -> None:
        self.assertEqual(ShiftGaps.START_TO_BREAK1, 4)
        self.assertEqual(ShiftGaps.BREAK1_TO_LUNCH, 5)
        self.assertEqual(ShiftGaps.LUNCH_TO_BREAK2, 8)
        self.assertEqual(ShiftGaps.BREAK2_TO_END, 4)

    def test_window_offsets(self) -> None:
        self.assertEqual(WindowOffsets.START_EARLIEST_AFTER_FIRST, 0)
        self.assertEqual(WindowOffsets.START_LATEST_BEFORE_LAST, 27)
        self.assertEqual(WindowOffsets.BREAK1_EARLIEST_AFTER_FIRST, 4)
        self.assertEqual(WindowOffsets.BREAK1_LATEST_BEFORE_LAST, 17)
        self.assertEqual(WindowOffsets.LUNCH_EARLIEST_AFTER_FIRST, 9)
        self.assertEqual(WindowOffsets.LUNCH_LATEST_BEFORE_LAST, 12)
        self.assertEqual(WindowOffsets.BREAK2_EARLIEST_AFTER_FIRST, 17)
        self.assertEqual(WindowOffsets.BREAK2_LATEST_BEFORE_LAST, 4)
        self.assertEqual(WindowOffsets.END_EARLIEST_AFTER_FIRST, 27)
        self.assertEqual(WindowOffsets.END_LATEST_BEFORE_LAST, 0)

    def test_model_conventions(self) -> None:
        self.assertEqual(ShiftStructure.ACTIVITIES_PER_SHIFT, 4)
        self.assertEqual(ModelIndexing.FIRST_INDEX, 1)
        self.assertEqual(ModelIndexing.NO_ACTIVITY, 0)


class TestInternalConsistency(unittest.TestCase):
    """Les règles sont cohérentes entre elles."""

    def test_durations_are_positive(self) -> None:
        for duration in (
            ShiftStructure.BREAK_DURATION,
            ShiftStructure.LUNCH_DURATION,
            ShiftStructure.MIN_ACTIVITY_DURATION,
        ):
            with self.subTest(duration=duration):
                self.assertGreater(duration, 0)

    def test_span_bounds_are_ordered(self) -> None:
        self.assertLessEqual(ShiftStructure.MIN_SHIFT_SPAN, ShiftStructure.MAX_SHIFT_SPAN)

    def test_shortest_milestone_sequence_fits_in_shortest_shift(self) -> None:
        shortest_sequence = (
            ShiftGaps.START_TO_BREAK1 + ShiftGaps.BREAK1_TO_LUNCH + ShiftGaps.LUNCH_TO_BREAK2 + ShiftGaps.BREAK2_TO_END
        )
        self.assertLessEqual(shortest_sequence, ShiftStructure.MIN_SHIFT_SPAN)

    def test_every_window_reserves_exactly_the_shortest_sequence(self) -> None:
        # Pour chaque jalon intermédiaire, l'espace réservé avant et après lui est exactement la séquence minimale.
        shortest_sequence = (
            ShiftGaps.START_TO_BREAK1 + ShiftGaps.BREAK1_TO_LUNCH + ShiftGaps.LUNCH_TO_BREAK2 + ShiftGaps.BREAK2_TO_END
        )
        reserved_space_by_milestone = {
            "pause1": WindowOffsets.BREAK1_EARLIEST_AFTER_FIRST + WindowOffsets.BREAK1_LATEST_BEFORE_LAST,
            "diner": WindowOffsets.LUNCH_EARLIEST_AFTER_FIRST + WindowOffsets.LUNCH_LATEST_BEFORE_LAST,
            "pause2": WindowOffsets.BREAK2_EARLIEST_AFTER_FIRST + WindowOffsets.BREAK2_LATEST_BEFORE_LAST,
        }
        for milestone, reserved_space in reserved_space_by_milestone.items():
            with self.subTest(milestone=milestone):
                self.assertEqual(reserved_space, shortest_sequence)


class MiniZincModelProbe:
    """Interroge horaire.mzn sur une instance : valeurs de paramètres dérivés et faisabilité de contraintes ajoutées."""

    TIME_LIMIT: timedelta = timedelta(seconds=60)

    def __init__(self, instance_file_name: str) -> None:
        driver = locate_minizinc_driver()
        solver = lookup_solver(MiniZincConfig.DEFAULT_SOLVER_ID, driver)
        model = minizinc.Model(ProjectPaths.MODEL_FILE)
        model.add_file(ProjectPaths.DATA_DIR / instance_file_name)
        self.instance = minizinc.Instance(solver, model)

    def evaluate(self, parameter_names: list[str]) -> dict[str, int]:
        """Retourne la valeur calculée par MiniZinc pour chaque paramètre nommé."""
        probe_variable = "probe_values"
        with self.instance.branch() as branch:
            branch.add_string(
                f"array[1..{len(parameter_names)}] of var int: {probe_variable} ::add_to_output = "
                f"[{', '.join(parameter_names)}];"
            )
            result = asyncio.run(self._first_result(branch))
        return dict(zip(parameter_names, result[probe_variable]))

    def status_with(self, constraint: str) -> minizinc.Status:
        """Statut de la première réponse du solveur une fois ``constraint`` ajoutée au modèle."""
        with self.instance.branch() as branch:
            branch.add_string(constraint)
            # MiniZinc avertit (« model inconsistency detected ») quand la contrainte rend le modèle infaisable :
            # c'est précisément l'un des cas que l'on sonde.
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", MiniZincWarning)
                return asyncio.run(self._first_result(branch)).status

    async def _first_result(self, instance: minizinc.Instance) -> minizinc.Result:
        # Une première solution (ou une preuve d'infaisabilité) suffit : inutile d'attendre l'optimum.
        last_result = None
        async for result in instance.solutions(time_limit=self.TIME_LIMIT, intermediate_solutions=True):
            last_result = result
            if result.status.has_solution() or result.status == minizinc.Status.UNSATISFIABLE:
                break
        return last_result


class TestConsistencyWithMiniZinc(unittest.TestCase):
    """Les fenêtres, écarts et durées de quart calculés en Python sont ceux que MiniZinc applique."""

    # bench_1 : 32 périodes, rapide. bench_3 : 48 périodes, assez pour un quart de durée maximale.
    SHORT_INSTANCE: str = "bench_1.json"
    LONG_INSTANCE: str = "bench_3.json"

    # Jalon de MiniZinc → (nom du minimum, nom du maximum, décalage du minimum, décalage du maximum).
    WINDOWS: dict[str, tuple[str, str, int, int]] = {
        "debut": ("MIN_DEBUT", "MAX_DEBUT",
                  WindowOffsets.START_EARLIEST_AFTER_FIRST, WindowOffsets.START_LATEST_BEFORE_LAST),
        "pause1": ("MIN_P1", "MAX_P1",
                   WindowOffsets.BREAK1_EARLIEST_AFTER_FIRST, WindowOffsets.BREAK1_LATEST_BEFORE_LAST),
        "diner": ("MIN_DINER", "MAX_DINER",
                  WindowOffsets.LUNCH_EARLIEST_AFTER_FIRST, WindowOffsets.LUNCH_LATEST_BEFORE_LAST),
        "pause2": ("MIN_P2", "MAX_P2",
                   WindowOffsets.BREAK2_EARLIEST_AFTER_FIRST, WindowOffsets.BREAK2_LATEST_BEFORE_LAST),
        "fin": ("MIN_FIN", "MAX_FIN",
                WindowOffsets.END_EARLIEST_AFTER_FIRST, WindowOffsets.END_LATEST_BEFORE_LAST),
    }

    # (jalon précédent, jalon suivant, écart minimal).
    GAPS: tuple[tuple[str, str, int], ...] = (
        ("debut", "pause1", ShiftGaps.START_TO_BREAK1),
        ("pause1", "diner", ShiftGaps.BREAK1_TO_LUNCH),
        ("diner", "pause2", ShiftGaps.LUNCH_TO_BREAK2),
        ("pause2", "fin", ShiftGaps.BREAK2_TO_END),
    )

    # On ne contraint que le premier employé : les autres restent libres de couvrir la demande.
    PROBED_EMPLOYEE: int = ModelIndexing.FIRST_INDEX

    # Écart d'une période sous une borne minimale ou au-dessus d'une borne maximale.
    ONE_PERIOD: int = 1

    @classmethod
    def setUpClass(cls) -> None:
        cls.short_probe = MiniZincModelProbe(cls.SHORT_INSTANCE)
        cls.long_probe = MiniZincModelProbe(cls.LONG_INSTANCE)

    def assert_feasible(self, probe: MiniZincModelProbe, constraint: str) -> None:
        self.assertTrue(probe.status_with(constraint).has_solution(), constraint)

    def assert_infeasible(self, probe: MiniZincModelProbe, constraint: str) -> None:
        self.assertEqual(probe.status_with(constraint), minizinc.Status.UNSATISFIABLE, constraint)

    def test_windows_match_model(self) -> None:
        for probe in (self.short_probe, self.long_probe):
            parameter_names = ["MIN_PERIODES", "MAX_PERIODES"]
            for minimum_name, maximum_name, _, _ in self.WINDOWS.values():
                parameter_names += [minimum_name, maximum_name]
            values = probe.evaluate(parameter_names)

            for milestone, (minimum_name, maximum_name, earliest_offset, latest_offset) in self.WINDOWS.items():
                with self.subTest(milestone=milestone, max_periodes=values["MAX_PERIODES"]):
                    self.assertEqual(values[minimum_name], values["MIN_PERIODES"] + earliest_offset)
                    self.assertEqual(values[maximum_name], values["MAX_PERIODES"] - latest_offset)

    def test_minimal_gaps_match_model(self) -> None:
        employee = self.PROBED_EMPLOYEE
        for earlier, later, gap in self.GAPS:
            with self.subTest(earlier=earlier, later=later):
                self.assert_feasible(
                    self.short_probe, f"constraint {later}[{employee}] - {earlier}[{employee}] = {gap};"
                )
                self.assert_infeasible(
                    self.short_probe, f"constraint {later}[{employee}] - {earlier}[{employee}] = {gap - self.ONE_PERIOD};"
                )

    def test_shift_span_bounds_match_model(self) -> None:
        employee = self.PROBED_EMPLOYEE
        span = f"fin[{employee}] - debut[{employee}]"
        minimum = ShiftStructure.MIN_SHIFT_SPAN
        maximum = ShiftStructure.MAX_SHIFT_SPAN

        self.assert_feasible(self.long_probe, f"constraint {span} = {minimum};")
        self.assert_infeasible(self.long_probe, f"constraint {span} = {minimum - self.ONE_PERIOD};")
        self.assert_feasible(self.long_probe, f"constraint {span} = {maximum};")
        self.assert_infeasible(self.long_probe, f"constraint {span} = {maximum + self.ONE_PERIOD};")

    def test_activities_per_shift_matches_model(self) -> None:
        values = self.short_probe.evaluate(["card(index_set_2of2(activites))"])
        self.assertEqual(list(values.values()), [ShiftStructure.ACTIVITIES_PER_SHIFT])


if __name__ == "__main__":
    unittest.main()
