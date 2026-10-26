"""Test de fumée : la chaîne Python → MiniZinc → CP-SAT résout le modèle sur une petite instance."""

import json
import unittest
from datetime import timedelta

import minizinc

from src.config import MiniZincConfig, ProjectPaths
from src.utils.minizinc_env import locate_minizinc_driver, lookup_solver


class TestSmokeMiniZinc(unittest.TestCase):
    """Résolution complète de ``horaire.mzn`` sur ``bench_1.json`` avec le solveur par défaut."""

    INSTANCE_FILE_NAME: str = "bench_1.json"
    TIME_LIMIT: timedelta = timedelta(seconds=30)

    # Optimum prouvé par CP-SAT le 2026-10-26. Servira de référence pour la validation croisée de l'étape 4.
    KNOWN_OPTIMAL_COST: int = 94

    # Variables de décision indexées par employé, telles que nommées dans horaire.mzn.
    EMPLOYEE_VARIABLES: tuple[str, ...] = ("debut", "pause1", "diner", "pause2", "fin", "activites")

    @classmethod
    def setUpClass(cls) -> None:
        instance_path = ProjectPaths.DATA_DIR / cls.INSTANCE_FILE_NAME
        with instance_path.open() as instance_file:
            cls.instance_data = json.load(instance_file)

        driver = locate_minizinc_driver()
        solver = lookup_solver(MiniZincConfig.DEFAULT_SOLVER_ID, driver)
        model = minizinc.Model(ProjectPaths.MODEL_FILE)
        model.add_file(instance_path)
        cls.result = minizinc.Instance(solver, model).solve(time_limit=cls.TIME_LIMIT)

    def test_model_file_exists(self) -> None:
        self.assertTrue(ProjectPaths.MODEL_FILE.is_file())

    def test_solver_proves_optimality(self) -> None:
        self.assertEqual(self.result.status, minizinc.Status.OPTIMAL_SOLUTION)

    def test_optimal_cost_matches_known_value(self) -> None:
        self.assertEqual(self.result.objective, self.KNOWN_OPTIMAL_COST)

    def test_every_employee_receives_a_schedule(self) -> None:
        employee_count = self.instance_data["NB_EMPLOYES"]
        for variable_name in self.EMPLOYEE_VARIABLES:
            with self.subTest(variable=variable_name):
                self.assertEqual(len(self.result[variable_name]), employee_count)


if __name__ == "__main__":
    unittest.main()
