"""Exécution d'une expérience décrite par un fichier de configuration JSON (étape 10a).

Usage, depuis la racine du dépôt :

    python -m experiments.drivers.run_experiment experiments/config/integration_bench1.json
    python -m experiments.drivers.run_experiment CONFIG [--results-dir RÉPERTOIRE] [--log JOURNAL]

Trois chemins :
    - ``CONFIG`` : le fichier de configuration (par convention dans ``experiments/config/``) ;
    - ``--results-dir`` : le répertoire où écrire le fichier de résultats ; par défaut, le répertoire du jour
      ``experiments/results/<AAAA-MM-JJ>/``, créé au besoin ;
    - ``--log`` : le journal des expériences ; par défaut ``experiments/EXPLOG.md``.

Le script lit la configuration, construit le moteur avec l'assemblage de référence (``build_block_memetic_config``),
l'exécute avec les quatre collecteurs de 8b, écrit un fichier JSON de résultats et ajoute une entrée au journal :
description, chemins, coût obtenu et effort cumulé du solveur.

Format de la configuration (``ConfigKeys``) :

    {
      "description": "Texte lisible : ce que l'expérience cherche à montrer.",
      "instance": "bench_1",
      "settings": {"population_size": 6, "crossover_count": 2, "master_seed": 7}
    }

``instance`` est le nom d'un fichier de ``data/`` sans son extension. ``settings`` est facultatif : ses clés sont des
champs de ``AssemblySettings`` (``src/memetic/assembly.py``), et les champs absents prennent leur valeur par défaut.

``strategies`` (facultatif, étape 10c) choisit des stratégies par leur nom, rôle par rôle (``StrategyRoles``), sous
une forme courte (le nom seul) ou objet (le nom et les paramètres de sa fabrique) ; les rôles absents gardent la
stratégie de l'assemblage de référence. Noms disponibles : ``StrategyNames`` (``src/memetic/catalog.py``).

    "strategies": {"crossover": "uniform_gene", "mutation": {"name": "activity", "parameters": {}}}
"""

import argparse
import dataclasses
import json
import platform
import sys
import time
import warnings
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from minizinc.error import MiniZincWarning

from src.config import ProjectPaths
from src.ga.registry import RegistryError
from src.memetic.assembly import AssemblySettings, build_block_memetic_config
from src.memetic.catalog import StrategyCatalog, StrategyChoice, StrategyChoices, StrategyError, StrategyKeys
from src.memetic.engine import Memetic, MemeticResult
from src.model.evaluation import CostBreakdown
from src.observability.collectors import (
    CostStatisticsCollector,
    DiversityCollector,
    FeasibilityRateCollector,
    RecordFields,
    RecordNames,
    Scopes,
    SolverEffortCollector,
    SolverEffortFields,
)
from src.observability.events import RecordSchema
from src.observability.hub import ObservationHub
from src.observability.run_directory import current_git_commit, package_versions, working_tree_is_dirty
from src.observability.sinks import MemorySink
from src.utils.io import ProblemInstance, load_instance


class ExperimentDefaults:
    """Emplacements par défaut et formats des fichiers d'une expérience."""

    RESULTS_ROOT: Path = ProjectPaths.EXPERIMENT_RESULTS_DIR
    EXPLOG_FILE: Path = ProjectPaths.EXPLOG_FILE
    INSTANCE_DIR: Path = ProjectPaths.DATA_DIR
    INSTANCE_EXTENSION: str = ".json"
    RESULTS_EXTENSION: str = ".json"
    # Répertoire du jour et horodatage du fichier de résultats (heure locale : la date est celle de l'expérimentateur).
    DATE_FORMAT: str = "%Y-%m-%d"
    TIME_FORMAT: str = "%H%M%S"
    LOG_TIMESTAMP_FORMAT: str = "%Y-%m-%d %H:%M"
    RESULTS_FILE_TEMPLATE: str = "{experiment}_{time}{extension}"
    RESULTS_SCHEMA_VERSION: int = 1
    # Ignorés pour décider si la copie de travail est modifiée : les sorties des expériences elles-mêmes, qu'on
    # accumule souvent avant de les commiter. Les configurations, elles, comptent.
    GIT_DIRTY_EXCLUDED: tuple[Path, ...] = (
        ProjectPaths.EXPERIMENT_RESULTS_DIR.relative_to(ProjectPaths.ROOT),
        ProjectPaths.EXPLOG_FILE.relative_to(ProjectPaths.ROOT),
    )
    JSON_INDENT: int = 2
    ENCODING: str = "utf-8"
    DURATION_DECIMALS: int = 1
    DETERMINISTIC_TIME_DECIMALS: int = 3


class ConfigKeys:
    """Clés du fichier de configuration."""

    DESCRIPTION: str = "description"
    INSTANCE: str = "instance"
    SETTINGS: str = "settings"
    STRATEGIES: str = "strategies"
    REQUIRED: tuple[str, ...] = (DESCRIPTION, INSTANCE)
    ALLOWED: tuple[str, ...] = (DESCRIPTION, INSTANCE, SETTINGS, STRATEGIES)
    # Chemin d'une clé imbriquée dans les messages d'erreur, par exemple « strategies.mutation.name ».
    PATH_TEMPLATE: str = "{parent}.{key}"


class ResultKeys:
    """Clés du fichier de résultats."""

    SCHEMA_VERSION: str = "schema_version"
    EXPERIMENT: str = "experiment"
    DESCRIPTION: str = "description"
    CONFIG_PATH: str = "config_path"
    INSTANCE: str = "instance"
    SETTINGS: str = "settings"
    STRATEGIES: str = "strategies"
    STARTED_AT: str = "started_at"
    DURATION_SECONDS: str = "duration_seconds"
    GIT_COMMIT: str = "git_commit"
    GIT_DIRTY: str = "git_dirty"
    PYTHON_VERSION: str = "python_version"
    PACKAGES: str = "packages"
    BEST: str = "best"
    BEST_COST: str = "cost"
    BEST_SCHEDULE: str = "schedule"
    TOTAL: str = "total"
    IS_FEASIBLE: str = "is_feasible"
    GENERATIONS: str = "generations"
    RESTARTS: str = "restarts"
    SOLVER_EFFORT: str = "solver_effort"
    SOLVER_EFFORT_BY_GENERATION: str = "solver_effort_by_generation"
    FEASIBILITY_RATES: str = "feasibility_rates"
    COST_STATISTICS: str = "cost_statistics"
    DIVERSITY: str = "diversity"


class ExplogTexts:
    """Gabarits du journal des expériences (``EXPLOG.md``)."""

    HEADER: str = (
        "# Journal des expériences\n\n"
        "Une entrée par exécution de `python -m experiments.drivers.run_experiment`, ajoutée automatiquement. "
        "Les fichiers de résultats complets sont dans `experiments/results/<date>/`.\n"
    )
    ENTRY: str = (
        "\n## {timestamp} — {experiment}\n\n"
        "{description}\n\n"
        "- Configuration : `{config_path}`\n"
        "- Résultats : `{results_path}`\n"
        "- Instance : {instance} ; graine {seed} ; population {population_size}, NR = {crossover_count}, "
        "NM = {mutation_count}, {generations_setting} générations\n"
        "- Stratégies : {strategies}\n"
        "- **Coût obtenu : {best_total}** ({feasibility}) ; {generations} générations, {restarts} restart(s)\n"
        "- **Effort cumulé du solveur** : {calls} appels ; failures {failures} ; propagations {propagations} ; "
        "nodes {nodes} ; temps déterministe {deterministic_time} ; temps de résolution {solve_time} s (non déterministe)\n"
        "- Durée de l'exécution : {duration} s ; commit `{git_commit}`{git_state}\n"
    )
    GIT_CLEAN: str = ""
    GIT_DIRTY: str = (
        " — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**"
    )
    GIT_UNKNOWN: str = " (état de la copie de travail inconnu)"
    FEASIBLE: str = "faisable"
    INFEASIBLE: str = "infaisable"
    NOT_REPORTED: str = "non rapporté"
    STRATEGY_ITEM: str = "{role} `{name}`{parameters}"
    STRATEGY_PARAMETERS: str = " {parameters}"
    STRATEGY_SEPARATOR: str = " ; "


class ExperimentMessages:
    """Gabarits des messages d'erreur des expériences."""

    UNREADABLE_CONFIG: str = "Configuration {path} illisible : {detail}"
    NOT_AN_OBJECT: str = "Configuration {path} : un objet JSON est attendu à la racine."
    MISSING_KEY: str = "Configuration {path} : la clé « {key} » est obligatoire."
    UNKNOWN_KEY: str = "Configuration {path} : clé « {key} » inconnue ; clés permises : {allowed}."
    UNKNOWN_SETTING: str = "Configuration {path} : paramètre « {key} » inconnu ; paramètres permis : {allowed}."
    WRONG_TYPE: str = "Configuration {path} : « {key} » doit être de type {expected} ; trouvé {value!r}."
    UNKNOWN_STRATEGY_KEY: str = "Configuration {path} : clé « {key} » inconnue dans « {parent} » ; clés permises : {allowed}."
    INVALID_STRATEGY: str = "Configuration {path} : stratégie « {key} » invalide : {detail}"
    INSTANCE_NOT_FOUND: str = "Configuration {path} : instance « {instance} » introuvable ({instance_path})."
    RESULTS_FILE_EXISTS: str = "Le fichier de résultats {path} existe déjà."
    SUMMARY: str = "Coût obtenu : {best_total} ; effort cumulé du solveur : {calls} appels. Résultats : {results_path}"


class ExperimentError(Exception):
    """Erreur de base des expériences."""


class InvalidExperimentConfigError(ExperimentError):
    """Le fichier de configuration est illisible ou ne respecte pas le format attendu."""


class ResultsFileExistsError(ExperimentError):
    """Le fichier de résultats existe déjà : on n'écrase jamais un résultat."""


@dataclass(frozen=True)
class ExperimentConfig:
    """Une expérience lue dans un fichier de configuration : son nom (celui du fichier), sa description, son
    instance, les paramètres complets de l'assemblage et les stratégies choisies (celles de l'assemblage de référence
    par défaut)."""

    name: str
    path: Path
    description: str
    instance_name: str
    settings: AssemblySettings
    strategies: StrategyChoices = field(default_factory=StrategyChoices)

    def instance_path(self) -> Path:
        return ExperimentDefaults.INSTANCE_DIR / (self.instance_name + ExperimentDefaults.INSTANCE_EXTENSION)


@dataclass(frozen=True)
class ExperimentOutcome:
    """Ce que rend ``run_experiment`` : le résultat du moteur, les enregistrements des collecteurs, le moment et la
    durée de l'exécution, et l'état Git du code au moment du lancement (commit, copie de travail modifiée ou non,
    ``None`` si inconnu)."""

    result: MemeticResult
    records: tuple[dict[str, Any], ...]
    started_at: datetime
    duration_seconds: float
    git_commit: str
    git_dirty: bool | None


# ---------------------------------------------------------------------------------------------------------------------
# Lecture de la configuration
# ---------------------------------------------------------------------------------------------------------------------

def load_experiment_config(path: Path) -> ExperimentConfig:
    """Lit et valide le fichier de configuration ``path``.

    Raises:
        InvalidExperimentConfigError: fichier illisible ou JSON invalide, racine qui n'est pas un objet, clé
            obligatoire absente, clé ou paramètre inconnu, valeur du mauvais type, stratégie inconnue ou mal
            paramétrée, instance introuvable ; le chemin du fichier et la clé en cause sont dans le message.
    """
    try:
        content = json.loads(path.read_text(encoding=ExperimentDefaults.ENCODING))
    except (OSError, json.JSONDecodeError) as error:
        raise InvalidExperimentConfigError(ExperimentMessages.UNREADABLE_CONFIG.format(path=path, detail=error)) from error
    if not isinstance(content, dict):
        raise InvalidExperimentConfigError(ExperimentMessages.NOT_AN_OBJECT.format(path=path))

    for key in content:
        if key not in ConfigKeys.ALLOWED:
            raise InvalidExperimentConfigError(ExperimentMessages.UNKNOWN_KEY.format(
                path=path, key=key, allowed=", ".join(ConfigKeys.ALLOWED)
            ))
    for key in ConfigKeys.REQUIRED:
        if key not in content:
            raise InvalidExperimentConfigError(ExperimentMessages.MISSING_KEY.format(path=path, key=key))
    for key in ConfigKeys.REQUIRED:
        check_type(path, key, content[key], str)

    raw_settings = content.get(ConfigKeys.SETTINGS, {})
    check_type(path, ConfigKeys.SETTINGS, raw_settings, dict)
    config = ExperimentConfig(
        name=path.stem,
        path=path,
        description=content[ConfigKeys.DESCRIPTION],
        instance_name=content[ConfigKeys.INSTANCE],
        settings=settings_from(path, raw_settings),
        strategies=strategies_from(path, content.get(ConfigKeys.STRATEGIES, {})),
    )
    if not config.instance_path().is_file():
        raise InvalidExperimentConfigError(ExperimentMessages.INSTANCE_NOT_FOUND.format(
            path=path, instance=config.instance_name, instance_path=config.instance_path()
        ))
    return config


def settings_from(path: Path, raw_settings: Mapping[str, Any]) -> AssemblySettings:
    """``AssemblySettings`` dont les champs donnés dans ``raw_settings`` remplacent les valeurs par défaut.

    Les types sont vérifiés ici ; les domaines (par exemple une taille au moins 1) le sont par ``MemeticConfig`` et
    par les composants, à la construction du moteur.
    """
    fields_by_name = {field.name: field for field in dataclasses.fields(AssemblySettings)}
    for key, value in raw_settings.items():
        if key not in fields_by_name:
            raise InvalidExperimentConfigError(ExperimentMessages.UNKNOWN_SETTING.format(
                path=path, key=key, allowed=", ".join(fields_by_name)
            ))
        check_type(path, key, value, fields_by_name[key].type)
    return AssemblySettings(**raw_settings)


def strategies_from(path: Path, raw_strategies: Any) -> StrategyChoices:
    """Les stratégies choisies dans ``raw_strategies`` ; les rôles absents gardent leur valeur par défaut.

    Chaque choix est vérifié par le catalogue (rôle, nom, paramètres) sans créer la stratégie : une configuration
    invalide est refusée avant toute exécution.
    """
    check_type(path, ConfigKeys.STRATEGIES, raw_strategies, dict)
    catalog = StrategyCatalog()
    choices: dict[str, StrategyChoice] = {}
    for role, raw_choice in raw_strategies.items():
        key = ConfigKeys.PATH_TEMPLATE.format(parent=ConfigKeys.STRATEGIES, key=role)
        choice = strategy_choice_from(path, key, raw_choice)
        try:
            catalog.check(role, choice)
        except (StrategyError, RegistryError) as error:
            raise InvalidExperimentConfigError(ExperimentMessages.INVALID_STRATEGY.format(
                path=path, key=key, detail=error
            )) from error
        choices[role] = choice
    return StrategyChoices(**choices)


def strategy_choice_from(path: Path, key: str, raw_choice: Any) -> StrategyChoice:
    """Un choix sous sa forme courte (le nom) ou objet (``{"name": ..., "parameters": {...}}``)."""
    if isinstance(raw_choice, str):
        return StrategyChoice(raw_choice)
    check_type(path, key, raw_choice, dict)
    for choice_key in raw_choice:
        if choice_key not in StrategyKeys.ALLOWED:
            raise InvalidExperimentConfigError(ExperimentMessages.UNKNOWN_STRATEGY_KEY.format(
                path=path, key=choice_key, parent=key, allowed=", ".join(StrategyKeys.ALLOWED)
            ))
    name_key = ConfigKeys.PATH_TEMPLATE.format(parent=key, key=StrategyKeys.NAME)
    if StrategyKeys.NAME not in raw_choice:
        raise InvalidExperimentConfigError(ExperimentMessages.MISSING_KEY.format(path=path, key=name_key))
    check_type(path, name_key, raw_choice[StrategyKeys.NAME], str)
    parameters = raw_choice.get(StrategyKeys.PARAMETERS, {})
    check_type(path, ConfigKeys.PATH_TEMPLATE.format(parent=key, key=StrategyKeys.PARAMETERS), parameters, dict)
    return StrategyChoice(raw_choice[StrategyKeys.NAME], parameters)


def check_type(path: Path, key: str, value: Any, expected: type) -> None:
    """Vérifie que ``value`` est du type ``expected``. Un booléen n'est pas accepté comme nombre, et un entier est
    accepté comme réel.

    Raises:
        InvalidExperimentConfigError: sinon.
    """
    if expected is bool:
        valid = isinstance(value, bool)
    elif expected is int:
        valid = isinstance(value, int) and not isinstance(value, bool)
    elif expected is float:
        valid = isinstance(value, (int, float)) and not isinstance(value, bool)
    else:
        valid = isinstance(value, expected)
    if not valid:
        raise InvalidExperimentConfigError(ExperimentMessages.WRONG_TYPE.format(
            path=path, key=key, expected=expected.__name__, value=value
        ))


# ---------------------------------------------------------------------------------------------------------------------
# Exécution
# ---------------------------------------------------------------------------------------------------------------------

def local_now() -> datetime:
    """Date et heure locales, avec leur fuseau."""
    return datetime.now().astimezone()


def run_experiment(config: ExperimentConfig, clock: Callable[[], datetime] = local_now) -> ExperimentOutcome:
    """Construit le moteur avec l'assemblage de référence, les stratégies choisies et les quatre collecteurs de 8b,
    puis l'exécute."""
    instance: ProblemInstance = load_instance(config.instance_path())
    memory = MemorySink()
    hub = ObservationHub(
        collectors=(
            CostStatisticsCollector(),
            DiversityCollector(instance.period_count),
            FeasibilityRateCollector(),
            SolverEffortCollector(),
        ),
        sinks=(memory,),
    )
    engine = Memetic(build_block_memetic_config(instance, config.settings, hub, strategies=config.strategies))
    # L'état Git est lu avant l'exécution : c'est le code qui a produit le résultat.
    git_commit = current_git_commit()
    git_dirty = working_tree_is_dirty(excluded=ExperimentDefaults.GIT_DIRTY_EXCLUDED)
    started_at = clock()
    start = time.perf_counter()
    # Le modèle de référence avertit sur un sous-problème insatisfiable ; c'est une issue normale (D11).
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", MiniZincWarning)
        result = engine.run()
    duration_seconds = time.perf_counter() - start
    return ExperimentOutcome(
        result=result,
        records=tuple(memory.records),
        started_at=started_at,
        duration_seconds=duration_seconds,
        git_commit=git_commit,
        git_dirty=git_dirty,
    )


# ---------------------------------------------------------------------------------------------------------------------
# Résultats
# ---------------------------------------------------------------------------------------------------------------------

def default_results_dir(day: datetime) -> Path:
    """Le répertoire des résultats du jour : ``experiments/results/<AAAA-MM-JJ>/``."""
    return ExperimentDefaults.RESULTS_ROOT / day.strftime(ExperimentDefaults.DATE_FORMAT)


def records_of(outcome: ExperimentOutcome, record_name: str) -> list[dict[str, Any]]:
    return [record for record in outcome.records if record[RecordSchema.EVENT_FIELD] == record_name]


def cumulative_record(outcome: ExperimentOutcome, record_name: str) -> list[dict[str, Any]]:
    """Les enregistrements de portée cumulée (émis à la fin de l'exécution) de type ``record_name``."""
    return [record for record in records_of(outcome, record_name) if record[RecordFields.SCOPE] == Scopes.CUMULATIVE]


def generation_records(outcome: ExperimentOutcome, record_name: str) -> list[dict[str, Any]]:
    """Les enregistrements de portée génération (un par génération, la génération 0 comprise) de type
    ``record_name``."""
    return [record for record in records_of(outcome, record_name) if record[RecordFields.SCOPE] == Scopes.GENERATION]


def cost_to_json(cost: CostBreakdown) -> dict[str, Any]:
    """Le coût décomposé, avec ``total`` et ``is_feasible`` (propriétés calculées)."""
    return dataclasses.asdict(cost) | {ResultKeys.TOTAL: cost.total, ResultKeys.IS_FEASIBLE: cost.is_feasible}


def results_document(config: ExperimentConfig, outcome: ExperimentOutcome) -> dict[str, Any]:
    """Le contenu du fichier de résultats : configuration complète, provenance, meilleur individu, effort cumulé du
    solveur, taux de faisabilité cumulés, et pour chaque génération les statistiques de coût, la diversité et
    l'effort du solveur (étape 10d)."""
    best = outcome.result.best
    (solver_effort,) = cumulative_record(outcome, RecordNames.SOLVER_EFFORT)
    return {
        ResultKeys.SCHEMA_VERSION: ExperimentDefaults.RESULTS_SCHEMA_VERSION,
        ResultKeys.EXPERIMENT: config.name,
        ResultKeys.DESCRIPTION: config.description,
        ResultKeys.CONFIG_PATH: display_path(config.path),
        ResultKeys.INSTANCE: config.instance_name,
        ResultKeys.SETTINGS: dataclasses.asdict(config.settings),
        ResultKeys.STRATEGIES: config.strategies.to_json(),
        ResultKeys.STARTED_AT: outcome.started_at.isoformat(),
        ResultKeys.DURATION_SECONDS: outcome.duration_seconds,
        ResultKeys.GIT_COMMIT: outcome.git_commit,
        ResultKeys.GIT_DIRTY: outcome.git_dirty,
        ResultKeys.PYTHON_VERSION: platform.python_version(),
        ResultKeys.PACKAGES: package_versions(),
        ResultKeys.BEST: {
            ResultKeys.BEST_COST: cost_to_json(best.cost),
            ResultKeys.BEST_SCHEDULE: [dataclasses.asdict(shift) for shift in best.horaire.employees],
        },
        ResultKeys.GENERATIONS: outcome.result.generations,
        ResultKeys.RESTARTS: outcome.result.restarts,
        ResultKeys.SOLVER_EFFORT: solver_effort,
        ResultKeys.SOLVER_EFFORT_BY_GENERATION: generation_records(outcome, RecordNames.SOLVER_EFFORT),
        ResultKeys.FEASIBILITY_RATES: cumulative_record(outcome, RecordNames.FEASIBILITY_RATES),
        ResultKeys.COST_STATISTICS: records_of(outcome, RecordNames.COST_STATISTICS),
        ResultKeys.DIVERSITY: records_of(outcome, RecordNames.DIVERSITY),
    }


def write_results(document: Mapping[str, Any], results_dir: Path, experiment: str, started_at: datetime) -> Path:
    """Écrit ``document`` dans ``<results_dir>/<expérience>_<HHMMSS>.json`` (répertoire créé au besoin).

    Raises:
        ResultsFileExistsError: si ce fichier existe déjà.
    """
    results_dir.mkdir(parents=True, exist_ok=True)
    path = results_dir / ExperimentDefaults.RESULTS_FILE_TEMPLATE.format(
        experiment=experiment,
        time=started_at.strftime(ExperimentDefaults.TIME_FORMAT),
        extension=ExperimentDefaults.RESULTS_EXTENSION,
    )
    if path.exists():
        raise ResultsFileExistsError(ExperimentMessages.RESULTS_FILE_EXISTS.format(path=path))
    path.write_text(
        json.dumps(document, indent=ExperimentDefaults.JSON_INDENT, ensure_ascii=False) + "\n",
        encoding=ExperimentDefaults.ENCODING,
    )
    return path


def display_path(path: Path) -> str:
    """``path`` relatif à la racine du dépôt s'il s'y trouve, absolu sinon."""
    absolute = path.resolve()
    if absolute.is_relative_to(ProjectPaths.ROOT):
        return absolute.relative_to(ProjectPaths.ROOT).as_posix()
    return absolute.as_posix()


# ---------------------------------------------------------------------------------------------------------------------
# Journal des expériences
# ---------------------------------------------------------------------------------------------------------------------

def reported(value: Any) -> str:
    """Une statistique du solveur, ou « non rapporté » si le solveur ne la donne pas."""
    return ExplogTexts.NOT_REPORTED if value is None else str(value)


def explog_entry(
        config: ExperimentConfig, document: Mapping[str, Any], results_path: Path, started_at: datetime
) -> str:
    """L'entrée d'EXPLOG.md d'une exécution, à partir de sa configuration et de son document de résultats."""
    settings = config.settings
    best_cost = document[ResultKeys.BEST][ResultKeys.BEST_COST]
    effort = document[ResultKeys.SOLVER_EFFORT]
    solve_time = effort[SolverEffortFields.SOLVE_TIME_SECONDS]
    return ExplogTexts.ENTRY.format(
        timestamp=started_at.strftime(ExperimentDefaults.LOG_TIMESTAMP_FORMAT),
        experiment=document[ResultKeys.EXPERIMENT],
        description=document[ResultKeys.DESCRIPTION],
        config_path=document[ResultKeys.CONFIG_PATH],
        results_path=display_path(results_path),
        instance=document[ResultKeys.INSTANCE],
        seed=settings.master_seed,
        population_size=settings.population_size,
        crossover_count=settings.crossover_count,
        mutation_count=settings.mutation_count,
        generations_setting=settings.generations,
        strategies=strategies_text(config.strategies),
        best_total=best_cost[ResultKeys.TOTAL],
        feasibility=ExplogTexts.FEASIBLE if best_cost[ResultKeys.IS_FEASIBLE] else ExplogTexts.INFEASIBLE,
        generations=document[ResultKeys.GENERATIONS],
        restarts=document[ResultKeys.RESTARTS],
        calls=effort[SolverEffortFields.CALLS],
        failures=reported(effort[SolverEffortFields.FAILURES]),
        propagations=reported(effort[SolverEffortFields.PROPAGATIONS]),
        nodes=reported(effort[SolverEffortFields.NODES]),
        deterministic_time=reported(rounded(effort[SolverEffortFields.DETERMINISTIC_TIME])),
        solve_time=reported(None if solve_time is None else round(solve_time, ExperimentDefaults.DURATION_DECIMALS)),
        duration=round(document[ResultKeys.DURATION_SECONDS], ExperimentDefaults.DURATION_DECIMALS),
        git_commit=document[ResultKeys.GIT_COMMIT],
        git_state=git_state_text(document[ResultKeys.GIT_DIRTY]),
    )


def strategies_text(strategies: StrategyChoices) -> str:
    """Les stratégies choisies, rôle par rôle, pour l'entrée du journal ; les paramètres seulement s'il y en a."""
    items = []
    for role, choice in strategies.by_role().items():
        parameters = ""
        if choice.parameters:
            parameters = ExplogTexts.STRATEGY_PARAMETERS.format(parameters=json.dumps(dict(choice.parameters)))
        items.append(ExplogTexts.STRATEGY_ITEM.format(role=role, name=choice.name, parameters=parameters))
    return ExplogTexts.STRATEGY_SEPARATOR.join(items)


def rounded(value: float | None) -> float | None:
    """``value`` arrondi pour le journal (``ExperimentDefaults.DETERMINISTIC_TIME_DECIMALS``) ; ``None`` reste ``None``."""
    return None if value is None else round(value, ExperimentDefaults.DETERMINISTIC_TIME_DECIMALS)


def git_state_text(git_dirty: bool | None) -> str:
    """La mention de l'état de la copie de travail, à la suite du commit dans l'entrée du journal."""
    if git_dirty is None:
        return ExplogTexts.GIT_UNKNOWN
    return ExplogTexts.GIT_DIRTY if git_dirty else ExplogTexts.GIT_CLEAN


def append_explog_entry(log_path: Path, entry: str) -> None:
    """Ajoute ``entry`` à la fin du journal ; crée le journal (avec son en-tête) s'il est absent ou vide."""
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if not log_path.exists() or log_path.stat().st_size == 0:
        log_path.write_text(ExplogTexts.HEADER, encoding=ExperimentDefaults.ENCODING)
    with log_path.open("a", encoding=ExperimentDefaults.ENCODING) as log:
        log.write(entry)


# ---------------------------------------------------------------------------------------------------------------------
# Ligne de commande
# ---------------------------------------------------------------------------------------------------------------------

def parse_arguments(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m experiments.drivers.run_experiment",
        description="Exécute une expérience décrite par un fichier de configuration JSON.",
    )
    parser.add_argument("config", type=Path, help="fichier de configuration (par convention dans experiments/config/)")
    parser.add_argument(
        "--results-dir", type=Path, default=None,
        help="répertoire des résultats (par défaut : experiments/results/<date du jour>/)",
    )
    parser.add_argument(
        "--log", type=Path, default=ExperimentDefaults.EXPLOG_FILE,
        help="journal des expériences (par défaut : experiments/EXPLOG.md)",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None, clock: Callable[[], datetime] = local_now) -> Path:
    """Exécute l'expérience de la ligne de commande ``argv`` ; rend le chemin du fichier de résultats."""
    arguments = parse_arguments(sys.argv[1:] if argv is None else argv)
    config = load_experiment_config(arguments.config)
    outcome = run_experiment(config, clock)
    results_dir = arguments.results_dir if arguments.results_dir is not None else default_results_dir(outcome.started_at)
    document = results_document(config, outcome)
    results_path = write_results(document, results_dir, config.name, outcome.started_at)
    append_explog_entry(arguments.log, explog_entry(config, document, results_path, outcome.started_at))
    print(ExperimentMessages.SUMMARY.format(
        best_total=document[ResultKeys.BEST][ResultKeys.BEST_COST][ResultKeys.TOTAL],
        calls=document[ResultKeys.SOLVER_EFFORT][SolverEffortFields.CALLS],
        results_path=display_path(results_path),
    ))
    return results_path


if __name__ == "__main__":
    main()
