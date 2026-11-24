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
  - recherches locales hors du moteur (initialisation, restart) : publiées par le moteur à partir de `InitializationResult.searches` et `RestartResult.searches` (2026-11-22, 9-intégration) ;
  - une exécution = `results/<expérience>/<run_id>/` (`config.json` avec graine, commit Git et versions, `events.jsonl`, `generations.csv`, `run.log`), ignoré par Git ;
  - principes : enregistrer assez de données brutes pour recalculer plus tard ; `schema_version` et `event` dans chaque enregistrement ; un collecteur ne consomme jamais le générateur aléatoire du moteur ; événements émis par le thread principal après chaque lot (D7) ; temps marqués non déterministes ; bibliothèque standard seulement.
- [x] **D4 — Remplacement / convergence / restart** (tranchée le 2026-11-16, Pascal et Claude, précisée le 2026-11-21 à la révision de l'étape 8) :
  - **remplacement (`SelectPop`)** : (μ+λ) sans doublons. Parents et nouveaux individus sont triés par `cost.total` croissant (tri stable) ; on garde les μ meilleurs en ne retenant qu'un exemplaire de chaque génome identique. Élitiste : le meilleur individu n'est jamais perdu. L'élimination des doublons empêche les copies produites par le `LocalSolver` (plusieurs individus réparés vers la même solution) d'envahir la population. S'il y a moins de μ génomes distincts, on complète avec les doublons écartés, dans l'ordre des coûts, pour garder la taille μ. Limite connue : deux génomes égaux à une permutation des employés près (D3) ne sont pas des doublons ;
  - **convergence** : stagnation du meilleur. La population a convergé quand le coût du meilleur individu n'a pas baissé depuis G générations (G configurable). La diversité (8b) est mesurée pour l'observation, pas pour décider ;
  - **restart** : élite k + réinitialisation. On garde jusqu'à k meilleurs individus distincts (k petit, 1 par défaut) et on régénère le reste avec le `PopulationInitializer` de l'étape 6 (avec son option `LocalSolver`), puis on évalue. Pas de complément par des doublons pour l'élite : s'il y a moins de k génomes distincts, on en garde moins et on en régénère davantage, et la taille de la population est conservée. Le critère de convergence repart de zéro ;
  - **variante « peine de mort »** : au remplacement, les individus faisables (`cost.is_feasible`) passent d'abord, sans doublons ; s'il en reste moins de μ, on complète avec les meilleurs infaisables selon `cost.total`. S'il manque encore des individus, même complément par les doublons écartés (faisables d'abord) : les deux sélecteurs suivent la même règle de complétion. La population garde sa taille, et la variante se dégrade doucement vers la pénalité quand les faisables manquent ;
  - valeurs par défaut proposées (classe de constantes de `src/ga/population.py`) : G = 10 générations, k = 1.
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
- [x] **D12 — Couverture « au moins 1 » dans le `LocalSolver` : contrainte dure ou pénalité ?** (relevée par Pascal le 2026-11-13 ; à trancher en équipe avant l'étape 8, touche `src/model/` et `src/memetic/`, modules partagés) :
  - constat : l'évaluation (étape 4) pénalise chaque cellule vide où la demande est positive, mais le sous-problème du `LocalSolver` résout `horaire.mzn`, où c'est une contrainte dure (ligne 154). Une entrée qui viole « au moins 1 » avec peu d'employés libérés donne un sous-problème insatisfiable et revient inchangée, au lieu d'être améliorée (mesures du 2026-11-13 dans DEVLOG.md : 6 cas sur 6 sur bench_3 et bench_5 avec 2 employés libérés) ;
  - piste : une variante du modèle où la contrainte devient un terme `poids × cellules vides` dans l'objectif, avec le poids de `PenaltyWeights.coverage_violation` (même fonction de coût que `CostEvaluator.total`) ; le `LocalSolver` choisit le modèle (Stratégie, D5) ; la borne de coût porte alors sur le coût pénalisé, donc s'applique aussi aux entrées infaisables ;
  - questions : un seul modèle paramétré ou deux fichiers ? garder la variante dure pour comparer (lien avec la variante « peine de mort », étape 8) ? effet sur la propagation et le temps de CP-SAT ?
  - **décision (2026-11-20) : deux fichiers.** `horaire_assoupli.mzn`, où « au moins 1 » est une pénalité, est le modèle du pipeline : il minimise la même fonction de coût que `CostEvaluator.total`. `horaire.mzn`, le modèle original fourni (couverture dure), est gardé tel quel comme référence (résolution complète, comparaisons, variante « peine de mort »). Le `SolverAdapter` reçoit le modèle à résoudre (Stratégie, D5) ; le poids de la pénalité vient de `PenaltyWeights.coverage_violation`, jamais écrit dans le modèle.
- [ ] **D13 — Redondance entre `horaire.mzn` et le pipeline Python** (relevée par Pascal le 2026-11-13 ; à discuter en équipe, touche `src/model/` et `src/memetic/solver.py`, modules partagés) :
  - constat : les règles du problème existent deux fois. Les **constantes** (durées et écarts du quart : 27, 35, 4, 5, 8…) sont écrites en dur dans `horaire.mzn` et dans `shift_rules.py`. La **logique** (contraintes structurelles, fonction de coût) est dans le modèle et dans `feasibility.py` / `evaluation.py`. Les deux copies peuvent diverger : c'est arrivé avec D12 (couverture pénalisée à l'étape 4, mais encore dure dans le modèle, découvert seulement aux tests d'intégration de l'étape 6) ;
  - limite : la redondance de la logique ne peut pas disparaître entièrement. Évaluer chaque individu avec MiniZinc (toutes les variables fixées) coûte au moins quelques dixièmes de seconde par appel, juste pour la mise à plat, ce qui est beaucoup trop lent pour la boucle génétique. Générer le modèle et le Python à partir d'un langage commun serait trop lourd pour un proof of concept ;
  - piste 1, constantes : une seule source, Python. Les littéraux du modèle deviennent des paramètres (`DUREE_MIN_QUART`, `ECART_DINER`…), remplis par le `SolverAdapter` à partir de `ShiftStructure` / `ShiftGaps`, comme le poids de la pénalité dans 5c ;
  - piste 2, logique : le modèle est la spécification de référence et le Python une implémentation rapide, vérifiée par une **suite de conformance** en CI. Elle génère beaucoup d'horaires (au hasard, cas limites, chaque règle violée isolément) et compare verdict et coût Python / MiniZinc **terme par terme** (sous-couverture, surcouverture, violations ; le modèle doit exposer ces termes dans sa sortie JSON). Elle généralise les sondes ponctuelles de `test_shift_rules.py`, `test_horaire.py` et `test_feasibility.py` ;
  - questions : générer les horaires au hasard à la main ou avec une bibliothèque de tests par propriétés (`hypothesis`) ? combien de cas, pour garder une CI rapide ? quand le faire : après 5c, avant l'étape 8 ?
- [ ] **D14 — Exceptions qui construisent leur propre message** (relevée à la revue de la PR #4, 2026-11-13 ; à trancher en équipe, touche la convention de CLAUDE.md « Gestion des erreurs ») :
  - constat : à l'étape 7a, les trois exceptions de `src/ga/registry.py` (`DuplicateOperatorError`, `UnknownOperatorError`, `IncompatibleOperatorError`) ont reçu un `__init__` qui prend les données brutes, les garde en attributs (`operator_name`, `known`…) et formate lui-même le gabarit de `RegistryMessages`. Partout ailleurs, dans `selection.py` par exemple, c'est le code qui lève l'exception qui formate le gabarit et passe une chaîne. Ce changement d'interface a été fait sans concertation, dans le même commit que l'implémentation ;
  - pour : les attributs structurés permettent aux tests (et au code appelant) de vérifier les valeurs sans analyser le message ; le formatage est écrit une seule fois ;
  - contre : deux conventions coexistent dans le projet, alors que CLAUDE.md demande une gestion cohérente des exceptions ;
  - questions : adopter cette forme comme convention (et l'inscrire dans CLAUDE.md, puis l'appliquer progressivement aux autres modules) ou revenir à la forme commune dans `registry.py` ? En attendant, la version de l'étape 7a reste en place.

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
- [ ] ***Optionnel*** — **`TimeWindowNeighborhood`, voisinage par fenêtre temporelle** **(C→P)** (idée de Pascal, 2026-11-21 ; responsable à désigner ; après le prototype) : alternative à `RandomEmployeesNeighborhood`, sans changer d'interface. Elle choisit une fenêtre `[t, t + w)` de largeur fixe et libère les employés dont le quart la chevauche, plus tous les employés structurellement infaisables (règle de D11).
  - Pourquoi une fenêtre plutôt que l'idée de départ, « tout fixer avant la première cellule fautive et libérer tout ce qui suit » ? Avec D12, seules les règles d'un quart sont dures. Elles portent sur un employé, pas sur une période ; une période mal couverte n'est qu'un coût. Libérer tout un suffixe peut équivaloir à une résolution complète (contraire à l'objectif de réduire la charge du solveur), donne une taille de sous-problème qui varie d'un individu à l'autre, et favorise toujours les premières périodes. Fixer seulement les variables avant `t` couperait aussi en deux les blocs qui chevauchent `t`, ce qui obligerait à changer `Neighborhood.select` et `fixing_constraints`
  - Choix de `t` (stratégies à comparer) : période la plus coûteuse ; tirage pondéré par le coût de chaque période ; première période coûteuse (l'idée de départ). Le coût par période n'est pas exposé pour l'instant : il se déduit de `CostEvaluator.coverage_totals` (période × activité) et de la demande. Il faudra l'ajouter à `evaluation.py`, un module partagé
  - Taille maîtrisée : un plafond sur le nombre d'employés libérés (tirage au hasard parmi ceux qui chevauchent la fenêtre). `w` et ce plafond sont des constantes de `NeighborhoodDefaults`
  - Tests : seuls les employés qui chevauchent la fenêtre et les infaisables sont libérés ; plafond respecté ; fenêtre au début et à la fin de la journée ; fenêtre qu'aucun quart ne touche ; horaire de coût nul ; reproductibilité ; entrée jamais modifiée
  - À mesurer à l'étape 10, contre `RandomEmployeesNeighborhood` à taille de voisinage égale : baisse du coût par appel et effort du solveur par appel (D10)

### 5c — Couverture « au moins 1 » en pénalité : modèle assoupli `horaire_assoupli.mzn` (D12) **(P)** — Pascal, branche `etape-5c-couverture-souple`
Constat (tests d'intégration de l'étape 6, 2026-11-13) : `horaire.mzn` impose « au moins 1 employé si demande > 0 » en contrainte dure (ligne 154), alors que `CostEvaluator` la pénalise (étape 4). Une entrée qui viole cette contrainte avec peu d'employés libérés donne un sous-problème insatisfiable : le `LocalSolver` la rend inchangée au lieu de l'améliorer. Objectif : que MiniZinc et le pipeline minimisent **la même fonction de coût**.

Décision D12 (2026-11-20) : deux fichiers. `horaire.mzn` reste **inchangé** (référence) ; le nouveau `horaire_assoupli.mzn` est le modèle du pipeline. Modules partagés touchés : `src/config.py`, `src/model/` (nouveau fichier seulement), `src/memetic/solver.py`, `src/memetic/local_search.py`.

- [x] **Trancher D12** : deux fichiers, la variante dure gardée comme référence, le poids passé par Python (voir D12).
- [x] **Scaffold et tests** **(C)** (2026-11-20 ; 12 tests rouges, validés contre une implémentation de référence jetable) :
  - `ProjectPaths` : `REFERENCE_MODEL_FILE` (`horaire.mzn`) et `RELAXED_MODEL_FILE` (`horaire_assoupli.mzn`), à la place de `MODEL_FILE` ;
  - `solver.py` : description d'un modèle (`ModelVariant` : fichier, nom de l'objectif, pénalité de couverture ou non) et les deux variantes (`ModelVariants.REFERENCE`, `ModelVariants.RELAXED`) ; noms des nouvelles variables (`violations_couverture`, `cout_penalise`, paramètre `POIDS_COUVERTURE`) ; le `SolverAdapter` reçoit la variante et les poids, `RELAXED` par défaut ;
  - tests rouges qui servent de cahier des charges (liste ci-dessous).
- [x] **Modèle** `horaire_assoupli.mzn` **(P)**, copie de `horaire.mzn` (écrit et validé le 2026-11-20) :
  - paramètre `int: POIDS_COUVERTURE`, fourni par Python ;
  - la contrainte « au moins 1 » devient un compteur `violations_couverture` (cellules de `RPER × RACT` où `demande > 0` et `total = 0`), sur les mêmes cellules que `CostEvaluator` (plage utile) ;
  - nouvel objectif `cout_penalise = cout_total + POIDS_COUVERTURE × violations_couverture`, et `solve minimize cout_penalise` ; `cout_total` reste défini, pour la décomposition du coût ;
  - `violations_couverture` et `cout_penalise` dans la sortie JSON ;
  - `violations_couverture`, `cout_total` et les six variables de décision annotés `::add_to_output` (sinon minizinc-python ne rend plus les variables de décision) ;
  - vérifier l'effet du poids de 1 000 000 sur la propagation et le temps de CP-SAT ; débordement : au plus 48 × 5 = 240 cellules, donc au plus 2,4 × 10⁸ de pénalité, sous 2³¹.
- [x] **`SolverAdapter`** (`solver.py`) **(P)** : résout le fichier de la variante ; passe `POIDS_COUVERTURE` seulement à une variante qui a la pénalité. Résolution complète (D10) : sur les bench actuels, l'optimum ne change pas, puisqu'ils respectent « au moins 1 » à l'optimum.
- [x] **`MiniZincLocalSolver`** (`local_search.py`) **(P)** :
  - variante assouplie : borne `cout_penalise ≤ CostEvaluator.total(entrée)`, posée dès que l'entrée n'a **aucune violation structurelle** (elle est alors une solution du sous-problème), même si elle viole « au moins 1 » ;
  - variante de référence : règle actuelle (borne sur `cout_total` seulement si l'entrée est faisable) ;
  - mettre à jour la docstring du module et la règle de D11 (« une entrée infaisable n'a pas de borne »).
- [x] **Tests** (tous verts et mesures faites le 2026-11-20) :
  - `horaire.mzn` inchangé (empreinte du fichier) ; les deux fichiers existent ;
  - validation croisée Python / MiniZinc : pour des horaires fixés à la main, dont certains qui violent « au moins 1 », `cout_penalise` du modèle assoupli = `CostEvaluator.total`, et `violations_couverture` = `coverage_violations` ;
  - instance construite pour que « au moins 1 » soit impossible à respecter ⇒ solution rendue par le modèle assoupli (plus d'UNSAT), avec le bon nombre de violations ; le modèle de référence donne UNSAT ;
  - optimum de `bench_1` inchangé (94) avec les deux modèles (`tests/test_smoke_minizinc.py`) ;
  - `SolverAdapter` : le poids n'est passé qu'au modèle assoupli (sans MiniZinc si possible) ;
  - `LocalSolver` : bornes des deux variantes, sans MiniZinc ; une entrée structurellement faisable qui viole « au moins 1 », avec 2 employés libérés ⇒ plus d'UNSAT, et `total` du résultat ≤ `total` de l'entrée ;
  - refaire les mesures du 2026-11-13 (bench_3 et bench_5, 2 employés libérés, 6 cas sur 6 en UNSAT) avec les deux modèles et consigner les résultats dans DEVLOG.md.
- [~] **Suivi** (documentation faite le 2026-11-20) :
  - `docs/PROBLEME.md` (« au moins 1 » est une pénalité dans le modèle du pipeline) ; `docs/PROJECT_STRUCT.md` et l'arbre de CLAUDE.md (nouveau fichier) ;
  - revoir l'amélioration possible de `SolverAdapter.solve` (5a, avertissement `model inconsistency detected`), qui devrait devenir rare ;
  - D13 : la redondance concerne maintenant deux modèles ; à reprendre après 5c.

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
- [x] Scaffold **(C)**, dans le scaffold commun : interfaces `ParentSelector[G]` et `MutableSelector[G]` (tirage par lot, D7), vérification commune de la population (vide, individus non évalués), squelettes de `TournamentSelector`, `UniformMutableSelector` et `OperatorRegistry`, exceptions et messages (dont `IncompatibleOperatorError`)
- [x] `TournamentSelector(size)` **(P)** : `SelectParent`, tournoi sur `cost.total`
- [x] `UniformMutableSelector` **(P)** : `SelectMutable`, tirage uniforme
- [x] `OperatorRegistry` **(P)** : enregistrement et création par nom, nom en double ou inconnu ⇒ exception ; vérification de compatibilité opérateur / encodage (`IncompatibleOperatorError`)
- [x] Tests **(P)** : individus construits à la main avec des coûts choisis ; le meilleur gagne un tournoi qui contient tout le monde ; tournoi de taille 1 = tirage uniforme ; population vide ou non évaluée ⇒ exception ; reproductibilité avec la même graine ; entrées jamais modifiées

### 7b — Opérateurs de variation pour `BlockEncoding` (`src/ga/operators.py`) **(C→P)** — Xavier, branche `etape-7b-variation`
- [x] Scaffold **(C)**, dans le scaffold commun : interfaces `VariationOperator[G]` (encodage compatible), `Crossover[G]` (`recombine(parents, rng) -> enfants`) et `Mutation[G]` (`mutate(genome, rng) -> génome`), squelettes des opérateurs concrets, exceptions et messages
- [x] `Recombine` **(P)** : `UniformGeneCrossover`, échange de gènes entiers entre deux parents (préserve la faisabilité de chaque quart)
- [x] `Mute` **(P)** : `ShiftStartMutation` (décaler un quart), `BlockBoundaryMutation` (déplacer une frontière entre deux blocs voisins, `Σd` conservée), `ActivityMutation` (changer l'activité d'un bloc)
- [x] Tests **(P)** : faisabilité préservée (`FeasibilityChecker`), entrées jamais modifiées, reproductibilité, cas limites (deux parents identiques, gènes en bordure de fenêtre, blocs à la durée minimale) — validés le 2026-11-16 après la revue de la PR #7 (Pascal), 41 tests, suite complète verte (326 tests)
- [ ] Amélioration possible de `BlockBoundaryMutation` (suggestion de Xavier, notée en commentaire dans le code, reportée ici le 2026-11-16) : calculer l'amplitude du transfert à partir des contraintes du quart, au lieu de la tirer dans un intervalle fixe (`OperatorDefaults.MIN_BOUNDARY_TRANSFER..MAX_BOUNDARY_TRANSFER`, soit 1..3). Le point d'entrée existe déjà : `BlockBoundaryMutation.get_transfer_bounds(genome)`, qui rend pour l'instant ces bornes fixes :
  - le bloc qui cède peut donner au plus `durée − ShiftStructure.MIN_ACTIVITY_DURATION` périodes ; tirer le transfert dans `1..marge` garantit des durées valides et supprime le cas « aucun gène ne peut céder » (bogue 3 de la revue de la PR #7) ;
  - Σd étant conservée, la borne de 6 à 8 heures rémunérées reste respectée d'elle-même. Un bloc ne peut donc pas dépasser `Σd − 3 × MIN_ACTIVITY_DURATION` périodes (au plus 30 − 12 = 18) ;
  - à étudier : tenir compte aussi des fenêtres des jalons (pause, dîner), pour que le déplacement de frontière garde le quart faisable ; plafonner le transfert (constante dans `OperatorDefaults`) pour garder une mutation locale ;
  - à mesurer à l'étape 10 : effet sur le taux de faisabilité des enfants de cet opérateur.

### 7c — *Optionnel* : croisement par interpolation linéaire (`src/ga/operators.py`) **(C→P)** — idée de Pascal, 2026-11-21 ; responsable à désigner
Croisement arithmétique : pour chaque employé, l'enfant reçoit `d·p1 + (1−d)·p2` sur les jalons, avec `d ∈ [0, 1]` tiré au hasard ; chaque activité vient de p1 avec probabilité `d`, sinon de p2.
- [ ] **(P)** `LinearInterpolationCrossover` : interpoler les **jalons** (`debut`, `pause1`, `diner`, `pause2`, `fin`) puis recalculer les durées, sans interpoler les durées une à une. Arrondir les jalons par une même fonction croissante `math.floor(x + 0.5)` : les règles d'un quart sont linéaires (écarts ≥ 4, amplitude entre `MIN_SHIFT_SPAN` et `MAX_SHIFT_SPAN`, fenêtres), donc deux parents faisables donnent un enfant faisable. Ne pas utiliser `round()`, qui arrondit au pair et casse cette garantie. Le même `d` vaut pour tous les jalons d'un employé ; un `d` par employé est permis, et c'est à mesurer
- [ ] **(P)** Appariement des employés avant l'interpolation (employés interchangeables, D3) : sinon un quart du matin interpolé avec un quart du soir donne un quart de midi que ni l'un ni l'autre des parents ne voulait. Variante simple : trier les quarts des deux parents par `debut`. Variante optimale : affectation hongroise sur la distance entre jalons (dépendance `scipy`, à discuter)
- [ ] **(P)** Variante : `d` biaisé par les coûts (le meilleur parent attire l'enfant). `d` reste aléatoire : on le tire de `Beta(κ·m, κ·(1−m))`, de moyenne `m = 1 / (1 + exp((c1 − c2) / T))`. Avec `T` relatif à l'écart des coûts dans la population, il n'y a ni division par zéro (deux coûts nuls) ni dépendance à l'échelle. Le biais ne remplace pas l'appariement : des coûts proches donnent `m ≈ 0,5`, l'interpolation la plus centrale
- [ ] **Prérequis de la variante biaisée, à trancher en équipe** (interface commune, règle 7) : `Crossover.recombine(parents, rng)` reçoit des génomes, pas des coûts. Soit l'interface reçoit les `Individual` ou leurs coûts, soit l'opérateur reçoit un paramètre facultatif `weights`. À décider avant de figer l'appel à `Recombine` dans la boucle (étape 9)
- [ ] Tests : parents faisables ⇒ enfant faisable (`FeasibilityChecker`, nombreux tirages) ; `d = 0` et `d = 1` redonnent un parent ; deux parents identiques ; jalons tombant sur un demi-entier ; appariement insensible à la permutation des employés ; entrées jamais modifiées ; reproductibilité
- [ ] À mesurer à l'étape 10, contre `UniformGeneCrossover` : perte de diversité (l'interpolation contracte la population vers le centre), taux de faisabilité des enfants, charge du solveur pour la réparation

## Étape 8 — Gestion de la population (`src/ga/population.py`) **(C→P)** — Tristan, branche `etape-8-population`
- [x] Trancher D4 (2026-11-16, voir la décision)
- [x] Scaffold **(C)**, dans le scaffold commun de la semaine du 16 novembre : interfaces `SurvivorSelector[G]`, `ConvergenceCriterion[G]`, `RestartPolicy[G]`, squelettes des classes concrètes, constantes, exceptions et messages — Tristan écrit les classes concrètes, branche `etape-8-population`
- [x] **(P)** `SelectPop` : `PlusSurvivorSelector` ((μ+λ) sans doublons) ; convergence : `StagnationCriterion(generations)` ; `Restart` : `EliteRestart(elite_count, initializer, evaluator)`
- [x] Tests : taille conservée, meilleur individu jamais perdu (si élitiste), convergence détectée sur population homogène
- [x] **(P)** `DeathPenaltySurvivorSelector` : variante rigide « peine de mort » (remarque de Pascal, 2026-11-07 ; cas limite tranché par D4 : compléter avec les meilleurs infaisables) : les individus infaisables (`not cost.is_feasible`) sont éliminés d'emblée, au lieu d'être pénalisés (étape 4). À brancher comme stratégie (filtre au remplacement ou `SurvivorSelector` dédié), sans toucher à l'évaluation. Cas limite à trancher : que faire si trop peu d'enfants sont faisables pour remplir la population ?

## Étape 8b — Observabilité (`src/observability/`) **(C→P)** — infrastructure par Claude dans le scaffold commun ; collecteurs par Mély, branche `etape-8b-observabilite`
- [x] Interfaces `MetricCollector` et `RecordSink`, catalogue des événements et schéma des enregistrements (`schema_version`, `event`) **(C)** ; diffusion `ObservationHub` (scaffold du 2026-11-16)
- [x] Destinations `ConsoleSink`, `JsonlSink`, `CsvSink`, `MemorySink`, `NullSink` **(C)**
- [x] Configuration du journal de diagnostic (`logging`) : console et/ou `run.log`, niveau choisi par l'expérience **(C)**
- [x] Répertoire d'exécution `results/<expérience>/<run_id>/` avec `config.json` (graine, commit Git, versions) ; `results/` ajouté au `.gitignore` **(C)**
- [x] Collecteurs de coût (statistiques + décomposition) et de diversité (génotypique insensible à la permutation, phénotypique, des coûts) **(P)**
- [x] Collecteur de **taux de faisabilité** des enfants, par opérateur, avant et après le `LocalSolver` (s'appuie sur `CostBreakdown.is_feasible` et les compteurs de violations) **(P)**
- [x] Collecteur de **charge cumulée du solveur** (D10), émis avec `local_search_done` **(P)**
- [ ] `MongoSink` si D9 est retenue **(C)** — proposition pour la rencontre : reportée, les fichiers de `results/` suffisent pour le POC
- [x] Tests : événements reçus dans l'ordre (`MemorySink`), fichiers JSONL/CSV relisibles, collecteurs sur des populations construites à la main, mesure sans effet sur le générateur aléatoire du moteur
- [x] Tests supplémentaires : populations vides ou non évaluées et remise à zéro des compteurs à RunStarted

## Étape 9 — Boucle mémétique `Memetic(NR, NM)` **(C→P)** — interfaces par Claude dans le scaffold commun ; moteur par Xavier, branche `etape-9-boucle`
- [x] `MemeticConfig` (dataclass) : stratégies choisies + paramètres scalaires (NR, NM, taille, graine)
- [x] Interface `Executor` + `SequentialExecutor` (écrits par Claude dans le scaffold) ; le moteur passe par `executor.map` pour traiter chaque lot (D7)
- [x] Dérivation des graines par tâche à partir de la graine maître (D7)
- [x] Assemblage selon le pseudo-code de CLAUDE.md ; le moteur ne dépend que des interfaces ; critère `terminé(P)` via `TerminationCriterion`
- [x] Émission des événements de D8 aux points prévus ; un `ObservationHub` (`MemeticConfig.dispatcher`, un hub vide par défaut) remplace les collecteurs et destinations ; le moteur le ferme à la fin de `run`
- [x] Tests (sans MiniZinc, avec des faux objets) : terminaison, coût du meilleur monotone non croissant, moteur exercé avec des opérateurs factices, reproductibilité (même graine ⇒ même historique, avec ou sans collecteurs ; solveur limité en effort plutôt qu'en temps), entrées des opérateurs jamais modifiées
  - validé le 2026-11-22 (PR #11 de Xavier, reprise et corrigée par Pascal et Claude) : lots NR et NM conformes à D7, graines par tâche, 46 tests dans `test_engine`, suite complète verte (506 tests)
- [ ] **9-intégration** (Pascal, après la fusion de 5c, 8, 8b et 9) : exécution complète sur `bench_1` avec les vrais composants (`MiniZincLocalSolver` + CP-SAT limité en effort déterministe), coût du meilleur monotone non croissant, reproductibilité avec et sans collecteurs, événements reçus dans l'ordre
  - [x] Scaffold et tests **(C)** (2026-11-22) : `src/memetic/assembly.py` (`AssemblyDefaults`, `AssemblySettings`, squelette de `build_block_memetic_config`) ; `tests/test_integration.py` : 11 tests de l'assemblage sans MiniZinc, 13 tests d'une exécution complète sur bench_1 (environ 30 s). Validés contre un assemblage de référence jetable : 24 tests verts, optimum 94 atteint, un restart
  - [x] **(P)** `build_block_memetic_config` : faire passer `tests.test_integration` — Pascal, 2026-11-22, 24 tests verts
  - [x] Tranché le 2026-11-22 (Pascal) : l'initialisation et le restart rendent explicitement ce qu'ils créent et les recherches locales faites pour cela. `PopulationInitializer.initialize` rend `InitializationResult(individuals, searches)` ; `RestartPolicy.restart` rend `RestartResult(elite, newcomers, searches)`. Le moteur émet un `LocalSearchDone` par recherche (origine `INITIALIZATION` ou `RESTART`, opérateur `None`), puis un `IndividualCreated` par nouvel individu : à la génération 0 avant `GenerationEnded(0)`, au restart entre `Converged(g)` et `Restarted(g)`. La charge du solveur (D10) est ainsi comptée partout

## Étape 10 — Driver et expériences (`experiments/`) **(C)**
Organisation (Pascal, 2026-11-23) : `src/` est le cœur ; `experiments/` contient ce qui sert à l'exploiter : scripts de pilotage (`experiments/drivers/`), scripts d'analyse (`experiments/analysis/`), configurations, résultats et journal.
Objectifs (Pascal, 2026-11-21) : montrer, sur au moins quelques instances, que le mémétique (1) bat une marche aléatoire, et (2) réduit la charge du solveur par rapport à CP-SAT seul, en monothread et sous limite déterministe.

### 10a — Script `run_experiment` **(C)** — Pascal et Claude, branche `etape-10a-run-experiment`
Conventions (Pascal, 2026-11-22) : configurations dans `experiments/config/`, résultats dans `experiments/results/<AAAA-MM-JJ>/` (un répertoire par jour, versionné dans Git), journal des expériences `experiments/EXPLOG.md`.
- [x] `experiments/drivers/run_experiment.py` (d'abord dans `src/drivers/`, déplacé le 2026-11-23) : trois chemins en paramètres (fichier de configuration JSON ; répertoire des résultats, par défaut celui du jour ; journal, par défaut `experiments/EXPLOG.md`). Lit la configuration (description lisible, instance, paramètres de `AssemblySettings`), construit le moteur avec `build_block_memetic_config`, l'exécute avec les quatre collecteurs de 8b, écrit un fichier JSON de résultats et ajoute une entrée à EXPLOG.md (description, chemins, coût obtenu, effort cumulé du solveur)
- [x] Configuration de base `experiments/config/integration_bench1.json` (les réglages de la 9-intégration) et première exécution consignée dans EXPLOG.md
- [x] Tests : lecture et validation de la configuration (champs manquants, clé inconnue, JSON invalide, instance introuvable), contenu du fichier de résultats, entrée d'EXPLOG.md, chemins par défaut, exécution complète courte sur bench_1
- [x] Point d'entrée CLI (instance, NR, NM, taille de population, graine, limite de temps) : couvert par 10a, la ligne de commande prend un fichier de configuration
  - validé le 2026-11-22 : 29 tests dans `test_run_experiment` et 5 de `working_tree_is_dirty`, suite complète verte ; `git_dirty` signale un résultat produit avec du code non commité ; première exécution de `integration_bench1` (copie de travail propre) consignée dans EXPLOG.md
- [ ] **Première expérience, avant la campagne** (remarque de Pascal, 2026-11-07) : vérifier que le croisement et la mutation ne produisent pas seulement des horaires infaisables ; sinon l'AG ne vaut pas mieux qu'une marche aléatoire. Mesures : taux de faisabilité par opérateur avant réparation, apport de la réparation. Témoins : marche aléatoire, et génome aléatoire + `LocalSolver` (pour isoler l'apport des opérateurs de celui du solveur)
- [ ] Comparer pénalité (étape 4) et peine de mort (étape 8) sur ces mêmes mesures
- [ ] Expériences décrites par fichier de configuration (encodage, opérateurs, paramètres), résolues via le registre
- [ ] Variantes à comparer (D1, D3) : `DirectEncoding`, `SortedBlockEncoding`, croisement avec alignement des employés
- [ ] **En fin de projet, si le besoin se fait sentir** (décision de Pascal, 2026-11-09) : parler directement à CP-SAT par l'API Python d'OR-Tools (`CpSatApiAdapter`), sans MiniZinc. Gains : pas d'aplatissement à chaque appel (environ 0,11 s sur bench_3, du même ordre que la résolution d'un sous-problème), démarrage à chaud (`AddHint`), `deterministic_time` consommé rapporté (D10). Coûts : réécrire `horaire.mzn` en `CpModel` (dont `total` par contraintes réifiées), avec une validation croisée contre le modèle MiniZinc ; dépendance `ortools` ; perte de l'indépendance du solveur (D2). Prérequis : une interface `SolverAdapter.solve` qui décrit le sous-problème (employés fixés, borne de coût) au lieu de recevoir des chaînes MiniZinc. À déclencher si les mesures montrent que l'aplatissement domine le temps du mémétique
- [ ] Campagne sur `bench_1` … `bench_5` : mémétique vs MiniZinc seul (coût, temps)
- [ ] Dans cette campagne, comparer aussi la charge cumulée du solveur (D10) : mémétique contre MiniZinc seul
- [ ] **Courbes « meilleur coût en fonction de l'effort cumulé du solveur »** (proposition retenue par Pascal, 2026-11-22) : pour chaque instance, une courbe pour CP-SAT seul et une pour le mémétique, avec la même métrique d'effort. Sur les deux axes, l'effort se mesure par le temps de résolution rapporté (`solve_time`) ou par les propagations, qui ne dépendent pas de la machine ; on ne compare **pas** le temps réel (aplatissement MiniZinc, démarrage du solveur), car le portrait changerait complètement avec un algorithme parallélisé et optimisé en C++.
  - CP-SAT seul : 1 thread, sous limite déterministe, modèle de référence (couverture dure : 3 fois moins d'effort que le modèle assoupli sur bench_1). On récupère ses solutions intermédiaires (coût et effort au moment de chacune), pour mesurer quand il **trouve** une solution d'un coût donné, pas seulement quand il prouve l'optimum.
  - Mémétique : on lit le meilleur coût et l'effort cumulé à chaque `GenerationEnded` (collecteurs de 8b). Plusieurs graines par instance.
  - Mesure de départ (2026-11-22, bench_1, optimum 94) : CP-SAT seul prouve l'optimum en environ 0,24 s de `solve_time` (environ 430 k propagations, 3 graines) ; `integration_bench1` atteint 94 en 0,20 s cumulées (238 k propagations, 35 appels), mais sans preuve. bench_1 est trop facile pour trancher, il faut regarder bench_3 à bench_5.
- [ ] Export des résultats (CSV/JSON), accompagnés de la configuration complète utilisée (via les destinations de D8)
- [ ] Scripts ou notebooks d'analyse qui relisent `results/` (évolution du coût, de la diversité, comparaison d'opérateurs)

### 10b — Distribution des coûts de la population, par génération **(C)** — proposée le 2026-11-23 (Pascal)
But : voir la convergence, l'effondrement de la diversité et l'effet des restarts, au-delà des résumés de `CostStatisticsCollector` (min, moyenne, médiane, max, écart-type). Les données passent déjà par le hub : `GenerationEnded` et `Restarted` portent la population ; il manque un collecteur qui garde les coûts individuels.
- [ ] **`CostDistributionCollector`** (`src/observability/collectors.py`) : à chaque `GenerationEnded`, un enregistrement `RecordNames.COST_DISTRIBUTION` avec `generation` et `totals` (liste triée des `cost.total`) ; à chaque `Restarted`, le même enregistrement, distingué par un champ `phase` (fin de génération ou restart). Noms de champs dans une classe de constantes ; population vide ou non évaluée : même exception que `CostStatisticsCollector`. Destinations : `JsonlSink`, `MemorySink` (pas `CsvSink`, dont les colonnes sont fixes)
- [ ] Optionnel : distribution des **candidats avant `SelectPop`** (enfants et mutants regroupés depuis les `IndividualCreated` de la génération), pour voir la sélection à l'œuvre (candidats contre survivants)
- [ ] Brancher le collecteur dans `run_experiment` (événements écrits avec les résultats)
- [ ] Tests : un enregistrement par génération et par restart, `totals` trié et de la taille de la population, champ `phase`, population vide ou non évaluée, aucun enregistrement pour les autres événements, passage par `JsonlSink`
- [ ] **Script de tracé** (`experiments/analysis/`) qui relit le `.jsonl` : avec de petites populations (6 individus), une heatmap (génération en x, tranches de coût en y, nombre d'individus en couleur) ou un nuage de points par génération avec la courbe du meilleur coût, plutôt qu'un histogramme par génération ; les histogrammes deviendront utiles avec de plus grandes populations (bench_3 à bench_5). Restarts marqués sur l'axe des générations
  - dépendance matplotlib dans un fichier à part (`requirements-analysis.txt`), pour ne pas alourdir l'image Docker des tests

## Étape 11 — Documentation **(C)**
- [ ] README : construction Docker, lancement des tests, lancement des expériences
- [ ] DEVLOG à jour
