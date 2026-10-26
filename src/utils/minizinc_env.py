"""Localisation de l'exécutable MiniZinc et des solveurs disponibles."""

import os
from pathlib import Path

import minizinc

from src.config import MiniZincConfig

class MiniZincEnvironmentMessages:
    """Messages d'erreur MiniZinc."""

    FILE_NOT_FOUND: str       =  "{variable}={path} n'est pas un fichier existant."
    INVALID_EXECUTABLE: str   =  "{variable}={path} n'est pas un exécutable MiniZinc valide."
    MINIZINC_NOT_FOUND: str   =  "MiniZinc est introuvable dans le PATH et les emplacements par défaut. " \
                                 "Installez-le ou définissez la variable d'environnement {variable}."
    SOLVER_NOT_AVAILABLE: str =  "Le solveur {solver_id} n'est pas disponible."


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
        MiniZincNotFoundError: si la variable pointe vers un fichier inexistant, si le fichier n'est pas exécutable ou
        si aucune installation n'est trouvée.
    """
    configured_path = os.environ.get(MiniZincConfig.EXECUTABLE_ENV_VAR)

    if configured_path is not None:
        executable = Path(configured_path)
        if not executable.is_file():
            raise MiniZincNotFoundError(
                MiniZincEnvironmentMessages.FILE_NOT_FOUND.format(variable=MiniZincConfig.EXECUTABLE_ENV_VAR, path=configured_path)
            )
        try:
            return minizinc.Driver(executable)
        except Exception as error:
            raise MiniZincNotFoundError(
                MiniZincEnvironmentMessages.INVALID_EXECUTABLE.format(variable=MiniZincConfig.EXECUTABLE_ENV_VAR, path=configured_path)
            ) from error

    driver = minizinc.Driver.find()
    if driver is None:
        raise MiniZincNotFoundError(
            MiniZincEnvironmentMessages.MINIZINC_NOT_FOUND.format(variable=MiniZincConfig.EXECUTABLE_ENV_VAR)
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
        raise SolverNotAvailableError(
            MiniZincEnvironmentMessages.SOLVER_NOT_AVAILABLE.format(solver_id=solver_id)
        ) from error