"""Moteur mémétique : la boucle ``Memetic(NR, NM)`` du pseudo-code de CLAUDE.md (étape 9).

Le moteur ne dépend que des interfaces (D5) : toutes les stratégies viennent de ``MemeticConfig``.

Déroulement d'une exécution (``run``) :
    1. valider la configuration ; émettre ``RunStarted`` ;
    2. génération 0 : ``initializer.initialize``, puis évaluer chaque individu ; émettre ``IndividualCreated``
       pour chacun et ``GenerationEnded`` ;
    3. tant que ``termination.is_done`` est faux, une génération :
        a. boucle NR, **par lot** (D7) : tirer tous les parents (``parent_selector``), produire tous les enfants
           (``crossover.recombine``), puis pour chaque enfant : décoder, évaluer (coût avant), ``local_solver``,
           ré-encoder l'horaire rendu (``encoding.encode``), évaluer ; émettre ``LocalSearchDone`` et
           ``IndividualCreated`` ;
        b. boucle NM, par lot : tirer les individus à muter (``mutable_selector``), ``mutation.mutate`` sur leur
           génome, puis comme en a. ;
        c. ``survivor_selector.select`` sur parents + nouveaux, ramenée à ``population_size`` ; émettre
           ``GenerationEnded`` ;
        d. si ``convergence.has_converged`` : émettre ``Converged``, ``restart.restart``, ``convergence.reset()``,
           émettre ``Restarted`` ;
    4. émettre ``RunEnded`` avec le meilleur individu ; fermer les destinations ; rendre ``MemeticResult``.

Chaque tâche d'un lot reçoit son propre ``random.Random`` (``derive_task_seeds``, D7) et passe par
``config.executor.map``. Les événements passent par ``ObservationHub`` (D8), depuis le fil principal, après chaque lot.
"""

from dataclasses import dataclass

from src.ga.individual import Individu
from src.memetic.config import MemeticConfig


@dataclass(frozen=True)
class MemeticResult[G]:
    """Résultat d'une exécution : meilleur individu, population finale, nombre de générations et de restarts."""

    best: Individu[G]
    population: tuple[Individu[G], ...]
    generations: int
    restarts: int


class Memetic[G]:
    """Moteur mémétique, configuré par ``config``."""

    def __init__(self, config: MemeticConfig[G]) -> None:
        self.config = config

    def run(self) -> MemeticResult[G]:
        """Exécute l'algorithme jusqu'au critère d'arrêt et rend le résultat.

        Raises:
            InvalidMemeticConfigError, IncompatibleOperatorError: si la configuration est invalide
                (``MemeticConfig.validate``).
        """
        raise NotImplementedError  # Étape 9 (Xavier)
