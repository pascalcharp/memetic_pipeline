"""Tests de la gestion de la population (src/ga/population.py) — étape 8, Tristan.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche
``etape-8-population`` (voir TODO.md, 8, et D4), sans MiniZinc, avec ``evaluated_individual`` (tests/fixtures.py) :
    - ``PlusSurvivorSelector`` : rend exactement ``size`` individus ; garde les meilleurs selon ``cost.total`` ;
      le meilleur n'est jamais perdu ; un seul exemplaire de chaque génome identique ; moins de ``size`` génomes
      distincts ⇒ complété par des doublons dans l'ordre des coûts ; égalités de coût départagées par l'ordre
      d'entrée (tri stable) ; population vide, non évaluée, ``size`` invalide ⇒ exception (``check_selectable``) ;
    - ``DeathPenaltySurvivorSelector`` : tous les faisables passent avant tout infaisable ; trop peu de faisables
      ⇒ complété par les meilleurs infaisables ; aucun faisable ⇒ les meilleurs infaisables ; sans doublons ;
    - ``StagnationCriterion`` : faux tant que le meilleur coût baisse ; vrai après exactement ``generations``
      générations sans baisse ; ``reset`` remet le compteur à zéro ;
    - ``EliteRestart`` : taille conservée ; les ``elite_count`` meilleurs sont gardés ; le reste vient de
      l'initialiseur (faux ``PopulationInitializer``) et est évalué ; ``elite_count`` > taille ⇒ exception ;
    - toutes les stratégies : la population reçue n'est jamais modifiée ; reproductibilité avec la même graine.
Préférer un vrai ``random.Random`` à graine fixée à un mock du générateur (leçon de la revue de 7b).
"""

import unittest

from src.ga.population import (
    ConvergenceCriterion,
    DeathPenaltySurvivorSelector,
    EliteRestart,
    InvalidPopulationParameterError,
    PlusSurvivorSelector,
    PopulationDefaults,
    PopulationError,
    RestartPolicy,
    StagnationCriterion,
    SurvivorSelector,
)
from src.ga.chromosome import BlockEncoding
from src.ga.initialization import RandomBlockInitializer
from src.model.evaluation import CostEvaluator
from tests.fixtures import synthetic_instance

INVALID_COUNT: int = 0


def elite_restart(elite_count: int = PopulationDefaults.RESTART_ELITE_COUNT) -> EliteRestart:
    instance = synthetic_instance()
    return EliteRestart(RandomBlockInitializer(instance, BlockEncoding()), CostEvaluator(instance), elite_count)


class TestScaffoldContract(unittest.TestCase):

    def test_givenInterfaces_whenInstantiated_thenRaiseTypeError(self) -> None:
        for interface in (SurvivorSelector, ConvergenceCriterion, RestartPolicy):
            with self.subTest(interface=interface.__name__):
                with self.assertRaises(TypeError):
                    interface()  # type: ignore[abstract]

    def test_givenConcreteStrategies_whenChecked_thenImplementTheirInterface(self) -> None:
        self.assertTrue(issubclass(PlusSurvivorSelector, SurvivorSelector))
        self.assertTrue(issubclass(DeathPenaltySurvivorSelector, SurvivorSelector))
        self.assertTrue(issubclass(StagnationCriterion, ConvergenceCriterion))
        self.assertTrue(issubclass(EliteRestart, RestartPolicy))

    def test_givenNoArgument_whenStagnationCriterion_thenDefaultGenerations(self) -> None:
        self.assertEqual(StagnationCriterion().generations, PopulationDefaults.STAGNATION_GENERATIONS)

    def test_givenInvalidGenerations_whenStagnationCriterion_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidPopulationParameterError) as context:
            StagnationCriterion(generations=INVALID_COUNT)
        self.assertIn(str(INVALID_COUNT), str(context.exception))

    def test_givenNoEliteCount_whenEliteRestart_thenDefaultEliteCount(self) -> None:
        self.assertEqual(elite_restart().elite_count, PopulationDefaults.RESTART_ELITE_COUNT)

    def test_givenInvalidEliteCount_whenEliteRestart_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidPopulationParameterError) as context:
            elite_restart(elite_count=INVALID_COUNT)
        self.assertIn(str(INVALID_COUNT), str(context.exception))

    def test_givenPopulationErrors_whenCheckingHierarchy_thenEveryErrorIsAPopulationError(self) -> None:
        self.assertTrue(issubclass(InvalidPopulationParameterError, PopulationError))


if __name__ == "__main__":
    unittest.main()
