"""Configuration d'une exécution du moteur mémétique (décisions D5 et D7).

``MemeticConfig`` réunit les stratégies choisies (une par rôle du pseudo-code) et les paramètres scalaires. Le moteur
ne connaît que les interfaces ; c'est la configuration qui choisit les classes concrètes (à l'étape 10, par leur nom,
avec le registre de l'étape 7a).
"""

from dataclasses import dataclass, field

from src.ga.chromosome import Encoding
from src.ga.initialization import PopulationInitializer
from src.ga.operators import Crossover, Mutation
from src.ga.population import ConvergenceCriterion, RestartPolicy, SurvivorSelector
from src.ga.selection import MutableSelector, ParentSelector
from src.memetic.executor import Executor, SequentialExecutor
from src.memetic.local_search import LocalSolver
from src.memetic.termination import TerminationCriterion
from src.model.evaluation import CostEvaluator
from src.observability.collectors import MetricCollector
from src.observability.sinks import RecordSink


class MemeticDefaults:
    """Bornes des paramètres scalaires du moteur."""

    MIN_POPULATION_SIZE: int = 1
    # NR et NM peuvent être nuls séparément (pas de croisement, ou pas de mutation), mais pas tous les deux.
    MIN_OPERATION_COUNT: int = 0


class MemeticMessages:
    """Gabarits des messages d'erreur de la configuration et du moteur."""

    INVALID_POPULATION_SIZE: str = "La taille de la population doit être au moins {minimum} ; trouvé {value}."
    INVALID_OPERATION_COUNT: str = "{name} doit être au moins {minimum} ; trouvé {value}."
    NO_VARIATION: str = "NR et NM sont tous deux nuls : aucune variation à chaque génération."


class MemeticError(Exception):
    """Erreur de base du moteur mémétique."""


class InvalidMemeticConfigError(MemeticError):
    """Un paramètre de ``MemeticConfig`` est hors de son domaine."""


@dataclass(frozen=True)
class MemeticConfig[G]:
    """Stratégies et paramètres d'une exécution.

    ``crossover_count`` est NR (nombre de croisements par génération) et ``mutation_count`` NM (nombre de
    mutations par génération). ``master_seed`` est la graine dont dérivent toutes les graines des tâches (D7).
    ``convergence`` garde un état d'une génération à l'autre : utiliser une configuration par exécution.
    """

    encoding: Encoding[G]
    initializer: PopulationInitializer[G]
    parent_selector: ParentSelector[G]
    crossover: Crossover[G]
    mutable_selector: MutableSelector[G]
    mutation: Mutation[G]
    local_solver: LocalSolver
    evaluator: CostEvaluator
    survivor_selector: SurvivorSelector[G]
    convergence: ConvergenceCriterion[G]
    restart: RestartPolicy[G]
    termination: TerminationCriterion[G]
    population_size: int
    crossover_count: int
    mutation_count: int
    master_seed: int
    executor: Executor = field(default_factory=SequentialExecutor)
    collectors: tuple[MetricCollector, ...] = ()
    sinks: tuple[RecordSink, ...] = ()

    def validate(self) -> None:
        """Vérifie les paramètres et l'assemblage, avant toute exécution.

        À vérifier : taille de population, NR et NM (``MemeticDefaults``), et compatibilité du croisement et de la
        mutation avec l'encodage (``OperatorRegistry.check_compatibility``, étape 7a).

        Raises:
            InvalidMemeticConfigError: si un paramètre est hors de son domaine (son nom et sa valeur dans le message).
            IncompatibleOperatorError: si un opérateur de variation ne manipule pas les génomes de ``encoding``.
        """
        raise NotImplementedError  # Étape 9 (Xavier)
