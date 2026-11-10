"""Opérateurs de variation : ``Recombine`` et ``Mute`` du pseudo-code (décisions D5 et D7).

Un opérateur de variation est lié à un encodage (D5) : il manipule des **génomes** de type ``G``, jamais des
individus. Le moteur construit ensuite les individus (``Individu.from_genome``) et les évalue. La compatibilité
entre un opérateur et l'encodage choisi est vérifiée à l'assemblage (``OperatorRegistry``, ``src/ga/registry.py``).

Les opérateurs ne modifient jamais leurs entrées : ils rendent de nouveaux génomes (D7). Le seul aléa provient
du ``random.Random`` passé à chaque appel : même état ⇒ même résultat.

Opérateurs pour l'encodage par blocs (D1) ; un gène est le quart complet d'un employé :
    - ``UniformGeneCrossover`` : échange de gènes entiers entre deux parents ;
    - ``ShiftStartMutation`` : décale un quart entier ;
    - ``BlockBoundaryMutation`` : déplace la frontière entre deux blocs voisins (Σd conservée) ;
    - ``ActivityMutation`` : change l'activité d'un bloc.
Un opérateur peut produire un génome infaisable (D6) ; la première expérience de l'étape 10 mesurera le taux
de faisabilité des enfants par opérateur.
"""

import random
from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.ga.chromosome import BlockEncoding, BlockGenome, Encoding
from src.utils.io import ProblemInstance


class OperatorDefaults:
    """Paramètres par défaut des opérateurs de variation."""

    # Les croisements de ce module prennent deux parents.
    CROSSOVER_PARENT_COUNT: int = 2


class OperatorMessages:
    """Gabarits des messages d'erreur des opérateurs de variation."""

    WRONG_PARENT_COUNT: str = "Le croisement {operator} attend {expected} parents ; reçu {found}."
    PARENT_LENGTH_MISMATCH: str = "Les parents du croisement {operator} n'ont pas le même nombre de gènes : {lengths}."


class OperatorError(Exception):
    """Erreur de base des opérateurs de variation (pas pour un génome qui décode en horaire infaisable)."""


class WrongParentCountError(OperatorError):
    """Le croisement n'a pas reçu le nombre de parents attendu."""


class ParentLengthMismatchError(OperatorError):
    """Les parents d'un croisement n'ont pas le même nombre de gènes."""


class VariationOperator[G](ABC):
    """Base des opérateurs de variation : déclare l'encodage avec lequel l'opérateur est compatible (D5)."""

    @classmethod
    @abstractmethod
    def encoding_type(cls) -> type[Encoding[G]]:
        """Type d'encodage dont cet opérateur manipule les génomes."""

    @classmethod
    def is_compatible_with(cls, encoding: Encoding) -> bool:
        """Vrai si ``encoding`` est une instance du type d'encodage de cet opérateur."""
        return isinstance(encoding, cls.encoding_type())


class Crossover[G](VariationOperator[G]):
    """``Recombine`` : produit des enfants à partir de parents."""

    @abstractmethod
    def parent_count(self) -> int:
        """Nombre de parents attendus par ``recombine``."""

    @abstractmethod
    def recombine(self, parents: Sequence[G], rng: random.Random) -> tuple[G, ...]:
        """Enfants de ``parents`` ; les parents ne sont pas modifiés.

        Raises:
            WrongParentCountError: si ``len(parents) != parent_count()``.
        """


class Mutation[G](VariationOperator[G]):
    """``Mute`` : modifie un génome."""

    @abstractmethod
    def mutate(self, genome: G, rng: random.Random) -> G:
        """Nouveau génome muté ; ``genome`` n'est pas modifié."""


# ---------------------------------------------------------------------------------------------------------------------
# Opérateurs pour BlockEncoding (à écrire, étape 7b)
# ---------------------------------------------------------------------------------------------------------------------

class UniformGeneCrossover(Crossover[BlockGenome]):
    """Croisement uniforme de gènes entiers : pour chaque employé, chaque enfant reçoit le gène de l'un des
    deux parents. Un quart faisable reste faisable : seule la couverture change.

    Rend deux enfants complémentaires.

    Raises (``recombine``):
        WrongParentCountError: si le nombre de parents n'est pas 2.
        ParentLengthMismatchError: si les parents n'ont pas le même nombre de gènes.
    """

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def parent_count(self) -> int:
        return OperatorDefaults.CROSSOVER_PARENT_COUNT

    def recombine(self, parents: Sequence[BlockGenome], rng: random.Random) -> tuple[BlockGenome, ...]:
        raise NotImplementedError  # Étape 7b (Xavier)


class ShiftStartMutation(Mutation[BlockGenome]):
    """Décale le quart entier d'un employé tiré au hasard, en gardant le quart dans la plage utile de l'instance."""

    def __init__(self, instance: ProblemInstance) -> None:
        self.instance = instance

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        raise NotImplementedError  # Étape 7b (Xavier)


class BlockBoundaryMutation(Mutation[BlockGenome]):
    """Déplace la frontière entre deux blocs voisins d'un employé tiré au hasard : une durée augmente, l'autre
    diminue d'autant. Σd est conservée ; chaque durée reste au moins ``ShiftStructure.MIN_ACTIVITY_DURATION``.
    """

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        raise NotImplementedError  # Étape 7b (Xavier)


class ActivityMutation(Mutation[BlockGenome]):
    """Change l'activité d'un bloc tiré au hasard, pour une autre activité de 1..``instance.activity_count``.

    Cas limite : une instance à une seule activité (bench_1) n'offre aucune autre activité ; le génome est
    alors rendu inchangé.
    """

    def __init__(self, instance: ProblemInstance) -> None:
        self.instance = instance

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        raise NotImplementedError  # Étape 7b (Xavier)
