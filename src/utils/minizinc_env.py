"""Localisation de l'exécutable MiniZinc et des solveurs disponibles."""

import os
from pathlib import Path

import minizinc

from src.config import MiniZincConfig


class MiniZincEnvironmentError(Exception):
    """Erreur de base pour tout problème d'environnement MiniZinc."""


class MiniZincNotFoundError(MiniZincEnvironmentError):
    """L'exécutable MiniZinc est introuvable ou inutilisable."""


class SolverNotAvailableError(MiniZincEnvironmentError):
    """Le solveur demandé n'est pas installé dans la distribution MiniZinc."""


def locate_minizinc_driver() -> minizinc.Driver:
    """Retourne le pilote MiniZinc à utiliser.

    Ordre de recherche :
      1. le chemin donné par la variable d'environnement ``MiniZincConfig.EXECUTABLE_ENV_VAR`` ;
      2. la recherche par défaut de minizinc-python (PATH et emplacements d'installation usuels).

    Raises:
        MiniZincNotFoundError: si la variable pointe vers un fichier inexistant,
            ou si aucune installation n'est trouvée.
    """
    configured_path = os.environ.get(MiniZincConfig.EXECUTABLE_ENV_VAR)

    if configured_path is not None:
        executable = Path(configured_path)
        if not executable.is_file():
            raise MiniZincNotFoundError(
                f"{MiniZincConfig.EXECUTABLE_ENV_VAR}={configured_path} ne désigne pas un fichier existant."
            )
        return minizinc.Driver(executable)

    driver = minizinc.Driver.find()
    if driver is None:
        raise MiniZincNotFoundError(
            "MiniZinc est introuvable. Installez-le ou définissez "
            f"la variable d'environnement {MiniZincConfig.EXECUTABLE_ENV_VAR}."
        )
    return driver


def lookup_solver(solver_id: str, driver: minizinc.Driver) -> minizinc.Solver:
    """Retourne la configuration du solveur ``solver_id`` connue du pilote ``driver``.

    Raises:
        SolverNotAvailableError: si le solveur n'est pas installé.
    """
    try:
        return minizinc.Solver.lookup(solver_id, driver=driver)
    except LookupError as error:
        raise SolverNotAvailableError(f"Le solveur « {solver_id} » n'est pas disponible.") from error