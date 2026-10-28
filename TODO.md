# TODO — Proof of concept : algorithme mémétique pour l'horaire

Légende :
- `[ ]` à faire · `[~]` en cours · `[x]` validé (tests verts)
- **(C)** Claude écrit · **(P)** Pascal écrit, Claude vérifie · **(C→P)** Claude scaffolde (signatures, docstrings, tests), Pascal implémente

Règle : une seule étape à la fois ; on ne passe à la suivante qu'une fois les tests verts (cas nominaux + cas limites).

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
- [ ] Classes `Horaire` / `HoraireEmploye` (mêmes variables que `horaire.mzn`)
- [ ] Vérification de faisabilité structurelle (les contraintes de `horaire.mzn`), composant distinct de l'encodage **(P)**
- [ ] Conversion vers la grille « employé × période → activité ou 0 » (même sémantique que la 2ᵉ sortie du modèle)
- [ ] Tests : horaires valides, chaque contrainte violée isolément, bornes exactes des fenêtres

## Étape 3b — Génotype : `Encoding[G]` et `BlockEncoding` (`src/ga/chromosome.py`) **(C→P)**
- [x] Trancher D1 : encodage par blocs, un gène par employé
- [ ] Interface `Encoding[G]` : `encode(Horaire) -> G`, `decode(G) -> Horaire` (traduction pure, D6)
- [ ] Implémentation `BlockEncoding` **(P)**
- [ ] Classe `Individu` : génome, phénotype décodé (cache), coût
- [ ] Tests : aller-retour `decode(encode(h)) == h`, décodage d'un génome produisant un horaire infaisable, par exemple Σd hors de 22..30 ou quart débordant la plage utile (aucune exception)

## Étape 4 — Évaluation (fonction de coût) **(P)**
- [ ] Calcul de `total[p, a]` puis du coût sur/sous-couverture, identique à `cout_total`
- [ ] L'évaluation retourne une décomposition `CostBreakdown` (sous-couverture, sur-couverture, violations de « au moins 1 », cellules à pénalité 1 000 000, total), pas seulement un scalaire (D8)
- [ ] Traitement de la contrainte « au moins 1 employé si demande > 0 » (infaisable ou pénalité ?)
- [ ] Tests : cas calculés à la main + **validation croisée** avec le coût renvoyé par MiniZinc sur des solutions réelles

## Étape 5 — Interface MiniZinc (`src/memetic/local_search.py`) **(C→P)**
- [ ] Classe d'indirection `SolverAdapter` (interface) + `CpSatAdapter` : identifiant du solveur, options (threads, graine, limite de temps), traduction des statuts
- [ ] Résolution complète (référence / borne pour comparer le mémétique)
- [ ] `SolveurLocal(chromosome)` : fixer une partie des variables, résoudre sous limite de temps, reconstruire un `Chromosome`
- [ ] Gestion des erreurs MiniZinc (timeout, UNSAT, solveur absent) via exceptions sur mesure
- [ ] Tests : le résultat est faisable, son coût ≤ coût d'entrée, comportement en timeout / UNSAT

## Étape 6 — Initialisation de la population **(P)**
- [ ] Génération aléatoire d'individus structurellement faisables (graine contrôlée)
- [ ] Option : passer chaque individu initial au `SolveurLocal`
- [ ] Tests : taille, faisabilité de tous les individus, reproductibilité avec la même graine

## Étape 7 — Opérateurs génétiques (`src/ga/operators.py`) **(P)**
- [x] Trancher D3 : pas de normalisation au départ ; tri lexicographique et alignement en variantes
- [ ] Scaffold des interfaces `ParentSelector`, `Crossover[G]`, `MutableSelector`, `Mutation[G]` **(C→P)**
- [ ] `SelectParent` (ex. tournoi)
- [ ] `Recombine` (croisement préservant la faisabilité, ou suivi d'une réparation)
- [ ] `SelectMutable` et `Mute` (décaler un quart, une pause, changer une activité, …)
- [ ] Registre par nom et vérification de compatibilité opérateur / encodage (`IncompatibleOperatorError`)
- [ ] Tests : faisabilité préservée, cas limites (population de 2, individus identiques, gènes en bordure de fenêtre)

## Étape 8 — Gestion de la population (`src/ga/population.py`) **(P)**
- [ ] Trancher D4
- [ ] Scaffold des interfaces `SurvivorSelector`, `ConvergenceCriterion`, `RestartPolicy` **(C→P)**
- [ ] `SelectPop` (remplacement), détection de convergence, `Restart`
- [ ] Tests : taille conservée, meilleur individu jamais perdu (si élitiste), convergence détectée sur population homogène

## Étape 8b — Observabilité (`src/observability/`) **(C→P)**
- [ ] Interfaces `MetricCollector` et `RecordSink`, catalogue des événements et schéma des enregistrements (`schema_version`, `event`) **(C)**
- [ ] Destinations `ConsoleSink`, `JsonlSink`, `CsvSink`, `MemorySink`, `NullSink` **(C)**
- [ ] Configuration du journal de diagnostic (`logging`) : console et/ou `run.log`, niveau choisi par l'expérience **(C)**
- [ ] Répertoire d'exécution `results/<expérience>/<run_id>/` avec `config.json` (graine, commit Git, versions) ; `results/` ajouté au `.gitignore` **(C)**
- [ ] Collecteurs de coût (statistiques + décomposition) et de diversité (génotypique insensible à la permutation, phénotypique, des coûts) **(P)**
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
- [ ] Expériences décrites par fichier de configuration (encodage, opérateurs, paramètres), résolues via le registre
- [ ] Variantes à comparer (D1, D3) : `DirectEncoding`, `SortedBlockEncoding`, croisement avec alignement des employés
- [ ] Campagne sur `bench_1` … `bench_5` : mémétique vs MiniZinc seul (coût, temps)
- [ ] Export des résultats (CSV/JSON), accompagnés de la configuration complète utilisée (via les destinations de D8)
- [ ] Scripts ou notebooks d'analyse qui relisent `results/` (évolution du coût, de la diversité, comparaison d'opérateurs)

## Étape 11 — Documentation **(C)**
- [ ] README : construction Docker, lancement des tests, lancement des expériences
- [ ] DEVLOG à jour
