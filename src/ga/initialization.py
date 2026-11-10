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

from src.ga.chromosome import BlockEncoding, BlockGene, BlockGenome
from src.ga.individual import Individu
from src.memetic.local_search import LocalSolver
from src.utils.io import ProblemInstance


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
        raise NotImplementedError  # Étape 6 (Mély)

    def random_genome(self, rng: random.Random) -> BlockGenome:
        """Un gène faisable par employé de l'instance."""
        raise NotImplementedError  # Étape 6 (Mély)

    def random_gene(self, rng: random.Random) -> BlockGene:
        """Le quart d'un employé : début, puis activité et durée des quatre blocs, faisable (conditions du module)."""
        raise NotImplementedError  # Étape 6 (Mély)
