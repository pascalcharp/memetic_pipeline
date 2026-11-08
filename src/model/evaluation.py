"""Évaluation d'un horaire : coût de couverture de ``horaire.mzn`` et pénalités des violations.

Le coût de couverture est identique à ``cout_total`` du modèle. Pour chaque période p de la plage utile
et chaque activité a, ``total[p, a]`` est le nombre d'employés qui exercent l'activité a à la période p :

    cout_total = Σ (p, a)   max(0, demande[p, a] − total[p, a]) × souscout[p, a]     (employés manquants)
                          + max(0, total[p, a] − demande[p, a]) × surcout[p, a]      (employés de trop)

L'évaluation est définie pour tout horaire, faisable ou non (décision D6). Deux sortes de violations,
qui sont des contraintes dures dans le modèle, deviennent ici des pénalités (étape 4) :
    - « au moins 1 employé si demande > 0 » : une violation par cellule (p, a) de la plage utile où
      ``demande[p, a] > 0`` et ``total[p, a] = 0`` ;
    - les violations structurelles d'un quart, telles que les rapporte ``FeasibilityChecker``.

Le résultat est une décomposition (``CostBreakdown``, décision D8), pas seulement un scalaire.
"""

from dataclasses import dataclass

import numpy as np

from src.model.feasibility import FeasibilityChecker
from src.model.horaire import Horaire
from src.model.shift_rules import ShiftStructure
from src.utils.io import ProblemInstance


class EvaluationDefaults:
    """Valeurs par défaut de l'évaluation : poids des pénalités et seuil des cellules quasi dures."""

    # Même ordre de grandeur que le sous-coût quasi dur des instances : une violation coûte autant
    # qu'un employé manquant là où c'est pratiquement interdit.
    COVERAGE_VIOLATION_PENALTY: int = 1_000_000
    STRUCTURAL_VIOLATION_PENALTY: int = 1_000_000

    # Sous-coût à partir duquel une cellule est dite quasi dure (docs/PROBLEME.md).
    QUASI_HARD_UNDER_COST: int = 1_000_000


@dataclass(frozen=True)
class PenaltyWeights:
    """Poids des pénalités ajoutées au coût de couverture, par violation."""

    coverage_violation: int = EvaluationDefaults.COVERAGE_VIOLATION_PENALTY
    structural_violation: int = EvaluationDefaults.STRUCTURAL_VIOLATION_PENALTY


@dataclass(frozen=True)
class CostBreakdown:
    """Décomposition du coût d'un horaire (D8). Le coût à minimiser par l'algorithme est ``total``.

    ``under_coverage_cost`` et ``over_coverage_cost`` sont les deux termes de ``cout_total``.
    ``quasi_hard_cells`` compte les cellules sous-couvertes dont le sous-coût atteint le seuil quasi dur ;
    c'est une information de diagnostic, déjà comptée dans ``under_coverage_cost``.
    ``coverage_violations`` et ``structural_violations`` comptent les violations ; ``penalty_cost`` est
    leur somme pondérée par ``PenaltyWeights``.
    """

    under_coverage_cost: int
    over_coverage_cost: int
    quasi_hard_cells: int
    coverage_violations: int
    structural_violations: int
    penalty_cost: int

    @property
    def coverage_cost(self) -> int:
        """Coût de couverture, identique à ``cout_total`` de ``horaire.mzn``."""
        return self.under_coverage_cost + self.over_coverage_cost

    @property
    def total(self) -> int:
        """Coût à minimiser : coût de couverture plus pénalités."""
        return self.coverage_cost + self.penalty_cost

    @property
    def is_feasible(self) -> bool:
        """Vrai si l'horaire respecte toutes les contraintes dures du modèle (aucune violation)."""
        return self.coverage_violations == 0 and self.structural_violations == 0


class CostEvaluator:
    """Évalue des horaires pour une instance donnée. Ne modifie jamais l'horaire qu'on lui passe."""

    # PenaltyWeights est figée : partager l'instance par défaut entre évaluateurs est sans danger.
    def __init__(self, instance: ProblemInstance, weights: PenaltyWeights = PenaltyWeights()) -> None:
        self.instance = instance
        self.weights = weights
        self.feasibility_checker = FeasibilityChecker(instance)

    def coverage_totals(self, horaire: Horaire) -> np.ndarray:
        """Le tableau ``total`` de ``horaire.mzn`` : nombre d'employés par période et par activité.

        Tableau numpy de forme (period_count, activity_count), comme ``instance.demand`` : la cellule
        (p, a) se lit à l'indice ``[p - 1, a - 1]``. Seules les périodes de la plage utile sont comptées ;
        les autres cellules valent 0. Une activité hors de 1..activity_count (horaire infaisable) n'a pas
        de colonne : elle n'est comptée nulle part.
        """
        total = np.zeros((self.instance.period_count, self.instance.activity_count), dtype=int)

        for employee in horaire.employees:
            activity1, activity2, activity3, activity4 = employee.activities
            for period in range(self.instance.first_useful_period, self.instance.last_useful_period + 1):
                if employee.start <= period < employee.break1:
                    if 1 <= activity1 <= self.instance.activity_count:
                        total[period - 1, activity1 - 1] += 1
                if employee.break1 + ShiftStructure.BREAK_DURATION <= period < employee.lunch:
                    if 1 <= activity2 <= self.instance.activity_count:
                        total[period - 1, activity2 - 1] += 1
                if employee.lunch + ShiftStructure.LUNCH_DURATION <= period < employee.break2:
                    if 1 <= activity3 <= self.instance.activity_count:
                        total[period - 1, activity3 - 1] += 1
                if employee.break2 + ShiftStructure.BREAK_DURATION <= period <= employee.end:
                    if 1 <= activity4 <= self.instance.activity_count:
                        total[period - 1, activity4 - 1] += 1

        return total

    def evaluate(self, horaire: Horaire) -> CostBreakdown:
        """Décomposition du coût de ``horaire``, faisable ou non.

        Raises:
            EmployeeCountMismatchError: si l'horaire n'a pas ``instance.employee_count`` employés
                (propagée depuis ``FeasibilityChecker``).
        """

        # En premier, car si l'exception est levée, les autres calculs seront inutiles
        total_structural_violations = len(self.feasibility_checker.violations(horaire))

        useful_range = slice(self.instance.first_useful_period - 1, self.instance.last_useful_period)
        coverage = self.coverage_totals(horaire)
        useful_coverage = coverage[useful_range]
        useful_demand = self.instance.demand[useful_range]
        useful_under_cost = self.instance.under_cost[useful_range]

        diff = useful_demand - useful_coverage
        shortage = np.maximum(0, diff)
        surplus = np.maximum(0, -diff)


        under_cost_matrix = shortage * useful_under_cost
        total_under_cost = int(np.sum(under_cost_matrix))
        total_over_cost = int(np.sum(surplus * self.instance.over_cost[useful_range]))

        zero_coverage_cases = (useful_demand > 0) & (useful_coverage == 0)
        total_coverage_violations = int(np.count_nonzero(zero_coverage_cases))

        quasi_hard_cases = (shortage > 0) & (useful_under_cost >=  EvaluationDefaults.QUASI_HARD_UNDER_COST)
        total_quasi_hard_cells = int(np.count_nonzero(quasi_hard_cases))

        penalty_cost = (
                total_coverage_violations * self.weights.coverage_violation
                + total_structural_violations * self.weights.structural_violation
        )

        return CostBreakdown(
            under_coverage_cost=total_under_cost,
            over_coverage_cost=total_over_cost,
            quasi_hard_cells=total_quasi_hard_cells,
            coverage_violations=total_coverage_violations,
            structural_violations=total_structural_violations,
            penalty_cost=penalty_cost,
        )

