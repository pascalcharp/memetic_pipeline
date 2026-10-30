"""Phénotype canonique : l'horaire de tous les employés, avec les mêmes variables que ``horaire.mzn``.

Chaque employé a cinq jalons (numéros de période MiniZinc, à partir de 1) et quatre activités :

    debut ─ activité 1 ─ pause1 ─ activité 2 ─ diner (4 périodes) ─ activité 3 ─ pause2 ─ activité 4 ─ fin

Un ``Horaire`` est une simple donnée : il peut être structurellement infaisable (décision D6).
La faisabilité est vérifiée par un composant distinct (``src/model/feasibility.py``).
Seule une forme invalide (nombre d'activités, aucun employé) lève une exception.
"""

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

import numpy as np

from src.model.shift_rules import ModelIndexing, ModelVariableNames, ShiftStructure


class HoraireMessages:
    """Gabarits des messages d'erreur liés à la forme d'un horaire."""

    WRONG_ACTIVITY_COUNT: str = "Un employé doit avoir {expected} activités ; trouvé {found} : {activities}."
    NO_EMPLOYEE: str = "Un horaire doit contenir au moins un employé."
    MISSING_VARIABLE: str = "Variable « {variable} » absente des variables du modèle."
    WRONG_VARIABLE_LENGTH: str = (
        "La variable « {variable} » doit avoir une valeur par employé ({expected}) ; trouvé {found}."
    )


class HoraireError(Exception):
    """Erreur de base pour un horaire mal formé (pas pour un horaire infaisable, qui est une donnée valide)."""


class MalformedHoraireError(HoraireError):
    """L'horaire n'a pas la forme attendue : nombre d'activités, nombre d'employés, variable manquante."""


@dataclass(frozen=True)
class HoraireEmploye:
    """Quart d'un employé : cinq jalons (bornes incluses, numérotation MiniZinc) et quatre activités.

    Les activités sont numérotées à partir de 1, comme dans le modèle. Aucune règle structurelle
    n'est vérifiée ici : un quart trop court, ou des jalons dans le désordre, restent représentables.
    """

    start: int
    break1: int
    lunch: int
    break2: int
    end: int
    activities: tuple[int, ...]

    def __post_init__(self) -> None:
        if len(self.activities) != ShiftStructure.ACTIVITIES_PER_SHIFT:
            raise MalformedHoraireError(
                HoraireMessages.WRONG_ACTIVITY_COUNT.format(
                    expected=ShiftStructure.ACTIVITIES_PER_SHIFT,
                    found=len(self.activities),
                    activities=self.activities,
                )
            )

    def activity_at(self, period: int) -> int:
        """Activité exercée à la période ``period``, ou ``ModelIndexing.NO_ACTIVITY`` (hors quart, pause, dîner).

        Reprend, dans le même ordre, la cascade de conditions de la 2ᵉ sortie de ``horaire.mzn`` :
        la première condition vraie l'emporte. Pour un quart structurellement faisable, le résultat
        coïncide avec la définition de ``total`` dans le modèle. Pour un quart infaisable (blocs qui se
        chevauchent), ``total`` compterait l'employé deux fois, ce qu'une grille ne peut pas représenter.
        """
        first_activity, second_activity, third_activity, fourth_activity = self.activities

        if period < self.start:
            return ModelIndexing.NO_ACTIVITY
        elif period < self.break1:
            return first_activity
        elif period < self.break1 + ShiftStructure.BREAK_DURATION:
            return ModelIndexing.NO_ACTIVITY
        elif period < self.lunch:
            return second_activity
        elif period < self.lunch + ShiftStructure.LUNCH_DURATION:
            return ModelIndexing.NO_ACTIVITY
        elif period < self.break2:
            return third_activity
        elif period < self.break2 + ShiftStructure.BREAK_DURATION:
            return ModelIndexing.NO_ACTIVITY
        elif period <= self.end:
            return fourth_activity
        else:
            return ModelIndexing.NO_ACTIVITY


@dataclass(frozen=True)
class Horaire:
    """Horaire complet : un ``HoraireEmploye`` par employé, l'employé e (à partir de 1) à l'indice e - 1.

    Figé et comparable par valeur, ce qui permet de vérifier l'aller-retour ``decode(encode(h)) == h``.
    """

    employees: tuple[HoraireEmploye, ...]

    def __post_init__(self) -> None:
        if len(self.employees) == 0:
            raise MalformedHoraireError(HoraireMessages.NO_EMPLOYEE)

    @property
    def employee_count(self) -> int:
        return len(self.employees)

    @classmethod
    def from_model_variables(cls, values: Mapping[str, Sequence[Any]]) -> "Horaire":
        """Construit l'horaire à partir des variables de décision de ``horaire.mzn``.

        ``values`` associe chaque nom de ``ModelVariableNames`` à une liste indexée par employé :
        un entier par employé pour les jalons, une liste de 4 activités par employé pour ``activites``.
        C'est la forme des résultats de minizinc-python (``result[nom]``).

        Raises:
            MalformedHoraireError: variable absente, longueurs différentes, ou nombre d'activités invalide.
        """
        milestone_names = (
            ModelVariableNames.START,
            ModelVariableNames.BREAK1,
            ModelVariableNames.LUNCH,
            ModelVariableNames.BREAK2,
            ModelVariableNames.END,
        )
        all_names = milestone_names + (ModelVariableNames.ACTIVITIES,)

        for variable in all_names:
            if variable not in values:
                raise MalformedHoraireError(HoraireMessages.MISSING_VARIABLE.format(variable=variable))

        employee_count = len(values[ModelVariableNames.START])
        for variable in all_names:
            if len(values[variable]) != employee_count:
                raise MalformedHoraireError(
                    HoraireMessages.WRONG_VARIABLE_LENGTH.format(
                        variable=variable, expected=employee_count, found=len(values[variable])
                    )
                )

        employees = []
        for employee_index in range(employee_count):
            employees.append(
                HoraireEmploye(
                    start=values[ModelVariableNames.START][employee_index],
                    break1=values[ModelVariableNames.BREAK1][employee_index],
                    lunch=values[ModelVariableNames.LUNCH][employee_index],
                    break2=values[ModelVariableNames.BREAK2][employee_index],
                    end=values[ModelVariableNames.END][employee_index],
                    activities=tuple(values[ModelVariableNames.ACTIVITIES][employee_index]),
                )
            )
        return cls(employees=tuple(employees))

    def to_grid(self, period_count: int) -> np.ndarray:
        """Grille « employé × période → activité ou 0 », comme la 2ᵉ sortie de ``horaire.mzn``.

        Tableau numpy de forme (employee_count, period_count), indexé à partir de 0 :
        la période p de l'employé e se lit à l'indice ``[e - 1, p - 1]``.
        Les périodes d'un quart qui déborde de 1..period_count sont simplement ignorées.
        """
        grid = np.full((self.employee_count, period_count), ModelIndexing.NO_ACTIVITY, dtype=np.int64)
        for employee_index, employee in enumerate(self.employees):
            for period_index in range(period_count):
                period = period_index + ModelIndexing.FIRST_INDEX
                grid[employee_index, period_index] = employee.activity_at(period)
        return grid
