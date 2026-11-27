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
from collections import Counter
from dataclasses import dataclass
from statistics import mean, median, pstdev

from src.memetic.solver import SolverStatistics
from src.observability.events import (
    Event, 
    GenerationEnded,  
    LocalSearchDone,
    Record,
    RunEnded, 
    RunStarted,
    make_record,
)


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
    DETERMINISTIC_TIME: str = "deterministic_time"


class CollectorMessages:
    """Gabarits des messages d'erreur des collecteurs."""

    INVALID_DIVERSITY_EVERY: str = (
        "La diversité se mesure toutes les N générations, N au moins {minimum} ; trouvé {value}."
    )
    INVALID_POPULATION: str = (
        "La population doit être non vide et tous ses individus doivent être évalués."
    )

class CollectorError(Exception):
    """Erreur de base des collecteurs."""


class InvalidCollectorParameterError(CollectorError):
    """Un paramètre de collecteur est hors de son domaine."""

class InvalidPopulationError(CollectorError):
    """Une population est vide ou contient un individu non évalué."""

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
        # On calcule les statistiques seulement à la fin d'une génération.
        if not isinstance(event, GenerationEnded):
            return []

        population = event.population
        costs = [individu.cost for individu in population]

        # La population doit être non vide et évaluée.
        if not costs or any(cost is None for cost in costs):
            raise InvalidPopulationError(CollectorMessages.INVALID_POPULATION)

        totals = [int(cost.total) for cost in costs]

        record = make_record(
            RecordNames.COST_STATISTICS,
            **{
                RecordFields.GENERATION: int(event.generation),
                CostStatisticsFields.SIZE: len(population),
                CostStatisticsFields.FEASIBLE_COUNT: sum(
                    1 for cost in costs if cost.is_feasible
                ),
                CostStatisticsFields.TOTAL_MIN: min(totals),
                CostStatisticsFields.TOTAL_MEAN: float(mean(totals)),
                CostStatisticsFields.TOTAL_MEDIAN: float(median(totals)),
                CostStatisticsFields.TOTAL_MAX: max(totals),
                CostStatisticsFields.TOTAL_STDEV: float(pstdev(totals)),
                CostStatisticsFields.UNDER_COVERAGE_MEAN: float(
                    mean(cost.under_coverage_cost for cost in costs)
                ),
                CostStatisticsFields.OVER_COVERAGE_MEAN: float(
                    mean(cost.over_coverage_cost for cost in costs)
                ),
                CostStatisticsFields.COVERAGE_VIOLATIONS_MEAN: float(
                    mean(cost.coverage_violations for cost in costs)
                ),
                CostStatisticsFields.QUASI_HARD_CELLS_MEAN: float(
                    mean(cost.quasi_hard_cells for cost in costs)
                ),
            },
        )

        return [record]


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
        # On mesure la diversité uniquement à la fin des générations prévues.
        if not isinstance(event, GenerationEnded):
            return []

        if event.generation % self.every != 0:
            return []

        population = event.population
        if not population or any(individu.cost is None for individu in population):
            raise InvalidPopulationError(CollectorMessages.INVALID_POPULATION)

        # Diversité génotypique : l'ordre des employés ne compte pas.
        genotypes: set[frozenset[tuple[object, int]]] = {
            frozenset(Counter(individu.genome).items())
            for individu in population
}

        # Diversité phénotypique : comparaison des grilles employé × période.
        phenotypes: set[tuple[tuple[int, ...], ...]] = set()
        for individu in population:
            grid = individu.horaire.to_grid(self.period_count)
            canonical_grid = tuple(tuple(row) for row in grid.tolist())
            phenotypes.add(canonical_grid)

        # Nombre de coûts totaux distincts.
        distinct_costs = len({
            int(individu.cost.total)
            for individu in population
        })

        size = len(population)

        return [
            make_record(
                RecordNames.DIVERSITY,
                **{
                    RecordFields.GENERATION: int(event.generation),
                    DiversityFields.GENOTYPIC: float(len(genotypes) / size),
                    DiversityFields.PHENOTYPIC: float(len(phenotypes) / size),
                    DiversityFields.DISTINCT_COSTS: int(distinct_costs),
                },
            )
        ]

@dataclass
class _FeasibilityCounts:
    """Compteurs de faisabilité pour un groupe (origine, opérateur)."""
    count: int = 0
    feasible_before: int = 0
    feasible_after: int = 0

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
    def __init__(self) -> None:
        self._generation_stats: dict[tuple[str, str | None], _FeasibilityCounts] = {}
        self._cumulative_stats: dict[tuple[str, str | None], _FeasibilityCounts] = {}

    @staticmethod
    def _update(
        stats: dict[tuple[str, str | None], _FeasibilityCounts],
        event: LocalSearchDone,
    ) -> None:
        key = (event.origin, event.operator)

        if key not in stats:
            stats[key] = _FeasibilityCounts()

        stats[key].count += 1
        stats[key].feasible_before += int(event.cost_before.is_feasible)
        stats[key].feasible_after += int(event.cost_after.is_feasible)

    @staticmethod
    def _make_records(
        stats: dict[tuple[str, str | None], _FeasibilityCounts],
        generation: int,
        scope: str,
    ) -> list[Record]:
        records: list[Record] = []

        for (origin, operator), counts in stats.items():
            records.append(
                make_record(
                    RecordNames.FEASIBILITY_RATES,
                    **{
                        RecordFields.GENERATION: int(generation),
                        RecordFields.SCOPE: scope,
                        FeasibilityFields.ORIGIN: origin,
                        FeasibilityFields.OPERATOR: operator,
                        FeasibilityFields.COUNT: counts.count,
                        FeasibilityFields.FEASIBLE_BEFORE: counts.feasible_before,
                        FeasibilityFields.FEASIBLE_AFTER: counts.feasible_after,
                        FeasibilityFields.RATE_BEFORE: float(
                            counts.feasible_before / counts.count
                        ),
                        FeasibilityFields.RATE_AFTER: float(
                            counts.feasible_after / counts.count
                        ),
                    },
                )
            )

        return records


    def on_event(self, event: Event) -> list[Record]:
        if isinstance(event, RunStarted):
            self._generation_stats.clear()
            self._cumulative_stats.clear()
            return []
        if isinstance(event, LocalSearchDone):
            self._update(self._generation_stats, event)
            self._update(self._cumulative_stats, event)
            return []

        if isinstance(event, GenerationEnded):
            records = self._make_records(
                self._generation_stats,
                event.generation,
                Scopes.GENERATION,
            )
            self._generation_stats.clear()
            return records

        if isinstance(event, RunEnded):
            return self._make_records(
                self._cumulative_stats,
                event.generations,
                Scopes.CUMULATIVE,
            )

        return []


@dataclass
class _SolverEffortCounts:
    """Statistiques cumulées des appels au solveur."""

    calls: int = 0
    nodes: int | None = None
    failures: int | None = None
    propagations: int | None = None
    solve_time_seconds: float | None = None
    deterministic_time: float | None = None

    def add(self, statistics: SolverStatistics) -> None:
        """Additionne les statistiques rapportées par un appel."""
        self.calls += 1

        if statistics.nodes is not None:
            self.nodes = (self.nodes or 0) + statistics.nodes

        if statistics.failures is not None:
            self.failures = (self.failures or 0) + statistics.failures

        if statistics.propagations is not None:
            self.propagations = (
                (self.propagations or 0) + statistics.propagations
            )

        if statistics.solve_time is not None:
            seconds = statistics.solve_time.total_seconds()
            self.solve_time_seconds = (
                (self.solve_time_seconds or 0.0) + seconds
            )

        if statistics.deterministic_time is not None:
            self.deterministic_time = (self.deterministic_time or 0.0) + statistics.deterministic_time


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
    secondes (``float``), même règle pour ``None`` ; ``deterministic_time`` : somme des temps déterministes consommés
    (étape 10d, unités de ``DeterministicTimeLimit``), même règle. ``solve_time`` n'est pas déterministe (D8) ; les
    autres le sont sous limite déterministe."""

    def __init__(self) -> None:
        self._generation_stats: _SolverEffortCounts = _SolverEffortCounts()
        self._cumulative_stats: _SolverEffortCounts = _SolverEffortCounts()

    @staticmethod
    def _make_record(
        statistics: _SolverEffortCounts,
        generation: int,
        scope: str,
    ) -> Record:
        return make_record(
            RecordNames.SOLVER_EFFORT,
            **{
                RecordFields.GENERATION: generation,
                RecordFields.SCOPE: scope,
                SolverEffortFields.CALLS: statistics.calls,
                SolverEffortFields.NODES: statistics.nodes,
                SolverEffortFields.FAILURES: statistics.failures,
                SolverEffortFields.PROPAGATIONS: statistics.propagations,
                SolverEffortFields.SOLVE_TIME_SECONDS: statistics.solve_time_seconds,
                SolverEffortFields.DETERMINISTIC_TIME: statistics.deterministic_time,
            },
        )

    def on_event(self, event: Event) -> list[Record]:
        if isinstance(event, RunStarted):
            self._generation_stats = _SolverEffortCounts()
            self._cumulative_stats = _SolverEffortCounts()
            return []
        if isinstance(event, LocalSearchDone):
            statistics = event.result.statistics

            self._generation_stats.add(statistics)
            self._cumulative_stats.add(statistics)
            return []

        if isinstance(event, GenerationEnded):
            record = self._make_record(
                self._generation_stats,
                event.generation,
                Scopes.GENERATION,
            )

            self._generation_stats = _SolverEffortCounts()
            return [record]

        if isinstance(event, RunEnded):
            return [
                self._make_record(
                    self._cumulative_stats,
                    event.generations,
                    Scopes.CUMULATIVE,
                )
            ]

        return []
