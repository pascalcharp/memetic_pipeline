"""Tests des fonctions de l'analyse « mémétique contre CP-SAT seul » (étape 10g), sur des données construites."""

import json
import tempfile
import unittest
from pathlib import Path

from experiments.analysis.analyze_bench3_cpsat_alone import (
    AnalysisConstants,
    best_at_effort,
    effort_to_reach,
    load_cpsat_runs,
    load_memetic_groups,
    run_ended_mark,
)
from experiments.drivers.run_cpsat_alone import CpSatAloneResultKeys

KEYS = CpSatAloneResultKeys
TRAJECTORY: list[dict] = [
    {KEYS.OBJECTIVE: 900, KEYS.PROPAGATIONS: 10, KEYS.SOLVE_TIME_SECONDS: 1.0, KEYS.FAILURES: 0},
    {KEYS.OBJECTIVE: 500, KEYS.PROPAGATIONS: 50, KEYS.SOLVE_TIME_SECONDS: 4.0, KEYS.FAILURES: 1},
    {KEYS.OBJECTIVE: 40, KEYS.PROPAGATIONS: 200, KEYS.SOLVE_TIME_SECONDS: 9.0, KEYS.FAILURES: 3},
]
SETTINGS: dict = {
    "population_size": 18, "generations": 26, "crossover_count": 3, "mutation_count": 12, "neighborhood_size": 1,
    "deterministic_time_units": 5.0, "stagnation_generations": 10, "initial_local_search": True,
}
STRATEGIES: dict = {"crossover": {"name": "uniform_gene", "parameters": {}},
                    "mutation": {"name": "shift_start", "parameters": {}}}


def memetic_document(seed: int, total: int, instance: str = AnalysisConstants.INSTANCE) -> dict:
    return {
        "instance": instance,
        "settings": SETTINGS | {"master_seed": seed},
        "strategies": STRATEGIES,
        "best": {"cost": {"total": total}},
        "solver_effort": {"propagations": 100 * total, "solve_time_seconds": float(total)},
    }


class TestEffortLookups(unittest.TestCase):
    """Meilleur coût à un effort donné, effort pour atteindre un coût."""

    def test_best_at_effort_between_solutions(self) -> None:
        self.assertEqual(best_at_effort(TRAJECTORY, KEYS.PROPAGATIONS, 60), 500)

    def test_best_at_effort_exactly_on_a_solution(self) -> None:
        self.assertEqual(best_at_effort(TRAJECTORY, KEYS.PROPAGATIONS, 200), 40)

    def test_best_at_effort_before_first_solution(self) -> None:
        self.assertIsNone(best_at_effort(TRAJECTORY, KEYS.SOLVE_TIME_SECONDS, 0.5))

    def test_best_at_effort_empty_trajectory(self) -> None:
        self.assertIsNone(best_at_effort([], KEYS.PROPAGATIONS, 1000))

    def test_effort_to_reach(self) -> None:
        self.assertEqual(effort_to_reach(TRAJECTORY, KEYS.PROPAGATIONS, 500), 50)
        self.assertEqual(effort_to_reach(TRAJECTORY, KEYS.SOLVE_TIME_SECONDS, 41), 9.0)

    def test_effort_to_reach_never(self) -> None:
        self.assertIsNone(effort_to_reach(TRAJECTORY, KEYS.PROPAGATIONS, 16))

    def test_run_ended_mark(self) -> None:
        run = {KEYS.FINAL_STATISTICS: {"propagations": 250, "solveTime": 10.0}}
        self.assertEqual(run_ended_mark(run, KEYS.PROPAGATIONS, 200), "")
        self.assertEqual(run_ended_mark(run, KEYS.PROPAGATIONS, 300), AnalysisConstants.RUN_ENDED_MARK)


class TestLoading(unittest.TestCase):
    """Lecture des fichiers de résultats."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name: str, document: dict) -> Path:
        path = self.root / name
        path.write_text(json.dumps(document), encoding="utf-8")
        return path

    def test_memetic_groups_keep_first_run_of_each_seed(self) -> None:
        paths = [
            self.write("a_s00.json", memetic_document(0, 38)),
            self.write("b_s00.json", memetic_document(0, 99)),
            self.write("a_s01.json", memetic_document(1, 40)),
        ]
        (group,) = load_memetic_groups(paths).values()
        self.assertEqual(sorted(group.costs()), [38, 40])
        self.assertEqual(group.median_cost(), 39)

    def test_other_instances_and_cpsat_files_are_ignored(self) -> None:
        paths = [
            self.write("x.json", memetic_document(0, 38, instance="bench_2")),
            self.write(AnalysisConstants.CPSAT_PREFIX + "reference_s00.json",
                       {"instance": AnalysisConstants.INSTANCE, KEYS.SOLUTIONS: TRAJECTORY}),
        ]
        self.assertEqual(load_memetic_groups(paths), {})
        self.assertEqual(len(load_cpsat_runs(paths)), 1)


if __name__ == "__main__":
    unittest.main()
