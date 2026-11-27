"""Témoin « CP-SAT seul » : une résolution de l'instance complète, sans mémétique (étape 10g).

Usage, depuis la racine du dépôt :

    python -m experiments.drivers.run_cpsat_alone CONFIG [--results-dir RÉPERTOIRE] [--log JOURNAL]

CP-SAT résout l'instance entière, dans les conditions des sous-problèmes du mémétique : un seul thread, limite
déterministe (``max_deterministic_time``), graine fixée. On garde **toutes** ses solutions intermédiaires, chacune
avec l'effort dépensé au moment où elle est trouvée (``solveTime``, propagations, failures), pour tracer le meilleur
coût en fonction de l'effort cumulé et le comparer à celui du mémétique (docs/archive/TODO.md, étape 10 : courbes « meilleur coût
en fonction de l'effort cumulé du solveur »).

Format de la configuration (``CpSatAloneKeys``) :

    {
      "description": "Texte lisible.",
      "instance": "bench_3",
      "model": "reference",            # "reference" (horaire.mzn, couverture dure) ou "relaxed" (horaire_assoupli.mzn)
      "seed": 0,
      "deterministic_time_units": 5400
    }

On appelle l'exécutable ``minizinc`` directement (``-i -s``) : il imprime les statistiques du solveur après chaque
solution, ce que l'interface ``SolverAdapter`` (qui ne garde que la dernière solution) ne rend pas.
"""

import argparse
import json
import platform
import re
import subprocess
import sys
import time
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any

from experiments.drivers.run_experiment import (
    ExperimentDefaults,
    append_explog_entry,
    default_results_dir,
    display_path,
    git_state_text,
    local_now,
    write_results,
)
from src.config import MiniZincConfig, ProjectPaths
from src.memetic.solver import CpSatFlags, RelaxedModelNames
from src.model.evaluation import PenaltyWeights
from src.observability.run_directory import current_git_commit, working_tree_is_dirty
from src.utils.minizinc_env import locate_minizinc_driver


# ---------------------------------------------------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------------------------------------------------

class CpSatAloneKeys:
    """Clés du fichier de configuration."""

    DESCRIPTION: str = "description"
    INSTANCE: str = "instance"
    MODEL: str = "model"
    SEED: str = "seed"
    DETERMINISTIC_TIME_UNITS: str = "deterministic_time_units"

    REQUIRED: tuple[str, ...] = (DESCRIPTION, INSTANCE, MODEL, SEED, DETERMINISTIC_TIME_UNITS)


class ModelChoices:
    """Noms des modèles acceptés dans la configuration, et fichier de chacun."""

    REFERENCE: str = "reference"
    RELAXED: str = "relaxed"

    FILES: dict[str, Path] = {
        REFERENCE: ProjectPaths.REFERENCE_MODEL_FILE,
        RELAXED: ProjectPaths.RELAXED_MODEL_FILE,
    }


class CpSatAloneDefaults:
    """Réglages fixes du témoin."""

    # Un seul thread : mêmes conditions que les sous-problèmes du mémétique (SolverDefaults.THREADS).
    THREADS: int = 1
    INSTANCE_EXTENSION: str = ".json"
    RESULTS_SCHEMA_VERSION: int = 1
    # Constante MiniZinc passée par -D au modèle assoupli : « NOM=valeur; ».
    DEFINE_TEMPLATE: str = "{name}={value};"
    VERSION_SEPARATOR: str = "."


class MiniZincCliFlags:
    """Options de la ligne de commande ``minizinc`` utilisées par le témoin."""

    SOLVER: str = "--solver"
    THREADS: str = "-p"
    ALL_INTERMEDIATE_SOLUTIONS: str = "-i"
    STATISTICS: str = "-s"
    DEFINE: str = "-D"
    LONG_OPTION_PREFIX: str = "--"


class MiniZincOutput:
    """Repères de la sortie texte de ``minizinc -i -s``."""

    # Une statistique : « %%%mzn-stat: nom=valeur ».
    STAT_PATTERN: re.Pattern[str] = re.compile(r"^%%%mzn-stat: (\w+)=(.*)$")
    SOLUTION_SEPARATOR: str = "----------"
    SEARCH_COMPLETE: str = "=========="
    UNSATISFIABLE: str = "=====UNSATISFIABLE====="

    OBJECTIVE: str = "objective"
    SOLVE_TIME: str = "solveTime"
    PROPAGATIONS: str = "propagations"
    FAILURES: str = "failures"
    FLAT_TIME: str = "flatTime"


class CpSatAloneResultKeys:
    """Clés du fichier de résultats."""

    SCHEMA_VERSION: str = "schema_version"
    EXPERIMENT: str = "experiment"
    DESCRIPTION: str = "description"
    CONFIG_PATH: str = "config_path"
    INSTANCE: str = "instance"
    MODEL: str = "model"
    MODEL_FILE: str = "model_file"
    SEED: str = "seed"
    DETERMINISTIC_TIME_UNITS: str = "deterministic_time_units"
    THREADS: str = "threads"
    STARTED_AT: str = "started_at"
    DURATION_SECONDS: str = "duration_seconds"
    GIT_COMMIT: str = "git_commit"
    GIT_DIRTY: str = "git_dirty"
    PYTHON_VERSION: str = "python_version"
    MINIZINC_VERSION: str = "minizinc_version"
    BEST_OBJECTIVE: str = "best_objective"
    PROVEN_OPTIMAL: str = "proven_optimal"
    SOLUTIONS: str = "solutions"
    FINAL_STATISTICS: str = "final_statistics"

    # Un point de la trajectoire.
    OBJECTIVE: str = "objective"
    SOLVE_TIME_SECONDS: str = "solve_time_seconds"
    PROPAGATIONS: str = "propagations"
    FAILURES: str = "failures"


class CpSatAloneTexts:
    """Gabarits de l'entrée d'EXPLOG.md et du résumé imprimé."""

    ENTRY: str = (
        "\n## {timestamp} — {experiment}\n\n"
        "{description}\n\n"
        "- Configuration : `{config_path}`\n"
        "- Résultats : `{results_path}`\n"
        "- Témoin CP-SAT seul : instance {instance} ; modèle `{model}` ; graine {seed} ; {threads} thread ; "
        "limite déterministe {units}\n"
        "- **Meilleur coût : {best}** ({proof}) ; {solutions} solutions intermédiaires\n"
        "- **Effort du solveur** : propagations {propagations} ; failures {failures} ; "
        "temps de résolution {solve_time} s (non déterministe)\n"
        "- Durée de l'exécution : {duration} s ; commit `{git_commit}`{git_state}\n"
    )
    PROVEN: str = "optimum prouvé"
    NOT_PROVEN: str = "non prouvé"
    NO_SOLUTION: str = "aucune solution"
    SUMMARY: str = "Meilleur coût {best} ({proof}), {solutions} solutions ; résultats : {results_path}"


# ---------------------------------------------------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------------------------------------------------

class CpSatAloneMessages:
    """Gabarits des messages d'erreur du témoin."""

    MISSING_KEY: str = "Configuration {path} : clé obligatoire {key} absente."
    UNKNOWN_KEY: str = "Configuration {path} : clé inconnue {key}."
    INVALID_JSON: str = "Configuration {path} : JSON invalide ({detail})."
    UNKNOWN_MODEL: str = "Configuration {path} : modèle {model} inconnu ; modèles permis : {allowed}."
    INSTANCE_NOT_FOUND: str = "Configuration {path} : instance {instance} introuvable ({instance_path})."
    NON_POSITIVE_LIMIT: str = "Configuration {path} : limite déterministe {value} non strictement positive."
    WRONG_TYPE: str = "Configuration {path} : la clé {key} doit être de type {expected} ; trouvé {value!r}."
    SOLVER_FAILURE: str = "MiniZinc a échoué (code {code}) sur {instance} : {detail}"


class CpSatAloneError(Exception):
    """Erreur de base du témoin CP-SAT seul."""


class InvalidCpSatAloneConfigError(CpSatAloneError):
    """Le fichier de configuration est illisible ou incomplet, ou une valeur est hors de son domaine."""


class CpSatAloneSolverError(CpSatAloneError):
    """L'exécutable MiniZinc s'est terminé en erreur."""


# ---------------------------------------------------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class CpSatAloneConfig:
    """Une résolution « CP-SAT seul » telle que décrite par son fichier de configuration."""

    path: Path
    description: str
    instance_name: str
    model: str
    seed: int
    deterministic_time_units: float

    @property
    def name(self) -> str:
        return self.path.stem

    @property
    def instance_path(self) -> Path:
        return ProjectPaths.DATA_DIR / (self.instance_name + CpSatAloneDefaults.INSTANCE_EXTENSION)

    @property
    def model_file(self) -> Path:
        return ModelChoices.FILES[self.model]


def load_cpsat_alone_config(path: Path) -> CpSatAloneConfig:
    """Lit et valide un fichier de configuration du témoin.

    Raises:
        InvalidCpSatAloneConfigError: JSON invalide, clé absente ou inconnue, mauvais type, modèle inconnu,
            instance introuvable, limite non strictement positive.
    """
    try:
        raw = json.loads(path.read_text(encoding=ExperimentDefaults.ENCODING))
    except json.JSONDecodeError as error:
        raise InvalidCpSatAloneConfigError(CpSatAloneMessages.INVALID_JSON.format(path=path, detail=error)) from error
    for key in CpSatAloneKeys.REQUIRED:
        if key not in raw:
            raise InvalidCpSatAloneConfigError(CpSatAloneMessages.MISSING_KEY.format(path=path, key=key))
    for key in raw:
        if key not in CpSatAloneKeys.REQUIRED:
            raise InvalidCpSatAloneConfigError(CpSatAloneMessages.UNKNOWN_KEY.format(path=path, key=key))
    check_type(path, CpSatAloneKeys.DESCRIPTION, raw[CpSatAloneKeys.DESCRIPTION], (str,))
    check_type(path, CpSatAloneKeys.INSTANCE, raw[CpSatAloneKeys.INSTANCE], (str,))
    check_type(path, CpSatAloneKeys.MODEL, raw[CpSatAloneKeys.MODEL], (str,))
    check_type(path, CpSatAloneKeys.SEED, raw[CpSatAloneKeys.SEED], (int,))
    check_type(path, CpSatAloneKeys.DETERMINISTIC_TIME_UNITS, raw[CpSatAloneKeys.DETERMINISTIC_TIME_UNITS], (int, float))

    model = raw[CpSatAloneKeys.MODEL]
    if model not in ModelChoices.FILES:
        raise InvalidCpSatAloneConfigError(CpSatAloneMessages.UNKNOWN_MODEL.format(
            path=path, model=model, allowed=", ".join(ModelChoices.FILES),
        ))
    units = raw[CpSatAloneKeys.DETERMINISTIC_TIME_UNITS]
    if units <= 0:
        raise InvalidCpSatAloneConfigError(CpSatAloneMessages.NON_POSITIVE_LIMIT.format(path=path, value=units))
    config = CpSatAloneConfig(
        path=path,
        description=raw[CpSatAloneKeys.DESCRIPTION],
        instance_name=raw[CpSatAloneKeys.INSTANCE],
        model=model,
        seed=raw[CpSatAloneKeys.SEED],
        deterministic_time_units=float(units),
    )
    if not config.instance_path.exists():
        raise InvalidCpSatAloneConfigError(CpSatAloneMessages.INSTANCE_NOT_FOUND.format(
            path=path, instance=config.instance_name, instance_path=config.instance_path,
        ))
    return config


def check_type(path: Path, key: str, value: Any, expected: tuple[type, ...]) -> None:
    """Refuse ``value`` si elle n'est pas d'un des types ``expected`` (un booléen n'est jamais un nombre)."""
    if isinstance(value, bool) or not isinstance(value, expected):
        raise InvalidCpSatAloneConfigError(CpSatAloneMessages.WRONG_TYPE.format(
            path=path, key=key, expected=" ou ".join(kind.__name__ for kind in expected), value=value,
        ))


# ---------------------------------------------------------------------------------------------------------------------
# Lecture de la sortie de MiniZinc
# ---------------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class SolverTrace:
    """Ce que rend une résolution : les solutions dans l'ordre, la preuve d'optimalité et les statistiques finales."""

    solutions: list[dict[str, Any]]
    proven_optimal: bool
    final_statistics: dict[str, Any]


def parse_stat_value(text: str) -> Any:
    """Une valeur de statistique : entier, sinon flottant, sinon le texte sans guillemets."""
    stripped = text.strip()
    for convert in (int, float):
        try:
            return convert(stripped)
        except ValueError:
            pass
    return stripped.strip('"')


def parse_minizinc_output(text: str) -> SolverTrace:
    """Découpe la sortie de ``minizinc -i -s`` : une solution par séparateur ``----------``, avec les statistiques
    imprimées juste avant lui ; les statistiques après la dernière solution sont les statistiques finales.

    L'objectif est arrondi à l'entier : CP-SAT l'imprime en notation scientifique (``7.00008e+06``), mais les deux
    modèles minimisent une somme entière.
    """
    solutions: list[dict[str, Any]] = []
    pending: dict[str, Any] = {}
    proven_optimal = False
    for line in text.splitlines():
        stripped = line.strip()
        match = MiniZincOutput.STAT_PATTERN.match(stripped)
        if match:
            pending[match.group(1)] = parse_stat_value(match.group(2))
        elif stripped == MiniZincOutput.SOLUTION_SEPARATOR:
            if MiniZincOutput.OBJECTIVE in pending:
                solutions.append(solution_point(pending))
            pending = {}
        elif stripped == MiniZincOutput.SEARCH_COMPLETE:
            proven_optimal = bool(solutions)
    return SolverTrace(solutions=solutions, proven_optimal=proven_optimal, final_statistics=pending)


def solution_point(statistics: Mapping[str, Any]) -> dict[str, Any]:
    """Un point de la trajectoire : coût de la solution et effort dépensé jusqu'à elle."""
    return {
        CpSatAloneResultKeys.OBJECTIVE: round(statistics[MiniZincOutput.OBJECTIVE]),
        CpSatAloneResultKeys.SOLVE_TIME_SECONDS: statistics.get(MiniZincOutput.SOLVE_TIME),
        CpSatAloneResultKeys.PROPAGATIONS: statistics.get(MiniZincOutput.PROPAGATIONS),
        CpSatAloneResultKeys.FAILURES: statistics.get(MiniZincOutput.FAILURES),
    }


# ---------------------------------------------------------------------------------------------------------------------
# Exécution
# ---------------------------------------------------------------------------------------------------------------------

def minizinc_command(config: CpSatAloneConfig, executable: Path) -> list[str]:
    """La ligne de commande : CP-SAT, un thread, toutes les solutions et leurs statistiques, limite et graine."""
    parameters = CpSatFlags.PARAMETER_SEPARATOR.join((
        CpSatFlags.PARAMETER_TEMPLATE.format(
            name=CpSatFlags.MAX_DETERMINISTIC_TIME, value=config.deterministic_time_units),
        CpSatFlags.PARAMETER_TEMPLATE.format(name=CpSatFlags.RANDOM_SEED, value=config.seed),
    ))
    command = [
        str(executable),
        MiniZincCliFlags.SOLVER, MiniZincConfig.DEFAULT_SOLVER_ID,
        MiniZincCliFlags.THREADS, str(CpSatAloneDefaults.THREADS),
        MiniZincCliFlags.ALL_INTERMEDIATE_SOLUTIONS, MiniZincCliFlags.STATISTICS,
        MiniZincCliFlags.LONG_OPTION_PREFIX + CpSatFlags.FZN_FLAGS_OPTION, CpSatFlags.PARAMS_TEMPLATE.format(parameters=parameters),
    ]
    if config.model == ModelChoices.RELAXED:
        command += [MiniZincCliFlags.DEFINE, CpSatAloneDefaults.DEFINE_TEMPLATE.format(
            name=RelaxedModelNames.COVERAGE_WEIGHT, value=PenaltyWeights().coverage_violation,
        )]
    return command + [str(config.model_file), str(config.instance_path)]


def run_cpsat_alone(config: CpSatAloneConfig) -> tuple[SolverTrace, float, str]:
    """Lance la résolution ; rend la trace, la durée murale et la version de MiniZinc.

    Raises:
        CpSatAloneSolverError: si ``minizinc`` se termine avec un code non nul.
    """
    driver = locate_minizinc_driver()
    start = time.perf_counter()
    completed = subprocess.run(
        minizinc_command(config, Path(driver.executable)), capture_output=True, text=True, check=False,
    )
    duration = time.perf_counter() - start
    if completed.returncode != 0:
        raise CpSatAloneSolverError(CpSatAloneMessages.SOLVER_FAILURE.format(
            code=completed.returncode, instance=config.instance_name, detail=completed.stderr.strip(),
        ))
    return parse_minizinc_output(completed.stdout), duration, version_text(driver.parsed_version)


def version_text(version: Sequence[int]) -> str:
    """La version de MiniZinc sous la forme « 2.10.0 »."""
    return CpSatAloneDefaults.VERSION_SEPARATOR.join(str(part) for part in version)


def results_document(
        config: CpSatAloneConfig, trace: SolverTrace, duration: float, minizinc_version: str,
        started_at: datetime, git_commit: str, git_dirty: bool | None,
) -> dict[str, Any]:
    """Le contenu du fichier de résultats."""
    keys = CpSatAloneResultKeys
    best = trace.solutions[-1][keys.OBJECTIVE] if trace.solutions else None
    return {
        keys.SCHEMA_VERSION: CpSatAloneDefaults.RESULTS_SCHEMA_VERSION,
        keys.EXPERIMENT: config.name,
        keys.DESCRIPTION: config.description,
        keys.CONFIG_PATH: display_path(config.path),
        keys.INSTANCE: config.instance_name,
        keys.MODEL: config.model,
        keys.MODEL_FILE: display_path(config.model_file),
        keys.SEED: config.seed,
        keys.DETERMINISTIC_TIME_UNITS: config.deterministic_time_units,
        keys.THREADS: CpSatAloneDefaults.THREADS,
        keys.STARTED_AT: started_at.isoformat(),
        keys.DURATION_SECONDS: duration,
        keys.GIT_COMMIT: git_commit,
        keys.GIT_DIRTY: git_dirty,
        keys.PYTHON_VERSION: platform.python_version(),
        keys.MINIZINC_VERSION: minizinc_version,
        keys.BEST_OBJECTIVE: best,
        keys.PROVEN_OPTIMAL: trace.proven_optimal,
        keys.SOLUTIONS: trace.solutions,
        keys.FINAL_STATISTICS: trace.final_statistics,
    }


def explog_entry(document: Mapping[str, Any], results_path: Path, started_at: datetime) -> str:
    """L'entrée d'EXPLOG.md d'une résolution « CP-SAT seul »."""
    keys = CpSatAloneResultKeys
    final = document[keys.FINAL_STATISTICS]
    solve_time = final.get(MiniZincOutput.SOLVE_TIME)
    return CpSatAloneTexts.ENTRY.format(
        timestamp=started_at.strftime(ExperimentDefaults.LOG_TIMESTAMP_FORMAT),
        experiment=document[keys.EXPERIMENT],
        description=document[keys.DESCRIPTION],
        config_path=document[keys.CONFIG_PATH],
        results_path=display_path(results_path),
        instance=document[keys.INSTANCE],
        model=document[keys.MODEL],
        seed=document[keys.SEED],
        threads=document[keys.THREADS],
        units=document[keys.DETERMINISTIC_TIME_UNITS],
        best=document[keys.BEST_OBJECTIVE],
        proof=proof_text(document),
        solutions=len(document[keys.SOLUTIONS]),
        propagations=final.get(MiniZincOutput.PROPAGATIONS),
        failures=final.get(MiniZincOutput.FAILURES),
        solve_time=None if solve_time is None else round(solve_time, ExperimentDefaults.DURATION_DECIMALS),
        duration=round(document[keys.DURATION_SECONDS], ExperimentDefaults.DURATION_DECIMALS),
        git_commit=document[keys.GIT_COMMIT],
        git_state=git_state_text(document[keys.GIT_DIRTY]),
    )


def proof_text(document: Mapping[str, Any]) -> str:
    if document[CpSatAloneResultKeys.BEST_OBJECTIVE] is None:
        return CpSatAloneTexts.NO_SOLUTION
    return CpSatAloneTexts.PROVEN if document[CpSatAloneResultKeys.PROVEN_OPTIMAL] else CpSatAloneTexts.NOT_PROVEN


# ---------------------------------------------------------------------------------------------------------------------
# Ligne de commande
# ---------------------------------------------------------------------------------------------------------------------

def parse_arguments(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="python -m experiments.drivers.run_cpsat_alone",
        description="Témoin CP-SAT seul : résout l'instance complète et garde toutes les solutions intermédiaires.",
    )
    parser.add_argument("config", type=Path, help="fichier de configuration du témoin")
    parser.add_argument("--results-dir", type=Path, default=None,
                        help="répertoire des résultats (par défaut : experiments/results/<date du jour>/)")
    parser.add_argument("--log", type=Path, default=ExperimentDefaults.EXPLOG_FILE,
                        help="journal des expériences (par défaut : experiments/EXPLOG.md)")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None, clock: Callable[[], datetime] = local_now) -> Path:
    """Exécute le témoin de la ligne de commande ``argv`` ; rend le chemin du fichier de résultats."""
    arguments = parse_arguments(sys.argv[1:] if argv is None else argv)
    config = load_cpsat_alone_config(arguments.config)
    started_at = clock()
    git_commit = current_git_commit()
    git_dirty = working_tree_is_dirty(excluded=ExperimentDefaults.GIT_DIRTY_EXCLUDED)
    trace, duration, minizinc_version = run_cpsat_alone(config)
    document = results_document(config, trace, duration, minizinc_version, started_at, git_commit, git_dirty)
    results_dir = arguments.results_dir if arguments.results_dir is not None else default_results_dir(started_at)
    results_path = write_results(document, results_dir, config.name, started_at)
    append_explog_entry(arguments.log, explog_entry(document, results_path, started_at))
    print(CpSatAloneTexts.SUMMARY.format(
        best=document[CpSatAloneResultKeys.BEST_OBJECTIVE], proof=proof_text(document),
        solutions=len(trace.solutions), results_path=display_path(results_path),
    ))
    return results_path


if __name__ == "__main__":
    main()
