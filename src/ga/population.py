"""Gestion de la population : ``SelectPop``, convergence et ``Restart`` du pseudo-code (décision D4).

Après les boucles NR et NM, la population contient μ parents et λ nouveaux individus, tous évalués.
``SurvivorSelector`` la ramène à μ individus ; ``ConvergenceCriterion`` dit si elle a convergé ; ``RestartPolicy``
la régénère alors en gardant une élite.

D4 (tranchée le 2026-11-16 et 2026-11-21, précisée à la révision de l'étape 8) :
    - remplacement : (μ+λ) sans doublons. Tri stable par ``cost.total`` croissant, un seul exemplaire de chaque
      génome identique, les μ meilleurs ; s'il y a moins de μ génomes distincts, on complète avec les doublons
      écartés, dans l'ordre des coûts. Le meilleur individu n'est jamais perdu ;
    - variante « peine de mort » : les faisables d'abord (sans doublons), puis les meilleurs infaisables
      selon ``cost.total`` pour compléter à μ. S'il manque encore des individus, même complément par les doublons
      écartés (faisables d'abord). Les deux sélecteurs suivent donc la même règle de complétion ;
    - convergence : le coût du meilleur n'a pas baissé depuis G générations ;
    - restart : on garde jusqu'à k meilleurs individus distincts et on régénère le reste avec le
      ``PopulationInitializer`` (étape 6). Pas de complément par des doublons pour l'élite : s'il y a moins de k
      génomes distincts, on en garde moins et on en régénère davantage, la taille de la population est conservée.

Les stratégies ne modifient jamais la population reçue ni ses individus (D7) : elles rendent un nouveau tuple.
"""

import random
from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.ga.individual import Individu
from src.ga.initialization import PopulationInitializer
from src.ga.selection import check_selectable
from src.model.evaluation import CostBreakdown, CostEvaluator


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
    INVALID_STAGNATION_POPULATION: str = "La population ne doit pas être vide."


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
# Implémentations 
# ---------------------------------------------------------------------------------------------------------------------

def _distinct_by_cost[G](
        ordered: Sequence[Individu[G]],
        size: int,
        *,
        fill_duplicates: bool = False,
) -> tuple[Individu[G], ...]:
    """Les ``size`` premiers individus de ``ordered`` en un seul exemplaire par génome (égalité d'``Individu``).

    ``ordered`` est déjà trié par ordre de préférence : l'ordre est conservé. Si ``ordered`` compte moins de
    ``size`` génomes distincts :
        - ``fill_duplicates`` faux : on rend ces génomes distincts, soit moins de ``size`` individus ;
        - ``fill_duplicates`` vrai : on complète avec les doublons écartés pendant le parcours, dans l'ordre où ils
          ont été rencontrés (donc dans l'ordre de préférence).
    """
    unique: list[Individu[G]] = []
    duplicates: list[Individu[G]] = []
    for individu in ordered:
        if individu not in unique:
            unique.append(individu)
            if len(unique) == size:
                return tuple(unique)
        elif fill_duplicates:
            duplicates.append(individu)
    if fill_duplicates:
        unique.extend(duplicates[:size - len(unique)])
    return tuple(unique)
class PlusSurvivorSelector[G](SurvivorSelector[G]):
    """(μ+λ) sans doublons (D4) : tri stable par ``cost.total`` croissant, un seul exemplaire de chaque génome
    identique, les ``size`` meilleurs. S'il y a moins de ``size`` génomes distincts, complète avec des doublons,
    dans l'ordre des coûts.
    """

    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        """Les ``size`` meilleurs individus distincts de ``population``, complétés par des doublons si besoin.

        Raises:
            voir ``src.ga.selection.check_selectable``.
        """
        check_selectable(population, size)
        ordered: list[Individu[G]] = sorted(population, key=lambda individu: individu.cost.total)
        return _distinct_by_cost(ordered, size, fill_duplicates=True)


class DeathPenaltySurvivorSelector[G](SurvivorSelector[G]):
    """Variante « peine de mort » (D4) : les individus faisables (``cost.is_feasible``) d'abord, sans doublons et
    par ``cost.total`` croissant ; s'il en reste moins de ``size``, complète avec les meilleurs infaisables selon
    ``cost.total``. S'il y a encore moins de ``size`` génomes distincts, complète avec les doublons écartés
    (faisables d'abord, puis par ``cost.total``), comme ``PlusSurvivorSelector``.
    """

    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        """Les ``size`` meilleurs individus distincts, faisables d'abord, complétés par des doublons si besoin.

        Raises:
            voir ``src.ga.selection.check_selectable``.
        """
        check_selectable(population, size)
        ordered: list[Individu[G]] = sorted(
            population, key=lambda individu: (not individu.cost.is_feasible, individu.cost.total)
        )
        return _distinct_by_cost(ordered, size, fill_duplicates=True)


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
        """Vrai si le meilleur coût n'a pas baissé depuis ``generations`` générations.

        La première génération fixe la référence. Une hausse du coût compte comme une génération sans baisse.

        Raises:
            PopulationError: si ``population`` est vide.
        """
        if len(population) == 0:
            raise PopulationError(PopulationMessages.INVALID_STAGNATION_POPULATION)
        self._update_convergence(min(individu.cost.total for individu in population))
        return self._count >= self.generations

    def reset(self) -> None:
        self._best_cost = None
        self._count = 0

    def _update_convergence(self, best_cost: int) -> None:
        """Met à jour la référence et le compteur : une baisse du meilleur coût remet le compteur à zéro,
        sinon il augmente d'une génération. Le premier appel (après ``reset`` compris) fixe seulement la référence.
        """
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
    """Restart (D4) : garde jusqu'à ``elite_count`` meilleurs individus distincts (``cost.total``) et régénère le
    reste avec ``initializer`` ; les nouveaux individus sont évalués par ``evaluator``. Pour qu'ils passent aussi
    par le ``LocalSolver``, construire ``initializer`` avec son option ``local_solver`` (étape 6).

    L'élite n'est jamais complétée par des doublons : s'il y a moins de ``elite_count`` génomes distincts, on en
    garde moins et on en régénère davantage, de sorte que la taille de la population est conservée.

    Raises (``restart``):
        InvalidPopulationParameterError: si ``elite_count`` dépasse la taille de la population (c'est toujours le
            cas pour une population vide, car ``elite_count`` vaut au moins 1).
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
        sorted_population: list[Individu[G]] = sorted(population, key=lambda individu: individu.cost.total)
        new_population: list[Individu[G]] = list(
            _distinct_by_cost(sorted_population, self.elite_count, fill_duplicates=False)
        )
        missing_count: int = len(population) - len(new_population)
        if not missing_count:
            return tuple(new_population)
        new_individus: tuple[Individu[G], ...] = self.initializer.initialize(missing_count, rng)
        for individu in new_individus:
            cost: CostBreakdown = self.evaluator.evaluate(individu.horaire)
            new_population.append(individu.with_cost(cost))
        return tuple(new_population)
