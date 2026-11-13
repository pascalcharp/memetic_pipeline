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

Seule exception : ``TestInitializationWithCpSat`` (ajout de Pascal) branche l'initialiseur sur
``MiniZincLocalSolver`` avec CP-SAT (bench_1 et bench_5, quelques secondes).
"""

import random
import unittest

from src.config import ProjectPaths
from src.ga.chromosome import BlockEncoding, BlockGenome
from src.ga.individual import Individu
from src.ga.initialization import PopulationInitializer, RandomBlockInitializer, InvalidPopulationSizeError
from src.memetic.local_search import (
    LocalSearchResult,
    LocalSolver,
    MiniZincLocalSolver,
    RandomEmployeesNeighborhood,
)
from src.memetic.solver import CpSatAdapter, DeterministicTimeLimit, SolverOptions
from src.model.evaluation import CostEvaluator
from src.model.horaire import Horaire
from tests.fixtures import FakeLocalSolver, synthetic_instance
from tests.test_feasibility import REFERENCE_SHIFT, single
from src.model.feasibility import FeasibilityChecker
from pathlib import Path
from src.utils.io import ProblemInstance, load_instance

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


# ---------------------------------------------------------------------------------------------------------------------
# Intégration avec le vrai solveur (MiniZincLocalSolver + CP-SAT) — ajout de Pascal, après la fusion de 5b
# ---------------------------------------------------------------------------------------------------------------------

INTEGRATION_POPULATION_SIZE: int = 6

# Budget déterministe largement suffisant pour bench_1 (voir tests/test_local_search.py).
GENEROUS_UNITS: float = 5.0

# Optimum de bench_1, prouvé par CP-SAT (étape 0).
BENCH_1_OPTIMUM: int = 94

# Taille de voisinage trop petite pour réparer un horaire tiré au hasard sur bench_5 (mesure du 2026-11-13).
SMALL_NEIGHBORHOOD: int = 2


class RecordingLocalSolver(LocalSolver):
    """Délègue à un vrai ``LocalSolver`` et note chaque paire (horaire reçu, résultat rendu)."""

    def __init__(self, inner: LocalSolver) -> None:
        self.inner = inner
        self.calls: list[tuple[Horaire, LocalSearchResult]] = []

    def improve(self, horaire: Horaire, rng: random.Random) -> LocalSearchResult:
        result = self.inner.improve(horaire, rng)
        self.calls.append((horaire, result))
        return result


def bench(number: int) -> ProblemInstance:
    return load_instance(ProjectPaths.DATA_DIR / f"bench_{number}.json")


def recording_cp_sat_solver(instance: ProblemInstance, size: int) -> RecordingLocalSolver:
    return RecordingLocalSolver(
        MiniZincLocalSolver(
            instance,
            CpSatAdapter(SolverOptions(limit=DeterministicTimeLimit(GENEROUS_UNITS))),
            RandomEmployeesNeighborhood(instance, size=size),
            CostEvaluator(instance),
        )
    )


class TestInitializationWithCpSat(unittest.TestCase):
    """L'initialiseur branché sur ``MiniZincLocalSolver`` : ce que le faux solveur ne peut pas vérifier."""

    def initialize(
        self, instance: ProblemInstance, size: int, seed: int = SEED
    ) -> tuple[tuple[Individu[BlockGenome], ...], RecordingLocalSolver]:
        local_solver = recording_cp_sat_solver(instance, size)
        initializer = RandomBlockInitializer(instance, BlockEncoding(), local_solver=local_solver)
        population = initializer.initialize(INTEGRATION_POPULATION_SIZE, random.Random(seed))
        return population, local_solver

    def assert_common_invariants(
        self,
        instance: ProblemInstance,
        population: tuple[Individu[BlockGenome], ...],
        local_solver: RecordingLocalSolver,
    ) -> None:
        """Invariants valables quelle que soit l'issue de chaque résolution."""
        encoding = BlockEncoding()
        evaluator = CostEvaluator(instance)
        checker = FeasibilityChecker(instance)

        self.assertEqual(len(local_solver.calls), INTEGRATION_POPULATION_SIZE)

        for index, (individu, (sampled, result)) in enumerate(zip(population, local_solver.calls)):
            with self.subTest(individu=index, outcome=result.outcome):
                self.assertIsNone(individu.cost)
                self.assertEqual(checker.violations(individu.horaire), [])

                # L'horaire rendu par le solveur est représentable par l'encodage par blocs, sans perte.
                self.assertEqual(individu.horaire, result.horaire)
                self.assertEqual(individu.genome, encoding.encode(result.horaire))

                if not result.outcome.has_solution:
                    # Sans solution, l'horaire tiré au hasard entre tel quel dans la population.
                    self.assertEqual(individu.horaire, sampled)

                sampled_cost = evaluator.evaluate(sampled)
                if sampled_cost.is_feasible:
                    # Borne de coût de 5b : jamais pire qu'un horaire tiré déjà faisable.
                    self.assertLessEqual(evaluator.evaluate(individu.horaire).coverage_cost,
                                         sampled_cost.coverage_cost)

    def test_small_neighborhood_repairs_bench_1(self) -> None:
        """bench_1, un seul employé libéré : chaque horaire tiré est réparé en un horaire faisable."""
        instance = bench(1)
        population, local_solver = self.initialize(instance, size=1)

        self.assert_common_invariants(instance, population, local_solver)

        evaluator = CostEvaluator(instance)
        for index, individu in enumerate(population):
            with self.subTest(individu=index):
                self.assertTrue(evaluator.evaluate(individu.horaire).is_feasible)

    def test_everyone_freed_collapses_bench_1_to_the_optimum(self) -> None:
        """bench_1, tous les employés libérés : chaque individu atteint l'optimum, la population perd sa diversité."""
        instance = bench(1)
        population, local_solver = self.initialize(instance, size=instance.employee_count)

        self.assert_common_invariants(instance, population, local_solver)

        evaluator = CostEvaluator(instance)
        for index, individu in enumerate(population):
            with self.subTest(individu=index):
                cost = evaluator.evaluate(individu.horaire)
                self.assertTrue(cost.is_feasible)
                self.assertEqual(cost.coverage_cost, BENCH_1_OPTIMUM)

    def test_unrepairable_samples_enter_unchanged_on_bench_5(self) -> None:
        """bench_5, petit voisinage : le sous-problème est sans solution, l'horaire tiré est gardé tel quel."""
        instance = bench(5)
        population, local_solver = self.initialize(instance, size=SMALL_NEIGHBORHOOD)

        self.assert_common_invariants(instance, population, local_solver)

        # Le test n'a de sens que si la branche « sans solution » est effectivement exercée.
        self.assertTrue(any(not result.outcome.has_solution for _, result in local_solver.calls))

    def test_same_seed_same_population(self) -> None:
        """Même graine ⇒ même population, solveur réel compris (limite d'effort déterministe)."""
        instance = bench(1)
        first, _ = self.initialize(instance, size=1)
        second, _ = self.initialize(instance, size=1)
        self.assertEqual(first, second)


if __name__ == "__main__":
    unittest.main()
