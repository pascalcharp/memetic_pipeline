# DEVLOG

## 2026-10-23 — Planification initiale

**Fait**
- Lecture de CLAUDE.md, `docs/ALGO.md`, `src/model/horaire.mzn` et des instances `data/bench_1..5.json`.
- Rédaction du `TODO.md` : 12 étapes (0 à 11), du conteneur jusqu'aux expériences, avec répartition des rôles (Claude / Pascal).

**Constats**
- Instances : de 3 employés × 1 activité × 32 périodes (`bench_1`) à 8 employés × 5 activités × 48 périodes (`bench_5`).
- MiniZinc 2.10.0 est installé localement (`/Applications/MiniZincIDE.app/Contents/Resources/minizinc`), mais il n'est pas dans le `PATH`, ni dans celui de PyCharm. CP-SAT 9.15 est disponible et c'est le solveur par défaut. Pas encore de Dockerfile.

**Décision D2** : `SolveurLocal` = recherche locale d'amélioration avec CP-SAT par défaut, derrière une classe d'indirection pour pouvoir changer de solveur.
- Écarts avec la structure de CLAUDE.md : modèle nommé `horaire.mzn` (et non `schedule_model.mzn`), instances `bench_*.json`.
- `requirements.txt` existe, mais les paquets ne sont pas installés dans `.venv`.

**Décisions en suspens** : D1, D3, D4 (voir `TODO.md`).

## 2026-10-25 — Architecture polymorphe du moteur génétique

**Besoin** : comparer en expérience des variantes d'opérateurs (crossover A vs B, taux et type de mutation, …) sans toucher au moteur. Même principe que pour les solveurs (D2).

**Décision D5** : patron Stratégie.
- Une interface abstraite par rôle du pseudo-code. Le moteur `Memetic` ne dépend que de ces interfaces.
- `MemeticConfig` assemble les stratégies et les paramètres scalaires. Un registre par nom permet de décrire une expérience dans un fichier de configuration.
- Un `random.Random` est injecté dans chaque opérateur pour la reproductibilité.
- Le taux de mutation (paramètre) et le type de mutation (implémentation) sont deux axes distincts.

**Génotype / phénotype** : l'encodage dépend du type de crossover, donc il est polymorphe lui aussi.
- Le phénotype canonique `Horaire` est unique. Faisabilité, coût, grille et MiniZinc l'utilisent et sont écrits une seule fois.
- Le génotype passe par `Encoding[G]`. `Crossover[G]` et `Mutation[G]` sont liés à un encodage, alors que les sélecteurs, qui ne regardent que le coût, n'en dépendent pas.
- La compatibilité opérateur / encodage est vérifiée à l'assemblage (`IncompatibleOperatorError`).
- Garde-fou POC : un seul encodage (direct) tant que la boucle complète ne tourne pas.

**Décision D6** : `encode` / `decode` sont une traduction pure, sans aucune autre responsabilité. Leur confier la validation ou la réparation violerait la responsabilité unique. `decode` peut donc rendre un `Horaire` infaisable. La faisabilité est vérifiée par un composant distinct et la réparation relève du `LocalSolver`.

**D1 reformulée** : il reste à trancher la forme de l'interface `Encoding[G]` et le premier encodage implémenté.

**Impact sur le TODO** : l'étape 3 est scindée en 3a (phénotype) et 3b (génotype). Des scaffolds d'interfaces sont ajoutés aux étapes 7 et 8. Les étapes 9 et 10 intègrent `MemeticConfig` et les expériences pilotées par configuration.

## 2026-10-25 — Préparation au parallélisme (D7)

**Besoin** : le parallélisme est une force des AG, mais il est exclu du POC parce que le débogage est trop coûteux. L'architecture doit cependant permettre de l'ajouter plus tard sans réécrire le moteur.

**Analyse** : presque tout le temps de calcul passera dans le `LocalSolver` (MiniZinc). MiniZinc tourne dans un sous-processus, donc des threads ou de l'async suffiront plus tard, sans le multiprocessing et ses problèmes de sérialisation.

**Décision D7** : quatre règles à respecter dès la version séquentielle.
1. **Boucles par lot.** Dans le pseudo-code, `P = P + Enfants` s'exécute à chaque itération (*steady-state*), ce qui est séquentiel par nature. On tire donc tous les parents dans P, on produit tous les enfants, puis on les ajoute. Ce choix modifie le comportement de l'algorithme : il est donc fixé avant d'avoir des résultats.
2. **Individus immuables** (`frozen dataclass`). `Mute(i)` retourne un nouvel individu. Sans état partagé modifiable, la plupart des bogues de concurrence disparaissent par construction.
3. **RNG dérivé par tâche.** Une graine déterministe par tâche, dérivée de la graine maître, rend le résultat indépendant de l'ordre d'exécution : le séquentiel et le futur parallèle donneront les mêmes résultats, ce qui fournira un test de non-régression.
4. **Interface `Executor`** (patron Stratégie). Le moteur appelle `executor.map(tâche, lot)`. Pour l'instant, la seule implémentation est `SequentialExecutor`.

**À garder en tête** :
- N appels parallèles à CP-SAT, chacun multi-thread, peuvent saturer la machine : cet arbitrage deviendra un paramètre d'expérience.
- Une limite en temps rend le solveur non déterministe même en séquentiel : pour les tests reproductibles, il faudra limiter l'effort (nœuds, conflits).
- Le modèle en îles reste possible plus tard (plusieurs moteurs + `MigrationPolicy`).

**Impact sur le TODO** : D7 est ajoutée. L'étape 9 intègre `Executor`, la dérivation des graines et de nouveaux tests (reproductibilité, entrées des opérateurs jamais modifiées).
