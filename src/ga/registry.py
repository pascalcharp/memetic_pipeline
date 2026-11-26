"""Registre des opérateurs par nom (décision D5).

Une expérience décrit ses stratégies par leur **nom** dans un fichier de configuration (étape 10), par exemple
``{"crossover": "uniform_gene", "mutation": "activity"}``. Le registre associe chaque nom à une **fabrique**
(une classe ou une fonction) et crée l'opérateur à partir de ses paramètres.

On utilise un registre par rôle : un pour les croisements, un pour les mutations, un pour les sélecteurs, etc.
Le registre vérifie aussi, à l'assemblage, qu'un opérateur de variation est compatible avec l'encodage choisi :
une incompatibilité est découverte avant l'exécution, pas au milieu (``IncompatibleOperatorError``).
"""

import inspect
from collections.abc import Callable, Iterable, Mapping
from typing import Any

from src.ga.chromosome import Encoding
from src.ga.operators import VariationOperator


class RegistryMessages:
    """Gabarits des messages d'erreur du registre."""

    DUPLICATE_NAME: str = "Le registre {registry} contient déjà un opérateur nommé « {name} »."
    UNKNOWN_NAME: str = "Le registre {registry} ne contient aucun opérateur nommé « {name} » ; noms connus : {known}."
    INVALID_PARAMETERS: str = (
        "Paramètres {parameters} invalides pour l'opérateur « {name} » du registre {registry} : {detail}."
    )
    INCOMPATIBLE_OPERATOR: str = (
        "L'opérateur {operator} manipule des génomes de {expected} ; il est incompatible avec l'encodage {found}."
    )


class RegistryError(Exception):
    """Erreur de base du registre des opérateurs."""


class DuplicateOperatorError(RegistryError):
    """Un nom est déjà enregistré."""
    def __init__(self, registry_name: str, operator_name: str) -> None:
        self.registry_name = registry_name
        self.operator_name = operator_name
        super().__init__(RegistryMessages.DUPLICATE_NAME.format(registry=registry_name, name=operator_name))


class UnknownOperatorError(RegistryError):
    """Aucun opérateur n'est enregistré sous ce nom."""
    def __init__(self, registry_name: str, operator_name: str, known: Iterable[str]) -> None:
        self.registry_name = registry_name
        self.operator_name = operator_name
        self.known = tuple(sorted(known))
        super().__init__(RegistryMessages.UNKNOWN_NAME.format(
            registry=registry_name,
            name=operator_name,
            known=", ".join(self.known)
        ))


class InvalidOperatorParametersError(RegistryError):
    """Les paramètres ne conviennent pas à la fabrique de l'opérateur : paramètre inattendu ou paramètre obligatoire
    absent (étape 10c)."""
    def __init__(self, registry_name: str, operator_name: str, parameters: Mapping[str, Any], detail: str) -> None:
        self.registry_name = registry_name
        self.operator_name = operator_name
        self.parameters = dict(parameters)
        super().__init__(RegistryMessages.INVALID_PARAMETERS.format(
            parameters=self.parameters,
            name=operator_name,
            registry=registry_name,
            detail=detail,
        ))


class IncompatibleOperatorError(RegistryError):
    """L'opérateur de variation ne manipule pas les génomes de l'encodage choisi (D5)."""
    def __init__(self, operator: VariationOperator, encoding: Encoding) -> None:
        self.operator_class: str = operator.__class__.__name__
        self.expected_encoding: str = operator.encoding_type().__name__
        self.actual_encoding = encoding.__class__.__name__
        super().__init__(RegistryMessages.INCOMPATIBLE_OPERATOR.format(
            operator=self.operator_class,
            expected=self.expected_encoding,
            found=self.actual_encoding
        ))


class OperatorRegistry:
    """Associe des noms à des fabriques d'opérateurs d'un même rôle (D5).

    ``name`` identifie le registre dans les messages d'erreur (par exemple ``"croisements"``).
    """

    def __init__(self, name: str) -> None:
        self.name = name
        self._factories: dict[str, Callable[..., Any]] = {}

    def register(self, operator_name: str, factory: Callable[..., Any]) -> None:
        """Enregistre ``factory`` sous ``operator_name``.

        Raises:
            DuplicateOperatorError: si ``operator_name`` est déjà enregistré.
        """
        if operator_name in self._factories:
            raise DuplicateOperatorError(self.name, operator_name)

        self._factories[operator_name] = factory

    def names(self) -> tuple[str, ...]:
        """Noms enregistrés, triés."""
        return tuple(sorted(self._factories.keys()))

    def create(self, operator_name: str, **parameters: Any) -> Any:
        """Nouvel opérateur, créé par la fabrique de ``operator_name`` avec ``parameters``.

        Raises:
            UnknownOperatorError: si ``operator_name`` n'est pas enregistré (les noms connus sont dans le message).
        """
        return self.factory(operator_name)(**parameters)

    def factory(self, operator_name: str) -> Callable[..., Any]:
        """La fabrique enregistrée sous ``operator_name``.

        Raises:
            UnknownOperatorError: si ``operator_name`` n'est pas enregistré (les noms connus sont dans le message).
        """
        if operator_name not in self._factories:
            raise UnknownOperatorError(self.name, operator_name, self._factories.keys())
        return self._factories[operator_name]

    def check_parameters(self, operator_name: str, **parameters: Any) -> None:
        """Vérifie, sans créer l'opérateur, que ``parameters`` conviennent à la fabrique de ``operator_name`` : aucun
        paramètre inattendu, aucun paramètre obligatoire absent. Les valeurs, elles, ne sont vérifiées qu'à la création.

        Raises:
            UnknownOperatorError: si ``operator_name`` n'est pas enregistré.
            InvalidOperatorParametersError: si les paramètres ne conviennent pas ; le message nomme l'opérateur, le
                registre et le paramètre en cause.
        """
        factory = self.factory(operator_name)
        try:
            inspect.signature(factory).bind(**parameters)
        except TypeError as error:
            raise InvalidOperatorParametersError(self.name, operator_name, parameters, str(error)) from error

    @staticmethod
    def check_compatibility(operator: VariationOperator, encoding: Encoding) -> None:
        """Vérifie que ``operator`` manipule les génomes de ``encoding`` (``VariationOperator.is_compatible_with``).

        Raises:
            IncompatibleOperatorError: sinon ; le message nomme l'opérateur, son encodage et l'encodage reçu.
        """
        if not operator.is_compatible_with(encoding):
            raise IncompatibleOperatorError(operator, encoding)
