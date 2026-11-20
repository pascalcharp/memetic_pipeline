# Planification du travail en équipe

## Règles communes

### Branches et fusion
- **Chacun travaille sur sa propre branche**, créée à partir de `main` et nommée d'après sa sous-étape : `etape-5b-local-solver`, `etape-6-initialisation`, `etape-7a-selection`, `etape-7b-variation`.
- **On ne fusionne dans `main` que lorsque tous les tests sont verts** : ceux de sa sous-étape et la suite complète (`python -m unittest discover`). La fusion passe par une *pull request* sur GitHub, relue par au moins un autre membre.
- Avant d'ouvrir la *pull request*, on intègre le dernier `main` dans sa branche et on relance la suite complète (voir les commandes ci-dessous).
- Une tâche à la fois par personne. Seules des sous-étapes sans dépendance entre elles avancent en parallèle.

### Commandes Git

Les branches existent déjà sur GitHub. Remplacer `<branche>` par la sienne (par exemple `etape-6-initialisation`).

**Pour commencer** (une seule fois, dans un clone du dépôt) :
```bash
git fetch origin            # récupère les branches créées sur GitHub
git switch <branche>        # crée la branche locale, reliée à origin/<branche>
```

**En cours de travail** (aussi souvent que voulu) :
```bash
git add <fichiers>
git commit -m "Étape Xy : ce qui a été fait"
git push                    # publie la branche sur GitHub (sauvegarde, visible par l'équipe)
```

**Avant d'ouvrir la *pull request*** :
```bash
git fetch origin
git merge origin/main       # intègre le main de GitHub, pas le main local, qui peut être en retard
python -m unittest discover # la suite complète doit être verte
git push
```
Puis ouvrir la *pull request* de `<branche>` vers `main` sur GitHub. La CI relance la suite complète dans Docker ; on fusionne quand elle est verte et qu'un autre membre a relu.

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
- [x] Étape 5b

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
- [x] Étape 6

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
- [x] Étape 7a

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
- [x] Étape 7b

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
- [x] Trancher **D4** (remplacement, convergence, restart ; voir TODO.md), pour que l'étape 8 démarre la semaine suivante. Tranchée le 2026-11-16 (Pascal et Claude).

---

## Semaine du 16 novembre

Avant le départ, Claude scaffolde en un seul commit sur `main` les interfaces, l'infrastructure d'observabilité et les squelettes de tests des étapes 8, 8b et 9. Chacun crée ensuite sa branche à partir de ce commit (Pascal garde la sienne, déjà créée, et y intègre `main`). Les noms de classes ci-dessous sont ceux du plan ; le scaffold peut les préciser.

Les quatre sous-étapes avancent en parallèle : chacune ne dépend que d'interfaces scaffoldées ou déjà sur `main`, et se teste avec des faux objets. Seule la sous-étape **9-intégration** (Pascal) attend la fusion des autres.

**Les tests à faire passer attendent déjà sur chaque branche** (`etape-8-population`, `etape-8b-observabilite`, `etape-9-boucle`) : écrits par Claude, ils sont rouges tant que la sous-étape n'est pas écrite, et ont été validés contre une implémentation de référence jetable, qui n'est pas dans le dépôt. Pour commencer : `git fetch origin`, puis `git switch <sa branche>`. Si un test semble contredire ce qu'il faudrait faire, on en discute avant de le modifier.

Rappel : les tests peuvent être écrits par un agent de codage (règle 0 de CLAUDE.md, PR #5) ; les méthodes et algorithmes de sa sous-étape, chacun les écrit lui-même. Préférer un vrai `random.Random` à graine fixée et des propriétés vérifiées sur beaucoup de tirages plutôt qu'un mock du générateur (leçon de la revue de 7b, DEVLOG du 2026-11-16).

### Pascal — Étape 5c : couverture « au moins 1 » en pénalité dans `horaire.mzn` (D12), puis 9-intégration
- [ ] Étape 5c
- [ ] Étape 9-intégration (après la fusion de 5c, 8, 8b et 9) : exécution complète sur `bench_1` avec les vrais composants (`MiniZincLocalSolver` + CP-SAT limité en effort déterministe), coût du meilleur monotone non croissant, reproductibilité avec et sans collecteurs, événements reçus dans l'ordre ; `tests/test_engine_integration.py` (appelle MiniZinc)

**Fichiers**
- `src/model/horaire.mzn`
- `src/memetic/solver.py`, `src/memetic/local_search.py`
- `tests/test_smoke_minizinc.py`, `tests/test_solver.py`, `tests/test_local_search.py`, et un test de validation croisée Python / MiniZinc

**À faire** (détail dans TODO.md, 5c)
- Trancher D12 en équipe d'abord : `src/model/` et `src/memetic/` sont des modules partagés.
- Modèle : la contrainte « au moins 1 » devient un compteur `violations_couverture`, et l'objectif devient `cout_penalise = cout_total + POIDS_COUVERTURE × violations_couverture`, avec le poids passé par Python (`PenaltyWeights.coverage_violation`).
- `SolverAdapter` : passe le poids au modèle ; nouveau nom d'objectif dans `ModelObjective`.
- `MiniZincLocalSolver` : la borne porte sur le coût pénalisé, posée dès que l'entrée n'a aucune violation structurelle.

**Dépendances**
- `src/model/evaluation.py` : `PenaltyWeights`, `CostEvaluator.total` (même fonction de coût que le modèle)
- `src/model/feasibility.py` : `FeasibilityChecker` (violations structurelles)

**Décisions de référence** : D10, D11, D12 ; D13 (redondance modèle / pipeline) à garder en tête.

**Tests** : `python -m unittest tests.test_smoke_minizinc tests.test_solver tests.test_local_search` (appellent MiniZinc).

### Tristan — Étape 8 : gestion de la population
- [ ] Étape 8

**Fichiers**
- `src/ga/population.py`
- `tests/test_population.py`

**Classes à écrire**
- `PlusSurvivorSelector` : implémente `SurvivorSelector` ; `SelectPop` en (μ+λ) sans doublons : tri stable par `cost.total` croissant, un seul exemplaire de chaque génome identique, les μ meilleurs ; s'il y a moins de μ génomes distincts, complète avec des doublons dans l'ordre des coûts.
- `DeathPenaltySurvivorSelector` : implémente `SurvivorSelector` ; les faisables (`cost.is_feasible`) d'abord, sans doublons, puis les meilleurs infaisables selon `cost.total` pour compléter à μ.
- `StagnationCriterion(generations)` : implémente `ConvergenceCriterion` ; convergence quand le coût du meilleur n'a pas baissé depuis `generations` générations ; `reset()` après un restart.
- `EliteRestart(elite_count, initializer, evaluator)` : implémente `RestartPolicy` ; garde les `elite_count` meilleurs, régénère le reste avec le `PopulationInitializer`, évalue les nouveaux individus.

**Scaffoldé d'avance** : interfaces `SurvivorSelector[G]`, `ConvergenceCriterion[G]`, `RestartPolicy[G]`, classe de constantes (G = 10, k = 1), exceptions et messages.

**Dépendances**
- `src/ga/individual.py` : `Individu`, `genome` (comparaison des génomes pour les doublons), `cost`, `with_cost`
- `src/model/evaluation.py` : `CostBreakdown.total`, `CostBreakdown.is_feasible`, `CostEvaluator.evaluate`
- `src/ga/initialization.py` : interface `PopulationInitializer` (restart)
- `src/ga/selection.py` : `check_selectable` (population vide, individus non évalués), si utile
- `random.Random`, injecté (D5)

**Décisions de référence** : D4 (tranchée le 2026-11-16), D5, D7 (individus immuables, entrées jamais modifiées).

**Tests** : `python -m unittest tests.test_population` (sans MiniZinc). Individus construits à la main avec des coûts choisis (`tests/fixtures.py`) ; faux `PopulationInitializer` pour le restart. Cas : taille conservée, meilleur jamais perdu, doublons éliminés, moins de μ génomes distincts, peine de mort avec trop peu de faisables, stagnation détectée après exactement G générations puis remise à zéro, élite conservée au restart.

### Mély — Étape 8b : collecteurs de l'observabilité
- [x] Étape 8b

**Fichiers**
- `src/observability/collectors.py`
- `tests/test_collectors.py`

**Classes à écrire**
- `CostStatisticsCollector` : à chaque fin de génération, statistiques de `cost.total` (min, moyenne, médiane, max, écart-type) et coût décomposé (sous-couverture, sur-couverture, violations « au moins 1 », cellules quasi dures).
- `DiversityCollector` : diversité génotypique insensible à la permutation des employés (par exemple la proportion de génomes distincts une fois les gènes triés), phénotypique (proportion de grilles « employé × période » distinctes) et des coûts (nombre de coûts distincts) ; fréquence configurable.
- `FeasibilityRateCollector` : taux de faisabilité des nouveaux individus par opérateur, avant et après le `LocalSolver`.
- `SolverEffortCollector` : charge cumulée du solveur (D10), à partir des statistiques des `local_search_done`.

**Scaffoldé d'avance** (par Claude, marqué (C) dans TODO.md, écrit et testé dans `tests/test_observability.py`) : catalogue des événements de D8 et schéma des enregistrements (`events.py` : `make_record`, `RunStarted`, `LocalSearchDone`, `IndividualCreated`, `GenerationEnded`, `Converged`, `Restarted`, `RunEnded`) ; interface `RecordSink` et les destinations `MemorySink`, `NullSink`, `ConsoleSink`, `JsonlSink`, `CsvSink` (`sinks.py`) ; diffusion `ObservationHub` (`hub.py`) ; configuration de `logging` (`logging_config.py`) ; répertoire d'exécution `results/<expérience>/<run_id>/` (`run_directory.py`). Dans `collectors.py` : interface `MetricCollector`, `RecordNames`, constantes, exceptions et squelettes des quatre collecteurs.

**Dépendances**
- `src/ga/individual.py` : `Individu`
- `src/model/evaluation.py` : `CostBreakdown` (total, termes, compteurs de violations, `is_feasible`)
- `src/model/horaire.py` : `Horaire.to_grid` (diversité phénotypique)
- `src/ga/chromosome.py` : `BlockGenome` (diversité génotypique)
- `src/memetic/solver.py` : `SolverStatistics` ; `src/memetic/local_search.py` : `LocalSearchResult`
- les événements scaffoldés de `src/observability/`

**Décisions de référence** : D8 (un collecteur ne consomme jamais le générateur aléatoire du moteur ; bibliothèque standard seulement), D10. D9 (MongoDB) : proposition de la reporter.

**Tests** : `python -m unittest tests.test_collectors` (sans MiniZinc). Populations construites à la main, résultats lus dans un `MemorySink`.

### Xavier — Étape 9 : boucle mémétique
- [ ] Étape 9

**Fichiers**
- `src/memetic/engine.py` (moteur `Memetic`), `src/memetic/config.py` (`MemeticConfig.validate`), `src/memetic/seeds.py` (`derive_task_seeds`), `src/memetic/termination.py` (`GenerationLimit`)
- `tests/test_engine.py`

**Classes à écrire**
- `Memetic` : la boucle du pseudo-code de CLAUDE.md. Tirage par lot des parents (NR) et des individus à muter (NM), variation, `LocalSolver`, ré-encodage de l'horaire réparé (`encoding.encode`), évaluation, `SelectPop`, convergence et restart, critère d'arrêt ; émission des événements de D8 après chaque lot.
- `MemeticConfig.validate` : la dataclass figée des stratégies et des paramètres scalaires (NR, NM, taille de population, graine maître) est scaffoldée ; reste sa validation (bornes de `MemeticDefaults`, compatibilité des opérateurs avec l'encodage).
- `derive_task_seeds(master_seed, generation, stream, task_count)` : dérivation des graines par tâche à partir de la graine maître (D7) ; les lots sont identifiés par `SeedStreams`.
- `GenerationLimit(generations)` : implémente `TerminationCriterion`.

**Scaffoldé d'avance** : `Executor` et `SequentialExecutor` (écrits et testés), interface `TerminationCriterion`, champs de `MemeticConfig`, `MemeticResult`, squelette de `Memetic` (le déroulement attendu est décrit dans la docstring de `engine.py`), `SeedStreams`, constantes, exceptions et messages ; faux objets communs dans `tests/fixtures.py` (`FakeCrossover`, `FakeMutation`, `FakeLocalSolver`, `FakeSurvivorSelector`, `FakeConvergenceCriterion`, `FakeRestartPolicy`, `RecordingCollector`) et une configuration factice complète dans `tests/test_engine.py`.

**Dépendances** (interfaces seulement ; le moteur ne connaît aucune classe concrète)
- `src/ga/initialization.py` : `PopulationInitializer` (étape 6)
- `src/ga/selection.py` : `ParentSelector`, `MutableSelector` (7a)
- `src/ga/operators.py` : `Crossover[G]`, `Mutation[G]` (7b)
- `src/memetic/local_search.py` : `LocalSolver`, `LocalSearchResult` (5b)
- `src/model/evaluation.py` : `CostEvaluator` (4)
- `src/ga/chromosome.py` : `Encoding[G]` (`encode`, `decode`) ; `src/ga/individual.py` : `Individu.from_genome`, `with_cost`
- `src/ga/population.py` : `SurvivorSelector`, `ConvergenceCriterion`, `RestartPolicy` (8, interfaces scaffoldées)
- `src/observability/` : `ObservationHub` (diffusion des événements), événements de `events.py`, `MetricCollector`, `RecordSink` (8b, scaffoldés)
- `src/memetic/executor.py` : `Executor`, `SequentialExecutor`

**Décisions de référence** : D5, D7 (lots, individus immuables, graines dérivées, `Executor`), D8 (événements), D10 (limite d'effort déterministe pour la reproductibilité).

**Tests** : `python -m unittest tests.test_engine` (sans MiniZinc, avec les faux objets) : terminaison, coût du meilleur monotone non croissant, reproductibilité (même graine ⇒ même historique, avec ou sans collecteurs), entrées des opérateurs jamais modifiées, événements reçus dans l'ordre. L'intégration avec les vrais composants (9-intégration) est faite par Pascal après les fusions.

### En équipe, pendant la semaine
- [ ] Trancher **D12** (couverture dure ou pénalisée), avant que Pascal modifie les modules partagés.
- [ ] Trancher **D14** (forme des exceptions), avant que les nouveaux modules en écrivent.
- [ ] Trancher **D9** (MongoDB) ; proposition : reportée, les fichiers de `results/` suffisent pour le POC.
- [ ] Relire et fusionner la PR #5 (règle des tests par agent dans CLAUDE.md).
- [ ] **D13** (redondance modèle / pipeline) : à discuter après 5c.
