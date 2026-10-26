# TODO — Proof of concept : algorithme mémétique pour l'horaire

Légende :
- `[ ]` à faire · `[~]` en cours · `[x]` validé (tests verts)
- **(C)** Claude écrit · **(P)** Pascal écrit, Claude vérifie · **(C→P)** Claude scaffolde (signatures, docstrings, tests), Pascal implémente

Règle : une seule étape à la fois ; on ne passe à la suivante qu'une fois les tests verts (cas nominaux + cas limites).

---

## Décisions de conception à trancher (avant l'étape concernée)

- [ ] **D1 — Encodage du chromosome** (avant étape 3) : l'encodage est polymorphe (interface `Encoding[G]`, voir D5). À trancher : la forme exacte de l'interface et l'encodage implémenté en premier (proposition : direct, par employé : `debut, pause1, diner, pause2, fin, activites[4]`). Les autres (par paramètres, direct trié, …) viendront une fois la boucle complète fonctionnelle.
- [x] **D2 — Rôle de MiniZinc comme `SolveurLocal`** : recherche locale d'amélioration (on fixe une partie des gènes, le solveur ré-optimise le reste sous limite de temps). Solveur par défaut : CP-SAT. Les particularités de chaque solveur sont cachées derrière une classe d'indirection, pour pouvoir en changer (Gecode, Chuffed, HiGHS, …).
- [ ] **D3 — Symétrie entre employés** (avant étape 7) : les employés sont interchangeables ; un croisement « par employé » peut être destructeur. Normaliser (trier les employés) avant de croiser ?
- [x] **D5 — Architecture polymorphe du moteur génétique** : patron Stratégie, une interface abstraite par rôle du pseudo-code (`ParentSelector`, `Crossover[G]`, `MutableSelector`, `Mutation[G]`, `LocalSolver`, `SurvivorSelector`, `ConvergenceCriterion`, `RestartPolicy`, `TerminationCriterion`). Séparation génotype / phénotype : phénotype canonique unique `Horaire` (faisabilité, coût, grille, MiniZinc) ; génotype polymorphe via `Encoding[G]`. Les opérateurs de variation sont liés à un encodage ; la compatibilité est vérifiée à l'assemblage (`MemeticConfig`, exception `IncompatibleOperatorError`). Registre par nom pour décrire les expériences en configuration. `random.Random` injecté dans chaque opérateur (reproductibilité). Taux de mutation (scalaire) et type de mutation (implémentation) sont deux axes distincts.
- [x] **D6 — Responsabilité de `encode` / `decode`** : traduction pure, rien d'autre. `decode` peut rendre un `Horaire` infaisable ; la vérification de faisabilité et la réparation (`LocalSolver`) sont des responsabilités distinctes.
- [x] **D7 — Préparation au parallélisme** (aucun parallélisme dans le POC, mais l'architecture doit le permettre sans réécriture) :
  - boucles NR / NM traitées **par lot** : tous les parents sont tirés dans P, tous les enfants sont produits, puis ajoutés (pas de *steady-state*) ;
  - individus **immuables** (`frozen dataclass`) : les opérateurs retournent de nouveaux individus et ne modifient jamais leurs entrées ;
  - **RNG dérivé par tâche** (graine déterministe par tâche, ex. `SeedSequence.spawn`), jamais un RNG partagé entre tâches ;
  - interface **`Executor`** (`map(tâche, lot)`), avec pour seule implémentation `SequentialExecutor` ; une version par threads ou async viendra plus tard ;
  - à garder en tête : arbitrage entre appels parallèles et threads internes de CP-SAT ; une limite en temps rend le solveur non déterministe ; modèle en îles possible plus tard (`MigrationPolicy`).
- [ ] **D4 — Remplacement / convergence / restart** (avant étape 8) : élitisme (μ+λ) ? mesure de diversité ? quelle fraction conserver au restart ?

---

## Étape 0 — Infrastructure et environnement **(C)**
- [x] Localisation de l'exécutable MiniZinc : variable d'environnement `MINIZINC_PATH` en priorité, sinon repli sur `minizinc.Driver.find()`, qui trouve aussi `/Applications/MiniZincIDE.app` sans `PATH` (donc pas de constante de repli). Exécutable absent ou invalide ⇒ `MiniZincNotFoundError`
- [x] Installer `requirements.txt` dans `.venv` (minizinc 0.10.0, numpy 2.5.4, Python 3.13.3)
- [x] Squelette `tests/` (unittest, découverte via `python -m unittest discover`) + `tests/test_minizinc_env.py` (15 tests verts)
- [x] Test de fumée : MiniZinc + CP-SAT résolvent `horaire.mzn` sur `bench_1.json` depuis Python (`tests/test_smoke_minizinc.py`, optimum 94 prouvé en < 1 s)
- [ ] Dockerfile (Python 3.13 + MiniZinc + CP-SAT) : en second, le développement se fait d'abord en local dans PyCharm
- [x] Harmoniser la structure réelle avec CLAUDE.md (`horaire.mzn` vs `schedule_model.mzn`, noms des instances `bench_*.json`) : la documentation a été alignée sur les fichiers réels

## Étape 1 — Constantes du domaine **(C)**
- [ ] Classe(s) de constantes : 4 activités par quart, durées pause (1 période) / dîner (4 périodes), activité min. (4 périodes), durée de quart (27..35), décalages des fenêtres (`+4`, `-17`, `+9`, `-12`, …)
- [ ] Aucune valeur magique ailleurs dans le code ; tests vérifiant la cohérence avec `horaire.mzn`

## Étape 2 — Lecture des instances (`src/utils/io.py`) **(C)**
- [ ] Classe `Instance` (dataclass typée) : `NB_EMPLOYES`, `NB_ACTIVITES`, `NB_PERIODES`, `demande`, `surcout`, `souscout`
- [ ] Calcul de `MIN_PERIODES` / `MAX_PERIODES` et des fenêtres dérivées (mêmes formules que le modèle)
- [ ] Exceptions sur mesure (`InstanceError`, …) : fichier absent, champ manquant, dimensions incohérentes, valeurs négatives
- [ ] Tests : les 5 bench se chargent ; JSON malformés ; instance où aucun quart ne rentre (ex. trop peu de périodes)

## Étape 3a — Phénotype `Horaire` **(C→P)**
- [ ] Classes `Horaire` / `HoraireEmploye` (mêmes variables que `horaire.mzn`)
- [ ] Vérification de faisabilité structurelle (les contraintes de `horaire.mzn`), composant distinct de l'encodage **(P)**
- [ ] Conversion vers la grille « employé × période → activité ou 0 » (même sémantique que la 2ᵉ sortie du modèle)
- [ ] Tests : horaires valides, chaque contrainte violée isolément, bornes exactes des fenêtres

## Étape 3b — Génotype : `Encoding[G]` et `DirectEncoding` (`src/ga/chromosome.py`) **(C→P)**
- [ ] Trancher D1
- [ ] Interface `Encoding[G]` : `encode(Horaire) -> G`, `decode(G) -> Horaire` (traduction pure, D6)
- [ ] Implémentation `DirectEncoding` **(P)**
- [ ] Classe `Individu` : génome, phénotype décodé (cache), coût
- [ ] Tests : aller-retour `decode(encode(h)) == h`, décodage d'un génome produisant un horaire infaisable (aucune exception)

## Étape 4 — Évaluation (fonction de coût) **(P)**
- [ ] Calcul de `total[p, a]` puis du coût sur/sous-couverture, identique à `cout_total`
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
- [ ] Trancher D3
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

## Étape 9 — Boucle mémétique `Memetic(NR, NM)` **(P)**
- [ ] `MemeticConfig` (dataclass) : stratégies choisies + paramètres scalaires (NR, NM, taille, graine)
- [ ] Interface `Executor` + `SequentialExecutor` ; le moteur passe par `executor.map` pour traiter chaque lot (D7)
- [ ] Dérivation des graines par tâche à partir de la graine maître (D7)
- [ ] Assemblage selon le pseudo-code de CLAUDE.md ; le moteur ne dépend que des interfaces ; critère `terminé(P)` via `TerminationCriterion`
- [ ] Journalisation de l'historique (meilleur coût, coût moyen, diversité par génération)
- [ ] Tests : terminaison, coût du meilleur monotone non croissant, exécution complète sur `bench_1`, moteur exercé avec des opérateurs factices, reproductibilité (même graine ⇒ même historique, solveur limité en effort plutôt qu'en temps), entrées des opérateurs jamais modifiées

## Étape 10 — Driver et expériences (`src/drivers/`) **(C)**
- [ ] Point d'entrée CLI (instance, NR, NM, taille de population, graine, limite de temps)
- [ ] Expériences décrites par fichier de configuration (encodage, opérateurs, paramètres), résolues via le registre
- [ ] Campagne sur `bench_1` … `bench_5` : mémétique vs MiniZinc seul (coût, temps)
- [ ] Export des résultats (CSV/JSON), accompagnés de la configuration complète utilisée

## Étape 11 — Documentation **(C)**
- [ ] README : construction Docker, lancement des tests, lancement des expériences
- [ ] DEVLOG à jour
