"""Tests du registre des opérateurs (src/ga/registry.py) — étape 7a, Tristan.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche
``etape-7a-selection`` (voir TODO.md, 7a), sans MiniZinc :
    - ``register`` puis ``create`` : l'opérateur créé est du bon type et reçoit ses paramètres
      (ex. ``TournamentSelector`` avec ``size=3``) ; chaque ``create`` rend une nouvelle instance ;
    - ``names`` : noms triés ; registre vide ;
    - nom en double ⇒ ``DuplicateOperatorError`` ; nom inconnu ⇒ ``UnknownOperatorError``, qui cite le nom
      demandé et le nom du registre ;
    - deux registres distincts ne partagent pas leurs fabriques ;
    - ``check_compatibility`` : un opérateur de ``BlockEncoding`` avec ``BlockEncoding`` passe ; avec un encodage
      factice ⇒ ``IncompatibleOperatorError``, qui nomme l'opérateur et les deux encodages.
"""

import unittest

from src.ga.chromosome import BlockEncoding, BlockGenome, Encoding
from src.ga.operators import VariationOperator
from src.ga.registry import (
    DuplicateOperatorError,
    IncompatibleOperatorError,
    OperatorRegistry,
    RegistryError,
    UnknownOperatorError,
)
from src.ga.selection import SelectionDefaults, TournamentSelector, UniformMutableSelector
from src.model.horaire import Horaire

REGISTRY_NAME: str = "croisements"
OTHER_REGISTRY_NAME: str = "mutations"
SELECTOR_NAME: str = "tournoi"
OTHER_SELECTOR_NAME: str = "uniforme"
ALPHA_NAME: str = "alpha"
UNKNOWN_NAME: str = "inexistant"
TOURNAMENT_SIZE: int = 3
UNORDERED_NAMES: tuple[str, ...] = (SELECTOR_NAME, ALPHA_NAME, OTHER_SELECTOR_NAME)
SORTED_NAMES: tuple[str, ...] = (ALPHA_NAME, SELECTOR_NAME, OTHER_SELECTOR_NAME)


class DummyEncoding(Encoding[int]):
    """Encodage factice, différent de ``BlockEncoding``."""

    def encode(self, horaire: Horaire) -> int:
        raise NotImplementedError

    def decode(self, genome: int) -> Horaire:
        raise NotImplementedError


class BlockOperator(VariationOperator[BlockGenome]):
    """Opérateur factice qui manipule les génomes de ``BlockEncoding``."""

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding


def registry() -> OperatorRegistry:
    return OperatorRegistry(REGISTRY_NAME)


class TestScaffoldContract(unittest.TestCase):

    def test_givenRegistryName_whenConstructed_thenRegistryKeepsIt(self) -> None:
        self.assertEqual(OperatorRegistry(REGISTRY_NAME).name, REGISTRY_NAME)

    def test_givenRegistryErrors_whenCheckingHierarchy_thenEveryErrorIsARegistryError(self) -> None:
        for error in (DuplicateOperatorError, UnknownOperatorError, IncompatibleOperatorError):
            with self.subTest(error=error.__name__):
                self.assertTrue(issubclass(error, RegistryError))


class TestRegisterAndCreate(unittest.TestCase):

    def test_givenRegisteredClass_whenCreateWithParameters_thenInstanceHasRightTypeAndParameters(self) -> None:
        operators = registry()
        operators.register(SELECTOR_NAME, TournamentSelector)
        created = operators.create(SELECTOR_NAME, size=TOURNAMENT_SIZE)
        self.assertIsInstance(created, TournamentSelector)
        self.assertEqual(created.size, TOURNAMENT_SIZE)

    def test_givenRegisteredClass_whenCreateWithoutParameters_thenFactoryDefaultsApply(self) -> None:
        operators = registry()
        operators.register(SELECTOR_NAME, TournamentSelector)
        created = operators.create(SELECTOR_NAME)
        self.assertEqual(created.size, SelectionDefaults.TOURNAMENT_SIZE)

    def test_givenRegisteredFunction_whenCreate_thenFunctionReceivesParameters(self) -> None:
        operators = registry()
        operators.register(SELECTOR_NAME, lambda size: TournamentSelector(size=size))
        created = operators.create(SELECTOR_NAME, size=TOURNAMENT_SIZE)
        self.assertIsInstance(created, TournamentSelector)
        self.assertEqual(created.size, TOURNAMENT_SIZE)

    def test_givenRegisteredName_whenCreateTwice_thenEachCreateReturnsANewInstance(self) -> None:
        operators = registry()
        operators.register(SELECTOR_NAME, TournamentSelector)
        self.assertIsNot(operators.create(SELECTOR_NAME), operators.create(SELECTOR_NAME))

    def test_givenSeveralNames_whenCreate_thenEachNameUsesItsOwnFactory(self) -> None:
        operators = registry()
        operators.register(SELECTOR_NAME, TournamentSelector)
        operators.register(OTHER_SELECTOR_NAME, UniformMutableSelector)
        self.assertIsInstance(operators.create(SELECTOR_NAME), TournamentSelector)
        self.assertIsInstance(operators.create(OTHER_SELECTOR_NAME), UniformMutableSelector)

    def test_givenTwoRegistries_whenRegisterInOne_thenTheOtherIsUnaffected(self) -> None:
        operators = registry()
        other_operators = OperatorRegistry(OTHER_REGISTRY_NAME)
        operators.register(SELECTOR_NAME, TournamentSelector)
        self.assertEqual(other_operators.names(), ())
        with self.assertRaises(UnknownOperatorError):
            other_operators.create(SELECTOR_NAME)


class TestNames(unittest.TestCase):

    def test_givenEmptyRegistry_whenNames_thenReturnsEmptyTuple(self) -> None:
        self.assertEqual(registry().names(), ())

    def test_givenUnorderedRegistrations_whenNames_thenReturnsSortedTuple(self) -> None:
        operators = registry()
        for name in UNORDERED_NAMES:
            operators.register(name, TournamentSelector)
        self.assertEqual(operators.names(), SORTED_NAMES)


class TestRegistryErrors(unittest.TestCase):

    def test_givenDuplicateName_whenRegister_thenRaisesDuplicateOperatorErrorNamingOperatorAndRegistry(self) -> None:
        operators = registry()
        operators.register(SELECTOR_NAME, TournamentSelector)
        with self.assertRaises(DuplicateOperatorError) as context:
            operators.register(SELECTOR_NAME, UniformMutableSelector)
        error = context.exception
        self.assertEqual(error.operator_name, SELECTOR_NAME)
        self.assertEqual(error.registry_name, REGISTRY_NAME)
        self.assertIn(SELECTOR_NAME, str(error))
        self.assertIn(REGISTRY_NAME, str(error))

    def test_givenDuplicateName_whenRegister_thenOriginalFactoryIsKept(self) -> None:
        operators = registry()
        operators.register(SELECTOR_NAME, TournamentSelector)
        with self.assertRaises(DuplicateOperatorError):
            operators.register(SELECTOR_NAME, UniformMutableSelector)
        self.assertIsInstance(operators.create(SELECTOR_NAME), TournamentSelector)

    def test_givenUnknownName_whenCreate_thenRaisesUnknownOperatorErrorNamingRequestAndRegistry(self) -> None:
        with self.assertRaises(UnknownOperatorError) as context:
            registry().create(UNKNOWN_NAME)
        error = context.exception
        self.assertEqual(error.operator_name, UNKNOWN_NAME)
        self.assertEqual(error.registry_name, REGISTRY_NAME)
        self.assertIn(UNKNOWN_NAME, str(error))
        self.assertIn(REGISTRY_NAME, str(error))

    def test_givenUnknownName_whenCreate_thenMessageListsSortedKnownNames(self) -> None:
        operators = registry()
        operators.register(OTHER_SELECTOR_NAME, UniformMutableSelector)
        operators.register(ALPHA_NAME, TournamentSelector)
        expected_known = (ALPHA_NAME, OTHER_SELECTOR_NAME)
        with self.assertRaises(UnknownOperatorError) as context:
            operators.create(UNKNOWN_NAME)
        self.assertEqual(context.exception.known, expected_known)
        self.assertIn(f"{ALPHA_NAME}, {OTHER_SELECTOR_NAME}", str(context.exception))

    def test_givenEmptyRegistry_whenCreate_thenErrorKnownNamesAreEmpty(self) -> None:
        with self.assertRaises(UnknownOperatorError) as context:
            registry().create(UNKNOWN_NAME)
        self.assertEqual(context.exception.known, ())

    def test_givenUnknownName_whenCreate_thenErrorIsARegistryError(self) -> None:
        with self.assertRaises(RegistryError):
            registry().create(UNKNOWN_NAME)


class TestCheckCompatibility(unittest.TestCase):

    def test_givenBlockEncoding_whenCheckCompatibilityOfBlockOperator_thenPasses(self) -> None:
        OperatorRegistry.check_compatibility(BlockOperator(), BlockEncoding())

    def test_givenSubclassOfBlockEncoding_whenCheckCompatibility_thenPasses(self) -> None:
        class DerivedBlockEncoding(BlockEncoding):
            pass

        OperatorRegistry.check_compatibility(BlockOperator(), DerivedBlockEncoding())

    def test_givenDummyEncoding_whenCheckCompatibility_thenRaisesIncompatibleOperatorError(self) -> None:
        with self.assertRaises(IncompatibleOperatorError):
            OperatorRegistry.check_compatibility(BlockOperator(), DummyEncoding())

    def test_givenDummyEncoding_whenCheckCompatibility_thenErrorNamesOperatorAndBothEncodings(self) -> None:
        operator_name = BlockOperator.__name__
        expected_encoding_name = BlockEncoding.__name__
        actual_encoding_name = DummyEncoding.__name__
        with self.assertRaises(IncompatibleOperatorError) as context:
            OperatorRegistry.check_compatibility(BlockOperator(), DummyEncoding())
        error = context.exception
        self.assertEqual(error.operator_class, operator_name)
        self.assertEqual(error.expected_encoding, expected_encoding_name)
        self.assertEqual(error.actual_encoding, actual_encoding_name)
        for name in (operator_name, expected_encoding_name, actual_encoding_name):
            self.assertIn(name, str(error))

    def test_givenIncompatibleOperator_whenCheckCompatibility_thenErrorIsARegistryError(self) -> None:
        with self.assertRaises(RegistryError):
            OperatorRegistry.check_compatibility(BlockOperator(), DummyEncoding())


if __name__ == "__main__":
    unittest.main()