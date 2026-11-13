"""
Tests de l'initialisation de la population (étape 6 — Mély).

Ces tests vérifient :
    - Le respect du contrat des interfaces.
    - La construction de l'initialiseur.
    - Le fonctionnement du faux solveur local.
    - La taille de la population générée.
    - L'absence de coût initial pour les individus.
    - La faisabilité des horaires générés.
    - La reproductibilité avec une graine fixe.
    - Le rejet des tailles de population invalides.
    - La diversité des populations selon la graine.
    - La faisabilité sur les cinq benchmarks.
    - L'intégration du solveur local.
    - L'utilisation de l'horaire retourné par le solveur.

Les tests utilisent FakeLocalSolver et ne nécessitent
pas l'exécution du solveur MiniZinc.
"""

import random
import unittest

from src.ga.chromosome import BlockEncoding
from src.ga.initialization import PopulationInitializer, RandomBlockInitializer, InvalidPopulationSizeError
from tests.fixtures import FakeLocalSolver, synthetic_instance
from tests.test_feasibility import REFERENCE_SHIFT, single
from src.model.feasibility import FeasibilityChecker
from pathlib import Path
from src.utils.io import load_instance

SEED: int = 0


class TestScaffoldContract(unittest.TestCase):

    def test_interface_is_abstract(self) -> None:
        """Vérifie que l'interface abstraite ne peut pas être instanciée."""
        with self.assertRaises(TypeError):
            PopulationInitializer()  # type: ignore[abstract]

    def test_construction(self) -> None:
        """Vérifie la construction de l'initialiseur."""
        local_solver = FakeLocalSolver()
        initializer = RandomBlockInitializer(
            synthetic_instance(),
            BlockEncoding(),
            local_solver=local_solver
        )

        self.assertIs(initializer.local_solver, local_solver)
        self.assertIsNone(
            RandomBlockInitializer(
                synthetic_instance(),
                BlockEncoding()
            ).local_solver
        )

    def test_fake_local_solver(self) -> None:
        """Vérifie que le faux solveur retourne et enregistre l'horaire."""
        horaire = single(REFERENCE_SHIFT)
        local_solver = FakeLocalSolver()

        result = local_solver.improve(
            horaire,
            random.Random(SEED)
        )

        self.assertIs(result.horaire, horaire)
        self.assertEqual(local_solver.received, [horaire])


class TestRandomBlockInitializer(unittest.TestCase):

    def test_population_size(self) -> None:
        """Vérifie le nombre d'individus et leur coût non évalué."""

        instance = synthetic_instance()
        initializer = RandomBlockInitializer(
            instance,
            BlockEncoding()
        )

        population = initializer.initialize(
            5,
            random.Random(SEED)
        )

        self.assertEqual(len(population), 5)

        for individu in population:
            self.assertIsNone(individu.cost)

    def test_population_feasibility(self) -> None:
        """Vérifie que tous les horaires générés sont faisables."""

        instance = synthetic_instance()
        initializer = RandomBlockInitializer(
            instance,
            BlockEncoding()
        )

        checker = FeasibilityChecker(instance)

        population = initializer.initialize(
            20,
            random.Random(SEED)
        )

        for individu in population:
            violations = checker.violations(individu.horaire)
            self.assertEqual(violations, [])

    def test_reproducibility(self) -> None:
        """Vérifie que la même graine produit la même population."""

        instance = synthetic_instance()
        initializer = RandomBlockInitializer(
            instance,
            BlockEncoding()
        )

        population1 = initializer.initialize(
            20,
            random.Random(SEED)
        )

        population2 = initializer.initialize(
            20,
            random.Random(SEED)
        )

        self.assertEqual(population1, population2)

    def test_invalid_population_size(self) -> None:
        """Vérifie le rejet des tailles de population nulles ou négatives."""
        instance = synthetic_instance()
        initializer = RandomBlockInitializer(
            instance,
            BlockEncoding()
        )

        for size in [0, -1, -5]:
            with self.subTest(size=size):
                with self.assertRaises(InvalidPopulationSizeError):
                    initializer.initialize(size, random.Random(SEED))

    def test_population_diversity(self) -> None:
        """Vérifie que deux graines différentes produisent des populations différentes."""
        instance = synthetic_instance()
        initializer = RandomBlockInitializer(
            instance,
            BlockEncoding()
        )

        population1 = initializer.initialize(
            20,
            random.Random(SEED)
        )

        population2 = initializer.initialize(
            20,
            random.Random(SEED + 1)
        )

        self.assertNotEqual(population1, population2)

    def test_benchmarks_feasibility(self) -> None:
        """Vérifie la faisabilité des individus sur les cinq benchmarks."""

        for number in range(1, 6):
            with self.subTest(benchmark=number):

                path = Path("data") / f"bench_{number}.json"
                instance = load_instance(path)

                initializer = RandomBlockInitializer(
                    instance,
                    BlockEncoding()
                )

                checker = FeasibilityChecker(instance)

                population = initializer.initialize(
                    20,
                    random.Random(SEED)
                )

                for individu in population:
                    violations = checker.violations(individu.horaire)
                    self.assertEqual(violations, [])

    def test_local_solver(self) -> None:
        """Vérifie l'utilisation du solveur local pendant l'initialisation."""

        instance = synthetic_instance()
        encoding = BlockEncoding()
        local_solver = FakeLocalSolver()

        initializer = RandomBlockInitializer(
            instance,
            encoding,
            local_solver=local_solver
        )

        population = initializer.initialize(
            5,
            random.Random(SEED)
        )

        # Le solveur doit être appelé une fois par individu
        self.assertEqual(len(local_solver.received), 5)

        # Chaque horaire reçu correspond à l'individu final
        for individu, horaire in zip(population, local_solver.received):
            self.assertEqual(individu.horaire, horaire)

    def test_local_solver_replacement(self) -> None:
        """Vérifie que l'horaire retourné par le solveur est utilisé."""

        instance = synthetic_instance()
        encoding = BlockEncoding()

        replacement = single(REFERENCE_SHIFT)
        local_solver = FakeLocalSolver(replacement=replacement)

        initializer = RandomBlockInitializer(
            instance,
            encoding,
            local_solver=local_solver
        )

        population = initializer.initialize(
            5,
            random.Random(SEED)
        )

        self.assertEqual(len(local_solver.received), 5)

        for individu in population:
            self.assertEqual(individu.horaire, replacement)
            self.assertEqual(individu.genome, encoding.encode(replacement))
            self.assertIsNone(individu.cost)

if __name__ == "__main__":
    unittest.main()
