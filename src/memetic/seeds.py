"""Graines dérivées par tâche (décision D7).

Chaque tâche d'un lot (un croisement, une mutation, un appel au ``LocalSolver``):
    1. reçoit son propre ``random.Random``, construit avec une graine dérivée de la graine maître, de la génération et de la position de la tâche dans le lot.
Jamais de générateur partagé entre tâches : le résultat ne dépend alors ni de l'ordre d'exécution ni d'un futur parallélisme.
Piste : ``numpy.random.SeedSequence(...).spawn(...)``.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Generator, Iterable
import numpy


class SeedStreams(Enum):
    """Identifiants des lots d'une génération, pour ``derive_task_seeds``."""

    INITIALIZATION = 0
    PARENT_SELECTION = 1
    CROSSOVER = 2
    MUTABLE_SELECTION = 3
    MUTATION = 4
    LOCAL_SEARCH = 5
    SURVIVOR_SELECTION = 6
    RESTART = 7

@dataclass(frozen=True)
class SeedsCollection:
    INITIALIZATION: Generator[int]
    PARENT_SELECTION: Generator[int]
    CROSSOVER: Generator[int]
    MUTABLE_SELECTION: Generator[int]
    MUTATION: Generator[int]
    LOCAL_SEARCH: Generator[int]
    SURVIVOR_SELECTION: Generator[int]
    RESTART: Generator[int]

def derive_task_seeds(master_seed: int, generation: int, stream: SeedStreams, task_count: int) -> Generator[int]:
    """Une graine par tâche du lot, ``task_count`` en tout.
    Garanties attendues :
        - déterministe : mêmes arguments ⇒ mêmes graines ;
        - deux lots différents (autre génération, ou autre ``stream``) donnent des graines différentes ;
        - la graine d'une tâche ne dépend que de sa position, pas du nombre de tâches du lot qui la suivent.

    Args:
        master_seed: graine maître de l'exécution (``MemeticConfig.master_seed``).
        generation: numéro de la génération (0 pour l'initialisation).
        stream: identifiant du lot dans la génération (par exemple croisements, mutations, recherche locale) ;
            voir ``SeedStreams``.
        task_count: nombre de tâches du lot.
    """

    rng_from_seed = numpy.random.default_rng([master_seed, generation, stream.value])
    while True:
        yield int(rng_from_seed.integers(0, 2**63))
