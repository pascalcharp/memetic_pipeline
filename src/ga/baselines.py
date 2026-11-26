"""Opérateurs témoins (étape 10d) : une « variation » qui ignore ses entrées et rend des génomes aléatoires neufs.

Branchés dans le moteur mémétique à la place du croisement et de la mutation, ils en font le témoin « redémarrages
aléatoires » : à chaque génération, 2·NR + NM génomes aléatoires passent par le même LocalSolver, sont évalués et
sélectionnés comme dans le mémétique. Le budget d'appels au solveur, la mesure et le journal sont donc identiques ; seul
l'apport de la variation (hériter des parents) disparaît. Ils se choisissent dans une configuration d'expérience par
le nom ``random_genome`` (catalogue, ``src/memetic/catalog.py``).
"""

import random
from collections.abc import Sequence

from src.ga.chromosome import BlockEncoding, BlockGenome, Encoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.operators import Crossover, Mutation, OperatorDefaults, OperatorMessages, WrongParentCountError


class RandomGenomeCrossover(Crossover[BlockGenome]):
    """« Croisement » témoin : rend deux génomes aléatoires neufs, tirés par ``generator``, sans regarder les parents.

    Garde l'interface d'un croisement à deux parents, pour que le moteur fasse exactement le même nombre d'appels au
    LocalSolver qu'avec un vrai croisement.
    """

    def __init__(self, generator: RandomBlockInitializer) -> None:
        self.generator = generator

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def parent_count(self) -> int:
        return OperatorDefaults.CROSSOVER_PARENT_COUNT

    def recombine(self, parents: Sequence[BlockGenome], rng: random.Random) -> tuple[BlockGenome, ...]:
        """Deux génomes aléatoires ; ``parents`` ne sert qu'à vérifier leur nombre.

        Raises:
            WrongParentCountError: si ``parents`` ne contient pas exactement ``parent_count()`` génomes.
        """
        if len(parents) != self.parent_count():
            raise WrongParentCountError(OperatorMessages.WRONG_PARENT_COUNT.format(
                operator=type(self).__name__, expected=self.parent_count(), found=len(parents)
            ))
        return tuple(self.generator.random_genome(rng) for _ in range(self.parent_count()))


class RandomGenomeMutation(Mutation[BlockGenome]):
    """« Mutation » témoin : rend un génome aléatoire neuf, tiré par ``generator``, sans regarder le génome reçu."""

    def __init__(self, generator: RandomBlockInitializer) -> None:
        self.generator = generator

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        return self.generator.random_genome(rng)
