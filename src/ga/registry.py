"""Registre des opérateurs par nom (décision D5).

Une expérience décrit ses stratégies par leur **nom** dans un fichier de configuration (étape 10), par exemple
``{"crossover": "uniform_gene", "mutation": "activity"}``. Le registre associe chaque nom à une **fabrique**
(une classe ou une fonction) et crée l'opérateur à partir de ses paramètres.

On utilise un registre par rôle : un pour les croisements, un pour les mutations, un pour les sélecteurs, etc.
Le registre vérifie aussi, à l'assemblage, qu'un opérateur de variation est compatible avec l'encodage choisi :
une incompatibilité est découverte avant l'exécution, pas au milieu (``IncompatibleOperatorError``).
"""

from collections.abc import Callable
from typing import Any

from src.ga.chromosome import Encoding
from src.ga.operators import VariationOperator


class RegistryMessages:
    """Gabarits des messages d'erreur du registre."""

    DUPLICATE_NAME: str = "Le registre {registry} contient déjà un opérateur nommé « {name} »."
    UNKNOWN_NAME: str = "Le registre {registry} ne contient aucun opérateur nommé « {name} » ; noms connus : {known}."
    INCOMPATIBLE_OPERATOR: str = (
        "L'opérateur {operator} manipule des génomes de {expected} ; il est incompatible avec l'encodage {found}."
    )


class RegistryError(Exception):
    """Erreur de base du registre des opérateurs."""


class DuplicateOperatorError(RegistryError):
    """Un nom est déjà enregistré."""


class UnknownOperatorError(RegistryError):
    """Aucun opérateur n'est enregistré sous ce nom."""


class IncompatibleOperatorError(RegistryError):
    """L'opérateur de variation ne manipule pas les génomes de l'encodage choisi (D5)."""


class OperatorRegistry:
    """Associe des noms à des fabriques d'opérateurs d'un même rôle (D5).

    ``name`` identifie le registre dans les messages d'erreur (par exemple ``"croisements"``).
    """

    def __init__(self, name: str) -> None:
        self.name = name

    def register(self, operator_name: str, factory: Callable[..., Any]) -> None:
        """Enregistre ``factory`` sous ``operator_name``.

        Raises:
            DuplicateOperatorError: si ``operator_name`` est déjà enregistré.
        """
        raise NotImplementedError  # Étape 7a (Tristan)

    def names(self) -> tuple[str, ...]:
        """Noms enregistrés, triés."""
        raise NotImplementedError  # Étape 7a (Tristan)

    def create(self, operator_name: str, **parameters: Any) -> Any:
        """Nouvel opérateur, créé par la fabrique de ``operator_name`` avec ``parameters``.

        Raises:
            UnknownOperatorError: si ``operator_name`` n'est pas enregistré (les noms connus sont dans le message).
        """
        raise NotImplementedError  # Étape 7a (Tristan)

    @staticmethod
    def check_compatibility(operator: VariationOperator, encoding: Encoding) -> None:
        """Vérifie que ``operator`` manipule les génomes de ``encoding`` (``VariationOperator.is_compatible_with``).

        Raises:
            IncompatibleOperatorError: sinon ; le message nomme l'opérateur, son encodage et l'encodage reçu.
        """
        raise NotImplementedError  # Étape 7a (Tristan)
