"""Collecteurs de mesures (décision D8) : ils transforment les événements du moteur en enregistrements.

Un collecteur reçoit chaque événement (``events.py``) et rend zéro, un ou plusieurs enregistrements
(``events.make_record``), que ``ObservationHub`` écrit dans les destinations. Il peut garder un état d'un événement
à l'autre (par exemple des compteurs cumulés).

Règles (D8) :
    - un collecteur ne consomme **jamais** le générateur aléatoire du moteur ; s'il échantillonne, il a le sien ;
    - les valeurs des enregistrements sont des types simples de Python (``int``, ``float``, ``str``, listes,
      dictionnaires), jamais des types numpy : convertir avec ``int(...)`` ou ``float(...)`` ;
    - bibliothèque standard seulement (``statistics`` pour moyenne, médiane, écart-type).

Collecteurs prévus (étape 8b, Mély) : coût, diversité, taux de faisabilité par opérateur, charge du solveur (D10).
"""

from abc import ABC, abstractmethod

from src.observability.events import Event, Record


class CollectorDefaults:
    """Paramètres par défaut des collecteurs."""

    # DiversityCollector : une mesure toutes les N générations (la diversité génotypique compare des génomes).
    DIVERSITY_EVERY_GENERATIONS: int = 1
    MIN_DIVERSITY_EVERY_GENERATIONS: int = 1


class RecordNames:
    """Types des enregistrements produits par les collecteurs (champ ``event`` de l'enregistrement)."""

    COST_STATISTICS: str = "cost_statistics"
    DIVERSITY: str = "diversity"
    FEASIBILITY_RATES: str = "feasibility_rates"
    SOLVER_EFFORT: str = "solver_effort"


class Scopes:
    """Portée des valeurs d'un enregistrement de ``FeasibilityRateCollector`` ou de ``SolverEffortCollector``."""

    # Valeurs de la seule génération qui vient de finir (enregistrement émis à GenerationEnded).
    GENERATION: str = "generation"
    # Valeurs de toute l'exécution (enregistrement émis à RunEnded).
    CUMULATIVE: str = "cumulative"


class RecordFields:
    """Champs communs aux enregistrements des collecteurs."""

    GENERATION: str = "generation"
    SCOPE: str = "scope"


class CostStatisticsFields:
    """Champs de ``RecordNames.COST_STATISTICS``."""

    SIZE: str = "size"
    FEASIBLE_COUNT: str = "feasible_count"
    TOTAL_MIN: str = "total_min"
    TOTAL_MEAN: str = "total_mean"
    TOTAL_MEDIAN: str = "total_median"
    TOTAL_MAX: str = "total_max"
    TOTAL_STDEV: str = "total_stdev"
    UNDER_COVERAGE_MEAN: str = "under_coverage_mean"
    OVER_COVERAGE_MEAN: str = "over_coverage_mean"
    COVERAGE_VIOLATIONS_MEAN: str = "coverage_violations_mean"
    QUASI_HARD_CELLS_MEAN: str = "quasi_hard_cells_mean"


class DiversityFields:
    """Champs de ``RecordNames.DIVERSITY``."""

    GENOTYPIC: str = "genotypic_diversity"
    PHENOTYPIC: str = "phenotypic_diversity"
    DISTINCT_COSTS: str = "distinct_costs"


class FeasibilityFields:
    """Champs de ``RecordNames.FEASIBILITY_RATES``."""

    ORIGIN: str = "origin"
    OPERATOR: str = "operator"
    COUNT: str = "count"
    FEASIBLE_BEFORE: str = "feasible_before"
    FEASIBLE_AFTER: str = "feasible_after"
    RATE_BEFORE: str = "rate_before"
    RATE_AFTER: str = "rate_after"


class SolverEffortFields:
    """Champs de ``RecordNames.SOLVER_EFFORT``."""

    CALLS: str = "calls"
    NODES: str = "nodes"
    FAILURES: str = "failures"
    PROPAGATIONS: str = "propagations"
    SOLVE_TIME_SECONDS: str = "solve_time_seconds"


class CollectorMessages:
    """Gabarits des messages d'erreur des collecteurs."""

    INVALID_DIVERSITY_EVERY: str = (
        "La diversité se mesure toutes les N générations, N au moins {minimum} ; trouvé {value}."
    )


class CollectorError(Exception):
    """Erreur de base des collecteurs."""


class InvalidCollectorParameterError(CollectorError):
    """Un paramètre de collecteur est hors de son domaine."""


# ---------------------------------------------------------------------------------------------------------------------
# Interface
# ---------------------------------------------------------------------------------------------------------------------

class MetricCollector(ABC):
    """Calcule des mesures à partir des événements du moteur."""

    @abstractmethod
    def on_event(self, event: Event) -> list[Record]:
        """Enregistrements produits en réponse à ``event`` ; liste vide si l'événement ne concerne pas ce collecteur.

        Ne consomme jamais le générateur aléatoire du moteur.
        """


# ---------------------------------------------------------------------------------------------------------------------
# Implémentations (à écrire, étape 8b)
# ---------------------------------------------------------------------------------------------------------------------

class CostStatisticsCollector(MetricCollector):
    """À chaque ``GenerationEnded`` : un enregistrement ``RecordNames.COST_STATISTICS`` ; rien pour les autres
    événements.

    Champs (``RecordFields``, ``CostStatisticsFields``) : ``generation`` ; ``size`` (taille de la population) ;
    ``feasible_count`` (individus dont ``cost.is_feasible``) ; ``total_min``, ``total_mean``, ``total_median``,
    ``total_max``, ``total_stdev`` de ``cost.total`` (écart-type de population, ``statistics.pstdev`` : 0 pour un
    seul individu) ; moyennes du coût décomposé : ``under_coverage_mean``, ``over_coverage_mean``,
    ``coverage_violations_mean``, ``quasi_hard_cells_mean``. Les moyennes et l'écart-type sont des ``float``."""

    def on_event(self, event: Event) -> list[Record]:
        raise NotImplementedError  # Étape 8b (Mély)


class DiversityCollector(MetricCollector):
    """À chaque ``GenerationEnded`` dont la génération est un multiple de ``every`` (la génération 0 comprise) :
    un enregistrement ``RecordNames.DIVERSITY`` ; rien pour les autres événements.

    Champs (``RecordFields``, ``DiversityFields``) : ``generation`` ;
        - ``genotypic_diversity`` : nombre de génomes distincts une fois les gènes triés (insensible à la
          permutation des employés), divisé par la taille de la population (``float`` dans ]0, 1]) ;
        - ``phenotypic_diversity`` : nombre de grilles « employé × période » distinctes
          (``Horaire.to_grid(period_count)``), divisé par la taille de la population ;
        - ``distinct_costs`` : nombre de valeurs distinctes de ``cost.total``."""

    def __init__(self, period_count: int, every: int = CollectorDefaults.DIVERSITY_EVERY_GENERATIONS) -> None:
        """
        Raises:
            InvalidCollectorParameterError: si ``every < CollectorDefaults.MIN_DIVERSITY_EVERY_GENERATIONS``.
        """
        if every < CollectorDefaults.MIN_DIVERSITY_EVERY_GENERATIONS:
            raise InvalidCollectorParameterError(CollectorMessages.INVALID_DIVERSITY_EVERY.format(
                minimum=CollectorDefaults.MIN_DIVERSITY_EVERY_GENERATIONS, value=every
            ))
        self.period_count = period_count
        self.every = every

    def on_event(self, event: Event) -> list[Record]:
        raise NotImplementedError  # Étape 8b (Mély)


class FeasibilityRateCollector(MetricCollector):
    """Taux de faisabilité (``cost.is_feasible``) avant et après le ``LocalSolver``, par groupe (origine, opérateur),
    à partir des ``LocalSearchDone`` (``cost_before``, ``cost_after``). C'est la mesure de la première expérience
    de l'étape 10.

    Un enregistrement ``RecordNames.FEASIBILITY_RATES`` par groupe vu :
        - à chaque ``GenerationEnded`` : ``scope`` = ``Scopes.GENERATION``, les appels de cette génération
          seulement ; ``generation`` = celle de l'événement ;
        - à ``RunEnded`` : ``scope`` = ``Scopes.CUMULATIVE``, tous les appels de l'exécution ;
          ``generation`` = ``RunEnded.generations``.
    Un groupe sans appel dans la portée ne produit pas d'enregistrement (pas de division par zéro).

    Champs (``RecordFields``, ``FeasibilityFields``) : ``generation``, ``scope``, ``origin``, ``operator`` (``None``
    pour l'initialisation et le restart), ``count`` (nombre d'appels), ``feasible_before``, ``feasible_after``
    (nombres de faisables), ``rate_before``, ``rate_after`` (``float`` dans [0, 1])."""

    def on_event(self, event: Event) -> list[Record]:
        raise NotImplementedError  # Étape 8b (Mély)


class SolverEffortCollector(MetricCollector):
    """Charge du solveur (D10), à partir de ``LocalSearchDone.result.statistics``.

    Un enregistrement ``RecordNames.SOLVER_EFFORT`` :
        - à chaque ``GenerationEnded`` : ``scope`` = ``Scopes.GENERATION``, les appels de cette génération
          seulement (``calls`` = 0 s'il n'y en a eu aucun) ;
        - à ``RunEnded`` : ``scope`` = ``Scopes.CUMULATIVE``, la charge cumulée de toute l'exécution ;
          ``generation`` = ``RunEnded.generations``.

    Champs (``RecordFields``, ``SolverEffortFields``) : ``generation``, ``scope``, ``calls`` ; ``nodes``,
    ``failures``, ``propagations`` : somme des valeurs rapportées (une statistique ``None`` n'est pas comptée ;
    ``None`` si aucun appel de la portée ne l'a rapportée) ; ``solve_time_seconds`` : somme des ``solve_time`` en
    secondes (``float``), même règle pour ``None``. ``solve_time`` n'est pas déterministe (D8) ; les trois autres
    le sont sous limite déterministe."""

    def on_event(self, event: Event) -> list[Record]:
        raise NotImplementedError  # Étape 8b (Mély)
