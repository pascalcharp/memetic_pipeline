"""Tests des collecteurs (src/observability/collectors.py) — étape 8b, Mély.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche
``etape-8b-observabilite`` (voir TODO.md, 8b), sans MiniZinc, avec des populations construites à la main
(``evaluated_individual`` et ``cost_with_total`` dans tests/fixtures.py, ou des ``CostBreakdown`` écrits à la main)
et les enregistrements lus dans un ``MemorySink`` à travers ``ObservationHub`` :
    - ``CostStatisticsCollector`` : min, moyenne, médiane, max, écart-type de ``cost.total`` calculés à la main ;
      termes du coût décomposé ; population d'un seul individu (écart-type nul) ; rien pour les autres événements ;
    - ``DiversityCollector`` : deux génomes égaux à une permutation des employés près comptent comme un seul
      (génotypique) ; grilles distinctes (phénotypique) ; nombre de coûts distincts ; une mesure toutes les
      ``every`` générations seulement ;
    - ``FeasibilityRateCollector`` : taux avant et après le ``LocalSolver``, par origine et par opérateur, sur des
      ``LocalSearchDone`` construits à la main ; taux de la génération puis taux cumulés à ``RunEnded`` ; aucun
      appel (division par zéro évitée) ;
    - ``SolverEffortCollector`` : sommes cumulées des statistiques ; statistiques absentes (``None``) ; nombre
      d'appels ; ``solve_time`` séparé des mesures déterministes ;
    - tous : les enregistrements contiennent ``schema_version`` et ``event`` et sont sérialisables en JSON
      (``json.dumps``, pas de types numpy) ; un collecteur ne consomme pas le générateur aléatoire du moteur
      (l'état d'un ``random.Random`` passé à côté est inchangé).
"""

import unittest

from src.observability.collectors import (
    CollectorDefaults,
    CollectorError,
    CostStatisticsCollector,
    DiversityCollector,
    FeasibilityRateCollector,
    InvalidCollectorParameterError,
    MetricCollector,
    SolverEffortCollector,
)
from tests.fixtures import synthetic_instance

INVALID_EVERY: int = 0


class TestScaffoldContract(unittest.TestCase):

    def test_givenInterface_whenInstantiated_thenRaisesTypeError(self) -> None:
        with self.assertRaises(TypeError):
            MetricCollector()  # type: ignore[abstract]

    def test_givenCollectors_whenChecked_thenImplementMetricCollector(self) -> None:
        for collector in (CostStatisticsCollector, DiversityCollector, FeasibilityRateCollector, SolverEffortCollector):
            with self.subTest(collector=collector.__name__):
                self.assertTrue(issubclass(collector, MetricCollector))

    def test_givenNoEvery_whenDiversityCollector_thenDefaultFrequency(self) -> None:
        collector = DiversityCollector(synthetic_instance().period_count)
        self.assertEqual(collector.every, CollectorDefaults.DIVERSITY_EVERY_GENERATIONS)

    def test_givenInvalidEvery_whenDiversityCollector_thenRaisesWithValueInMessage(self) -> None:
        with self.assertRaises(InvalidCollectorParameterError) as context:
            DiversityCollector(synthetic_instance().period_count, every=INVALID_EVERY)
        self.assertIn(str(INVALID_EVERY), str(context.exception))
        self.assertIsInstance(context.exception, CollectorError)


if __name__ == "__main__":
    unittest.main()
