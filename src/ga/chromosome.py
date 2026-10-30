"""Génotype : l'interface ``Encoding[G]`` et les encodages concrets.

Le phénotype canonique est ``Horaire`` (``src/model/horaire.py``). Un encodage traduit un ``Horaire``
en génome de type ``G`` et inversement, sans rien faire d'autre (décision D6) : ni vérification de
faisabilité, ni réparation. ``decode`` peut donc rendre un horaire infaisable.

Premier encodage : ``BlockEncoding`` (décision D1), un gène par employé. Le gène donne la période de
début, puis l'activité et la durée (en périodes) de chacun des quatre blocs d'activité :

    debut ─ bloc 1 ─ pause1 ─ bloc 2 ─ diner ─ bloc 3 ─ pause2 ─ bloc 4 ─ fin

Les jalons s'en déduisent (d_i est la durée du bloc i) :
    pause1 = debut + d1
    diner  = pause1 + 1 + d2         (1 = durée de la pause)
    pause2 = diner + 4 + d3          (4 = durée du dîner)
    fin    = pause2 + d4
C'est une bijection avec les jalons de ``HoraireEmploye`` : l'ordre des jalons est garanti par
construction dès que chaque d_i est positif.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.model.horaire import Horaire, HoraireEmploye
from src.model.shift_rules import ShiftStructure


class GenomeMessages:
    """Gabarits des messages d'erreur liés à la forme d'un génome."""

    WRONG_BLOCK_COUNT: str = "Un gène doit avoir {expected} blocs d'activité ; trouvé {found}."


class GenomeError(Exception):
    """Erreur de base pour un génome mal formé (pas pour un génome qui décode en horaire infaisable)."""


class MalformedGenomeError(GenomeError):
    """Le génome n'a pas la forme attendue par son encodage (par exemple, un nombre de blocs invalide)."""


class Encoding[G](ABC):
    """Traduction entre le phénotype ``Horaire`` et un génome de type ``G`` (décisions D1, D5 et D6).

    Les deux méthodes sont des traductions pures et réciproques : pour tout horaire ``h`` et tout génome
    ``g`` de l'encodage, ``decode(encode(h)) == h`` et ``encode(decode(g)) == g``. Elles ne vérifient pas
    la faisabilité et ne lèvent pas d'exception pour un horaire ou un génome infaisable.
    """

    @abstractmethod
    def encode(self, horaire: Horaire) -> G:
        """Génome qui représente ``horaire``."""

    @abstractmethod
    def decode(self, genome: G) -> Horaire:
        """Horaire représenté par ``genome``, faisable ou non."""


@dataclass(frozen=True)
class ActivityBlock:
    """Un bloc d'activité d'un quart : l'activité exercée (à partir de 1) et sa durée en périodes."""

    activity: int
    duration: int


@dataclass(frozen=True)
class BlockGene:
    """Gène d'un employé dans ``BlockEncoding`` : période de début et quatre blocs d'activité, dans l'ordre.

    Aucune règle structurelle n'est vérifiée ici : une durée trop courte ou négative reste représentable.
    """

    start: int
    blocks: tuple[ActivityBlock, ...]

    def __post_init__(self) -> None:
        if len(self.blocks) != ShiftStructure.ACTIVITIES_PER_SHIFT:
            raise MalformedGenomeError(
                GenomeMessages.WRONG_BLOCK_COUNT.format(
                    expected=ShiftStructure.ACTIVITIES_PER_SHIFT, found=len(self.blocks)
                )
            )


# Génome de BlockEncoding : un gène par employé, l'employé e (à partir de 1) à l'indice e - 1.
type BlockGenome = tuple[BlockGene, ...]


class BlockEncoding(Encoding[BlockGenome]):
    """Encodage par blocs (D1) : un ``BlockGene`` par employé, dans l'ordre des employés de l'horaire."""

    def encode(self, horaire: Horaire) -> BlockGenome:
        """Un gène par employé de ``horaire``, dans le même ordre."""
        # À écrire (P).
        raise NotImplementedError

    def decode(self, genome: BlockGenome) -> Horaire:
        """Un quart par gène de ``genome``, dans le même ordre."""
        # À écrire (P).
        raise NotImplementedError

    def encode_shift(self, shift: HoraireEmploye) -> BlockGene:
        """Gène d'un seul employé : début, puis activité et durée de chaque bloc (formules du module)."""
        # À écrire (P).
        raise NotImplementedError

    def decode_gene(self, gene: BlockGene) -> HoraireEmploye:
        """Quart d'un seul employé : jalons déduits du début et des durées (formules du module)."""
        # À écrire (P).
        raise NotImplementedError
