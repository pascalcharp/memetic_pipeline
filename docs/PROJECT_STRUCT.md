# Structure du projet

Arborescence **actuelle** du dépôt : seuls les fichiers qui existent y figurent. Les fichiers prévus mais pas encore créés sont planifiés dans [`TODO.md`](../TODO.md).

À mettre à jour à chaque ajout, déplacement ou suppression de fichier.

```text
memetic_pipeline/
├── .github/
│   └── workflows/
│       └── tests.yml           # CI : construit l'image Docker et lance les tests à chaque push sur main
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
│   ├── ga/                     # Algorithme génétique (vide pour l'instant)
│   │   └── __init__.py
│   ├── memetic/                # Couplage mémétique et recherche locale (vide pour l'instant)
│   │   └── __init__.py
│   ├── model/                  # Modèle CP (MiniZinc) et ses règles côté Python
│   │   ├── __init__.py
│   │   ├── horaire.mzn         # Modèle MiniZinc fourni
│   │   └── shift_rules.py      # Constantes du domaine : durées, écarts entre jalons, décalages des fenêtres
│   └── utils/                  # Utilitaires : environnement, lecture de fichiers
│       ├── __init__.py
│       └── minizinc_env.py     # Localisation de MiniZinc et des solveurs, exceptions associées
├── tests/                      # Tests unittest : python -m unittest discover
│   ├── __init__.py
│   ├── test_minizinc_env.py    # Localisation de MiniZinc, solveurs, messages d'erreur
│   ├── test_shift_rules.py     # Constantes du domaine et sondes de cohérence avec horaire.mzn
│   └── test_smoke_minizinc.py  # Test de fumée : CP-SAT résout bench_1 (optimum 94)
├── .dockerignore
├── .gitignore
├── CLAUDE.md                   # Guide de développement (méthode, architecture, style), lu par Claude Code
├── DEVLOG.md                   # Journal de bord : décisions, blocages, correctifs
├── Dockerfile                  # Image Python 3.13 + MiniZinc 2.10 (CP-SAT, Gecode, Chuffed, HiGHS)
├── README.md                   # Point d'entrée de la documentation
├── TODO.md                     # Planification des étapes et décisions de conception
└── requirements.txt            # Dépendances Python (minizinc, numpy)
```

Non suivis par Git : `.venv/` (environnement virtuel local), `.idea/` (PyCharm) et les caches `__pycache__/`.
