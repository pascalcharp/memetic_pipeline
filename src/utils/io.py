"""Lecture et validation des instances du problème d'horaire (fichiers JSON de ``data/``).

Conventions de numérotation :
    - les **numéros** de période (plage utile, fenêtres des jalons) suivent MiniZinc et commencent à 1 ;
    - les **tableaux** (demande, coûts) sont des tableaux numpy indexés à partir de 0 :
      la période p et l'activité a se lisent à l'indice ``[p - 1, a - 1]``.
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np

from src.model.shift_rules import ModelIndexing, ModelVariableNames, WindowOffsets


class InstanceFields:
    """Noms des champs du fichier JSON d'une instance (mêmes noms que les paramètres de horaire.mzn)."""

    EMPLOYEE_COUNT: str = "NB_EMPLOYES"
    ACTIVITY_COUNT: str = "NB_ACTIVITES"
    PERIOD_COUNT: str = "NB_PERIODES"
    DEMAND: str = "demande"
    OVER_COST: str = "surcout"
    UNDER_COST: str = "souscout"

    COUNTS: tuple[str, ...] = (EMPLOYEE_COUNT, ACTIVITY_COUNT, PERIOD_COUNT)
    MATRICES: tuple[str, ...] = (DEMAND, OVER_COST, UNDER_COST)


class InstanceDomain:
    """Domaine des valeurs des matrices d'une instance."""

    # Demande et coûts sont des entiers positifs ou nuls.
    MIN_MATRIX_VALUE: int = 0

    # Valeur d'une donnée absente : une période dont toutes les données valent NO_DATA est hors de la plage utile.
    NO_DATA: int = 0


class InstanceMessages:
    """Gabarits des messages d'erreur liés à la lecture des instances."""

    FILE_NOT_FOUND: str = "Fichier d'instance introuvable : {path}."
    INVALID_JSON: str = "{source} : JSON invalide ({detail})."
    NOT_AN_OBJECT: str = "{source} : la racine du JSON doit être un objet, pas {found}."
    MISSING_FIELD: str = "{source} : champ obligatoire « {field} » absent."
    NOT_AN_INTEGER: str = "{source} : « {field} » doit contenir des entiers ; trouvé {value!r}{location}."
    COUNT_NOT_POSITIVE: str = "{source} : « {field} » doit être au moins 1 ; trouvé {value}."
    WRONG_ROW_COUNT: str = "{source} : « {field} » doit avoir {expected} lignes ({rows_field}) ; trouvé {found}."
    WRONG_COLUMN_COUNT: str = (
        "{source} : la ligne {row} de « {field} » doit avoir {expected} colonnes ({columns_field}) ; trouvé {found}."
    )
    NOT_A_MATRIX: str = "{source} : « {field} » doit être une liste de listes ; trouvé {found}{location}."
    NEGATIVE_VALUE: str = "{source} : « {field} » contient une valeur négative ({value}) à la période {period}, activité {activity}."
    DEMAND_EXCEEDS_EMPLOYEES: str = (
        "{source} : la demande ({value}) dépasse le nombre d'employés ({employees}) à la période {period}, activité {activity}."
    )
    EMPTY_USEFUL_RANGE: str = "{source} : toutes les données sont nulles ; la plage utile est vide."
    NO_SHIFT_FITS: str = (
        "{source} : la plage utile (périodes {first} à {last}) est trop courte pour un quart ; "
        "le jalon « {milestone} » n'a aucune période possible (de {earliest} à {latest})."
    )
    # Précisions d'emplacement, ajoutées après la valeur fautive (d'où l'espace initial).
    ROW_LOCATION: str = " à la ligne {row}"
    CELL_LOCATION: str = " à la ligne {row}, colonne {column}"
    NO_LOCATION: str = ""


class InstanceDisplay:
    """Gabarits d'affichage d'une instance (``repr`` pour le développeur, ``str`` pour un résumé lisible)."""

    REPR: str = (
        "ProblemInstance(name={name!r}, employee_count={employees}, activity_count={activities}, "
        "period_count={periods}, useful_range={useful_range})"
    )
    WINDOW: str = "{earliest}..{latest}"

    SUMMARY_HEADER: str = "Instance {name} — employés : {employees}, activités : {activities}, périodes : {periods}"
    SUMMARY_USEFUL_RANGE: str = "Plage utile : périodes {first} à {last}"
    SUMMARY_WINDOWS_TITLE: str = "Fenêtres des jalons :"
    SUMMARY_WINDOW_LINE: str = "  {milestone:<{width}}  {window}"
    SUMMARY_DEMAND: str = "Demande : {total} employés-périodes au total, au plus {peak} sur une activité à une période"
    LINE_SEPARATOR: str = "\n"


class InstanceError(Exception):
    """Erreur de base pour tout problème de lecture ou de validation d'une instance."""


class InstanceFileNotFoundError(InstanceError):
    """Le fichier d'instance n'existe pas."""


class InstanceFormatError(InstanceError):
    """Le fichier n'est pas un JSON valide, ou sa structure ne correspond pas au format attendu."""


class InstanceDimensionError(InstanceError):
    """Les dimensions d'une matrice ne correspondent pas aux nombres de périodes et d'activités."""


class InstanceValueError(InstanceError):
    """Une valeur est hors de son domaine (compte nul, valeur négative, demande supérieure au nombre d'employés)."""


class NoShiftFitsError(InstanceError):
    """La plage utile est vide, ou trop courte pour contenir le plus court des quarts."""


@dataclass(frozen=True)
class MilestoneWindow:
    """Périodes possibles pour un jalon, bornes incluses (numérotation MiniZinc, à partir de 1)."""

    earliest: int
    latest: int

    def is_empty(self) -> bool:
        return self.earliest > self.latest

    def __str__(self) -> str:
        return InstanceDisplay.WINDOW.format(earliest=self.earliest, latest=self.latest)


@dataclass(frozen=True)
class ShiftWindows:
    """Fenêtres des cinq jalons d'un quart, calculées comme dans horaire.mzn (MIN_DEBUT..MAX_FIN)."""

    start: MilestoneWindow
    break1: MilestoneWindow
    lunch: MilestoneWindow
    break2: MilestoneWindow
    end: MilestoneWindow

    @classmethod
    def from_useful_range(cls, first_period: int, last_period: int) -> "ShiftWindows":
        """Calcule les fenêtres à partir de la plage utile [first_period, last_period]."""

        def window(earliest_after_first: int, latest_before_last: int) -> MilestoneWindow:
            return MilestoneWindow(first_period + earliest_after_first, last_period - latest_before_last)

        return cls(
            start=window(WindowOffsets.START_EARLIEST_AFTER_FIRST, WindowOffsets.START_LATEST_BEFORE_LAST),
            break1=window(WindowOffsets.BREAK1_EARLIEST_AFTER_FIRST, WindowOffsets.BREAK1_LATEST_BEFORE_LAST),
            lunch=window(WindowOffsets.LUNCH_EARLIEST_AFTER_FIRST, WindowOffsets.LUNCH_LATEST_BEFORE_LAST),
            break2=window(WindowOffsets.BREAK2_EARLIEST_AFTER_FIRST, WindowOffsets.BREAK2_LATEST_BEFORE_LAST),
            end=window(WindowOffsets.END_EARLIEST_AFTER_FIRST, WindowOffsets.END_LATEST_BEFORE_LAST),
        )

    def by_milestone(self) -> dict[str, MilestoneWindow]:
        """Fenêtres indexées par le nom du jalon dans horaire.mzn."""
        return {
            ModelVariableNames.START: self.start,
            ModelVariableNames.BREAK1: self.break1,
            ModelVariableNames.LUNCH: self.lunch,
            ModelVariableNames.BREAK2: self.break2,
            ModelVariableNames.END: self.end,
        }


# eq=False : les tableaux numpy ne se comparent pas avec ==. Deux instances se comparent par leur contenu
# avec numpy (voir les tests), pas par l'opérateur d'égalité.
# repr=False : le repr généré afficherait les matrices en entier ; on le remplace par un repr concis.
@dataclass(frozen=True, eq=False, repr=False)
class ProblemInstance:
    """Instance validée du problème d'horaire.

    Nommée ``ProblemInstance`` pour éviter la confusion avec ``minizinc.Instance``.
    Les matrices sont en lecture seule, de forme (period_count, activity_count).
    """

    name: str
    employee_count: int
    activity_count: int
    period_count: int
    demand: np.ndarray
    over_cost: np.ndarray
    under_cost: np.ndarray
    first_useful_period: int
    last_useful_period: int
    windows: ShiftWindows

    def __repr__(self) -> str:
        """Représentation concise sur une ligne, pour le débogage et les journaux : dimensions, sans les matrices."""
        useful_range = MilestoneWindow(self.first_useful_period, self.last_useful_period)
        return InstanceDisplay.REPR.format(
            name=self.name,
            employees=self.employee_count,
            activities=self.activity_count,
            periods=self.period_count,
            useful_range=useful_range,
        )

    def __str__(self) -> str:
        """Résumé lisible sur plusieurs lignes : dimensions, plage utile, fenêtres des jalons et demande."""
        windows_by_milestone = self.windows.by_milestone()
        name_width = max(len(milestone) for milestone in windows_by_milestone)

        lines = [
            InstanceDisplay.SUMMARY_HEADER.format(
                name=self.name,
                employees=self.employee_count,
                activities=self.activity_count,
                periods=self.period_count,
            ),
            InstanceDisplay.SUMMARY_USEFUL_RANGE.format(first=self.first_useful_period, last=self.last_useful_period),
            InstanceDisplay.SUMMARY_WINDOWS_TITLE,
        ]
        for milestone, window in windows_by_milestone.items():
            lines.append(InstanceDisplay.SUMMARY_WINDOW_LINE.format(milestone=milestone, width=name_width, window=window))
        lines.append(InstanceDisplay.SUMMARY_DEMAND.format(total=int(self.demand.sum()), peak=int(self.demand.max())))

        return InstanceDisplay.LINE_SEPARATOR.join(lines)


def load_instance(path: Path) -> ProblemInstance:
    """Lit, valide et retourne l'instance contenue dans le fichier JSON ``path``.

    Raises:
        InstanceFileNotFoundError: si le fichier n'existe pas.
        InstanceFormatError: si le JSON est invalide, ou si un champ manque ou n'a pas le bon type.
        InstanceDimensionError: si une matrice n'a pas les dimensions annoncées.
        InstanceValueError: si une valeur est hors de son domaine.
        NoShiftFitsError: si aucun quart ne rentre dans la plage utile.
    """
    if not path.is_file():
        raise InstanceFileNotFoundError(InstanceMessages.FILE_NOT_FOUND.format(path=path))

    try:
        with path.open(encoding="utf-8") as instance_file:
            data = json.load(instance_file)
    except json.JSONDecodeError as error:
        raise InstanceFormatError(InstanceMessages.INVALID_JSON.format(source=path.name, detail=error)) from error

    return parse_instance(data, name=path.stem)


def parse_instance(data: Any, name: str) -> ProblemInstance:
    """Valide les données JSON déjà décodées ``data`` et construit l'instance ``name``.

    Mêmes exceptions que ``load_instance``, sauf ``InstanceFileNotFoundError``.
    """
    if not isinstance(data, dict):
        raise InstanceFormatError(InstanceMessages.NOT_AN_OBJECT.format(source=name, found=type(data).__name__))

    for field in InstanceFields.COUNTS + InstanceFields.MATRICES:
        if field not in data:
            raise InstanceFormatError(InstanceMessages.MISSING_FIELD.format(source=name, field=field))

    employee_count = _read_count(data, InstanceFields.EMPLOYEE_COUNT, name)
    activity_count = _read_count(data, InstanceFields.ACTIVITY_COUNT, name)
    period_count = _read_count(data, InstanceFields.PERIOD_COUNT, name)

    demand = _read_matrix(data, InstanceFields.DEMAND, period_count, activity_count, name)
    over_cost = _read_matrix(data, InstanceFields.OVER_COST, period_count, activity_count, name)
    under_cost = _read_matrix(data, InstanceFields.UNDER_COST, period_count, activity_count, name)

    _check_demand_within_employees(demand, employee_count, name)

    first_useful_period, last_useful_period = _useful_range(demand, over_cost, under_cost, name)
    windows = ShiftWindows.from_useful_range(first_useful_period, last_useful_period)
    _check_every_window_is_open(windows, first_useful_period, last_useful_period, name)

    return ProblemInstance(
        name=name,
        employee_count=employee_count,
        activity_count=activity_count,
        period_count=period_count,
        demand=demand,
        over_cost=over_cost,
        under_cost=under_cost,
        first_useful_period=first_useful_period,
        last_useful_period=last_useful_period,
        windows=windows,
    )


def _is_integer(value: Any) -> bool:
    # En Python, bool est une sous-classe de int : true/false du JSON ne sont pas des entiers valides ici.
    return isinstance(value, int) and not isinstance(value, bool)


def _read_count(data: dict, field: str, source: str) -> int:
    value = data[field]
    if not _is_integer(value):
        raise InstanceFormatError(
            InstanceMessages.NOT_AN_INTEGER.format(source=source, field=field, value=value, location=InstanceMessages.NO_LOCATION)
        )
    if value < ModelIndexing.FIRST_INDEX:
        raise InstanceValueError(InstanceMessages.COUNT_NOT_POSITIVE.format(source=source, field=field, value=value))
    return value


def _read_matrix(data: dict, field: str, row_count: int, column_count: int, source: str) -> np.ndarray:
    """Valide la matrice ``field`` (lignes = périodes, colonnes = activités) et la retourne en lecture seule."""
    rows = data[field]
    if not isinstance(rows, list):
        raise InstanceFormatError(
            InstanceMessages.NOT_A_MATRIX.format(source=source, field=field, found=type(rows).__name__, location=InstanceMessages.NO_LOCATION)
        )
    if len(rows) != row_count:
        raise InstanceDimensionError(
            InstanceMessages.WRONG_ROW_COUNT.format(
                source=source, field=field, expected=row_count, rows_field=InstanceFields.PERIOD_COUNT, found=len(rows)
            )
        )

    for row_index, row in enumerate(rows):
        row_number = row_index + ModelIndexing.FIRST_INDEX
        if not isinstance(row, list):
            location = InstanceMessages.ROW_LOCATION.format(row=row_number)
            raise InstanceFormatError(
                InstanceMessages.NOT_A_MATRIX.format(
                    source=source, field=field, found=type(row).__name__, location=location
                )
            )
        if len(row) != column_count:
            raise InstanceDimensionError(
                InstanceMessages.WRONG_COLUMN_COUNT.format(
                    source=source,
                    field=field,
                    row=row_number,
                    expected=column_count,
                    columns_field=InstanceFields.ACTIVITY_COUNT,
                    found=len(row),
                )
            )
        for column_index, value in enumerate(row):
            if not _is_integer(value):
                location = InstanceMessages.CELL_LOCATION.format(
                    row=row_number, column=column_index + ModelIndexing.FIRST_INDEX
                )
                raise InstanceFormatError(
                    InstanceMessages.NOT_AN_INTEGER.format(source=source, field=field, value=value, location=location)
                )
            if value < InstanceDomain.MIN_MATRIX_VALUE:
                raise InstanceValueError(
                    InstanceMessages.NEGATIVE_VALUE.format(
                        source=source,
                        field=field,
                        value=value,
                        period=row_number,
                        activity=column_index + ModelIndexing.FIRST_INDEX,
                    )
                )

    matrix = np.array(rows, dtype=np.int64)
    matrix.setflags(write=False)
    return matrix


def _check_demand_within_employees(demand: np.ndarray, employee_count: int, source: str) -> None:
    # Dans horaire.mzn, la demande a pour domaine 0..NB_EMPLOYES.
    excessive_cells = np.argwhere(demand > employee_count)
    if excessive_cells.size > 0:
        period_index, activity_index = excessive_cells[0]
        raise InstanceValueError(
            InstanceMessages.DEMAND_EXCEEDS_EMPLOYEES.format(
                source=source,
                value=demand[period_index, activity_index],
                employees=employee_count,
                period=period_index + ModelIndexing.FIRST_INDEX,
                activity=activity_index + ModelIndexing.FIRST_INDEX,
            )
        )


def _useful_range(demand: np.ndarray, over_cost: np.ndarray, under_cost: np.ndarray, source: str) -> tuple[int, int]:
    """Première et dernière période dont les données ne sont pas toutes nulles (MIN_PERIODES, MAX_PERIODES)."""
    period_has_data = (
        (demand != InstanceDomain.NO_DATA).any(axis=1)
        | (over_cost != InstanceDomain.NO_DATA).any(axis=1)
        | (under_cost != InstanceDomain.NO_DATA).any(axis=1)
    )
    useful_period_indices = np.flatnonzero(period_has_data)
    if useful_period_indices.size == 0:
        raise NoShiftFitsError(InstanceMessages.EMPTY_USEFUL_RANGE.format(source=source))

    first_useful_period = int(useful_period_indices[0]) + ModelIndexing.FIRST_INDEX
    last_useful_period = int(useful_period_indices[-1]) + ModelIndexing.FIRST_INDEX
    return first_useful_period, last_useful_period


def _check_every_window_is_open(windows: ShiftWindows, first_period: int, last_period: int, source: str) -> None:
    for milestone, window in windows.by_milestone().items():
        if window.is_empty():
            raise NoShiftFitsError(
                InstanceMessages.NO_SHIFT_FITS.format(
                    source=source,
                    first=first_period,
                    last=last_period,
                    milestone=milestone,
                    earliest=window.earliest,
                    latest=window.latest,
                )
            )
