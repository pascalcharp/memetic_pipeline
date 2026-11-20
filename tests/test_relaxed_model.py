"""Tests du modèle assoupli horaire_assoupli.mzn (décision D12) — étape 5c, Pascal.

Tests écrits par Claude, à faire passer sur la branche ``etape-5c-couverture-souple``. Ils appellent MiniZinc.

Trois niveaux :
    - les deux fichiers : le modèle de référence ``horaire.mzn`` reste inchangé, le modèle assoupli existe ;
    - validation croisée Python / MiniZinc : pour des horaires fixés à la main (toutes les variables imposées),
      le modèle assoupli calcule le même coût que ``CostEvaluator``, terme par terme ;
    - une instance où « au moins 1 » est impossible à respecter : le modèle assoupli rend une solution avec une
      violation, le modèle de référence est insatisfiable ; le poids transmis par Python est bien celui utilisé.
"""

import hashlib
import unittest
import warnings
from datetime import timedelta
from typing import Any

import minizinc
from minizinc.error import MiniZincWarning

from src.config import MiniZincConfig, ProjectPaths
from src.memetic.solver import (
    CpSatAdapter,
    DeterministicTimeLimit,
    ModelObjective,
    ModelVariant,
    ModelVariants,
    RelaxedModelNames,
    SolveOutcome,
    SolverOptions,
    SolverRun,
)
from src.model.evaluation import CostEvaluator, PenaltyWeights
from src.model.horaire import Horaire
from src.model.shift_rules import ModelVariableNames
from src.utils.io import InstanceFields, ProblemInstance, parse_instance
from src.utils.minizinc_env import locate_minizinc_driver, lookup_solver
from tests.test_feasibility import REFERENCE_SHIFT, single, synthetic_data
from tests.test_local_search import BENCH_1_OPTIMUM, bench, bench_1_optimum, expected_fixing_constraints, with_employee

# Empreinte SHA-256 de horaire.mzn, le modèle original fourni (D12 : gardé inchangé comme référence).
# Une modification voulue du modèle de référence se décide en équipe, puis met à jour cette empreinte.
REFERENCE_MODEL_SHA256: str = "ba6ba10d0b8cf2826958a84f1ee5d068a60ac72cbcd562027cef7016f9609c88"

GENEROUS_UNITS: float = 5.0
TIME_LIMIT: timedelta = timedelta(seconds=60)

# Instance synthétique à un seul employé, où les deux activités sont demandées à la même période :
# un employé ne peut en couvrir qu'une, donc « au moins 1 » est violée exactement une fois à l'optimum.
IMPOSSIBLE_NAME: str = "couverture_impossible"
CONTESTED_PERIOD: int = 20
CONTESTED_DEMAND: int = 1
VIOLATIONS_AT_OPTIMUM: int = 1

# Deux poids distincts, pour vérifier que le modèle utilise celui transmis par Python.
SMALL_WEIGHT: int = 1_000
LARGE_WEIGHT: int = 50_000


def impossible_coverage_instance() -> ProblemInstance:
    data = synthetic_data(employee_count=1)
    demand = [list(row) for row in data[InstanceFields.DEMAND]]
    demand[CONTESTED_PERIOD - 1] = [CONTESTED_DEMAND] * len(demand[CONTESTED_PERIOD - 1])
    data[InstanceFields.DEMAND] = demand
    return parse_instance(data, name=IMPOSSIBLE_NAME)


def cp_sat(model: ModelVariant, weights: PenaltyWeights = PenaltyWeights()) -> CpSatAdapter:
    return CpSatAdapter(SolverOptions(limit=DeterministicTimeLimit(GENEROUS_UNITS)), model=model, weights=weights)


def solve_quietly(adapter: CpSatAdapter, instance: ProblemInstance) -> SolverRun:
    """Résolution sans l'avertissement « model inconsistency detected » qu'émet MiniZinc pour un modèle UNSAT."""
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", MiniZincWarning)
        return adapter.solve(instance)


def all_fixing_constraints(horaire: Horaire) -> list[str]:
    constraints: set[str] = set()
    for employee in range(1, horaire.employee_count + 1):
        constraints |= expected_fixing_constraints(horaire, employee)
    return sorted(constraints)


class RelaxedModelReading:
    """Résout directement le modèle assoupli, toutes les variables fixées à ``horaire``, et lit ses trois termes.

    Passe par minizinc-python plutôt que par le ``SolverAdapter`` : ``SolverRun`` ne rend ni ``cout_total`` ni
    ``violations_couverture``. Le modèle doit les annoter ``::add_to_output``.
    """

    def __init__(self, instance: ProblemInstance, horaire: Horaire, weights: PenaltyWeights) -> None:
        solver = lookup_solver(MiniZincConfig.DEFAULT_SOLVER_ID, locate_minizinc_driver())
        minizinc_instance = minizinc.Instance(solver, minizinc.Model(ProjectPaths.RELAXED_MODEL_FILE))
        minizinc_instance[InstanceFields.EMPLOYEE_COUNT] = instance.employee_count
        minizinc_instance[InstanceFields.ACTIVITY_COUNT] = instance.activity_count
        minizinc_instance[InstanceFields.PERIOD_COUNT] = instance.period_count
        minizinc_instance[InstanceFields.DEMAND] = instance.demand.tolist()
        minizinc_instance[InstanceFields.OVER_COST] = instance.over_cost.tolist()
        minizinc_instance[InstanceFields.UNDER_COST] = instance.under_cost.tolist()
        minizinc_instance[RelaxedModelNames.COVERAGE_WEIGHT] = weights.coverage_violation
        for constraint in all_fixing_constraints(horaire):
            minizinc_instance.add_string(constraint)
        self.result = minizinc_instance.solve(time_limit=TIME_LIMIT)

    def value(self, name: str) -> Any:
        return self.result[name]


# ---------------------------------------------------------------------------------------------------------------------
# Les deux fichiers
# ---------------------------------------------------------------------------------------------------------------------

class TestModelFiles(unittest.TestCase):

    def test_both_model_files_exist(self) -> None:
        for variant in (ModelVariants.REFERENCE, ModelVariants.RELAXED):
            with self.subTest(variant=variant.name):
                self.assertTrue(variant.path.is_file(), variant.path)

    def test_reference_model_is_unchanged(self) -> None:
        digest = hashlib.sha256(ProjectPaths.REFERENCE_MODEL_FILE.read_bytes()).hexdigest()
        self.assertEqual(digest, REFERENCE_MODEL_SHA256)

    def test_relaxed_model_is_a_distinct_file(self) -> None:
        self.assertNotEqual(ProjectPaths.RELAXED_MODEL_FILE.read_bytes(), ProjectPaths.REFERENCE_MODEL_FILE.read_bytes())


# ---------------------------------------------------------------------------------------------------------------------
# Résolution complète : l'optimum des bench ne change pas
# ---------------------------------------------------------------------------------------------------------------------

class TestBench1Optimum(unittest.TestCase):
    """bench_1 respecte « au moins 1 » à l'optimum : les deux modèles ont le même optimum (94)."""

    def test_both_models_prove_the_same_optimum(self) -> None:
        for variant in (ModelVariants.REFERENCE, ModelVariants.RELAXED):
            with self.subTest(variant=variant.name):
                run = cp_sat(variant).solve(bench("bench_1"))
                self.assertEqual(run.outcome, SolveOutcome.OPTIMAL)
                self.assertEqual(run.objective, BENCH_1_OPTIMUM)


# ---------------------------------------------------------------------------------------------------------------------
# Validation croisée Python / MiniZinc
# ---------------------------------------------------------------------------------------------------------------------

class TestCrossValidation(unittest.TestCase):
    """Horaires structurellement faisables, fixés à la main ; certains violent « au moins 1 »."""

    @classmethod
    def setUpClass(cls) -> None:
        bench_1 = bench("bench_1")
        optimum = bench_1_optimum()
        first_shift = optimum.employees[0]
        cls.cases: dict[str, tuple[ProblemInstance, Horaire]] = {
            "optimum de bench_1": (bench_1, optimum),
            "bench_1, trois quarts identiques": (bench_1, Horaire(employees=(first_shift,) * bench_1.employee_count)),
            "bench_1, l'employé 3 reprend le quart de l'employé 1": (bench_1, with_employee(optimum, 3, first_shift)),
            "couverture impossible, quart de référence": (impossible_coverage_instance(), single(REFERENCE_SHIFT)),
        }
        cls.weights = PenaltyWeights()

    def test_cases_include_coverage_violations(self) -> None:
        violating = [name for name, (instance, horaire) in self.cases.items()
                     if CostEvaluator(instance).evaluate(horaire).coverage_violations > 0]
        self.assertGreaterEqual(len(violating), 2, "la validation croisée doit couvrir des violations de « au moins 1 »")

    def test_cases_are_structurally_feasible(self) -> None:
        for name, (instance, horaire) in self.cases.items():
            with self.subTest(case=name):
                self.assertEqual(CostEvaluator(instance).evaluate(horaire).structural_violations, 0)

    def test_relaxed_model_computes_the_same_cost_as_the_evaluator(self) -> None:
        for name, (instance, horaire) in self.cases.items():
            with self.subTest(case=name):
                expected = CostEvaluator(instance, self.weights).evaluate(horaire)
                reading = RelaxedModelReading(instance, horaire, self.weights)
                self.assertEqual(reading.result.status, minizinc.Status.OPTIMAL_SOLUTION)
                self.assertEqual(reading.value(RelaxedModelNames.COVERAGE_VIOLATIONS), expected.coverage_violations)
                self.assertEqual(reading.value(ModelObjective.TOTAL_COST), expected.coverage_cost)
                self.assertEqual(reading.result.objective, expected.total)


# ---------------------------------------------------------------------------------------------------------------------
# « Au moins 1 » impossible à respecter
# ---------------------------------------------------------------------------------------------------------------------

class TestImpossibleCoverage(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = impossible_coverage_instance()

    def test_reference_model_is_unsatisfiable(self) -> None:
        run = solve_quietly(cp_sat(ModelVariants.REFERENCE), self.instance)
        self.assertEqual(run.outcome, SolveOutcome.UNSATISFIABLE)

    def test_relaxed_model_returns_a_solution_with_one_violation(self) -> None:
        run = cp_sat(ModelVariants.RELAXED).solve(self.instance)
        self.assertEqual(run.outcome, SolveOutcome.OPTIMAL)
        horaire = Horaire.from_model_variables(run.variables)
        cost = CostEvaluator(self.instance).evaluate(horaire)
        self.assertEqual(cost.structural_violations, 0)
        self.assertEqual(cost.coverage_violations, VIOLATIONS_AT_OPTIMUM)
        self.assertEqual(run.objective, cost.total)

    def test_relaxed_model_uses_the_weight_given_by_python(self) -> None:
        small = cp_sat(ModelVariants.RELAXED, PenaltyWeights(coverage_violation=SMALL_WEIGHT)).solve(self.instance)
        large = cp_sat(ModelVariants.RELAXED, PenaltyWeights(coverage_violation=LARGE_WEIGHT)).solve(self.instance)
        # Même nombre de violations à l'optimum, même coût de couverture : seul le poids change l'objectif.
        self.assertEqual(large.objective - small.objective, (LARGE_WEIGHT - SMALL_WEIGHT) * VIOLATIONS_AT_OPTIMUM)


if __name__ == "__main__":
    unittest.main()
