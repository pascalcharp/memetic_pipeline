"""Initialisation de la population : la ligne « Initialiser population P » du pseudo-code.

Un ``PopulationInitializer`` produit des individus **non évalués** : l'évaluation est la responsabilité du
moteur, qui évalue de la même façon les individus initiaux, les enfants et les mutants.

Premier initialiseur : ``RandomBlockInitializer``, pour l'encodage par blocs (D1). Il tire au hasard des génomes
structurellement faisables, ce qui revient à respecter, pour chaque gène :
    - chaque durée de bloc d_i ≥ ``ShiftStructure.MIN_ACTIVITY_DURATION`` (4) ;
    - 22 ≤ d1 + d2 + d3 + d4 ≤ 30, soit 6 à 8 heures rémunérées (``fin - debut = Σd + 5``, entre
      ``ShiftStructure.MIN_SHIFT_SPAN`` et ``MAX_SHIFT_SPAN``) ;
    - le quart entier dans la plage utile : ``first_useful_period ≤ debut`` et ``fin ≤ last_useful_period`` ;
    - chaque activité dans 1..``activity_count``.
Le test de référence est ``FeasibilityChecker`` : tout individu produit doit être sans violation.

Option : chaque individu initial passe par un ``LocalSolver`` avant d'entrer dans la population.
"""

import random
from abc import ABC, abstractmethod

from src.ga.chromosome import ActivityBlock, BlockEncoding, BlockGene, BlockGenome
from src.ga.individual import Individu
from src.memetic.local_search import LocalSolver
from src.utils.io import ProblemInstance
from src.model.shift_rules import ShiftStructure


class InitializationDefaults:
    """Bornes des paramètres de l'initialisation."""

    MIN_POPULATION_SIZE: int = 1


class InitializationMessages:
    """Gabarits des messages d'erreur de l'initialisation."""

    INVALID_POPULATION_SIZE: str = "La taille de la population doit être au moins {minimum} ; trouvé {value}."


class InitializationError(Exception):
    """Erreur de base de l'initialisation de la population."""


class InvalidPopulationSizeError(InitializationError):
    """La taille demandée est hors de son domaine."""


class PopulationInitializer[G](ABC):
    """Stratégie d'initialisation de la population (D5)."""

    @abstractmethod
    def initialize(self, size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        """``size`` individus non évalués. Le seul aléa provient de ``rng`` : même état ⇒ même population.

        Raises:
            InvalidPopulationSizeError: si ``size < InitializationDefaults.MIN_POPULATION_SIZE``.
        """


class RandomBlockInitializer(PopulationInitializer[BlockGenome]):
    """Génomes ``BlockGenome`` structurellement faisables, tirés au hasard (D1).

    Si ``local_solver`` est donné, chaque horaire tiré lui est passé, et l'individu est construit à partir de
    l'horaire rendu (ré-encodé par ``encoding``).
    """

    def __init__(
        self,
        instance: ProblemInstance,
        encoding: BlockEncoding,
        local_solver: LocalSolver | None = None,
    ) -> None:
        self.instance = instance
        self.encoding = encoding
        self.local_solver = local_solver

    def initialize(self, size: int, rng: random.Random) -> tuple[Individu[BlockGenome], ...]:
        """Initialise une population de taille ``size``."""
        if size < InitializationDefaults.MIN_POPULATION_SIZE:
            raise InvalidPopulationSizeError(
                InitializationMessages.INVALID_POPULATION_SIZE.format(
                    minimum=InitializationDefaults.MIN_POPULATION_SIZE,
                    value=size,
                )
            )

        population: list[Individu[BlockGenome]] = []

        for _ in range(size):
            genome = self.random_genome(rng)
            individu = Individu.from_genome(genome, self.encoding)

            if self.local_solver is not None:
                result = self.local_solver.improve(individu.horaire, rng)
                genome = self.encoding.encode(result.horaire)
                individu = Individu.from_genome(genome, self.encoding)

            population.append(individu)

        return tuple(population)  # Étape 6 (Mély)

    def random_genome(self, rng: random.Random) -> BlockGenome:
        """Génère un génome contenant un gène faisable pour chaque employé."""
        genes: list[BlockGene] = []

        for _ in range(self.instance.employee_count):
            gene = self.random_gene(rng)
            genes.append(gene)

        return tuple(genes)  # Étape 6 (Mély)

    def random_gene(self, rng: random.Random) -> BlockGene:
        """Génère un quart aléatoire structurellement faisable pour un employé."""
        paid_break_duration = 2 * ShiftStructure.BREAK_DURATION

        minimum_total = (
            ShiftStructure.MIN_PAID_HOURS
            * ShiftStructure.PERIODS_PER_HOUR
            - paid_break_duration
        )

        maximum_total = (
            ShiftStructure.MAX_PAID_HOURS
            * ShiftStructure.PERIODS_PER_HOUR
            - paid_break_duration
        )

        available_span = (
            self.instance.last_useful_period
            - self.instance.first_useful_period
        )

        maximum_total = min(
            maximum_total,
            available_span
            - ShiftStructure.BREAK_DURATION
            - ShiftStructure.LUNCH_DURATION,
        )

        total_duration = rng.randint(minimum_total, maximum_total)

        durations: list[int] = []
        for _ in range(ShiftStructure.ACTIVITIES_PER_SHIFT):
            durations.append(ShiftStructure.MIN_ACTIVITY_DURATION)

        remaining = total_duration - sum(durations)
        for _ in range(remaining):
            index = rng.randrange(ShiftStructure.ACTIVITIES_PER_SHIFT)
            durations[index] += 1

        blocks: list[ActivityBlock] = []
        for duration in durations:
            activity = rng.randint(1, self.instance.activity_count)
            blocks.append(ActivityBlock(activity=activity, duration=duration))

        shift_span = (
            total_duration
            + ShiftStructure.BREAK_DURATION
            + ShiftStructure.LUNCH_DURATION
        )

        latest_start = self.instance.last_useful_period - shift_span
        start = rng.randint(self.instance.first_useful_period, latest_start)

        return BlockGene(
            start=start,
            blocks=tuple(blocks),
        )  # Étape 6 (Mély)