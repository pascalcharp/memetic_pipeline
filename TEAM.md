# Planification du travail en équipe

## Règles communes

### Branches et fusion
- **Chacun travaille sur sa propre branche**, créée à partir de `main` et nommée d'après sa sous-étape : `etape-5b-local-solver`, `etape-6-initialisation`, `etape-7a-selection`, `etape-7b-variation`.
- **On ne fusionne dans `main` que lorsque tous les tests sont verts** : ceux de sa sous-étape et la suite complète (`python -m unittest discover`). La fusion passe par une *pull request* sur GitHub, relue par au moins un autre membre.
- Avant d'ouvrir la *pull request*, on intègre le dernier `main` dans sa branche (`git merge main`) et on relance la suite complète.
- Une tâche à la fois par personne. Seules des sous-étapes sans dépendance entre elles avancent en parallèle.

### Code partagé
- Les **interfaces** (classes abstraites, signatures, docstrings) sont scaffoldées d'avance et communes à tous. On ne les modifie pas seul : un changement d'interface se discute avec les membres qui l'utilisent, puis se fait dans un commit à part.
- Modules déjà validés, à ne modifier qu'après concertation : `src/model/` (`horaire.py`, `feasibility.py`, `evaluation.py`, `shift_rules.py`), `src/ga/chromosome.py`, `src/ga/individual.py`, `src/memetic/solver.py`, `src/utils/`.
- Le style est celui de [`CLAUDE.md`](CLAUDE.md) : clarté avant concision, hints de type, aucune constante codée en dur, exceptions sur mesure avec gabarits de messages dans une classe `...Messages`.

### Journal et planification
- **DEVLOG.md** : chacun ajoute ses entrées **à la fin du fichier**, sous un titre `## AAAA-MM-JJ — Étape Xy : sujet (prénom)`. On y consigne les décisions, les blocages et les correctifs. On ne modifie jamais l'entrée d'un autre membre.
- **TODO.md** : chacun coche les cases de **sa** sous-étape seulement (`[~]` en cours, `[x]` validée, tests verts).
- **TEAM.md** (ce fichier) porte la répartition de la semaine. Chacun coche sa ligne quand sa branche est fusionnée.

### Environnement et tests
- Installation : voir la section 2, « Je viens de cloner le dépôt. Et ensuite ? », du [`README.md`](README.md) (Python 3.13, `.venv`, `requirements.txt`, MiniZinc 2.10 avec CP-SAT ; ou Docker).
- Suite complète : `python -m unittest discover`
- Un module de tests : `python -m unittest tests.test_<module>` ; un seul test : `python -m unittest tests.test_<module>.<Classe>.<test>`
- Seuls les tests qui appellent MiniZinc sont lents (quelques secondes). Les autres doivent rester instantanés : on teste la logique Python sans solveur chaque fois que c'est possible (encodage factice, faux `LocalSolver`).

---

## Semaine du 9 novembre

Avant le départ, Claude scaffolde en un seul commit sur `main` les interfaces et les squelettes de tests des quatre sous-étapes. Chacun crée ensuite sa branche à partir de ce commit. Les noms de classes ci-dessous sont ceux du plan ; le scaffold peut les préciser.

### Pascal — Étape 5b : recherche locale par MiniZinc
- [ ] Étape 5b

**Fichiers**
- `src/memetic/local_search.py`
- `tests/test_local_search.py`

**Classes à écrire**
- `RandomEmployeesNeighborhood(k)` : choisit les employés à libérer, k au hasard plus tous les employés structurellement infaisables.
- `MiniZincLocalSolver(instance, adapter, neighborhood, evaluator)` : fixe les employés non libérés, ajoute la borne `cout_total ≤ coût de l'entrée` si l'entrée est faisable, résout, reconstruit l'`Horaire` ; rend l'entrée inchangée s'il n'y a aucune solution.

**Scaffoldé d'avance** : interfaces `Neighborhood` et `LocalSolver`, `LocalSearchResult`, exceptions et messages.

**Dépendances**
- `src/memetic/solver.py` : `CpSatAdapter`, `SolverOptions`, `DeterministicTimeLimit`, `SolverRun`, `SolveOutcome`
- `src/model/horaire.py` : `Horaire`, `Horaire.from_model_variables`
- `src/model/feasibility.py` : `FeasibilityChecker` (employés infaisables)
- `src/model/evaluation.py` : `CostEvaluator`, `CostBreakdown.is_feasible`, `coverage_cost`
- `src/model/shift_rules.py` : `ModelVariableNames` (noms des variables dans les contraintes)
- `random.Random`, injecté (D5)

**Décisions de référence** : D10 et D11 dans TODO.md.

**Tests** : `python -m unittest tests.test_local_search` (appelle MiniZinc).

### Mély — Étape 6 : initialisation de la population
- [ ] Étape 6

**Fichiers**
- `src/ga/initialization.py`
- `tests/test_initialization.py`

**Classes à écrire**
- `RandomBlockInitializer` : génère au hasard des génomes `BlockGenome` **structurellement faisables**, reproductibles avec la même graine :
  - chaque durée de bloc `d_i ≥ 4` ;
  - `22 ≤ d1 + d2 + d3 + d4 ≤ 30` (6 à 8 heures rémunérées) ;
  - le quart entier dans la plage utile de l'instance ;
  - les activités dans `1..activity_count`.
- Option : passer chaque individu initial au `LocalSolver`. Le code s'écrit contre l'interface `LocalSolver` et se teste avec un faux solveur ; on le branchera sur le vrai quand 5b sera fusionnée.

**Scaffoldé d'avance** : interface `PopulationInitializer`, exceptions et messages.

**Dépendances**
- `src/ga/chromosome.py` : `BlockEncoding`, `BlockGene`, `ActivityBlock`, `BlockGenome`
- `src/ga/individual.py` : `Individu.from_genome`
- `src/utils/io.py` : `ProblemInstance` (plage utile `first_useful_period`, `last_useful_period`, fenêtres `windows`)
- `src/model/shift_rules.py` : `ShiftStructure`, `ShiftGaps` (durées minimales, bornes du quart)
- `src/model/feasibility.py` : `FeasibilityChecker` (dans les tests, pour vérifier la faisabilité)
- `src/memetic/local_search.py` : interface `LocalSolver` seulement (option)
- `random.Random`, injecté (D5)

**Décisions de référence** : D1 (encodage par blocs et ses conditions de faisabilité), D6, D7 dans TODO.md.

**Tests** : `python -m unittest tests.test_initialization` (sans MiniZinc).

### Tristan — Étape 7a : sélection et registre des opérateurs
- [ ] Étape 7a

**Fichiers**
- `src/ga/selection.py`
- `src/ga/registry.py`
- `tests/test_selection.py`, `tests/test_registry.py`

**Classes à écrire**
- `TournamentSelector(size)` : implémente `ParentSelector` ; tire `size` individus au hasard et retient le meilleur (coût `total` le plus faible), autant de fois que de parents demandés.
- Une première implémentation de `MutableSelector` (par exemple tirage uniforme, ou tournoi).
- `OperatorRegistry` : enregistre les opérateurs par nom, pour décrire les expériences en configuration ; vérifie qu'un opérateur de variation est compatible avec l'encodage choisi, sinon `IncompatibleOperatorError`.

**Scaffoldé d'avance** : interfaces `ParentSelector` et `MutableSelector`, exceptions et messages.

**Dépendances**
- `src/ga/individual.py` : `Individu`, `cost`, `is_evaluated`
- `src/model/evaluation.py` : `CostBreakdown.total` (critère de comparaison)
- `src/ga/chromosome.py` : `Encoding` (pour la compatibilité dans le registre)
- `src/ga/operators.py` : interfaces `Crossover[G]` et `Mutation[G]` seulement (registre)
- `random.Random`, injecté (D5)

**Décisions de référence** : D5 (patron Stratégie, registre par nom, `IncompatibleOperatorError`) et D7 (individus immuables, traitement par lot) dans TODO.md.

**Tests** : `python -m unittest tests.test_selection tests.test_registry` (sans MiniZinc). Les individus de test sont construits à la main, avec des coûts choisis.

### Xavier — Étape 7b : opérateurs de variation pour `BlockEncoding`
- [ ] Étape 7b

**Fichiers**
- `src/ga/operators.py`
- `tests/test_operators.py`

**Classes à écrire**
- Un croisement pour `BlockGenome`, par exemple un échange uniforme de gènes entiers (un gène = le quart complet d'un employé) : il préserve la faisabilité structurelle de chaque quart.
- Des mutations pour `BlockGenome`, par exemple :
  - décaler un quart entier (changer `start`, en restant dans la plage utile) ;
  - déplacer une frontière entre deux blocs voisins (une durée augmente, l'autre diminue d'autant : `Σd` est conservée) ;
  - changer l'activité d'un bloc.
- Les opérateurs ne modifient jamais leurs entrées : ils rendent de nouveaux génomes (D7).

**Scaffoldé d'avance** : interfaces `Crossover[G]` et `Mutation[G]`, exceptions et messages.

**Dépendances**
- `src/ga/chromosome.py` : `BlockGenome`, `BlockGene`, `ActivityBlock`, `BlockEncoding`
- `src/utils/io.py` : `ProblemInstance` (plage utile, nombre d'activités)
- `src/model/shift_rules.py` : `ShiftStructure`, `ShiftGaps` (durées minimales)
- `src/model/feasibility.py` : `FeasibilityChecker` (dans les tests : un opérateur appliqué à un génome faisable rend-il un génome faisable ?)
- `random.Random`, injecté (D5)

**Décisions de référence** : D1, D3 (pas de normalisation des employés au départ), D5 et D7 dans TODO.md. À garder en tête : la première expérience de l'étape 10 mesurera le taux de faisabilité des enfants par opérateur.

**Tests** : `python -m unittest tests.test_operators` (sans MiniZinc). Cas limites : population de deux individus identiques, gènes en bordure de fenêtre, blocs à la durée minimale.

### En équipe, pendant la semaine
- [ ] Trancher **D4** (remplacement, convergence, restart ; voir TODO.md), pour que l'étape 8 démarre la semaine suivante.
