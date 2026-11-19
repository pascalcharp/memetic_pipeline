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
from statistics import mean, median, pstdev
from src.observability.events import (Event, GenerationEnded, Record, make_record, LocalSearchDone, RunEnded)
from src.ga.chromosome import BlockGene

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
        # On calcule les statistiques seulement à la fin d'une génération.
        if not isinstance(event, GenerationEnded):
            return []

        population = event.population
        costs = [individu.cost for individu in population]

        # La population doit être non vide et évaluée.
        if not costs or any(cost is None for cost in costs):
            raise ValueError("La population doit être non vide et évaluée.")

        totals = [float(cost.total) for cost in costs]

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

        return [record] # Étape 8b (Mély)


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
        if not population:
            return []

        # Représentation canonique d'un gène, comparable et triable.
        def gene_key(gene: BlockGene) -> tuple:
            return (
                int(gene.start),
                tuple(
                    (int(block.activity), int(block.duration))
                    for block in gene.blocks
                ),
            )

        # Diversité génotypique : l'ordre des employés ne compte pas.
        genotypes = set()
        for individu in population:
            canonical_genome = tuple(
                sorted(gene_key(gene) for gene in individu.genome)
            )
            genotypes.add(canonical_genome)

        # Diversité phénotypique : comparaison des grilles employé × période.
        phenotypes = set()
        for individu in population:
            grid = individu.horaire.to_grid(self.period_count)
            canonical_grid = tuple(
                tuple(int(value) for value in row)
                for row in grid
            )
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
        ] # Étape 8b (Mély)


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
        # Statistiques par génération et pour toute l'exécution.
        self._generation_stats = {}
        self._cumulative_stats = {}

    @staticmethod
    def _update(stats, event: LocalSearchDone) -> None:
        key = (event.origin, event.operator)

        if key not in stats:
            stats[key] = [0, 0, 0]

        stats[key][0] += 1
        stats[key][1] += int(event.cost_before.is_feasible)
        stats[key][2] += int(event.cost_after.is_feasible)

    @staticmethod
    def _make_records(stats, generation: int, scope: str) -> list[Record]:
        records = []

        for (origin, operator), (count, before, after) in stats.items():
            records.append(
                make_record(
                    RecordNames.FEASIBILITY_RATES,
                    **{
                        RecordFields.GENERATION: int(generation),
                        RecordFields.SCOPE: scope,
                        FeasibilityFields.ORIGIN: origin,
                        FeasibilityFields.OPERATOR: operator,
                        FeasibilityFields.COUNT: int(count),
                        FeasibilityFields.FEASIBLE_BEFORE: int(before),
                        FeasibilityFields.FEASIBLE_AFTER: int(after),
                        FeasibilityFields.RATE_BEFORE: float(before / count),
                        FeasibilityFields.RATE_AFTER: float(after / count),
                    },
                )
            )

        return records

    def on_event(self, event: Event) -> list[Record]:
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

        return [] # Étape 8b (Mély)


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

    def __init__(self) -> None:
        # Statistiques de la génération et de toute l'exécution.
        self._generation_stats = []
        self._cumulative_stats = []

    @staticmethod
    def _make_record(statistics, generation: int, scope: str) -> Record:
        # Additionne une statistique, en ignorant les valeurs None.
        # Si aucune valeur n'est rapportée, le résultat reste None.
        def total(attribute: str):
            values = [
                getattr(stat, attribute)
                for stat in statistics
                if getattr(stat, attribute) is not None
            ]
            return int(sum(values)) if values else None

        # Le temps est un timedelta : conversion en secondes.
        times = [
            stat.solve_time.total_seconds()
            for stat in statistics
            if stat.solve_time is not None
        ]

        return make_record(
            RecordNames.SOLVER_EFFORT,
            **{
                RecordFields.GENERATION: int(generation),
                RecordFields.SCOPE: scope,
                SolverEffortFields.CALLS: int(len(statistics)),
                SolverEffortFields.NODES: total("nodes"),
                SolverEffortFields.FAILURES: total("failures"),
                SolverEffortFields.PROPAGATIONS: total("propagations"),
                SolverEffortFields.SOLVE_TIME_SECONDS: (
                    float(sum(times)) if times else None
                ),
            },
        )

    def on_event(self, event: Event) -> list[Record]:
        if isinstance(event, LocalSearchDone):
            self._generation_stats.append(event.result.statistics)
            self._cumulative_stats.append(event.result.statistics)
            return []

        if isinstance(event, GenerationEnded):
            record = self._make_record(
                self._generation_stats,
                event.generation,
                Scopes.GENERATION,
            )
            self._generation_stats.clear()
            return [record]

        if isinstance(event, RunEnded):
            return [
                self._make_record(
                    self._cumulative_stats,
                    event.generations,
                    Scopes.CUMULATIVE,
                )
            ]

        return [] # Étape 8b (Mély)
