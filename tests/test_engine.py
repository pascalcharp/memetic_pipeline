"""Tests du moteur mémétique (src/memetic/engine.py, config.py, seeds.py, termination.py) — étape 9, Xavier.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche ``etape-9-boucle``
(voir TODO.md, 9), sans MiniZinc, avec les faux objets de tests/fixtures.py (``FakeCrossover``, ``FakeMutation``,
``FakeLocalSolver``, ``FakeSurvivorSelector``, ``FakeConvergenceCriterion``, ``FakeRestartPolicy``,
``RecordingCollector``), les vrais sélecteurs de 7a, ``RandomBlockInitializer`` et ``CostEvaluator`` sur l'instance
synthétique :
    - ``derive_task_seeds`` : déterministe ; lots différents ⇒ graines différentes ; préfixe stable (la graine d'une
      tâche ne dépend pas du nombre de tâches qui la suivent) ;
    - ``GenerationLimit`` : faux avant la limite, vrai à la limite ;
    - ``MemeticConfig.validate`` : taille, NR, NM hors domaine ⇒ ``InvalidMemeticConfigError`` (nom et valeur dans
      le message) ; NR = NM = 0 ⇒ exception ; opérateur incompatible avec l'encodage ⇒ ``IncompatibleOperatorError`` ;
    - ``Memetic.run`` : s'arrête selon ``termination`` ; population de taille ``population_size`` à chaque génération ;
      NR croisements et NM mutations par génération (compter les appels des faux opérateurs) ; le coût du meilleur
      ne remonte jamais ; restart appelé quand le critère converge, puis ``reset`` ; événements de D8 reçus dans
      l'ordre prévu (``RecordingCollector``) ; reproductibilité : même graine ⇒ même historique, avec et sans
      collecteurs ; entrées des opérateurs jamais modifiées.
L'exécution complète avec les vrais composants (MiniZinc) est la sous-étape 9-intégration (Pascal).
"""

import unittest

from src.ga.chromosome import BlockEncoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.selection import TournamentSelector, UniformMutableSelector
from src.memetic.config import InvalidMemeticConfigError, MemeticConfig, MemeticError
from src.memetic.engine import Memetic
from src.memetic.executor import SequentialExecutor
from src.memetic.seeds import SeedStreams
from src.memetic.termination import (
    GenerationLimit,
    InvalidTerminationParameterError,
    TerminationCriterion,
)
from src.model.evaluation import CostEvaluator
from tests.fixtures import (
    FakeConvergenceCriterion,
    FakeCrossover,
    FakeLocalSolver,
    FakeMutation,
    FakeRestartPolicy,
    FakeSurvivorSelector,
    synthetic_instance,
)

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


class TestScaffoldContract(unittest.TestCase):

    def test_givenInterface_whenInstantiated_thenRaisesTypeError(self) -> None:
        with self.assertRaises(TypeError):
            TerminationCriterion()  # type: ignore[abstract]

    def test_givenGenerationLimit_whenConstructed_thenKeepsItsLimit(self) -> None:
        self.assertEqual(GenerationLimit(GENERATIONS).generations, GENERATIONS)

    def test_givenInvalidGenerations_whenGenerationLimit_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidTerminationParameterError) as context:
            GenerationLimit(INVALID_GENERATIONS)
        self.assertIn(str(INVALID_GENERATIONS), str(context.exception))

    def test_givenFakeObjects_whenBuildingConfig_thenDefaultsAreSequentialAndNoObservation(self) -> None:
        config = fake_config()
        self.assertIsInstance(config.executor, SequentialExecutor)
        self.assertEqual(config.collectors, ())
        self.assertEqual(config.sinks, ())

    def test_givenConfig_whenBuildingEngine_thenEngineKeepsIt(self) -> None:
        config = fake_config()
        self.assertIs(Memetic(config).config, config)

    def test_givenSeedStreams_whenListed_thenAllDistinct(self) -> None:
        streams = [value for name, value in vars(SeedStreams).items() if name.isupper()]
        self.assertEqual(len(streams), len(set(streams)))

    def test_givenMemeticErrors_whenCheckingHierarchy_thenConfigErrorIsAMemeticError(self) -> None:
        self.assertTrue(issubclass(InvalidMemeticConfigError, MemeticError))


if __name__ == "__main__":
    unittest.main()
