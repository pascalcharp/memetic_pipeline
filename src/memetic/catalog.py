"""Catalogue des stratégies choisies par leur nom (étape 10c, D5).

Une expérience décrit ses stratégies par leur **nom**, dans son fichier de configuration :

    "strategies": {"crossover": "uniform_gene", "mutation": {"name": "activity", "parameters": {}}}

Le catalogue tient un registre (``OperatorRegistry``, étape 7a) par **rôle** du pseudo-code. Chaque nom y est associé
à une fabrique, qui reçoit le **contexte de construction** (``BuildContext`` : l'instance et l'encodage, qui ne
viennent pas du fichier de configuration) et les paramètres du choix. Les noms sont stables : ils figurent dans les
configurations et dans les fichiers de résultats ; ils ne dépendent pas du nom des classes.

Rôles couverts : le croisement et la mutation. Les autres rôles (sélecteurs, survivants, restart, voisinage) suivront
le même patron : un nom dans ``StrategyRoles``, un registre dans ``StrategyCatalog``, un champ dans
``StrategyChoices``.
"""

from collections.abc import Callable, Mapping
from dataclasses import dataclass, field
from typing import Any

from src.ga.baselines import RandomGenomeCrossover, RandomGenomeMutation
from src.ga.chromosome import BlockEncoding, Encoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.operators import (
    ActivityMutation,
    BlockBoundaryMutation,
    Crossover,
    Mutation,
    ShiftStartMutation,
    UniformGeneCrossover,
)
from src.ga.registry import OperatorRegistry
from src.utils.io import ProblemInstance


class StrategyRoles:
    """Rôles du pseudo-code que le catalogue sait construire ; ce sont aussi les clés de ``strategies``."""

    CROSSOVER: str = "crossover"
    MUTATION: str = "mutation"
    ALL: tuple[str, ...] = (CROSSOVER, MUTATION)


class StrategyNames:
    """Noms stables des stratégies, tels qu'écrits dans les configurations et les résultats."""

    # Croisements
    UNIFORM_GENE: str = "uniform_gene"
    # Mutations
    SHIFT_START: str = "shift_start"
    BLOCK_BOUNDARY: str = "block_boundary"
    ACTIVITY: str = "activity"
    # Témoin (étape 10d), pour les deux rôles : un génome aléatoire neuf, sans hériter des parents
    RANDOM_GENOME: str = "random_genome"


class StrategyKeys:
    """Clés de la forme objet d'un choix : ``{"name": ..., "parameters": {...}}``."""

    NAME: str = "name"
    PARAMETERS: str = "parameters"
    ALLOWED: tuple[str, ...] = (NAME, PARAMETERS)


class CatalogDefaults:
    """Choix par défaut (ceux de l'assemblage de référence) et nom des registres."""

    CROSSOVER: str = StrategyNames.UNIFORM_GENE
    MUTATION: str = StrategyNames.SHIFT_START
    # Nom réservé : chaque fabrique reçoit le contexte de construction sous ce nom, en plus des paramètres du choix.
    CONTEXT_PARAMETER: str = "context"
    REGISTRY_NAMES: dict[str, str] = {
        StrategyRoles.CROSSOVER: "croisements",
        StrategyRoles.MUTATION: "mutations",
    }


class CatalogMessages:
    """Gabarits des messages d'erreur du catalogue."""

    UNKNOWN_ROLE: str = "Rôle de stratégie « {role} » inconnu ; rôles connus : {known}."
    BLOCK_ENCODING_REQUIRED: str = "La stratégie « {name} » tire des génomes de BlockEncoding ; encodage reçu : {encoding}."
    RESERVED_PARAMETER: str = (
        "Le paramètre « {parameter} » de la stratégie « {name} » ({role}) est réservé : le catalogue y passe le "
        "contexte de construction."
    )


class StrategyError(Exception):
    """Erreur de base du catalogue des stratégies."""


class UnknownStrategyRoleError(StrategyError):
    """Le catalogue ne connaît pas ce rôle."""


class IncompatibleStrategyEncodingError(StrategyError):
    """La stratégie ne sait pas construire de génomes pour l'encodage du contexte."""


class ReservedStrategyParameterError(StrategyError):
    """Un choix donne un paramètre au nom réservé au contexte de construction."""


@dataclass(frozen=True)
class BuildContext:
    """Ce dont les fabriques ont besoin et qui ne vient pas du fichier de configuration."""

    instance: ProblemInstance
    encoding: Encoding


@dataclass(frozen=True)
class StrategyChoice:
    """Une stratégie choisie par son nom, avec les paramètres de sa fabrique (aucun par défaut)."""

    name: str
    parameters: Mapping[str, Any] = field(default_factory=dict)

    def to_json(self) -> dict[str, Any]:
        return {StrategyKeys.NAME: self.name, StrategyKeys.PARAMETERS: dict(self.parameters)}


@dataclass(frozen=True)
class StrategyChoices:
    """Une stratégie par rôle. Les valeurs par défaut redonnent l'assemblage de référence."""

    crossover: StrategyChoice = field(default_factory=lambda: StrategyChoice(CatalogDefaults.CROSSOVER))
    mutation: StrategyChoice = field(default_factory=lambda: StrategyChoice(CatalogDefaults.MUTATION))

    def by_role(self) -> dict[str, StrategyChoice]:
        """Le choix de chaque rôle, dans l'ordre de ``StrategyRoles.ALL``."""
        return {StrategyRoles.CROSSOVER: self.crossover, StrategyRoles.MUTATION: self.mutation}

    def to_json(self) -> dict[str, dict[str, Any]]:
        return {role: choice.to_json() for role, choice in self.by_role().items()}


# ---------------------------------------------------------------------------------------------------------------------
# Fabriques : une par nom ; chacune reçoit le contexte de construction et les paramètres du choix
# ---------------------------------------------------------------------------------------------------------------------

def uniform_gene_crossover(context: BuildContext) -> UniformGeneCrossover:
    return UniformGeneCrossover()


def shift_start_mutation(context: BuildContext) -> ShiftStartMutation:
    return ShiftStartMutation(context.instance)


def block_boundary_mutation(context: BuildContext) -> BlockBoundaryMutation:
    return BlockBoundaryMutation()


def activity_mutation(context: BuildContext) -> ActivityMutation:
    return ActivityMutation(context.instance)


def random_genome_generator(context: BuildContext) -> RandomBlockInitializer:
    """Le tireur de génomes aléatoires des opérateurs témoins : sans LocalSolver, le moteur s'en charge."""
    if not isinstance(context.encoding, BlockEncoding):
        raise IncompatibleStrategyEncodingError(CatalogMessages.BLOCK_ENCODING_REQUIRED.format(
            name=StrategyNames.RANDOM_GENOME, encoding=type(context.encoding).__name__
        ))
    return RandomBlockInitializer(context.instance, context.encoding)


def random_genome_crossover(context: BuildContext) -> RandomGenomeCrossover:
    return RandomGenomeCrossover(random_genome_generator(context))


def random_genome_mutation(context: BuildContext) -> RandomGenomeMutation:
    return RandomGenomeMutation(random_genome_generator(context))


CROSSOVER_FACTORIES: dict[str, Callable[..., Crossover]] = {
    StrategyNames.UNIFORM_GENE: uniform_gene_crossover,
    StrategyNames.RANDOM_GENOME: random_genome_crossover,
}
MUTATION_FACTORIES: dict[str, Callable[..., Mutation]] = {
    StrategyNames.SHIFT_START: shift_start_mutation,
    StrategyNames.BLOCK_BOUNDARY: block_boundary_mutation,
    StrategyNames.ACTIVITY: activity_mutation,
    StrategyNames.RANDOM_GENOME: random_genome_mutation,
}


class StrategyCatalog:
    """Un registre par rôle, rempli avec les stratégies disponibles.

    Chaque catalogue a ses propres registres : en créer un ne modifie aucun état global.
    """

    def __init__(self) -> None:
        factories_by_role = {
            StrategyRoles.CROSSOVER: CROSSOVER_FACTORIES,
            StrategyRoles.MUTATION: MUTATION_FACTORIES,
        }
        self._registries: dict[str, OperatorRegistry] = {}
        for role, factories in factories_by_role.items():
            registry = OperatorRegistry(CatalogDefaults.REGISTRY_NAMES[role])
            for name, factory in factories.items():
                registry.register(name, factory)
            self._registries[role] = registry

    def roles(self) -> tuple[str, ...]:
        return StrategyRoles.ALL

    def names(self, role: str) -> tuple[str, ...]:
        """Les noms disponibles pour ``role``, triés.

        Raises:
            UnknownStrategyRoleError: si ``role`` est inconnu.
        """
        return self.registry(role).names()

    def registry(self, role: str) -> OperatorRegistry:
        """Le registre de ``role``.

        Raises:
            UnknownStrategyRoleError: si ``role`` est inconnu ; les rôles connus sont dans le message.
        """
        if role not in self._registries:
            raise UnknownStrategyRoleError(CatalogMessages.UNKNOWN_ROLE.format(role=role, known=", ".join(self.roles())))
        return self._registries[role]

    def check(self, role: str, choice: StrategyChoice) -> None:
        """Vérifie ``choice`` sans créer la stratégie (donc sans instance) : rôle et nom connus, paramètres qui
        conviennent à la fabrique.

        Raises:
            UnknownStrategyRoleError: si ``role`` est inconnu.
            UnknownOperatorError: si le nom est inconnu ; les noms connus sont dans le message.
            ReservedStrategyParameterError: si un paramètre porte le nom réservé au contexte.
            InvalidOperatorParametersError: si les paramètres ne conviennent pas à la fabrique.
        """
        registry = self.registry(role)
        if CatalogDefaults.CONTEXT_PARAMETER in choice.parameters:
            raise ReservedStrategyParameterError(CatalogMessages.RESERVED_PARAMETER.format(
                parameter=CatalogDefaults.CONTEXT_PARAMETER, name=choice.name, role=role
            ))
        # Le contexte n'est pas connu ici : seule sa présence compte pour vérifier la signature.
        registry.check_parameters(choice.name, **{CatalogDefaults.CONTEXT_PARAMETER: None}, **choice.parameters)

    def check_all(self, choices: StrategyChoices) -> None:
        """``check`` pour chaque rôle de ``choices``."""
        for role, choice in choices.by_role().items():
            self.check(role, choice)

    def create(self, role: str, choice: StrategyChoice, context: BuildContext) -> Any:
        """Nouvelle stratégie de ``role``, créée par la fabrique de ``choice.name`` avec ``context`` et les
        paramètres du choix.

        Raises:
            les mêmes exceptions que ``check``.
        """
        self.check(role, choice)
        return self.registry(role).create(choice.name, **{CatalogDefaults.CONTEXT_PARAMETER: context}, **choice.parameters)
