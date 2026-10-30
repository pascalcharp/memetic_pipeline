"""Vérification de la faisabilité structurelle d'un horaire : les contraintes de ``horaire.mzn`` sur chaque quart.

Composant distinct de l'encodage (décision D6) : ``decode`` peut rendre un horaire infaisable, et c'est ici
qu'on le constate. Un horaire infaisable n'est pas une erreur : la vérification retourne la liste des violations.

Contraintes vérifiées, pour chaque employé (celles de ``horaire.mzn``) :
    - domaines des variables : chaque jalon dans sa fenêtre (``ProblemInstance.windows``),
      chaque activité dans 1..NB_ACTIVITES ;
    - écarts minimaux entre jalons consécutifs (``ShiftGaps``) ;
    - durée du quart, ``fin - debut`` dans ``MIN_SHIFT_SPAN..MAX_SHIFT_SPAN`` (``ShiftStructure``).

Certaines de ces contraintes sont redondantes : les fenêtres de ``pause1``, ``diner`` et ``pause2``
découlent des autres. Les violer viole donc aussi un écart ou une autre fenêtre.

La couverture (« au moins 1 employé si demande > 0 ») n'est pas structurelle : elle relève de l'évaluation.
"""

from dataclasses import dataclass
from enum import Enum


from src.model.horaire import Horaire, HoraireEmploye
from src.model.shift_rules import ShiftStructure, ModelVariableNames, ShiftGaps, ModelIndexing
from src.utils.io import ProblemInstance


class StructuralRule(Enum):
    """Règles structurelles d'un quart ; la valeur est une description lisible de la violation."""

    START_WINDOW = "debut hors de sa fenêtre"
    BREAK1_WINDOW = "pause1 hors de sa fenêtre"
    LUNCH_WINDOW = "diner hors de sa fenêtre"
    BREAK2_WINDOW = "pause2 hors de sa fenêtre"
    END_WINDOW = "fin hors de sa fenêtre"

    START_TO_BREAK1_GAP = "écart debut → pause1 trop court"
    BREAK1_TO_LUNCH_GAP = "écart pause1 → diner trop court"
    LUNCH_TO_BREAK2_GAP = "écart diner → pause2 trop court"
    BREAK2_TO_END_GAP = "écart pause2 → fin trop court"

    SHIFT_SPAN = "durée du quart (fin - debut) hors des bornes"

    ACTIVITY_DOMAIN = "activité hors de 1..NB_ACTIVITES"


class FeasibilityMessages:
    """Gabarits des messages d'erreur et d'affichage liés à la vérification de faisabilité."""

    EMPLOYEE_COUNT_MISMATCH: str = (
        "L'horaire contient {found} employés, mais l'instance « {instance} » en prévoit {expected}."
    )
    VIOLATION: str = "Employé {employee} : {rule} (valeur : {found})."


class FeasibilityError(Exception):
    """Erreur de base de la vérification de faisabilité (l'infaisabilité elle-même n'en est pas une)."""


class EmployeeCountMismatchError(FeasibilityError):
    """L'horaire n'a pas le nombre d'employés de l'instance : il ne peut pas être comparé à ses contraintes."""


@dataclass(frozen=True)
class Violation:
    """Une contrainte structurelle violée par un employé.

    ``employee`` est le numéro de l'employé (à partir de 1, comme dans MiniZinc).
    ``found`` est la valeur fautive, selon la règle :
        - fenêtre : la valeur du jalon ;
        - écart : l'écart constaté entre les deux jalons ;
        - durée : ``fin - debut`` ;
        - activité : le numéro de l'activité (une violation par activité fautive).
    """

    employee: int
    rule: StructuralRule
    found: int

    def __str__(self) -> str:
        return FeasibilityMessages.VIOLATION.format(employee=self.employee, rule=self.rule.value, found=self.found)


class FeasibilityChecker:
    """Vérifie les contraintes structurelles de ``horaire.mzn`` pour une instance donnée.

    L'instance fournit les fenêtres des jalons et le nombre d'activités. Le vérificateur ne modifie
    jamais l'horaire qu'on lui passe.
    """

    def __init__(self, instance: ProblemInstance) -> None:
        self.instance = instance

    def violations(self, horaire: Horaire) -> list[Violation]:
        """Toutes les violations structurelles de ``horaire``, employé par employé ; liste vide si faisable.

        Toutes les violations sont rapportées, pas seulement la première : un employé peut en cumuler
        plusieurs, et chaque règle violée donne une ``Violation`` distincte.

        Raises:
            EmployeeCountMismatchError: si l'horaire n'a pas ``instance.employee_count`` employés.
        """

        if self.instance.employee_count != horaire.employee_count:
            raise EmployeeCountMismatchError(
                FeasibilityMessages.EMPLOYEE_COUNT_MISMATCH.format(
                    found=horaire.employee_count, instance=self.instance.name, expected=self.instance.employee_count
                )
            )

        violations = []
        for employee, shift in enumerate(horaire.employees, start=ModelIndexing.FIRST_INDEX):
            violations.extend(self.employee_violations(employee, shift))

        return violations

    def time_violations_for_employee(self, employee: int, shift: HoraireEmploye) -> list[Violation]:
        """
        Détecte si la durée de la journée est trop courte ou trop longue, et si les écarts entre les jalons sont
        trop petits.
        """

        violations = []

        span = shift.end - shift.start
        if span > ShiftStructure.MAX_SHIFT_SPAN or span < ShiftStructure.MIN_SHIFT_SPAN:
            violations.append(
                Violation(employee=employee, rule=StructuralRule.SHIFT_SPAN, found=span))

        if shift.break1 - shift.start < ShiftGaps.START_TO_BREAK1:
            violations.append(
                Violation(employee=employee, rule=StructuralRule.START_TO_BREAK1_GAP, found=shift.break1 - shift.start))

        if shift.lunch - shift.break1 < ShiftGaps.BREAK1_TO_LUNCH:
            violations.append(
                Violation(employee=employee, rule=StructuralRule.BREAK1_TO_LUNCH_GAP, found=shift.lunch - shift.break1))

        if shift.break2 - shift.lunch < ShiftGaps.LUNCH_TO_BREAK2:
            violations.append(
                Violation(employee=employee, rule=StructuralRule.LUNCH_TO_BREAK2_GAP, found=shift.break2 - shift.lunch))

        if shift.end - shift.break2 < ShiftGaps.BREAK2_TO_END:
            violations.append(
                Violation(employee=employee, rule=StructuralRule.BREAK2_TO_END_GAP, found=shift.end - shift.break2))

        return violations

    def activity_domain_violations_for_employee(self, employee: int, shift: HoraireEmploye) -> list[Violation]:
        """Détecte les numéros anormaux d'activité"""

        violations = []
        for activity in shift.activities:
            if not (ModelIndexing.FIRST_INDEX <= activity <= self.instance.activity_count):
                violations.append(Violation(employee=employee, rule=StructuralRule.ACTIVITY_DOMAIN, found=activity))
        return violations

    def window_violations_for_employee(self, employee: int, shift: HoraireEmploye) -> list[Violation]:
        """Détecte les jalons hors-fenêtre. """

        violations = []
        for regle, valeur, fenetre in [(StructuralRule.START_WINDOW, shift.start, self.instance.windows.start),
                                       (StructuralRule.BREAK1_WINDOW, shift.break1, self.instance.windows.break1),
                                       (StructuralRule.LUNCH_WINDOW, shift.lunch, self.instance.windows.lunch),
                                       (StructuralRule.BREAK2_WINDOW, shift.break2, self.instance.windows.break2),
                                       (StructuralRule.END_WINDOW, shift.end, self.instance.windows.end)]:
            if not fenetre.contains(valeur):
                violations.append(
                    Violation(employee=employee, rule=regle, found=valeur))
        return violations

    def employee_violations(self, employee: int, shift: HoraireEmploye) -> list[Violation]:
        """Violations structurelles du quart ``shift`` de l'employé numéro ``employee`` (à partir de 1)."""

        violations = []

        violations.extend(self.time_violations_for_employee(employee, shift))
        violations.extend(self.activity_domain_violations_for_employee(employee, shift))
        violations.extend(self.window_violations_for_employee(employee, shift))

        return violations

    def is_feasible(self, horaire: Horaire) -> bool:
        """Vrai si ``horaire`` ne viole aucune contrainte structurelle.

        Raises:
            EmployeeCountMismatchError: si l'horaire n'a pas ``instance.employee_count`` employés.
        """

        return len(self.violations(horaire)) == 0
