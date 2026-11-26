"""Tests des opérateurs témoins ``src/ga/baselines.py`` (étape 10d).

Le témoin « redémarrages aléatoires » passe par le moteur mémétique, avec un croisement et une mutation qui ignorent
leurs entrées et rendent des génomes aléatoires neufs. Le LocalSolver, l'évaluation, la sélection et la mesure sont
ceux du mémétique : seule la variation change. Sans MiniZinc.
"""

import random
import unittest

from src.config import ProjectPaths
from src.ga.baselines import RandomGenomeCrossover, RandomGenomeMutation
from src.ga.chromosome import BlockEncoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.operators import OperatorDefaults, WrongParentCountError
from src.model.feasibility import FeasibilityChecker
from src.utils.io import load_instance

BENCH_FILE: str = "bench_2.json"
SEED: int = 11
OTHER_SEED: int = 12
REPETITIONS: int = 20


class BaselineTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = load_instance(ProjectPaths.DATA_DIR / BENCH_FILE)
        self.encoding = BlockEncoding()
        self.generator = RandomBlockInitializer(self.instance, self.encoding)
        self.checker = FeasibilityChecker(self.instance)
        rng = random.Random(SEED)
        self.parents = (self.generator.random_genome(rng), self.generator.random_genome(rng))

    def assert_feasible_genome(self, genome) -> None:
        self.assertEqual(len(genome), self.instance.employee_count)
        self.assertEqual(self.checker.violations(self.encoding.decode(genome)), [])


class TestRandomGenomeCrossover(BaselineTestCase):

    def test_givenTwoParents_whenRecombine_thenTwoFeasibleRandomGenomes(self) -> None:
        crossover = RandomGenomeCrossover(self.generator)
        rng = random.Random(OTHER_SEED)
        for _ in range(REPETITIONS):
            children = crossover.recombine(self.parents, rng)
            self.assertEqual(len(children), OperatorDefaults.CROSSOVER_PARENT_COUNT)
            for child in children:
                self.assert_feasible_genome(child)

    def test_givenSeed_whenRecombine_thenSameChildrenAsTheGeneratorWithTheSameSeed(self) -> None:
        children = RandomGenomeCrossover(self.generator).recombine(self.parents, random.Random(OTHER_SEED))
        rng = random.Random(OTHER_SEED)
        expected = (self.generator.random_genome(rng), self.generator.random_genome(rng))
        self.assertEqual(children, expected)

    def test_givenDifferentParents_whenRecombineWithTheSameSeed_thenChildrenIgnoreTheParents(self) -> None:
        crossover = RandomGenomeCrossover(self.generator)
        other_parents = (self.parents[1], self.parents[0])
        self.assertEqual(
            crossover.recombine(self.parents, random.Random(OTHER_SEED)),
            crossover.recombine(other_parents, random.Random(OTHER_SEED)),
        )

    def test_givenParents_whenRecombine_thenParentsAreUnchanged(self) -> None:
        before = tuple(self.parents)
        RandomGenomeCrossover(self.generator).recombine(self.parents, random.Random(OTHER_SEED))
        self.assertEqual(self.parents, before)

    def test_givenWrongParentCount_whenRecombine_thenRaisesWrongParentCountError(self) -> None:
        with self.assertRaises(WrongParentCountError) as context:
            RandomGenomeCrossover(self.generator).recombine(self.parents[:1], random.Random(OTHER_SEED))
        self.assertIn(RandomGenomeCrossover.__name__, str(context.exception))

    def test_givenCrossover_whenCheckingInterface_thenTwoParentsAndBlockEncoding(self) -> None:
        crossover = RandomGenomeCrossover(self.generator)
        self.assertEqual(crossover.parent_count(), OperatorDefaults.CROSSOVER_PARENT_COUNT)
        self.assertTrue(crossover.is_compatible_with(self.encoding))


class TestRandomGenomeMutation(BaselineTestCase):

    def test_givenGenome_whenMutate_thenFeasibleRandomGenome(self) -> None:
        mutation = RandomGenomeMutation(self.generator)
        rng = random.Random(OTHER_SEED)
        for _ in range(REPETITIONS):
            self.assert_feasible_genome(mutation.mutate(self.parents[0], rng))

    def test_givenSeed_whenMutate_thenSameGenomeAsTheGeneratorWithTheSameSeedWhateverTheInput(self) -> None:
        mutation = RandomGenomeMutation(self.generator)
        expected = self.generator.random_genome(random.Random(OTHER_SEED))
        self.assertEqual(mutation.mutate(self.parents[0], random.Random(OTHER_SEED)), expected)
        self.assertEqual(mutation.mutate(self.parents[1], random.Random(OTHER_SEED)), expected)

    def test_givenMutation_whenCheckingInterface_thenBlockEncoding(self) -> None:
        self.assertTrue(RandomGenomeMutation(self.generator).is_compatible_with(self.encoding))


if __name__ == "__main__":
    unittest.main()
