"""Indirection vers les solveurs MiniZinc : options, limite d'effort, issue et statistiques d'une résolution.

Le reste du projet ne parle jamais directement à minizinc-python : il passe par un ``SolverAdapter``
(décision D2). Chaque adaptateur cache les particularités de son solveur, notamment la façon de limiter
l'effort (décision D10) :

    - ``WallTimeLimit`` : temps mural, compris par tous les solveurs, mais non reproductible ;
    - ``DeterministicTimeLimit`` : temps déterministe de CP-SAT (``max_deterministic_time``), reproductible
      avec un seul thread et une graine fixée.

Il n'existe pas de limite « générique » que chaque solveur traduirait : les unités d'effort ne sont pas
comparables d'un solveur à l'autre. Un adaptateur déclare les types de limites qu'il comprend, et refuse
les autres dès sa construction (``UnsupportedLimitError``).

Une résolution sans solution (insatisfiable, ou budget épuisé) n'est pas une erreur : c'est une issue
(``SolveOutcome``). Seules les pannes lèvent une exception.
"""

from abc import ABC, abstractmethod
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from datetime import timedelta
from enum import Enum
from typing import Any

import minizinc

from src.config import ProjectPaths
from src.model.shift_rules import ModelVariableNames
from src.utils.io import InstanceFields, ProblemInstance
from src.utils.minizinc_env import locate_minizinc_driver, lookup_solver


# ---------------------------------------------------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------------------------------------------------

class SolverIds:
    """Identifiants des solveurs dans la distribution MiniZinc (``minizinc --solvers``)."""

    CP_SAT: str = "cp-sat"


class SolverDefaults:
    """Valeurs par défaut des options d'un solveur."""

    # Un seul thread : condition de la reproductibilité de CP-SAT sous limite déterministe (D7, D10).
    THREADS: int = 1
    SEED: int = 0

    # Ordre de grandeur mesuré le 2026-11-08 : environ 5 unités pour une première solution de bench_3
    # sans variable fixée ; un sous-problème avec un employé libéré se résout en bien moins.
    DETERMINISTIC_TIME_UNITS: float = 5.0

    # Plus petite valeur acceptée pour un nombre de threads.
    MIN_THREADS: int = 1


class ModelObjective:
    """Nom de la variable objectif de ``horaire.mzn``."""

    TOTAL_COST: str = "cout_total"


class MiniZincStatisticNames:
    """Noms standard des statistiques rapportées par MiniZinc (tous les solveurs ne les rapportent pas toutes)."""

    NODES: str = "nodes"
    FAILURES: str = "failures"
    PROPAGATIONS: str = "propagations"
    SOLVE_TIME: str = "solveTime"


class CpSatFlags:
    """Options de ligne de commande propres à CP-SAT, transmises par minizinc-python.

    minizinc-python transmet chaque mot-clé tel quel, préfixé de ``--`` : il faut écrire ``fzn-flags``,
    car ``fzn_flags`` deviendrait ``--fzn_flags``, que MiniZinc refuse.
    """

    FZN_FLAGS_OPTION: str = "fzn-flags"
    PARAMS_TEMPLATE: str = "--params {parameters}"

    # Paramètres de ``SatParameters`` (proto texte), séparés par des virgules.
    PARAMETER_TEMPLATE: str = "{name}:{value}"
    PARAMETER_SEPARATOR: str = ","
    MAX_DETERMINISTIC_TIME: str = "max_deterministic_time"
    RANDOM_SEED: str = "random_seed"


class MiniZincPythonArguments:
    """Mots-clés de ``minizinc.Instance.solve`` utilisés par les adaptateurs."""

    THREADS: str = "processes"
    TIME_LIMIT: str = "time_limit"
    INTERMEDIATE_SOLUTIONS: str = "intermediate_solutions"


# ---------------------------------------------------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------------------------------------------------

class SolverMessages:
    """Gabarits des messages d'erreur des solveurs."""

    UNSUPPORTED_LIMIT: str = "Le solveur {solver_id} ne comprend pas la limite {limit} ; limites comprises : {supported}."
    NON_POSITIVE_LIMIT: str = "La limite {limit} doit être strictement positive ; trouvé {value}."
    INVALID_THREADS: str = "Le nombre de threads doit être au moins {minimum} ; trouvé {value}."
    SOLVER_FAILURE: str = "Le solveur {solver_id} a échoué sur l'instance {instance} : {detail}"
    UNEXPECTED_STATUS: str = "Le solveur {solver_id} a rendu le statut inattendu {status} sur l'instance {instance}."


class SolverError(Exception):
    """Erreur de base pour toute panne d'un solveur (jamais pour une simple absence de solution)."""


class InvalidSolverOptionsError(SolverError):
    """Une option du solveur est hors de son domaine (limite nulle ou négative, nombre de threads invalide)."""


class UnsupportedLimitError(SolverError):
    """L'adaptateur ne sait pas traduire ce type de limite d'effort pour son solveur."""


class SolverFailureError(SolverError):
    """MiniZinc ou le solveur a échoué (erreur de syntaxe dans une contrainte ajoutée, statut ERROR, …)."""


# ---------------------------------------------------------------------------------------------------------------------
# Options
# ---------------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class EffortLimit:
    """Limite d'effort d'une résolution. Classe de base : seules ses sous-classes sont utilisées."""


@dataclass(frozen=True)
class WallTimeLimit(EffortLimit):
    """Temps mural en secondes. Compris par tous les solveurs, mais les résultats ne sont pas reproductibles."""

    seconds: float

    def __post_init__(self) -> None:
        if self.seconds <= 0:
            raise InvalidSolverOptionsError(
                SolverMessages.NON_POSITIVE_LIMIT.format(limit=type(self).__name__, value=self.seconds)
            )


@dataclass(frozen=True)
class DeterministicTimeLimit(EffortLimit):
    """Temps déterministe de CP-SAT (``max_deterministic_time``), en unités propres à CP-SAT.

    Reproductible avec un seul thread et une graine fixée. Une unité vaut environ une seconde de calcul,
    mais ce n'est pas une durée : seul compte le fait que deux appels identiques font le même travail.
    """

    units: float

    def __post_init__(self) -> None:
        if self.units <= 0:
            raise InvalidSolverOptionsError(
                SolverMessages.NON_POSITIVE_LIMIT.format(limit=type(self).__name__, value=self.units)
            )


@dataclass(frozen=True)
class SolverOptions:
    """Options d'une résolution : limite d'effort, graine et nombre de threads."""

    limit: EffortLimit = field(default_factory=lambda: DeterministicTimeLimit(SolverDefaults.DETERMINISTIC_TIME_UNITS))
    seed: int = SolverDefaults.SEED
    threads: int = SolverDefaults.THREADS

    def __post_init__(self) -> None:
        if self.threads < SolverDefaults.MIN_THREADS:
            raise InvalidSolverOptionsError(
                SolverMessages.INVALID_THREADS.format(minimum=SolverDefaults.MIN_THREADS, value=self.threads)
            )


# ---------------------------------------------------------------------------------------------------------------------
# Résultat d'une résolution
# ---------------------------------------------------------------------------------------------------------------------

class SolveOutcome(Enum):
    """Issue d'une résolution, indépendante du solveur."""

    OPTIMAL = "optimal"                # solution prouvée optimale (pour le problème posé, contraintes ajoutées comprises)
    FEASIBLE = "feasible"              # solution trouvée, optimalité non prouvée (budget épuisé)
    UNSATISFIABLE = "unsatisfiable"    # aucune solution n'existe
    NO_SOLUTION = "no_solution"        # budget épuisé avant toute solution

    @property
    def has_solution(self) -> bool:
        """Vrai si la résolution a produit une solution."""
        return self in (SolveOutcome.OPTIMAL, SolveOutcome.FEASIBLE)


@dataclass(frozen=True)
class SolverStatistics:
    """Charge de travail d'une résolution (D10), d'après les statistiques standard de MiniZinc.

    Chaque champ vaut ``None`` si le solveur ne le rapporte pas (CP-SAT ne rapporte pas ``nodes``).
    ``nodes``, ``failures`` et ``propagations`` sont déterministes sous limite déterministe ;
    ``solve_time`` ne l'est jamais (D8).
    """

    nodes: int | None = None
    failures: int | None = None
    propagations: int | None = None
    solve_time: timedelta | None = None


@dataclass(frozen=True)
class SolverRun:
    """Résultat d'une résolution : issue, meilleure solution trouvée et statistiques.

    ``variables`` associe chaque nom de ``ModelVariableNames`` à sa liste indexée par employé, dans la forme
    attendue par ``Horaire.from_model_variables`` ; il vaut ``None`` si aucune solution n'a été trouvée,
    comme ``objective``.
    """

    outcome: SolveOutcome
    variables: Mapping[str, Sequence[Any]] | None
    objective: int | None
    statistics: SolverStatistics


# ---------------------------------------------------------------------------------------------------------------------
# Adaptateurs
# ---------------------------------------------------------------------------------------------------------------------

class SolverAdapter(ABC):
    """Indirection vers un solveur MiniZinc (D2) : traduit les options, lance ``horaire.mzn``, traduit le résultat.

    Patron Méthode modèle : ``solve`` est commun à tous les solveurs ; une sous-classe ne fournit que son
    identifiant, les limites qu'elle comprend et la traduction des options en arguments de minizinc-python.
    """

    # Variables de décision récupérées dans chaque solution, une liste indexée par employé.
    EMPLOYEE_VARIABLES: tuple[str, ...] = (
        ModelVariableNames.START,
        ModelVariableNames.BREAK1,
        ModelVariableNames.LUNCH,
        ModelVariableNames.BREAK2,
        ModelVariableNames.END,
        ModelVariableNames.ACTIVITIES,
    )

    def __init__(self, options: SolverOptions = SolverOptions()) -> None:
        """Vérifie que la limite est comprise, puis localise MiniZinc et le solveur.

        Raises:
            UnsupportedLimitError: si le type de ``options.limit`` n'est pas dans ``supported_limits()``.
            MiniZincNotFoundError, SolverNotAvailableError: propagées depuis ``src.utils.minizinc_env``.
        """
        if not isinstance(options.limit, self.supported_limits()):
            supported_names = ", ".join(limit_type.__name__ for limit_type in self.supported_limits())
            raise UnsupportedLimitError(
                SolverMessages.UNSUPPORTED_LIMIT.format(
                    solver_id=self.solver_id(), limit=type(options.limit).__name__, supported=supported_names
                )
            )
        self.options = options
        self.solver = lookup_solver(self.solver_id(), locate_minizinc_driver())

    @classmethod
    @abstractmethod
    def solver_id(cls) -> str:
        """Identifiant du solveur dans la distribution MiniZinc."""

    @classmethod
    @abstractmethod
    def supported_limits(cls) -> tuple[type[EffortLimit], ...]:
        """Types de limites d'effort que cet adaptateur sait traduire."""

    @abstractmethod
    def solver_arguments(self) -> dict[str, Any]:
        """Arguments de ``minizinc.Instance.solve`` qui traduisent ``self.options`` pour ce solveur."""

    def solve(self, instance: ProblemInstance, extra_constraints: Sequence[str] = ()) -> SolverRun:
        """Résout ``horaire.mzn`` sur ``instance``, avec en plus les contraintes MiniZinc ``extra_constraints``.

        Chaque élément de ``extra_constraints`` est un item MiniZinc complet (ex. ``"constraint debut[1] = 4;"``).
        Sans contrainte ajoutée, c'est la résolution complète du modèle (référence de D10).

        Raises:
            SolverFailureError: si MiniZinc échoue (contrainte mal formée, statut ERROR ou inattendu).
        """
        minizinc_instance = minizinc.Instance(self.solver, minizinc.Model(ProjectPaths.MODEL_FILE))
        self._assign_instance_data(minizinc_instance, instance)
        for constraint in extra_constraints:
            minizinc_instance.add_string(constraint)

        try:
            # Solutions intermédiaires : quelle que soit la façon dont le solveur s'arrête, la dernière reçue
            # est la meilleure trouvée.
            result = minizinc_instance.solve(
                **{MiniZincPythonArguments.INTERMEDIATE_SOLUTIONS: True}, **self.solver_arguments()
            )
        except minizinc.MiniZincError as error:
            raise SolverFailureError(
                SolverMessages.SOLVER_FAILURE.format(solver_id=self.solver_id(), instance=instance.name, detail=error)
            ) from error

        outcome = self._outcome_of(result.status, instance)
        statistics = self._statistics_of(result.statistics)
        if not outcome.has_solution:
            return SolverRun(outcome=outcome, variables=None, objective=None, statistics=statistics)

        best_solution = result.solution[-1]
        variables = {name: getattr(best_solution, name) for name in self.EMPLOYEE_VARIABLES}
        return SolverRun(
            outcome=outcome, variables=variables, objective=int(best_solution.objective), statistics=statistics
        )

    @staticmethod
    def _assign_instance_data(minizinc_instance: minizinc.Instance, instance: ProblemInstance) -> None:
        """Transmet les paramètres de ``instance`` à MiniZinc, sans passer par un fichier."""
        minizinc_instance[InstanceFields.EMPLOYEE_COUNT] = instance.employee_count
        minizinc_instance[InstanceFields.ACTIVITY_COUNT] = instance.activity_count
        minizinc_instance[InstanceFields.PERIOD_COUNT] = instance.period_count
        minizinc_instance[InstanceFields.DEMAND] = instance.demand.tolist()
        minizinc_instance[InstanceFields.OVER_COST] = instance.over_cost.tolist()
        minizinc_instance[InstanceFields.UNDER_COST] = instance.under_cost.tolist()

    def _outcome_of(self, status: minizinc.Status, instance: ProblemInstance) -> SolveOutcome:
        """Traduit un statut minizinc-python en issue ; ERROR et UNBOUNDED sont des pannes.

        Raises:
            SolverFailureError: pour un statut qui ne correspond à aucune issue.
        """
        outcomes_by_status = {
            minizinc.Status.OPTIMAL_SOLUTION: SolveOutcome.OPTIMAL,
            minizinc.Status.SATISFIED: SolveOutcome.FEASIBLE,
            minizinc.Status.ALL_SOLUTIONS: SolveOutcome.FEASIBLE,
            minizinc.Status.UNSATISFIABLE: SolveOutcome.UNSATISFIABLE,
            minizinc.Status.UNKNOWN: SolveOutcome.NO_SOLUTION,
        }
        if status not in outcomes_by_status:
            raise SolverFailureError(
                SolverMessages.UNEXPECTED_STATUS.format(solver_id=self.solver_id(), status=status.name, instance=instance.name)
            )
        return outcomes_by_status[status]

    @staticmethod
    def _statistics_of(raw_statistics: Mapping[str, Any]) -> SolverStatistics:
        """Extrait les statistiques standard ; une statistique absente vaut ``None``."""

        def optional_int(name: str) -> int | None:
            value = raw_statistics.get(name)
            return None if value is None else int(value)

        return SolverStatistics(
            nodes=optional_int(MiniZincStatisticNames.NODES),
            failures=optional_int(MiniZincStatisticNames.FAILURES),
            propagations=optional_int(MiniZincStatisticNames.PROPAGATIONS),
            solve_time=raw_statistics.get(MiniZincStatisticNames.SOLVE_TIME),
        )


class CpSatAdapter(SolverAdapter):
    """Adaptateur pour OR-Tools CP-SAT, le solveur par défaut (D2).

    Limites comprises : ``DeterministicTimeLimit`` (par défaut, reproductible avec un seul thread)
    et ``WallTimeLimit``. La graine est transmise dans les deux cas.
    """

    @classmethod
    def solver_id(cls) -> str:
        return SolverIds.CP_SAT

    @classmethod
    def supported_limits(cls) -> tuple[type[EffortLimit], ...]:
        return DeterministicTimeLimit, WallTimeLimit

    def solver_arguments(self) -> dict[str, Any]:
        parameters = [CpSatFlags.PARAMETER_TEMPLATE.format(name=CpSatFlags.RANDOM_SEED, value=self.options.seed)]
        arguments: dict[str, Any] = {MiniZincPythonArguments.THREADS: self.options.threads}

        limit = self.options.limit
        if isinstance(limit, DeterministicTimeLimit):
            parameters.append(
                CpSatFlags.PARAMETER_TEMPLATE.format(name=CpSatFlags.MAX_DETERMINISTIC_TIME, value=limit.units)
            )
        elif isinstance(limit, WallTimeLimit):
            arguments[MiniZincPythonArguments.TIME_LIMIT] = timedelta(seconds=limit.seconds)

        arguments[CpSatFlags.FZN_FLAGS_OPTION] = CpSatFlags.PARAMS_TEMPLATE.format(
            parameters=CpSatFlags.PARAMETER_SEPARATOR.join(parameters)
        )
        return arguments
