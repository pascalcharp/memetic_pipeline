"""Tests de la localisation de MiniZinc et de la recherche des solveurs."""

import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

import minizinc

from src.config import MiniZincConfig
from src.utils.minizinc_env import (
    MiniZincEnvironmentError,
    MiniZincNotFoundError,
    SolverNotAvailableError,
    locate_minizinc_driver,
    lookup_solver,
)


class TestExceptionHierarchy(unittest.TestCase):
    """Les exceptions spécifiques dérivent toutes de MiniZincEnvironmentError."""

    def test_not_found_is_environment_error(self) -> None:
        self.assertTrue(issubclass(MiniZincNotFoundError, MiniZincEnvironmentError))

    def test_solver_not_available_is_environment_error(self) -> None:
        self.assertTrue(issubclass(SolverNotAvailableError, MiniZincEnvironmentError))


class TestLocateMiniZincDriver(unittest.TestCase):
    """Ordre de recherche : variable d'environnement d'abord, puis recherche par défaut."""

    # Seul macOS a un emplacement d'installation connu de minizinc-python hors du PATH (/Applications/MiniZincIDE.app).
    MACOS_PLATFORM: str = "darwin"

    def setUp(self) -> None:
        # Environnement sans la variable, pour exercer la recherche par défaut.
        self.environment_without_variable = {
            name: value for name, value in os.environ.items() if name != MiniZincConfig.EXECUTABLE_ENV_VAR
        }

    def test_default_search_finds_installed_minizinc(self) -> None:
        with mock.patch.dict(os.environ, self.environment_without_variable, clear=True):
            driver = locate_minizinc_driver()
        self.assertIsInstance(driver, minizinc.Driver)

    @unittest.skipUnless(sys.platform == MACOS_PLATFORM, "Recherche hors PATH propre à l'installation macOS.")
    def test_default_search_does_not_need_path(self) -> None:
        # Cas PyCharm sous macOS : le PATH ne contient pas MiniZinc.
        environment_without_path = dict(self.environment_without_variable, PATH="")
        with mock.patch.dict(os.environ, environment_without_path, clear=True):
            driver = locate_minizinc_driver()
        self.assertIsInstance(driver, minizinc.Driver)

    def assert_configured_value_is_rejected(self, configured_value: str, *expected_fragments: str) -> None:
        """Vérifie que la valeur de la variable est rejetée et que le message contient chaque fragment attendu."""
        with mock.patch.dict(os.environ, {MiniZincConfig.EXECUTABLE_ENV_VAR: configured_value}):
            with self.assertRaises(MiniZincNotFoundError) as context:
                locate_minizinc_driver()
        message = str(context.exception)
        for fragment in expected_fragments:
            self.assertIn(fragment, message)

    def test_default_search_failure_raises(self) -> None:
        with mock.patch.dict(os.environ, self.environment_without_variable, clear=True):
            with mock.patch.object(minizinc.Driver, "find", return_value=None):
                with self.assertRaises(MiniZincNotFoundError) as context:
                    locate_minizinc_driver()
        # Le message doit indiquer comment corriger : définir la variable d'environnement.
        self.assertIn(MiniZincConfig.EXECUTABLE_ENV_VAR, str(context.exception))

    def test_environment_variable_is_used_when_valid(self) -> None:
        installed_executable = locate_minizinc_driver().executable
        with mock.patch.dict(os.environ, {MiniZincConfig.EXECUTABLE_ENV_VAR: str(installed_executable)}):
            driver = locate_minizinc_driver()
        self.assertEqual(Path(driver.executable), Path(installed_executable))

    def test_environment_variable_takes_precedence_over_default_search(self) -> None:
        installed_executable = locate_minizinc_driver().executable
        with mock.patch.dict(os.environ, {MiniZincConfig.EXECUTABLE_ENV_VAR: str(installed_executable)}):
            with mock.patch.object(minizinc.Driver, "find", return_value=None) as default_search:
                locate_minizinc_driver()
        default_search.assert_not_called()

    def test_environment_variable_pointing_to_missing_file_raises(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing_file = str(Path(directory) / "minizinc_inexistant")
            self.assert_configured_value_is_rejected(missing_file, MiniZincConfig.EXECUTABLE_ENV_VAR, missing_file)

    def test_environment_variable_pointing_to_directory_raises(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            self.assert_configured_value_is_rejected(directory, MiniZincConfig.EXECUTABLE_ENV_VAR, directory)

    def test_environment_variable_pointing_to_non_executable_file_raises(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            non_executable_file = Path(directory) / "minizinc"
            non_executable_file.write_text("pas un exécutable")
            self.assert_configured_value_is_rejected(
                str(non_executable_file), MiniZincConfig.EXECUTABLE_ENV_VAR, str(non_executable_file)
            )

    def test_environment_variable_pointing_to_foreign_executable_raises(self) -> None:
        # Exécutable valide, mais qui n'est pas MiniZinc : sa sortie de --version est inexploitable.
        with tempfile.TemporaryDirectory() as directory:
            foreign_executable = Path(directory) / "minizinc"
            foreign_executable.write_text("#!/bin/sh\necho bonjour\n")
            foreign_executable.chmod(0o755)
            self.assert_configured_value_is_rejected(
                str(foreign_executable), MiniZincConfig.EXECUTABLE_ENV_VAR, str(foreign_executable)
            )

    def test_environment_variable_pointing_to_unloadable_executable_raises(self) -> None:
        # Exécutable sans shebang ni format binaire reconnu : le système refuse de le lancer (Exec format error).
        with tempfile.TemporaryDirectory() as directory:
            unloadable_executable = Path(directory) / "minizinc"
            unloadable_executable.write_bytes(b"\x00\x01 pas un binaire")
            unloadable_executable.chmod(0o755)
            self.assert_configured_value_is_rejected(
                str(unloadable_executable), MiniZincConfig.EXECUTABLE_ENV_VAR, str(unloadable_executable)
            )

    def test_empty_environment_variable_raises(self) -> None:
        # Une variable définie mais vide est une erreur de configuration, pas une absence.
        self.assert_configured_value_is_rejected("", MiniZincConfig.EXECUTABLE_ENV_VAR)


class TestLookupSolver(unittest.TestCase):
    """Recherche d'un solveur dans la distribution MiniZinc."""

    UNKNOWN_SOLVER_ID: str = "solveur-qui-n-existe-pas"

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = locate_minizinc_driver()

    def test_default_solver_is_available(self) -> None:
        solver = lookup_solver(MiniZincConfig.DEFAULT_SOLVER_ID, self.driver)
        self.assertIsInstance(solver, minizinc.Solver)
        self.assertIn(MiniZincConfig.DEFAULT_SOLVER_ID, solver.id)

    def test_unknown_solver_raises(self) -> None:
        with self.assertRaises(SolverNotAvailableError) as context:
            lookup_solver(self.UNKNOWN_SOLVER_ID, self.driver)
        self.assertIsInstance(context.exception.__cause__, LookupError)
        self.assertIn(self.UNKNOWN_SOLVER_ID, str(context.exception))


if __name__ == "__main__":
    unittest.main()
