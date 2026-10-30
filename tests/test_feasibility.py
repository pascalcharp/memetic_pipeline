"""Tests de la vérification de faisabilité structurelle (src/model/feasibility.py).

Instance synthétique : 44 périodes, dont 3 vides au début et 1 à la fin, soit une plage utile de 4 à 43
(40 périodes, assez pour un quart trop long). La demande est nulle partout : la contrainte de couverture
de horaire.mzn est alors vide, et MiniZinc ne juge plus que la faisabilité structurelle, ce qui permet
la validation croisée. Fenêtres des jalons :

    debut 4..16   pause1 8..26   diner 13..31   pause2 21..39   fin 31..43

Les quarts sont écrits par leurs jalons : (debut, pause1, diner, pause2, fin).
"""

import dataclasses
import json
import tempfile
import unittest
from pathlib import Path
from typing import Any

from src.config import ProjectPaths
from src.model.feasibility import (
    EmployeeCountMismatchError,
    FeasibilityChecker,
    FeasibilityError,
    StructuralRule,
    Violation,
)
from src.model.horaire import Horaire, HoraireEmploye
from src.model.shift_rules import ModelIndexing, ModelVariableNames, ShiftStructure
from src.utils.io import InstanceFields, ProblemInstance, load_instance, parse_instance
from tests.minizinc_probe import MiniZincModelProbe

SYNTHETIC_NAME: str = "instance_synthetique"
SYNTHETIC_PERIOD_COUNT: int = 44
SYNTHETIC_ACTIVITY_COUNT: int = 2
EMPTY_PERIODS_BEFORE: int = 3
EMPTY_PERIODS_AFTER: int = 1
USEFUL_PERIOD_COST: int = 1

FIRST_USEFUL_PERIOD: int = 4
LAST_USEFUL_PERIOD: int = 43

EMPLOYEE: int = 1
ALTERNATING_ACTIVITIES: tuple[int, ...] = (1, 2, 1, 2)


def synthetic_data(employee_count: int) -> dict[str, Any]:
    """Données JSON de l'instance synthétique, à demande nulle."""
    useful_period_count = SYNTHETIC_PERIOD_COUNT - EMPTY_PERIODS_BEFORE - EMPTY_PERIODS_AFTER
    zero_row = [0] * SYNTHETIC_ACTIVITY_COUNT
    cost_row = [USEFUL_PERIOD_COST] * SYNTHETIC_ACTIVITY_COUNT
    costs = (
        [zero_row] * EMPTY_PERIODS_BEFORE + [cost_row] * useful_period_count + [zero_row] * EMPTY_PERIODS_AFTER
    )
    return {
        InstanceFields.EMPLOYEE_COUNT: employee_count,
        InstanceFields.ACTIVITY_COUNT: SYNTHETIC_ACTIVITY_COUNT,
        InstanceFields.PERIOD_COUNT: SYNTHETIC_PERIOD_COUNT,
        InstanceFields.DEMAND: [zero_row] * SYNTHETIC_PERIOD_COUNT,
        InstanceFields.OVER_COST: costs,
        InstanceFields.UNDER_COST: costs,
    }


def synthetic_instance(employee_count: int = 1) -> ProblemInstance:
    return parse_instance(synthetic_data(employee_count), name=SYNTHETIC_NAME)


def shift(
    start: int, break1: int, lunch: int, break2: int, end: int, activities: tuple[int, ...] = ALTERNATING_ACTIVITIES
) -> HoraireEmploye:
    return HoraireEmploye(start=start, break1=break1, lunch=lunch, break2=break2, end=end, activities=activities)


def single(employee_shift: HoraireEmploye) -> Horaire:
    return Horaire(employees=(employee_shift,))


# Quart de référence, faisable avec du jeu sur presque toutes les contraintes : écarts 4, 5, 9, 9 ; durée 27.
REFERENCE_SHIFT: HoraireEmploye = shift(10, 14, 19, 28, 37)

# Quarts faisables, dont plusieurs exactement aux bornes.
FEASIBLE_SHIFTS: dict[str, HoraireEmploye] = {
    "référence": REFERENCE_SHIFT,
    "toutes les fenêtres à leur borne inférieure": shift(4, 8, 13, 21, 31),
    "toutes les fenêtres à leur borne supérieure": shift(16, 26, 31, 39, 43),
    "écart diner → pause2 minimal (8)": shift(10, 14, 19, 27, 37),
    "écart pause2 → fin minimal (4)": shift(10, 14, 19, 33, 37),
    "durée maximale (35)": shift(8, 12, 17, 26, 43),
    "dernière activité (NB_ACTIVITES)": shift(10, 14, 19, 28, 37, activities=(2, 2, 2, 2)),
}

# Quarts qui violent exactement une contrainte, un cran au-delà de sa borne.
SINGLE_VIOLATION_SHIFTS: dict[str, tuple[HoraireEmploye, Violation]] = {
    "debut avant la plage utile": (shift(3, 8, 13, 22, 31), Violation(EMPLOYEE, StructuralRule.START_WINDOW, 3)),
    "fin après la plage utile": (shift(16, 20, 25, 34, 44), Violation(EMPLOYEE, StructuralRule.END_WINDOW, 44)),
    "écart debut → pause1 de 3": (
        shift(11, 14, 19, 28, 38),
        Violation(EMPLOYEE, StructuralRule.START_TO_BREAK1_GAP, 3),
    ),
    "écart pause1 → diner de 4": (
        shift(10, 14, 18, 28, 37),
        Violation(EMPLOYEE, StructuralRule.BREAK1_TO_LUNCH_GAP, 4),
    ),
    "écart diner → pause2 de 7": (
        shift(10, 14, 19, 26, 37),
        Violation(EMPLOYEE, StructuralRule.LUNCH_TO_BREAK2_GAP, 7),
    ),
    "écart pause2 → fin de 3": (
        shift(10, 14, 19, 34, 37),
        Violation(EMPLOYEE, StructuralRule.BREAK2_TO_END_GAP, 3),
    ),
    "quart trop court (26)": (shift(10, 14, 19, 28, 36), Violation(EMPLOYEE, StructuralRule.SHIFT_SPAN, 26)),
    "quart trop long (36)": (shift(7, 11, 16, 25, 43), Violation(EMPLOYEE, StructuralRule.SHIFT_SPAN, 36)),
    "activité 0": (
        shift(10, 14, 19, 28, 37, activities=(1, 2, ModelIndexing.NO_ACTIVITY, 2)),
        Violation(EMPLOYEE, StructuralRule.ACTIVITY_DOMAIN, ModelIndexing.NO_ACTIVITY),
    ),
    "activité NB_ACTIVITES + 1": (
        shift(10, 14, 19, 28, 37, activities=(1, 2, 1, SYNTHETIC_ACTIVITY_COUNT + 1)),
        Violation(EMPLOYEE, StructuralRule.ACTIVITY_DOMAIN, SYNTHETIC_ACTIVITY_COUNT + 1),
    ),
}


class TestSyntheticInstance(unittest.TestCase):
    """Garde-fou : l'instance synthétique a bien la plage utile et les fenêtres sur lesquelles les cas reposent."""

    def test_useful_range_and_windows(self) -> None:
        instance = synthetic_instance()
        self.assertEqual((instance.first_useful_period, instance.last_useful_period), (FIRST_USEFUL_PERIOD, LAST_USEFUL_PERIOD))
        windows = instance.windows
        self.assertEqual((windows.start.earliest, windows.start.latest), (4, 16))
        self.assertEqual((windows.break1.earliest, windows.break1.latest), (8, 26))
        self.assertEqual((windows.lunch.earliest, windows.lunch.latest), (13, 31))
        self.assertEqual((windows.break2.earliest, windows.break2.latest), (21, 39))
        self.assertEqual((windows.end.earliest, windows.end.latest), (31, 43))


class TestFeasibleShifts(unittest.TestCase):
    """Les quarts faisables, y compris exactement aux bornes, ne donnent aucune violation."""

    def setUp(self) -> None:
        self.checker = FeasibilityChecker(synthetic_instance())

    def test_no_violation(self) -> None:
        for case, employee_shift in FEASIBLE_SHIFTS.items():
            with self.subTest(case=case):
                self.assertEqual(self.checker.violations(single(employee_shift)), [])
                self.assertTrue(self.checker.is_feasible(single(employee_shift)))

    def test_shift_span_bounds_are_the_model_ones(self) -> None:
        # Les cas ci-dessus couvrent les deux bornes de la durée ; on vérifie qu'elles sont bien 27 et 35.
        self.assertEqual(REFERENCE_SHIFT.end - REFERENCE_SHIFT.start, ShiftStructure.MIN_SHIFT_SPAN)
        longest = FEASIBLE_SHIFTS["durée maximale (35)"]
        self.assertEqual(longest.end - longest.start, ShiftStructure.MAX_SHIFT_SPAN)


class TestSingleViolation(unittest.TestCase):
    """Chaque contrainte violée isolément donne exactement une violation, avec la bonne règle et la bonne valeur."""

    def setUp(self) -> None:
        self.checker = FeasibilityChecker(synthetic_instance())

    def test_exactly_one_violation(self) -> None:
        for case, (employee_shift, expected) in SINGLE_VIOLATION_SHIFTS.items():
            with self.subTest(case=case):
                self.assertEqual(self.checker.violations(single(employee_shift)), [expected])
                self.assertFalse(self.checker.is_feasible(single(employee_shift)))

    def test_every_rule_except_inner_windows_is_covered(self) -> None:
        # Les fenêtres intérieures ne peuvent pas être violées seules (voir TestRedundantWindows).
        inner_windows = {StructuralRule.BREAK1_WINDOW, StructuralRule.LUNCH_WINDOW, StructuralRule.BREAK2_WINDOW}
        covered = {expected.rule for _, expected in SINGLE_VIOLATION_SHIFTS.values()}
        self.assertEqual(covered, set(StructuralRule) - inner_windows)

    def test_employee_violations_matches_violations(self) -> None:
        for case, (employee_shift, expected) in SINGLE_VIOLATION_SHIFTS.items():
            with self.subTest(case=case):
                self.assertEqual(self.checker.employee_violations(EMPLOYEE, employee_shift), [expected])


class TestRedundantWindows(unittest.TestCase):
    """Les fenêtres de pause1, diner et pause2 découlent des autres contraintes : les violer en viole d'autres.

    On vérifie que la violation de fenêtre est bien rapportée, en plus de celles qui l'accompagnent.
    """

    def setUp(self) -> None:
        self.checker = FeasibilityChecker(synthetic_instance())

    def test_inner_window_violations_are_reported(self) -> None:
        cases = {
            "pause1 trop tôt": (
                shift(4, 7, 13, 22, 31),
                {
                    Violation(EMPLOYEE, StructuralRule.BREAK1_WINDOW, 7),
                    Violation(EMPLOYEE, StructuralRule.START_TO_BREAK1_GAP, 3),
                },
            ),
            "diner trop tard": (
                shift(16, 20, 32, 40, 43),
                {
                    Violation(EMPLOYEE, StructuralRule.LUNCH_WINDOW, 32),
                    Violation(EMPLOYEE, StructuralRule.BREAK2_WINDOW, 40),
                    Violation(EMPLOYEE, StructuralRule.BREAK2_TO_END_GAP, 3),
                },
            ),
        }
        for case, (employee_shift, expected) in cases.items():
            with self.subTest(case=case):
                self.assertEqual(set(self.checker.violations(single(employee_shift))), expected)


class TestSeveralViolations(unittest.TestCase):
    """Toutes les violations sont rapportées, pour chaque employé, avec son numéro (à partir de 1)."""

    def test_one_employee_with_several_violations(self) -> None:
        checker = FeasibilityChecker(synthetic_instance())
        # Écart debut → pause1 de 3, durée 26, deux activités hors domaine.
        employee_shift = shift(11, 14, 19, 28, 37, activities=(0, 2, 1, 3))
        expected = {
            Violation(EMPLOYEE, StructuralRule.START_TO_BREAK1_GAP, 3),
            Violation(EMPLOYEE, StructuralRule.SHIFT_SPAN, 26),
            Violation(EMPLOYEE, StructuralRule.ACTIVITY_DOMAIN, 0),
            Violation(EMPLOYEE, StructuralRule.ACTIVITY_DOMAIN, 3),
        }
        violations = checker.violations(single(employee_shift))
        self.assertEqual(len(violations), len(expected))
        self.assertEqual(set(violations), expected)

    def test_violations_are_attributed_to_the_right_employee(self) -> None:
        checker = FeasibilityChecker(synthetic_instance(employee_count=3))
        too_short, _ = SINGLE_VIOLATION_SHIFTS["quart trop court (26)"]
        bad_activity, _ = SINGLE_VIOLATION_SHIFTS["activité 0"]
        horaire = Horaire(employees=(too_short, REFERENCE_SHIFT, bad_activity))
        expected = {
            Violation(1, StructuralRule.SHIFT_SPAN, 26),
            Violation(3, StructuralRule.ACTIVITY_DOMAIN, ModelIndexing.NO_ACTIVITY),
        }
        self.assertEqual(set(checker.violations(horaire)), expected)

    def test_identical_employees_are_all_checked(self) -> None:
        checker = FeasibilityChecker(synthetic_instance(employee_count=3))
        too_short, _ = SINGLE_VIOLATION_SHIFTS["quart trop court (26)"]
        horaire = Horaire(employees=(too_short, too_short, too_short))
        expected = {Violation(employee, StructuralRule.SHIFT_SPAN, 26) for employee in (1, 2, 3)}
        self.assertEqual(set(checker.violations(horaire)), expected)


class TestEmployeeCountMismatch(unittest.TestCase):
    """Un horaire qui n'a pas le nombre d'employés de l'instance est une erreur, pas une infaisabilité."""

    def test_mismatch_raises(self) -> None:
        checker = FeasibilityChecker(synthetic_instance(employee_count=3))
        for employee_count in (1, 2, 4):
            with self.subTest(employee_count=employee_count):
                horaire = Horaire(employees=(REFERENCE_SHIFT,) * employee_count)
                with self.assertRaises(EmployeeCountMismatchError) as context:
                    checker.violations(horaire)
                message = str(context.exception)
                self.assertIn(str(employee_count), message)
                self.assertIn(str(3), message)
                self.assertIn(SYNTHETIC_NAME, message)

    def test_is_feasible_raises_too(self) -> None:
        checker = FeasibilityChecker(synthetic_instance(employee_count=3))
        with self.assertRaises(FeasibilityError) as context:
            checker.is_feasible(single(REFERENCE_SHIFT))
        # Le message de diagnostic doit survivre au passage par is_feasible.
        self.assertIn(SYNTHETIC_NAME, str(context.exception))


class TestViolationDisplay(unittest.TestCase):
    """Le message d'une violation contient l'employé, la règle et la valeur fautive."""

    def test_str_contains_diagnostic_information(self) -> None:
        violation = Violation(2, StructuralRule.LUNCH_TO_BREAK2_GAP, 7)
        message = str(violation)
        self.assertIn("2", message)
        self.assertIn(StructuralRule.LUNCH_TO_BREAK2_GAP.value, message)
        self.assertIn("7", message)

    def test_every_rule_description_is_text(self) -> None:
        # Une virgule finale (« A = "texte", ») ferait de la valeur un tuple, affiché « ('texte',) ».
        for rule in StructuralRule:
            with self.subTest(rule=rule.name):
                self.assertIsInstance(rule.value, str)
                self.assertIn(rule.value, str(Violation(EMPLOYEE, rule, 0)))

    def test_violation_is_frozen(self) -> None:
        violation = Violation(2, StructuralRule.SHIFT_SPAN, 26)
        with self.assertRaises(dataclasses.FrozenInstanceError):
            violation.found = 27  # type: ignore[misc]


class TestBenchmarkSolutionsAreFeasible(unittest.TestCase):
    """Validation croisée : une solution trouvée par MiniZinc sur un bench est structurellement faisable."""

    BENCHMARKS: tuple[str, ...] = ("bench_1", "bench_2", "bench_3")
    INSTANCE_EXTENSION: str = ".json"
    EMPLOYEE_VARIABLES: tuple[str, ...] = (
        ModelVariableNames.START,
        ModelVariableNames.BREAK1,
        ModelVariableNames.LUNCH,
        ModelVariableNames.BREAK2,
        ModelVariableNames.END,
        ModelVariableNames.ACTIVITIES,
    )

    def test_minizinc_solutions_have_no_violation(self) -> None:
        for benchmark in self.BENCHMARKS:
            with self.subTest(benchmark=benchmark):
                path = ProjectPaths.DATA_DIR / f"{benchmark}{self.INSTANCE_EXTENSION}"
                result = MiniZincModelProbe(path).first_solution()
                horaire = Horaire.from_model_variables({name: result[name] for name in self.EMPLOYEE_VARIABLES})
                checker = FeasibilityChecker(load_instance(path))
                self.assertEqual(checker.violations(horaire), [])


class TestVerdictMatchesMiniZinc(unittest.TestCase):
    """Validation croisée : pour chaque cas, le verdict Python est celui de horaire.mzn, horaire fixé.

    La demande étant nulle, MiniZinc ne juge que les contraintes structurelles et les domaines.
    """

    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary_directory = tempfile.TemporaryDirectory()
        instance_path = Path(cls.temporary_directory.name) / f"{SYNTHETIC_NAME}.json"
        instance_path.write_text(json.dumps(synthetic_data(employee_count=1)), encoding="utf-8")
        cls.probe = MiniZincModelProbe(instance_path)
        cls.checker = FeasibilityChecker(synthetic_instance())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary_directory.cleanup()

    @staticmethod
    def fixing_constraints(employee_shift: HoraireEmploye) -> str:
        """Contraintes MiniZinc qui fixent toutes les variables du seul employé à celles de ``employee_shift``."""
        milestones = {
            ModelVariableNames.START: employee_shift.start,
            ModelVariableNames.BREAK1: employee_shift.break1,
            ModelVariableNames.LUNCH: employee_shift.lunch,
            ModelVariableNames.BREAK2: employee_shift.break2,
            ModelVariableNames.END: employee_shift.end,
        }
        constraints = [f"constraint {name}[{EMPLOYEE}] = {value};" for name, value in milestones.items()]
        for position, activity in enumerate(employee_shift.activities, start=ModelIndexing.FIRST_INDEX):
            constraints.append(f"constraint {ModelVariableNames.ACTIVITIES}[{EMPLOYEE}, {position}] = {activity};")
        return "\n".join(constraints)

    def test_verdicts_agree(self) -> None:
        cases = dict(FEASIBLE_SHIFTS)
        cases.update({case: employee_shift for case, (employee_shift, _) in SINGLE_VIOLATION_SHIFTS.items()})
        for case, employee_shift in cases.items():
            with self.subTest(case=case):
                model_says_feasible = self.probe.status_with(self.fixing_constraints(employee_shift)).has_solution()
                self.assertEqual(self.checker.is_feasible(single(employee_shift)), model_says_feasible)


if __name__ == "__main__":
    unittest.main()
