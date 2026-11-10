"""Recherche locale par MiniZinc : le ``SolveurLocal`` du pseudo-code (décisions D2 et D11).

Principe (recherche à grand voisinage) : un ``Neighborhood`` choisit les employés à **libérer** ; tous les
autres sont fixés à leur valeur actuelle. MiniZinc ré-optimise les employés libérés, sous la limite d'effort
de son ``SolverAdapter`` (D10).

    - Les employés structurellement infaisables sont toujours libérés : fixés, ils rendraient le sous-problème
      insatisfiable, puisque leurs jalons sont hors domaine.
    - Si l'entrée est faisable, elle est elle-même une solution du sous-problème : on ajoute la borne
      ``cout_total ≤ coût de couverture de l'entrée``, qui garantit un résultat au moins aussi bon et élague.
      Une entrée infaisable n'a pas de borne : le ``LocalSolver`` la répare.
    - Sans solution (insatisfiable, ou budget épuisé), on rend l'entrée inchangée, avec l'issue : ce n'est pas
      une erreur.

Le ``LocalSolver`` travaille sur le phénotype ``Horaire`` (D5) ; le moteur ré-encode le résultat.
Les employés sont numérotés à partir de 1, comme dans MiniZinc et dans ``Violation.employee``.
"""

import random
from abc import ABC, abstractmethod
from dataclasses import dataclass

from src.memetic.solver import ModelObjective, SolveOutcome, SolverAdapter, SolverStatistics
from src.model.evaluation import CostEvaluator
from src.model.feasibility import FeasibilityChecker
from src.model.horaire import Horaire
from src.model.shift_rules import ModelVariableNames, ShiftStructure, ModelIndexing
from src.utils.io import ProblemInstance


# ---------------------------------------------------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------------------------------------------------

class LocalSearchConstraints:
    """Gabarits des contraintes MiniZinc ajoutées au sous-problème.

    Les noms de variables viennent de ``ModelVariableNames`` et ``ModelObjective`` ; les employés et les blocs
    d'activité sont numérotés à partir de 1, comme dans ``horaire.mzn``.
    """

    # Ex. : FIX_MILESTONE.format(variable=ModelVariableNames.START, employee=2, value=10)
    #       → "constraint debut[2] = 10;"
    FIX_MILESTONE: str = "constraint {variable}[{employee}] = {value};"

    # Ex. : FIX_ACTIVITY.format(variable=ModelVariableNames.ACTIVITIES, employee=2, block=3, value=1)
    #       → "constraint activites[2, 3] = 1;"
    FIX_ACTIVITY: str = "constraint {variable}[{employee}, {block}] = {value};"

    # Ex. : COST_BOUND.format(objective=ModelObjective.TOTAL_COST, bound=94) → "constraint cout_total <= 94;"
    COST_BOUND: str = "constraint {objective} <= {bound};"


class NeighborhoodDefaults:
    """Valeurs par défaut et bornes des voisinages."""

    # Mesure du 2026-11-08 (bench_3, budget de 2 unités) : un employé libéré faisait mieux que deux ou trois.
    RANDOM_EMPLOYEE_COUNT: int = 1

    # k = 0 est permis : seuls les employés infaisables sont alors libérés.
    MIN_RANDOM_EMPLOYEE_COUNT: int = 0


# ---------------------------------------------------------------------------------------------------------------------
# Exceptions
# ---------------------------------------------------------------------------------------------------------------------

class LocalSearchMessages:
    """Gabarits des messages d'erreur de la recherche locale."""

    INVALID_NEIGHBORHOOD_SIZE: str = "Le nombre d'employés à libérer doit être au moins {minimum} ; trouvé {value}."


class LocalSearchError(Exception):
    """Erreur de base de la recherche locale (jamais pour une simple absence de solution)."""


class InvalidNeighborhoodError(LocalSearchError):
    """Un paramètre du voisinage est hors de son domaine."""


# ---------------------------------------------------------------------------------------------------------------------
# Résultat
# ---------------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class LocalSearchResult:
    """Résultat d'un appel au ``LocalSolver``.

    ``horaire`` est la meilleure solution trouvée, ou l'horaire d'entrée inchangé si ``outcome`` n'a pas de
    solution. ``freed_employees`` donne les employés libérés (à partir de 1). ``statistics`` mesure la charge
    du solveur (D10).
    """

    horaire: Horaire
    outcome: SolveOutcome
    freed_employees: frozenset[int]
    statistics: SolverStatistics


# ---------------------------------------------------------------------------------------------------------------------
# Interfaces
# ---------------------------------------------------------------------------------------------------------------------

class Neighborhood(ABC):
    """Stratégie de voisinage (D5, D11) : choisit les employés que le sous-problème laisse libres."""

    @abstractmethod
    def select(self, horaire: Horaire, rng: random.Random) -> frozenset[int]:
        """Employés à libérer dans ``horaire`` (numéros à partir de 1). Ne modifie pas ``horaire``.

        Le seul aléa provient de ``rng`` : même état de ``rng`` ⇒ même sélection.
        """


class LocalSolver(ABC):
    """Le ``SolveurLocal`` du pseudo-code (D5) : améliore ou répare un horaire."""

    @abstractmethod
    def improve(self, horaire: Horaire, rng: random.Random) -> LocalSearchResult:
        """Meilleur horaire trouvé au voisinage de ``horaire`` ; ``horaire`` lui-même n'est jamais modifié.

        Une absence de solution n'est pas une erreur : le résultat contient alors ``horaire`` inchangé.

        Raises:
            SolverFailureError: propagée depuis le ``SolverAdapter`` en cas de panne du solveur.
        """


# ---------------------------------------------------------------------------------------------------------------------
# Implémentations (à écrire, étape 5b)
# ---------------------------------------------------------------------------------------------------------------------

class RandomEmployeesNeighborhood(Neighborhood):
    """Libère ``size`` employés tirés au hasard, plus tous les employés structurellement infaisables (D11).

    Si ``size`` dépasse le nombre d'employés faisables, tous les employés sont libérés.
    """

    def __init__(self, instance: ProblemInstance, size: int = NeighborhoodDefaults.RANDOM_EMPLOYEE_COUNT) -> None:
        """
        Raises:
            InvalidNeighborhoodError: si ``size`` est négatif.
        """
        if size < NeighborhoodDefaults.MIN_RANDOM_EMPLOYEE_COUNT:
            raise InvalidNeighborhoodError(
                LocalSearchMessages.INVALID_NEIGHBORHOOD_SIZE.format(
                    minimum=NeighborhoodDefaults.MIN_RANDOM_EMPLOYEE_COUNT, value=size
                )
            )
        self.instance = instance
        self.size = size
        self.feasibility_checker = FeasibilityChecker(instance)

    def select(self, horaire: Horaire, rng: random.Random) -> frozenset[int]:
        freed = []
        eligible = set(range(1, self.instance.employee_count + 1))

        violations = self.feasibility_checker.violations(horaire)
        for violation in violations:
            if violation.employee in eligible:
                eligible.remove(violation.employee)
                freed.append(violation.employee)

        chosen = rng.sample(sorted(eligible), min(self.size, len(eligible)))
        freed.extend(chosen)
        return frozenset(freed)


class MiniZincLocalSolver(LocalSolver):
    """Recherche locale par MiniZinc : fixe les employés non libérés et ré-optimise les autres (D11)."""

    def __init__(
        self,
        instance: ProblemInstance,
        adapter: SolverAdapter,
        neighborhood: Neighborhood,
        evaluator: CostEvaluator,
    ) -> None:
        self.instance = instance
        self.adapter = adapter
        self.neighborhood = neighborhood
        self.evaluator = evaluator

    def improve(self, horaire: Horaire, rng: random.Random) -> LocalSearchResult:
        freed_employees = self.neighborhood.select(horaire, rng)
        additional_constraints = self.fixing_constraints(horaire, freed_employees)
        additional_constraints.extend(self.cost_bound_constraints(horaire))

        solver_run = self.adapter.solve(self.instance, additional_constraints)

        return LocalSearchResult(
            horaire=Horaire.from_model_variables(solver_run.variables) if solver_run.outcome.has_solution else horaire,
            outcome=solver_run.outcome,
            freed_employees=freed_employees,
            statistics=solver_run.statistics,
        )

    def fixing_constraints(self, horaire: Horaire, freed_employees: frozenset[int]) -> list[str]:
        """Contraintes MiniZinc qui fixent les cinq jalons et les quatre activités de chaque employé non libéré.

        Utilise ``LocalSearchConstraints.FIX_MILESTONE`` et ``FIX_ACTIVITY``, avec les noms de
        ``ModelVariableNames``.
        """
        constraints = []

        for number, schedule in enumerate(horaire.employees, start=ModelIndexing.FIRST_INDEX):
            if number not in freed_employees:
                constraints.extend([
                    LocalSearchConstraints.FIX_MILESTONE.format(variable=name, employee=number,value=value)
                    for name, value in [(ModelVariableNames.START, schedule.start),
                                        (ModelVariableNames.BREAK1, schedule.break1),
                                        (ModelVariableNames.LUNCH, schedule.lunch),
                                        (ModelVariableNames.BREAK2, schedule.break2),
                                        (ModelVariableNames.END, schedule.end)]
                ])

                for block, activity in enumerate(schedule.activities, start=ModelIndexing.FIRST_INDEX):
                    constraints.append(
                        LocalSearchConstraints.FIX_ACTIVITY.format(
                            variable=ModelVariableNames.ACTIVITIES,
                            employee=number,
                            block=block ,
                            value=activity
                        )
                    )

        return constraints

    def cost_bound_constraints(self, horaire: Horaire) -> list[str]:
        """La borne ``cout_total ≤ coût de couverture de horaire`` si ``horaire`` est faisable ET que la contrainte de
        couverture non-nulle est respectée, sinon, aucune.

        Utilise ``LocalSearchConstraints.COST_BOUND`` et ``ModelObjective.TOTAL_COST``.
        """

        breakdown = self.evaluator.evaluate(horaire)
        if breakdown.is_feasible:
            return [LocalSearchConstraints.COST_BOUND.format(objective=ModelObjective.TOTAL_COST, bound=breakdown.coverage_cost)]
        return []
