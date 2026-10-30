"""Individu de l'algorithme mémétique : un génome, son phénotype décodé et, une fois évalué, son coût."""

import dataclasses
from dataclasses import dataclass

from src.ga.chromosome import Encoding
from src.model.horaire import Horaire


@dataclass(frozen=True)
class Individu[G]:
    """Individu immuable (D7) : génome, horaire décodé une seule fois à la construction, coût optionnel.

    Construire un individu par ``from_genome``, qui garantit que ``horaire`` est bien le décodage de
    ``genome``. Les opérateurs ne modifient jamais un individu : ils en retournent un nouveau.

    ``cost`` vaut ``None`` tant que l'individu n'a pas été évalué. Son type deviendra probablement
    une décomposition du coût (``CostBreakdown``, D8) à l'étape 4.
    """

    genome: G
    horaire: Horaire
    cost: int | None = None

    @classmethod
    def from_genome(cls, genome: G, encoding: Encoding[G]) -> "Individu[G]":
        """Individu non évalué, dont l'horaire est le décodage de ``genome`` par ``encoding``."""
        return cls(genome=genome, horaire=encoding.decode(genome))

    def is_evaluated(self) -> bool:
        return self.cost is not None

    def with_cost(self, cost: int) -> "Individu[G]":
        """Copie de cet individu avec le coût ``cost`` ; l'individu d'origine n'est pas modifié."""
        return dataclasses.replace(self, cost=cost)
