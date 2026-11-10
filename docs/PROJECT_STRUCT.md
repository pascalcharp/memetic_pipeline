# Structure du projet

Arborescence **actuelle** du dépôt : seuls les fichiers qui existent y figurent. Les fichiers prévus mais pas encore créés sont planifiés dans [`TODO.md`](../TODO.md).

À mettre à jour à chaque ajout, déplacement ou suppression de fichier.

```text
memetic_pipeline/
├── .github/
│   └── workflows/
│       └── tests.yml           # CI : construit l'image Docker et lance les tests (push sur main, pull requests vers main)
├── data/                       # Instances au format JSON (lues directement par MiniZinc)
│   ├── bench_1.json            # 3 employés × 1 activité  × 32 périodes
│   ├── bench_2.json            # 4 employés × 2 activités × 28 périodes
│   ├── bench_3.json            # 6 employés × 3 activités × 48 périodes
│   ├── bench_4.json            # 8 employés × 4 activités × 44 périodes
│   └── bench_5.json            # 8 employés × 5 activités × 48 périodes (difficile : ~1 min pour une 1re solution)
├── docs/                       # Toute la documentation, accessible depuis README.md
│   ├── ALGO.md                 # Pseudo-code de l'algorithme mémétique
│   ├── PROBLEME.md             # Description du problème : données, règles d'un quart, coût, exemple
│   └── PROJECT_STRUCT.md       # Ce document
├── src/                        # Code source principal
│   ├── __init__.py
│   ├── config.py               # Configuration : chemins du projet (ProjectPaths), MiniZinc (MiniZincConfig)
│   ├── drivers/                # Points d'entrée des expériences (vide pour l'instant)
│   │   └── __init__.py
│   ├── ga/                     # Algorithme génétique
│   │   ├── __init__.py
│   │   ├── chromosome.py       # Génotype : interface Encoding[G], BlockEncoding (gènes BlockGene, ActivityBlock)
│   │   ├── individual.py       # Individu : génome, horaire décodé, coût
│   │   ├── initialization.py   # Initialisation : PopulationInitializer, RandomBlockInitializer (scaffold, étape 6)
│   │   ├── operators.py        # Variation : Crossover[G], Mutation[G], opérateurs de BlockEncoding (scaffold, étape 7b)
│   │   ├── registry.py         # Registre des opérateurs par nom, IncompatibleOperatorError (scaffold, étape 7a)
│   │   └── selection.py        # Sélection : ParentSelector, MutableSelector, TournamentSelector (scaffold, étape 7a)
│   ├── memetic/                # Couplage mémétique et recherche locale
│   │   ├── __init__.py
│   │   ├── local_search.py     # Recherche locale : Neighborhood, LocalSolver, MiniZincLocalSolver (scaffold, étape 5b)
│   │   └── solver.py           # Indirection vers les solveurs : SolverAdapter, CpSatAdapter, limites d'effort, SolverRun
│   ├── model/                  # Modèle CP (MiniZinc) et ses règles côté Python
│   │   ├── __init__.py
│   │   ├── evaluation.py       # Coût : couverture (cout_total) et pénalités (CostEvaluator, CostBreakdown, PenaltyWeights)
│   │   ├── feasibility.py      # Faisabilité structurelle d'un horaire (FeasibilityChecker, Violation, StructuralRule)
│   │   ├── horaire.mzn         # Modèle MiniZinc fourni
│   │   ├── horaire.py          # Phénotype canonique (Horaire, HoraireEmploye) et grille « employé × période »
│   │   └── shift_rules.py      # Constantes du domaine : noms des variables MiniZinc, durées, écarts, décalages des fenêtres
│   └── utils/                  # Utilitaires : environnement, lecture de fichiers
│       ├── __init__.py
│       ├── io.py               # Lecture et validation des instances (ProblemInstance, plage utile, fenêtres)
│       └── minizinc_env.py     # Localisation de MiniZinc et des solveurs, exceptions associées
├── tests/                      # Tests unittest : python -m unittest discover
│   ├── __init__.py
│   ├── fixtures.py             # Outil de test (pas un test) : individus aux coûts choisis, génome de référence, faux LocalSolver
│   ├── minizinc_probe.py       # Outil de test (pas un test) : sonde horaire.mzn pour vérifier la cohérence avec Python
│   ├── test_chromosome.py      # Génotype : allers-retours, génomes infaisables, conditions de D1, solutions MiniZinc
│   ├── test_evaluation.py      # Évaluation : cas à la main, totaux de couverture, pénalités, coût comparé à MiniZinc
│   ├── test_feasibility.py     # Faisabilité structurelle : bornes exactes, violations isolées, verdict comparé à MiniZinc
│   ├── test_horaire.py         # Phénotype : construction, forme, grille comparée à la 2ᵉ sortie de MiniZinc
│   ├── test_individual.py      # Individu : décodage unique, évaluation sans modification (encodage factice)
│   ├── test_initialization.py  # Initialisation (étape 6) : contrat du scaffold, cas à couvrir en tête de fichier
│   ├── test_io.py              # Lecture des instances : 5 bench, cas d'erreur, plage utile comparée à MiniZinc
│   ├── test_local_search.py    # Recherche locale (étape 5b) : contrat du scaffold, cas à couvrir en tête de fichier
│   ├── test_minizinc_env.py    # Localisation de MiniZinc, solveurs, messages d'erreur
│   ├── test_operators.py       # Variation (étape 7b) : contrat du scaffold, cas à couvrir en tête de fichier
│   ├── test_registry.py        # Registre (étape 7a) : contrat du scaffold, cas à couvrir en tête de fichier
│   ├── test_selection.py       # Sélection (étape 7a) : check_selectable, contrat du scaffold, cas à couvrir
│   ├── test_shift_rules.py     # Constantes du domaine et sondes de cohérence avec horaire.mzn
│   ├── test_smoke_minizinc.py  # Test de fumée : CP-SAT résout bench_1 (optimum 94)
│   └── test_solver.py          # Solveurs : traduction des options et des statuts, reproductibilité, issues sans solution
├── .dockerignore
├── .gitignore
├── CLAUDE.md                   # Guide de développement (méthode, architecture, style), lu par Claude Code
├── DEVLOG.md                   # Journal de bord : décisions, blocages, correctifs
├── Dockerfile                  # Image Python 3.13 + MiniZinc 2.10 (CP-SAT, Gecode, Chuffed, HiGHS)
├── README.md                   # Point d'entrée de la documentation
├── TEAM.md                     # Travail en équipe : règles communes et répartition de la semaine
├── TODO.md                     # Planification des étapes et décisions de conception
└── requirements.txt            # Dépendances Python (minizinc, numpy)
```

Non suivis par Git : `.venv/` (environnement virtuel local), `.idea/` (PyCharm) et les caches `__pycache__/`.
