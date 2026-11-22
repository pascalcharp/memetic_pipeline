from typing import Sequence
import unittest
import random

from src.ga.chromosome import BlockEncoding, BlockGenome, Encoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.operators import Crossover, Mutation
from src.ga.registry import IncompatibleOperatorError
from src.ga.selection import TournamentSelector, UniformMutableSelector
from src.memetic.config import InvalidMemeticConfigError, MemeticConfig
from src.memetic.termination import GenerationLimit
from src.model.evaluation import CostEvaluator
from src.model.horaire import Horaire
from tests.fixtures import FakeConvergenceCriterion, FakeCrossover, FakeLocalSolver, FakeMutation, FakeRestartPolicy, FakeSurvivorSelector
from tests.test_feasibility import synthetic_instance

POPULATION_SIZE: int = 4
CROSSOVER_COUNT: int = 2
MUTATION_COUNT: int = 1
MASTER_SEED: int = 42
GENERATIONS: int = 3
INVALID_GENERATIONS: int = 0

def fake_config() -> MemeticConfig:
    """Configuration complète avec les faux objets, sans MiniZinc."""
    instance = synthetic_instance()
    encoding = BlockEncoding()
    return MemeticConfig(
        encoding=encoding,
        initializer=RandomBlockInitializer(instance, encoding),
        parent_selector=TournamentSelector(),
        crossover=FakeCrossover(),
        mutable_selector=UniformMutableSelector(),
        mutation=FakeMutation(),
        local_solver=FakeLocalSolver(),
        evaluator=CostEvaluator(instance),
        survivor_selector=FakeSurvivorSelector(),
        convergence=FakeConvergenceCriterion(),
        restart=FakeRestartPolicy(),
        termination=GenerationLimit(GENERATIONS),
        population_size=POPULATION_SIZE,
        crossover_count=CROSSOVER_COUNT,
        mutation_count=MUTATION_COUNT,
        master_seed=MASTER_SEED,
    )

def fake_config_with_crossover(crossover: Crossover):
    """Configuration complète avec les faux objets, sans MiniZinc."""
    instance = synthetic_instance()
    encoding = BlockEncoding()
    return MemeticConfig(
        encoding=encoding,
        initializer=RandomBlockInitializer(instance, encoding),
        parent_selector=TournamentSelector(),
        crossover=crossover,
        mutable_selector=UniformMutableSelector(),
        mutation=FakeMutation(),
        local_solver=FakeLocalSolver(),
        evaluator=CostEvaluator(instance),
        survivor_selector=FakeSurvivorSelector(),
        convergence=FakeConvergenceCriterion(),
        restart=FakeRestartPolicy(),
        termination=GenerationLimit(GENERATIONS),
        population_size=POPULATION_SIZE,
        crossover_count=CROSSOVER_COUNT,
        mutation_count=MUTATION_COUNT,
        master_seed=MASTER_SEED,
    )

def fake_config_with_mutation(mutation: Mutation):
    """Configuration complète avec les faux objets, sans MiniZinc."""
    instance = synthetic_instance()
    encoding = BlockEncoding()
    return MemeticConfig(
        encoding=encoding,
        initializer=RandomBlockInitializer(instance, encoding),
        parent_selector=TournamentSelector(),
        crossover=FakeCrossover(),
        mutable_selector=UniformMutableSelector(),
        mutation=mutation,
        local_solver=FakeLocalSolver(),
        evaluator=CostEvaluator(instance),
        survivor_selector=FakeSurvivorSelector(),
        convergence=FakeConvergenceCriterion(),
        restart=FakeRestartPolicy(),
        termination=GenerationLimit(GENERATIONS),
        population_size=POPULATION_SIZE,
        crossover_count=CROSSOVER_COUNT,
        mutation_count=MUTATION_COUNT,
        master_seed=MASTER_SEED,
    )

def fake_config_with_size_and_count(population_size: int, crossover_count: int, mutation_count: int):
    """Configuration complète avec les faux objets, sans MiniZinc."""
    instance = synthetic_instance()
    encoding = BlockEncoding()
    return MemeticConfig(
        encoding=encoding,
        initializer=RandomBlockInitializer(instance, encoding),
        parent_selector=TournamentSelector(),
        crossover=FakeCrossover(),
        mutable_selector=UniformMutableSelector(),
        mutation=FakeMutation(),
        local_solver=FakeLocalSolver(),
        evaluator=CostEvaluator(instance),
        survivor_selector=FakeSurvivorSelector(),
        convergence=FakeConvergenceCriterion(),
        restart=FakeRestartPolicy(),
        termination=GenerationLimit(GENERATIONS),
        population_size=population_size,
        crossover_count=crossover_count,
        mutation_count=mutation_count,
        master_seed=MASTER_SEED,
    )


class OtherEncoding[str](Encoding[str]):
    def encode(self, horaire: Horaire) -> str:
        raise NotImplemented()
    def decode(self, genome: str) -> Horaire:
        raise NotImplemented()

class NotCompatibleCrossover(Crossover[OtherEncoding]):
    """Fausse mutation pour ``BlockEncoding`` : rend le génome inchangé et note chaque appel."""

    @classmethod
    def encoding_type(cls) -> type[Encoding[OtherEncoding]]:
        return OtherEncoding

    def parent_count(self) -> int:
        raise NotImplemented()

    def recombine(self, parents: Sequence[OtherEncoding], rng: random.Random) -> tuple[OtherEncoding, ...]:
        raise NotImplemented()

class NotCompatibleMutation(Mutation[OtherEncoding]):
    """Fausse mutation pour ``BlockEncoding`` : rend le génome inchangé et note chaque appel."""

    def __init__(self) -> None:
        self.received: list[BlockGenome] = []

    @classmethod
    def encoding_type(cls) -> type[Encoding[OtherEncoding]]:
        return OtherEncoding

    def mutate(self, genome: OtherEncoding, rng: random.Random) -> OtherEncoding:
        raise NotImplemented()


class MemeticConfigTest(unittest.TestCase):
    config: MemeticConfig

    def setUp(self) -> None:
        self.config = fake_config()
        return super().setUp()

    def test_validate_mutation(self):
        self.config = fake_config_with_mutation(NotCompatibleMutation())
        with self.assertRaises(IncompatibleOperatorError):
            self.config.validate()

    def test_validate_crossover(self):
        self.config = fake_config_with_crossover(NotCompatibleCrossover())
        with self.assertRaises(IncompatibleOperatorError):
            self.config.validate()

    def test_validate_invalide_population_size(self):
        self.config = fake_config_with_size_and_count(0, 100, 100)
        with self.assertRaises(InvalidMemeticConfigError):
            self.config.validate()

    def test_validate_invalide_crossover_count(self):
        self.config = fake_config_with_size_and_count(100, -1, 100)
        with self.assertRaises(InvalidMemeticConfigError):
            self.config.validate()

    def test_validate_invalide_mutation_count(self):
        self.config = fake_config_with_size_and_count(100, 100, -1)
        with self.assertRaises(InvalidMemeticConfigError):
            self.config.validate()

    def test_validate_invalide_both_crossover_and_mutation_count(self):
        self.config = fake_config_with_size_and_count(100, 0, 0)
        with self.assertRaises(InvalidMemeticConfigError) as cm:
            self.config.validate()

if __name__ == "__main__":
    unittest.main()
