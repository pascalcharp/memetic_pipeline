"""Graines dérivées par tâche (décision D7).

Chaque tâche d'un lot (un croisement, une mutation) reçoit son propre ``random.Random``, construit avec une graine
dérivée de la graine maître, de la génération, du lot (``SeedStreams``) et de la position de la tâche dans le lot.
Jamais de générateur partagé entre tâches : le résultat ne dépend alors ni de l'ordre d'exécution ni d'un futur
parallélisme.

``derive_task_seeds`` rend un générateur infini : la tâche ``i`` du lot prend la ``i``-ième graine. Le générateur
NumPy est initialisé avec ``[graine maître, génération, lot]`` (un ``SeedSequence`` en interne) ; les graines sont
ensuite tirées une à une, si bien que la graine d'une tâche ne dépend que de sa position.
"""

from collections.abc import Iterator
from enum import Enum

import numpy


class SeedDefaults:
    """Bornes des graines tirées."""

    # Les graines sont tirées dans [0, MAX_TASK_SEED[ ; 2⁶³ rend les collisions négligeables.
    MAX_TASK_SEED: int = 2 ** 63


class SeedStreams(Enum):
    """Identifiants des lots d'une génération, pour ``derive_task_seeds``.

    Les lots d'une seule tâche (sélections, initialisation, restart) prennent la première graine de leur générateur.
    Une tâche de croisement ou de mutation utilise sa graine pour l'opérateur, puis pour le ``LocalSolver``.
    """

    INITIALIZATION = 0
    PARENT_SELECTION = 1
    CROSSOVER = 2
    MUTABLE_SELECTION = 3
    MUTATION = 4
    SURVIVOR_SELECTION = 5
    RESTART = 6


def derive_task_seeds(master_seed: int, generation: int, stream: SeedStreams) -> Iterator[int]:
    """Générateur infini des graines des tâches d'un lot, dans l'ordre des tâches.

    Garanties :
        - déterministe : mêmes arguments ⇒ mêmes graines ;
        - deux lots différents (autre génération, autre ``stream`` ou autre graine maître) donnent des graines
          différentes ;
        - la graine d'une tâche ne dépend que de sa position, pas du nombre de tâches tirées après elle.

    Args:
        master_seed: graine maître de l'exécution (``MemeticConfig.master_seed``).
        generation: numéro de la génération (0 pour l'initialisation).
        stream: identifiant du lot dans la génération.
    """
    generator = numpy.random.default_rng([master_seed, generation, stream.value])
    while True:
        yield int(generator.integers(0, SeedDefaults.MAX_TASK_SEED))
