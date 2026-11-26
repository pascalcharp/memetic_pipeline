"""Tests du catalogue des stratégies ``src/memetic/catalog.py`` (étape 10c).

Sans MiniZinc : noms stables des stratégies, création par le nom avec le contexte de construction, vérification des
paramètres sans création, choix par défaut (ceux de l'assemblage de référence), forme JSON des choix.
"""

import unittest

from src.config import ProjectPaths
from src.ga.baselines import RandomGenomeCrossover, RandomGenomeMutation
from src.ga.chromosome import BlockEncoding, Encoding
from src.ga.operators import ActivityMutation, BlockBoundaryMutation, ShiftStartMutation, UniformGeneCrossover
from src.ga.registry import InvalidOperatorParametersError, UnknownOperatorError
from src.memetic.catalog import (
    BuildContext,
    CatalogDefaults,
    IncompatibleStrategyEncodingError,
    ReservedStrategyParameterError,
    StrategyCatalog,
    StrategyChoice,
    StrategyChoices,
    StrategyError,
    StrategyKeys,
    StrategyNames,
    StrategyRoles,
    UnknownStrategyRoleError,
)
from src.utils.io import load_instance

UNKNOWN_ROLE: str = "sélection_magique"
UNKNOWN_NAME: str = "croisement_inexistant"
UNEXPECTED_PARAMETER: str = "taux"
EXPECTED_CLASSES: dict[str, dict[str, type]] = {
    StrategyRoles.CROSSOVER: {
        StrategyNames.UNIFORM_GENE: UniformGeneCrossover,
        StrategyNames.RANDOM_GENOME: RandomGenomeCrossover,
    },
    StrategyRoles.MUTATION: {
        StrategyNames.SHIFT_START: ShiftStartMutation,
        StrategyNames.BLOCK_BOUNDARY: BlockBoundaryMutation,
        StrategyNames.ACTIVITY: ActivityMutation,
        StrategyNames.RANDOM_GENOME: RandomGenomeMutation,
    },
}


class TestCatalogNames(unittest.TestCase):

    def test_givenCatalog_whenListingNames_thenEachRoleHasItsSortedStableNames(self) -> None:
        catalog = StrategyCatalog()
        for role, classes in EXPECTED_CLASSES.items():
            with self.subTest(role=role):
                self.assertEqual(catalog.names(role), tuple(sorted(classes)))

    def test_givenCatalog_whenListingRoles_thenCrossoverAndMutation(self) -> None:
        self.assertEqual(StrategyCatalog().roles(), StrategyRoles.ALL)

    def test_givenUnknownRole_whenListingNames_thenRaisesNamingTheRoleAndTheKnownRoles(self) -> None:
        with self.assertRaises(UnknownStrategyRoleError) as context:
            StrategyCatalog().names(UNKNOWN_ROLE)
        for text in (UNKNOWN_ROLE, StrategyRoles.CROSSOVER, StrategyRoles.MUTATION):
            self.assertIn(text, str(context.exception))

    def test_givenStrategyErrors_whenCheckingHierarchy_thenEveryErrorIsAStrategyError(self) -> None:
        for error in (UnknownStrategyRoleError, ReservedStrategyParameterError, IncompatibleStrategyEncodingError):
            with self.subTest(error=error.__name__):
                self.assertTrue(issubclass(error, StrategyError))


class TestCatalogCreate(unittest.TestCase):

    def setUp(self) -> None:
        self.instance = load_instance(ProjectPaths.DATA_DIR / "bench_1.json")
        self.encoding = BlockEncoding()
        self.context = BuildContext(instance=self.instance, encoding=self.encoding)
        self.catalog = StrategyCatalog()

    def test_givenEachName_whenCreate_thenOperatorOfTheExpectedClassCompatibleWithTheEncoding(self) -> None:
        for role, classes in EXPECTED_CLASSES.items():
            for name, expected_class in classes.items():
                with self.subTest(role=role, name=name):
                    operator = self.catalog.create(role, StrategyChoice(name), self.context)
                    self.assertIsInstance(operator, expected_class)
                    self.assertTrue(operator.is_compatible_with(self.encoding))

    def test_givenMutationNeedingTheInstance_whenCreate_thenItReceivesTheContextInstance(self) -> None:
        for name in (StrategyNames.SHIFT_START, StrategyNames.ACTIVITY):
            with self.subTest(name=name):
                mutation = self.catalog.create(StrategyRoles.MUTATION, StrategyChoice(name), self.context)
                self.assertIs(mutation.instance, self.instance)

    def test_givenRandomGenome_whenCreate_thenItsGeneratorUsesTheContextInstanceAndEncodingWithoutLocalSolver(self) -> None:
        for role in StrategyRoles.ALL:
            with self.subTest(role=role):
                operator = self.catalog.create(role, StrategyChoice(StrategyNames.RANDOM_GENOME), self.context)
                self.assertIs(operator.generator.instance, self.instance)
                self.assertIs(operator.generator.encoding, self.encoding)
                self.assertIsNone(operator.generator.local_solver)

    def test_givenOtherEncoding_whenCreateRandomGenome_thenRaisesNamingTheStrategyAndTheEncoding(self) -> None:
        class OtherEncoding(Encoding[int]):
            def encode(self, horaire):
                raise NotImplementedError

            def decode(self, genome):
                raise NotImplementedError

        context = BuildContext(instance=self.instance, encoding=OtherEncoding())
        with self.assertRaises(IncompatibleStrategyEncodingError) as raised:
            self.catalog.create(StrategyRoles.MUTATION, StrategyChoice(StrategyNames.RANDOM_GENOME), context)
        self.assertIn(StrategyNames.RANDOM_GENOME, str(raised.exception))
        self.assertIn("OtherEncoding", str(raised.exception))

    def test_givenSameChoice_whenCreateTwice_thenTwoDistinctOperators(self) -> None:
        choice = StrategyChoice(StrategyNames.SHIFT_START)
        first = self.catalog.create(StrategyRoles.MUTATION, choice, self.context)
        second = self.catalog.create(StrategyRoles.MUTATION, choice, self.context)
        self.assertIsNot(first, second)

    def test_givenUnknownName_whenCreate_thenRaisesUnknownOperatorErrorListingKnownNames(self) -> None:
        with self.assertRaises(UnknownOperatorError) as context:
            self.catalog.create(StrategyRoles.CROSSOVER, StrategyChoice(UNKNOWN_NAME), self.context)
        self.assertIn(UNKNOWN_NAME, str(context.exception))
        self.assertIn(StrategyNames.UNIFORM_GENE, str(context.exception))

    def test_givenUnexpectedParameter_whenCreate_thenRaisesInvalidOperatorParametersError(self) -> None:
        choice = StrategyChoice(StrategyNames.UNIFORM_GENE, {UNEXPECTED_PARAMETER: 0.5})
        with self.assertRaises(InvalidOperatorParametersError) as context:
            self.catalog.create(StrategyRoles.CROSSOVER, choice, self.context)
        self.assertIn(UNEXPECTED_PARAMETER, str(context.exception))

    def test_givenUnknownRole_whenCreate_thenRaisesUnknownStrategyRoleError(self) -> None:
        with self.assertRaises(UnknownStrategyRoleError):
            self.catalog.create(UNKNOWN_ROLE, StrategyChoice(StrategyNames.UNIFORM_GENE), self.context)


class TestCatalogCheck(unittest.TestCase):
    """``check`` valide un choix sans instance : c'est ce que fait ``run_experiment`` avant toute exécution."""

    def setUp(self) -> None:
        self.catalog = StrategyCatalog()

    def test_givenEveryKnownName_whenCheck_thenPasses(self) -> None:
        for role, classes in EXPECTED_CLASSES.items():
            for name in classes:
                with self.subTest(role=role, name=name):
                    self.catalog.check(role, StrategyChoice(name))

    def test_givenDefaultChoices_whenCheckAll_thenPasses(self) -> None:
        self.catalog.check_all(StrategyChoices())

    def test_givenUnknownName_whenCheck_thenRaisesUnknownOperatorError(self) -> None:
        with self.assertRaises(UnknownOperatorError):
            self.catalog.check(StrategyRoles.MUTATION, StrategyChoice(UNKNOWN_NAME))

    def test_givenUnexpectedParameter_whenCheck_thenRaisesNamingTheParameter(self) -> None:
        choice = StrategyChoice(StrategyNames.ACTIVITY, {UNEXPECTED_PARAMETER: 1})
        with self.assertRaises(InvalidOperatorParametersError) as context:
            self.catalog.check(StrategyRoles.MUTATION, choice)
        self.assertIn(UNEXPECTED_PARAMETER, str(context.exception))

    def test_givenReservedContextParameter_whenCheck_thenRaisesNamingTheParameter(self) -> None:
        choice = StrategyChoice(StrategyNames.ACTIVITY, {CatalogDefaults.CONTEXT_PARAMETER: 1})
        with self.assertRaises(ReservedStrategyParameterError) as context:
            self.catalog.check(StrategyRoles.MUTATION, choice)
        self.assertIn(CatalogDefaults.CONTEXT_PARAMETER, str(context.exception))
        self.assertIn(StrategyNames.ACTIVITY, str(context.exception))

    def test_givenUnknownRole_whenCheck_thenRaisesUnknownStrategyRoleError(self) -> None:
        with self.assertRaises(UnknownStrategyRoleError):
            self.catalog.check(UNKNOWN_ROLE, StrategyChoice(StrategyNames.UNIFORM_GENE))


class TestStrategyChoices(unittest.TestCase):

    def test_givenNoArgument_whenBuildingChoices_thenReferenceAssemblyStrategies(self) -> None:
        choices = StrategyChoices()
        self.assertEqual(choices.crossover, StrategyChoice(StrategyNames.UNIFORM_GENE))
        self.assertEqual(choices.mutation, StrategyChoice(StrategyNames.SHIFT_START))
        self.assertEqual(CatalogDefaults.CROSSOVER, StrategyNames.UNIFORM_GENE)
        self.assertEqual(CatalogDefaults.MUTATION, StrategyNames.SHIFT_START)

    def test_givenChoices_whenByRole_thenOneChoicePerRoleInRoleOrder(self) -> None:
        choices = StrategyChoices(mutation=StrategyChoice(StrategyNames.ACTIVITY))
        self.assertEqual(tuple(choices.by_role()), StrategyRoles.ALL)
        self.assertEqual(choices.by_role()[StrategyRoles.MUTATION], StrategyChoice(StrategyNames.ACTIVITY))

    def test_givenChoice_whenNoParameters_thenEmptyParameters(self) -> None:
        self.assertEqual(dict(StrategyChoice(StrategyNames.ACTIVITY).parameters), {})

    def test_givenChoices_whenToJson_thenNameAndParametersPerRole(self) -> None:
        choices = StrategyChoices(mutation=StrategyChoice(StrategyNames.ACTIVITY))
        self.assertEqual(choices.to_json(), {
            StrategyRoles.CROSSOVER: {StrategyKeys.NAME: StrategyNames.UNIFORM_GENE, StrategyKeys.PARAMETERS: {}},
            StrategyRoles.MUTATION: {StrategyKeys.NAME: StrategyNames.ACTIVITY, StrategyKeys.PARAMETERS: {}},
        })


if __name__ == "__main__":
    unittest.main()
