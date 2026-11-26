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
Opérateurs témoins (étape 10d) : ils ignorent leurs entrées et rendent des génomes tirés au hasard, comme à
l'initialisation, pour mesurer ce que les vrais opérateurs apportent :
    - ``RandomGenomeCrossover`` : deux génomes aléatoires, quels que soient les parents ;
    - ``RandomGenomeMutation`` : un génome aléatoire, quel que soit le génome reçu.
Un opérateur peut produire un génome infaisable (D6) ; la première expérience de l'étape 10 mesurera le taux
de faisabilité des enfants par opérateur.
"""

import random
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Generator, Literal

from src.ga.chromosome import ActivityBlock, BlockEncoding, BlockGene, BlockGenome, Encoding
from src.ga.initialization import RandomBlockInitializer
from src.model.shift_rules import ModelIndexing, ShiftStructure
from src.utils.io import ProblemInstance


class OperatorDefaults:
    """Paramètres par défaut des opérateurs de variation."""

    # Les croisements de ce module prennent deux parents.
    CROSSOVER_PARENT_COUNT: int = 2

    # RandomGenomeCrossover rend autant d'enfants que UniformGeneCrossover : le témoin de l'étape 10d soumet ainsi
    # au solveur le même nombre d'individus par génération (2 × NR) que le mémétique.
    RANDOM_CROSSOVER_CHILD_COUNT: int = 2

    # BlockBoundaryMutation : nombre de périodes déplacées d'un bloc à l'autre, tiré dans cet intervalle (bornes
    # incluses). Une petite amplitude garde la mutation locale (voir TODO.md, 7b, pour une amplitude calculée).
    MIN_BOUNDARY_TRANSFER: int = 1
    MAX_BOUNDARY_TRANSFER: int = 3

    # ShiftStartMutation : amplitude du décalage du début, en périodes, tirée dans cet intervalle (bornes incluses),
    # puis appliquée dans l'une des deux directions (vers le plus tôt, vers le plus tard). Jamais nulle.
    MIN_SHIFT_AMPLITUDE: int = 1
    MAX_SHIFT_AMPLITUDE: int = 3
    SHIFT_DIRECTIONS: tuple[int, int] = (-1, 1)

    # ActivityMutation : il faut au moins deux activités pour qu'un bloc puisse en changer.
    MIN_ACTIVITY_COUNT_TO_MUTATE: int = 2


class OperatorMessages:
    """Gabarits des messages d'erreur des opérateurs de variation."""

    WRONG_PARENT_COUNT: str = "Le croisement {operator} attend {expected} parents ; reçu {found}."
    PARENT_LENGTH_MISMATCH: str = "Les parents du croisement {operator} n'ont pas le même nombre de gènes : {lengths}."
    EMPTY_GENOME: str = "La mutation {operator} a reçu un génome sans aucun gène."
    GENE_CANNOT_GIVE: str = "Aucun bloc du gène ne peut céder {transfer} périodes à un voisin sans descendre sous {minimum}."


class OperatorError(Exception):
    """Erreur de base des opérateurs de variation (pas pour un génome qui décode en horaire infaisable)."""


class WrongParentCountError(OperatorError):
    """Le croisement n'a pas reçu le nombre de parents attendu."""


class ParentLengthMismatchError(OperatorError):
    """Les parents d'un croisement n'ont pas le même nombre de gènes."""

class EmptyGenomeError(OperatorError):
    """La mutation a reçu un génome sans aucun gène : c'est une erreur d'appel, pas un cas de l'exécution."""

class GeneCannotMutateBoundaryError(OperatorError):
    """Le gène n'a aucun bloc valide permettant une mutation qui respecte Σd."""


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
        def _create_mask(length: int) -> Generator[tuple[int, Literal[0] | Literal[1]]]:
            """
            Generator function to create a mask to be used to create children

            From *Uniform Crossover in genetic Algorithms* Syswerda 1989
            The generated mask is constituted of 0 and 1,
            where 0 means using its parent, and 1 using the other parent.
            Child 1 uses parent 1, and child 2 uses parent 2.

            Example:
                Parent 1:   1, 0, 1
                Parent 2:   0, 1, 1
                Mask:       1, 1, 0
                Children 1: 0, 1, 1
                Children 2: 1, 1, 1
            """
            zero: Literal[0] = 0
            one: Literal[1] = 1
            for i in range(length):
                yield i, rng.choice([zero, one])

        progenitor_1, progenitor_2 = self._valid_parent(parents)
        mask_length = len(progenitor_1)

        child_1 = list(progenitor_1)
        child_2 = list(progenitor_2)

        for i, mask in _create_mask(mask_length):
            if mask:
                child_1[i] = progenitor_2[i]
                child_2[i] = progenitor_1[i]

        return tuple(child_1), tuple(child_2)

    def _valid_parent(self, parents: Sequence[BlockGenome]) -> tuple[BlockGenome, BlockGenome]:
        """
        Validates the parents: their number and their lengths.
        """
        if not len(parents) == self.parent_count():
            raise WrongParentCountError(OperatorMessages.WRONG_PARENT_COUNT.format(
                operator=type(self).__name__, expected=self.parent_count(), found=len(parents)
            ))

        progenitors = (parents[0], parents[1])

        if not len(progenitors[0]) == len(parents[1]):
            raise ParentLengthMismatchError(OperatorMessages.PARENT_LENGTH_MISMATCH.format(
                operator=type(self).__name__, lengths=[len(parent) for parent in progenitors]
            ))

        return progenitors



class ShiftStartMutation(Mutation[BlockGenome]):
    """Décale le quart entier d'un employé tiré au hasard, en gardant le quart dans la plage utile de l'instance."""

    def __init__(self, instance: ProblemInstance) -> None:
        self.instance = instance

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        if len(genome) == 0:
            raise EmptyGenomeError(OperatorMessages.EMPTY_GENOME.format(operator=type(self).__name__))
        return self._mutate_by(
            index=rng.randrange(len(genome)),
            amount=rng.choice(OperatorDefaults.SHIFT_DIRECTIONS)
                   * rng.randint(OperatorDefaults.MIN_SHIFT_AMPLITUDE, OperatorDefaults.MAX_SHIFT_AMPLITUDE),
            genome=genome
        )

    def _mutate_by(self, index: int, amount: int, genome: BlockGenome) -> BlockGenome:
        mutated = list(genome)
        start = self._clamp(mutated[index], amount)
        mutated[index] = BlockGene(start, mutated[index].blocks)
        return tuple(mutated)

    def _clamp(self, gene: BlockGene, value: int):
        windows = self.instance.windows
        debut_min = windows.start.earliest

        longueur = sum(block.duration for block in gene.blocks)
        longueur += (ShiftStructure.BREAK_DURATION + ShiftStructure.BREAK_DURATION
                + ShiftStructure.LUNCH_DURATION - ShiftStructure.INCLUSIVE_BOUNDS_CORRECTION)
        debut_maximal = min(windows.start.latest, windows.end.latest - longueur)

        nouveau_debut = gene.start + value
        if debut_min > nouveau_debut: return debut_min
        if debut_maximal < nouveau_debut: return debut_maximal
        return nouveau_debut



class BlockBoundaryMutation(Mutation[BlockGenome]):
    """Déplace la frontière entre deux blocs voisins d'un employé tiré au hasard : une durée augmente, l'autre
    diminue d'autant. Σd est conservée ; chaque durée reste au moins ``ShiftStructure.MIN_ACTIVITY_DURATION``.
    """

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        def validate(genes):
            if len(genes) == 0:
                raise EmptyGenomeError(OperatorMessages.EMPTY_GENOME.format(operator=type(self).__name__))

        min_transfer, max_transfer = self.get_transfer_bounds(genome)
        transfer = rng.randint(min_transfer, max_transfer)
        genes_to_try = [x for x in range(len(genome))]
        validate(genes_to_try)
        mutated = list(genome)

        while True:
            if not genes_to_try:
                return genome
            index = rng.randrange(len(genes_to_try))
            try:
                gene_index = genes_to_try[index]
                mutated_gene = mutated[gene_index]
                first_index, second_index = self._get_2_valid_block_to_mutate(mutated_gene, transfer, rng)

                blocks = list(mutated_gene.blocks)
                old_first = blocks[first_index]
                old_second = blocks[second_index]

                new_first = ActivityBlock(old_first.activity, old_first.duration + transfer)
                new_second = ActivityBlock(old_second.activity, old_second.duration - transfer)

                blocks[first_index] = new_first
                blocks[second_index] = new_second

                mutated[gene_index] = BlockGene(mutated_gene.start, tuple(blocks))
                break
            except GeneCannotMutateBoundaryError:
                del genes_to_try[index]

        return tuple(mutated)

    def get_transfer_bounds(self, genome: BlockGenome) -> tuple[int, int]:
        """Bornes (incluses) du nombre de périodes que ``mutate`` peut déplacer d'un bloc à l'autre dans ``genome``.

        Politique actuelle : bornes fixes, ``OperatorDefaults.MIN_BOUNDARY_TRANSFER`` et
        ``OperatorDefaults.MAX_BOUNDARY_TRANSFER``, quel que soit le génome. Le paramètre ``genome`` prépare une
        politique calculée à partir des durées des blocs (voir TODO.md, 7b).
        """
        return OperatorDefaults.MIN_BOUNDARY_TRANSFER, OperatorDefaults.MAX_BOUNDARY_TRANSFER

    def _get_2_valid_block_to_mutate(self, gene: BlockGene, add: int, rng: random.Random):
        minimum_duration = ShiftStructure.MIN_ACTIVITY_DURATION + add
        blocks = gene.blocks

        valid_pairs = []
        for i in range(len(blocks) - 1):
            if blocks[i].duration >= minimum_duration:
                valid_pairs.append((i + 1, i))
            if blocks[i + 1].duration >= minimum_duration:
                valid_pairs.append((i, i + 1))

        if not valid_pairs:
            raise GeneCannotMutateBoundaryError(OperatorMessages.GENE_CANNOT_GIVE.format(
                transfer=add, minimum=ShiftStructure.MIN_ACTIVITY_DURATION
            ))

        return rng.choice(valid_pairs)


class ActivityMutation(Mutation[BlockGenome]):
    """Change l'activité d'un bloc tiré au hasard, pour une autre activité de 1..``instance.activity_count``.

    Cas limite : une instance à une seule activité (bench_1) n'offre aucune autre activité ; le génome est
    alors rendu inchangé.

    Raises (``mutate``):
        EmptyGenomeError: si le génome ne contient aucun gène.
    """

    def __init__(self, instance: ProblemInstance) -> None:
        self.instance = instance

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        if len(genome) == 0:
            raise EmptyGenomeError(OperatorMessages.EMPTY_GENOME.format(operator=type(self).__name__))

        mutated = list(genome)
        max_activity = self.instance.activity_count

        if max_activity < OperatorDefaults.MIN_ACTIVITY_COUNT_TO_MUTATE:
            return tuple(mutated)

        gene_index = rng.randrange(len(mutated))
        old_gene = mutated[gene_index]

        blocks = list(old_gene.blocks)

        block_index = rng.randrange(len(blocks))
        old_block = blocks[block_index]

        all_activities = range(ModelIndexing.FIRST_INDEX, max_activity + ModelIndexing.FIRST_INDEX)
        new_activities = [x for x in all_activities if not x == old_block.activity]
        new_activity = rng.choice(new_activities)

        blocks[block_index] = ActivityBlock(new_activity, old_block.duration)

        mutated[gene_index] = BlockGene(old_gene.start, tuple(blocks))

        return tuple(mutated)


# ---------------------------------------------------------------------------------------------------------------------
# Opérateurs témoins pour BlockEncoding (à écrire, étape 10d)
# ---------------------------------------------------------------------------------------------------------------------

class RandomGenomeCrossover(Crossover[BlockGenome]):
    """Croisement témoin (étape 10d) : ignore les gènes de ses parents et rend deux génomes tirés au hasard.

    Les génomes suivent exactement la loi de l'initialisation : ce sont ceux que rendrait
    ``RandomBlockInitializer.random_genome`` avec le même ``rng``. Garde le nombre de parents et d'enfants de
    ``UniformGeneCrossover`` (2 → 2) : le remplacer ne change ni la sélection des parents ni le nombre d'appels au
    solveur par génération.

    Contrat de ``recombine`` :
        - vérifie seulement le nombre de parents, sans lire leurs gènes ;
        - premier enfant : ``random_genome(rng)`` ; deuxième : le tirage ``random_genome(rng)`` suivant ;
        - ne consomme rien d'autre dans ``rng`` : la recherche locale qui suit, dans la même tâche, voit le même état
          du générateur qu'après deux appels à ``random_genome``.

    Raises (``recombine``):
        WrongParentCountError: si le nombre de parents n'est pas 2.
    """

    def __init__(self, instance: ProblemInstance) -> None:
        self.instance = instance

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def parent_count(self) -> int:
        return OperatorDefaults.CROSSOVER_PARENT_COUNT

    def recombine(self, parents: Sequence[BlockGenome], rng: random.Random) -> tuple[BlockGenome, ...]:
        raise NotImplementedError  # Étape 10d (Pascal)


class RandomGenomeMutation(Mutation[BlockGenome]):
    """Mutation témoin (étape 10d) : ignore le génome reçu et rend un génome tiré au hasard.

    Le génome suit exactement la loi de l'initialisation : c'est celui que rendrait
    ``RandomBlockInitializer.random_genome`` avec le même ``rng``. Contrairement aux autres mutations, un génome
    vide est accepté, puisqu'il n'est pas lu.

    Contrat de ``mutate`` :
        - rend ``random_genome(rng)`` ;
        - ne consomme rien d'autre dans ``rng``.
    """

    def __init__(self, instance: ProblemInstance) -> None:
        self.instance = instance

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        raise NotImplementedError  # Étape 10d (Pascal)
