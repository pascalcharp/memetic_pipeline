"""Gestion de la population : ``SelectPop``, convergence et ``Restart`` du pseudo-code (décision D4).

Après les boucles NR et NM, la population contient μ parents et λ nouveaux individus, tous évalués.
``SurvivorSelector`` la ramène à μ individus ; ``ConvergenceCriterion`` dit si elle a convergé ; ``RestartPolicy``
la régénère alors en gardant une élite.

D4 (tranchée le 2026-11-16) :
    - remplacement : (μ+λ) sans doublons. Tri stable par ``cost.total`` croissant, un seul exemplaire de chaque
      génome identique, les μ meilleurs ; s'il y a moins de μ génomes distincts, on complète avec des doublons,
      dans l'ordre des coûts. Le meilleur individu n'est jamais perdu ;
    - variante « peine de mort » : les faisables d'abord (sans doublons), puis les meilleurs infaisables
      selon ``cost.total`` pour compléter à μ ;
    - convergence : le coût du meilleur n'a pas baissé depuis G générations ;
    - restart : on garde les k meilleurs et on régénère le reste avec le ``PopulationInitializer`` (étape 6).

Les stratégies ne modifient jamais la population reçue ni ses individus (D7) : elles rendent un nouveau tuple.
"""

import random
from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.ga.individual import Individu
from src.ga.initialization import PopulationInitializer
from src.model.evaluation import CostEvaluator, CostBreakdown

from itertools import cycle, islice


class PopulationDefaults:
    """Paramètres par défaut et bornes de la gestion de la population (D4)."""

    # Nombre de générations sans baisse du coût du meilleur avant de déclarer la convergence (G de D4).
    STAGNATION_GENERATIONS: int = 10
    MIN_STAGNATION_GENERATIONS: int = 1

    # Nombre de meilleurs individus gardés au restart (k de D4). Au moins 1 : le meilleur n'est jamais perdu.
    RESTART_ELITE_COUNT: int = 1
    MIN_RESTART_ELITE_COUNT: int = 1


class PopulationMessages:
    """Gabarits des messages d'erreur de la gestion de la population."""

    INVALID_STAGNATION_GENERATIONS: str = (
        "Le nombre de générations de stagnation doit être au moins {minimum} ; trouvé {value}."
    )
    INVALID_ELITE_COUNT: str = "La taille de l'élite gardée au restart doit être au moins {minimum} ; trouvé {value}."
    ELITE_LARGER_THAN_POPULATION: str = (
        "L'élite gardée au restart ({elite_count} individus) dépasse la taille de la population ({size})."
    )


class PopulationError(Exception):
    """Erreur de base de la gestion de la population."""


class InvalidPopulationParameterError(PopulationError):
    """Un paramètre de la gestion de la population (stagnation, élite) est hors de son domaine."""


# ---------------------------------------------------------------------------------------------------------------------
# Interfaces
# ---------------------------------------------------------------------------------------------------------------------

class SurvivorSelector[G](ABC):
    """``SelectPop`` : ramène la population (parents et nouveaux individus) à ``size`` individus."""

    @abstractmethod
    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        """Les ``size`` survivants de ``population`` ; ``population`` n'est pas modifiée.

        Raises:
            voir ``src.ga.selection.check_selectable`` (taille invalide, population vide, individu non évalué).
        """


class ConvergenceCriterion[G](ABC):
    """Dit si la population a convergé. Appelé une fois par génération, après ``SelectPop``.

    Un critère peut garder un état d'une génération à l'autre (par exemple le meilleur coût vu et depuis quand) ;
    ``reset`` l'efface après un restart.
    """

    @abstractmethod
    def has_converged(self, population: Sequence[Individu[G]]) -> bool:
        """Vrai si ``population`` (évaluée, après ``SelectPop``) a convergé."""

    @abstractmethod
    def reset(self) -> None:
        """Oublie l'historique : appelé après un restart."""


class RestartPolicy[G](ABC):
    """``Restart`` : régénère une population qui a convergé."""

    @abstractmethod
    def restart(self, population: Sequence[Individu[G]], rng: random.Random) -> tuple[Individu[G], ...]:
        """Nouvelle population évaluée, de même taille que ``population`` ; ``population`` n'est pas modifiée."""


# ---------------------------------------------------------------------------------------------------------------------
# Implémentations (à écrire, étape 8)
# ---------------------------------------------------------------------------------------------------------------------

class PlusSurvivorSelector[G](SurvivorSelector[G]):
    """(μ+λ) sans doublons (D4) : tri stable par ``cost.total`` croissant, un seul exemplaire de chaque génome
    identique, les ``size`` meilleurs. S'il y a moins de ``size`` génomes distincts, complète avec des doublons,
    dans l'ordre des coûts.
    """

    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        if size == 0 or len(population) == 0:
            return tuple()
        ordered_sequence: Sequence[Individu[G]] = sorted(population, key=lambda individu: individu.cost.total)
        if len(ordered_sequence) == 0:
            return tuple()
        if size == 1:
            return (ordered_sequence[0],)
        unique: list[Individu[G]] = [ordered_sequence[0]]
        for individu in ordered_sequence:
            if individu not in unique:
                unique.append(individu)
            if len(unique) == size:
                return tuple(unique)
        missing: int = size - len(unique)
        unique.extend(islice(cycle(unique), missing))
        return tuple(unique)


class DeathPenaltySurvivorSelector[G](SurvivorSelector[G]):
    """Variante « peine de mort » (D4) : les individus faisables (``cost.is_feasible``) d'abord, sans doublons et
    par ``cost.total`` croissant ; s'il en reste moins de ``size``, complète avec les meilleurs infaisables selon
    ``cost.total``.
    """

    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        if size == 0 or len(population) == 0:
            return tuple()
        ordered_sequence: Sequence[Individu[G]] = sorted(population, key=lambda individu: (not individu.cost.is_feasible, individu.cost.total))
        if len(ordered_sequence) == 0:
            return tuple()
        if size == 1:
            return (ordered_sequence[0],)
        unique: list[Individu[G]] = [ordered_sequence[0]]
        for individu in ordered_sequence:
            if individu not in unique:
                unique.append(individu)
            if len(unique) == size:
                return tuple(unique)
        return tuple(unique)


class StagnationCriterion[G](ConvergenceCriterion[G]):
    """Convergence quand le coût du meilleur individu n'a pas baissé depuis ``generations`` générations (D4)."""

    def __init__(self, generations: int = PopulationDefaults.STAGNATION_GENERATIONS) -> None:
        """
        Raises:
            InvalidPopulationParameterError: si ``generations < PopulationDefaults.MIN_STAGNATION_GENERATIONS``.
        """
        if generations < PopulationDefaults.MIN_STAGNATION_GENERATIONS:
            raise InvalidPopulationParameterError(PopulationMessages.INVALID_STAGNATION_GENERATIONS.format(
                minimum=PopulationDefaults.MIN_STAGNATION_GENERATIONS, value=generations
            ))
        self.generations = generations
        self._best_cost: int | None = None
        self._count: int = 0

    def has_converged(self, population: Sequence[Individu[G]]) -> bool:
        self._update_convergence(min(individu.cost.total for individu in population))
        return self._count >= self.generations            

    def reset(self) -> None:
        self._best_cost = None
        self._count = 0

    def _update_convergence(self, best_cost: int) -> None:
        if self._best_cost is None:
            self._best_cost = best_cost
            self._count = 0
            return
        if self._best_cost > best_cost:
            self._best_cost = best_cost
            self._count = 0
        else:
            self._count += 1


class EliteRestart[G](RestartPolicy[G]):
    """Restart (D4) : garde les ``elite_count`` meilleurs individus (``cost.total``) et régénère le reste avec
    ``initializer`` ; les nouveaux individus sont évalués par ``evaluator``. Pour qu'ils passent aussi par le
    ``LocalSolver``, construire ``initializer`` avec son option ``local_solver`` (étape 6).

    Raises (``restart``):
        InvalidPopulationParameterError: si ``elite_count`` dépasse la taille de la population.
    """

    def __init__(
            self,
            initializer: PopulationInitializer[G],
            evaluator: CostEvaluator,
            elite_count: int = PopulationDefaults.RESTART_ELITE_COUNT,
    ) -> None:
        """
        Raises:
            InvalidPopulationParameterError: si ``elite_count < PopulationDefaults.MIN_RESTART_ELITE_COUNT``.
        """
        if elite_count < PopulationDefaults.MIN_RESTART_ELITE_COUNT:
            raise InvalidPopulationParameterError(PopulationMessages.INVALID_ELITE_COUNT.format(
                minimum=PopulationDefaults.MIN_RESTART_ELITE_COUNT, value=elite_count
            ))
        self.initializer = initializer
        self.evaluator = evaluator
        self.elite_count = elite_count

    def restart(self, population: Sequence[Individu[G]], rng: random.Random) -> tuple[Individu[G], ...]:
        if self.elite_count > len(population):
            raise InvalidPopulationParameterError(PopulationMessages.ELITE_LARGER_THAN_POPULATION.format(
                elite_count=self.elite_count, size=len(population)
            ))
        if (len(population) == self.elite_count):
            return tuple(population)
        new_population: list[Individu[G]] = sorted(population, key= lambda individu: individu.cost.total)[:self.elite_count]
        new_individus: tuple[Individu[G], ...] = self.initializer.initialize(len(population) - self.elite_count, rng)
        for individu in new_individus:
            cost: CostBreakdown = self.evaluator.evaluate(individu.horaire)
            individu_with_cost: Individu[G] = individu.with_cost(cost)
            new_population.append(individu_with_cost)
        return tuple(new_population)
