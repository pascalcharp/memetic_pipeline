"""Assemblage du moteur mémétique avec les vrais composants (sous-étape 9-intégration).

``build_block_memetic_config`` construit une ``MemeticConfig[BlockGenome]`` complète pour une instance : encodage par
blocs (D1), opérateurs de 7b, sélecteurs de 7a, gestion de la population de 8, et ``MiniZincLocalSolver`` branché sur
CP-SAT avec le modèle assoupli (D12), en monothread et sous limite d'effort déterministe (D10), pour que deux
exécutions de même graine soient identiques.

Les paramètres numériques viennent de ``AssemblySettings`` (valeurs par défaut dans ``AssemblyDefaults``). À
l'étape 10, les expériences pourront choisir les composants par leur nom (registre de 7a) ; cet assemblage reste la
configuration de référence du prototype.
"""

from dataclasses import dataclass

from src.ga.chromosome import BlockGenome, BlockEncoding
from src.ga.initialization import RandomBlockInitializer
from src.ga.operators import UniformGeneCrossover, ShiftStartMutation
from src.ga.population import PopulationDefaults, PlusSurvivorSelector, StagnationCriterion, EliteRestart
from src.ga.selection import SelectionDefaults, TournamentSelector, UniformMutableSelector
from src.memetic.config import MemeticConfig
from src.memetic.executor import SequentialExecutor
from src.memetic.local_search import NeighborhoodDefaults, MiniZincLocalSolver, RandomEmployeesNeighborhood
from src.memetic.solver import SolverDefaults, CpSatAdapter, SolverOptions, DeterministicTimeLimit, ModelVariants
from src.memetic.termination import GenerationLimit
from src.model.evaluation import CostEvaluator
from src.observability.hub import ObservationHub
from src.utils.io import ProblemInstance


class AssemblyDefaults:
    """Valeurs par défaut de l'assemblage de référence (petites, pour un prototype sur bench_1)."""

    POPULATION_SIZE: int = 6
    CROSSOVER_COUNT: int = 2
    MUTATION_COUNT: int = 2
    GENERATIONS: int = 5
    MASTER_SEED: int = 0
    TOURNAMENT_SIZE: int = SelectionDefaults.TOURNAMENT_SIZE
    STAGNATION_GENERATIONS: int = PopulationDefaults.STAGNATION_GENERATIONS
    ELITE_COUNT: int = PopulationDefaults.RESTART_ELITE_COUNT
    NEIGHBORHOOD_SIZE: int = NeighborhoodDefaults.RANDOM_EMPLOYEE_COUNT
    DETERMINISTIC_TIME_UNITS: float = SolverDefaults.DETERMINISTIC_TIME_UNITS
    # Les individus de l'initialisation (et du restart) passent aussi par le LocalSolver (option de l'étape 6).
    INITIAL_LOCAL_SEARCH: bool = True


@dataclass(frozen=True)
class AssemblySettings:
    """Paramètres de l'assemblage de référence.

    Les paramètres du moteur (``population_size``, ``crossover_count``, ``mutation_count``, ``master_seed``) vont
    dans ``MemeticConfig``, qui les valide. Les autres paramètres sont validés par les composants qui les reçoivent
    (``TournamentSelector``, ``StagnationCriterion``, ``EliteRestart``, ``RandomEmployeesNeighborhood``,
    ``GenerationLimit``, ``DeterministicTimeLimit``).
    """

    population_size: int = AssemblyDefaults.POPULATION_SIZE
    crossover_count: int = AssemblyDefaults.CROSSOVER_COUNT
    mutation_count: int = AssemblyDefaults.MUTATION_COUNT
    generations: int = AssemblyDefaults.GENERATIONS
    master_seed: int = AssemblyDefaults.MASTER_SEED
    tournament_size: int = AssemblyDefaults.TOURNAMENT_SIZE
    stagnation_generations: int = AssemblyDefaults.STAGNATION_GENERATIONS
    elite_count: int = AssemblyDefaults.ELITE_COUNT
    neighborhood_size: int = AssemblyDefaults.NEIGHBORHOOD_SIZE
    deterministic_time_units: float = AssemblyDefaults.DETERMINISTIC_TIME_UNITS
    initial_local_search: bool = AssemblyDefaults.INITIAL_LOCAL_SEARCH


def build_block_memetic_config(
        instance: ProblemInstance,
        settings: AssemblySettings = AssemblySettings(),
        dispatcher: ObservationHub | None = None,
) -> MemeticConfig[BlockGenome]:
    """Configuration complète du moteur pour ``instance``, avec les vrais composants.

    Composants attendus :
        - encodage : ``BlockEncoding`` ;
        - ``LocalSolver`` : ``MiniZincLocalSolver(instance, adapter, neighborhood, evaluator)``, avec
          ``CpSatAdapter(SolverOptions(limit=DeterministicTimeLimit(settings.deterministic_time_units)),
          model=ModelVariants.RELAXED)`` (monothread et graine par défaut de ``SolverOptions``) et
          ``RandomEmployeesNeighborhood(instance, size=settings.neighborhood_size)`` ;
        - évaluateur : ``CostEvaluator(instance)``, le même objet pour le ``LocalSolver``, le moteur et le restart ;
        - initialiseur : ``RandomBlockInitializer(instance, encoding)``, avec ``local_solver`` si
          ``settings.initial_local_search`` est vrai ; le même objet pour le moteur et le restart ;
        - sélection : ``TournamentSelector(settings.tournament_size)`` et ``UniformMutableSelector()`` ;
        - variation : ``UniformGeneCrossover()`` et ``ShiftStartMutation(instance)`` ;
        - population : ``PlusSurvivorSelector()``, ``StagnationCriterion(settings.stagnation_generations)``,
          ``EliteRestart(initializer, evaluator, settings.elite_count)`` ;
        - arrêt : ``GenerationLimit(settings.generations)`` ;
        - ``dispatcher`` : celui reçu, ou un ``ObservationHub()`` neuf s'il vaut ``None``.

    Chaque appel construit des composants neufs : le critère de convergence a un état, donc une configuration ne
    sert qu'à une exécution.
    """
    encoding = BlockEncoding()

    solver_adaptor = CpSatAdapter(SolverOptions(limit=DeterministicTimeLimit(settings.deterministic_time_units)), model=ModelVariants.RELAXED)
    neighborhood = RandomEmployeesNeighborhood(instance, size=settings.neighborhood_size)
    evaluator = CostEvaluator(instance)
    local_solver = MiniZincLocalSolver(instance, solver_adaptor, neighborhood, evaluator)
    initializer = RandomBlockInitializer(instance, encoding, local_solver if settings.initial_local_search else None)
    if dispatcher is None:
        dispatcher = ObservationHub()

    return MemeticConfig(
        encoding=encoding,
        initializer=initializer,
        parent_selector=TournamentSelector(settings.tournament_size),
        crossover=UniformGeneCrossover(),
        mutable_selector=UniformMutableSelector(),
        mutation=ShiftStartMutation(instance),
        local_solver=local_solver,
        evaluator=evaluator,
        survivor_selector=PlusSurvivorSelector(),
        convergence=StagnationCriterion(settings.stagnation_generations),
        restart=EliteRestart(initializer=initializer, evaluator=evaluator, elite_count=settings.elite_count),
        termination=GenerationLimit(settings.generations),
        population_size=settings.population_size,
        crossover_count=settings.crossover_count,
        mutation_count=settings.mutation_count,
        master_seed=settings.master_seed,
        dispatcher=dispatcher,
        executor=SequentialExecutor()
    )
