"""Constantes de configuration du projet : chemins et paramètres d'environnement MiniZinc."""

from pathlib import Path


class ProjectPaths:
    """Chemins des répertoires et fichiers du projet, calculés à partir de la racine du dépôt."""

    ROOT: Path = Path(__file__).resolve().parent.parent
    DATA_DIR: Path = ROOT / "data"
    MODEL_DIR: Path = ROOT / "src" / "model"
    MODEL_FILE: Path = MODEL_DIR / "horaire.mzn"


class MiniZincConfig:
    """Paramètres de localisation de MiniZinc et choix du solveur par défaut."""

    # Variable d'environnement permettant d'imposer l'exécutable MiniZinc (ex. dans Docker).
    # Si elle est absente, on se fie à la recherche par défaut de minizinc-python
    # (PATH, puis emplacements usuels comme /Applications/MiniZincIDE.app sur macOS).
    EXECUTABLE_ENV_VAR: str = "MINIZINC_PATH"

    DEFAULT_SOLVER_ID: str = "cp-sat"