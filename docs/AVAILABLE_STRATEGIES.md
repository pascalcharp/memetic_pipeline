# Stratégies disponibles

Catalogue de ce que le pipeline offre déjà, rôle par rôle : la classe, son fichier, ses paramètres (avec leur valeur par défaut), ce qu'elle fait, ce qu'elle garantit, et si l'assemblage de référence (`build_block_memetic_config`, `src/memetic/assembly.py`) l'utilise. État au 22 novembre 2026.

Pour **brancher** une stratégie, ou en **écrire** une nouvelle, voir [`HOWTO.md`](HOWTO.md). Pour la correspondance entre les rôles et le pseudo-code, voir [`ALGO.md`](ALGO.md). La dernière section liste les stratégies **prévues** mais pas encore écrites.

Légende de la colonne « Réf. » : ✅ utilisée par l'assemblage de référence ; ➖ disponible, à brancher soi-même.

1. [Encodage](#1-encodage)
2. [Initialisation](#2-initialisation)
3. [Sélection des parents](#3-sélection-des-parents)
4. [Croisement](#4-croisement)
5. [Sélection des individus à muter](#5-sélection-des-individus-à-muter)
6. [Mutation](#6-mutation)
7. [Recherche locale](#7-recherche-locale)
8. [Solveur, limites d'effort et modèles](#8-solveur-limites-deffort-et-modèles)
9. [Évaluation](#9-évaluation)
10. [Sélection des survivants (`SelectPop`)](#10-sélection-des-survivants-selectpop)
11. [Convergence](#11-convergence)
12. [Redémarrage](#12-redémarrage)
13. [Critère d'arrêt](#13-critère-darrêt)
14. [Exécution des lots](#14-exécution-des-lots)
15. [Observation : collecteurs et destinations](#15-observation--collecteurs-et-destinations)
16. [Stratégies prévues](#16-stratégies-prévues)

---

## 1. Encodage

Rôle `encoding` de `MemeticConfig`, interface `Encoding[G]` (`src/ga/chromosome.py`). L'encodage fixe le type `G` des génomes, donc les opérateurs et l'initialiseur compatibles.

| Classe | Paramètres | Réf. |
|---|---|---|
| `BlockEncoding` | aucun | ✅ |

**`BlockEncoding`** (décision D1). Un gène par employé (`BlockGene`) : la période de début, puis l'activité et la durée de chacun des quatre blocs (`ActivityBlock`). Les jalons se déduisent : `pause1 = debut + d1`, `diner = pause1 + 1 + d2`, `pause2 = diner + 4 + d3`, `fin = pause2 + d4`.
- Traduction pure et réciproque avec le phénotype `Horaire` (`decode(encode(h)) == h`) ; un génome peut décoder en horaire infaisable (D6).
- L'ordre des jalons est garanti par construction ; restent à respecter les durées minimales (`d_i ≥ 4`), l'amplitude du quart (6 à 8 heures rémunérées) et les fenêtres de l'instance.

---

## 2. Initialisation

Rôle `initializer`, interface `PopulationInitializer[G]` (`src/ga/initialization.py`). `initialize(size, rng)` rend un `InitializationResult(individuals, searches)` : des individus **non évalués** (le moteur les évalue) et les recherches locales faites pour les obtenir.

| Classe | Paramètres | Réf. |
|---|---|---|
| `RandomBlockInitializer` | `instance`, `encoding: BlockEncoding`, `local_solver: LocalSolver \| None = None` | ✅ avec `local_solver` (`AssemblySettings.initial_local_search = True`) |

**`RandomBlockInitializer`**. Tire des génomes `BlockGenome` **structurellement faisables** : durées, amplitude, quart dans la plage utile, activités valides. Si `local_solver` est donné, chaque horaire tiré lui est passé, et l'individu est construit à partir de l'horaire rendu ; chaque appel est noté dans `searches` (la charge du solveur à l'initialisation est ainsi comptée, D10). Le même initialiseur sert au restart (`EliteRestart`).

---

## 3. Sélection des parents

Rôle `parent_selector`, interface `ParentSelector[G]` (`src/ga/selection.py`). Le moteur tire en **un seul appel** les `NR × parent_count()` parents d'une génération (D7), avec remise.

| Classe | Paramètres | Réf. |
|---|---|---|
| `TournamentSelector` | `size: int = 2` (`SelectionDefaults.TOURNAMENT_SIZE`, au moins 1) | ✅ `AssemblySettings.tournament_size` |

**`TournamentSelector`**. Pour chaque parent, tire `size` individus au hasard (avec remise) et retient celui de plus petit `cost.total`. `size = 1` équivaut à un tirage uniforme ; plus `size` est grand, plus la pression de sélection est forte.

Commun à tous les sélecteurs : `check_selectable(population, count)` lève `InvalidSelectionParameterError` (`count < 1`), `EmptyPopulationError` ou `UnevaluatedIndividualError`.

---

## 4. Croisement

Rôle `crossover`, interface `Crossover[G]` (`src/ga/operators.py`). Le moteur fait exactement **NR croisements par génération** (`crossover_count`) ; il n'y a pas de probabilité de croisement (voir [`HOWTO.md`, section 2](HOWTO.md#2-je-veux-modifier-la-probabilité-de-crossover)).

| Classe | Encodage | Parents → enfants | Paramètres | Réf. |
|---|---|---|---|---|
| `UniformGeneCrossover` | `BlockEncoding` | 2 → 2 | aucun | ✅ |

**`UniformGeneCrossover`** (croisement uniforme, Syswerda 1989). Pour chaque employé, un tirage décide si les deux enfants échangent le gène de cet employé. Rend deux enfants complémentaires.
- Échange des **gènes entiers** : chaque quart reste faisable, seule la couverture change.
- Lève `WrongParentCountError` (pas exactement 2 parents) et `ParentLengthMismatchError` (parents de longueurs différentes).
- Limite connue (D3) : les employés sont interchangeables, et deux parents peuvent décrire presque le même horaire avec les employés permutés ; le croisement ne les aligne pas.

---

## 5. Sélection des individus à muter

Rôle `mutable_selector`, interface `MutableSelector[G]` (`src/ga/selection.py`). Le moteur tire en un seul appel les NM individus à muter, dans la population qui contient déjà les enfants du lot NR.

| Classe | Paramètres | Réf. |
|---|---|---|
| `UniformMutableSelector` | aucun | ✅ |

**`UniformMutableSelector`**. Tirage uniforme avec remise, sans regard au coût.

---

## 6. Mutation

Rôle `mutation`, interface `Mutation[G]` (`src/ga/operators.py`). Le moteur fait exactement **NM mutations par génération** (`mutation_count`). Chaque opérateur ci-dessous modifie **un seul gène** (un seul employé) par appel, et lève `EmptyGenomeError` pour un génome vide. Les amplitudes sont des constantes de `OperatorDefaults`.

| Classe | Encodage | Paramètres | Réf. |
|---|---|---|---|
| `ShiftStartMutation` | `BlockEncoding` | `instance` | ✅ |
| `BlockBoundaryMutation` | `BlockEncoding` | aucun | ➖ |
| `ActivityMutation` | `BlockEncoding` | `instance` | ➖ |

**`ShiftStartMutation`**. Décale le quart entier d'un employé tiré au hasard, de 1 à 3 périodes (`MIN_SHIFT_AMPLITUDE`, `MAX_SHIFT_AMPLITUDE`) vers le plus tôt ou le plus tard. Le décalage est borné pour que le quart reste dans les fenêtres de début et de fin de l'instance. Les durées ne changent pas.

**`BlockBoundaryMutation`**. Déplace la frontière entre deux blocs voisins d'un employé tiré au hasard : une durée augmente de 1 à 3 périodes (`MIN_BOUNDARY_TRANSFER`, `MAX_BOUNDARY_TRANSFER`), l'autre diminue d'autant. La somme des durées est conservée, et chaque durée reste au moins `ShiftStructure.MIN_ACTIVITY_DURATION`. Si aucun gène ne peut céder la quantité tirée, le génome est rendu inchangé.
- Limite connue : le déplacement d'une pause ou du dîner peut sortir de sa fenêtre ; une amplitude calculée à partir des contraintes du quart est prévue (TODO, étape 7b).

**`ActivityMutation`**. Change l'activité d'un bloc tiré au hasard pour une **autre** activité de l'instance. Les jalons ne changent pas, donc le quart reste faisable. Sur une instance à une seule activité (`bench_1`), le génome est rendu inchangé.

---

## 7. Recherche locale

Rôle `local_solver`, interface `LocalSolver` (`src/memetic/local_search.py`). `improve(horaire, rng)` rend un `LocalSearchResult` : l'horaire amélioré (ou l'horaire d'entrée si aucune solution), l'issue, les employés libérés et les statistiques du solveur.

| Classe | Paramètres | Réf. |
|---|---|---|
| `MiniZincLocalSolver` | `instance`, `adapter: SolverAdapter`, `neighborhood: Neighborhood`, `evaluator: CostEvaluator` | ✅ |

**`MiniZincLocalSolver`** (décision D11). Fixe les cinq jalons et les quatre activités de chaque employé **non libéré** par le voisinage, puis demande au solveur de ré-optimiser les autres. Quand l'horaire d'entrée est une solution du sous-problème, ajoute la borne « coût ≤ coût actuel », et le résultat n'est jamais pire : avec le modèle `RELAXED`, dès qu'il n'a aucune violation structurelle ; avec le modèle `REFERENCE`, seulement s'il est faisable. Sans solution, rend l'horaire d'entrée avec l'issue du solveur.

Le **voisinage** choisit les employés libérés ; interface `Neighborhood`, même fichier :

| Classe | Paramètres | Réf. |
|---|---|---|
| `RandomEmployeesNeighborhood` | `instance`, `size: int = 1` (`NeighborhoodDefaults.RANDOM_EMPLOYEE_COUNT`, au moins 0) | ✅ `AssemblySettings.neighborhood_size` |

**`RandomEmployeesNeighborhood`**. Libère `size` employés tirés au hasard, **plus** tous les employés structurellement infaisables (ils doivent être réparés). `size = 0` ne libère que les infaisables ; `size ≥` nombre d'employés libère tout l'horaire (résolution complète). Plus `size` est grand, plus le sous-problème est gros et la charge du solveur élevée.

---

## 8. Solveur, limites d'effort et modèles

Tout est dans `src/memetic/solver.py`. Le `MiniZincLocalSolver` reçoit un `SolverAdapter`, qui reçoit des `SolverOptions` et un modèle (`ModelVariant`).

**Adaptateurs** (interface `SolverAdapter`) :

| Classe | Solveur MiniZinc | Limites comprises | Réf. |
|---|---|---|---|
| `CpSatAdapter` | `cp-sat` (OR-Tools CP-SAT) | `DeterministicTimeLimit`, `WallTimeLimit` | ✅ |

**`CpSatAdapter`**. Transmet la graine (`random_seed`), le nombre de threads et la limite. Les autres solveurs du *bundle* MiniZinc (Gecode, Chuffed, HiGHS) n'ont pas encore d'adaptateur : voir [`HOWTO.md`, section 9](HOWTO.md#9-je-veux-essayer-la-boucle-avec-un-autre-solveur-sur-minizinc).

**Options** (`SolverOptions`) :

| Champ | Défaut | Remarque |
|---|---|---|
| `limit: EffortLimit` | `DeterministicTimeLimit(5.0)` (`SolverDefaults.DETERMINISTIC_TIME_UNITS`) | l'assemblage passe `AssemblySettings.deterministic_time_units` |
| `seed: int` | `0` | |
| `threads: int` | `1` | au moins 1 ; plus d'un thread rend CP-SAT non reproductible |

**Limites d'effort** (décision D10), sous-classes d'`EffortLimit` :

| Classe | Paramètre | Reproductible | Comprise par |
|---|---|---|---|
| `DeterministicTimeLimit` | `units` (> 0), temps déterministe de CP-SAT | oui, avec un thread et une graine fixée | CP-SAT |
| `WallTimeLimit` | `seconds` (> 0) | non | tous les solveurs |

Une limite qu'un adaptateur ne comprend pas lève `UnsupportedLimitError` à sa construction.

**Modèles** (décision D12), constantes de `ModelVariants` :

| Modèle | Fichier | Couverture « au moins un employé par activité » | Objectif | Réf. |
|---|---|---|---|---|
| `ModelVariants.RELAXED` | `src/model/horaire_assoupli.mzn` | pénalité (même fonction de coût que `CostEvaluator.total`) | `cout_penalise` | ✅ |
| `ModelVariants.REFERENCE` | `src/model/horaire.mzn` (le modèle fourni, inchangé) | contrainte dure | `cout_total` | ➖ |

`REFERENCE` sert aux comparaisons (résolution complète par CP-SAT seul) et à une éventuelle variante « peine de mort ». Dans la recherche locale, un sous-problème qui viole la couverture y devient insatisfiable.

---

## 9. Évaluation

Rôle `evaluator` (`src/model/evaluation.py`). Il n'y a pas d'interface : une seule classe.

| Classe | Paramètres | Réf. |
|---|---|---|
| `CostEvaluator` | `instance`, `weights: PenaltyWeights = PenaltyWeights()` | ✅ (le même objet pour le moteur, le `LocalSolver` et le restart) |

**`CostEvaluator`**. `evaluate(horaire)` rend un `CostBreakdown` : coût de sous-couverture, de sur-couverture, cellules quasi dures, violations de la couverture « au moins un », violations structurelles, pénalités, et `total`, le coût à minimiser. `is_feasible` est vrai s'il n'y a ni violation structurelle ni violation de la couverture « au moins un employé par activité » : depuis D12, cette couverture est une pénalité dans le coût, mais elle compte toujours pour la faisabilité.

**Poids** (`PenaltyWeights`) : `coverage_violation = 1 000 000` et `structural_violation = 1 000 000` par violation (`EvaluationDefaults`). Le poids de couverture est aussi transmis au modèle `RELAXED`.

---

## 10. Sélection des survivants (`SelectPop`)

Rôle `survivor_selector`, interface `SurvivorSelector[G]` (`src/ga/population.py`). `select(population, size, rng)` ramène parents et nouveaux individus à `size` individus. Les deux sélecteurs appellent `check_selectable`, ne modifient pas leur entrée, et rendent toujours `size` individus si la population en compte au moins autant.

| Classe | Paramètres | Élitiste | Réf. |
|---|---|---|---|
| `PlusSurvivorSelector` | aucun | oui | ✅ |
| `DeathPenaltySurvivorSelector` | aucun | parmi les faisables | ➖ |

**`PlusSurvivorSelector`** ((μ+λ) sans doublons, décision D4). Tri stable par `cost.total` croissant ; un seul exemplaire de chaque génome ; les `size` meilleurs. S'il y a moins de `size` génomes distincts, complète avec les doublons écartés, dans l'ordre des coûts. Le meilleur individu n'est jamais perdu.
- L'élimination des doublons empêche les copies produites par le `LocalSolver` (plusieurs individus réparés vers la même solution) d'envahir la population.
- Limite connue (D3) : deux génomes égaux à une permutation des employés près ne sont pas des doublons.

**`DeathPenaltySurvivorSelector`** (variante « peine de mort », D4). Les individus faisables d'abord, sans doublons et par `cost.total` croissant ; s'il en manque, les meilleurs infaisables ; s'il manque encore des individus, les doublons écartés (faisables d'abord). La population garde sa taille, et la variante se rapproche de la pénalité quand les faisables manquent. « Faisable » veut dire `cost.is_feasible` : ni violation structurelle, ni violation de la couverture « au moins un » (section 9).

---

## 11. Convergence

Rôle `convergence`, interface `ConvergenceCriterion[G]` (`src/ga/population.py`). `has_converged(population)` est appelé une fois par génération, après `SelectPop` ; `reset()` après chaque restart. Un critère garde un état : une configuration par exécution.

| Classe | Paramètres | Réf. |
|---|---|---|
| `StagnationCriterion` | `generations: int = 10` (`PopulationDefaults.STAGNATION_GENERATIONS`, au moins 1) | ✅ `AssemblySettings.stagnation_generations` |

**`StagnationCriterion`**. La population a convergé quand le coût du meilleur individu n'a pas **baissé** depuis `generations` générations. La première génération (et la première après `reset`) fixe la référence ; une hausse compte comme une génération sans baisse. Lève `EmptyPopulationForConvergenceError` pour une population vide.

---

## 12. Redémarrage

Rôle `restart`, interface `RestartPolicy[G]` (`src/ga/population.py`). `restart(population, rng)` rend un `RestartResult(elite, newcomers, searches)` ; le moteur publie les recherches et les nouveaux individus, puis remplace la population par `result.population`.

| Classe | Paramètres | Réf. |
|---|---|---|
| `EliteRestart` | `initializer`, `evaluator`, `elite_count: int = 1` (`PopulationDefaults.RESTART_ELITE_COUNT`, au moins 1) | ✅ `AssemblySettings.elite_count` |

**`EliteRestart`** (D4). Garde jusqu'à `elite_count` meilleurs individus **distincts** et régénère le reste avec `initializer` (donc avec son `LocalSolver`, s'il en a un), puis évalue les nouveaux. L'élite n'est jamais complétée par des doublons : s'il y a moins de `elite_count` génomes distincts, on en garde moins et on en régénère davantage. Le nombre de nouveaux individus varie donc entre `μ − elite_count` et `μ − 1`. Lève `InvalidPopulationParameterError` si `elite_count` dépasse la taille de la population.

---

## 13. Critère d'arrêt

Rôle `termination`, interface `TerminationCriterion[G]` (`src/memetic/termination.py`). `is_done(generation, population)` est consulté après chaque génération, à partir de la génération 0 (l'initialisation).

| Classe | Paramètres | Réf. |
|---|---|---|
| `GenerationLimit` | `maximum_generations: int` (au moins 1) | ✅ `AssemblySettings.generations` |

**`GenerationLimit`**. Exactement `maximum_generations` générations après l'initialisation.

---

## 14. Exécution des lots

Rôle `executor`, interface `Executor` (`src/memetic/executor.py`). `map(tâche, lot)` applique une tâche à chaque élément d'un lot et rend les résultats **dans l'ordre du lot** (D7).

| Classe | Paramètres | Réf. |
|---|---|---|
| `SequentialExecutor` | aucun | ✅ (valeur par défaut de `MemeticConfig.executor`) |

**`SequentialExecutor`**. Exécute les tâches une à une, dans le fil courant. Les tâches du moteur sont indépendantes (chacune a sa graine, aucune ne modifie d'état partagé) : un exécuteur parallèle pourra le remplacer sans changer le résultat (TODO, D7).

---

## 15. Observation : collecteurs et destinations

Rôle `dispatcher` : un `ObservationHub(collectors, sinks)` (`src/observability/hub.py`), qui diffuse chaque événement du moteur aux collecteurs et écrit leurs enregistrements dans chaque destination (D8). Par défaut, un hub sans collecteur : rien n'est mesuré. Le moteur ferme le hub à la fin de `run`. Exemple complet : [`HOWTO.md`, section 1](HOWTO.md#1-je-veux-faire-rouler-la-boucle-mémétique).

**Collecteurs** (interface `MetricCollector`, `src/observability/collectors.py`). Les noms des champs sont des constantes de `RecordFields`, `CostStatisticsFields`, `DiversityFields`, `FeasibilityFields` et `SolverEffortFields`.

| Classe | Paramètres | Enregistrement (`RecordNames`) | Quand | Contenu |
|---|---|---|---|---|
| `CostStatisticsCollector` | aucun | `cost_statistics` | à chaque fin de génération | taille, nombre de faisables, min, moyenne, médiane, max et écart-type de `cost.total`, moyennes du coût décomposé |
| `DiversityCollector` | `period_count` (`instance.period_count`), `every: int = 1` | `diversity` | toutes les `every` générations | diversité génotypique (insensible à la permutation des employés), phénotypique (grilles distinctes), nombre de coûts distincts |
| `FeasibilityRateCollector` | aucun | `feasibility_rates` | par génération et cumulé à la fin, par (origine, opérateur) | taux de faisabilité avant et après le `LocalSolver` |
| `SolverEffortCollector` | aucun | `solver_effort` | par génération et cumulé à la fin | nombre d'appels, `nodes`, `failures`, `propagations`, temps de résolution (non déterministe) |

Les origines sont `initialization`, `crossover`, `mutation` et `restart` (`Origins`, `src/observability/events.py`) ; l'opérateur est le nom de la classe du croisement ou de la mutation, `None` pour l'initialisation et le restart.

**Destinations** (interface `RecordSink`, `src/observability/sinks.py`) :

| Classe | Paramètres | Écrit |
|---|---|---|
| `NullSink` | aucun | rien (destination par défaut d'un hub sans destination) |
| `MemorySink` | aucun | une liste en mémoire, `records` ; `of_event(nom)` filtre par type (pour les tests) |
| `ConsoleSink` | `stream = sys.stdout` | une ligne JSON par enregistrement |
| `JsonlSink` | `path` | une ligne JSON par enregistrement dans un fichier (créé ou écrasé) |
| `CsvSink` | `path`, `event` | un tableau CSV des seuls enregistrements de type `event` (colonnes fixées par le premier) |

**Autour** : `RunDirectory.create(expérience)` crée `results/<expérience>/<run_id>/` et ses chemins (`events_path`, `generations_path`, `run_log_path`, `config_path`) ; `write_config(seed, parameters)` écrit `config.json` (graine, commit Git, versions). `configure_logging(level, console, run_log)` configure le journal de diagnostic (`src/observability/logging_config.py`).

---

## 16. Stratégies prévues

Planifiées dans [`TODO.md`](../TODO.md), pas encore écrites :

| Rôle | Stratégie | Où dans le TODO |
|---|---|---|
| Encodage | `DirectEncoding` (le phénotype comme génome), `SortedBlockEncoding` (gènes triés, contre l'interchangeabilité des employés) | étape 10, décisions D1 et D3 |
| Croisement | croisement avec alignement des employés entre les parents | étape 10, D3 |
| Croisement | `LinearInterpolationCrossover` : interpolation des jalons, avec appariement des employés, et variante biaisée par les coûts | 7c, optionnelle |
| Mutation | `BlockBoundaryMutation` avec une amplitude calculée à partir des contraintes du quart | 7b |
| Voisinage | `TimeWindowNeighborhood` : libère les employés qui chevauchent une fenêtre de temps coûteuse | 5b, optionnelle |
| Limite d'effort | `FailureLimit` (nombre d'échecs, reproductible avec Gecode) | D10 |
| Solveur | `CpSatApiAdapter` : CP-SAT par l'API Python d'OR-Tools, sans MiniZinc | étape 10, si l'aplatissement domine le temps |
| Exécution | exécuteur parallèle (threads ou processus) | D7 |
| Destination | `MongoSink` | D9, reportée |
