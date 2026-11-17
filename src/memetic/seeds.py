"""Graines dérivées par tâche (décision D7).

Chaque tâche d'un lot (un croisement, une mutation, un appel au ``LocalSolver``) reçoit son propre
``random.Random``, construit avec une graine dérivée de la graine maître, de la génération et de la position de la
tâche dans le lot. Jamais de générateur partagé entre tâches : le résultat ne dépend alors ni de l'ordre
d'exécution ni d'un futur parallélisme. Piste : ``numpy.random.SeedSequence(...).spawn(...)``.
"""


class SeedStreams:
    """Identifiants des lots d'une génération, pour ``derive_task_seeds``."""

    INITIALIZATION: int = 0
    PARENT_SELECTION: int = 1
    CROSSOVER: int = 2
    MUTABLE_SELECTION: int = 3
    MUTATION: int = 4
    LOCAL_SEARCH: int = 5
    SURVIVOR_SELECTION: int = 6
    RESTART: int = 7


def derive_task_seeds(master_seed: int, generation: int, stream: int, task_count: int) -> tuple[int, ...]:
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
    raise NotImplementedError  # Étape 9 (Xavier)
