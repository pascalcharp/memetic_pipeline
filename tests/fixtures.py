"""Outils de test partagés (pas un test) : individus aux coûts choisis, génomes faisables, faux objets.

À utiliser dans les tests des étapes 5b à 9 pour tester la logique Python sans lancer MiniZinc. Les faux objets
du moteur (``FakeCrossover``, ``FakeMutation``, ``FakeSurvivorSelector``, ``FakeConvergenceCriterion``,
``FakeRestartPolicy``, ``RecordingCollector``) permettent de tester l'étape 9 avant la fusion de 8 et 8b.
L'instance synthétique et le quart de référence viennent de ``tests/test_feasibility.py`` :
plage utile 4..43, 2 activités ; quart de référence (10, 14, 19, 28, 37), durées de blocs 4, 4, 5, 9.
"""

import random
from collections.abc import Sequence

from src.ga.chromosome import BlockEncoding, BlockGene, BlockGenome, Encoding
from src.ga.individual import Individu
from src.ga.operators import Crossover, Mutation
from src.ga.population import ConvergenceCriterion, RestartPolicy, SurvivorSelector
from src.memetic.local_search import LocalSearchResult, LocalSolver
from src.memetic.solver import SolveOutcome, SolverStatistics
from src.model.evaluation import CostBreakdown
from src.model.horaire import Horaire
from src.observability.collectors import MetricCollector
from src.observability.events import Event, Record
from tests.test_feasibility import REFERENCE_SHIFT, single, synthetic_instance

__all__ = [
    "REFERENCE_GENE",
    "FakeConvergenceCriterion",
    "FakeCrossover",
    "FakeLocalSolver",
    "FakeMutation",
    "FakeRestartPolicy",
    "FakeSurvivorSelector",
    "RecordingCollector",
    "cost_with_total",
    "evaluated_individual",
    "reference_genome",
    "synthetic_instance",
]

# Gène du quart de référence : début 10, blocs (activité, durée) = (1, 4), (2, 4), (1, 5), (2, 9).
REFERENCE_GENE: BlockGene = BlockEncoding().encode_shift(REFERENCE_SHIFT)


def reference_genome(employee_count: int = 1) -> BlockGenome:
    """Génome faisable sur l'instance synthétique : ``employee_count`` copies du gène de référence."""
    return tuple(REFERENCE_GENE for _ in range(employee_count))


def cost_with_total(total: int) -> CostBreakdown:
    """Coût faisable dont le total vaut ``total`` (entièrement en sur-couverture)."""
    return CostBreakdown(
        under_coverage_cost=0,
        over_coverage_cost=total,
        quasi_hard_cells=0,
        coverage_violations=0,
        structural_violations=0,
        penalty_cost=0,
    )


def evaluated_individual[G](genome: G, total: int) -> Individu[G]:
    """Individu évalué de coût ``total``, construit sans décodage : pour les tests de sélection.

    L'horaire est celui de référence, quel que soit ``genome`` : les sélecteurs ne regardent que le coût.
    Le génome sert d'étiquette pour reconnaître l'individu tiré (par exemple un entier ou une chaîne).
    """
    return Individu(genome=genome, horaire=single(REFERENCE_SHIFT), cost=cost_with_total(total))


class FakeLocalSolver(LocalSolver):
    """Faux ``LocalSolver`` : rend l'horaire reçu (ou ``replacement`` s'il est donné) et note chaque appel."""

    def __init__(self, replacement: Horaire | None = None) -> None:
        self.replacement = replacement
        self.received: list[Horaire] = []

    def improve(self, horaire: Horaire, rng: random.Random) -> LocalSearchResult:
        self.received.append(horaire)
        result_horaire = horaire if self.replacement is None else self.replacement
        return LocalSearchResult(
            horaire=result_horaire,
            outcome=SolveOutcome.FEASIBLE,
            freed_employees=frozenset(),
            statistics=SolverStatistics(),
        )


class FakeCrossover(Crossover[BlockGenome]):
    """Faux croisement pour ``BlockEncoding`` : rend deux enfants identiques aux deux parents et note chaque appel."""

    PARENT_COUNT: int = 2

    def __init__(self) -> None:
        self.received: list[tuple[BlockGenome, ...]] = []

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def parent_count(self) -> int:
        return self.PARENT_COUNT

    def recombine(self, parents: Sequence[BlockGenome], rng: random.Random) -> tuple[BlockGenome, ...]:
        self.received.append(tuple(parents))
        return tuple(parents)


class FakeMutation(Mutation[BlockGenome]):
    """Fausse mutation pour ``BlockEncoding`` : rend le génome inchangé et note chaque appel."""

    def __init__(self) -> None:
        self.received: list[BlockGenome] = []

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        self.received.append(genome)
        return genome


class FakeSurvivorSelector[G](SurvivorSelector[G]):
    """Faux ``SelectPop`` : les ``size`` meilleurs selon ``cost.total`` (tri stable), doublons compris."""

    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        ranked = sorted(population, key=lambda individual: individual.cost.total)
        return tuple(ranked[:size])


class FakeConvergenceCriterion[G](ConvergenceCriterion[G]):
    """Faux critère de convergence : converge aux appels dont le numéro (à partir de 1) est dans ``converge_at``.

    Note les appels à ``has_converged`` et à ``reset``.
    """

    def __init__(self, converge_at: frozenset[int] = frozenset()) -> None:
        self.converge_at = converge_at
        self.calls = 0
        self.reset_count = 0

    def has_converged(self, population: Sequence[Individu[G]]) -> bool:
        self.calls += 1
        return self.calls in self.converge_at

    def reset(self) -> None:
        self.reset_count += 1


class FakeRestartPolicy[G](RestartPolicy[G]):
    """Faux restart : rend la population inchangée et note chaque appel."""

    def __init__(self) -> None:
        self.received: list[tuple[Individu[G], ...]] = []

    def restart(self, population: Sequence[Individu[G]], rng: random.Random) -> tuple[Individu[G], ...]:
        self.received.append(tuple(population))
        return tuple(population)


class RecordingCollector(MetricCollector):
    """Faux collecteur : garde chaque événement reçu, dans l'ordre, et ne produit aucun enregistrement."""

    def __init__(self) -> None:
        self.events: list[Event] = []

    def on_event(self, event: Event) -> list[Record]:
        self.events.append(event)
        return []
