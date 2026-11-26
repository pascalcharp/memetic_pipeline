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
│   ├── AVAILABLE_STRATEGIES.md # Catalogue des stratégies disponibles par rôle : classes, paramètres, garanties, stratégies prévues
│   ├── ALGO.md                 # Pseudo-code de l'algorithme mémétique, correspondance avec le code, écarts assumés
│   ├── HOWTO.md                # Comment faire ? Lancer la boucle, ajouter un opérateur, changer de solveur, etc.
│   ├── PROBLEME.md             # Description du problème : données, règles d'un quart, coût, exemple
│   └── PROJECT_STRUCT.md       # Ce document
├── experiments/                # Exploitation du cœur (étape 10) : pilotage, configurations, résultats, analyses ; versionné
│   ├── __init__.py
│   ├── EXPLOG.md               # Journal des expériences : une entrée par exécution, ajoutée par run_experiment
│   ├── analysis/               # Scripts d'analyse (analyze_*.py) et rapports (bench2_*.md) des séries d'expériences
│   │   ├── analyze_random_restarts.py, bench2_temoin_redemarrages.md # 10d : mémétique contre redémarrages aléatoires (population 6)
│   │   └── analyze_random_witness.py, bench2_temoin_aleatoire.md     # 10d : mémétique contre individus aléatoires + LocalSolver (population 18)
│   ├── config/                 # Configurations JSON des expériences (description, instance, paramètres, stratégies), une série par répertoire
│   │   └── integration_bench1.json # Configuration de base : les réglages de la 9-intégration sur bench_1
│   ├── drivers/                # Scripts de pilotage des expériences
│   │   ├── __init__.py
│   │   └── run_experiment.py   # Script d'expériences : configuration JSON → exécution mesurée → résultats JSON et entrée d'EXPLOG.md (étape 10a)
│   └── results/                # Résultats JSON, un répertoire par jour (AAAA-MM-JJ/)
├── src/                        # Cœur : modèle, algorithme génétique, mémétique, observabilité
│   ├── __init__.py
│   ├── config.py               # Configuration : chemins du projet et des deux modèles (ProjectPaths), MiniZinc (MiniZincConfig)
│   ├── ga/                     # Algorithme génétique
│   │   ├── __init__.py
│   │   ├── chromosome.py       # Génotype : interface Encoding[G], BlockEncoding (gènes BlockGene, ActivityBlock)
│   │   ├── individual.py       # Individu : génome, horaire décodé, coût
│   │   ├── initialization.py   # Initialisation : PopulationInitializer, InitializationResult, RandomBlockInitializer (étape 6)
│   │   ├── operators.py        # Variation : Crossover[G], Mutation[G], opérateurs de BlockEncoding (étape 7b)
│   │   ├── population.py       # SelectPop, convergence, restart : PlusSurvivorSelector, StagnationCriterion, EliteRestart, RestartResult (étape 8)
│   │   ├── registry.py         # Registre des opérateurs par nom, IncompatibleOperatorError (étape 7a)
│   │   └── selection.py        # Sélection : ParentSelector, MutableSelector, TournamentSelector (étape 7a)
│   ├── memetic/                # Couplage mémétique, recherche locale et moteur
│   │   ├── __init__.py
│   │   ├── assembly.py         # Assemblage de référence avec les vrais composants : AssemblySettings, build_block_memetic_config (9-intégration)
│   │   ├── catalog.py          # Catalogue des stratégies choisies par leur nom : StrategyCatalog, StrategyChoices, BuildContext (étape 10c)
│   │   ├── config.py           # MemeticConfig : stratégies, paramètres et hub d'observation d'une exécution (étape 9)
│   │   ├── engine.py           # Moteur Memetic(NR, NM), lots NR et NM (D7), MemeticResult (étape 9)
│   │   ├── executor.py         # Exécution des lots : Executor, SequentialExecutor (D7)
│   │   ├── local_search.py     # Recherche locale : Neighborhood, LocalSolver, MiniZincLocalSolver, LocalSearchRecord, borne selon le modèle (étapes 5b, 5c)
│   │   ├── seeds.py            # Graines dérivées par tâche : derive_task_seeds, SeedStreams (étape 9)
│   │   ├── solver.py           # Indirection vers les solveurs : SolverAdapter, CpSatAdapter, ModelVariant, limites d'effort, SolverRun
│   │   └── termination.py      # Critère d'arrêt : TerminationCriterion, GenerationLimit (étape 9)
│   ├── model/                  # Modèle CP (MiniZinc) et ses règles côté Python
│   │   ├── __init__.py
│   │   ├── evaluation.py       # Coût : couverture (cout_total) et pénalités (CostEvaluator, CostBreakdown, PenaltyWeights)
│   │   ├── feasibility.py      # Faisabilité structurelle d'un horaire (FeasibilityChecker, Violation, StructuralRule)
│   │   ├── horaire.mzn         # Modèle MiniZinc fourni, couverture dure : référence, gardé inchangé (D12)
│   │   ├── horaire_assoupli.mzn # Modèle du pipeline : couverture « au moins 1 » en pénalité (D12, étape 5c)
│   │   ├── horaire.py          # Phénotype canonique (Horaire, HoraireEmploye) et grille « employé × période »
│   │   └── shift_rules.py      # Constantes du domaine : noms des variables MiniZinc, durées, écarts, décalages des fenêtres
│   ├── observability/          # Observabilité (D8) : événements, collecteurs, destinations, journal, répertoire d'exécution
│   │   ├── __init__.py
│   │   ├── collectors.py       # MetricCollector et collecteurs : coût, diversité, taux de faisabilité, charge du solveur (étape 8b)
│   │   ├── events.py           # Catalogue des événements du moteur, schéma des enregistrements (make_record)
│   │   ├── hub.py              # ObservationHub : diffuse les événements aux collecteurs, écrit dans les destinations
│   │   ├── logging_config.py   # Journal de diagnostic : configure_logging, get_logger
│   │   ├── run_directory.py    # Répertoire results/<expérience>/<run_id>/ et config.json
│   │   └── sinks.py            # Destinations : RecordSink, NullSink, MemorySink, ConsoleSink, JsonlSink, CsvSink
│   └── utils/                  # Utilitaires : environnement, lecture de fichiers
│       ├── __init__.py
│       ├── io.py               # Lecture et validation des instances (ProblemInstance, plage utile, fenêtres)
│       └── minizinc_env.py     # Localisation de MiniZinc et des solveurs, exceptions associées
├── tests/                      # Tests unittest : python -m unittest discover
│   ├── __init__.py
│   ├── fixtures.py             # Outil de test (pas un test) : individus aux coûts choisis, génome de référence, faux objets (LocalSolver, opérateurs, stratégies de population, collecteur)
│   ├── minizinc_probe.py       # Outil de test (pas un test) : sonde horaire.mzn pour vérifier la cohérence avec Python
│   ├── test_catalog.py         # Catalogue des stratégies (étape 10c) : noms, création avec le contexte, vérification des paramètres, choix par défaut
│   ├── test_chromosome.py      # Génotype : allers-retours, génomes infaisables, conditions de D1, solutions MiniZinc
│   ├── test_collectors.py      # Collecteurs (étape 8b) : événements construits à la main, valeurs attendues calculées à la main
│   ├── test_engine.py          # Moteur (étape 9) : faux objets, lots NR et NM, graines, événements (initialisation et restart compris), reproductibilité
│   ├── test_evaluation.py      # Évaluation : cas à la main, totaux de couverture, pénalités, coût comparé à MiniZinc
│   ├── test_executor.py        # Exécution des lots : SequentialExecutor
│   ├── test_feasibility.py     # Faisabilité structurelle : bornes exactes, violations isolées, verdict comparé à MiniZinc
│   ├── test_horaire.py         # Phénotype : construction, forme, grille comparée à la 2ᵉ sortie de MiniZinc
│   ├── test_individual.py      # Individu : décodage unique, évaluation sans modification (encodage factice)
│   ├── test_integration.py     # 9-intégration : assemblage de référence, puis exécution complète sur bench_1 avec CP-SAT (~30 s)
│   ├── test_initialization.py  # Initialisation (étape 6) : faux solveur, puis CP-SAT sur bench_1 et bench_5 avec les deux modèles
│   ├── test_io.py              # Lecture des instances : 5 bench, cas d'erreur, plage utile comparée à MiniZinc
│   ├── test_local_search.py    # Recherche locale (étapes 5b, 5c) : voisinage, fixation, bornes des deux modèles, CP-SAT
│   ├── test_minizinc_env.py    # Localisation de MiniZinc, solveurs, messages d'erreur
│   ├── test_relaxed_model.py   # Modèle assoupli (étape 5c) : référence inchangée, mêmes optimums, validation croisée Python / MiniZinc
│   ├── test_observability.py   # Observabilité : schéma, destinations, ObservationHub, journal, répertoire d'exécution
│   ├── test_operators.py       # Variation (étape 7b) : propriétés avec un vrai Random, cas limites, messages
│   ├── test_population.py      # Population (étape 8) : sélecteurs (doublons, peine de mort), stagnation, restart (élite, nouveaux, recherches)
│   ├── test_run_experiment.py  # Script d'expériences (étapes 10a, 10c) : configuration et stratégies, chemins, résultats, journal, exécution courte sur bench_1
│   ├── test_registry.py        # Registre (étapes 7a, 10c) : enregistrement et création par nom, vérification des paramètres, compatibilité opérateur / encodage
│   ├── test_selection.py       # Sélection (étape 7a) : check_selectable, tournoi, tirage uniforme, reproductibilité
│   ├── test_shift_rules.py     # Constantes du domaine et sondes de cohérence avec horaire.mzn
│   ├── test_smoke_minizinc.py  # Test de fumée : CP-SAT résout horaire.mzn sur bench_1 (optimum 94)
│   └── test_solver.py          # Solveurs : options, modèles (ModelVariant), traduction des statuts, reproductibilité, issues
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

Non suivis par Git : `.venv/` (environnement virtuel local), `.idea/` (PyCharm), les caches `__pycache__/` et `/results/` à la racine (répertoires de `RunDirectory`, D8). `experiments/results/` est versionné.
