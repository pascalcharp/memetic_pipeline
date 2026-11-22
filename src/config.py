"""Constantes de configuration du projet : chemins et paramètres d'environnement MiniZinc."""

from pathlib import Path


class ProjectPaths:
    """Chemins des répertoires et fichiers du projet, calculés à partir de la racine du dépôt."""

    ROOT: Path = Path(__file__).resolve().parent.parent
    DATA_DIR: Path = ROOT / "data"
    MODEL_DIR: Path = ROOT / "src" / "model"
    # Modèle original fourni, couverture « au moins 1 » dure ; gardé inchangé comme référence (D12).
    REFERENCE_MODEL_FILE: Path = MODEL_DIR / "horaire.mzn"
    # Modèle du pipeline : « au moins 1 » pénalisée, même fonction de coût que CostEvaluator.total (D12).
    RELAXED_MODEL_FILE: Path = MODEL_DIR / "horaire_assoupli.mzn"
    # Expériences (étape 10) : configurations, résultats (un répertoire par jour) et journal des expériences.
    EXPERIMENTS_DIR: Path = ROOT / "experiments"
    EXPERIMENT_CONFIG_DIR: Path = EXPERIMENTS_DIR / "config"
    EXPERIMENT_RESULTS_DIR: Path = EXPERIMENTS_DIR / "results"
    EXPLOG_FILE: Path = EXPERIMENTS_DIR / "EXPLOG.md"


class MiniZincConfig:
    """Paramètres de localisation de MiniZinc et choix du solveur par défaut."""

    # Variable d'environnement permettant d'imposer l'exécutable MiniZinc (ex. dans Docker).
    # Si elle est absente, on se fie à la recherche par défaut de minizinc-python
    # (PATH, puis emplacements usuels comme /Applications/MiniZincIDE.app sur macOS).
    EXECUTABLE_ENV_VAR: str = "MINIZINC_PATH"

    DEFAULT_SOLVER_ID: str = "cp-sat"