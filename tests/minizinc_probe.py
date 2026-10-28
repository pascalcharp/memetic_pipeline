"""Sonde MiniZinc partagée par les tests : interroge horaire.mzn pour vérifier la cohérence du code Python avec le modèle."""

import asyncio
import warnings
from datetime import timedelta
from pathlib import Path

import minizinc
from minizinc.error import MiniZincWarning

from src.config import MiniZincConfig, ProjectPaths
from src.utils.minizinc_env import locate_minizinc_driver, lookup_solver


class MiniZincModelProbe:
    """Interroge horaire.mzn sur une instance : valeurs de paramètres dérivés et faisabilité de contraintes ajoutées."""

    TIME_LIMIT: timedelta = timedelta(seconds=60)

    def __init__(self, instance_path: Path) -> None:
        driver = locate_minizinc_driver()
        solver = lookup_solver(MiniZincConfig.DEFAULT_SOLVER_ID, driver)
        model = minizinc.Model(ProjectPaths.MODEL_FILE)
        model.add_file(instance_path)
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
