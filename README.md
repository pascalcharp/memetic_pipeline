# Algorithme mémétique pour la confection d'horaires

[![Tests](https://github.com/pascalcharp/memetic_pipeline/actions/workflows/tests.yml/badge.svg)](https://github.com/pascalcharp/memetic_pipeline/actions/workflows/tests.yml)

Preuve de concept : un algorithme génétique couplé à une recherche locale par programmation par contraintes (MiniZinc + CP-SAT) pour construire des horaires de travail.

---

## 1. Description du projet

### 1.1 Le problème

On affecte des employés à des activités sur une journée découpée en périodes de 15 minutes. Chaque quart suit une structure imposée : début, première pause, dîner, deuxième pause et fin, avec une activité entre chaque jalon. L'horaire doit suivre au mieux la demande de chaque activité à chaque période. Le coût pénalise la sur-couverture et la sous-couverture.

Description détaillée (données, règles d'un quart, coût, exemple commenté) : [`docs/PROBLEME.md`](docs/PROBLEME.md). La référence formelle reste le modèle MiniZinc [`src/model/horaire.mzn`](src/model/horaire.mzn).

### 1.2 Algorithme employé

Un algorithme **mémétique** : une population d'horaires évolue par croisement et mutation, et chaque nouvel individu est amélioré par une recherche locale confiée à MiniZinc.

Pseudo-code, et correspondance avec le code : [`docs/ALGO.md`](docs/ALGO.md).

**État (22 novembre 2026)** : le prototype tourne de bout en bout (étape 9). Avec les vrais composants (CP-SAT en monothread, sous limite d'effort déterministe), il atteint l'optimum de `bench_1` (coût 94) en quatre générations. Prochaine étape : les expériences (étape 10).

### 1.3 Structure du projet

Arborescence actuelle du dépôt et rôle de chaque fichier : [`docs/PROJECT_STRUCT.md`](docs/PROJECT_STRUCT.md).

---

## 2. Je viens de cloner le dépôt. Et ensuite ?

### 2.1 Environnement requis

Deux possibilités :

| | Avec Docker (préféré) | En local |
|---|---|---|
| À installer | [Docker](https://docs.docker.com/get-docker/) | Python 3.13 et [MiniZinc 2.10](https://www.minizinc.org/downloads/) (le *bundle* inclut le solveur CP-SAT) |
| Avantage | Environnement identique pour tous, et identique à la CI | Débogage direct dans l'IDE (PyCharm) |

**En local, MiniZinc est localisé ainsi :**
1. la variable d'environnement `MINIZINC_PATH`, si elle est définie (chemin complet de l'exécutable `minizinc`) ;
2. sinon, la recherche par défaut : le `PATH`, puis les emplacements d'installation usuels. Sous macOS, `/Applications/MiniZincIDE.app` est trouvé même si MiniZinc n'est pas dans le `PATH`.

Pour vérifier que CP-SAT est disponible : `minizinc --solvers` doit afficher la ligne `OR Tools CP-SAT`.

### 2.2 Exécuter les tests

La suite complète prend environ une minute et demie, dont une trentaine de secondes pour deux exécutions complètes du moteur sur `bench_1` (`tests.test_integration`). Les mêmes tests tournent dans la CI (GitHub Actions) à chaque push sur `main` et pour chaque *pull request* vers `main`.

#### Avec Docker (préféré)

Depuis la racine du dépôt :

```bash
docker build -t memetic-pipeline .
docker run --rm memetic-pipeline
```

La commande par défaut de l'image lance toute la suite de tests. Le code est **copié** dans l'image au moment de la construction : après une modification, il faut soit reconstruire l'image, soit monter le dépôt dans le conteneur pour tester le code courant sans reconstruire :

```bash
docker run --rm -v "$PWD":/app memetic-pipeline
```

Dans l'image, six tests sont ignorés : un test propre à macOS, et les cinq tests de `working_tree_is_dirty`, qui ont besoin de `git` (absent de l'image). Le résultat attendu est `OK (skipped=6)`.

#### En local

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m unittest discover -v
```

Pour lancer un seul module de tests : `python -m unittest tests.test_shift_rules -v`.

Les commandes se lancent **depuis la racine du dépôt** (les imports partent de `src.`). Dans PyCharm, le répertoire de travail des configurations d'exécution doit être la racine.

### 2.3 Exécuter des expériences

Une expérience est décrite par un fichier de configuration JSON dans `experiments/config/`. Depuis la racine du dépôt :

```bash
python -m src.drivers.run_experiment experiments/config/integration_bench1.json
```

Le script construit le moteur avec l'assemblage de référence, l'exécute en mesurant tout, écrit un fichier de résultats JSON dans `experiments/results/<date du jour>/` et ajoute une entrée au journal des expériences, [`experiments/EXPLOG.md`](experiments/EXPLOG.md) : description, chemins, coût obtenu, effort cumulé du solveur. Options : `--results-dir` (autre répertoire de résultats) et `--log` (autre journal). Format de la configuration : docstring de `src/drivers/run_experiment.py`, et [`docs/HOWTO.md`, section 1](docs/HOWTO.md#1-je-veux-faire-rouler-la-boucle-mémétique).

Le moteur peut aussi être lancé depuis Python, avec l'assemblage de référence (`src/memetic/assembly.py`) :

```python
from src.config import ProjectPaths
from src.memetic.assembly import AssemblySettings, build_block_memetic_config
from src.memetic.engine import Memetic
from src.utils.io import load_instance

instance = load_instance(ProjectPaths.DATA_DIR / "bench_1.json")
settings = AssemblySettings(generations=4, master_seed=7, stagnation_generations=1)
result = Memetic(build_block_memetic_config(instance, settings)).run()
print(result.best.cost.total, result.generations, result.restarts)   # 94 4 1
```

Les paramètres (taille de la population, NR, NM, générations, graine, budget de CP-SAT, etc.) et leurs valeurs par défaut sont dans `AssemblySettings`. Pour mesurer une exécution et écrire ses résultats dans `results/`, voir [`docs/HOWTO.md`, section 1](docs/HOWTO.md#1-je-veux-faire-rouler-la-boucle-mémétique).

---

## 3. Comment faire ?

Guide pratique, avec pour chaque question les fichiers à modifier, l'interface à dériver et un exemple exécuté : [`docs/HOWTO.md`](docs/HOWTO.md).

Ce qui existe déjà, rôle par rôle (classes, paramètres, garanties, stratégies prévues) : [`docs/AVAILABLE_STRATEGIES.md`](docs/AVAILABLE_STRATEGIES.md).

- [Je veux faire rouler la boucle mémétique. Je m'y prends comment ?](docs/HOWTO.md#1-je-veux-faire-rouler-la-boucle-mémétique)
- [Je veux modifier la probabilité de crossover. Que faire ?](docs/HOWTO.md#2-je-veux-modifier-la-probabilité-de-crossover)
- [Je veux modifier la probabilité de mutation. Comment faire ça ?](docs/HOWTO.md#3-je-veux-modifier-la-probabilité-de-mutation)
- [Je veux créer un nouveau crossover. Je fais comment ?](docs/HOWTO.md#4-je-veux-créer-un-nouveau-crossover)
- [Je veux créer un nouvel opérateur de mutation. Je fais quoi ?](docs/HOWTO.md#5-je-veux-créer-un-nouvel-opérateur-de-mutation)
- [Je veux modifier la stratégie de sélection de la population. Que dois-je faire ?](docs/HOWTO.md#6-je-veux-modifier-la-stratégie-de-sélection-de-la-population)
- [Je veux une autre stratégie de redémarrage. Comment je devrais m'y prendre ?](docs/HOWTO.md#7-je-veux-une-autre-stratégie-de-redémarrage)
- [Je veux modifier les options de CP-SAT pour ma prochaine expérience. Que dois-je changer ?](docs/HOWTO.md#8-je-veux-modifier-les-options-de-cp-sat-pour-ma-prochaine-expérience)
- [Je veux essayer la boucle avec un autre solveur sur MiniZinc. On fait comment ?](docs/HOWTO.md#9-je-veux-essayer-la-boucle-avec-un-autre-solveur-sur-minizinc)
- [Je veux modifier l'encodage des génomes. Comment ?](docs/HOWTO.md#10-je-veux-modifier-lencodage-des-génomes)

---

## 4. Contribuer

### 4.1 Méthode de travail

Le projet suit une méthode stricte, décrite dans [`CLAUDE.md`](CLAUDE.md) :

- **une seule tâche à la fois**, planifiée au préalable dans `TODO.md` ;
- **des tests automatisés pour chaque tâche** (`unittest`), qui couvrent les cas nominaux et les cas limites ;
- **on ne passe à la tâche suivante que si tous les tests sont verts** ;
- **`TODO.md` et `DEVLOG.md` sont mis à jour** à la fin de chaque tâche validée.

Le projet est aussi pédagogique : les méthodes et algorithmes clés sont écrits à la main, et Claude Code prépare le squelette et vérifie le résultat. Dans le TODO, chaque tâche porte l'une de ces marques : **(C)** Claude écrit, **(P)** le développeur écrit et Claude vérifie, **(C→P)** Claude prépare le squelette et le développeur implémente.

### 4.2 État d'avancement

Étapes planifiées, tâches terminées et décisions de conception encore ouvertes : [`TODO.md`](TODO.md).

### 4.3 Décisions de conception

Le **pourquoi** du code. Les décisions de conception D1 à D14 sont énoncées en tête de [`TODO.md`](TODO.md). Leur contexte, les blocages rencontrés et les correctifs appliqués sont consignés dans l'ordre chronologique dans [`DEVLOG.md`](DEVLOG.md).

### 4.4 Conventions de code

Clarté avant concision, annotations de type, exceptions sur mesure, aucune constante ni message d'erreur codé en dur : voir la section *Style de Code & Lisibilité* de [`CLAUDE.md`](CLAUDE.md).
