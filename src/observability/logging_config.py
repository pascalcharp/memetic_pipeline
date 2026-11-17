"""Journal de diagnostic (décision D8) : messages texte à niveaux, distincts des données d'expérience.

Tout le projet écrit dans le logger ``LoggingDefaults.LOGGER_NAME`` ou dans ses enfants : dans un module, obtenir
son logger par ``get_logger(__name__)``, qui le rattache au logger du projet.
``configure_logging`` choisit le niveau et les sorties : la console et/ou le fichier ``run.log`` de l'exécution.
"""

import logging
import sys
from pathlib import Path

from src.observability.sinks import SinkDefaults


class LoggingDefaults:
    """Paramètres par défaut du journal de diagnostic."""

    LOGGER_NAME: str = "memetic"
    LEVEL: int = logging.INFO
    FORMAT: str = "%(asctime)s %(levelname)s %(name)s : %(message)s"
    CHILD_LOGGER_NAME: str = "{root}.{module}"


def get_logger(module_name: str) -> logging.Logger:
    """Logger d'un module, enfant du logger du projet (``memetic.<module_name>``)."""
    child_name = LoggingDefaults.CHILD_LOGGER_NAME.format(root=LoggingDefaults.LOGGER_NAME, module=module_name)
    return logging.getLogger(child_name)


def configure_logging(
        level: int = LoggingDefaults.LEVEL,
        console: bool = True,
        run_log: Path | None = None,
) -> logging.Logger:
    """Configure le logger du projet et le rend.

    Remplace les sorties d'une configuration précédente : appeler deux fois ne double pas les messages.
    Les messages ne remontent pas au logger racine (``propagate = False``).

    Args:
        level: niveau minimal des messages (``logging.DEBUG``, ``logging.INFO``, …).
        console: écrire sur la sortie d'erreur standard.
        run_log: fichier où écrire aussi les messages (par exemple ``RunDirectory.run_log_path``), ou ``None``.
    """
    logger = logging.getLogger(LoggingDefaults.LOGGER_NAME)
    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()
    logger.setLevel(level)
    logger.propagate = False
    formatter = logging.Formatter(LoggingDefaults.FORMAT)
    if console:
        console_handler = logging.StreamHandler(sys.stderr)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    if run_log is not None:
        file_handler = logging.FileHandler(run_log, encoding=SinkDefaults.ENCODING)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger
