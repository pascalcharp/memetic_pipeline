"""Sélection : ``SelectParent`` et ``SelectMutable`` du pseudo-code (décisions D5 et D7).

Les sélecteurs tirent **par lot** (D7) : tous les individus d'une boucle NR ou NM sont tirés dans la population
avant de produire le moindre enfant. Ils comparent les individus sur ``cost.total`` (le coût à minimiser) ;
la population doit donc être entièrement évaluée.

Un sélecteur ne modifie jamais la population ni les individus. Le même individu peut être tiré plusieurs fois
(tirage avec remise). Le seul aléa provient du ``random.Random`` passé à chaque appel.
"""

import random
from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.ga.individual import Individu


class SelectionDefaults:
    """Paramètres par défaut et bornes des sélecteurs."""

    TOURNAMENT_SIZE: int = 2
    MIN_TOURNAMENT_SIZE: int = 1
    MIN_SELECTION_COUNT: int = 1


class SelectionMessages:
    """Gabarits des messages d'erreur de la sélection."""

    EMPTY_POPULATION: str = "Impossible de sélectionner dans une population vide."
    UNEVALUATED_INDIVIDUAL: str = "L'individu d'indice {index} n'est pas évalué : la sélection compare les coûts."
    INVALID_SELECTION_COUNT: str = "Le nombre d'individus à sélectionner doit être au moins {minimum} ; trouvé {value}."
    INVALID_TOURNAMENT_SIZE: str = "La taille du tournoi doit être au moins {minimum} ; trouvé {value}."


class SelectionError(Exception):
    """Erreur de base de la sélection."""


class EmptyPopulationError(SelectionError):
    """La population est vide."""


class UnevaluatedIndividualError(SelectionError):
    """Un individu de la population n'a pas de coût."""


class InvalidSelectionParameterError(SelectionError):
    """Un paramètre de sélection (nombre d'individus, taille du tournoi) est hors de son domaine."""


def check_selectable(population: Sequence[Individu], count: int) -> None:
    """Vérifications communes à tous les sélecteurs, à appeler au début de chaque ``select``.

    Raises:
        InvalidSelectionParameterError: si ``count < SelectionDefaults.MIN_SELECTION_COUNT``.
        EmptyPopulationError: si la population est vide.
        UnevaluatedIndividualError: si un individu n'est pas évalué (son indice est dans le message).
    """
    if count < SelectionDefaults.MIN_SELECTION_COUNT:
        raise InvalidSelectionParameterError(
            SelectionMessages.INVALID_SELECTION_COUNT.format(minimum=SelectionDefaults.MIN_SELECTION_COUNT, value=count)
        )
    if len(population) == 0:
        raise EmptyPopulationError(SelectionMessages.EMPTY_POPULATION)
    for index, individual in enumerate(population):
        if not individual.is_evaluated():
            raise UnevaluatedIndividualError(SelectionMessages.UNEVALUATED_INDIVIDUAL.format(index=index))


class ParentSelector[G](ABC):
    """``SelectParent`` : tire les parents des croisements d'une boucle NR."""

    @abstractmethod
    def select(self, population: Sequence[Individu[G]], count: int, rng: random.Random) -> tuple[Individu[G], ...]:
        """``count`` parents tirés dans ``population``, avec remise.

        Raises:
            voir ``check_selectable``.
        """


class MutableSelector[G](ABC):
    """``SelectMutable`` : tire les individus à muter d'une boucle NM."""

    @abstractmethod
    def select(self, population: Sequence[Individu[G]], count: int, rng: random.Random) -> tuple[Individu[G], ...]:
        """``count`` individus à muter tirés dans ``population``, avec remise.

        Raises:
            voir ``check_selectable``.
        """


# ---------------------------------------------------------------------------------------------------------------------
# Implémentations (à écrire, étape 7a)
# ---------------------------------------------------------------------------------------------------------------------

class TournamentSelector[G](ParentSelector[G]):
    """Sélection par tournoi : pour chaque parent, tire ``size`` individus au hasard (avec remise) et retient
    celui de plus faible ``cost.total``. Un tournoi de taille 1 est un tirage uniforme.
    """

    def __init__(self, size: int = SelectionDefaults.TOURNAMENT_SIZE) -> None:
        """
        Raises:
            InvalidSelectionParameterError: si ``size < SelectionDefaults.MIN_TOURNAMENT_SIZE``.
        """
        if size < SelectionDefaults.MIN_TOURNAMENT_SIZE:
            raise InvalidSelectionParameterError(
                SelectionMessages.INVALID_TOURNAMENT_SIZE.format(minimum=SelectionDefaults.MIN_TOURNAMENT_SIZE, value=size)
            )
        self.size = size

    def select(self, population: Sequence[Individu[G]], count: int, rng: random.Random) -> tuple[Individu[G], ...]:
        raise NotImplementedError  # Étape 7a (Tristan)


class UniformMutableSelector[G](MutableSelector[G]):
    """Tirage uniforme des individus à muter, sans regard au coût."""

    def select(self, population: Sequence[Individu[G]], count: int, rng: random.Random) -> tuple[Individu[G], ...]:
        raise NotImplementedError  # Étape 7a (Tristan)
