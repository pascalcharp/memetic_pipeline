"""Outils de test partagés (pas un test) : individus aux coûts choisis, génomes faisables, faux LocalSolver.

À utiliser dans les tests des étapes 5b, 6, 7a et 7b pour tester la logique Python sans lancer MiniZinc.
L'instance synthétique et le quart de référence viennent de ``tests/test_feasibility.py`` :
plage utile 4..43, 2 activités ; quart de référence (10, 14, 19, 28, 37), durées de blocs 4, 4, 5, 9.
"""

import random

from src.ga.chromosome import BlockEncoding, BlockGene, BlockGenome
from src.ga.individual import Individu
from src.memetic.local_search import LocalSearchResult, LocalSolver
from src.memetic.solver import SolveOutcome, SolverStatistics
from src.model.evaluation import CostBreakdown
from src.model.horaire import Horaire
from tests.test_feasibility import REFERENCE_SHIFT, single, synthetic_instance

__all__ = [
    "REFERENCE_GENE",
    "FakeLocalSolver",
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
