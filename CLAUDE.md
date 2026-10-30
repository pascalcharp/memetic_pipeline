# CLAUDE.md - Guide de développement d'un 'proof of concept' pour un algo mémétique servant à résoudre des problèmes d'horaire

## Algorithme choisi pour proof of concept

```Text
Memetic(NR, NM):

    Initialiser population P

    while not terminé(P):

        for j in NR:
            Parents = SelectParent(P)
            Enfants = Recombine(Parents)
            Enfants = SolveurLocal(Enfants)
            Evaluer(Enfants)
            P = P + Enfants

        for j  in NM:
            i = SelectMutable(P)
            Mute(i)
            i = SolveurLocal(i)
            Evaluer(i)
            P = P + {i}
        P = SelectPop(P)
        if (P a convergé)
            P = Restart(P)
   ```

## 🔄 Workflow de Développement & Validation Strict
L'implémentation de fonctionnalités doit suivre une méthodologie rigoureuse étape par étape.
0. **Pédagogie :** Le projet est pédagogique. Les méthodes et algos clés sont scaffoldés, mais je les écris moi-même, Claude vérifie ensuite.
1. **Planification (TODO.md) :** Avant d'écrire la moindre ligne de code, les étapes du travail doivent être planifiées à l'avance et consignées dans un fichier `TODO.md` à la racine du projet.
2. **Journal de bord (DEVLOG.md) :** Les étapes du développement, les décisions architecturales prises, les blocages rencontrés et les correctifs appliqués sont consignés au fur et à mesure dans un fichier `DEVLOG.md`.
3. **Isolation par Étape :** Claude Code doit traiter une seule tâche du `TODO.md` à la fois.
4. **Automatisation des Tests :** Chaque étape doit obligatoirement inclure l'écriture de tests automatisés. Nous suggérons **unittest**.
5. **Validation Avant Passage à la Suite :** Il est strictement interdit de passer à l'étape subséquente avant d'avoir testé à fond l'étape courante. Les tests doivent tous passer au vert (`green`) et couvrir les cas nominaux ainsi que les cas aux limites (edge cases).
6. **Mise à jour du statut :** Le fichier `TODO.md` et le `DEVLOG.md` doivent être mis à jour à la fin de chaque étape validée.

## 🏗️ Architecture & Stack Technique
Le projet est entièrement conteneurisé avec Docker.

### Architecture cible

L'arbre ci-dessous décrit **où l'on va** : il inclut des fichiers prévus mais pas encore créés, et omet les fichiers d'infrastructure (Docker, CI). La structure **actuelle** et exacte du dépôt est dans [`docs/PROJECT_STRUCT.md`](docs/PROJECT_STRUCT.md).

```Graph
memetic_pipeline/
├── data/                       # Instances au format JSON (lues directement par MiniZinc)
│   ├── bench_1.json            # 3 employés × 1 activité × 32 périodes (la plus petite)
│   ├── …
│   └── bench_5.json            # 8 employés × 5 activités × 48 périodes (la plus grande)
├── docs/                       # Documentation de conception (ALGO.md, PROJECT_STRUCT.md)
├── src/                        # Code source principal
│   ├── __init__.py
│   ├── config.py               # Constantes de configuration : chemins du projet, MiniZinc
│   ├── model/                  # Modèle CP (MiniZinc) et ses règles côté Python
│   │   ├── __init__.py
│   │   ├── feasibility.py      # Faisabilité structurelle d'un horaire
│   │   ├── horaire.mzn         # Modèle MiniZinc fourni
│   │   ├── horaire.py          # Phénotype canonique Horaire et grille « employé × période »
│   │   └── shift_rules.py      # Constantes du domaine : noms des variables MiniZinc, durées, écarts, décalages des fenêtres
│   ├── ga/                     # Logique de l'Algorithme Génétique (à venir)
│   │   ├── __init__.py
│   │   ├── chromosome.py       # Génotype : interface Encoding[G] et encodages concrets
│   │   ├── individual.py       # Individu : génome, horaire décodé, coût
│   │   ├── operators.py        # Crossover, Mutation, Sélection
│   │   └── population.py       # Gestion de la population globale
│   ├── memetic/                # Couplage Mémétique & Réparation (à venir)
│   │   ├── __init__.py
│   │   └── local_search.py     # LocalSolver et SolverAdapter : recherche locale et réparation par MiniZinc
│   ├── utils/                  # Environnement, lecture de fichiers et parsing
│   │   ├── __init__.py
│   │   ├── minizinc_env.py     # Localisation de MiniZinc et des solveurs
│   │   └── io.py               # Lecture et validation des instances (ProblemInstance)
│   └── drivers/                # Point d'entrée pour lancer les expériences (à venir)
├── tests/                      # Tests unittest (python -m unittest discover)
├── CLAUDE.md                   # Guide de développement
├── TODO.md                     # Planification des étapes
├── DEVLOG.md                   # Journal de bord
├── requirements.txt            # Dépendances Python
└── README.md                   # Instructions d'exécution
```

## ✍️ Style de Code & Lisibilité
* **Règle d'or: Clarté > Concision :** Éviter le code trop condensé ou "astucieux". Le code doit se lire comme de la prose.
* **Python avec hints de type:** 
* **Documentation :** Documentation des méthodes importantes des interfaces, documentation des classes obligatoire
* **Gestion des erreurs :** Exceptions sur mesure pour les classes, gestion cohérente de celles-ci au même niveau
* **Constantes et nombres magiques:** Aucune constante codée en dur dans le code.  Elles sont toutes stockées dans une classe spéciale ou une classe ayant un lien logique avec le code.
* **Messages d'erreur :** ce sont des constantes. Chaque module qui définit des exceptions sur mesure regroupe ses gabarits de messages dans une classe `...Messages` placée à côté de ces exceptions. Les gabarits utilisent des espaces réservés nommés (`"{path} ..."`, remplis par `.format(path=...)`), jamais de f-strings. Les tests vérifient que le message contient l'information utile au diagnostic (chemin, nom de variable, identifiant), pas son texte exact.