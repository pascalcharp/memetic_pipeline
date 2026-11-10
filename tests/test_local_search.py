"""Tests de la recherche locale (src/memetic/local_search.py) — étape 5b, Pascal.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Les tests complets sont écrits sur la branche
``etape-5b-local-solver`` (voir TODO.md, 5b) :
    - les employés non libérés sont inchangés ; l'entrée n'est jamais modifiée ;
    - entrée faisable ⇒ coût de couverture du résultat ≤ celui de l'entrée ;
    - un employé infaisable est toujours libéré ; réparation d'une entrée infaisable sur bench_1 ;
    - cas limites : k = 0, k ≥ nombre d'employés, sous-problème insatisfiable ⇒ entrée rendue avec son issue ;
    - reproductibilité : même graine et même limite déterministe ⇒ même résultat.
"""

import dataclasses
import unittest

from src.memetic.local_search import (
    InvalidNeighborhoodError,
    LocalSearchConstraints,
    LocalSearchResult,
    LocalSolver,
    Neighborhood,
    NeighborhoodDefaults,
    RandomEmployeesNeighborhood,
)
from src.memetic.solver import ModelObjective, SolveOutcome, SolverStatistics
from src.model.shift_rules import ModelVariableNames
from tests.fixtures import synthetic_instance
from tests.test_feasibility import REFERENCE_SHIFT, single


class TestScaffoldContract(unittest.TestCase):

    def test_interfaces_are_abstract(self) -> None:
        for interface in (Neighborhood, LocalSolver):
            with self.subTest(interface=interface.__name__):
                with self.assertRaises(TypeError):
                    interface()  # type: ignore[abstract]

    def test_result_is_frozen(self) -> None:
        result = LocalSearchResult(
            horaire=single(REFERENCE_SHIFT),
            outcome=SolveOutcome.OPTIMAL,
            freed_employees=frozenset({1}),
            statistics=SolverStatistics(),
        )
        with self.assertRaises(dataclasses.FrozenInstanceError):
            result.outcome = SolveOutcome.FEASIBLE  # type: ignore[misc]

    def test_constraint_templates(self) -> None:
        self.assertEqual(
            LocalSearchConstraints.FIX_MILESTONE.format(variable=ModelVariableNames.START, employee=2, value=10),
            "constraint debut[2] = 10;",
        )
        self.assertEqual(
            LocalSearchConstraints.FIX_ACTIVITY.format(variable=ModelVariableNames.ACTIVITIES, employee=2, block=3, value=1),
            "constraint activites[2, 3] = 1;",
        )
        self.assertEqual(
            LocalSearchConstraints.COST_BOUND.format(objective=ModelObjective.TOTAL_COST, bound=94),
            "constraint cout_total <= 94;",
        )


class TestRandomEmployeesNeighborhoodConstruction(unittest.TestCase):

    def test_default_size(self) -> None:
        neighborhood = RandomEmployeesNeighborhood(synthetic_instance())
        self.assertEqual(neighborhood.size, NeighborhoodDefaults.RANDOM_EMPLOYEE_COUNT)

    def test_zero_is_allowed(self) -> None:
        self.assertEqual(RandomEmployeesNeighborhood(synthetic_instance(), size=0).size, 0)

    def test_negative_size_is_rejected(self) -> None:
        with self.assertRaises(InvalidNeighborhoodError) as context:
            RandomEmployeesNeighborhood(synthetic_instance(), size=-1)
        self.assertIn("-1", str(context.exception))


if __name__ == "__main__":
    unittest.main()
