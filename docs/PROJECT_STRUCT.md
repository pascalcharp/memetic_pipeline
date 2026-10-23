```Graph
ift4001-memetic-timetabling/
├── data/                       # Contient les instances (.dzn ou .json)
│   ├── instance_test_sprint.json
│   └── instance_test_large.json
├── src/                        # Code source principal
│   ├── __init__.py
│   ├── model/                  # Modèle CP (MiniZinc)
│   │   └── schedule_model.mzn  # fichier MiniZinc fourni
│   ├── ga/                     # Logique de l'Algorithme Génétique
│   │   ├── __init__.py
│   │   ├── chromosome.py       # Structure des gènes (Direct ou Paramètres)
│   │   ├── operators.py        # Crossover, Mutation, Sélection
│   │   └── population.py       # Gestion de la population globale
│   ├── memetic/                # Couplage Mémétique & Réparation
│   │   ├── __init__.py
│   │   └── local_search.py     # Interface avec MiniZinc pour réparation/décodage
│   ├── utils/                  # Lecture de fichiers et parsing
│   │   ├── __init__.py
│   │   └── io.py
│   └── main.py                 # Point d'entrée pour lancer le POC
├── requirements.txt            # Dépendances Python
└── README.md                   # Instructions d'exécution
```
