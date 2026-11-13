# TODO — Proof of concept : algorithme mémétique pour l'horaire

Légende :
- `[ ]` à faire · `[~]` en cours · `[x]` validé (tests verts)
- **(C)** Claude écrit · **(P)** le membre responsable écrit, Claude vérifie · **(C→P)** Claude scaffolde (signatures, docstrings, tests), le membre responsable implémente
- Responsable : Pascal jusqu'à l'étape 5a ; depuis le 9 novembre, voir la répartition dans [`TEAM.md`](TEAM.md)

Règle : une seule étape à la fois **par personne et par branche** ; on ne fusionne dans `main` qu'une fois les tests verts (cas nominaux + cas limites). Seules des étapes sans dépendance entre elles avancent en parallèle.

---

## Décisions de conception à trancher (avant l'étape concernée)

- [x] **D1 — Encodage du chromosome** : l'encodage est polymorphe (interface `Encoding[G]`, voir D5) ; interface réduite à `encode(Horaire) -> G` et `decode(G) -> Horaire`, traduction pure (D6).
  - premier encodage implémenté : **par blocs** (`BlockEncoding`), un gène par employé : `debut, a1, d1, a2, d2, a3, d3, a4, d4` (activité et durée de chacun des 4 blocs) ;
  - jalons déduits : `pause1 = debut + d1`, `diner = pause1 + 1 + d2`, `pause2 = diner + 4 + d3`, `fin = pause2 + d4` ; bijection avec les jalons du phénotype, donc traduction pure ;
  - l'ordre des jalons est garanti par construction, et les 4 écarts minimaux deviennent des domaines par gène (`d_i ≥ 4`) ;
  - restent deux contraintes de couplage : `22 ≤ d1 + d2 + d3 + d4 ≤ 30` (6 à 8 h rémunérées, `fin - debut = Σd + 5`), et le quart dans la plage utile (`MIN_PERIODES ≤ debut`, `debut + Σd + 5 ≤ MAX_PERIODES`) ;
  - la contrainte de couverture concerne tous les encodages : elle relève de l'évaluation et du `LocalSolver`, pas de l'encodage ;
  - l'encodage direct (`DirectEncoding`, 5 jalons + 4 activités) devient une variante de comparaison, après la boucle complète ;
  - la représentation concrète du génome (tuple, tableau numpy) se décide au scaffold de l'étape 3b.
- [x] **D2 — Rôle de MiniZinc comme `SolveurLocal`** : recherche locale d'amélioration (on fixe une partie des gènes, le solveur ré-optimise le reste sous limite de temps). Solveur par défaut : CP-SAT. Les particularités de chaque solveur sont cachées derrière une classe d'indirection, pour pouvoir en changer (Gecode, Chuffed, HiGHS, …).
- [x] **D3 — Symétrie entre employés** : dans l'AG, c'est un problème de représentation (croiser deux parents équivalents mais permutés), pas de recherche.
  - **aucune contrainte de bris de symétrie dans le modèle MiniZinc** : CP-SAT gère les symétries mieux que nous, et la contrainte s'était montrée nuisible ;
  - premier temps : pas de normalisation ; on mesure l'effet (D8) avant de compliquer ;
  - variante 1 : ordre **lexicographique** sur le gène complet, dans un encodage distinct (`SortedBlockEncoding`, dont le génome est la liste triée des gènes) ; le tri est un invariant du génome, rétabli après chaque opérateur et après le `LocalSolver` ; c'est une vraie forme canonique, mais fragile aux quasi-permutations (la première clé, `debut`, domine l'ordre) ;
  - variante 2, en réserve : **alignement** des employés au croisement (affectation minimisant la distance entre quarts), responsabilité de l'opérateur, sans modifier les génomes.
- [x] **D5 — Architecture polymorphe du moteur génétique** : patron Stratégie, une interface abstraite par rôle du pseudo-code (`ParentSelector`, `Crossover[G]`, `MutableSelector`, `Mutation[G]`, `LocalSolver`, `SurvivorSelector`, `ConvergenceCriterion`, `RestartPolicy`, `TerminationCriterion`). Séparation génotype / phénotype : phénotype canonique unique `Horaire` (faisabilité, coût, grille, MiniZinc) ; génotype polymorphe via `Encoding[G]`. Les opérateurs de variation sont liés à un encodage ; la compatibilité est vérifiée à l'assemblage (`MemeticConfig`, exception `IncompatibleOperatorError`). Registre par nom pour décrire les expériences en configuration. `random.Random` injecté dans chaque opérateur (reproductibilité). Taux de mutation (scalaire) et type de mutation (implémentation) sont deux axes distincts.
- [x] **D6 — Responsabilité de `encode` / `decode`** : traduction pure, rien d'autre. `decode` peut rendre un `Horaire` infaisable ; la vérification de faisabilité et la réparation (`LocalSolver`) sont des responsabilités distinctes.
- [x] **D7 — Préparation au parallélisme** (aucun parallélisme dans le POC, mais l'architecture doit le permettre sans réécriture) :
  - boucles NR / NM traitées **par lot** : tous les parents sont tirés dans P, tous les enfants sont produits, puis ajoutés (pas de *steady-state*) ;
  - individus **immuables** (`frozen dataclass`) : les opérateurs retournent de nouveaux individus et ne modifient jamais leurs entrées ;
  - **RNG dérivé par tâche** (graine déterministe par tâche, ex. `SeedSequence.spawn`), jamais un RNG partagé entre tâches ;
  - interface **`Executor`** (`map(tâche, lot)`), avec pour seule implémentation `SequentialExecutor` ; une version par threads ou async viendra plus tard ;
  - à garder en tête : arbitrage entre appels parallèles et threads internes de CP-SAT ; une limite en temps rend le solveur non déterministe ; modèle en îles possible plus tard (`MigrationPolicy`).
- [x] **D8 — Observabilité : journal de diagnostic et données d'expérience** :
  - deux flux séparés : **diagnostic** (texte, niveaux, module `logging`) et **données d'expérience** (enregistrements structurés, schéma versionné) ;
  - patron **Observateur** : le moteur émet des événements (`run_started`, `individual_created`, `local_search_done`, `generation_ended`, `converged`, `restarted`, `run_ended`) ; des `MetricCollector` calculent, des `RecordSink` écrivent (`ConsoleSink`, `JsonlSink`, `CsvSink`, `MemorySink` pour les tests, `NullSink` par défaut) ; choix par configuration ;
  - statistiques : coût (min, moyenne, médiane, max, écart-type), **coût décomposé** (sous-couverture, sur-couverture, violations de la contrainte « au moins 1 », cellules à 1 000 000), diversité (génotypique insensible à la permutation des employés, phénotypique, des coûts ; fréquence configurable ou échantillonnage), efficacité des opérateurs, apport de la recherche locale ;
  - une exécution = `results/<expérience>/<run_id>/` (`config.json` avec graine, commit Git et versions, `events.jsonl`, `generations.csv`, `run.log`), ignoré par Git ;
  - principes : enregistrer assez de données brutes pour recalculer plus tard ; `schema_version` et `event` dans chaque enregistrement ; un collecteur ne consomme jamais le générateur aléatoire du moteur ; événements émis par le thread principal après chaque lot (D7) ; temps marqués non déterministes ; bibliothèque standard seulement.
- [ ] **D4 — Remplacement / convergence / restart** (avant étape 8) : élitisme (μ+λ) ? mesure de diversité ? quelle fraction conserver au restart ?
- [ ] **D9 — Résultats d'expérience dans MongoDB** (proposition de Pascal, 2026-11-07 ; à trancher avant l'étape 8b) :
  - se branche naturellement comme une destination de plus (`MongoSink`, patron Observateur de D8) : le moteur et les collecteurs ne changent pas ;
  - contredit le principe « bibliothèque standard seulement » de D8 : dépendance `pymongo` à isoler (import seulement dans `MongoSink`, tests sautés si absente) ;
  - à trancher : Atlas (nuage : identifiants hors du dépôt, accès réseau, tests sans connexion) ou conteneur `mongo` local dans un `docker-compose.yml` (pas encore créé ; seul le `Dockerfile` existe) ; garder ou non `results/` en fichiers comme copie de référence.
- [x] **D10 — Charge de travail cumulée du solveur** (proposition de Pascal, 2026-11-07 ; tranchée le 2026-11-08) :
  - idée : cumuler la charge de chaque appel au `LocalSolver` et la comparer à celle de MiniZinc seul, **avec le même solveur**, à coût égal (ou le coût atteint à charge égale) ;
  - **limite d'effort configurable et typée**, car chaque solveur a sa propre notion d'effort : `WallTimeLimit` (universel, non reproductible), `DeterministicTimeLimit` (CP-SAT : `max_deterministic_time`), plus tard `FailureLimit` (Gecode : `--fail`). Chuffed et HiGHS n'exposent que le temps mural. Pas de limite « générique » traduite par chaque solveur : les unités ne sont pas comparables ;
  - chaque `SolverAdapter` déclare les types de limites qu'il comprend ; une limite non comprise lève `UnsupportedLimitError` à la construction (comme `IncompatibleOperatorError`, D5) ;
  - défaut de `CpSatAdapter` : `DeterministicTimeLimit`, 1 thread, graine transmise. Vérifié : objectif, `failures` et `propagations` identiques d'une exécution à l'autre ; seul `solveTime` varie ;
  - mesure de la charge : statistiques standard de MiniZinc (`nodes`, `failures`, `propagations`, `solveTime`), en champs optionnels, puisque tous les solveurs ne les rapportent pas toutes ; `solveTime` est marqué non déterministe (D8).
- [x] **D11 — Recherche locale par MiniZinc** (tranchée le 2026-11-08) :
  - **voisinage** : interface `Neighborhood` (Stratégie, D5) qui choisit les employés à libérer ; les autres sont fixés à leur valeur actuelle. Première implémentation : k employés tirés avec le RNG injecté, **plus toujours les employés structurellement infaisables** (fixés, ils rendraient le sous-problème insatisfiable : leurs jalons sont hors domaine) ;
  - **borne de coût** : `cout_total ≤ coût de couverture de l'entrée` seulement si l'entrée est faisable (elle est alors elle-même solution du sous-problème : la borne est sûre et élague). Une entrée infaisable n'a pas de borne : le `LocalSolver` la répare ;
  - **échec** (insatisfiable, ou budget épuisé sans solution) : ce n'est pas une erreur. Le `LocalSolver` rend l'horaire d'entrée inchangé, avec le statut et les statistiques. Les exceptions sur mesure sont réservées aux pannes (MiniZinc absent, erreur du solveur, limite non supportée) ;
  - le `LocalSolver` travaille sur le phénotype `Horaire` (D5) ; le moteur ré-encode le résultat avec l'`Encoding`.
- [ ] **D12 — Couverture « au moins 1 » dans le `LocalSolver` : contrainte dure ou pénalité ?** (relevée par Pascal le 2026-11-13 ; à trancher en équipe avant l'étape 8, touche `src/model/` et `src/memetic/`, modules partagés) :
  - constat : l'évaluation (étape 4) pénalise chaque cellule vide où la demande est positive, mais le sous-problème du `LocalSolver` résout `horaire.mzn`, où c'est une contrainte dure (ligne 154). Une entrée qui viole « au moins 1 » avec peu d'employés libérés donne un sous-problème insatisfiable et revient inchangée, au lieu d'être améliorée (mesures du 2026-11-13 dans DEVLOG.md : 6 cas sur 6 sur bench_3 et bench_5 avec 2 employés libérés) ;
  - piste : une variante du modèle où la contrainte devient un terme `poids × cellules vides` dans l'objectif, avec le poids de `PenaltyWeights.coverage_violation` (même fonction de coût que `CostEvaluator.total`) ; le `LocalSolver` choisit le modèle (Stratégie, D5) ; la borne de coût porte alors sur le coût pénalisé, donc s'applique aussi aux entrées infaisables ;
  - questions : un seul modèle paramétré ou deux fichiers ? garder la variante dure pour comparer (lien avec la variante « peine de mort », étape 8) ? effet sur la propagation et le temps de CP-SAT ?

---

## Documentation (transversale) **(C)**
Principe : toute la documentation est dans `docs/`, et chaque document est accessible depuis le `README.md` à la racine. Objectif : un coéquipier entre dans le projet sans difficulté.
- [x] `docs/PROJECT_STRUCT.md` : arbre qui reflète **exactement** la structure actuelle du dépôt (CLAUDE.md garde l'arbre de l'**architecture cible**, avec un lien vers ce document)
- [x] `README.md` : point d'entrée, avec des liens vers chaque document de `docs/`. Structure : 1. Description (problème, algorithme, structure) ; 2. Je viens de cloner le dépôt (environnement, tests, expériences) ; 3. Contribuer (méthode, avancement, décisions, conventions)
- [x] `docs/PROBLEME.md` : description du problème pour un nouveau venu (employés, activités, périodes de 15 min, structure d'un quart et ses jalons, demande, coût de sur- et sous-couverture, contrainte « au moins 1 employé si demande > 0 », format des instances JSON). Retirer ensuite la mention « à venir » du README

## Étape 0 — Infrastructure et environnement **(C)**
- [x] Localisation de l'exécutable MiniZinc : variable d'environnement `MINIZINC_PATH` en priorité, sinon repli sur `minizinc.Driver.find()`, qui trouve aussi `/Applications/MiniZincIDE.app` sans `PATH` (donc pas de constante de repli). Exécutable absent ou invalide ⇒ `MiniZincNotFoundError`
- [x] Installer `requirements.txt` dans `.venv` (minizinc 0.10.0, numpy 2.5.4, Python 3.13.3)
- [x] Squelette `tests/` (unittest, découverte via `python -m unittest discover`) + `tests/test_minizinc_env.py` (15 tests verts)
- [x] Test de fumée : MiniZinc + CP-SAT résolvent `horaire.mzn` sur `bench_1.json` depuis Python (`tests/test_smoke_minizinc.py`, optimum 94 prouvé en < 1 s)
- [x] Dockerfile (Python 3.13 + MiniZinc + CP-SAT) : en second, le développement se fait d'abord en local dans PyCharm. Multi-stage depuis `minizinc/minizinc:2.10.0-noble`, testé en arm64 et amd64
- [x] Action GitHub : à chaque push sur `main`, construire l'image Docker et y lancer la suite de tests (`.github/workflows/tests.yml`, premier run vert)
- [x] Harmoniser la structure réelle avec CLAUDE.md (`horaire.mzn` vs `schedule_model.mzn`, noms des instances `bench_*.json`) : la documentation a été alignée sur les fichiers réels

## Étape 1 — Constantes du domaine **(C)**
- [x] Classe(s) de constantes : 4 activités par quart, durées pause (1 période) / dîner (4 périodes), activité min. (4 périodes), durée de quart (27..35), décalages des fenêtres (`+4`, `-17`, `+9`, `-12`, …) — `src/model/shift_rules.py` : `ModelIndexing`, `ShiftStructure`, `ShiftGaps`, `WindowOffsets`
- [x] Aucune valeur magique ailleurs dans le code ; tests vérifiant la cohérence avec `horaire.mzn` (`tests/test_shift_rules.py`, 12 tests, dont des sondes MiniZinc)

## Étape 2 — Lecture des instances (`src/utils/io.py`) **(C)**
- [x] Classe `Instance` (dataclass typée) : `NB_EMPLOYES`, `NB_ACTIVITES`, `NB_PERIODES`, `demande`, `surcout`, `souscout` — nommée `ProblemInstance` (évite la confusion avec `minizinc.Instance`), figée, matrices numpy en lecture seule
- [x] Calcul de `MIN_PERIODES` / `MAX_PERIODES` et des fenêtres dérivées (mêmes formules que le modèle) — `first_useful_period`, `last_useful_period`, `ShiftWindows`, vérifiés contre MiniZinc
- [x] Exceptions sur mesure (`InstanceError`, …) : fichier absent, champ manquant, dimensions incohérentes, valeurs négatives — plus types invalides, demande supérieure au nombre d'employés, plage utile vide ou trop courte (`NoShiftFitsError`)
- [x] Tests : les 5 bench se chargent ; JSON malformés ; instance où aucun quart ne rentre (ex. trop peu de périodes) — `tests/test_io.py`, 32 tests
- [x] `__repr__` (une ligne, sans les matrices) et `__str__` (résumé lisible : dimensions, plage utile, fenêtres, demande) pour `ProblemInstance` ; `__str__` pour `MilestoneWindow` (`début..fin`)

## Étape 3a — Phénotype `Horaire` **(C→P)**
- [x] Classes `Horaire` / `HoraireEmploye` (mêmes variables que `horaire.mzn`) — `src/model/horaire.py` : dataclasses figées, construction depuis les variables MiniZinc (`from_model_variables`), `MalformedHoraireError` pour une forme invalide (≠ 4 activités, aucun employé, variable manquante) **(C)**
- [x] Vérification de faisabilité structurelle (les contraintes de `horaire.mzn`), composant distinct de l'encodage — `src/model/feasibility.py` : `FeasibilityChecker.violations(horaire) -> list[Violation]` (règle `StructuralRule`, employé, valeur fautive) ; un horaire infaisable n'est pas une exception (D6), un nombre d'employés différent de l'instance en est une. Scaffold **(C)**, corps des vérifications **(P)**, vérifié
- [x] Conversion vers la grille « employé × période → activité ou 0 » (même sémantique que la 2ᵉ sortie du modèle) — `Horaire.to_grid(period_count)` **(C)**
- [x] Tests : horaires valides, chaque contrainte violée isolément, bornes exactes des fenêtres, contraintes redondantes (fenêtres intérieures), validation croisée avec MiniZinc (verdict de faisabilité, grille de la 2ᵉ sortie) — `tests/test_horaire.py` (20), `tests/test_feasibility.py` (17) **(C)**
- La couverture « au moins 1 employé si demande > 0 » n'est **pas** structurelle : elle relève de l'étape 4

## Étape 3b — Génotype : `Encoding[G]` et `BlockEncoding` (`src/ga/chromosome.py`) **(C→P)**
- [x] Trancher D1 : encodage par blocs, un gène par employé
- [x] Représentation du génome (D1, tranchée au scaffold) : dataclasses figées `ActivityBlock(activity, duration)`, `BlockGene(start, blocks)`, génome `BlockGenome = tuple[BlockGene, ...]` ; lisible, immuable (D7), hachable (D8). `MalformedGenomeError` si un gène n'a pas 4 blocs **(C)**
- [x] Interface `Encoding[G]` : `encode(Horaire) -> G`, `decode(G) -> Horaire` (traduction pure, D6) **(C)**
- [x] Implémentation `BlockEncoding` : `encode_shift`, `decode_gene` (un employé), `encode`, `decode` **(P)**
- [x] Classe `Individu` (`src/ga/individual.py`) : génome, phénotype décodé à la construction (`from_genome`), coût optionnel, `with_cost` qui retourne un nouvel individu (D7) **(C)**
- [x] Tests **(C)** :
  - aller-retour dans les deux sens, `decode(encode(h)) == h` et `encode(decode(g)) == g`, y compris pour un horaire infaisable (jalons dans le désordre, durées négatives) ;
  - exemple de D1 : employé 1 de l'optimum de bench_1, d = 4, 4, 6, 8 ;
  - décodage d'un génome infaisable sans exception (Σd hors de 22..30, quart débordant la plage utile), constaté par `FeasibilityChecker` ;
  - propriété de D1 sur des gènes tirés au hasard (graine fixe) : l'horaire décodé est faisable si et seulement si chaque `d_i ≥ 4`, `22 ≤ Σd ≤ 30`, le quart est dans la plage utile et les activités dans leur domaine ;
  - validation croisée : aller-retour sur les solutions MiniZinc de bench_1 à bench_3 ;
  - `Individu` testé avec un encodage factice, indépendant de `BlockEncoding`

## Étape 4 — Évaluation (`src/model/evaluation.py`) **(C→P)**
- [x] Trancher le traitement des violations (2026-11-07) : **pénalité**, pas d'infaisabilité ni d'exception. L'évaluation est définie pour tout horaire décodé (D6) :
  - « au moins 1 employé si demande > 0 » (contrainte dure de `horaire.mzn`, absente de `cout_total`) : chaque cellule (période, activité) violée est comptée et pénalisée ;
  - violations structurelles (`FeasibilityChecker`) : comptées et pénalisées elles aussi ; la couverture est calculée quand même, à partir de la grille ;
  - poids des pénalités dans `PenaltyWeights` (dataclass figée, valeurs par défaut dans `EvaluationDefaults`), injectables pour les expériences.
- [x] Scaffold **(C)** :
  - `CostBreakdown` (dataclass figée, D8) : `under_coverage_cost`, `over_coverage_cost`, `quasi_hard_cells` (cellules sous-couvertes à sous-coût ≥ 1 000 000, informatif : déjà inclus dans le sous-coût), `coverage_violations`, `structural_violations`, `penalty_cost` ; propriétés `coverage_cost` (identique à `cout_total`), `total` (fitness), `is_feasible` ;
  - `CostEvaluator(instance, weights)` : signatures et docstrings de `coverage_totals(horaire)` et `evaluate(horaire)` ;
  - `Individu.cost` devient `CostBreakdown | None`.
- [x] Implémentation **(P)** (2026-11-08) : `coverage_totals` (`total[p, a]` calculé bloc par bloc, plage utile seulement, quatre blocs testés indépendamment comme les quatre `sum` de `horaire.mzn`), puis `evaluate`.
- [x] Tests **(C)** — `tests/test_evaluation.py`, 30 tests verts :
  - `CostBreakdown` : propriétés, immuabilité ;
  - `coverage_totals` : forme, cellule par cellule sur des cas à la main, périodes hors plage utile ignorées, blocs qui se chevauchent comptés une fois par bloc ;
  - cas calculés à la main sur l'instance synthétique : couverture parfaite (coût 0), sous-couverture, sur-couverture, bonne colonne d'activité, violation de « au moins 1 », cellule quasi dure, violation structurelle, poids personnalisés ;
  - optimum de bench_1 : coût 94, aucune violation ;
  - nombre d'employés différent de l'instance : `EmployeeCountMismatchError` (propagée depuis `FeasibilityChecker`) ;
  - **validation croisée** : `coverage_cost` égal à l'objectif renvoyé par MiniZinc sur les solutions de bench_1 à bench_3, sans aucune violation.

## Étape 5 — Interface MiniZinc et recherche locale **(C→P)**
- [x] Trancher D10 (limite d'effort) et D11 (voisinage, borne, échec) — 2026-11-08

### 5a — `SolverAdapter` (`src/memetic/solver.py`) **(C)** — validée le 2026-11-08, 23 tests verts
- [x] Limites d'effort, dataclasses figées : `EffortLimit` (base), `WallTimeLimit(seconds)`, `DeterministicTimeLimit(units)`
- [x] `SolverOptions(limit, seed, threads = 1)` ; valeurs par défaut dans une classe de constantes
- [x] `SolverStatistics` : `nodes`, `failures`, `propagations` (optionnels, déterministes), `solve_time` (optionnel, non déterministe)
- [x] `SolveOutcome` (enum) : `OPTIMAL`, `FEASIBLE`, `UNSATISFIABLE`, `NO_SOLUTION` (budget épuisé sans solution) ; traduction des `minizinc.Status`
- [x] `SolverRun` : issue, variables de la meilleure solution (ou `None`), objectif, statistiques
- [x] Interface `SolverAdapter` : `solver_id`, `supported_limits`, `solve(instance, extra_constraints) -> SolverRun` ; vérification de la limite à la construction
- [x] `CpSatAdapter` : traduction des limites (`--fzn-flags "--params max_deterministic_time:…,random_seed:…"`, ou `time_limit`), threads, solutions intermédiaires (on garde la dernière)
- [x] Exceptions : `SolverError` (base), `UnsupportedLimitError`, `SolverFailureError` (enveloppe `minizinc.MiniZincError`) ; gabarits dans `SolverMessages`
- [x] Résolution complète = `solve` sans contrainte ajoutée (référence pour comparer le mémétique, D10)
- [ ] **Amélioration possible de `SolverAdapter.solve`** (relevée le 2026-11-10, à discuter en équipe : `solver.py` est un module partagé) : quand toutes les variables d'un sous-problème insatisfiable sont fixées, MiniZinc émet `MiniZincWarning: model inconsistency detected` dès l'aplatissement. Pour le mémétique, c'est une issue normale (D11) ; dans la boucle, cet avertissement apparaîtra chaque fois qu'un individu viole « au moins 1 » avec peu d'employés libérés. Piste : ignorer **seulement** cet avertissement dans `solve`, filtré par son message, sans masquer les autres avertissements de MiniZinc ; puis retirer les `warnings.catch_warnings` des tests (`test_solver.py`, `test_local_search.py`). Dans un commit à part
- [x] Tests :
  - traduction des limites en options, sans lancer MiniZinc ; limite non supportée ⇒ `UnsupportedLimitError` ;
  - traduction de chaque `minizinc.Status` ;
  - bench_1 : optimum 94 prouvé (`OPTIMAL`) ;
  - reproductibilité : deux appels de même graine et de même limite déterministe ⇒ même objectif, mêmes `failures` et `propagations` ;
  - contrainte impossible ajoutée ⇒ `UNSATISFIABLE` ; budget minuscule sur bench_5 ⇒ `NO_SOLUTION` ;
  - statistiques présentes pour CP-SAT.

### 5b — `LocalSolver` (`src/memetic/local_search.py`) **(C→P)** — Pascal, branche `etape-5b-local-solver` — validée le 2026-11-10
- [x] Scaffold **(C)**, dans le scaffold commun : interface `Neighborhood` (`select(horaire, rng) -> employés à libérer`), interface `LocalSolver` (`improve(horaire, rng) -> LocalSearchResult`), `LocalSearchResult` (horaire, issue, employés libérés, statistiques, figé), gabarits des contraintes MiniZinc, exceptions et messages
- [x] `RandomEmployeesNeighborhood(instance, size)` **(P)** : `size` employés tirés au hasard, plus les employés structurellement infaisables (`FeasibilityChecker`)
- [x] `MiniZincLocalSolver(instance, adapter, neighborhood, evaluator)` **(P)** :
  - contraintes de fixation des employés non libérés (noms tirés de `ModelVariableNames`) ;
  - borne `cout_total ≤ coverage_cost` si l'entrée est faisable (`CostBreakdown.is_feasible`) ;
  - solution ⇒ `Horaire.from_model_variables` ; aucune solution ⇒ horaire d'entrée inchangé
- [x] Tests **(C)**, écrits sur la branche de Pascal (2026-11-09, 26 tests ; validés contre une implémentation de référence jetable) ; implémentation validée le 2026-11-10, suite complète verte (228 tests) :
  - les employés non libérés sont inchangés ; l'entrée n'est jamais modifiée ;
  - entrée faisable ⇒ coût de couverture du résultat ≤ celui de l'entrée ;
  - un employé infaisable est toujours libéré ; réparation d'une entrée infaisable sur bench_1 ;
  - cas limites : k = 0 (seuls les infaisables sont libérés), k ≥ nombre d'employés (tout est libre), sous-problème insatisfiable ⇒ entrée rendue avec son statut ;
  - reproductibilité : même graine du RNG et même limite déterministe ⇒ même résultat.

## Travail en équipe — semaine du 9 novembre **(C)**
Répartition et règles communes : [`TEAM.md`](TEAM.md). Les étapes 5b, 6, 7a et 7b avancent en parallèle, chacune sur sa branche.
- [x] Répartition du travail et règles communes (`TEAM.md`) ; workflow d'équipe dans `CLAUDE.md` ; CI déclenchée aussi sur les *pull requests* vers `main`
- [x] **Scaffold commun** (2026-11-09), en un seul commit sur `main`, avant la création des branches : interfaces, classes concrètes en squelette (`NotImplementedError`), exceptions et messages des étapes 5b, 6, 7a et 7b ; squelettes de tests (outils communs et tests de contrat des interfaces, verts sur `main`)

## Étape 6 — Initialisation de la population (`src/ga/initialization.py`) **(C→P)** — Mély, branche `etape-6-initialisation`
- [x] Scaffold **(C)**, dans le scaffold commun : interface `PopulationInitializer[G]` (`initialize(size, rng) -> individus non évalués`), squelette de `RandomBlockInitializer`, exceptions et messages
- [x] `RandomBlockInitializer(instance, encoding, local_solver = None)` **(P)** : génomes `BlockGenome` structurellement faisables tirés au hasard (graine contrôlée) :
  - chaque durée de bloc `d_i ≥ 4` ; `22 ≤ Σd ≤ 30` ; le quart entier dans la plage utile ; les activités dans `1..activity_count` (conditions de D1)
- [x] Option **(P)** : passer chaque individu initial au `LocalSolver` (écrit contre l'interface, testé avec un faux solveur ; branché sur `MiniZincLocalSolver` après la fusion de 5b)
- [x] Tests **(P)** : taille, faisabilité de tous les individus (`FeasibilityChecker`), reproductibilité avec la même graine, diversité (deux graines différentes ⇒ populations différentes), taille invalide, option `LocalSolver` (faux solveur appelé une fois par individu)
- [x] Tests d'intégration avec `MiniZincLocalSolver` + CP-SAT **(C)** — Pascal, branche `etape-6-integration-cpsat` : ré-encodage sans perte de l'horaire rendu, faisabilité structurelle, jamais pire qu'une entrée faisable, entrée gardée sans solution, reproductibilité (bench_1, bench_5)

## Étape 7 — Opérateurs génétiques
- [x] Trancher D3 : pas de normalisation au départ ; tri lexicographique et alignement en variantes

### 7a — Sélection et registre (`src/ga/selection.py`, `src/ga/registry.py`) **(C→P)** — Tristan, branche `etape-7a-selection`
- [ ] Scaffold **(C)**, dans le scaffold commun : interfaces `ParentSelector[G]` et `MutableSelector[G]` (tirage par lot, D7), vérification commune de la population (vide, individus non évalués), squelettes de `TournamentSelector`, `UniformMutableSelector` et `OperatorRegistry`, exceptions et messages (dont `IncompatibleOperatorError`)
- [ ] `TournamentSelector(size)` **(P)** : `SelectParent`, tournoi sur `cost.total`
- [ ] `UniformMutableSelector` **(P)** : `SelectMutable`, tirage uniforme
- [ ] `OperatorRegistry` **(P)** : enregistrement et création par nom, nom en double ou inconnu ⇒ exception ; vérification de compatibilité opérateur / encodage (`IncompatibleOperatorError`)
- [ ] Tests **(P)** : individus construits à la main avec des coûts choisis ; le meilleur gagne un tournoi qui contient tout le monde ; tournoi de taille 1 = tirage uniforme ; population vide ou non évaluée ⇒ exception ; reproductibilité avec la même graine ; entrées jamais modifiées

### 7b — Opérateurs de variation pour `BlockEncoding` (`src/ga/operators.py`) **(C→P)** — Xavier, branche `etape-7b-variation`
- [ ] Scaffold **(C)**, dans le scaffold commun : interfaces `VariationOperator[G]` (encodage compatible), `Crossover[G]` (`recombine(parents, rng) -> enfants`) et `Mutation[G]` (`mutate(genome, rng) -> génome`), squelettes des opérateurs concrets, exceptions et messages
- [ ] `Recombine` **(P)** : `UniformGeneCrossover`, échange de gènes entiers entre deux parents (préserve la faisabilité de chaque quart)
- [ ] `Mute` **(P)** : `ShiftStartMutation` (décaler un quart), `BlockBoundaryMutation` (déplacer une frontière entre deux blocs voisins, `Σd` conservée), `ActivityMutation` (changer l'activité d'un bloc)
- [ ] Tests **(P)** : faisabilité préservée (`FeasibilityChecker`), entrées jamais modifiées, reproductibilité, cas limites (deux parents identiques, gènes en bordure de fenêtre, blocs à la durée minimale)

## Étape 8 — Gestion de la population (`src/ga/population.py`) **(P)**
- [ ] Trancher D4
- [ ] Scaffold des interfaces `SurvivorSelector`, `ConvergenceCriterion`, `RestartPolicy` **(C→P)**
- [ ] `SelectPop` (remplacement), détection de convergence, `Restart`
- [ ] Tests : taille conservée, meilleur individu jamais perdu (si élitiste), convergence détectée sur population homogène
- [ ] Variante rigide « peine de mort » (remarque de Pascal, 2026-11-07) : les individus infaisables (`not cost.is_feasible`) sont éliminés d'emblée, au lieu d'être pénalisés (étape 4). À brancher comme stratégie (filtre au remplacement ou `SurvivorSelector` dédié), sans toucher à l'évaluation. Cas limite à trancher : que faire si trop peu d'enfants sont faisables pour remplir la population ?

## Étape 8b — Observabilité (`src/observability/`) **(C→P)**
- [ ] Interfaces `MetricCollector` et `RecordSink`, catalogue des événements et schéma des enregistrements (`schema_version`, `event`) **(C)**
- [ ] Destinations `ConsoleSink`, `JsonlSink`, `CsvSink`, `MemorySink`, `NullSink` **(C)**
- [ ] Configuration du journal de diagnostic (`logging`) : console et/ou `run.log`, niveau choisi par l'expérience **(C)**
- [ ] Répertoire d'exécution `results/<expérience>/<run_id>/` avec `config.json` (graine, commit Git, versions) ; `results/` ajouté au `.gitignore` **(C)**
- [ ] Collecteurs de coût (statistiques + décomposition) et de diversité (génotypique insensible à la permutation, phénotypique, des coûts) **(P)**
- [ ] Collecteur de **taux de faisabilité** des enfants, par opérateur, avant et après le `LocalSolver` (s'appuie sur `CostBreakdown.is_feasible` et les compteurs de violations) **(P)**
- [ ] Collecteur de **charge cumulée du solveur** (D10), émis avec `local_search_done` **(P)**
- [ ] `MongoSink` si D9 est retenue **(C)**
- [ ] Tests : événements reçus dans l'ordre (`MemorySink`), fichiers JSONL/CSV relisibles, collecteurs sur des populations construites à la main, mesure sans effet sur le générateur aléatoire du moteur

## Étape 9 — Boucle mémétique `Memetic(NR, NM)` **(P)**
- [ ] `MemeticConfig` (dataclass) : stratégies choisies + paramètres scalaires (NR, NM, taille, graine)
- [ ] Interface `Executor` + `SequentialExecutor` ; le moteur passe par `executor.map` pour traiter chaque lot (D7)
- [ ] Dérivation des graines par tâche à partir de la graine maître (D7)
- [ ] Assemblage selon le pseudo-code de CLAUDE.md ; le moteur ne dépend que des interfaces ; critère `terminé(P)` via `TerminationCriterion`
- [ ] Émission des événements de D8 aux points prévus ; collecteurs et destinations choisis dans `MemeticConfig`
- [ ] Tests : terminaison, coût du meilleur monotone non croissant, exécution complète sur `bench_1`, moteur exercé avec des opérateurs factices, reproductibilité (même graine ⇒ même historique, avec ou sans collecteurs ; solveur limité en effort plutôt qu'en temps), entrées des opérateurs jamais modifiées

## Étape 10 — Driver et expériences (`src/drivers/`) **(C)**
- [ ] Point d'entrée CLI (instance, NR, NM, taille de population, graine, limite de temps)
- [ ] **Première expérience, avant la campagne** (remarque de Pascal, 2026-11-07) : vérifier que le croisement et la mutation ne produisent pas seulement des horaires infaisables ; sinon l'AG ne vaut pas mieux qu'une marche aléatoire. Mesures : taux de faisabilité par opérateur avant réparation, apport de la réparation. Témoins : marche aléatoire, et génome aléatoire + `LocalSolver` (pour isoler l'apport des opérateurs de celui du solveur)
- [ ] Comparer pénalité (étape 4) et peine de mort (étape 8) sur ces mêmes mesures
- [ ] Expériences décrites par fichier de configuration (encodage, opérateurs, paramètres), résolues via le registre
- [ ] Variantes à comparer (D1, D3) : `DirectEncoding`, `SortedBlockEncoding`, croisement avec alignement des employés
- [ ] **En fin de projet, si le besoin se fait sentir** (décision de Pascal, 2026-11-09) : parler directement à CP-SAT par l'API Python d'OR-Tools (`CpSatApiAdapter`), sans MiniZinc. Gains : pas d'aplatissement à chaque appel (environ 0,11 s sur bench_3, du même ordre que la résolution d'un sous-problème), démarrage à chaud (`AddHint`), `deterministic_time` consommé rapporté (D10). Coûts : réécrire `horaire.mzn` en `CpModel` (dont `total` par contraintes réifiées), avec une validation croisée contre le modèle MiniZinc ; dépendance `ortools` ; perte de l'indépendance du solveur (D2). Prérequis : une interface `SolverAdapter.solve` qui décrit le sous-problème (employés fixés, borne de coût) au lieu de recevoir des chaînes MiniZinc. À déclencher si les mesures montrent que l'aplatissement domine le temps du mémétique
- [ ] Campagne sur `bench_1` … `bench_5` : mémétique vs MiniZinc seul (coût, temps)
- [ ] Dans cette campagne, comparer aussi la charge cumulée du solveur (D10) : mémétique contre MiniZinc seul
- [ ] Export des résultats (CSV/JSON), accompagnés de la configuration complète utilisée (via les destinations de D8)
- [ ] Scripts ou notebooks d'analyse qui relisent `results/` (évolution du coût, de la diversité, comparaison d'opérateurs)

## Étape 11 — Documentation **(C)**
- [ ] README : construction Docker, lancement des tests, lancement des expériences
- [ ] DEVLOG à jour
