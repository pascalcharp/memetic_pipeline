"""Tests de l'évaluation (src/model/evaluation.py) : décomposition du coût, totaux de couverture, pénalités."""

import dataclasses
import unittest

import numpy as np

from src.config import ProjectPaths
from src.model.evaluation import CostBreakdown, CostEvaluator, EvaluationDefaults, PenaltyWeights
from src.model.feasibility import EmployeeCountMismatchError, FeasibilityChecker
from src.model.horaire import Horaire
from src.model.shift_rules import ModelIndexing, ModelVariableNames
from src.utils.io import InstanceFields, ProblemInstance, load_instance, parse_instance
from tests.minizinc_probe import MiniZincModelProbe
from tests.test_feasibility import (
    FIRST_USEFUL_PERIOD,
    LAST_USEFUL_PERIOD,
    REFERENCE_SHIFT,
    SYNTHETIC_ACTIVITY_COUNT,
    SYNTHETIC_PERIOD_COUNT,
    shift,
    single,
    synthetic_data,
)
from tests.test_horaire import BENCH_1_OPTIMUM_VARIABLES

INSTANCE_EXTENSION: str = ".json"
EVALUATION_INSTANCE_NAME: str = "instance_evaluation"

# Coûts unitaires distincts dans la plage utile, pour repérer toute confusion entre sur- et sous-couverture.
OVER_COST: int = 3
UNDER_COST: int = 5

# Cellules (période, activité) où travaille le quart de référence (10, 14, 19, 28, 37), activités (1, 2, 1, 2) :
#   bloc 1 : 10..13 (4)   pause : 14   bloc 2 : 15..18 (4)   dîner : 19..22
#   bloc 3 : 23..27 (5)   pause : 28   bloc 4 : 29..37 (9)   soit 22 périodes travaillées.
REFERENCE_WORK_CELLS: frozenset[tuple[int, int]] = frozenset(
    {(period, 1) for period in range(10, 14)}
    | {(period, 2) for period in range(15, 19)}
    | {(period, 1) for period in range(23, 28)}
    | {(period, 2) for period in range(29, 38)}
)
REFERENCE_WORKED_PERIODS: int = 22

# Cellules du bloc 4 du quart de référence (activité 2, périodes 29..37).
REFERENCE_BLOCK4_PERIODS: int = 9

# Période de la plage utile après la fin du quart de référence : personne n'y travaille.
PERIOD_AFTER_REFERENCE_SHIFT: int = 40

# Période du bloc 1 du quart de référence (activité 1).
PERIOD_IN_REFERENCE_BLOCK1: int = 12

QUASI_HARD: int = EvaluationDefaults.QUASI_HARD_UNDER_COST


def instance_with(
    demand_cells: dict[tuple[int, int], int] | None = None,
    under_cost_cells: dict[tuple[int, int], int] | None = None,
    over_cost: int = OVER_COST,
    under_cost: int = UNDER_COST,
    employee_count: int = 1,
) -> ProblemInstance:
    """Instance synthétique (plage utile 4..43, 2 activités), coûts uniformes dans la plage utile.

    ``demand_cells`` et ``under_cost_cells`` associent une cellule (période, activité), numérotée à partir de 1,
    à sa demande ou à son sous-coût ; les autres cellules ont une demande nulle et le sous-coût uniforme.
    """
    shape = (SYNTHETIC_PERIOD_COUNT, SYNTHETIC_ACTIVITY_COUNT)
    demand = np.zeros(shape, dtype=np.int64)
    over = np.zeros(shape, dtype=np.int64)
    under = np.zeros(shape, dtype=np.int64)
    useful_rows = slice(FIRST_USEFUL_PERIOD - ModelIndexing.FIRST_INDEX, LAST_USEFUL_PERIOD)
    over[useful_rows, :] = over_cost
    under[useful_rows, :] = under_cost
    for (period, activity), value in (demand_cells or {}).items():
        demand[period - ModelIndexing.FIRST_INDEX, activity - ModelIndexing.FIRST_INDEX] = value
    for (period, activity), value in (under_cost_cells or {}).items():
        under[period - ModelIndexing.FIRST_INDEX, activity - ModelIndexing.FIRST_INDEX] = value

    data = synthetic_data(employee_count)
    data[InstanceFields.DEMAND] = demand.tolist()
    data[InstanceFields.OVER_COST] = over.tolist()
    data[InstanceFields.UNDER_COST] = under.tolist()
    return parse_instance(data, name=EVALUATION_INSTANCE_NAME)


def cells_of(totals: np.ndarray) -> dict[tuple[int, int], int]:
    """Cellules non nulles de ``totals``, numérotées à partir de 1, avec leur valeur."""
    return {
        (period_index + ModelIndexing.FIRST_INDEX, activity_index + ModelIndexing.FIRST_INDEX): int(value)
        for (period_index, activity_index), value in np.ndenumerate(totals)
        if value != 0
    }


def breakdown(
    under: int = 0, over: int = 0, quasi_hard: int = 0, coverage: int = 0, structural: int = 0, penalty: int = 0
) -> CostBreakdown:
    return CostBreakdown(
        under_coverage_cost=under,
        over_coverage_cost=over,
        quasi_hard_cells=quasi_hard,
        coverage_violations=coverage,
        structural_violations=structural,
        penalty_cost=penalty,
    )


class TestCostBreakdown(unittest.TestCase):
    """Propriétés dérivées de la décomposition."""

    def test_coverage_cost_is_under_plus_over(self) -> None:
        self.assertEqual(breakdown(under=5, over=66).coverage_cost, 71)

    def test_total_adds_penalties(self) -> None:
        self.assertEqual(breakdown(under=5, over=66, coverage=1, penalty=1_000_000).total, 1_000_071)

    def test_quasi_hard_cells_do_not_change_the_total(self) -> None:
        # Information de diagnostic : leur coût est déjà dans under_coverage_cost.
        self.assertEqual(breakdown(under=QUASI_HARD, quasi_hard=1).total, QUASI_HARD)

    def test_feasible_without_violation(self) -> None:
        self.assertTrue(breakdown(under=5, over=66, quasi_hard=1).is_feasible)

    def test_infeasible_with_any_violation(self) -> None:
        self.assertFalse(breakdown(coverage=1).is_feasible)
        self.assertFalse(breakdown(structural=1).is_feasible)

    def test_is_frozen(self) -> None:
        with self.assertRaises(dataclasses.FrozenInstanceError):
            breakdown().penalty_cost = 1  # type: ignore[misc]


class TestPenaltyWeights(unittest.TestCase):

    def test_defaults(self) -> None:
        weights = PenaltyWeights()
        self.assertEqual(weights.coverage_violation, EvaluationDefaults.COVERAGE_VIOLATION_PENALTY)
        self.assertEqual(weights.structural_violation, EvaluationDefaults.STRUCTURAL_VIOLATION_PENALTY)

    def test_evaluator_uses_defaults_when_not_given(self) -> None:
        self.assertEqual(CostEvaluator(instance_with()).weights, PenaltyWeights())


class TestCoverageTotals(unittest.TestCase):
    """Le tableau ``total`` de horaire.mzn, cellule par cellule."""

    def test_shape_matches_demand(self) -> None:
        instance = instance_with()
        totals = CostEvaluator(instance).coverage_totals(single(REFERENCE_SHIFT))
        self.assertEqual(totals.shape, instance.demand.shape)

    def test_reference_shift_cell_by_cell(self) -> None:
        totals = CostEvaluator(instance_with()).coverage_totals(single(REFERENCE_SHIFT))
        self.assertEqual(cells_of(totals), dict.fromkeys(REFERENCE_WORK_CELLS, 1))

    def test_employees_add_up(self) -> None:
        horaire = Horaire(employees=(REFERENCE_SHIFT, REFERENCE_SHIFT))
        totals = CostEvaluator(instance_with(employee_count=2)).coverage_totals(horaire)
        self.assertEqual(cells_of(totals), dict.fromkeys(REFERENCE_WORK_CELLS, 2))

    def test_periods_outside_useful_range_are_ignored(self) -> None:
        # Plage utile 4..43 sur 44 périodes. Activité 1 pour le début, activité 2 pour la fin du quart.
        cases = {
            "début avant la plage utile (périodes 2 et 3 hors plage)": (shift(2, 6, 11, 20, 29, (1, 1, 1, 1)), 1),
            "fin après la plage utile (période 44 hors plage)": (shift(16, 26, 31, 39, 44, (2, 2, 2, 2)), 2),
        }
        for name, (employee_shift, activity) in cases.items():
            with self.subTest(name):
                totals = CostEvaluator(instance_with()).coverage_totals(single(employee_shift))
                counted_periods = {period for (period, counted) in cells_of(totals) if counted == activity}
                self.assertTrue(all(FIRST_USEFUL_PERIOD <= period <= LAST_USEFUL_PERIOD for period in counted_periods))

    def test_useful_periods_of_an_overflowing_shift_are_counted(self) -> None:
        # Le quart commence à 2 : les périodes 4 et 5 de son bloc 1 (2..5) sont dans la plage utile.
        totals = CostEvaluator(instance_with()).coverage_totals(single(shift(2, 6, 11, 20, 29, (1, 1, 1, 1))))
        counted = cells_of(totals)
        for period in (FIRST_USEFUL_PERIOD, FIRST_USEFUL_PERIOD + 1):
            self.assertEqual(counted.get((period, 1)), 1)

    def test_activities_outside_domain_are_not_counted(self) -> None:
        # Le bloc 4 (9 périodes) porte une activité invalide ; les 13 autres périodes restent comptées.
        # Une activité négative ne doit pas retomber dans une colonne par l'indexation négative de numpy.
        for invalid_activity in (SYNTHETIC_ACTIVITY_COUNT + 1, ModelIndexing.NO_ACTIVITY, -1):
            with self.subTest(activity=invalid_activity):
                employee_shift = shift(10, 14, 19, 28, 37, activities=(1, 2, 1, invalid_activity))
                totals = CostEvaluator(instance_with()).coverage_totals(single(employee_shift))
                expected = {cell: 1 for cell in REFERENCE_WORK_CELLS if cell[0] < 29}
                self.assertEqual(cells_of(totals), expected)
                self.assertEqual(int(totals.sum()), REFERENCE_WORKED_PERIODS - REFERENCE_BLOCK4_PERIODS)

    def test_overlapping_blocks_count_the_employee_once_per_block(self) -> None:
        # Comme les quatre ``sum`` additionnées de ``total`` dans horaire.mzn : pause1 (25) placée après le dîner (19).
        #   bloc 1 : 10..24 (activité 1)   bloc 2 : 26..18, vide   bloc 3 : 23..27 (activité 1)   bloc 4 : 29..37
        # Les périodes 23 et 24 sont à la fois dans le bloc 1 et dans le bloc 3 : l'employé y compte deux fois.
        overlapping_shift = shift(10, 25, 19, 28, 37, activities=(1, 1, 1, 2))
        totals = CostEvaluator(instance_with()).coverage_totals(single(overlapping_shift))

        expected = (
            {(period, 1): 1 for period in range(10, 28)}
            | {(period, 1): 2 for period in (23, 24)}
            | {(period, 2): 1 for period in range(29, 38)}
        )
        self.assertEqual(cells_of(totals), expected)
        self.assertTrue(FeasibilityChecker(instance_with()).violations(single(overlapping_shift)))


class TestEvaluateHandComputed(unittest.TestCase):
    """Cas calculés à la main, un seul employé sauf mention contraire, quart de référence (22 périodes)."""

    def test_perfect_coverage_costs_nothing(self) -> None:
        instance = instance_with(demand_cells=dict.fromkeys(REFERENCE_WORK_CELLS, 1))
        cost = CostEvaluator(instance).evaluate(single(REFERENCE_SHIFT))
        self.assertEqual(cost, breakdown())
        self.assertTrue(cost.is_feasible)

    def test_over_coverage_only(self) -> None:
        cost = CostEvaluator(instance_with()).evaluate(single(REFERENCE_SHIFT))
        self.assertEqual(cost, breakdown(over=REFERENCE_WORKED_PERIODS * OVER_COST))

    def test_under_coverage_without_violation(self) -> None:
        # Deux employés, demande de 2 à une cellule où un seul travaille :
        # 1 employé manquant, mais « au moins 1 » respecté.
        other_shift = shift(10, 14, 19, 28, 37, activities=(2, 2, 2, 2))
        instance = instance_with(demand_cells={(PERIOD_IN_REFERENCE_BLOCK1, 1): 2}, over_cost=0, employee_count=2)
        cost = CostEvaluator(instance).evaluate(Horaire(employees=(REFERENCE_SHIFT, other_shift)))
        self.assertEqual(cost, breakdown(under=UNDER_COST))

    def test_activity_column_is_respected(self) -> None:
        # Demande sur les cellules du quart de référence, mais activités permutées : tout manque, tout est de trop.
        swapped_shift = shift(10, 14, 19, 28, 37, activities=(2, 1, 2, 1))
        instance = instance_with(demand_cells=dict.fromkeys(REFERENCE_WORK_CELLS, 1))
        cost = CostEvaluator(instance).evaluate(single(swapped_shift))
        violations = REFERENCE_WORKED_PERIODS
        expected = breakdown(
            under=REFERENCE_WORKED_PERIODS * UNDER_COST,
            over=REFERENCE_WORKED_PERIODS * OVER_COST,
            coverage=violations,
            penalty=violations * EvaluationDefaults.COVERAGE_VIOLATION_PENALTY,
        )
        self.assertEqual(cost, expected)

    def test_coverage_violation_is_counted_and_penalized(self) -> None:
        demand = dict.fromkeys(REFERENCE_WORK_CELLS, 1) | {(PERIOD_AFTER_REFERENCE_SHIFT, 1): 1}
        cost = CostEvaluator(instance_with(demand_cells=demand)).evaluate(single(REFERENCE_SHIFT))
        expected = breakdown(under=UNDER_COST, coverage=1, penalty=EvaluationDefaults.COVERAGE_VIOLATION_PENALTY)
        self.assertEqual(cost, expected)
        self.assertFalse(cost.is_feasible)

    def test_uncovered_quasi_hard_cell(self) -> None:
        cell = (PERIOD_AFTER_REFERENCE_SHIFT, 1)
        demand = dict.fromkeys(REFERENCE_WORK_CELLS, 1) | {cell: 1}
        instance = instance_with(demand_cells=demand, under_cost_cells={cell: QUASI_HARD})
        cost = CostEvaluator(instance).evaluate(single(REFERENCE_SHIFT))
        expected = breakdown(
            under=QUASI_HARD, quasi_hard=1, coverage=1, penalty=EvaluationDefaults.COVERAGE_VIOLATION_PENALTY
        )
        self.assertEqual(cost, expected)

    def test_under_covered_quasi_hard_cell_without_violation(self) -> None:
        cell = (PERIOD_IN_REFERENCE_BLOCK1, 1)
        other_shift = shift(10, 14, 19, 28, 37, activities=(2, 2, 2, 2))
        instance = instance_with(
            demand_cells={cell: 2}, under_cost_cells={cell: QUASI_HARD}, over_cost=0, employee_count=2
        )
        cost = CostEvaluator(instance).evaluate(Horaire(employees=(REFERENCE_SHIFT, other_shift)))
        self.assertEqual(cost, breakdown(under=QUASI_HARD, quasi_hard=1))
        self.assertTrue(cost.is_feasible)

    def test_covered_quasi_hard_cell_is_not_counted(self) -> None:
        cell = (PERIOD_IN_REFERENCE_BLOCK1, 1)
        instance = instance_with(
            demand_cells=dict.fromkeys(REFERENCE_WORK_CELLS, 1), under_cost_cells={cell: QUASI_HARD}
        )
        self.assertEqual(CostEvaluator(instance).evaluate(single(REFERENCE_SHIFT)), breakdown())

    def test_structural_violation_is_counted_and_penalized(self) -> None:
        # Quart trop court d'une période (fin - debut = 26) ; la couverture de ses cellules est parfaite.
        short_shift = shift(10, 14, 19, 28, 36)
        demand = {cell: 1 for cell in REFERENCE_WORK_CELLS if cell[0] <= 36}
        instance = instance_with(demand_cells=demand)
        self.assertEqual(len(FeasibilityChecker(instance).violations(single(short_shift))), 1)

        cost = CostEvaluator(instance).evaluate(single(short_shift))
        self.assertEqual(cost, breakdown(structural=1, penalty=EvaluationDefaults.STRUCTURAL_VIOLATION_PENALTY))
        self.assertFalse(cost.is_feasible)

    def test_every_structural_violation_counts(self) -> None:
        # Bloc 4 trop court et quart trop court : autant de violations que FeasibilityChecker en rapporte.
        bad_shift = shift(10, 14, 19, 28, 30)
        instance = instance_with()
        expected_count = len(FeasibilityChecker(instance).violations(single(bad_shift)))
        self.assertGreater(expected_count, 1)
        self.assertEqual(CostEvaluator(instance).evaluate(single(bad_shift)).structural_violations, expected_count)

    def test_infeasible_activity_does_not_crash(self) -> None:
        employee_shift = shift(10, 14, 19, 28, 37, activities=(1, 2, 1, -1))
        cost = CostEvaluator(instance_with()).evaluate(single(employee_shift))
        self.assertEqual(cost.over_coverage_cost, (REFERENCE_WORKED_PERIODS - REFERENCE_BLOCK4_PERIODS) * OVER_COST)
        self.assertEqual(cost.structural_violations, 1)

    def test_custom_weights(self) -> None:
        coverage_weight, structural_weight = 7, 11
        short_shift = shift(10, 14, 19, 28, 36)
        demand = {(PERIOD_AFTER_REFERENCE_SHIFT, 1): 1}
        weights = PenaltyWeights(coverage_violation=coverage_weight, structural_violation=structural_weight)
        evaluator = CostEvaluator(instance_with(demand_cells=demand), weights)
        cost = evaluator.evaluate(single(short_shift))
        self.assertEqual(cost.coverage_violations, 1)
        self.assertEqual(cost.structural_violations, 1)
        self.assertEqual(cost.penalty_cost, coverage_weight + structural_weight)

    def test_employee_count_mismatch(self) -> None:
        horaire = Horaire(employees=(REFERENCE_SHIFT, REFERENCE_SHIFT))
        with self.assertRaises(EmployeeCountMismatchError) as context:
            CostEvaluator(instance_with(employee_count=1)).evaluate(horaire)
        self.assertIn(EVALUATION_INSTANCE_NAME, str(context.exception))


class TestBench1Optimum(unittest.TestCase):
    """Optimum de bench_1 (docs/PROBLEME.md) : coût 94, entièrement dû à la sur-couverture."""

    OPTIMUM_COST: int = 94

    def test_optimum_cost(self) -> None:
        instance = load_instance(ProjectPaths.DATA_DIR / f"bench_1{INSTANCE_EXTENSION}")
        cost = CostEvaluator(instance).evaluate(Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES))
        self.assertEqual(cost, breakdown(over=self.OPTIMUM_COST))


class TestCrossValidationWithMiniZinc(unittest.TestCase):
    """Validation croisée : le coût de couverture est l'objectif (cout_total) d'une solution de horaire.mzn."""

    BENCHMARKS: tuple[str, ...] = ("bench_1", "bench_2", "bench_3")
    EMPLOYEE_VARIABLES: tuple[str, ...] = (
        ModelVariableNames.START,
        ModelVariableNames.BREAK1,
        ModelVariableNames.LUNCH,
        ModelVariableNames.BREAK2,
        ModelVariableNames.END,
        ModelVariableNames.ACTIVITIES,
    )

    def test_coverage_cost_matches_objective(self) -> None:
        for benchmark in self.BENCHMARKS:
            with self.subTest(benchmark=benchmark):
                path = ProjectPaths.DATA_DIR / f"{benchmark}{INSTANCE_EXTENSION}"
                result = MiniZincModelProbe(path).first_solution()
                horaire = Horaire.from_model_variables({name: result[name] for name in self.EMPLOYEE_VARIABLES})

                cost = CostEvaluator(load_instance(path)).evaluate(horaire)
                self.assertEqual(cost.coverage_cost, result.objective)
                self.assertTrue(cost.is_feasible)
                self.assertEqual(cost.penalty_cost, 0)


if __name__ == "__main__":
    unittest.main()
