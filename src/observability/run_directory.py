"""Répertoire d'une exécution (décision D8) : ``results/<expérience>/<run_id>/``.

Une exécution écrit tout au même endroit :
    - ``config.json`` : graine, commit Git, versions de Python et des paquets, paramètres de l'expérience ;
    - ``events.jsonl`` : les enregistrements (``JsonlSink``) ;
    - ``generations.csv`` : un tableau par génération (``CsvSink``) ;
    - ``run.log`` : le journal de diagnostic (``configure_logging``).
``results/`` est ignoré par Git. L'identifiant d'exécution par défaut et la date de création ne sont pas
déterministes (D8) ; tout le reste de ``config.json`` l'est.
"""

import json
import platform
import subprocess
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime, timezone
from importlib import metadata
from pathlib import Path
from typing import Any

from src.config import ProjectPaths
from src.observability.sinks import ObservabilityError, SinkDefaults


class RunDirectoryDefaults:
    """Noms et emplacements des fichiers d'une exécution."""

    RESULTS_DIR: Path = ProjectPaths.ROOT / "results"
    CONFIG_FILE: str = "config.json"
    EVENTS_FILE: str = "events.jsonl"
    GENERATIONS_FILE: str = "generations.csv"
    RUN_LOG_FILE: str = "run.log"
    # Identifiant par défaut : date et heure UTC de création, à la seconde.
    RUN_ID_FORMAT: str = "%Y%m%dT%H%M%SZ"
    JSON_INDENT: int = 2
    # Paquets dont la version est consignée dans config.json.
    TRACKED_PACKAGES: tuple[str, ...] = ("minizinc", "numpy")
    UNKNOWN_VALUE: str = "inconnu"
    GIT_COMMIT_COMMAND: tuple[str, ...] = ("git", "rev-parse", "HEAD")
    # Fichiers modifiés, ajoutés ou non suivis de tout le dépôt ; les chemins exclus sont ajoutés après « -- ».
    GIT_STATUS_COMMAND: tuple[str, ...] = ("git", "status", "--porcelain", "--untracked-files=all", "--", ".")
    GIT_EXCLUDE_TEMPLATE: str = ":(exclude){path}"


class ConfigFields:
    """Champs de ``config.json``."""

    EXPERIMENT: str = "experiment"
    RUN_ID: str = "run_id"
    CREATED_AT: str = "created_at"
    SEED: str = "seed"
    GIT_COMMIT: str = "git_commit"
    PYTHON_VERSION: str = "python_version"
    PACKAGES: str = "packages"
    PARAMETERS: str = "parameters"


class RunDirectoryMessages:
    """Gabarits des messages d'erreur du répertoire d'exécution."""

    ALREADY_EXISTS: str = "Le répertoire d'exécution {path} existe déjà : choisir un autre identifiant."


class RunDirectoryExistsError(ObservabilityError):
    """Le répertoire de l'exécution existe déjà : on n'écrase jamais les résultats d'une autre exécution."""


def current_git_commit(repository: Path = ProjectPaths.ROOT) -> str:
    """Commit Git courant de ``repository``, ou ``RunDirectoryDefaults.UNKNOWN_VALUE`` hors d'un dépôt Git."""
    try:
        completed = subprocess.run(
            RunDirectoryDefaults.GIT_COMMIT_COMMAND, cwd=repository, capture_output=True, text=True, check=True
        )
    except (OSError, subprocess.CalledProcessError):
        return RunDirectoryDefaults.UNKNOWN_VALUE
    return completed.stdout.strip()


def working_tree_is_dirty(repository: Path = ProjectPaths.ROOT, excluded: Sequence[Path] = ()) -> bool | None:
    """Vrai si la copie de travail de ``repository`` a des modifications non commitées (fichiers modifiés, ajoutés ou
    non suivis), en ignorant les chemins ``excluded`` (relatifs à la racine du dépôt) ; ``None`` hors d'un dépôt Git.

    Un résultat produit avec une copie de travail modifiée ne peut pas être reproduit à partir du seul commit noté.
    """
    exclusions = tuple(RunDirectoryDefaults.GIT_EXCLUDE_TEMPLATE.format(path=path.as_posix()) for path in excluded)
    try:
        completed = subprocess.run(
            RunDirectoryDefaults.GIT_STATUS_COMMAND + exclusions,
            cwd=repository, capture_output=True, text=True, check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return completed.stdout.strip() != ""


def package_versions(packages: Sequence[str] = RunDirectoryDefaults.TRACKED_PACKAGES) -> dict[str, str]:
    """Version installée de chaque paquet, ou ``RunDirectoryDefaults.UNKNOWN_VALUE`` s'il est absent."""
    versions: dict[str, str] = {}
    for package in packages:
        try:
            versions[package] = metadata.version(package)
        except metadata.PackageNotFoundError:
            versions[package] = RunDirectoryDefaults.UNKNOWN_VALUE
    return versions


@dataclass(frozen=True)
class RunDirectory:
    """Répertoire ``<results_root>/<experiment>/<run_id>/`` d'une exécution, et les chemins de ses fichiers."""

    path: Path
    experiment: str
    run_id: str

    @classmethod
    def create(
            cls,
            experiment: str,
            run_id: str | None = None,
            results_root: Path = RunDirectoryDefaults.RESULTS_DIR,
    ) -> "RunDirectory":
        """Crée le répertoire de l'exécution (et ses parents).

        Args:
            experiment: nom de l'expérience (premier niveau sous ``results_root``).
            run_id: identifiant de l'exécution ; par défaut, la date et l'heure UTC (non déterministe).
            results_root: racine des résultats ; ``results/`` à la racine du dépôt par défaut.

        Raises:
            RunDirectoryExistsError: si le répertoire existe déjà.
        """
        if run_id is None:
            run_id = datetime.now(timezone.utc).strftime(RunDirectoryDefaults.RUN_ID_FORMAT)
        path = results_root / experiment / run_id
        if path.exists():
            raise RunDirectoryExistsError(RunDirectoryMessages.ALREADY_EXISTS.format(path=path))
        path.mkdir(parents=True)
        return cls(path=path, experiment=experiment, run_id=run_id)

    @property
    def config_path(self) -> Path:
        return self.path / RunDirectoryDefaults.CONFIG_FILE

    @property
    def events_path(self) -> Path:
        return self.path / RunDirectoryDefaults.EVENTS_FILE

    @property
    def generations_path(self) -> Path:
        return self.path / RunDirectoryDefaults.GENERATIONS_FILE

    @property
    def run_log_path(self) -> Path:
        return self.path / RunDirectoryDefaults.RUN_LOG_FILE

    def write_config(self, seed: int, parameters: Mapping[str, Any]) -> Path:
        """Écrit ``config.json`` : expérience, identifiant, date de création, graine, commit Git, versions et
        ``parameters`` (valeurs sérialisables en JSON). Rend le chemin du fichier."""
        config = {
            ConfigFields.EXPERIMENT: self.experiment,
            ConfigFields.RUN_ID: self.run_id,
            ConfigFields.CREATED_AT: datetime.now(timezone.utc).isoformat(),
            ConfigFields.SEED: seed,
            ConfigFields.GIT_COMMIT: current_git_commit(),
            ConfigFields.PYTHON_VERSION: platform.python_version(),
            ConfigFields.PACKAGES: package_versions(),
            ConfigFields.PARAMETERS: dict(parameters),
        }
        with self.config_path.open("w", encoding=SinkDefaults.ENCODING) as file:
            json.dump(
                config, file, ensure_ascii=SinkDefaults.JSON_ENSURE_ASCII, indent=RunDirectoryDefaults.JSON_INDENT
            )
        return self.config_path
