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
│   │   ├── horaire.mzn         # Modèle MiniZinc fourni
│   │   └── shift_rules.py      # Constantes du domaine : durées, écarts entre jalons, décalages des fenêtres
│   ├── ga/                     # Logique de l'Algorithme Génétique (à venir)
│   │   ├── __init__.py
│   │   ├── chromosome.py       # Génotype : interface Encoding[G] et encodages concrets
│   │   ├── operators.py        # Crossover, Mutation, Sélection
│   │   └── population.py       # Gestion de la population globale
│   ├── memetic/                # Couplage Mémétique & Réparation (à venir)
│   │   ├── __init__.py
│   │   └── local_search.py     # LocalSolver et SolverAdapter : recherche locale et réparation par MiniZinc
│   ├── utils/                  # Environnement, lecture de fichiers et parsing
│   │   ├── __init__.py
│   │   ├── minizinc_env.py     # Localisation de MiniZinc et des solveurs
│   │   └── io.py               # Lecture des instances (à venir)
│   └── drivers/                # Point d'entrée pour lancer les expériences (à venir)
├── tests/                      # Tests unittest (python -m unittest discover)
├── CLAUDE.md                   # Guide de développement
├── TODO.md                     # Planification des étapes
├── DEVLOG.md                   # Journal de bord
├── requirements.txt            # Dépendances Python
└── README.md                   # Instructions d'exécution
```
