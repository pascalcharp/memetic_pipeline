"""Critère d'arrêt : ``terminé(P)`` du pseudo-code."""

from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.ga.individual import Individu


class TerminationDefaults:
    """Bornes des critères d'arrêt."""

    MIN_GENERATIONS: int = 1


class TerminationMessages:
    """Gabarits des messages d'erreur des critères d'arrêt."""

    INVALID_GENERATIONS: str = "Le nombre de générations doit être au moins {minimum} ; trouvé {value}."


class TerminationError(Exception):
    """Erreur de base des critères d'arrêt."""


class InvalidTerminationParameterError(TerminationError):
    """Un paramètre de critère d'arrêt est hors de son domaine."""


class TerminationCriterion[G](ABC):
    """Dit si l'exécution est terminée. Appelé une fois par génération, après ``SelectPop`` et un éventuel restart."""

    @abstractmethod
    def is_done(self, generation: int, population: Sequence[Individu[G]]) -> bool:
        """Vrai si l'exécution doit s'arrêter après la génération ``generation`` (la génération 0 est
        l'initialisation) ; ``population`` est la population courante, évaluée."""


class GenerationLimit[G](TerminationCriterion[G]):
    """Arrêt après ``maximum_generations`` générations (sans compter l'initialisation)."""

    def __init__(self, maximum_generations: int) -> None:
        """
        Raises:
            InvalidTerminationParameterError: si ``maximum_generations < TerminationDefaults.MIN_GENERATIONS``.
        """
        if maximum_generations < TerminationDefaults.MIN_GENERATIONS:
            raise InvalidTerminationParameterError(TerminationMessages.INVALID_GENERATIONS.format(
                minimum=TerminationDefaults.MIN_GENERATIONS, value=maximum_generations
            ))
        self.maximum_generations = maximum_generations

    def is_done(self, generation: int, population: Sequence[Individu[G]]) -> bool:
        return self.maximum_generations <= generation
