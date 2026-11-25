"""Tests du script d'expériences ``experiments/drivers/run_experiment.py`` (étape 10a).

Sans MiniZinc : lecture et validation de la configuration (dont les stratégies choisies par leur nom, étape 10c), chemins
par défaut, écriture des résultats, journal.
Avec MiniZinc et CP-SAT (``TestRunExperimentEndToEnd``, quelques secondes) : une exécution complète et courte sur
bench_1, de la ligne de commande jusqu'au fichier de résultats et à l'entrée d'EXPLOG.md, dans un répertoire
temporaire.
"""

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

from src.config import ProjectPaths
from experiments.drivers.run_experiment import (
    ConfigKeys,
    ExperimentDefaults,
    ExplogTexts,
    InvalidExperimentConfigError,
    ResultKeys,
    ResultsFileExistsError,
    append_explog_entry,
    git_state_text,
    default_results_dir,
    load_experiment_config,
    main,
    parse_arguments,
    write_results,
)
from src.memetic.assembly import AssemblyDefaults, AssemblySettings
from src.memetic.catalog import CatalogDefaults, StrategyChoice, StrategyChoices, StrategyKeys, StrategyNames, StrategyRoles
from src.observability.collectors import SolverEffortFields

BASE_CONFIG: Path = ProjectPaths.EXPERIMENT_CONFIG_DIR / "integration_bench1.json"
DESCRIPTION: str = "Essai court du script d'expériences."
INSTANCE: str = "bench_1"
UNKNOWN_INSTANCE: str = "bench_inexistant"
EXPERIMENT_NAME: str = "essai_court"
FIXED_TIME = datetime(2026, 11, 22, 14, 30, 5, tzinfo=timezone(timedelta(hours=-5)))
FIXED_DAY: str = "2026-11-22"
FIXED_FILE_TIME: str = "143005"

# Exécution réelle : une seule génération, pour rester courte.
SHORT_SETTINGS: dict = {
    "population_size": 4,
    "crossover_count": 1,
    "mutation_count": 1,
    "generations": 1,
    "master_seed": 3,
}
# Exécution réelle : une mutation choisie par son nom, autre que celle de l'assemblage de référence.
SHORT_STRATEGIES: dict = {StrategyRoles.MUTATION: StrategyNames.BLOCK_BOUNDARY}
CHILDREN_PER_CROSSOVER: int = 2
BENCH_1_EMPLOYEES: int = 3


def write_config(directory: Path, content: object, name: str = EXPERIMENT_NAME) -> Path:
    path = directory / (name + ".json")
    path.write_text(json.dumps(content), encoding="utf-8")
    return path


def valid_content(**settings) -> dict:
    return {ConfigKeys.DESCRIPTION: DESCRIPTION, ConfigKeys.INSTANCE: INSTANCE, ConfigKeys.SETTINGS: settings}


# ---------------------------------------------------------------------------------------------------------------------
# Lecture de la configuration
# ---------------------------------------------------------------------------------------------------------------------

class TestLoadExperimentConfig(unittest.TestCase):

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)

    def tearDown(self) -> None:
        self.directory.cleanup()

    def assert_invalid(self, content: object, *expected_in_message: str) -> None:
        path = write_config(self.root, content)
        with self.assertRaises(InvalidExperimentConfigError) as context:
            load_experiment_config(path)
        self.assertIn(str(path), str(context.exception))
        for text in expected_in_message:
            self.assertIn(text, str(context.exception))

    def test_givenBaseConfig_whenLoaded_thenIntegrationSettings(self) -> None:
        config = load_experiment_config(BASE_CONFIG)
        self.assertEqual(config.name, "integration_bench1")
        self.assertEqual(config.instance_name, INSTANCE)
        self.assertTrue(config.description)
        self.assertEqual(config.settings, AssemblySettings(
            population_size=6, crossover_count=2, mutation_count=2, generations=4, master_seed=7,
            stagnation_generations=1,
        ))

    def test_givenValidConfig_whenLoaded_thenNameComesFromTheFileAndMissingSettingsAreDefaults(self) -> None:
        config = load_experiment_config(write_config(self.root, valid_content(master_seed=11)))
        self.assertEqual(config.name, EXPERIMENT_NAME)
        self.assertEqual(config.description, DESCRIPTION)
        self.assertEqual(config.settings.master_seed, 11)
        self.assertEqual(config.settings.population_size, AssemblyDefaults.POPULATION_SIZE)
        self.assertEqual(config.instance_path(), ProjectPaths.DATA_DIR / "bench_1.json")

    def test_givenNoSettingsKey_whenLoaded_thenAllDefaults(self) -> None:
        content = {ConfigKeys.DESCRIPTION: DESCRIPTION, ConfigKeys.INSTANCE: INSTANCE}
        self.assertEqual(load_experiment_config(write_config(self.root, content)).settings, AssemblySettings())

    def test_givenIntegerForAFloatSetting_whenLoaded_thenAccepted(self) -> None:
        config = load_experiment_config(write_config(self.root, valid_content(deterministic_time_units=2)))
        self.assertEqual(config.settings.deterministic_time_units, 2)

    def test_givenMissingRequiredKey_whenLoaded_thenRaisesWithTheKey(self) -> None:
        for key in ConfigKeys.REQUIRED:
            with self.subTest(key=key):
                content = valid_content()
                del content[key]
                self.assert_invalid(content, key)

    def test_givenUnknownKey_whenLoaded_thenRaisesWithTheKey(self) -> None:
        self.assert_invalid(valid_content() | {"commentaire": "x"}, "commentaire")

    def test_givenUnknownSetting_whenLoaded_thenRaisesWithTheSetting(self) -> None:
        self.assert_invalid(valid_content(mutation_rate=0.1), "mutation_rate")

    def test_givenWrongTypes_whenLoaded_thenRaisesWithTheKey(self) -> None:
        cases = {
            "population_size": "six",
            "generations": True,
            "deterministic_time_units": "beaucoup",
            "initial_local_search": 1,
        }
        for key, value in cases.items():
            with self.subTest(key=key):
                self.assert_invalid(valid_content(**{key: value}), key)

    # --- Stratégies (étape 10c) ---------------------------------------------------------------------------------

    def with_strategies(self, strategies: object) -> dict:
        return valid_content() | {ConfigKeys.STRATEGIES: strategies}

    def test_givenNoStrategiesKey_whenLoaded_thenReferenceAssemblyStrategies(self) -> None:
        config = load_experiment_config(write_config(self.root, valid_content()))
        self.assertEqual(config.strategies, StrategyChoices())

    def test_givenShortForm_whenLoaded_thenChosenNameAndOtherRolesKeepTheirDefault(self) -> None:
        content = self.with_strategies({StrategyRoles.MUTATION: StrategyNames.ACTIVITY})
        config = load_experiment_config(write_config(self.root, content))
        self.assertEqual(config.strategies.mutation, StrategyChoice(StrategyNames.ACTIVITY))
        self.assertEqual(config.strategies.crossover, StrategyChoice(CatalogDefaults.CROSSOVER))

    def test_givenObjectForm_whenLoaded_thenNameAndParametersAreKept(self) -> None:
        content = self.with_strategies({
            StrategyRoles.CROSSOVER: {StrategyKeys.NAME: StrategyNames.UNIFORM_GENE, StrategyKeys.PARAMETERS: {}},
            StrategyRoles.MUTATION: {StrategyKeys.NAME: StrategyNames.BLOCK_BOUNDARY},
        })
        config = load_experiment_config(write_config(self.root, content))
        self.assertEqual(config.strategies, StrategyChoices(
            crossover=StrategyChoice(StrategyNames.UNIFORM_GENE), mutation=StrategyChoice(StrategyNames.BLOCK_BOUNDARY)
        ))

    def test_givenUnknownRole_whenLoaded_thenRaisesWithTheRoleAndTheKnownRoles(self) -> None:
        self.assert_invalid(self.with_strategies({"selection": "tournoi"}), "selection", StrategyRoles.MUTATION)

    def test_givenUnknownName_whenLoaded_thenRaisesWithTheNameAndTheKnownNames(self) -> None:
        content = self.with_strategies({StrategyRoles.MUTATION: "mutation_inexistante"})
        self.assert_invalid(content, StrategyRoles.MUTATION, "mutation_inexistante", StrategyNames.SHIFT_START)

    def test_givenUnexpectedParameter_whenLoaded_thenRaisesWithTheParameter(self) -> None:
        content = self.with_strategies({StrategyRoles.CROSSOVER: {
            StrategyKeys.NAME: StrategyNames.UNIFORM_GENE, StrategyKeys.PARAMETERS: {"taux": 0.8},
        }})
        self.assert_invalid(content, StrategyRoles.CROSSOVER, "taux")

    def test_givenReservedContextParameter_whenLoaded_thenRaisesWithTheParameter(self) -> None:
        content = self.with_strategies({StrategyRoles.MUTATION: {
            StrategyKeys.NAME: StrategyNames.ACTIVITY, StrategyKeys.PARAMETERS: {CatalogDefaults.CONTEXT_PARAMETER: 1},
        }})
        self.assert_invalid(content, CatalogDefaults.CONTEXT_PARAMETER)

    def test_givenMalformedStrategies_whenLoaded_thenRaisesWithTheKey(self) -> None:
        mutation = StrategyRoles.MUTATION
        cases = {
            "strategies pas un objet": ([StrategyNames.ACTIVITY], ConfigKeys.STRATEGIES),
            "choix ni texte ni objet": ({mutation: 3}, mutation),
            "nom pas un texte": ({mutation: {StrategyKeys.NAME: 3}}, StrategyKeys.NAME),
            "nom absent": ({mutation: {StrategyKeys.PARAMETERS: {}}}, StrategyKeys.NAME),
            "paramètres pas un objet": (
                {mutation: {StrategyKeys.NAME: StrategyNames.ACTIVITY, StrategyKeys.PARAMETERS: [1]}},
                StrategyKeys.PARAMETERS,
            ),
            "clé inconnue dans le choix": (
                {mutation: {StrategyKeys.NAME: StrategyNames.ACTIVITY, "taux": 1}}, "taux",
            ),
        }
        for case, (strategies, expected) in cases.items():
            with self.subTest(case=case):
                self.assert_invalid(self.with_strategies(strategies), expected)

    def test_givenNonStringDescriptionOrSettingsNotAnObject_whenLoaded_thenRaises(self) -> None:
        self.assert_invalid(valid_content() | {ConfigKeys.DESCRIPTION: 42}, ConfigKeys.DESCRIPTION)
        self.assert_invalid(valid_content() | {ConfigKeys.SETTINGS: [1, 2]}, ConfigKeys.SETTINGS)

    def test_givenRootNotAnObject_whenLoaded_thenRaises(self) -> None:
        self.assert_invalid([valid_content()])

    def test_givenInvalidJson_whenLoaded_thenRaisesWithThePath(self) -> None:
        path = self.root / "casse.json"
        path.write_text("{ pas du JSON", encoding="utf-8")
        with self.assertRaises(InvalidExperimentConfigError) as context:
            load_experiment_config(path)
        self.assertIn(str(path), str(context.exception))

    def test_givenMissingFile_whenLoaded_thenRaisesWithThePath(self) -> None:
        path = self.root / "absent.json"
        with self.assertRaises(InvalidExperimentConfigError) as context:
            load_experiment_config(path)
        self.assertIn(str(path), str(context.exception))

    def test_givenUnknownInstance_whenLoaded_thenRaisesWithTheInstance(self) -> None:
        self.assert_invalid(valid_content() | {ConfigKeys.INSTANCE: UNKNOWN_INSTANCE}, UNKNOWN_INSTANCE)


# ---------------------------------------------------------------------------------------------------------------------
# Chemins, résultats et journal, sans MiniZinc
# ---------------------------------------------------------------------------------------------------------------------

class TestPathsResultsAndLog(unittest.TestCase):

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)

    def tearDown(self) -> None:
        self.directory.cleanup()

    def test_givenADay_whenDefaultResultsDir_thenOneDirectoryPerDayUnderExperimentsResults(self) -> None:
        self.assertEqual(default_results_dir(FIXED_TIME), ProjectPaths.EXPERIMENT_RESULTS_DIR / FIXED_DAY)

    def test_givenOnlyTheConfig_whenParsingArguments_thenDefaultLogAndNoResultsDir(self) -> None:
        arguments = parse_arguments([str(BASE_CONFIG)])
        self.assertEqual(arguments.config, BASE_CONFIG)
        self.assertIsNone(arguments.results_dir)
        self.assertEqual(arguments.log, ProjectPaths.EXPLOG_FILE)

    def test_givenThreePaths_whenParsingArguments_thenAllThreeAreKept(self) -> None:
        arguments = parse_arguments([str(BASE_CONFIG), "--results-dir", "r", "--log", "j.md"])
        self.assertEqual((arguments.results_dir, arguments.log), (Path("r"), Path("j.md")))

    def test_givenDocument_whenWritingResults_thenNamedAfterExperimentAndTimeInACreatedDirectory(self) -> None:
        results_dir = self.root / "nouveau" / FIXED_DAY
        path = write_results({"a": 1}, results_dir, EXPERIMENT_NAME, FIXED_TIME)
        self.assertEqual(path, results_dir / f"{EXPERIMENT_NAME}_{FIXED_FILE_TIME}.json")
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {"a": 1})

    def test_givenExistingResultsFile_whenWritingAgain_thenRaisesWithoutOverwriting(self) -> None:
        path = write_results({"a": 1}, self.root, EXPERIMENT_NAME, FIXED_TIME)
        with self.assertRaises(ResultsFileExistsError) as context:
            write_results({"a": 2}, self.root, EXPERIMENT_NAME, FIXED_TIME)
        self.assertIn(str(path), str(context.exception))
        self.assertEqual(json.loads(path.read_text(encoding="utf-8")), {"a": 1})

    def test_givenNoLog_whenAppending_thenHeaderThenEntry(self) -> None:
        log = self.root / "sous" / "EXPLOG.md"
        append_explog_entry(log, "\n## entrée 1\n")
        self.assertEqual(log.read_text(encoding="utf-8"), ExplogTexts.HEADER + "\n## entrée 1\n")

    def test_givenEmptyLog_whenAppending_thenHeaderIsWritten(self) -> None:
        log = self.root / "EXPLOG.md"
        log.touch()
        append_explog_entry(log, "\n## entrée 1\n")
        self.assertTrue(log.read_text(encoding="utf-8").startswith(ExplogTexts.HEADER))

    def test_givenGitState_whenWritingTheLogMention_thenOnlyADirtyOrUnknownTreeIsMentioned(self) -> None:
        self.assertEqual(git_state_text(False), ExplogTexts.GIT_CLEAN)
        self.assertEqual(git_state_text(True), ExplogTexts.GIT_DIRTY)
        self.assertEqual(git_state_text(None), ExplogTexts.GIT_UNKNOWN)

    def test_givenExistingLog_whenAppending_thenPreviousEntriesAreKept(self) -> None:
        log = self.root / "EXPLOG.md"
        append_explog_entry(log, "\n## entrée 1\n")
        append_explog_entry(log, "\n## entrée 2\n")
        content = log.read_text(encoding="utf-8")
        self.assertEqual(content.count(ExplogTexts.HEADER), 1)
        self.assertLess(content.index("entrée 1"), content.index("entrée 2"))


# ---------------------------------------------------------------------------------------------------------------------
# Exécution complète, avec MiniZinc et CP-SAT
# ---------------------------------------------------------------------------------------------------------------------

class TestRunExperimentEndToEnd(unittest.TestCase):
    """Une exécution par la ligne de commande, sans ``--results-dir`` : le répertoire du jour est créé sous une racine
    de résultats temporaire (``ExperimentDefaults.RESULTS_ROOT`` remplacé le temps du test)."""

    directory: tempfile.TemporaryDirectory
    root: Path
    results_path: Path
    document: dict
    log_text: str

    @classmethod
    def setUpClass(cls) -> None:
        cls.directory = tempfile.TemporaryDirectory()
        cls.root = Path(cls.directory.name)
        content = valid_content(**SHORT_SETTINGS) | {ConfigKeys.STRATEGIES: SHORT_STRATEGIES}
        config_path = write_config(cls.root, content)
        cls.log_path = cls.root / "EXPLOG.md"
        results_root = cls.root / "results"
        with mock.patch.object(ExperimentDefaults, "RESULTS_ROOT", results_root), \
                mock.patch("builtins.print"):
            cls.results_path = main([str(config_path), "--log", str(cls.log_path)], clock=lambda: FIXED_TIME)
        cls.expected_results_path = results_root / FIXED_DAY / f"{EXPERIMENT_NAME}_{FIXED_FILE_TIME}.json"
        cls.document = json.loads(cls.results_path.read_text(encoding="utf-8"))
        cls.log_text = cls.log_path.read_text(encoding="utf-8")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.directory.cleanup()

    def test_givenNoResultsDir_whenRun_thenResultsGoToTheDayDirectory(self) -> None:
        self.assertEqual(self.results_path, self.expected_results_path)
        self.assertTrue(self.results_path.is_file())

    def test_givenRun_whenReadingResults_thenConfigurationAndProvenanceAreRecorded(self) -> None:
        self.assertEqual(self.document[ResultKeys.EXPERIMENT], EXPERIMENT_NAME)
        self.assertEqual(self.document[ResultKeys.DESCRIPTION], DESCRIPTION)
        self.assertEqual(self.document[ResultKeys.INSTANCE], INSTANCE)
        self.assertEqual(self.document[ResultKeys.SETTINGS]["master_seed"], SHORT_SETTINGS["master_seed"])
        self.assertEqual(self.document[ResultKeys.SETTINGS]["elite_count"], AssemblyDefaults.ELITE_COUNT)
        self.assertEqual(self.document[ResultKeys.STARTED_AT], FIXED_TIME.isoformat())
        for key in (ResultKeys.GIT_COMMIT, ResultKeys.PYTHON_VERSION, ResultKeys.PACKAGES, ResultKeys.DURATION_SECONDS):
            self.assertIn(key, self.document)
        # None hors d'un dépôt Git : c'est le cas dans l'image Docker de la CI, sans git ni .git/.
        self.assertIn(self.document[ResultKeys.GIT_DIRTY], (True, False, None))

    def test_givenChosenStrategies_whenReadingResultsAndLog_thenEveryRoleIsRecorded(self) -> None:
        expected = StrategyChoices(mutation=StrategyChoice(StrategyNames.BLOCK_BOUNDARY)).to_json()
        self.assertEqual(self.document[ResultKeys.STRATEGIES], expected)
        for name in (StrategyNames.UNIFORM_GENE, StrategyNames.BLOCK_BOUNDARY):
            with self.subTest(name=name):
                self.assertIn(name, self.log_text)

    def test_givenRun_whenReadingTheLog_thenTheGitStateMentionMatchesTheResults(self) -> None:
        self.assertIn(git_state_text(self.document[ResultKeys.GIT_DIRTY]) + "\n", self.log_text)

    def test_givenRun_whenReadingResults_thenBestCostMatchesTheLastGenerationStatistics(self) -> None:
        best_cost = self.document[ResultKeys.BEST][ResultKeys.BEST_COST]
        last_generation = self.document[ResultKeys.COST_STATISTICS][-1]
        self.assertEqual(best_cost[ResultKeys.TOTAL], last_generation["total_min"])
        self.assertIn(ResultKeys.IS_FEASIBLE, best_cost)
        self.assertEqual(len(self.document[ResultKeys.BEST][ResultKeys.BEST_SCHEDULE]), BENCH_1_EMPLOYEES)
        self.assertEqual(self.document[ResultKeys.GENERATIONS], SHORT_SETTINGS["generations"])

    def test_givenRun_whenReadingResults_thenCumulativeSolverEffortCountsEveryLocalSearch(self) -> None:
        effort = self.document[ResultKeys.SOLVER_EFFORT]
        new_per_generation = SHORT_SETTINGS["crossover_count"] * CHILDREN_PER_CROSSOVER + SHORT_SETTINGS["mutation_count"]
        expected_calls = SHORT_SETTINGS["population_size"] + new_per_generation * SHORT_SETTINGS["generations"]
        if self.document[ResultKeys.RESTARTS] == 0:
            self.assertEqual(effort[SolverEffortFields.CALLS], expected_calls)
        else:
            self.assertGreater(effort[SolverEffortFields.CALLS], expected_calls)
        self.assertIsNotNone(effort[SolverEffortFields.FAILURES])

    def test_givenRun_whenReadingResults_thenPerGenerationRecordsArePresent(self) -> None:
        generations = SHORT_SETTINGS["generations"] + 1
        self.assertEqual(len(self.document[ResultKeys.COST_STATISTICS]), generations)
        self.assertEqual(len(self.document[ResultKeys.DIVERSITY]), generations)
        self.assertTrue(self.document[ResultKeys.FEASIBILITY_RATES])

    def test_givenRun_whenReadingTheLog_thenEntryHasDescriptionPathsCostAndSolverEffort(self) -> None:
        self.assertTrue(self.log_text.startswith(ExplogTexts.HEADER))
        best_total = self.document[ResultKeys.BEST][ResultKeys.BEST_COST][ResultKeys.TOTAL]
        calls = self.document[ResultKeys.SOLVER_EFFORT][SolverEffortFields.CALLS]
        for text in (DESCRIPTION, EXPERIMENT_NAME, self.document[ResultKeys.CONFIG_PATH],
                     f"Coût obtenu : {best_total}", f"{calls} appels", "2026-11-22 14:30"):
            with self.subTest(text=text):
                self.assertIn(text, self.log_text)
        self.assertIn(self.results_path.resolve().as_posix(), self.log_text)


if __name__ == "__main__":
    unittest.main()
