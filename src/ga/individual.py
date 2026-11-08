"""Individu de l'algorithme mémétique : un génome, son phénotype décodé et, une fois évalué, son coût."""

import dataclasses
from dataclasses import dataclass

from src.ga.chromosome import Encoding
from src.model.evaluation import CostBreakdown
from src.model.horaire import Horaire


@dataclass(frozen=True)
class Individu[G]:
    """Individu immuable (D7) : génome, horaire décodé une seule fois à la construction, coût optionnel.

    Construire un individu par ``from_genome``, qui garantit que ``horaire`` est bien le décodage de
    ``genome``. Les opérateurs ne modifient jamais un individu : ils en retournent un nouveau.

    ``cost`` vaut ``None`` tant que l'individu n'a pas été évalué. C'est une décomposition du coût (D8) ;
    le coût à minimiser est ``cost.total``.
    """

    genome: G
    horaire: Horaire
    cost: CostBreakdown | None = None

    @classmethod
    def from_genome(cls, genome: G, encoding: Encoding[G]) -> "Individu[G]":
        """Individu non évalué, dont l'horaire est le décodage de ``genome`` par ``encoding``."""
        return cls(genome=genome, horaire=encoding.decode(genome))

    def is_evaluated(self) -> bool:
        return self.cost is not None

    def with_cost(self, cost: CostBreakdown) -> "Individu[G]":
        """Copie de cet individu avec le coût ``cost`` ; l'individu d'origine n'est pas modifié."""
        return dataclasses.replace(self, cost=cost)
