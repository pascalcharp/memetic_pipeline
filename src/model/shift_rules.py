"""Règles structurelles d'un quart de travail, telles qu'exprimées dans ``horaire.mzn``.

Les durées sont en périodes de 15 minutes. Dans le modèle, chaque employé a cinq jalons :
``debut``, ``pause1``, ``diner``, ``pause2`` et ``fin`` (bornes incluses). Une activité occupe chacun
des quatre intervalles qui les séparent.

    debut ─ activité 1 ─ pause1 ─ activité 2 ─ diner (4 périodes) ─ activité 3 ─ pause2 ─ activité 4 ─ fin

Les constantes de base sont dans ``ShiftStructure``. Les écarts minimaux entre jalons (``ShiftGaps``)
et les décalages des fenêtres (``WindowOffsets``) en sont dérivés : chaque nombre de ``horaire.mzn``
s'explique ainsi par les règles qui le produisent.
"""


class ModelIndexing:
    """Conventions d'indexation et de codage héritées de MiniZinc."""

    # Les périodes, les activités et les employés sont numérotés à partir de 1.
    FIRST_INDEX: int = 1

    # Valeur de la grille « employé × période » quand l'employé ne fait aucune activité
    # (hors quart, en pause ou au dîner), comme dans la seconde sortie de horaire.mzn.
    NO_ACTIVITY: int = 0


class ModelVariableNames:
    """Noms des variables de décision dans horaire.mzn, pour les échanges avec MiniZinc et les messages."""

    START: str = "debut"
    BREAK1: str = "pause1"
    LUNCH: str = "diner"
    BREAK2: str = "pause2"
    END: str = "fin"
    ACTIVITIES: str = "activites"


class ShiftStructure:
    """Constantes de base d'un quart : durées et nombre d'activités."""

    PERIODS_PER_HOUR: int = 4

    ACTIVITIES_PER_SHIFT: int = 4

    BREAK_DURATION: int = 1
    LUNCH_DURATION: int = 4
    MIN_ACTIVITY_DURATION: int = 4

    # Heures rémunérées par quart. Le dîner n'est pas rémunéré, les pauses le sont.
    MIN_PAID_HOURS: int = 6
    MAX_PAID_HOURS: int = 8

    # Les deux bornes du quart sont incluses : un quart de N périodes a un écart (fin - debut) de N - 1.
    INCLUSIVE_BOUNDS_CORRECTION: int = 1

    # Écart (fin - debut) permis : heures rémunérées + dîner, moins la correction des bornes incluses.
    MIN_SHIFT_SPAN: int = MIN_PAID_HOURS * PERIODS_PER_HOUR + LUNCH_DURATION - INCLUSIVE_BOUNDS_CORRECTION
    MAX_SHIFT_SPAN: int = MAX_PAID_HOURS * PERIODS_PER_HOUR + LUNCH_DURATION - INCLUSIVE_BOUNDS_CORRECTION


class ShiftGaps:
    """Écarts minimaux entre deux jalons consécutifs, déduits des durées.

    Chaque écart garantit une activité d'au moins ``MIN_ACTIVITY_DURATION`` périodes entre les jalons,
    plus la durée de la pause ou du dîner qui précède l'activité.
    """

    START_TO_BREAK1: int = ShiftStructure.MIN_ACTIVITY_DURATION
    BREAK1_TO_LUNCH: int = ShiftStructure.BREAK_DURATION + ShiftStructure.MIN_ACTIVITY_DURATION
    LUNCH_TO_BREAK2: int = ShiftStructure.LUNCH_DURATION + ShiftStructure.MIN_ACTIVITY_DURATION
    BREAK2_TO_END: int = ShiftStructure.MIN_ACTIVITY_DURATION


class WindowOffsets:
    """Décalages des fenêtres de chaque jalon par rapport à la plage utile de l'instance.

    La plage utile va de ``MIN_PERIODES`` à ``MAX_PERIODES`` (calculées par instance). Pour un jalon :
        - au plus tôt  = MIN_PERIODES + ``..._EARLIEST_AFTER_FIRST``
        - au plus tard = MAX_PERIODES - ``..._LATEST_BEFORE_LAST``
    Un jalon doit laisser la place, avant lui, aux écarts qui le précèdent et, après lui, à ceux qui le suivent.
    """

    START_EARLIEST_AFTER_FIRST: int = 0
    START_LATEST_BEFORE_LAST: int = ShiftStructure.MIN_SHIFT_SPAN

    BREAK1_EARLIEST_AFTER_FIRST: int = ShiftGaps.START_TO_BREAK1
    BREAK1_LATEST_BEFORE_LAST: int = ShiftGaps.BREAK1_TO_LUNCH + ShiftGaps.LUNCH_TO_BREAK2 + ShiftGaps.BREAK2_TO_END

    LUNCH_EARLIEST_AFTER_FIRST: int = ShiftGaps.START_TO_BREAK1 + ShiftGaps.BREAK1_TO_LUNCH
    LUNCH_LATEST_BEFORE_LAST: int = ShiftGaps.LUNCH_TO_BREAK2 + ShiftGaps.BREAK2_TO_END

    BREAK2_EARLIEST_AFTER_FIRST: int = ShiftGaps.START_TO_BREAK1 + ShiftGaps.BREAK1_TO_LUNCH + ShiftGaps.LUNCH_TO_BREAK2
    BREAK2_LATEST_BEFORE_LAST: int = ShiftGaps.BREAK2_TO_END

    END_EARLIEST_AFTER_FIRST: int = ShiftStructure.MIN_SHIFT_SPAN
    END_LATEST_BEFORE_LAST: int = 0
