"""Tests du registre des opérateurs (src/ga/registry.py) — étape 7a, Tristan.

Sur ``main`` : tests de contrat du scaffold seulement (verts). Cas à couvrir sur la branche
``etape-7a-selection`` (voir TODO.md, 7a), sans MiniZinc :
    - ``register`` puis ``create`` : l'opérateur créé est du bon type et reçoit ses paramètres
      (ex. ``TournamentSelector`` avec ``size=3``) ; chaque ``create`` rend une nouvelle instance ;
    - ``names`` : noms triés ; registre vide ;
    - nom en double ⇒ ``DuplicateOperatorError`` ; nom inconnu ⇒ ``UnknownOperatorError``, qui cite le nom
      demandé et le nom du registre ;
    - ``check_compatibility`` : un opérateur de ``BlockEncoding`` avec ``BlockEncoding`` passe ; avec un encodage
      factice ⇒ ``IncompatibleOperatorError``, qui nomme l'opérateur et les deux encodages.
"""

import unittest

from src.ga.registry import (
    DuplicateOperatorError,
    IncompatibleOperatorError,
    OperatorRegistry,
    RegistryError,
    UnknownOperatorError,
)

REGISTRY_NAME: str = "croisements"


class TestScaffoldContract(unittest.TestCase):

    def test_registry_keeps_its_name(self) -> None:
        self.assertEqual(OperatorRegistry(REGISTRY_NAME).name, REGISTRY_NAME)

    def test_exception_hierarchy(self) -> None:
        for error in (DuplicateOperatorError, UnknownOperatorError, IncompatibleOperatorError):
            with self.subTest(error=error.__name__):
                self.assertTrue(issubclass(error, RegistryError))


if __name__ == "__main__":
    unittest.main()
