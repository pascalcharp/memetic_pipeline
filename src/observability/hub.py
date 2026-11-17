"""Diffusion des événements (patron Observateur, décision D8).

Le moteur ne connaît que ``ObservationHub`` : il lui passe chaque événement, le hub le donne à chaque collecteur,
puis écrit dans chaque destination les enregistrements que les collecteurs ont produits.

Règles de D8 rappelées :
    - un collecteur ne consomme jamais le générateur aléatoire du moteur : observer ne change pas l'exécution ;
    - les événements sont émis par le fil principal, après chaque lot (D7) ; le hub n'est pas partagé entre fils.
"""

from collections.abc import Sequence

from src.observability.collectors import MetricCollector
from src.observability.events import Event
from src.observability.sinks import NullSink, RecordSink, check_record


class ObservationHub:
    """Relie le moteur aux collecteurs et aux destinations.

    Sans destination, les enregistrements vont dans un ``NullSink``.
    """

    def __init__(self, collectors: Sequence[MetricCollector] = (), sinks: Sequence[RecordSink] = ()) -> None:
        self.collectors: tuple[MetricCollector, ...] = tuple(collectors)
        self.sinks: tuple[RecordSink, ...] = tuple(sinks) if sinks else (NullSink(),)

    def emit(self, event: Event) -> None:
        """Donne ``event`` à chaque collecteur, dans l'ordre, et écrit leurs enregistrements dans chaque destination.

        Raises:
            InvalidRecordError: si un collecteur produit un enregistrement sans les champs de ``RecordSchema``.
        """
        for collector in self.collectors:
            for record in collector.on_event(event):
                check_record(record)
                for sink in self.sinks:
                    sink.write(record)

    def close(self) -> None:
        """Ferme toutes les destinations."""
        for sink in self.sinks:
            sink.close()
