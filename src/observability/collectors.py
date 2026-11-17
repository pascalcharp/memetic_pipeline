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
    """À chaque ``GenerationEnded`` : un enregistrement ``RecordNames.COST_STATISTICS`` avec la génération,
    les statistiques de ``cost.total`` (min, moyenne, médiane, max, écart-type) et le coût décomposé de la
    population (sous-couverture, sur-couverture, violations « au moins 1 », cellules quasi dures)."""

    def on_event(self, event: Event) -> list[Record]:
        raise NotImplementedError  # Étape 8b (Mély)


class DiversityCollector(MetricCollector):
    """Toutes les ``every`` générations (``GenerationEnded``) : un enregistrement ``RecordNames.DIVERSITY`` avec
    la diversité génotypique insensible à la permutation des employés (par exemple la proportion de génomes
    distincts une fois les gènes triés), phénotypique (proportion de grilles « employé × période » distinctes,
    ``Horaire.to_grid(period_count)``) et des coûts (nombre de ``cost.total`` distincts)."""

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
    """Taux de faisabilité (``cost.is_feasible``) des nouveaux individus, par origine et par opérateur, avant et
    après le ``LocalSolver`` (``LocalSearchDone.cost_before`` et ``cost_after``). Un enregistrement
    ``RecordNames.FEASIBILITY_RATES`` à chaque ``GenerationEnded`` (taux de la génération) et à ``RunEnded``
    (taux cumulés). C'est la mesure de la première expérience de l'étape 10."""

    def on_event(self, event: Event) -> list[Record]:
        raise NotImplementedError  # Étape 8b (Mély)


class SolverEffortCollector(MetricCollector):
    """Charge cumulée du solveur (D10) : somme des statistiques de ``LocalSearchDone.result.statistics``
    (``nodes``, ``failures``, ``propagations`` ; ``solve_time``, non déterministe, à part) et nombre d'appels.
    Un enregistrement ``RecordNames.SOLVER_EFFORT`` à chaque ``GenerationEnded`` et à ``RunEnded``."""

    def on_event(self, event: Event) -> list[Record]:
        raise NotImplementedError  # Étape 8b (Mély)
