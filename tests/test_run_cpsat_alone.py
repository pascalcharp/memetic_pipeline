"""Tests du témoin « CP-SAT seul » ``experiments/drivers/run_cpsat_alone.py`` (étape 10g).

Sans MiniZinc : lecture et validation de la configuration, lecture de la sortie de ``minizinc -i -s``, ligne de
commande, document de résultats et entrée du journal.
Avec MiniZinc et CP-SAT (``TestCpSatAloneEndToEnd``, quelques secondes) : une résolution courte de bench_1, de la
ligne de commande jusqu'au fichier de résultats et à l'entrée d'EXPLOG.md, dans un répertoire temporaire.
"""

import json
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

from experiments.drivers.run_cpsat_alone import (
    CpSatAloneConfig,
    CpSatAloneDefaults,
    CpSatAloneKeys,
    CpSatAloneResultKeys,
    CpSatAloneTexts,
    InvalidCpSatAloneConfigError,
    MiniZincCliFlags,
    ModelChoices,
    explog_entry,
    load_cpsat_alone_config,
    main,
    minizinc_command,
    parse_minizinc_output,
    parse_stat_value,
    results_document,
    version_text,
)
from src.config import ProjectPaths
from src.memetic.solver import CpSatFlags, RelaxedModelNames
from src.model.evaluation import PenaltyWeights

NAME: str = "essai_cpsat"
INSTANCE: str = "bench_1"
UNKNOWN_INSTANCE: str = "bench_inexistant"
SEED: int = 4
UNITS: float = 2.5
FIXED_TIME = datetime(2026, 11, 26, 21, 30, 5, tzinfo=timezone(timedelta(hours=-5)))
EXECUTABLE: Path = Path("/opt/minizinc/bin/minizinc")
GIT_COMMIT: str = "abc123"
DURATION: float = 12.34
VERSION: str = "2.10.0"

# bench_1 : optimum 94 (modèle de référence), prouvé en moins d'une seconde.
BENCH_1_OPTIMUM: int = 94
END_TO_END_UNITS: int = 30

# Sortie typique de ``minizinc -i -s`` : statistiques de compilation, deux solutions, preuve, statistiques finales.
SAMPLE_OUTPUT: str = """%%%mzn-stat: flatTime=0.21
%%%mzn-stat: method="minimize"
%%%mzn-stat-end
{ "Cout": 2000010 }
%%%mzn-stat: objective=2.00001e+06
%%%mzn-stat: solveTime=0.9
%%%mzn-stat: propagations=1500
%%%mzn-stat: failures=4
----------
{ "Cout": 120 }
%%%mzn-stat: objective=120
%%%mzn-stat: solveTime=1.5
%%%mzn-stat: propagations=4000
%%%mzn-stat: failures=9
----------
==========
%%%mzn-stat: objective=120
%%%mzn-stat: solveTime=1.7
%%%mzn-stat: propagations=4500
%%%mzn-stat: failures=11
%%%mzn-stat: nSolutions=2
%%%mzn-stat-end
"""


def raw_config(**overrides: object) -> dict:
    content = {
        CpSatAloneKeys.DESCRIPTION: "Essai du témoin.",
        CpSatAloneKeys.INSTANCE: INSTANCE,
        CpSatAloneKeys.MODEL: ModelChoices.REFERENCE,
        CpSatAloneKeys.SEED: SEED,
        CpSatAloneKeys.DETERMINISTIC_TIME_UNITS: UNITS,
    }
    content.update(overrides)
    return content


def write_config(directory: Path, content: object) -> Path:
    path = directory / (NAME + ".json")
    text = content if isinstance(content, str) else json.dumps(content)
    path.write_text(text, encoding="utf-8")
    return path


def config_of(model: str = ModelChoices.REFERENCE) -> CpSatAloneConfig:
    return CpSatAloneConfig(
        path=ProjectPaths.EXPERIMENT_CONFIG_DIR / (NAME + ".json"),
        description="Essai.", instance_name=INSTANCE, model=model, seed=SEED, deterministic_time_units=UNITS,
    )


class TestLoadConfig(unittest.TestCase):
    """Lecture et validation du fichier de configuration."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def load(self, content: object) -> CpSatAloneConfig:
        return load_cpsat_alone_config(write_config(self.root, content))

    def assert_rejected(self, content: object, *expected_fragments: str) -> None:
        with self.assertRaises(InvalidCpSatAloneConfigError) as context:
            self.load(content)
        for fragment in (NAME,) + expected_fragments:
            self.assertIn(fragment, str(context.exception))

    def test_nominal_config(self) -> None:
        config = self.load(raw_config())
        self.assertEqual(config.name, NAME)
        self.assertEqual(config.instance_name, INSTANCE)
        self.assertEqual(config.seed, SEED)
        self.assertEqual(config.deterministic_time_units, UNITS)
        self.assertEqual(config.model_file, ProjectPaths.REFERENCE_MODEL_FILE)
        self.assertTrue(config.instance_path.exists())

    def test_relaxed_model_file(self) -> None:
        config = self.load(raw_config(**{CpSatAloneKeys.MODEL: ModelChoices.RELAXED}))
        self.assertEqual(config.model_file, ProjectPaths.RELAXED_MODEL_FILE)

    def test_integer_limit_becomes_float(self) -> None:
        config = self.load(raw_config(**{CpSatAloneKeys.DETERMINISTIC_TIME_UNITS: 5}))
        self.assertIsInstance(config.deterministic_time_units, float)

    def test_invalid_json(self) -> None:
        self.assert_rejected("{ pas du JSON")

    def test_each_missing_key(self) -> None:
        for key in CpSatAloneKeys.REQUIRED:
            with self.subTest(key=key):
                content = raw_config()
                del content[key]
                self.assert_rejected(content, key)

    def test_unknown_key(self) -> None:
        self.assert_rejected(raw_config(threads=8), "threads")

    def test_unknown_model(self) -> None:
        self.assert_rejected(raw_config(**{CpSatAloneKeys.MODEL: "souple"}), "souple", ModelChoices.REFERENCE)

    def test_unknown_instance(self) -> None:
        self.assert_rejected(raw_config(**{CpSatAloneKeys.INSTANCE: UNKNOWN_INSTANCE}), UNKNOWN_INSTANCE)

    def test_zero_and_negative_limits(self) -> None:
        for value in (0, -1.5):
            with self.subTest(value=value):
                self.assert_rejected(raw_config(**{CpSatAloneKeys.DETERMINISTIC_TIME_UNITS: value}), str(value))

    def test_wrong_types(self) -> None:
        cases = {
            CpSatAloneKeys.SEED: "0",
            CpSatAloneKeys.DETERMINISTIC_TIME_UNITS: "5",
            CpSatAloneKeys.INSTANCE: 3,
            CpSatAloneKeys.DESCRIPTION: None,
        }
        for key, value in cases.items():
            with self.subTest(key=key):
                self.assert_rejected(raw_config(**{key: value}), key)

    def test_boolean_is_not_a_number(self) -> None:
        self.assert_rejected(raw_config(**{CpSatAloneKeys.SEED: True}), CpSatAloneKeys.SEED)


class TestParseOutput(unittest.TestCase):
    """Lecture de la sortie de ``minizinc -i -s``."""

    def test_stat_values(self) -> None:
        self.assertEqual(parse_stat_value("42"), 42)
        self.assertEqual(parse_stat_value("7.00008e+06"), 7.00008e+06)
        self.assertEqual(parse_stat_value('"minimize"'), "minimize")

    def test_one_point_per_solution_in_order(self) -> None:
        trace = parse_minizinc_output(SAMPLE_OUTPUT)
        objectives = [point[CpSatAloneResultKeys.OBJECTIVE] for point in trace.solutions]
        self.assertEqual(objectives, [2000010, 120])

    def test_scientific_objective_rounded_to_integer(self) -> None:
        first = parse_minizinc_output(SAMPLE_OUTPUT).solutions[0]
        self.assertIsInstance(first[CpSatAloneResultKeys.OBJECTIVE], int)

    def test_effort_attached_to_each_solution(self) -> None:
        second = parse_minizinc_output(SAMPLE_OUTPUT).solutions[1]
        self.assertEqual(second[CpSatAloneResultKeys.SOLVE_TIME_SECONDS], 1.5)
        self.assertEqual(second[CpSatAloneResultKeys.PROPAGATIONS], 4000)
        self.assertEqual(second[CpSatAloneResultKeys.FAILURES], 9)

    def test_compilation_statistics_are_not_a_solution(self) -> None:
        trace = parse_minizinc_output(SAMPLE_OUTPUT)
        self.assertEqual(len(trace.solutions), 2)

    def test_proof_and_final_statistics(self) -> None:
        trace = parse_minizinc_output(SAMPLE_OUTPUT)
        self.assertTrue(trace.proven_optimal)
        self.assertEqual(trace.final_statistics["propagations"], 4500)
        self.assertEqual(trace.final_statistics["nSolutions"], 2)

    def test_budget_exhausted_without_proof(self) -> None:
        output = SAMPLE_OUTPUT.replace("==========\n", "")
        trace = parse_minizinc_output(output)
        self.assertFalse(trace.proven_optimal)
        self.assertEqual(len(trace.solutions), 2)

    def test_no_solution(self) -> None:
        trace = parse_minizinc_output("%%%mzn-stat: solveTime=5.0\n=====UNKNOWN=====\n")
        self.assertEqual(trace.solutions, [])
        self.assertFalse(trace.proven_optimal)

    def test_unsatisfiable_is_not_a_proof_of_optimality(self) -> None:
        trace = parse_minizinc_output("=====UNSATISFIABLE=====\n==========\n")
        self.assertFalse(trace.proven_optimal)

    def test_empty_output(self) -> None:
        trace = parse_minizinc_output("")
        self.assertEqual((trace.solutions, trace.proven_optimal, trace.final_statistics), ([], False, {}))


class TestCommand(unittest.TestCase):
    """Ligne de commande ``minizinc``."""

    def test_reference_command(self) -> None:
        command = minizinc_command(config_of(), EXECUTABLE)
        self.assertEqual(command[0], str(EXECUTABLE))
        self.assertEqual(command[-2:], [str(ProjectPaths.REFERENCE_MODEL_FILE), str(config_of().instance_path)])
        threads_index = command.index(MiniZincCliFlags.THREADS)
        self.assertEqual(command[threads_index + 1], str(CpSatAloneDefaults.THREADS))
        self.assertIn(MiniZincCliFlags.ALL_INTERMEDIATE_SOLUTIONS, command)
        self.assertIn(MiniZincCliFlags.STATISTICS, command)
        self.assertNotIn(MiniZincCliFlags.DEFINE, command)

    def test_limit_and_seed_passed_to_cp_sat(self) -> None:
        command = minizinc_command(config_of(), EXECUTABLE)
        parameters = command[command.index(MiniZincCliFlags.LONG_OPTION_PREFIX + CpSatFlags.FZN_FLAGS_OPTION) + 1]
        self.assertIn(CpSatFlags.MAX_DETERMINISTIC_TIME + ":" + str(UNITS), parameters)
        self.assertIn(CpSatFlags.RANDOM_SEED + ":" + str(SEED), parameters)

    def test_relaxed_command_defines_coverage_weight(self) -> None:
        command = minizinc_command(config_of(ModelChoices.RELAXED), EXECUTABLE)
        definition = command[command.index(MiniZincCliFlags.DEFINE) + 1]
        self.assertIn(RelaxedModelNames.COVERAGE_WEIGHT, definition)
        self.assertIn(str(PenaltyWeights().coverage_violation), definition)
        self.assertEqual(command[-2], str(ProjectPaths.RELAXED_MODEL_FILE))


class TestDocumentAndLog(unittest.TestCase):
    """Document de résultats et entrée d'EXPLOG.md."""

    def document(self, output: str = SAMPLE_OUTPUT) -> dict:
        trace = parse_minizinc_output(output)
        return results_document(config_of(), trace, DURATION, VERSION, FIXED_TIME, GIT_COMMIT, False)

    def test_version_text(self) -> None:
        self.assertEqual(version_text((2, 10, 0)), VERSION)

    def test_document_content(self) -> None:
        document = self.document()
        self.assertEqual(document[CpSatAloneResultKeys.EXPERIMENT], NAME)
        self.assertEqual(document[CpSatAloneResultKeys.BEST_OBJECTIVE], 120)
        self.assertTrue(document[CpSatAloneResultKeys.PROVEN_OPTIMAL])
        self.assertEqual(len(document[CpSatAloneResultKeys.SOLUTIONS]), 2)
        self.assertEqual(document[CpSatAloneResultKeys.THREADS], CpSatAloneDefaults.THREADS)
        self.assertEqual(document[CpSatAloneResultKeys.MINIZINC_VERSION], VERSION)
        self.assertEqual(document[CpSatAloneResultKeys.MODEL_FILE], "src/model/horaire.mzn")
        json.dumps(document)

    def test_document_without_solution(self) -> None:
        document = self.document("=====UNKNOWN=====\n")
        self.assertIsNone(document[CpSatAloneResultKeys.BEST_OBJECTIVE])

    def test_log_entry(self) -> None:
        entry = explog_entry(self.document(), Path("/tmp/res.json"), FIXED_TIME)
        for fragment in (NAME, INSTANCE, ModelChoices.REFERENCE, "120", CpSatAloneTexts.PROVEN, "4500", GIT_COMMIT):
            self.assertIn(fragment, entry)

    def test_log_entry_without_proof_or_solution(self) -> None:
        not_proven = explog_entry(self.document(SAMPLE_OUTPUT.replace("==========\n", "")), Path("r.json"), FIXED_TIME)
        self.assertIn(CpSatAloneTexts.NOT_PROVEN, not_proven)
        nothing = explog_entry(self.document("=====UNKNOWN=====\n"), Path("r.json"), FIXED_TIME)
        self.assertIn(CpSatAloneTexts.NO_SOLUTION, nothing)


class TestCpSatAloneEndToEnd(unittest.TestCase):
    """Résolution réelle et courte de bench_1 par la ligne de commande (MiniZinc et CP-SAT requis)."""

    def test_bench_1_reaches_and_proves_optimum(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            config_path = write_config(root, raw_config(**{CpSatAloneKeys.DETERMINISTIC_TIME_UNITS: END_TO_END_UNITS}))
            log_path = root / "EXPLOG.md"
            results_path = main(
                [str(config_path), "--results-dir", str(root / "results"), "--log", str(log_path)],
                clock=lambda: FIXED_TIME,
            )
            document = json.loads(results_path.read_text(encoding="utf-8"))
            self.assertEqual(document[CpSatAloneResultKeys.BEST_OBJECTIVE], BENCH_1_OPTIMUM)
            self.assertTrue(document[CpSatAloneResultKeys.PROVEN_OPTIMAL])
            objectives = [point[CpSatAloneResultKeys.OBJECTIVE] for point in document[CpSatAloneResultKeys.SOLUTIONS]]
            self.assertEqual(objectives, sorted(objectives, reverse=True))
            times = [point[CpSatAloneResultKeys.SOLVE_TIME_SECONDS] for point in document[CpSatAloneResultKeys.SOLUTIONS]]
            self.assertEqual(times, sorted(times))
            self.assertIn(NAME, log_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
