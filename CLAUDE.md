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
0. **Pédagogie :** Le projet est pédagogique. Les méthodes et algos clés sont scaffoldés, mais chaque membre de l'équipe écrit lui-même ceux de sa sous-étape ; Claude vérifie ensuite. Les tests automatisés peuvent être écrits par un agent de codage (depuis le 13 novembre) : c'est plus rapide, et chaque membre se concentre sur l'essentiel. Le membre reste responsable de ses tests : il les relit, et ils sont revus comme le reste de la *pull request*. La provenance des tests est indiquée dans la *pull request* et dans le DEVLOG.
1. **Planification (TASKS.md) :** Avant d'écrire la moindre ligne de code, les étapes du travail doivent être planifiées à l'avance et consignées dans un fichier `TASKS.md` à la racine du projet, rangé par ordre de priorité. Le plan de conception du cœur (étapes 1 à 12-0, décisions D1 à D14) est archivé dans `docs/archive/TODO.md` depuis le 2026-11-27.
2. **Journal de bord (DEVLOG.md) :** Les étapes du développement, les décisions architecturales prises, les blocages rencontrés et les correctifs appliqués sont consignés au fur et à mesure dans un fichier `DEVLOG.md`.
3. **Isolation par Étape :** Claude Code doit traiter une seule tâche du `TASKS.md` à la fois.
4. **Automatisation des Tests :** Chaque étape doit obligatoirement inclure l'écriture de tests automatisés. Nous suggérons **unittest**.
5. **Validation Avant Passage à la Suite :** Il est strictement interdit de passer à l'étape subséquente avant d'avoir testé à fond l'étape courante. Les tests doivent tous passer au vert (`green`) et couvrir les cas nominaux ainsi que les cas aux limites (edge cases).
6. **Mise à jour du statut :** Le fichier `TASKS.md` et le `DEVLOG.md` doivent être mis à jour à la fin de chaque étape validée.
7. **Travail en équipe :** Depuis le 9 novembre, quatre membres travaillent sur le dépôt. La répartition et les règles communes sont dans [`TEAM.md`](TEAM.md). Les règles 3 et 5 s'appliquent **par personne et par branche** :
    * chacun travaille sur sa branche (`etape-<numéro>-<sujet>`), une sous-étape à la fois ;
    * une branche n'est fusionnée dans `main` (par *pull request*) que lorsque ses tests et la suite complète sont verts ;
    * seules des sous-étapes sans dépendance entre elles avancent en parallèle ; leurs interfaces communes sont scaffoldées d'avance sur `main` et ne changent qu'après concertation ;
    * DEVLOG.md : entrées ajoutées à la fin, sous un titre `## AAAA-MM-JJ — Étape Xy : sujet (prénom)` ; TASKS.md : chacun ne coche que sa tâche.

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
├── experiments/                # Exploitation du cœur : tout ce qui sert à s'en servir, hors de src/
│   ├── drivers/                # Scripts de pilotage (run_experiment.py)
│   ├── analysis/               # Scripts d'analyse des résultats (à venir)
│   ├── config/                 # Configurations JSON des expériences
│   ├── results/                # Résultats JSON, un répertoire par jour (versionnés)
│   └── EXPLOG.md               # Journal des expériences
├── src/                        # Cœur : modèle, algorithme génétique, mémétique, observabilité
│   ├── __init__.py
│   ├── config.py               # Constantes de configuration : chemins du projet, MiniZinc
│   ├── model/                  # Modèle CP (MiniZinc) et ses règles côté Python
│   │   ├── __init__.py
│   │   ├── evaluation.py       # Coût de couverture et pénalités (CostBreakdown)
│   │   ├── feasibility.py      # Faisabilité structurelle d'un horaire
│   │   ├── horaire.mzn         # Modèle MiniZinc fourni, couverture dure : référence (D12)
│   │   ├── horaire_assoupli.mzn # Modèle du pipeline : couverture « au moins 1 » en pénalité (D12)
│   │   ├── horaire.py          # Phénotype canonique Horaire et grille « employé × période »
│   │   └── shift_rules.py      # Constantes du domaine : noms des variables MiniZinc, durées, écarts, décalages des fenêtres
│   ├── ga/                     # Logique de l'Algorithme Génétique
│   │   ├── __init__.py
│   │   ├── chromosome.py       # Génotype : interface Encoding[G] et encodages concrets
│   │   ├── individual.py       # Individu : génome, horaire décodé, coût
│   │   ├── initialization.py   # Initialisation de la population (PopulationInitializer)
│   │   ├── operators.py        # Opérateurs de variation : Crossover[G], Mutation[G]
│   │   ├── population.py       # Gestion de la population globale
│   │   ├── registry.py         # Registre des opérateurs par nom (fabriques, vérification des paramètres), compatibilité opérateur / encodage
│   │   └── selection.py        # Sélection : ParentSelector, MutableSelector
│   ├── memetic/                # Couplage Mémétique, réparation et moteur
│   │   ├── __init__.py
│   │   ├── assembly.py         # Assemblage de référence avec les vrais composants (build_block_memetic_config)
│   │   ├── catalog.py          # Catalogue des stratégies choisies par leur nom (StrategyCatalog), pour les configurations d'expériences
│   │   ├── config.py           # MemeticConfig : stratégies, paramètres et hub d'observation d'une exécution
│   │   ├── engine.py           # Moteur Memetic(NR, NM) : lots NR et NM (D7), événements (D8)
│   │   ├── executor.py         # Exécution des lots : Executor, SequentialExecutor (D7)
│   │   ├── local_search.py     # Neighborhood et LocalSolver : recherche locale et réparation par MiniZinc
│   │   ├── seeds.py            # Graines dérivées par tâche (D7)
│   │   ├── solver.py           # SolverAdapter : modèle résolu (ModelVariant), options, limites d'effort, issue et statistiques
│   │   └── termination.py      # Critère d'arrêt : TerminationCriterion, GenerationLimit
│   ├── observability/          # Observabilité (D8) : événements, collecteurs, destinations, journal, répertoire d'exécution
│   ├── utils/                  # Environnement, lecture de fichiers et parsing
│   │   ├── __init__.py
│   │   ├── minizinc_env.py     # Localisation de MiniZinc et des solveurs
│   │   └── io.py               # Lecture et validation des instances (ProblemInstance)
├── tests/                      # Tests unittest (python -m unittest discover)
├── CLAUDE.md                   # Guide de développement
├── TASKS.md                    # Travail en cours, par ordre de priorité (l'ancien TODO.md est dans docs/archive/)
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