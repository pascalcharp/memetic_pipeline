"""Tests de la recherche locale (src/memetic/local_search.py) — étape 5b, Pascal.

Trois niveaux :
    - contrat du scaffold (interfaces, résultat figé, gabarits des contraintes) ;
    - logique Python sans MiniZinc : voisinage, contraintes de fixation, borne de coût, et ``improve`` avec un
      adaptateur scénarisé (``ScriptedAdapter``) qui rend un ``SolverRun`` choisi d'avance ;
    - résolutions réelles avec CP-SAT sur bench_1 (et bench_5 pour un budget épuisé).

Employés numérotés à partir de 1, comme dans MiniZinc.
"""

import dataclasses
import random
import unittest
from collections.abc import Sequence
from typing import Any

from src.memetic.local_search import (
    InvalidNeighborhoodError,
    LocalSearchConstraints,
    LocalSearchResult,
    LocalSolver,
    MiniZincLocalSolver,
    Neighborhood,
    NeighborhoodDefaults,
    RandomEmployeesNeighborhood,
)
from src.memetic.solver import (
    CpSatAdapter,
    DeterministicTimeLimit,
    EffortLimit,
    ModelObjective,
    SolveOutcome,
    SolverAdapter,
    SolverOptions,
    SolverRun,
    SolverStatistics,
)
from src.config import ProjectPaths
from src.model.evaluation import CostEvaluator
from src.model.feasibility import FeasibilityChecker
from src.model.horaire import Horaire, HoraireEmploye
from src.model.shift_rules import ModelIndexing, ModelVariableNames
from src.utils.io import ProblemInstance, load_instance
from tests.fixtures import synthetic_instance
from tests.test_feasibility import REFERENCE_SHIFT, shift, single
from tests.test_horaire import BENCH_1_OPTIMUM_VARIABLES

INSTANCE_EXTENSION: str = ".json"
SEED: int = 0
OTHER_SEED: int = 1

# Optimum de bench_1, prouvé par CP-SAT (étape 0).
BENCH_1_OPTIMUM: int = 94

# Budget largement suffisant pour bench_1 ; trop faible pour la moindre solution de bench_5 (mesures du 2026-11-08).
GENEROUS_UNITS: float = 5.0
TINY_UNITS: float = 0.5

# Quart trop court d'une période (fin - debut = 26) : structurellement infaisable sur l'instance synthétique.
SHORT_SHIFT: HoraireEmploye = shift(10, 14, 19, 28, 36)

# Quart dont tous les jalons sont hors domaine : infaisable sur toute instance.
DEGENERATE_SHIFT: HoraireEmploye = HoraireEmploye(start=1, break1=1, lunch=1, break2=1, end=1, activities=(1, 1, 1, 1))

# Nombre de tirages pour vérifier qu'un voisinage aléatoire finit par libérer chaque employé.
DRAW_COUNT: int = 200

MILESTONE_VARIABLES: tuple[str, ...] = (
    ModelVariableNames.START,
    ModelVariableNames.BREAK1,
    ModelVariableNames.LUNCH,
    ModelVariableNames.BREAK2,
    ModelVariableNames.END,
)


def bench(name: str) -> ProblemInstance:
    return load_instance(ProjectPaths.DATA_DIR / (name + INSTANCE_EXTENSION))


def bench_1_optimum() -> Horaire:
    return Horaire.from_model_variables(BENCH_1_OPTIMUM_VARIABLES)


def with_employee(horaire: Horaire, employee: int, replacement: HoraireEmploye) -> Horaire:
    """Copie de ``horaire`` où l'employé ``employee`` (à partir de 1) a le quart ``replacement``."""
    employees = list(horaire.employees)
    employees[employee - ModelIndexing.FIRST_INDEX] = replacement
    return Horaire(employees=tuple(employees))


def expected_fixing_constraints(horaire: Horaire, employee: int) -> set[str]:
    """Les neuf contraintes qui fixent l'employé ``employee`` : cinq jalons et quatre activités."""
    employee_shift = horaire.employees[employee - ModelIndexing.FIRST_INDEX]
    milestone_values = (employee_shift.start, employee_shift.break1, employee_shift.lunch,
                        employee_shift.break2, employee_shift.end)
    constraints = {
        LocalSearchConstraints.FIX_MILESTONE.format(variable=variable, employee=employee, value=value)
        for variable, value in zip(MILESTONE_VARIABLES, milestone_values)
    }
    for block, activity in enumerate(employee_shift.activities, start=ModelIndexing.FIRST_INDEX):
        constraints.add(
            LocalSearchConstraints.FIX_ACTIVITY.format(
                variable=ModelVariableNames.ACTIVITIES, employee=employee, block=block, value=activity
            )
        )
    return constraints


def model_variables(horaire: Horaire) -> dict[str, list[Any]]:
    """Variables de ``horaire`` sous la forme de ``SolverRun.variables`` (inverse de ``from_model_variables``)."""
    return {
        ModelVariableNames.START: [employee.start for employee in horaire.employees],
        ModelVariableNames.BREAK1: [employee.break1 for employee in horaire.employees],
        ModelVariableNames.LUNCH: [employee.lunch for employee in horaire.employees],
        ModelVariableNames.BREAK2: [employee.break2 for employee in horaire.employees],
        ModelVariableNames.END: [employee.end for employee in horaire.employees],
        ModelVariableNames.ACTIVITIES: [list(employee.activities) for employee in horaire.employees],
    }


SOME_STATISTICS: SolverStatistics = SolverStatistics(failures=3, propagations=5)


class ScriptedAdapter(SolverAdapter):
    """Adaptateur sans MiniZinc : rend ``run`` à chaque appel et note les contraintes reçues."""

    def __init__(self, run: SolverRun) -> None:
        # Pas d'appel à super().__init__ : il localiserait MiniZinc.
        self.run = run
        self.received_constraints: list[list[str]] = []

    @classmethod
    def solver_id(cls) -> str:
        return "scripted"

    @classmethod
    def supported_limits(cls) -> tuple[type[EffortLimit], ...]:
        return (DeterministicTimeLimit,)

    def solver_arguments(self) -> dict[str, Any]:
        return {}

    def solve(self, instance: ProblemInstance, extra_constraints: Sequence[str] = ()) -> SolverRun:
        self.received_constraints.append(list(extra_constraints))
        return self.run


class FixedNeighborhood(Neighborhood):
    """Voisinage qui libère toujours les mêmes employés et note le générateur reçu."""

    def __init__(self, freed: frozenset[int]) -> None:
        self.freed = freed
        self.received_rngs: list[random.Random] = []

    def select(self, horaire: Horaire, rng: random.Random) -> frozenset[int]:
        self.received_rngs.append(rng)
        return self.freed


def cp_sat_solver(instance: ProblemInstance, size: int, units: float = GENEROUS_UNITS) -> MiniZincLocalSolver:
    return MiniZincLocalSolver(
        instance,
        CpSatAdapter(SolverOptions(limit=DeterministicTimeLimit(units))),
        RandomEmployeesNeighborhood(instance, size=size),
        CostEvaluator(instance),
    )


# ---------------------------------------------------------------------------------------------------------------------
# Contrat du scaffold
# ---------------------------------------------------------------------------------------------------------------------

class TestScaffoldContract(unittest.TestCase):

    def test_interfaces_are_abstract(self) -> None:
        for interface in (Neighborhood, LocalSolver):
            with self.subTest(interface=interface.__name__):
                with self.assertRaises(TypeError):
                    interface()  # type: ignore[abstract]

    def test_result_is_frozen(self) -> None:
        result = LocalSearchResult(
            horaire=single(REFERENCE_SHIFT),
            outcome=SolveOutcome.OPTIMAL,
            freed_employees=frozenset({1}),
            statistics=SolverStatistics(),
        )
        with self.assertRaises(dataclasses.FrozenInstanceError):
            result.outcome = SolveOutcome.FEASIBLE  # type: ignore[misc]

    def test_constraint_templates(self) -> None:
        self.assertEqual(
            LocalSearchConstraints.FIX_MILESTONE.format(variable=ModelVariableNames.START, employee=2, value=10),
            "constraint debut[2] = 10;",
        )
        self.assertEqual(
            LocalSearchConstraints.FIX_ACTIVITY.format(variable=ModelVariableNames.ACTIVITIES, employee=2, block=3, value=1),
            "constraint activites[2, 3] = 1;",
        )
        self.assertEqual(
            LocalSearchConstraints.COST_BOUND.format(objective=ModelObjective.TOTAL_COST, bound=94),
            "constraint cout_total <= 94;",
        )


# ---------------------------------------------------------------------------------------------------------------------
# Voisinage
# ---------------------------------------------------------------------------------------------------------------------

class TestRandomEmployeesNeighborhood(unittest.TestCase):
    """Instance synthétique à demande nulle, trois employés ; sans MiniZinc."""

    EMPLOYEE_COUNT: int = 3
    ALL_EMPLOYEES: frozenset[int] = frozenset({1, 2, 3})
    INFEASIBLE_EMPLOYEE: int = 2

    def setUp(self) -> None:
        self.instance = synthetic_instance(self.EMPLOYEE_COUNT)
        self.feasible = Horaire(employees=(REFERENCE_SHIFT,) * self.EMPLOYEE_COUNT)
        self.one_infeasible = with_employee(self.feasible, self.INFEASIBLE_EMPLOYEE, SHORT_SHIFT)

    def select(self, horaire: Horaire, size: int, seed: int = SEED) -> frozenset[int]:
        return RandomEmployeesNeighborhood(self.instance, size=size).select(horaire, random.Random(seed))

    def test_default_size(self) -> None:
        self.assertEqual(RandomEmployeesNeighborhood(self.instance).size, NeighborhoodDefaults.RANDOM_EMPLOYEE_COUNT)

    def test_negative_size_is_rejected(self) -> None:
        with self.assertRaises(InvalidNeighborhoodError) as context:
            RandomEmployeesNeighborhood(self.instance, size=-1)
        self.assertIn("-1", str(context.exception))

    def test_frees_exactly_size_feasible_employees(self) -> None:
        for size in range(self.EMPLOYEE_COUNT + 1):
            with self.subTest(size=size):
                freed = self.select(self.feasible, size)
                self.assertEqual(len(freed), size)
                self.assertLessEqual(freed, self.ALL_EMPLOYEES)

    def test_size_beyond_employee_count_frees_everyone(self) -> None:
        self.assertEqual(self.select(self.feasible, self.EMPLOYEE_COUNT + 5), self.ALL_EMPLOYEES)

    def test_infeasible_employee_is_always_freed(self) -> None:
        self.assertEqual(self.select(self.one_infeasible, 0), frozenset({self.INFEASIBLE_EMPLOYEE}))
        for seed in range(DRAW_COUNT):
            with self.subTest(seed=seed):
                freed = self.select(self.one_infeasible, 1, seed)
                self.assertIn(self.INFEASIBLE_EMPLOYEE, freed)
                # Un employé faisable tiré au hasard, en plus de l'employé infaisable.
                self.assertEqual(len(freed), 2)

    def test_same_seed_same_selection(self) -> None:
        self.assertEqual(self.select(self.feasible, 1, SEED), self.select(self.feasible, 1, SEED))

    def test_every_employee_is_eventually_freed(self) -> None:
        drawn = set()
        for seed in range(DRAW_COUNT):
            drawn |= self.select(self.feasible, 1, seed)
        self.assertEqual(drawn, self.ALL_EMPLOYEES)


# ---------------------------------------------------------------------------------------------------------------------
# Contraintes ajoutées au sous-problème
# ---------------------------------------------------------------------------------------------------------------------

class TestSubproblemConstraints(unittest.TestCase):
    """Contraintes de fixation et borne de coût, sur l'optimum de bench_1 ; sans MiniZinc."""

    def setUp(self) -> None:
        self.instance = bench("bench_1")
        self.optimum = bench_1_optimum()
        self.solver = MiniZincLocalSolver(
            self.instance, ScriptedAdapter(SolverRun(SolveOutcome.NO_SOLUTION, None, None, SolverStatistics())),
            FixedNeighborhood(frozenset()), CostEvaluator(self.instance),
        )

    def test_non_freed_employees_are_fixed(self) -> None:
        constraints = self.solver.fixing_constraints(self.optimum, frozenset({2}))
        expected = expected_fixing_constraints(self.optimum, 1) | expected_fixing_constraints(self.optimum, 3)
        self.assertEqual(len(constraints), len(expected))
        self.assertEqual(set(constraints), expected)

    def test_nobody_freed_fixes_everyone(self) -> None:
        constraints = self.solver.fixing_constraints(self.optimum, frozenset())
        expected = set().union(*(expected_fixing_constraints(self.optimum, employee) for employee in (1, 2, 3)))
        self.assertEqual(set(constraints), expected)

    def test_everyone_freed_fixes_nothing(self) -> None:
        self.assertEqual(self.solver.fixing_constraints(self.optimum, frozenset({1, 2, 3})), [])

    def test_feasible_input_gets_its_coverage_cost_as_bound(self) -> None:
        expected = LocalSearchConstraints.COST_BOUND.format(objective=ModelObjective.TOTAL_COST, bound=BENCH_1_OPTIMUM)
        self.assertEqual(self.solver.cost_bound_constraints(self.optimum), [expected])

    def test_structurally_infeasible_input_gets_no_bound(self) -> None:
        infeasible = with_employee(self.optimum, 1, DEGENERATE_SHIFT)
        self.assertEqual(self.solver.cost_bound_constraints(infeasible), [])

    def test_coverage_violation_gets_no_bound(self) -> None:
        identical = Horaire(employees=(self.optimum.employees[0],) * self.instance.employee_count)
        cost = CostEvaluator(self.instance).evaluate(identical)
        self.assertEqual(cost.structural_violations, 0)
        self.assertGreater(cost.coverage_violations, 0)
        self.assertEqual(self.solver.cost_bound_constraints(identical), [])


# ---------------------------------------------------------------------------------------------------------------------
# improve, avec un adaptateur scénarisé
# ---------------------------------------------------------------------------------------------------------------------

class TestImproveWithScriptedAdapter(unittest.TestCase):
    """Orchestration de ``improve`` : ce qui est demandé au solveur et ce qui est rendu ; sans MiniZinc."""

    FREED: frozenset[int] = frozenset({2})

    def setUp(self) -> None:
        self.instance = bench("bench_1")
        self.optimum = bench_1_optimum()
        self.neighborhood = FixedNeighborhood(self.FREED)

    def improve(self, run: SolverRun, horaire: Horaire) -> tuple[LocalSearchResult, ScriptedAdapter, MiniZincLocalSolver]:
        adapter = ScriptedAdapter(run)
        solver = MiniZincLocalSolver(self.instance, adapter, self.neighborhood, CostEvaluator(self.instance))
        return solver.improve(horaire, random.Random(SEED)), adapter, solver

    def test_solution_becomes_the_result(self) -> None:
        # Un horaire différent de l'entrée : l'employé 2 reçoit le quart de l'employé 3.
        other = with_employee(self.optimum, 2, self.optimum.employees[2])
        run = SolverRun(SolveOutcome.FEASIBLE, model_variables(other), 100, SOME_STATISTICS)
        result, _, _ = self.improve(run, self.optimum)
        self.assertEqual(result.horaire, other)
        self.assertEqual(result.outcome, SolveOutcome.FEASIBLE)
        self.assertEqual(result.freed_employees, self.FREED)
        self.assertEqual(result.statistics, SOME_STATISTICS)

    def test_no_solution_returns_the_input(self) -> None:
        for outcome in (SolveOutcome.UNSATISFIABLE, SolveOutcome.NO_SOLUTION):
            with self.subTest(outcome=outcome.name):
                result, _, _ = self.improve(SolverRun(outcome, None, None, SOME_STATISTICS), self.optimum)
                self.assertIs(result.horaire, self.optimum)
                self.assertEqual(result.outcome, outcome)
                self.assertEqual(result.freed_employees, self.FREED)
                self.assertEqual(result.statistics, SOME_STATISTICS)

    def test_solver_receives_fixing_constraints_and_bound(self) -> None:
        run = SolverRun(SolveOutcome.OPTIMAL, model_variables(self.optimum), BENCH_1_OPTIMUM, SOME_STATISTICS)
        _, adapter, solver = self.improve(run, self.optimum)
        self.assertEqual(len(adapter.received_constraints), 1)
        expected = solver.fixing_constraints(self.optimum, self.FREED) + solver.cost_bound_constraints(self.optimum)
        self.assertEqual(sorted(adapter.received_constraints[0]), sorted(expected))

    def test_neighborhood_receives_the_generator(self) -> None:
        adapter = ScriptedAdapter(SolverRun(SolveOutcome.NO_SOLUTION, None, None, SOME_STATISTICS))
        solver = MiniZincLocalSolver(self.instance, adapter, self.neighborhood, CostEvaluator(self.instance))
        rng = random.Random(SEED)
        solver.improve(self.optimum, rng)
        self.assertEqual(self.neighborhood.received_rngs, [rng])


# ---------------------------------------------------------------------------------------------------------------------
# Résolutions réelles avec CP-SAT
# ---------------------------------------------------------------------------------------------------------------------

class TestImproveWithCpSat(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.instance = bench("bench_1")
        cls.optimum = bench_1_optimum()
        cls.evaluator = CostEvaluator(cls.instance)
        cls.checker = FeasibilityChecker(cls.instance)

    def assert_non_freed_unchanged(self, before: Horaire, result: LocalSearchResult) -> None:
        for employee, (old_shift, new_shift) in enumerate(zip(before.employees, result.horaire.employees),
                                                          start=ModelIndexing.FIRST_INDEX):
            if employee not in result.freed_employees:
                with self.subTest(employee=employee):
                    self.assertEqual(new_shift, old_shift)

    def test_feasible_input_is_never_worse(self) -> None:
        result = cp_sat_solver(self.instance, size=1).improve(self.optimum, random.Random(SEED))
        self.assertTrue(result.outcome.has_solution)
        self.assertEqual(len(result.freed_employees), 1)
        self.assert_non_freed_unchanged(self.optimum, result)
        self.assertLessEqual(self.evaluator.evaluate(result.horaire).coverage_cost, BENCH_1_OPTIMUM)

    def test_infeasible_employee_is_repaired(self) -> None:
        broken = with_employee(self.optimum, 1, DEGENERATE_SHIFT)
        result = cp_sat_solver(self.instance, size=0).improve(broken, random.Random(SEED))
        self.assertEqual(result.freed_employees, frozenset({1}))
        self.assertEqual(result.outcome, SolveOutcome.OPTIMAL)
        self.assert_non_freed_unchanged(broken, result)
        self.assertEqual(self.checker.violations(result.horaire), [])
        # Les employés 2 et 3 sont fixés à l'optimum : le meilleur quart pour l'employé 1 redonne l'optimum.
        self.assertEqual(self.evaluator.evaluate(result.horaire).coverage_cost, BENCH_1_OPTIMUM)

    def test_everyone_freed_reaches_the_optimum(self) -> None:
        identical = Horaire(employees=(self.optimum.employees[0],) * self.instance.employee_count)
        result = cp_sat_solver(self.instance, size=self.instance.employee_count).improve(identical, random.Random(SEED))
        self.assertEqual(result.freed_employees, frozenset({1, 2, 3}))
        self.assertEqual(result.outcome, SolveOutcome.OPTIMAL)
        cost = self.evaluator.evaluate(result.horaire)
        self.assertTrue(cost.is_feasible)
        self.assertEqual(cost.coverage_cost, BENCH_1_OPTIMUM)

    def test_unsatisfiable_subproblem_returns_the_input(self) -> None:
        # Trois quarts identiques, structurellement faisables, mais qui laissent des cellules demandées vides.
        # Avec size = 0, personne n'est libéré : la contrainte « au moins 1 » du modèle est alors violée.
        identical = Horaire(employees=(self.optimum.employees[0],) * self.instance.employee_count)
        result = cp_sat_solver(self.instance, size=0).improve(identical, random.Random(SEED))
        self.assertEqual(result.outcome, SolveOutcome.UNSATISFIABLE)
        self.assertEqual(result.freed_employees, frozenset())
        self.assertIs(result.horaire, identical)

    def test_exhausted_budget_returns_the_input(self) -> None:
        instance = bench("bench_5")
        degenerate = Horaire(employees=(DEGENERATE_SHIFT,) * instance.employee_count)
        result = cp_sat_solver(instance, size=0, units=TINY_UNITS).improve(degenerate, random.Random(SEED))
        self.assertEqual(result.outcome, SolveOutcome.NO_SOLUTION)
        self.assertEqual(result.freed_employees, frozenset(range(1, instance.employee_count + 1)))
        self.assertIs(result.horaire, degenerate)

    def test_same_seed_same_result(self) -> None:
        solver = cp_sat_solver(self.instance, size=1)
        first = solver.improve(self.optimum, random.Random(OTHER_SEED))
        second = solver.improve(self.optimum, random.Random(OTHER_SEED))
        self.assertEqual(first.freed_employees, second.freed_employees)
        self.assertEqual(first.horaire, second.horaire)
        self.assertEqual(first.statistics.failures, second.statistics.failures)
        self.assertEqual(first.statistics.propagations, second.statistics.propagations)


if __name__ == "__main__":
    unittest.main()
