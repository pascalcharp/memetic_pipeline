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

Pseudo-code : [`docs/ALGO.md`](docs/ALGO.md).

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

La suite complète prend une dizaine de secondes. Les mêmes tests tournent dans la CI (GitHub Actions) à chaque push sur `main`.

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

Sous Linux, un test propre à macOS est ignoré : le résultat attendu est `OK (skipped=1)`.

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

*À venir (étape 10 du [`TODO.md`](TODO.md)).*

---

## 3. Contribuer

### 3.1 Méthode de travail

Le projet suit une méthode stricte, décrite dans [`CLAUDE.md`](CLAUDE.md) :

- **une seule tâche à la fois**, planifiée au préalable dans `TODO.md` ;
- **des tests automatisés pour chaque tâche** (`unittest`), qui couvrent les cas nominaux et les cas limites ;
- **on ne passe à la tâche suivante que si tous les tests sont verts** ;
- **`TODO.md` et `DEVLOG.md` sont mis à jour** à la fin de chaque tâche validée.

Le projet est aussi pédagogique : les méthodes et algorithmes clés sont écrits à la main, et Claude Code prépare le squelette et vérifie le résultat. Dans le TODO, chaque tâche porte l'une de ces marques : **(C)** Claude écrit, **(P)** le développeur écrit et Claude vérifie, **(C→P)** Claude prépare le squelette et le développeur implémente.

### 3.2 État d'avancement

Étapes planifiées, tâches terminées et décisions de conception encore ouvertes : [`TODO.md`](TODO.md).

### 3.3 Décisions de conception

Le **pourquoi** du code : décisions architecturales (D1 à D7), blocages rencontrés et correctifs appliqués, dans l'ordre chronologique : [`DEVLOG.md`](DEVLOG.md).

### 3.4 Conventions de code

Clarté avant concision, annotations de type, exceptions sur mesure, aucune constante ni message d'erreur codé en dur : voir la section *Style de Code & Lisibilité* de [`CLAUDE.md`](CLAUDE.md).
