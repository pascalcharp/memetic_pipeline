"""Tests de l'indirection vers les solveurs (src/memetic/solver.py) : options, traduction, issues, statistiques."""

import dataclasses
import unittest
import warnings
from datetime import timedelta

import minizinc
from minizinc.error import MiniZincWarning

from src.config import ProjectPaths
from src.memetic.solver import (
    CpSatAdapter,
    CpSatFlags,
    DeterministicTimeLimit,
    EffortLimit,
    InvalidSolverOptionsError,
    MiniZincPythonArguments,
    SolveOutcome,
    SolverAdapter,
    SolverDefaults,
    SolverFailureError,
    SolverIds,
    SolverOptions,
    SolverStatistics,
    UnsupportedLimitError,
    WallTimeLimit,
)
from src.model.evaluation import CostEvaluator
from src.model.horaire import Horaire
from src.model.shift_rules import ModelVariableNames
from src.utils.io import load_instance

INSTANCE_EXTENSION: str = ".json"


def bench(name: str):
    return load_instance(ProjectPaths.DATA_DIR / (name + INSTANCE_EXTENSION))


# Optimum de bench_1, prouvé par CP-SAT (test de fumée, étape 0).
BENCH_1_OPTIMUM: int = 94

# Budget largement suffisant pour prouver l'optimum de bench_1 (moins d'une unité est nécessaire).
GENEROUS_DETERMINISTIC_UNITS: float = 5.0
GENEROUS_WALL_SECONDS: float = 30.0

# Budget trop faible pour la moindre solution de bench_5 (aucune solution avec 30 unités, mesuré le 2026-11-08).
TINY_DETERMINISTIC_UNITS: float = 0.5

# Valeurs arbitraires, distinctes des valeurs par défaut, pour vérifier la traduction des options.
SOME_SEED: int = 7
SOME_UNITS: float = 2.5
SOME_SECONDS: float = 3.0
SOME_THREADS: int = 4

# Contraintes ajoutées au modèle.
FIXED_START: int = 4
FIX_FIRST_START: str = "constraint {variable}[1] = {value};".format(variable=ModelVariableNames.START, value=FIXED_START)
# Une période bien au-delà de toute instance : hors du domaine de debut[1], donc insatisfiable.
IMPOSSIBLE_START: str = "constraint {variable}[1] = 1000;".format(variable=ModelVariableNames.START)
MALFORMED_CONSTRAINT: str = "constraint this is not minizinc;"


class FakeLimit(EffortLimit):
    """Limite qu'aucun adaptateur ne comprend."""


def cp_sat(limit: EffortLimit, seed: int = SolverDefaults.SEED) -> CpSatAdapter:
    return CpSatAdapter(SolverOptions(limit=limit, seed=seed))


class TestEffortLimits(unittest.TestCase):

    def test_non_positive_limits_are_rejected(self) -> None:
        for limit_type in (WallTimeLimit, DeterministicTimeLimit):
            for value in (0, -1):
                with self.subTest(limit=limit_type.__name__, value=value):
                    with self.assertRaises(InvalidSolverOptionsError) as context:
                        limit_type(value)
                    self.assertIn(limit_type.__name__, str(context.exception))
                    self.assertIn(str(value), str(context.exception))

    def test_limits_are_frozen(self) -> None:
        with self.assertRaises(dataclasses.FrozenInstanceError):
            WallTimeLimit(SOME_SECONDS).seconds = 1  # type: ignore[misc]


class TestSolverOptions(unittest.TestCase):

    def test_defaults(self) -> None:
        options = SolverOptions()
        self.assertEqual(options.limit, DeterministicTimeLimit(SolverDefaults.DETERMINISTIC_TIME_UNITS))
        self.assertEqual(options.seed, SolverDefaults.SEED)
        self.assertEqual(options.threads, SolverDefaults.THREADS)

    def test_threads_must_be_positive(self) -> None:
        with self.assertRaises(InvalidSolverOptionsError) as context:
            SolverOptions(threads=0)
        self.assertIn("0", str(context.exception))


class TestCpSatAdapterConfiguration(unittest.TestCase):
    """Traduction des options en arguments de minizinc-python, sans lancer le solveur."""

    def test_identity(self) -> None:
        self.assertEqual(CpSatAdapter.solver_id(), SolverIds.CP_SAT)
        self.assertEqual(set(CpSatAdapter.supported_limits()), {DeterministicTimeLimit, WallTimeLimit})

    def test_deterministic_limit(self) -> None:
        options = SolverOptions(limit=DeterministicTimeLimit(SOME_UNITS), seed=SOME_SEED, threads=SOME_THREADS)
        arguments = CpSatAdapter(options).solver_arguments()
        flags = arguments[CpSatFlags.FZN_FLAGS_OPTION]
        self.assertIn("{name}:{value}".format(name=CpSatFlags.MAX_DETERMINISTIC_TIME, value=SOME_UNITS), flags)
        self.assertIn("{name}:{value}".format(name=CpSatFlags.RANDOM_SEED, value=SOME_SEED), flags)
        self.assertEqual(arguments[MiniZincPythonArguments.THREADS], SOME_THREADS)
        self.assertNotIn(MiniZincPythonArguments.TIME_LIMIT, arguments)

    def test_wall_time_limit(self) -> None:
        arguments = cp_sat(WallTimeLimit(SOME_SECONDS), seed=SOME_SEED).solver_arguments()
        self.assertEqual(arguments[MiniZincPythonArguments.TIME_LIMIT], timedelta(seconds=SOME_SECONDS))
        flags = arguments[CpSatFlags.FZN_FLAGS_OPTION]
        self.assertNotIn(CpSatFlags.MAX_DETERMINISTIC_TIME, flags)
        self.assertIn("{name}:{value}".format(name=CpSatFlags.RANDOM_SEED, value=SOME_SEED), flags)

    def test_unsupported_limit_is_rejected_at_construction(self) -> None:
        with self.assertRaises(UnsupportedLimitError) as context:
            CpSatAdapter(SolverOptions(limit=FakeLimit()))
        self.assertIn(SolverIds.CP_SAT, str(context.exception))
        self.assertIn(FakeLimit.__name__, str(context.exception))

    def test_adapter_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            SolverAdapter()  # type: ignore[abstract]


class TestOutcomeTranslation(unittest.TestCase):

    def setUp(self) -> None:
        self.adapter = CpSatAdapter()
        self.instance = bench("bench_1")

    def test_every_status_with_an_outcome(self) -> None:
        expected = {
            minizinc.Status.OPTIMAL_SOLUTION: SolveOutcome.OPTIMAL,
            minizinc.Status.SATISFIED: SolveOutcome.FEASIBLE,
            minizinc.Status.ALL_SOLUTIONS: SolveOutcome.FEASIBLE,
            minizinc.Status.UNSATISFIABLE: SolveOutcome.UNSATISFIABLE,
            minizinc.Status.UNKNOWN: SolveOutcome.NO_SOLUTION,
        }
        for status, outcome in expected.items():
            with self.subTest(status=status.name):
                self.assertEqual(self.adapter._outcome_of(status, self.instance), outcome)

    def test_failure_statuses_raise(self) -> None:
        for status in (minizinc.Status.ERROR, minizinc.Status.UNBOUNDED):
            with self.subTest(status=status.name):
                with self.assertRaises(SolverFailureError) as context:
                    self.adapter._outcome_of(status, self.instance)
                self.assertIn(status.name, str(context.exception))
                self.assertIn(self.instance.name, str(context.exception))

    def test_has_solution(self) -> None:
        self.assertTrue(SolveOutcome.OPTIMAL.has_solution)
        self.assertTrue(SolveOutcome.FEASIBLE.has_solution)
        self.assertFalse(SolveOutcome.UNSATISFIABLE.has_solution)
        self.assertFalse(SolveOutcome.NO_SOLUTION.has_solution)


class TestStatisticsTranslation(unittest.TestCase):

    def test_missing_statistics_are_none(self) -> None:
        self.assertEqual(SolverAdapter._statistics_of({}), SolverStatistics())

    def test_values_are_extracted(self) -> None:
        raw = {"nodes": 3, "failures": 5.0, "propagations": 8, "solveTime": timedelta(seconds=1), "other": 13}
        expected = SolverStatistics(nodes=3, failures=5, propagations=8, solve_time=timedelta(seconds=1))
        self.assertEqual(SolverAdapter._statistics_of(raw), expected)


class TestCpSatSolve(unittest.TestCase):
    """Résolutions réelles avec CP-SAT."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.bench_1 = bench("bench_1")
        cls.optimum_run = cp_sat(DeterministicTimeLimit(GENEROUS_DETERMINISTIC_UNITS)).solve(cls.bench_1)

    def test_bench_1_optimum_is_proved(self) -> None:
        self.assertEqual(self.optimum_run.outcome, SolveOutcome.OPTIMAL)
        self.assertEqual(self.optimum_run.objective, BENCH_1_OPTIMUM)

    def test_variables_build_an_horaire_with_the_same_cost(self) -> None:
        horaire = Horaire.from_model_variables(self.optimum_run.variables)
        self.assertEqual(horaire.employee_count, self.bench_1.employee_count)
        cost = CostEvaluator(self.bench_1).evaluate(horaire)
        self.assertEqual(cost.coverage_cost, self.optimum_run.objective)
        self.assertTrue(cost.is_feasible)

    def test_cp_sat_statistics_are_reported(self) -> None:
        statistics = self.optimum_run.statistics
        self.assertIsNotNone(statistics.failures)
        self.assertIsNotNone(statistics.propagations)
        self.assertIsInstance(statistics.solve_time, timedelta)

    def test_deterministic_limit_is_reproducible(self) -> None:
        adapter = cp_sat(DeterministicTimeLimit(GENEROUS_DETERMINISTIC_UNITS), seed=SOME_SEED)
        first, second = adapter.solve(self.bench_1), adapter.solve(self.bench_1)
        self.assertEqual(first.objective, second.objective)
        self.assertEqual(first.variables, second.variables)
        self.assertEqual(first.statistics.failures, second.statistics.failures)
        self.assertEqual(first.statistics.propagations, second.statistics.propagations)

    def test_wall_time_limit(self) -> None:
        run = cp_sat(WallTimeLimit(GENEROUS_WALL_SECONDS)).solve(self.bench_1)
        self.assertEqual(run.outcome, SolveOutcome.OPTIMAL)
        self.assertEqual(run.objective, BENCH_1_OPTIMUM)

    def test_extra_constraint_is_respected(self) -> None:
        run = CpSatAdapter().solve(self.bench_1, extra_constraints=[FIX_FIRST_START])
        self.assertTrue(run.outcome.has_solution)
        self.assertEqual(run.variables[ModelVariableNames.START][0], FIXED_START)
        self.assertGreaterEqual(run.objective, BENCH_1_OPTIMUM)

    def test_impossible_constraint_is_unsatisfiable(self) -> None:
        # MiniZinc avertit (« model inconsistency detected ») : c'est précisément le cas testé.
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", MiniZincWarning)
            run = CpSatAdapter().solve(self.bench_1, extra_constraints=[IMPOSSIBLE_START])
        self.assertEqual(run.outcome, SolveOutcome.UNSATISFIABLE)
        self.assertIsNone(run.variables)
        self.assertIsNone(run.objective)

    def test_malformed_constraint_is_a_failure(self) -> None:
        with self.assertRaises(SolverFailureError) as context:
            CpSatAdapter().solve(self.bench_1, extra_constraints=[MALFORMED_CONSTRAINT])
        self.assertIn(self.bench_1.name, str(context.exception))
        self.assertIn(SolverIds.CP_SAT, str(context.exception))

    def test_exhausted_budget_without_solution(self) -> None:
        run = cp_sat(DeterministicTimeLimit(TINY_DETERMINISTIC_UNITS)).solve(bench("bench_5"))
        self.assertEqual(run.outcome, SolveOutcome.NO_SOLUTION)
        self.assertIsNone(run.variables)
        self.assertIsNone(run.objective)


if __name__ == "__main__":
    unittest.main()
