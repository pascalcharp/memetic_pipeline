"""Tests de l'infrastructure d'observabilité (src/observability/) — scaffold commun de la semaine du 16 novembre.

Couvre ce que Claude a écrit (marqué (C) dans docs/archive/TODO.md, 8b) : schéma des enregistrements, destinations, diffusion par
``ObservationHub``, journal de diagnostic, répertoire d'exécution. Les collecteurs (Mély) sont testés dans
``tests/test_collectors.py``.
"""

import csv
import io
import json
import logging
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from src.observability.collectors import MetricCollector
from src.observability.events import (
    Converged,
    Event,
    EventNames,
    Record,
    RecordSchema,
    make_record,
)
from src.observability.hub import ObservationHub
from src.observability.logging_config import LoggingDefaults, configure_logging, get_logger
from src.observability.run_directory import (
    ConfigFields,
    RunDirectory,
    RunDirectoryDefaults,
    RunDirectoryExistsError,
    current_git_commit,
    package_versions,
    working_tree_is_dirty,
)
from src.observability.sinks import (
    ConsoleSink,
    CsvColumnsMismatchError,
    CsvSink,
    InvalidRecordError,
    JsonlSink,
    MemorySink,
    NullSink,
    SinkClosedError,
)

RECORD_TYPE: str = "test_record"
OTHER_RECORD_TYPE: str = "other_record"
ACCENTED_TEXT: str = "génération"
FIRST_VALUE: int = 1
SECOND_VALUE: int = 2
GENERATION: int = 3
EXPERIMENT: str = "experience_test"
RUN_ID: str = "run_test"
SEED: int = 42
PARAMETERS: dict[str, int] = {"population_size": 10}
LOG_MESSAGE: str = "message de diagnostic"
MODULE_NAME: str = "module_test"


def record(value: int = FIRST_VALUE, record_type: str = RECORD_TYPE) -> Record:
    return make_record(record_type, value=value, label=ACCENTED_TEXT)


class EchoCollector(MetricCollector):
    """Collecteur factice : un enregistrement par événement, qui reprend le nom de l'événement."""

    def on_event(self, event: Event) -> list[Record]:
        return [make_record(RECORD_TYPE, source=event.NAME)]


class SilentCollector(MetricCollector):
    """Collecteur factice qui ne produit rien."""

    def on_event(self, event: Event) -> list[Record]:
        return []


class BrokenCollector(MetricCollector):
    """Collecteur factice qui produit un enregistrement sans les champs obligatoires."""

    def on_event(self, event: Event) -> list[Record]:
        return [{"value": FIRST_VALUE}]


class TestRecordSchema(unittest.TestCase):

    def test_givenFields_whenMakeRecord_thenSchemaVersionEventAndFieldsArePresent(self) -> None:
        made = make_record(RECORD_TYPE, value=FIRST_VALUE)
        self.assertEqual(made[RecordSchema.VERSION_FIELD], RecordSchema.VERSION)
        self.assertEqual(made[RecordSchema.EVENT_FIELD], RECORD_TYPE)
        self.assertEqual(made["value"], FIRST_VALUE)

    def test_givenEventClasses_whenReadingName_thenNameComesFromCatalogue(self) -> None:
        self.assertEqual(Converged.NAME, EventNames.CONVERGED)
        self.assertEqual(Converged(generation=GENERATION).generation, GENERATION)


class TestSinks(unittest.TestCase):

    def test_givenRecordWithoutEvent_whenWrite_thenRaisesNamingMissingField(self) -> None:
        for sink in (NullSink(), MemorySink(), ConsoleSink(io.StringIO())):
            with self.subTest(sink=type(sink).__name__):
                with self.assertRaises(InvalidRecordError) as context:
                    sink.write({RecordSchema.VERSION_FIELD: RecordSchema.VERSION})
                self.assertIn(RecordSchema.EVENT_FIELD, str(context.exception))

    def test_givenRecords_whenMemorySink_thenKeepsCopiesInOrderAndFiltersByEvent(self) -> None:
        sink = MemorySink()
        first = record(FIRST_VALUE)
        sink.write(first)
        sink.write(record(SECOND_VALUE, OTHER_RECORD_TYPE))
        first["value"] = SECOND_VALUE
        self.assertEqual([r["value"] for r in sink.records], [FIRST_VALUE, SECOND_VALUE])
        self.assertEqual(len(sink.of_event(RECORD_TYPE)), 1)

    def test_givenRecord_whenConsoleSink_thenWritesOneJsonLine(self) -> None:
        stream = io.StringIO()
        ConsoleSink(stream).write(record())
        lines = stream.getvalue().splitlines()
        self.assertEqual(len(lines), 1)
        self.assertEqual(json.loads(lines[0]), record())

    def test_givenRecords_whenJsonlSink_thenFileIsReadableLineByLineWithAccents(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "events.jsonl"
            sink = JsonlSink(path)
            sink.write(record(FIRST_VALUE))
            sink.write(record(SECOND_VALUE))
            sink.close()
            text = path.read_text(encoding="utf-8")
            self.assertIn(ACCENTED_TEXT, text)
            self.assertEqual([json.loads(line)["value"] for line in text.splitlines()], [FIRST_VALUE, SECOND_VALUE])

    def test_givenClosedJsonlSink_whenWrite_thenRaisesSinkClosedError(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            sink = JsonlSink(Path(directory) / "events.jsonl")
            sink.close()
            with self.assertRaises(SinkClosedError):
                sink.write(record())

    def test_givenRecordsOfSeveralTypes_whenCsvSink_thenOnlyItsTypeIsWrittenWithHeader(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "generations.csv"
            sink = CsvSink(path, RECORD_TYPE)
            sink.write(record(FIRST_VALUE))
            sink.write(record(SECOND_VALUE, OTHER_RECORD_TYPE))
            sink.write(record(SECOND_VALUE))
            sink.close()
            with path.open(encoding="utf-8", newline="") as file:
                rows = list(csv.DictReader(file))
            self.assertEqual([int(row["value"]) for row in rows], [FIRST_VALUE, SECOND_VALUE])
            self.assertEqual(rows[0]["label"], ACCENTED_TEXT)

    def test_givenRecordWithOtherFields_whenCsvSink_thenRaisesNamingThePath(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "generations.csv"
            sink = CsvSink(path, RECORD_TYPE)
            sink.write(record())
            with self.assertRaises(CsvColumnsMismatchError) as context:
                sink.write(make_record(RECORD_TYPE, other=FIRST_VALUE))
            sink.close()
            self.assertIn(str(path), str(context.exception))


class TestObservationHub(unittest.TestCase):

    def test_givenCollectorsAndSinks_whenEmit_thenEverySinkReceivesEveryRecordInOrder(self) -> None:
        first_sink, second_sink = MemorySink(), MemorySink()
        hub = ObservationHub([EchoCollector(), SilentCollector(), EchoCollector()], [first_sink, second_sink])
        hub.emit(Converged(generation=GENERATION))
        for sink in (first_sink, second_sink):
            self.assertEqual([r["source"] for r in sink.records], [EventNames.CONVERGED, EventNames.CONVERGED])

    def test_givenNoSink_whenEmit_thenRecordsGoToANullSink(self) -> None:
        hub = ObservationHub([EchoCollector()])
        self.assertEqual(len(hub.sinks), 1)
        self.assertIsInstance(hub.sinks[0], NullSink)
        hub.emit(Converged(generation=GENERATION))

    def test_givenCollectorProducingInvalidRecord_whenEmit_thenRaisesInvalidRecordError(self) -> None:
        hub = ObservationHub([BrokenCollector()], [MemorySink()])
        with self.assertRaises(InvalidRecordError):
            hub.emit(Converged(generation=GENERATION))


class TestLogging(unittest.TestCase):

    def tearDown(self) -> None:
        configure_logging(console=False)

    def test_givenRunLog_whenConfigureAndLog_thenMessageIsInFile(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_log = Path(directory) / "run.log"
            configure_logging(level=logging.INFO, console=False, run_log=run_log)
            get_logger(MODULE_NAME).info(LOG_MESSAGE)
            configure_logging(console=False)
            self.assertIn(LOG_MESSAGE, run_log.read_text(encoding="utf-8"))

    def test_givenLevelWarning_whenLogInfo_thenMessageIsNotWritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run_log = Path(directory) / "run.log"
            configure_logging(level=logging.WARNING, console=False, run_log=run_log)
            get_logger(MODULE_NAME).info(LOG_MESSAGE)
            configure_logging(console=False)
            self.assertNotIn(LOG_MESSAGE, run_log.read_text(encoding="utf-8"))

    def test_givenTwoConfigurations_whenConfigure_thenHandlersAreNotDuplicated(self) -> None:
        configure_logging(console=True)
        logger = configure_logging(console=True)
        self.assertEqual(len(logger.handlers), 1)
        self.assertFalse(logger.propagate)
        self.assertEqual(logger.name, LoggingDefaults.LOGGER_NAME)


class TestRunDirectory(unittest.TestCase):

    def test_givenExperimentAndRunId_whenCreate_thenDirectoryAndFilePathsExist(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run = RunDirectory.create(EXPERIMENT, RUN_ID, results_root=Path(directory))
            self.assertTrue(run.path.is_dir())
            self.assertEqual(run.path, Path(directory) / EXPERIMENT / RUN_ID)
            for file_path in (run.config_path, run.events_path, run.generations_path, run.run_log_path):
                self.assertEqual(file_path.parent, run.path)

    def test_givenExistingRunId_whenCreate_thenRaisesNamingThePath(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            RunDirectory.create(EXPERIMENT, RUN_ID, results_root=Path(directory))
            with self.assertRaises(RunDirectoryExistsError) as context:
                RunDirectory.create(EXPERIMENT, RUN_ID, results_root=Path(directory))
            self.assertIn(RUN_ID, str(context.exception))

    def test_givenNoRunId_whenCreate_thenAnIdentifierIsGenerated(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run = RunDirectory.create(EXPERIMENT, results_root=Path(directory))
            self.assertTrue(run.run_id)
            self.assertTrue(run.path.is_dir())

    def test_givenSeedAndParameters_whenWriteConfig_thenConfigJsonHasEveryField(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            run = RunDirectory.create(EXPERIMENT, RUN_ID, results_root=Path(directory))
            config = json.loads(run.write_config(SEED, PARAMETERS).read_text(encoding="utf-8"))
            self.assertEqual(config[ConfigFields.SEED], SEED)
            self.assertEqual(config[ConfigFields.PARAMETERS], PARAMETERS)
            self.assertEqual(config[ConfigFields.EXPERIMENT], EXPERIMENT)
            for field in (ConfigFields.GIT_COMMIT, ConfigFields.PYTHON_VERSION, ConfigFields.PACKAGES,
                          ConfigFields.CREATED_AT, ConfigFields.RUN_ID):
                self.assertIn(field, config)

    def test_givenRepository_whenCurrentGitCommit_thenReturnsANonEmptyString(self) -> None:
        self.assertTrue(current_git_commit())

    def test_givenMissingPackage_whenPackageVersions_thenUnknownValue(self) -> None:
        missing = "paquet_inexistant_pour_le_test"
        versions = package_versions((missing,))
        self.assertEqual(versions[missing], RunDirectoryDefaults.UNKNOWN_VALUE)


# ---------------------------------------------------------------------------------------------------------------------
# État de la copie de travail (git_dirty)
# ---------------------------------------------------------------------------------------------------------------------

GIT_IDENTITY: tuple[str, ...] = ("-c", "user.name=Test", "-c", "user.email=test@example.com")


@unittest.skipUnless(shutil.which("git"), "git absent (image Docker de la CI) : aucun dépôt temporaire possible")
class TestWorkingTreeIsDirty(unittest.TestCase):
    """Dans un dépôt Git temporaire, avec un fichier commité et un répertoire de sorties à exclure."""

    def setUp(self) -> None:
        self.directory = tempfile.TemporaryDirectory()
        self.root = Path(self.directory.name)
        self.git("init", "--quiet")
        (self.root / "code.py").write_text("x = 1\n", encoding="utf-8")
        (self.root / "sorties").mkdir()
        (self.root / "sorties" / "a.json").write_text("{}", encoding="utf-8")
        self.git("add", ".")
        self.git(*GIT_IDENTITY, "commit", "--quiet", "-m", "initial")
        self.excluded = (Path("sorties"),)

    def tearDown(self) -> None:
        self.directory.cleanup()

    def git(self, *arguments: str) -> None:
        subprocess.run(("git",) + arguments, cwd=self.root, check=True, capture_output=True)

    def test_givenCleanTree_whenChecked_thenFalse(self) -> None:
        self.assertFalse(working_tree_is_dirty(self.root))

    def test_givenModifiedTrackedFile_whenChecked_thenTrue(self) -> None:
        (self.root / "code.py").write_text("x = 2\n", encoding="utf-8")
        self.assertTrue(working_tree_is_dirty(self.root, self.excluded))

    def test_givenUntrackedFile_whenChecked_thenTrue(self) -> None:
        (self.root / "nouveau.py").write_text("y = 1\n", encoding="utf-8")
        self.assertTrue(working_tree_is_dirty(self.root, self.excluded))

    def test_givenChangesOnlyInExcludedPaths_whenChecked_thenFalse(self) -> None:
        (self.root / "sorties" / "a.json").write_text('{"b": 1}', encoding="utf-8")
        (self.root / "sorties" / "nouveau.json").write_text("{}", encoding="utf-8")
        self.assertFalse(working_tree_is_dirty(self.root, self.excluded))
        self.assertTrue(working_tree_is_dirty(self.root))

    def test_givenNotARepository_whenChecked_thenNone(self) -> None:
        with tempfile.TemporaryDirectory() as other:
            self.assertIsNone(working_tree_is_dirty(Path(other)))


if __name__ == "__main__":
    unittest.main()
