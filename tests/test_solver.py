"""Tests de l'indirection vers les solveurs (src/memetic/solver.py) : options, traduction, issues, statistiques."""

import dataclasses
import unittest
import warnings
from datetime import timedelta
from unittest import mock

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
    ModelObjective,
    ModelVariants,
    RelaxedModelNames,
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
from src.model.evaluation import CostEvaluator, PenaltyWeights
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
SOME_DETERMINISTIC_TIME: float = 0.25
SOME_SECONDS: float = 3.0
SOME_THREADS: int = 4
SOME_WEIGHT: int = 123
OTHER_WEIGHT: int = 456

# Contraintes ajoutées au modèle.
FIXED_START: int = 4
FIX_FIRST_START: str = "constraint {variable}[1] = {value};".format(variable=ModelVariableNames.START, value=FIXED_START)
# Une période bien au-delà de toute instance : hors du domaine de debut[1], donc insatisfiable.
IMPOSSIBLE_START: str = "constraint {variable}[1] = 1000;".format(variable=ModelVariableNames.START)

# Étape 12-0 : avec le minizinc.Model réutilisé, un appel ne refait plus qu'une analyse d'interface
# (``--model-interface-only``), celle qui suit les contraintes ajoutées ; il en faisait deux.
INTERFACE_ANALYSES_PER_REUSED_CALL: int = 1
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


class TestModelVariants(unittest.TestCase):
    """Les deux modèles (D12) et leurs paramètres propres ; sans MiniZinc."""

    def test_reference_variant(self) -> None:
        self.assertEqual(ModelVariants.REFERENCE.path, ProjectPaths.REFERENCE_MODEL_FILE)
        self.assertEqual(ModelVariants.REFERENCE.objective, ModelObjective.TOTAL_COST)
        self.assertFalse(ModelVariants.REFERENCE.penalizes_coverage)

    def test_relaxed_variant(self) -> None:
        self.assertEqual(ModelVariants.RELAXED.path, ProjectPaths.RELAXED_MODEL_FILE)
        self.assertEqual(ModelVariants.RELAXED.objective, ModelObjective.PENALIZED_COST)
        self.assertTrue(ModelVariants.RELAXED.penalizes_coverage)

    def test_variants_are_frozen(self) -> None:
        with self.assertRaises(dataclasses.FrozenInstanceError):
            ModelVariants.RELAXED.objective = ModelObjective.TOTAL_COST  # type: ignore[misc]

    def test_reference_model_has_no_parameter(self) -> None:
        self.assertEqual(ModelVariants.REFERENCE.parameters(PenaltyWeights()), {})

    def test_relaxed_model_receives_the_coverage_weight(self) -> None:
        self.assertEqual(
            ModelVariants.RELAXED.parameters(PenaltyWeights()),
            {RelaxedModelNames.COVERAGE_WEIGHT: PenaltyWeights().coverage_violation},
        )

    def test_relaxed_model_receives_a_custom_weight(self) -> None:
        weights = PenaltyWeights(coverage_violation=SOME_WEIGHT, structural_violation=OTHER_WEIGHT)
        self.assertEqual(ModelVariants.RELAXED.parameters(weights), {RelaxedModelNames.COVERAGE_WEIGHT: SOME_WEIGHT})


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

    def test_solver_log_is_requested_for_the_deterministic_time(self) -> None:
        # Étape 10d : le temps déterministe consommé n'est rapporté que dans le journal du solveur (-v).
        for limit in (DeterministicTimeLimit(SOME_UNITS), WallTimeLimit(SOME_SECONDS)):
            with self.subTest(limit=type(limit).__name__):
                self.assertIs(cp_sat(limit).solver_arguments()[CpSatFlags.VERBOSE_SOLVING_OPTION], True)

    def test_unsupported_limit_is_rejected_at_construction(self) -> None:
        with self.assertRaises(UnsupportedLimitError) as context:
            CpSatAdapter(SolverOptions(limit=FakeLimit()))
        self.assertIn(SolverIds.CP_SAT, str(context.exception))
        self.assertIn(FakeLimit.__name__, str(context.exception))

    def test_relaxed_model_and_default_weights_by_default(self) -> None:
        adapter = CpSatAdapter()
        self.assertEqual(adapter.model, ModelVariants.RELAXED)
        self.assertEqual(adapter.weights, PenaltyWeights())

    def test_model_and_weights_are_kept(self) -> None:
        weights = PenaltyWeights(coverage_violation=SOME_WEIGHT)
        adapter = CpSatAdapter(model=ModelVariants.REFERENCE, weights=weights)
        self.assertEqual(adapter.model, ModelVariants.REFERENCE)
        self.assertEqual(adapter.weights, weights)

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

    def test_deterministic_time_is_passed_through(self) -> None:
        statistics = SolverAdapter._statistics_of({}, deterministic_time=SOME_DETERMINISTIC_TIME)
        self.assertEqual(statistics, SolverStatistics(deterministic_time=SOME_DETERMINISTIC_TIME))


class TestDeterministicTimeParsing(unittest.TestCase):
    """Étape 10d : lecture du temps déterministe dans les commentaires du journal de CP-SAT."""

    def test_reported_line_is_parsed(self) -> None:
        comments = ["%% Parameters: max_deterministic_time: 5\n", "%% deterministic_time: 0.253438\n", "%% gap: 0\n"]
        self.assertAlmostEqual(CpSatAdapter.deterministic_time_of(comments), 0.253438)

    def test_scientific_notation_is_parsed(self) -> None:
        self.assertAlmostEqual(CpSatAdapter.deterministic_time_of(["%% deterministic_time: 1.5e-05\n"]), 1.5e-05)

    def test_last_reported_value_wins(self) -> None:
        comments = ["%% deterministic_time: 0.1\n", "%% deterministic_time: 0.3\n"]
        self.assertAlmostEqual(CpSatAdapter.deterministic_time_of(comments), 0.3)

    def test_missing_or_parameter_only_is_none(self) -> None:
        self.assertIsNone(CpSatAdapter.deterministic_time_of([]))
        self.assertIsNone(CpSatAdapter.deterministic_time_of(["%% Parameters: max_deterministic_time: 5\n"]))


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

    def test_deterministic_time_is_reported_within_the_limit_and_reproducible(self) -> None:
        deterministic_time = self.optimum_run.statistics.deterministic_time
        self.assertIsInstance(deterministic_time, float)
        self.assertGreater(deterministic_time, 0.0)
        self.assertLessEqual(deterministic_time, GENEROUS_DETERMINISTIC_UNITS)
        again = cp_sat(DeterministicTimeLimit(GENEROUS_DETERMINISTIC_UNITS)).solve(self.bench_1)
        self.assertEqual(again.statistics.deterministic_time, deterministic_time)

    def test_solver_log_does_not_change_the_search(self) -> None:
        # Le journal (-v) ne sert qu'à lire le temps déterministe : sans lui, la recherche est la même.
        class QuietCpSatAdapter(CpSatAdapter):
            def solver_arguments(self):
                arguments = super().solver_arguments()
                del arguments[CpSatFlags.VERBOSE_SOLVING_OPTION]
                return arguments

        limit = DeterministicTimeLimit(GENEROUS_DETERMINISTIC_UNITS)
        quiet = QuietCpSatAdapter(SolverOptions(limit=limit)).solve(self.bench_1)
        self.assertEqual(quiet.objective, self.optimum_run.objective)
        self.assertEqual(quiet.variables, self.optimum_run.variables)
        self.assertEqual(quiet.statistics.failures, self.optimum_run.statistics.failures)
        self.assertEqual(quiet.statistics.propagations, self.optimum_run.statistics.propagations)
        self.assertIsNone(quiet.statistics.deterministic_time)

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


class TestSharedMiniZincModel(unittest.TestCase):
    """Étape 12-0 : l'adaptateur réutilise son ``minizinc.Model`` d'un appel à l'autre, sans fuite entre appels."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.bench_1 = bench("bench_1")

    @staticmethod
    def count_interface_analyses(adapter: CpSatAdapter, instance, extra_constraints) -> int:
        """Nombre d'analyses d'interface (``minizinc.Instance.analyse``) lancées par un appel à ``solve``."""
        with mock.patch.object(
                minizinc.Instance, "analyse", autospec=True, side_effect=minizinc.Instance.analyse
        ) as analyse:
            adapter.solve(instance, extra_constraints=extra_constraints)
        return analyse.call_count

    def test_reused_call_makes_a_single_interface_analysis(self) -> None:
        adapter = CpSatAdapter()
        adapter.solve(self.bench_1, extra_constraints=[FIX_FIRST_START])
        analyses = self.count_interface_analyses(adapter, self.bench_1, [FIX_FIRST_START])
        self.assertEqual(analyses, INTERFACE_ANALYSES_PER_REUSED_CALL)

    def test_extra_constraints_do_not_leak_into_the_next_call(self) -> None:
        adapter = CpSatAdapter()
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", MiniZincWarning)
            impossible = adapter.solve(self.bench_1, extra_constraints=[IMPOSSIBLE_START])
        unconstrained = adapter.solve(self.bench_1)
        self.assertEqual(impossible.outcome, SolveOutcome.UNSATISFIABLE)
        self.assertEqual(unconstrained.outcome, SolveOutcome.OPTIMAL)
        self.assertEqual(unconstrained.objective, BENCH_1_OPTIMUM)

    def test_fixed_value_does_not_leak_into_the_next_call(self) -> None:
        adapter = CpSatAdapter()
        adapter.solve(self.bench_1, extra_constraints=[FIX_FIRST_START])
        reused = adapter.solve(self.bench_1)
        fresh = CpSatAdapter().solve(self.bench_1)
        self.assertEqual(reused.variables, fresh.variables)

    def test_reused_adapter_matches_a_fresh_adapter(self) -> None:
        limit = DeterministicTimeLimit(GENEROUS_DETERMINISTIC_UNITS)
        reused_adapter = cp_sat(limit, seed=SOME_SEED)
        reused_adapter.solve(self.bench_1, extra_constraints=[FIX_FIRST_START])
        reused = reused_adapter.solve(self.bench_1, extra_constraints=[FIX_FIRST_START])
        fresh = cp_sat(limit, seed=SOME_SEED).solve(self.bench_1, extra_constraints=[FIX_FIRST_START])
        self.assertEqual(reused.objective, fresh.objective)
        self.assertEqual(reused.variables, fresh.variables)
        self.assertEqual(reused.statistics.failures, fresh.statistics.failures)
        self.assertEqual(reused.statistics.propagations, fresh.statistics.propagations)


if __name__ == "__main__":
    unittest.main()
