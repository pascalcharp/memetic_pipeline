"""Destinations des enregistrements (décision D8) : où écrire les données d'expérience.

Une destination (``RecordSink``) reçoit des enregistrements déjà construits (``events.make_record``) et les écrit.
Elle ne calcule rien. Le choix des destinations se fait dans la configuration de l'expérience :
    - ``NullSink`` : n'écrit rien (par défaut) ;
    - ``MemorySink`` : garde les enregistrements en mémoire (tests) ;
    - ``ConsoleSink`` : une ligne JSON par enregistrement, sur un flux texte (la sortie standard par défaut) ;
    - ``JsonlSink`` : une ligne JSON par enregistrement, dans un fichier (``events.jsonl``) ;
    - ``CsvSink`` : un tableau CSV pour un seul type d'enregistrement (par exemple ``generations.csv``).

Les valeurs des enregistrements doivent être sérialisables en JSON avec la bibliothèque standard : un type numpy
fait échouer l'écriture (``TypeError``) au lieu d'être converti en silence.
"""

import csv
import json
import sys
from abc import ABC, abstractmethod
from collections.abc import Mapping
from pathlib import Path
from typing import Any, TextIO

from src.observability.events import Record, RecordSchema


class SinkDefaults:
    """Paramètres d'écriture des destinations."""

    ENCODING: str = "utf-8"
    # Les caractères accentués restent lisibles dans les fichiers (pas d'échappement \\u).
    JSON_ENSURE_ASCII: bool = False


class SinkMessages:
    """Gabarits des messages d'erreur des destinations."""

    MISSING_FIELD: str = "L'enregistrement n'a pas le champ obligatoire « {field} » : {record}."
    CSV_COLUMNS_MISMATCH: str = (
        "Le fichier CSV {path} a les colonnes {expected} ; l'enregistrement reçu a les champs {found}."
    )
    SINK_CLOSED: str = "La destination {sink} est fermée : impossible d'écrire."


class ObservabilityError(Exception):
    """Erreur de base de l'observabilité."""


class InvalidRecordError(ObservabilityError):
    """Un enregistrement n'a pas les champs obligatoires de ``RecordSchema``."""


class CsvColumnsMismatchError(ObservabilityError):
    """Un enregistrement n'a pas les mêmes champs que les colonnes du fichier CSV."""


class SinkClosedError(ObservabilityError):
    """On écrit dans une destination déjà fermée."""


def check_record(record: Mapping[str, Any]) -> None:
    """Vérifie que ``record`` contient ``schema_version`` et ``event``.

    Raises:
        InvalidRecordError: sinon ; le champ manquant est dans le message.
    """
    for field in (RecordSchema.VERSION_FIELD, RecordSchema.EVENT_FIELD):
        if field not in record:
            raise InvalidRecordError(SinkMessages.MISSING_FIELD.format(field=field, record=dict(record)))


def to_json_line(record: Mapping[str, Any]) -> str:
    """L'enregistrement en une ligne JSON, sans saut de ligne final."""
    return json.dumps(dict(record), ensure_ascii=SinkDefaults.JSON_ENSURE_ASCII)


# ---------------------------------------------------------------------------------------------------------------------
# Interface
# ---------------------------------------------------------------------------------------------------------------------

class RecordSink(ABC):
    """Destination des enregistrements."""

    @abstractmethod
    def write(self, record: Record) -> None:
        """Écrit ``record``.

        Raises:
            InvalidRecordError: si ``record`` n'a pas les champs de ``RecordSchema``.
            SinkClosedError: si la destination est fermée.
        """

    def close(self) -> None:
        """Libère les ressources (fichiers). Par défaut, rien à faire."""


# ---------------------------------------------------------------------------------------------------------------------
# Destinations
# ---------------------------------------------------------------------------------------------------------------------

class NullSink(RecordSink):
    """N'écrit rien : la destination par défaut quand l'expérience n'en demande aucune."""

    def write(self, record: Record) -> None:
        check_record(record)


class MemorySink(RecordSink):
    """Garde une copie de chaque enregistrement reçu, dans l'ordre, dans ``records`` : pour les tests."""

    def __init__(self) -> None:
        self.records: list[Record] = []

    def write(self, record: Record) -> None:
        check_record(record)
        self.records.append(dict(record))

    def of_event(self, event: str) -> list[Record]:
        """Les enregistrements reçus dont le type est ``event``, dans l'ordre."""
        return [record for record in self.records if record[RecordSchema.EVENT_FIELD] == event]


class ConsoleSink(RecordSink):
    """Une ligne JSON par enregistrement, sur ``stream`` (la sortie standard par défaut)."""

    def __init__(self, stream: TextIO | None = None) -> None:
        self.stream = stream if stream is not None else sys.stdout

    def write(self, record: Record) -> None:
        check_record(record)
        print(to_json_line(record), file=self.stream)


class JsonlSink(RecordSink):
    """Une ligne JSON par enregistrement, dans le fichier ``path`` (créé ou écrasé)."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self._file: TextIO | None = path.open("w", encoding=SinkDefaults.ENCODING)

    def write(self, record: Record) -> None:
        check_record(record)
        if self._file is None:
            raise SinkClosedError(SinkMessages.SINK_CLOSED.format(sink=self.path))
        self._file.write(to_json_line(record) + "\n")
        self._file.flush()

    def close(self) -> None:
        if self._file is not None:
            self._file.close()
            self._file = None


class CsvSink(RecordSink):
    """Tableau CSV des enregistrements de type ``event`` ; les autres types sont ignorés.

    Les colonnes sont les champs du premier enregistrement reçu, dans leur ordre ; chaque enregistrement suivant
    doit avoir exactement les mêmes champs. Le fichier ``path`` est créé ou écrasé.
    """

    def __init__(self, path: Path, event: str) -> None:
        self.path = path
        self.event = event
        self._file: TextIO | None = path.open("w", encoding=SinkDefaults.ENCODING, newline="")
        self._writer: csv.DictWriter | None = None

    def write(self, record: Record) -> None:
        """
        Raises:
            CsvColumnsMismatchError: si ``record`` n'a pas les mêmes champs que les colonnes du fichier.
        """
        check_record(record)
        if self._file is None:
            raise SinkClosedError(SinkMessages.SINK_CLOSED.format(sink=self.path))
        if record[RecordSchema.EVENT_FIELD] != self.event:
            return
        if self._writer is None:
            self._writer = csv.DictWriter(self._file, fieldnames=list(record.keys()))
            self._writer.writeheader()
        expected_columns = list(self._writer.fieldnames)
        if sorted(record.keys()) != sorted(expected_columns):
            raise CsvColumnsMismatchError(SinkMessages.CSV_COLUMNS_MISMATCH.format(
                path=self.path, expected=expected_columns, found=list(record.keys())
            ))
        self._writer.writerow(record)
        self._file.flush()

    def close(self) -> None:
        if self._file is not None:
            self._file.close()
            self._file = None
