"""Catalogue des événements du moteur et schéma des enregistrements (décision D8).

Deux notions distinctes :
    - un **événement** est un objet Python émis par le moteur (étape 9) à un point précis de la boucle. Il porte des
      objets du domaine (individus, coûts, résultats du ``LocalSolver``) ; il n'est jamais écrit tel quel ;
    - un **enregistrement** (``Record``) est un dictionnaire de valeurs simples (nombres, chaînes, listes,
      dictionnaires), sérialisable en JSON. Les collecteurs (``collectors.py``) transforment les événements en
      enregistrements ; les destinations (``sinks.py``) les écrivent.

Chaque enregistrement contient ``schema_version`` et ``event`` (``RecordSchema``), construits par ``make_record``.

Points d'émission prévus dans la boucle (le moteur émet depuis le fil principal, après chaque lot, D7) :
    - ``RunStarted`` : avant l'initialisation ;
    - ``LocalSearchDone`` : après chaque appel au ``LocalSolver``, avec le coût avant et après ;
    - ``IndividualCreated`` : pour chaque nouvel individu évalué (initialisation, croisement, mutation, restart) ;
    - ``GenerationEnded`` : après ``SelectPop``, avec la population de la génération ;
    - ``Converged`` puis ``Restarted`` : quand la population a convergé et a été régénérée ;
    - ``RunEnded`` : à la fin, avec le meilleur individu.
La génération 0 est l'initialisation.
"""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any, ClassVar

from src.ga.individual import Individu
from src.memetic.local_search import LocalSearchResult
from src.model.evaluation import CostBreakdown

type Record = dict[str, Any]


class EventNames:
    """Noms des événements de D8, tels qu'ils apparaissent dans les enregistrements."""

    RUN_STARTED: str = "run_started"
    INDIVIDUAL_CREATED: str = "individual_created"
    LOCAL_SEARCH_DONE: str = "local_search_done"
    GENERATION_ENDED: str = "generation_ended"
    CONVERGED: str = "converged"
    RESTARTED: str = "restarted"
    RUN_ENDED: str = "run_ended"


class Origins:
    """D'où vient un individu : utile pour mesurer la faisabilité et l'apport du solveur par opérateur."""

    INITIALIZATION: str = "initialization"
    CROSSOVER: str = "crossover"
    MUTATION: str = "mutation"
    RESTART: str = "restart"


class RecordSchema:
    """Champs obligatoires de tout enregistrement et version du schéma.

    Incrémenter ``VERSION`` à chaque changement incompatible des champs d'un enregistrement.
    """

    VERSION: int = 1
    VERSION_FIELD: str = "schema_version"
    EVENT_FIELD: str = "event"


def make_record(event: str, **fields: Any) -> Record:
    """Enregistrement de type ``event`` : ``schema_version``, ``event``, puis ``fields`` (valeurs simples)."""
    record: Record = {RecordSchema.VERSION_FIELD: RecordSchema.VERSION, RecordSchema.EVENT_FIELD: event}
    record.update(fields)
    return record


# ---------------------------------------------------------------------------------------------------------------------
# Événements
# ---------------------------------------------------------------------------------------------------------------------

@dataclass(frozen=True)
class Event:
    """Base des événements émis par le moteur. ``NAME`` est le nom de l'événement (``EventNames``)."""

    NAME: ClassVar[str]


@dataclass(frozen=True)
class RunStarted(Event):
    """Début d'une exécution, avec les paramètres scalaires de la configuration."""

    NAME: ClassVar[str] = EventNames.RUN_STARTED
    master_seed: int
    population_size: int
    crossover_count: int
    mutation_count: int


@dataclass(frozen=True)
class LocalSearchDone(Event):
    """Un appel au ``LocalSolver`` vient de finir.

    ``cost_before`` est le coût de l'individu avant la recherche locale (juste après la variation),
    ``cost_after`` celui de l'horaire rendu. ``operator`` est le nom de la classe de l'opérateur de variation
    (``None`` pour l'initialisation et le restart).
    """

    NAME: ClassVar[str] = EventNames.LOCAL_SEARCH_DONE
    generation: int
    origin: str
    operator: str | None
    cost_before: CostBreakdown
    cost_after: CostBreakdown
    result: LocalSearchResult


@dataclass(frozen=True)
class IndividualCreated(Event):
    """Un nouvel individu évalué entre dans la population candidate (avant ``SelectPop``)."""

    NAME: ClassVar[str] = EventNames.INDIVIDUAL_CREATED
    generation: int
    origin: str
    operator: str | None
    individual: Individu


@dataclass(frozen=True)
class GenerationEnded(Event):
    """Fin d'une génération : ``population`` est la population après ``SelectPop`` (évaluée)."""

    NAME: ClassVar[str] = EventNames.GENERATION_ENDED
    generation: int
    population: Sequence[Individu]


@dataclass(frozen=True)
class Converged(Event):
    """La population a convergé à la fin de ``generation`` (``ConvergenceCriterion``)."""

    NAME: ClassVar[str] = EventNames.CONVERGED
    generation: int


@dataclass(frozen=True)
class Restarted(Event):
    """La population vient d'être régénérée (``RestartPolicy``) ; ``population`` est la nouvelle population."""

    NAME: ClassVar[str] = EventNames.RESTARTED
    generation: int
    population: Sequence[Individu]


@dataclass(frozen=True)
class RunEnded(Event):
    """Fin de l'exécution, après ``generations`` générations, avec le meilleur individu trouvé."""

    NAME: ClassVar[str] = EventNames.RUN_ENDED
    generations: int
    best: Individu
