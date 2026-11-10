"""Tests de l'initialisation de la population (src/ga/initialization.py) — étape 6, Mély.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche
``etape-6-initialisation`` (voir TODO.md, étape 6), sans MiniZinc :
    - taille : ``initialize(n, rng)`` rend exactement n individus, non évalués ;
    - faisabilité : chaque horaire décodé est sans violation (``FeasibilityChecker``), sur l'instance synthétique
      et sur les cinq bench (``load_instance``) ;
    - conditions de D1 vérifiées gène par gène : d_i ≥ 4, 22 ≤ Σd ≤ 30, quart dans la plage utile, activités valides ;
    - reproductibilité : même graine ⇒ même population ; diversité : deux graines ⇒ populations différentes ;
    - taille invalide (0, négative) ⇒ ``InvalidPopulationSizeError`` ;
    - option ``LocalSolver`` : ``FakeLocalSolver`` (tests/fixtures.py) appelé une fois par individu, et l'individu
      construit à partir de l'horaire rendu (``FakeLocalSolver(replacement=...)``).
"""

import random
import unittest

from src.ga.chromosome import BlockEncoding
from src.ga.initialization import PopulationInitializer, RandomBlockInitializer
from tests.fixtures import FakeLocalSolver, synthetic_instance
from tests.test_feasibility import REFERENCE_SHIFT, single

SEED: int = 0


class TestScaffoldContract(unittest.TestCase):

    def test_interface_is_abstract(self) -> None:
        with self.assertRaises(TypeError):
            PopulationInitializer()  # type: ignore[abstract]

    def test_construction(self) -> None:
        local_solver = FakeLocalSolver()
        initializer = RandomBlockInitializer(synthetic_instance(), BlockEncoding(), local_solver=local_solver)
        self.assertIs(initializer.local_solver, local_solver)
        self.assertIsNone(RandomBlockInitializer(synthetic_instance(), BlockEncoding()).local_solver)

    def test_fake_local_solver(self) -> None:
        horaire = single(REFERENCE_SHIFT)
        local_solver = FakeLocalSolver()
        result = local_solver.improve(horaire, random.Random(SEED))
        self.assertIs(result.horaire, horaire)
        self.assertEqual(local_solver.received, [horaire])


if __name__ == "__main__":
    unittest.main()
