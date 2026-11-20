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

## 2026-10-26 — Étape 0 : localisation de MiniZinc, dépendances, squelette de tests

**Fait**
- `minizinc.Driver.find()` trouve MiniZinc même avec un `PATH` vide (cas PyCharm), parce qu'il cherche aussi dans `/Applications/MiniZincIDE.app`. La constante de repli prévue au TODO est donc inutile : le TODO est aligné sur le code.
- Dépendances déjà présentes dans `.venv` : minizinc 0.10.0, numpy 2.5.4 (Python 3.13.3).
- Squelette `tests/` (unittest) et `tests/test_minizinc_env.py`, qui compte 15 tests : hiérarchie des exceptions, recherche par défaut (y compris avec un `PATH` vide), priorité de `MINIZINC_PATH`, valeurs invalides de la variable, solveur par défaut disponible, solveur inconnu.
- `.gitignore` : ajout de `__pycache__/`.

**Défaut trouvé et corrigé** (correction écrite par Pascal)
- Quand `MINIZINC_PATH` désignait un fichier existant mais inutilisable, `minizinc.Driver(...)` laissait remonter une exception brute au lieu de `MiniZincNotFoundError` :
  - fichier non exécutable : `PermissionError` ;
  - exécutable sans format reconnu : `OSError` (Exec format error) ;
  - exécutable étranger : `AssertionError` (assert interne de la bibliothèque), qui devient un `AttributeError` sous `python -O`.
- Une première correction (`except (PermissionError, AssertionError)` autour de toute la fonction) laissait encore passer les deux derniers cas et donnait un message trompeur aux erreurs de `find()`.
- Correction retenue : `try` limité au seul appel `minizinc.Driver(executable)`, `except Exception` converti en `MiniZincNotFoundError ... from error`. Une capture large est acceptable ici parce qu'elle est confinée à une ligne, à la frontière avec une bibliothèque externe dont les exceptions ne font pas partie du contrat.
- Leçon : énumérer les exceptions « devinées » d'une bibliothèque est fragile, puisque la liste dépend de son code interne et même des options de l'interpréteur.

**Convention ajoutée à CLAUDE.md** : les messages d'erreur sont des constantes.
- Chaque module qui définit des exceptions regroupe ses gabarits dans une classe `...Messages` placée à côté d'elles (ici `MiniZincEnvironmentMessages`).
- Les gabarits utilisent des espaces réservés nommés et `.format`, jamais de f-strings.
- Les tests vérifient que le message contient l'information utile au diagnostic (variable, chemin, identifiant de solveur), pas son texte exact.

## 2026-10-26 — Étape 0 : test de fumée MiniZinc

**Fait**
- `tests/test_smoke_minizinc.py` : la chaîne Python → MiniZinc 2.10 → CP-SAT 9.15 résout `horaire.mzn` sur `bench_1.json`.
- Vérifications : le fichier modèle existe, le statut est `OPTIMAL_SOLUTION`, le coût vaut 94 et chaque variable de décision a une valeur par employé.
- CP-SAT prouve l'optimum en environ 0,4 s. Toute la suite (19 tests) passe, même quand les `DeprecationWarning` sont traités comme des erreurs.

**Constats**
- L'optimum de `bench_1` (94) est enregistré comme valeur de référence. Il servira à la validation croisée de la fonction de coût (étape 4).
- `minizinc-python` 0.10 déprécie le paramètre `timeout` au profit de `time_limit`. Seul `time_limit` sera utilisé.
- On peut passer une instance `.json` directement par `Model.add_file`, sans conversion en `.dzn`.

## 2026-10-26 — Étape 0 : harmonisation de la documentation

**Fait** : l'arborescence de CLAUDE.md et de `docs/PROJECT_STRUCT.md` a été alignée sur le dépôt réel. On a corrigé la documentation au lieu de renommer les fichiers.
- Racine `memetic_pipeline/`, modèle `horaire.mzn`, instances `bench_1..5.json`.
- Ajout de `config.py`, `utils/minizinc_env.py`, `tests/`, `docs/`, `TODO.md` et `DEVLOG.md`.
- Les fichiers prévus mais pas encore créés sont marqués « (à venir) ».
- Les descriptions suivent les décisions D5 et D6 : `chromosome.py` contient le génotype (`Encoding[G]`). `local_search.py` fait la recherche locale et la réparation, mais plus le décodage, qui revient à l'encodage.

**À noter** : l'arborescence existe en deux exemplaires (CLAUDE.md et `docs/PROJECT_STRUCT.md`), qu'il faudra garder synchronisés.

## 2026-10-26 — Étape 0 : Dockerfile

**Fait**
- `Dockerfile` en deux étapes (multi-stage). MiniZinc 2.10.0 est copié depuis l'image officielle `minizinc/minizinc:2.10.0-noble` dans `python:3.13-slim-trixie` : le pilote, `fzn-cp-sat`, `fzn-gecode`, `fzn-chuffed`, `libhighs.so` et `share/minizinc`.
- `ENV MINIZINC_PATH=/usr/local/bin/minizinc`, lu par `minizinc_env`.
- `.dockerignore` : `.git`, `.idea`, `.venv`, caches Python.
- Commande par défaut : la suite de tests. Elle passe en arm64 (Mac) et en amd64 (émulation, la même architecture que GitHub Actions) : 18 tests OK, 1 ignoré. L'image fait environ 373 Mo.

**Choix** : on copie les binaires au lieu de compiler MiniZinc ou de partir de l'image MiniZinc.
- L'image MiniZinc est basée sur Ubuntu noble, qui fournit Python 3.12 et non 3.13.
- Les binaires ne dépendent que de libc, libstdc++, libgcc, libm et libz. Ils sont compatibles entre noble (glibc 2.39) et trixie (glibc 2.41).
- CP-SAT 9.15 est inclus dans l'image officielle, la même version qu'en local.

**Blocage et correctif** : `test_default_search_does_not_need_path` échouait dans le conteneur.
- Sans `PATH`, `Driver.find()` ne trouve MiniZinc que sous macOS (`/Applications/MiniZincIDE.app`). Sous Linux, l'échec est le comportement attendu.
- Le test est donc limité à macOS (`skipUnless(sys.platform == "darwin")`).

## 2026-10-26 — Étape 0 : intégration continue (GitHub Actions) — étape 0 terminée

**Fait**
- `.github/workflows/tests.yml` : à chaque push sur `main`, le workflow construit l'image Docker et lance la suite de tests dans le conteneur, avec les `DeprecationWarning` traités comme des erreurs. Limite de temps : 20 minutes.
- Premier run (commit `5dd6d78`) vert : https://github.com/pascalcharp/memetic_pipeline/actions/runs/40331236691. Toutes les étapes ont réussi et le job a duré environ 16 s.

**Choix** : les tests tournent dans l'image du projet plutôt que dans un Python installé par l'action. La CI exerce ainsi exactement l'environnement de développement (Python 3.13, MiniZinc 2.10, CP-SAT 9.15).

**Étape 0 terminée** : toutes ses tâches sont validées.

## 2026-10-28 — Étape 1 : constantes du domaine

**Fait** : `src/model/shift_rules.py`, placé à côté de `horaire.mzn` (lien logique avec le modèle). Il contient quatre classes.
- `ModelIndexing` : indexation à partir de 1 et valeur 0 (« aucune activité ») de la grille.
- `ShiftStructure` : constantes de base. Périodes par heure (4), 4 activités par quart, pause 1, dîner 4, activité minimale 4, heures rémunérées 6 à 8.
- `ShiftGaps` : écarts minimaux entre jalons consécutifs (4, 5, 8, 4), **dérivés** des durées.
- `WindowOffsets` : décalages des fenêtres (0/27, 4/17, 9/12, 17/4, 27/0), **dérivés** des écarts.

**Décision** : on garde le moins possible de constantes de base et on dérive tout le reste. Chaque nombre de `horaire.mzn` s'explique alors par une règle. Par exemple, `MAX_P1 = MAX_PERIODES - 17` parce que 17 = 5 + 8 + 4, soit les trois écarts qui suivent la première pause.

**Interprétation confirmée par Pascal** : l'écart `fin - debut` de 27 à 35 est lu comme 6 à 8 heures rémunérées (dîner non rémunéré, pauses rémunérées) : 6 × 4 + 4 - 1 = 27 et 8 × 4 + 4 - 1 = 35, où le - 1 vient des bornes incluses (commentaire de `horaire.mzn`).

**Tests** (`tests/test_shift_rules.py`, 12 tests, environ 7 s)
- Valeurs attendues lues dans `horaire.mzn`, et cohérence interne des règles.
- **Sondes MiniZinc** (`MiniZincModelProbe`), qui vérifient la cohérence avec le modèle lui-même plutôt qu'avec une copie des nombres :
  - les fenêtres sont lues dans MiniZinc grâce à une variable `::add_to_output` qui expose `MIN_P1`, `MAX_DINER`, … ; vérifié sur `bench_1` (32 périodes) et `bench_3` (48) ;
  - pour les écarts minimaux et la durée du quart, on fixe le premier employé exactement à la borne (faisable), puis une période au-delà (UNSAT) ;
  - la résolution s'arrête à la première solution intermédiaire, puisqu'il est inutile d'attendre l'optimum.
- Vérification par mutation : en faussant `BREAK_DURATION` ou `MAX_PAID_HOURS`, les sondes échouent bien (7 et 1 échecs).
- Suite complète : 31 tests verts en local et dans Docker (1 ignoré).

**Constat important pour la suite** : sur `bench_5` (8 employés × 5 activités × 48 périodes), CP-SAT ne trouve **aucune solution réalisable en 30 s**, même sans contrainte ajoutée.
- Pascal confirme que l'instance est **satisfaisable**. Avec CP-SAT, 8 workers et des graines de 1 à 20, la première solution arrive en environ 1 minute (médiane).
- L'instance est donc difficile, pas infaisable : la contrainte « au moins 1 employé si demande > 0 » la rend très serrée.
- Ça touchera l'étape 4 (contrainte dure ou pénalité) et l'étape 6 (générer des individus initiaux faisables). Pour les tests, il faut garder `bench_1` et `bench_3`, et réserver `bench_5` aux expériences.

## 2026-10-28 — Documentation : principe et structure du projet

**Principe** : toute la documentation est dans `docs/`, et chaque document est accessible depuis le `README.md` à la racine. Objectif : un coéquipier entre dans le projet sans difficulté. Une section transversale « Documentation » est ajoutée au TODO.

**Fait** : `docs/PROJECT_STRUCT.md` est réécrit pour refléter **exactement** le dépôt actuel.
- Ajouts : `.github/`, `Dockerfile`, `.dockerignore`, `.gitignore`, les 5 instances avec leurs dimensions, et chaque fichier de test avec son rôle.
- Retraits : les fichiers prévus (renvoyés au TODO). Les répertoires encore vides sont marqués comme tels.
- Vérifié par script : chaque fichier de `git ls-files` figure dans l'arbre, et rien d'autre.

**Décision** : on garde deux arbres, qui répondent à deux questions différentes.
- CLAUDE.md : **architecture cible** (« où l'on va »). Elle reste dans le contexte de Claude à chaque session.
- `docs/PROJECT_STRUCT.md` : **structure actuelle** (« où l'on est »).
- CLAUDE.md renvoie vers `docs/PROJECT_STRUCT.md`.

## 2026-10-28 — Documentation : README

**Fait** : `README.md`, le point d'entrée de la documentation. Sa structure, proposée par Pascal et complétée :
1. **Description du projet** : le problème (court résumé, puis lien vers `docs/PROBLEME.md`, à venir), l'algorithme (`docs/ALGO.md`), la structure (`docs/PROJECT_STRUCT.md`).
2. **Je viens de cloner le dépôt** : l'environnement (Docker ou local, localisation de MiniZinc), les tests (Docker en premier puisque c'est la voie préférée, puis local), les expériences (à venir, étape 10).
3. **Contribuer** : la méthode de travail, l'état d'avancement (`TODO.md`), les décisions de conception (`DEVLOG.md`), les conventions de code (`CLAUDE.md`).

En plus : un badge CI en tête de fichier. Toutes les commandes Docker documentées ont été vérifiées, y compris le montage `-v "$PWD":/app` pour tester sans reconstruire l'image. Grâce à `PYTHONDONTWRITEBYTECODE`, ce montage ne laisse aucun cache dans le dépôt.

**Choix** : `TODO.md`, `DEVLOG.md` et `CLAUDE.md` restent à la racine (CLAUDE.md doit y être, et le TODO aussi selon nos règles). Ce sont des exceptions assumées au principe « toute la doc dans `docs/` ». Le README y donne accès comme au reste.

**Planifié** : `docs/PROBLEME.md` (description du problème pour un nouveau venu).

## 2026-10-28 — Documentation : PROBLEME.md

**Fait** : `docs/PROBLEME.md`, la description du problème pour un nouveau venu.
- Contenu : données et format JSON (avec le piège de l'indexation 0/1), plage utile, variables de décision et périodes couvertes par chaque bloc, règles d'un quart (durées, durée du quart, écarts, fenêtres, avec renvois aux constantes de `shift_rules.py`), couverture et contrainte dure, coût, exemple commenté, instances, particularités.
- Le README pointe maintenant vers ce document (sans la mention « à venir »), et `PROJECT_STRUCT.md` le liste.

**Vérifications**
- Exemple : la solution optimale de `bench_1` est recalculée à la main avec la formule documentée, et on retrouve bien un coût de 94 (entièrement de la sur-couverture).
- Tous les liens relatifs du document pointent vers des fichiers existants.

**Constats sur les données**, analysées pour la documentation :
- Les sous-coûts valent 1 000 000 seulement là où la demande est positive : c'est une pénalité quasi dure. Les autres sous-coûts sont petits (0 à 3) et les sur-coûts vont de 0 à 10.
- Dans les 5 instances, la plage utile couvre toute la journée.
- La contrainte de bris de symétrie de `horaire.mzn` est en commentaire, donc désactivée.

## 2026-10-28 — Décision D8 : observabilité (journal de diagnostic et données d'expérience)

**Besoin** : le projet est expérimental. On veut des statistiques complètes sur les chromosomes, leur diversité, leur coût en contraintes et leur évolution au fil des itérations, envoyées vers la console ou vers des fichiers selon ce que demande le concepteur de l'expérience.

**Décision D8**
1. **Deux flux séparés.**
   - *Journal de diagnostic* (« que s'est-il passé ? ») : texte avec des niveaux, module `logging`.
   - *Données d'expérience* (« comment l'algorithme se comporte-t-il ? ») : enregistrements structurés, relus par des scripts d'analyse.
   - Les mélanger produit des journaux inexploitables.
2. **Patron Observateur**, dans l'esprit de D5.
   - Le moteur ne calcule ni n'écrit aucune statistique : il émet des événements.
   - Des `MetricCollector` calculent, des `RecordSink` écrivent.
   - Le choix se fait par configuration, comme pour les opérateurs.
3. **Destinations** :
   - `ConsoleSink` : résumé lisible toutes les *k* générations ;
   - `JsonlSink` : écrit au fil de l'eau, résiste à un plantage, relu directement par pandas ;
   - `CsvSink` : résumé par génération ;
   - `MemorySink` : pour les tests ;
   - `NullSink` : par défaut.
4. **Statistiques** :
   - coût de la population ;
   - **coût décomposé** ;
   - diversité génotypique (distance insensible à la permutation des employés, lien avec D3), phénotypique et des coûts ; une diversité par paires coûte O(n²), d'où une fréquence configurable ou un échantillonnage ;
   - efficacité de chaque opérateur ;
   - apport de la recherche locale, qui justifie le volet mémétique par rapport à un GA pur.
5. **Une exécution = un répertoire** `results/<expérience>/<run_id>/`. Il contient `config.json` (configuration, graine, commit Git, versions), de quoi rejouer l'exécution.
6. **Principes** :
   - enregistrer assez de données brutes pour recalculer les statistiques plus tard ;
   - un schéma versionné ;
   - mesurer ne perturbe pas l'algorithme : un collecteur ne consomme jamais le générateur aléatoire du moteur, donc la même graine donne la même évolution, avec ou sans mesure ;
   - événements émis par le thread principal (compatible avec D7) ;
   - temps marqués comme non déterministes ;
   - pas de dépendance lourde (MLflow ou TensorBoard pourront devenir une destination de plus).

**Impact sur le TODO**
- Étape 4 : l'évaluation retourne un `CostBreakdown`. C'est le seul impact immédiat : sans lui, le coût décomposé serait impossible à obtenir plus tard.
- Nouvelle **étape 8b** (`src/observability/`), avant la boucle : interfaces, destinations, configuration de `logging`, répertoire d'exécution, collecteurs.
- Étape 9 : émission des événements, et un test de reproductibilité avec ou sans collecteurs.
- Étape 10 : analyse qui relit `results/`.

## 2026-10-28 — Étape 2 : lecture des instances

**Fait** : `src/utils/io.py`.
- `load_instance(path)` lit un fichier. `parse_instance(data, name)` valide des données déjà décodées, ce qui permet de tester sans fichier.
- `ProblemInstance` : dataclass figée. Ses matrices `demand`, `over_cost` et `under_cost` sont des tableaux numpy en lecture seule. Elle porte aussi la plage utile (`first_useful_period`, `last_useful_period`) et les fenêtres des jalons (`ShiftWindows`, `MilestoneWindow`).
- Exceptions, toutes sous `InstanceError` :
  - `InstanceFileNotFoundError` ;
  - `InstanceFormatError` : JSON invalide, champ manquant, mauvais type (y compris `true`/`false`, que Python traite comme des `int`) ;
  - `InstanceDimensionError` ;
  - `InstanceValueError` : compte < 1, valeur négative, demande > nombre d'employés, le domaine de `demande` dans le modèle ;
  - `NoShiftFitsError` : plage utile vide, ou trop courte pour un quart.
- Messages dans `InstanceMessages`, champs JSON dans `InstanceFields`, domaine des valeurs dans `InstanceDomain`.
- `shift_rules.py` reçoit `ModelVariableNames`, les noms des variables MiniZinc (`debut`, `pause1`, …), pour ne pas les écrire en dur.

**Décisions**
- **Nom `ProblemInstance`** plutôt que `Instance`, pour éviter la confusion avec `minizinc.Instance`, utilisé dans les mêmes modules.
- **Convention de numérotation**, validée par Pascal (elle conditionne les étapes 3 et 4) :
  - les **numéros** de période (plage utile, fenêtres et, plus tard, jalons du phénotype) suivent MiniZinc et commencent à 1. La validation croisée avec le modèle reste ainsi directe ;
  - les **tableaux** sont indexés à partir de 0 (numpy) : la période p se lit à l'indice `p - 1`.
- Les champs inconnus du JSON sont ignorés.

**Tests** (`tests/test_io.py`, 32 tests)
- Les 5 bench se chargent. Les matrices sont conformes au JSON, en lecture seule, et l'instance est figée.
- Plage utile : rognage des périodes vides aux deux bouts. Une période qui n'a qu'un coût compte comme utile.
- `bench_2` (28 périodes) est la journée la plus courte possible : un seul début, une seule fin. Une période de moins, ou une plage utile trop courte dans une longue journée, donne `NoShiftFitsError`. Une instance entièrement nulle est rejetée.
- **Cohérence avec MiniZinc** : sur une instance de `bench_1` complétée par 3 périodes vides au début et 2 à la fin (MiniZinc donne une plage de 4 à 35), et sur `bench_2`, la plage utile et les 5 fenêtres sont identiques à celles de `horaire.mzn`.
- Tous les cas d'erreur, avec vérification du contenu des messages (nom de l'instance, champ, ligne, colonne, période).
- Vérification par mutation : un décalage de 1 dans la plage utile, et `>=` à la place de `>` pour la demande, sont tous deux détectés.

**Refactorisation** : la sonde MiniZinc est extraite de `test_shift_rules.py` vers `tests/minizinc_probe.py`, qui n'est pas un module de test, pour être partagée. Elle prend maintenant un chemin d'instance quelconque.

Suite complète : 63 tests verts en local et dans Docker (1 ignoré sous Linux).

## 2026-10-28 — Étape 2 (complément) : affichage de `ProblemInstance`

**Fait**, à la demande de Pascal :
- `__repr__` : une seule ligne avec le nom, les dimensions et la plage utile, par exemple `ProblemInstance(name='bench_1', employee_count=3, activity_count=1, period_count=32, useful_range=1..32)`. Le repr généré par `dataclass` est désactivé (`repr=False`), parce qu'il afficherait les matrices numpy en entier, ce qui rend les journaux illisibles.
- `__str__` : un résumé sur plusieurs lignes, avec les dimensions, la plage utile, les fenêtres des 5 jalons alignées, la demande totale et la demande maximale.
- `MilestoneWindow.__str__` : `début..fin`, réutilisé par les deux.
- Gabarits dans `InstanceDisplay`, selon la convention sur les constantes textuelles.

**Tests** : 5 tests de plus dans `tests/test_io.py` (`TestDisplay`), dont un qui vérifie que le repr n'affiche pas les matrices et un autre qui vérifie que l'affichage suit le rognage de la plage utile.

## 2026-10-28 — Décisions D1 (encodage par blocs) et D3 (symétrie)

**D1** (validée par Pascal) :
- L'interface `Encoding[G]` se limite à `encode(Horaire) -> G` et `decode(G) -> Horaire`. C'est une traduction pure (D6) : ni vérification de faisabilité, ni réparation.
- D1 a d'abord été tranchée pour l'encodage direct (5 jalons + 4 activités par employé). Pascal a ensuite proposé un encodage moins fragile, retenu comme **premier encodage** : `BlockEncoding`, un gène par employé, `debut, a1, d1, a2, d2, a3, d3, a4, d4` (activité et durée de chacun des 4 blocs).
- Les jalons s'en déduisent : `pause1 = debut + d1`, `diner = pause1 + 1 + d2`, `pause2 = diner + 4 + d3`, `fin = pause2 + d4`. C'est une bijection avec les jalons du phénotype, donc `encode` / `decode` restent une traduction pure. Exemple, employé 1 de l'optimum de `bench_1` (1, 5, 10, 20, 28) : d = 4, 4, 6, 8.
- Ce que l'encodage garantit par construction : l'ordre des jalons. Les 4 écarts minimaux deviennent des domaines par gène (`d_i ≥ 4`), qu'une mutation respecte en tirant dans le domaine.
- Ce qui reste : deux contraintes de couplage linéaires. D'une part `22 ≤ Σd ≤ 30`, puisque `fin - debut = Σd + 5` et qu'on veut 6 à 8 h rémunérées. D'autre part, le quart doit rentrer dans la plage utile. Un croisement qui mélange des durées peut les violer, mais la réparation est triviale.
- L'encodage invite à des opérateurs naturels : décaler `debut` déplace le quart en gardant sa forme ; transférer une période d'un bloc à l'autre déplace une pause sans changer la durée.
- La contrainte de couverture est la vraie difficulté, mais elle est la même pour tous les encodages : elle relève de l'évaluation (étape 4) et du `LocalSolver` (étape 5).
- L'encodage direct (`DirectEncoding`) devient une variante de comparaison, après la boucle complète.

**D3** (validée par Pascal) :
- La contrainte de bris de symétrie du modèle MiniZinc avait été retirée parce qu'elle nuisait : CP-SAT gère les symétries mieux que nous. On n'en ajoute **aucune** au modèle envoyé au `LocalSolver`.
- Dans l'AG, le problème est différent : c'est un problème de représentation. Deux parents équivalents mais permutés donnent, par croisement employé par employé, un enfant incohérent.
- Premier temps : pas de normalisation. On mesure l'effet (D8) avant de compliquer.
- Variante 1 : ordre lexicographique sur le gène complet, dans un encodage distinct (`SortedBlockEncoding`, dont le génome est défini comme la liste triée des gènes ; ce qui respecte D6). C'est une vraie forme canonique : deux horaires égaux à une permutation près donnent le même génome. Mais elle est fragile aux quasi-permutations, parce que `debut`, première clé, domine l'ordre. Le tri est un invariant du génome, à rétablir après chaque opérateur et après le `LocalSolver`. Bonus pour D8 : une diversité génotypique calculée sur génomes triés est insensible à la permutation.
- Variante 2, en réserve : alignement des employés au moment du croisement, par affectation minimisant la distance entre quarts (au plus 8 employés). Responsabilité de l'opérateur, sans modifier les génomes.

**Impact sur le TODO** : l'étape 3b porte sur `BlockEncoding` ; les tests de décodage infaisable visent Σd hors de 22..30 et un quart qui déborde ; l'étape 10 reçoit une tâche de comparaison des variantes (`DirectEncoding`, `SortedBlockEncoding`, croisement avec alignement).

**Décision en suspens** : D4.

## 2026-10-29 — Étape 3a : phénotype `Horaire` (scaffold)

**Fait (C)**
- `src/model/horaire.py` :
  - `HoraireEmploye` : 5 jalons et 4 activités ;
  - `Horaire` : un tuple de `HoraireEmploye` ;
  - les deux sont des dataclasses figées, donc comparables par valeur et hachables, ce que demandent l'aller-retour `decode(encode(h)) == h` et D7 ;
  - noms des champs en anglais (`start`, `break1`, `lunch`, `break2`, `end`, `activities`), comme `ShiftWindows`. Les noms de classes restent ceux de D5.
- `Horaire.from_model_variables` : construction à partir des variables de `horaire.mzn` (forme des résultats de minizinc-python). Les activités sont converties en tuples.
- `MalformedHoraireError` (sous `HoraireError`) signale une **forme** invalide : nombre d'activités différent de 4, aucun employé, variable absente ou de mauvaise longueur. Un horaire **infaisable** n'est pas une erreur (D6) : jalons dans le désordre ou quart trop court restent représentables.
- `HoraireEmploye.activity_at(p)` et `Horaire.to_grid(period_count)` : grille numpy (employés × périodes), indexée à partir de 0. Elle reprend la cascade de conditions de la 2ᵉ sortie du modèle, dans le même ordre. Les périodes hors de `1..period_count` sont ignorées.
- `src/model/feasibility.py` (scaffold, corps à écrire par Pascal) :
  - `StructuralRule` : 11 règles. Fenêtre de chacun des 5 jalons, 4 écarts minimaux, durée du quart, domaine des activités ;
  - `Violation(employee, rule, found)`, figée, avec un `__str__` diagnostique ;
  - `FeasibilityChecker(instance)` : `violations`, `employee_violations` (à écrire) et `is_feasible` (écrite, déléguée à `violations`) ;
  - `EmployeeCountMismatchError` (sous `FeasibilityError`) quand l'horaire et l'instance n'ont pas le même nombre d'employés : c'est une erreur de programmation, pas une infaisabilité.
- `tests/minizinc_probe.py` : nouvelle méthode publique `first_solution()`.

**Décisions**
- **Retourner la liste des violations** plutôt qu'un booléen ou une exception. On peut ainsi tester chaque contrainte isolément, nourrir les diagnostics et collecteurs (D8) et, plus tard, guider la réparation.
- **Couverture hors du périmètre** : « au moins 1 employé si demande > 0 » dépend de tous les employés à la fois. Elle relève de l'étape 4 (évaluation), où se décidera son traitement (infaisabilité ou pénalité).
- **Grille et `total` peuvent diverger** pour un horaire infaisable. Si des blocs se chevauchent, `total` compte l'employé deux fois alors que la grille, dont chaque case contient une seule activité, ne le peut pas. Pour un horaire faisable, les deux coïncident. Conséquence pour l'étape 4 : le coût doit reproduire `total`, pas s'appuyer sur la grille.
- **Contraintes redondantes** : les fenêtres de `pause1`, `diner` et `pause2` découlent des écarts, de la durée et des fenêtres de `debut` et `fin`. On les vérifie quand même, par fidélité au modèle. Elles ne peuvent pas être violées seules : les tests le documentent.

**Tests**
- `tests/test_horaire.py`, 20 tests verts :
  - forme et égalité par valeur ;
  - `activity_at` aux bornes de chaque bloc, avec des activités distinctes par bloc ;
  - grille de l'optimum documenté dans `PROBLEME.md` ;
  - quarts qui débordent de la journée ;
  - **validation croisée** : sur bench_1 à bench_3, la grille Python est identique à la 2ᵉ sortie de MiniZinc.
- `tests/test_feasibility.py`, 16 tests, en attente de l'implémentation :
  - instance synthétique à demande nulle, plage utile 4..43 ;
  - 7 quarts faisables, dont toutes les fenêtres à leur borne inférieure, toutes à leur borne supérieure, et les durées 27 et 35 ;
  - 10 quarts qui violent une seule contrainte, d'un cran au-delà de la borne ;
  - fenêtres redondantes, cumul de violations et numérotation des employés ;
  - incohérence du nombre d'employés ;
  - **validation croisée** : solutions MiniZinc de bench_1 à bench_3 jugées faisables. Et pour les 17 cas, verdict Python = verdict de `horaire.mzn` avec l'horaire fixé (demande nulle, donc MiniZinc ne juge que la structure).
- Les tests ont été validés contre une implémentation de référence jetable, hors du dépôt : 16/16 verts.

**En attente** : implémentation de `violations` et `employee_violations` par Pascal, puis vérification par Claude.

## 2026-10-30 — Étape 3a validée : vérification de faisabilité (Pascal)

**Fait (P)**
- `FeasibilityChecker.violations` et `employee_violations` sont implémentées.
- `employee_violations` délègue à trois méthodes :
  - `time_violations_for_employee` : durée du quart et 4 écarts, seuils lus dans `ShiftGaps` ;
  - `activity_domain_violations_for_employee` ;
  - `window_violations_for_employee` : liste explicite de triplets (règle, jalon, fenêtre).
- `MilestoneWindow.contains(period)` est ajoutée dans `io.py`.

**Revue (C), en trois passes**
- **Bogues corrigés** :
  - parcours du dict des fenêtres sans `.items()` ;
  - noms MiniZinc confondus avec les champs anglais de `HoraireEmploye` ;
  - mauvaise règle et valeur fautive de type texte pour les fenêtres ;
  - **seuil pause1 → diner à 3 au lieu de 5**, l'écart re-dérivé à la main avec un signe faux. La validation croisée MiniZinc l'a détecté. Leçon : lire les seuils dans `ShiftGaps` plutôt que les re-dériver ;
  - exception relancée sans message dans `is_feasible` ;
  - membre d'enum dont la valeur était un dict, puis membres renommés hors de l'interface convenue ;
  - **virgules finales dans l'enum**, qui faisaient des descriptions des tuples ;
  - `in` sur un objet qui n'a pas de `__contains__`.
- **Nettoyage** : import `minizinc` inutile retiré, nombres magiques remplacés par `ModelIndexing.FIRST_INDEX`, méthode `get_milestone_by_name` supprimée (elle reposait sur `assert False` et une f-string).
- **Tests ajoutés pendant la revue**, chacun parce qu'un défaut était passé inaperçu :
  - `test_is_feasible_raises_too` vérifie maintenant le message de l'exception, pas seulement son type ;
  - `test_every_rule_description_is_text` attrape les virgules finales ;
  - `TestMilestoneWindowContains` (3 tests dans `test_io.py`) : bornes incluses, fenêtre d'une seule période, fenêtre vide.

**Tests** : suite complète, 108 tests verts en local.

## 2026-10-30 — Étape 3b : génotype `Encoding[G]` et `BlockEncoding` (scaffold)

**Fait (C)**
- `src/ga/chromosome.py` :
  - `Encoding[G]` : classe abstraite générique (syntaxe PEP 695), réduite à `encode` et `decode` (D1, D6) ;
  - `ActivityBlock(activity, duration)` et `BlockGene(start, blocks)`, des dataclasses figées. `MalformedGenomeError` (sous `GenomeError`) si un gène n'a pas 4 blocs ;
  - `BlockGenome = tuple[BlockGene, ...]` ;
  - `BlockEncoding` en scaffold : `encode`, `decode`, `encode_shift`, `decode_gene` sont à écrire (P). Les formules de D1 sont dans la docstring du module.
- `src/ga/individual.py` : `Individu[G]`, dataclass figée.
  - `from_genome(genome, encoding)` décode une seule fois, à la construction ;
  - `cost` vaut `None` tant que l'individu n'est pas évalué ;
  - `with_cost` retourne une copie, sans modifier l'original (D7).

**Décisions**
- **Représentation du génome** (laissée ouverte par D1) : des dataclasses figées nommées plutôt qu'un tableau numpy. Elles sont lisibles (`gene.blocks[2].duration` plutôt que `g[6]`), immuables (D7) et hachables, ce qui sera utile pour mesurer la diversité (D8). La performance n'est pas un enjeu à ce stade : au plus 8 employés.
- **`Individu` dans son propre module** (`individual.py`), plutôt que dans `chromosome.py`, qui reste consacré aux encodages. L'arbre cible de CLAUDE.md est mis à jour en conséquence.
- **`cost: int | None`** pour l'instant. Il deviendra probablement `CostBreakdown` à l'étape 4 (D8).

**Blocage corrigé (dans les tests)** : j'avais d'abord écrit `fin - debut = Σd + 2 pauses + dîner` (Σd + 6). Or les bornes du quart sont incluses : c'est Σd + 5, comme dans D1. La correction de bornes incluses (`INCLUSIVE_BOUNDS_CORRECTION`) s'applique ici comme dans `ShiftStructure`. C'est l'implémentation de référence qui l'a révélé.

**Tests**
- `tests/test_chromosome.py` : 17 tests, en attente de l'implémentation.
  - forme du gène, interface abstraite ;
  - exemple de D1 : d = 4, 4, 6, 8 ;
  - chaque durée est la longueur de son bloc dans la grille ;
  - génome de l'optimum de bench_1 calculé à la main ;
  - ordre des employés conservé ;
  - allers-retours dans les deux sens, y compris pour des horaires et génomes absurdes (200 génomes aléatoires) ;
  - 5 génomes infaisables qui se décodent sans exception ;
  - **propriété de D1** sur 3000 gènes aléatoires (graine fixe) : l'horaire décodé est faisable si et seulement si chaque `d_i ≥ 4`, `22 ≤ Σd ≤ 30`, le quart est dans la plage utile et les activités dans leur domaine. Au moins 50 cas de chaque verdict sont exigés ;
  - **validation croisée** : aller-retour et conditions de D1 sur les solutions MiniZinc de bench_1 à bench_3.
- `tests/test_individual.py` : 9 tests verts, avec un encodage factice qui compte les appels à `decode`.
- Les tests ont été validés contre une implémentation de référence jetable, hors du dépôt : 17/17 verts. Un mutant (dîner décalé de 3 au lieu de 4) est détecté par 10 tests distincts.

**En attente** : implémentation de `BlockEncoding` par Pascal, puis vérification par Claude.

## 2026-11-07 — Étape 3b validée : `BlockEncoding` (Pascal)

**Fait (P)** : `BlockEncoding.encode_shift`, `decode_gene`, `encode`, `decode` dans `src/ga/chromosome.py`.
- `encode_shift` : `d1 = pause1 - debut`, `d2 = diner - pause1 - BREAK_DURATION`, `d3 = pause2 - diner - LUNCH_DURATION`, `d4 = fin - pause2` ;
- `decode_gene` : formules de D1 dans l'autre sens ;
- aucune vérification ni troncature : une durée négative survit à l'aller-retour (D6) ;
- les durées de pause et de dîner viennent de `ShiftStructure`, sans nombre magique.

**Revue (C)** : le fond était correct dès la première version. Retouches de forme appliquées par Pascal :
- dépaquetage des blocs et des activités (`block1, …, block4 = gene.blocks`) plutôt que des indices `[0]` à `[3]` : plus lisible, échoue bruyamment si la forme change, et ramène les lignes sous 120 caractères ;
- noms explicites dans les générateurs (dont `shift` dans `encode`, qui masquait le paramètre `horaire`) ;
- restes du scaffold retirés (commentaires `# À écrire (P).`, lignes vides superflues).

**Tests** : suite complète, 134 tests verts en local, dont les 17 de `test_chromosome.py` : propriété de D1 sur 3000 gènes, 200 allers-retours aléatoires et validation croisée sur les solutions MiniZinc de bench_1 à bench_3.

**Suite** : étape 4, évaluation (fonction de coût).

## 2026-11-07 — Étape 4 : évaluation (scaffold)

**Décision (Pascal)** : les violations sont **pénalisées**, ni infaisables ni exceptions. L'évaluation est définie pour tout horaire décodé (D6).
- « au moins 1 employé si demande > 0 » : contrainte dure dans `horaire.mzn`, absente de `cout_total`. Une violation par cellule (période, activité) de la plage utile où la demande est positive et personne ne travaille ;
- violations structurelles : celles de `FeasibilityChecker`, comptées une à une. La couverture est calculée quand même, à partir de la grille ;
- motif : un individu qui viole une contrainte reste comparable aux autres, ce qui garde un gradient pour l'AG. L'option « infaisable » le perdait, et « compter seulement » misait tout sur la réparation par le `LocalSolver`.

**Fait (C)**
- `src/model/evaluation.py` :
  - `EvaluationDefaults` : poids par défaut (1 000 000 par violation, même ordre que le sous-coût quasi dur) et seuil des cellules quasi dures ;
  - `PenaltyWeights` : dataclass figée, injectable pour les expériences ;
  - `CostBreakdown` (D8) : sous-couverture, sur-couverture, cellules quasi dures sous-couvertes (informatif), violations de couverture, violations structurelles, coût des pénalités ; propriétés `coverage_cost` (= `cout_total`), `total` (fitness), `is_feasible` ;
  - `CostEvaluator` en scaffold : `coverage_totals` et `evaluate` sont à écrire (P).
- `Individu.cost` devient `CostBreakdown | None` ; `tests/test_individual.py` adapté.
- Arbres de `CLAUDE.md` et `docs/PROJECT_STRUCT.md` mis à jour.

**Décisions de forme**
- `evaluation.py` dans `src/model/` : l'évaluation porte sur le phénotype `Horaire` et l'instance, pas sur le génome.
- `coverage_totals` rend un tableau de la forme de `instance.demand`, à 0 hors de la plage utile, plutôt qu'un tableau restreint à la plage utile : un seul système d'indices (`[p - 1, a - 1]`).
- Une activité hors domaine (horaire infaisable) n'est comptée dans aucune colonne. Piège noté dans la docstring et testé : une activité négative retomberait dans une colonne par l'indexation négative de numpy.
- Pas de nouvelle exception : le nombre d'employés différent de l'instance lève déjà `EmployeeCountMismatchError` dans `FeasibilityChecker`, qu'on laisse se propager.

**Tests** : `tests/test_evaluation.py`, 29 tests, en attente de l'implémentation.
- `CostBreakdown` et `PenaltyWeights` : propriétés, valeurs par défaut, immuabilité ;
- `coverage_totals` : cellule par cellule, employés cumulés, périodes hors plage utile ignorées, activités hors domaine (au-delà du nombre d'activités, 0, négative) ;
- cas à la main avec des coûts distincts (sur-coût 3, sous-coût 5) : couverture parfaite, sur-couverture seule, sous-couverture sans violation, colonne d'activité respectée, violation de couverture, cellule quasi dure (découverte, sous-couverte sans violation, couverte), violations structurelles, poids personnalisés, nombre d'employés incorrect ;
- optimum de bench_1 : coût 94, entièrement en sur-couverture ;
- **validation croisée** : `coverage_cost` égal à l'objectif MiniZinc sur bench_1 à bench_3, sans violation.
- Validés contre une implémentation de référence jetable, hors du dépôt : tous verts. Les 7 mutants essayés sont tous détectés : indexation négative non bornée, toutes les périodes au lieu de la plage utile, coûts permutés, quasi dur sans condition de manque, violation confondue avec sous-couverture, pénalité structurelle ignorée, mauvais poids.

**En attente** : implémentation de `coverage_totals` et `evaluate` par Pascal, puis vérification par Claude.

## 2026-11-08 — Étape 4 : évaluation (implémentation et validation)

**Fait (P)** : `CostEvaluator.coverage_totals` et `CostEvaluator.evaluate` dans `src/model/evaluation.py`.

**Blocage : critère des cellules quasi dures.** Deux tests échouaient, `test_uncovered_quasi_hard_cell` et `test_under_covered_quasi_hard_cell_without_violation`. La première version comparait le coût *payé* par la cellule (`manque × sous-coût`) au seuil, avec `>` :
- avec un manque de 1, le coût payé vaut exactement 1 000 000, et `1 000 000 > 1 000 000` est faux : aucune cellule n'était comptée ;
- le produit confond deux choses : une cellule à petit sous-coût, mais très sous-couverte, pourrait franchir le seuil.

**Critère retenu** : une cellule de la plage utile est quasi dure si elle est sous-couverte (`manque > 0`) **et** si son sous-coût *unitaire* dans l'instance atteint le seuil (`under_cost ≥ 1 000 000`). On compte des cellules, une fois chacune, quel que soit le manque. C'est une propriété de l'instance, filtrée par l'horaire.

**Clarification : quasi dure ≠ violation de couverture.** Les deux compteurs sont indépendants :
- cellule quasi dure : une donnée de l'instance (un sous-coût énorme, mais une contrainte molle). Elle n'ajoute rien au coût, déjà compté dans `under_coverage_cost`, et ne touche pas `is_feasible` ;
- violation de couverture : la contrainte dure « au moins 1 employé si demande > 0 », transformée en pénalité. Elle ajoute au `penalty_cost` et rend l'horaire infaisable.
- Dans les instances fournies, le sous-coût vaut 1 000 000 partout où la demande est positive : toute violation y est aussi une cellule quasi dure, et une cellule vide coûte environ 2 000 000. L'indépendance ne se voit que sur l'instance synthétique des tests.

**Correctifs après revue (C)**
- Un import `from tests.test_feasibility import FIRST_USEFUL_PERIOD` (inutilisé) avait été laissé dans le code de production : supprimé. Le code de `src/` ne dépend jamais de `tests/`.
- `coverage_totals` utilisait des `elif` : pour un quart dont les blocs se chevauchent, l'employé n'était compté qu'une fois, alors que le `total` de `horaire.mzn` additionne quatre `sum` et le compterait deux fois. Les quatre blocs sont maintenant testés par des `if` indépendants : `coverage_cost` est identique à `cout_total` pour **tout** horaire, faisable ou non (D6). Docstring mise à jour.
- La fin de pause est écrite `pause + BREAK_DURATION <= p`, au lieu du `p > pause` du modèle, qui supposait implicitement une pause d'une période.
- Lisibilité : tranches de la plage utile nommées (`useful_demand`, `useful_coverage`, `useful_under_cost`), noms explicites (`coverage` au lieu de `underlying_coverage`, `useful_range` au lieu de `plage`).

**Tests** : un 30ᵉ test, `test_overlapping_blocks_count_the_employee_once_per_block` (pause1 après le dîner : les périodes 23 et 24 sont dans les blocs 1 et 3, donc comptées 2). Mutant vérifié sur une copie du dépôt : le retour aux `elif` est détecté par ce test, et par lui seul. Suite complète : 164 tests verts.

**Reporté** : `coverage_totals` est une double boucle Python (employés × périodes). C'est négligeable sur bench_5 ; on la vectorisera si le profilage du GA la désigne.

**Suite** : étape 5, interface MiniZinc (`SolverAdapter`, `LocalSolver`).

## 2026-11-08 — Étape 5 : décisions D10 et D11 (planification)

**Mesures préalables** (MiniZinc 2.10, CP-SAT 9.15, en local) :
- `--fzn-flags "--params max_deterministic_time:X,random_seed:S"` avec `-p 1` : objectif, `failures` et `propagations` identiques sur deux exécutions (bench_4) ; seul `solveTime` varie. Le temps déterministe consommé n'est pas exposé dans les statistiques.
- Avec minizinc-python, l'option s'écrit `**{"fzn-flags": "..."}` : le mot-clé `fzn_flags` est transmis tel quel (`--fzn_flags`) et refusé par MiniZinc.
- Un budget trop faible ne rend aucune solution, même si la statistique `objective` est renseignée : bench_3 n'a aucune solution avec 1 unité déterministe ni en 1 s de temps mural ; il en faut environ 5 unités. bench_5 : aucune solution avec 30 unités (16 s).
- Voisinage « libérer k employés » sur une solution de bench_3 (12 000 075), budget de 2 unités : k = 1 donne 8 000 056 (optimum du sous-problème prouvé, 0,4 s) ; k = 2 et k = 3 font moins bien (11 000 052 et 11 000 071), faute d'effort. Le compromis entre k et le budget sera un paramètre d'expérience.
- Limites d'effort des autres solveurs installés : Gecode a `--node` et `--fail` ; Chuffed et HiGHS n'ont que le temps mural.

**Décision (Pascal) — D10** : limite d'effort **configurable et typée**. Pascal a relevé que `max_deterministic_time` est propre à CP-SAT. Les unités d'effort ne sont pas comparables d'un solveur à l'autre : pas de limite générique, mais des types explicites (`WallTimeLimit`, `DeterministicTimeLimit`, plus tard `FailureLimit`), que chaque `SolverAdapter` déclare comprendre ou non (`UnsupportedLimitError` à la construction). Défaut de `CpSatAdapter` : déterministe, 1 thread. La charge est mesurée avec les statistiques standard de MiniZinc, en champs optionnels ; D10 compare le mémétique et MiniZinc seul avec le même solveur.

**Décision (Pascal) — D11** :
- voisinage : k employés libérés au hasard (RNG injecté), plus toujours les employés structurellement infaisables ;
- borne `cout_total ≤ coût de l'entrée` seulement si l'entrée est faisable ; sinon le `LocalSolver` répare ;
- aucune solution : on rend l'entrée inchangée, avec le statut ; pas d'exception.

**Décision de forme** : l'étape 5 se découpe en 5a (`src/memetic/solver.py` : adaptateur, limites, statistiques, issues) et 5b (`src/memetic/local_search.py` : voisinage et `LocalSolver`). L'arbre cible de CLAUDE.md, qui mettait tout dans `local_search.py`, sera mis à jour au scaffold.

**Suite** : 5a.

## 2026-11-08 — Étape 5a : `SolverAdapter` (validée)

**Fait (C)** : `src/memetic/solver.py`.
- Limites d'effort typées, figées et validées (strictement positives) : `EffortLimit`, `WallTimeLimit`, `DeterministicTimeLimit` ; `SolverOptions(limit, seed, threads)`, déterministe par défaut, 1 thread.
- `SolverAdapter` (patron Méthode modèle) : `solve(instance, extra_constraints)` est commun à tous les solveurs. Une sous-classe ne fournit que `solver_id()`, `supported_limits()` et `solver_arguments()`. La limite est vérifiée à la construction (`UnsupportedLimitError`).
- `CpSatAdapter` : `DeterministicTimeLimit` ⇒ `--params max_deterministic_time:…,random_seed:…` ; `WallTimeLimit` ⇒ `time_limit`, graine transmise dans les deux cas.
- `SolverRun(outcome, variables, objective, statistics)` : `variables` a la forme attendue par `Horaire.from_model_variables` ; `None` sans solution.
- `SolveOutcome` : `OPTIMAL`, `FEASIBLE`, `UNSATISFIABLE`, `NO_SOLUTION`. `ERROR` et `UNBOUNDED` lèvent `SolverFailureError`, tout comme une `minizinc.MiniZincError` (par exemple une contrainte ajoutée mal formée).
- `SolverStatistics` : `nodes`, `failures`, `propagations`, `solve_time`, chacun `None` s'il n'est pas rapporté (CP-SAT ne rapporte pas `nodes`).

**Décisions de forme**
- Les données sont transmises à MiniZinc depuis `ProblemInstance` (affectation des paramètres), sans fichier : l'adaptateur accepte aussi les instances synthétiques des tests.
- Solutions intermédiaires demandées systématiquement, et on garde la dernière : la meilleure solution est récupérée quelle que soit la façon dont le solveur s'arrête (limite déterministe ou temps mural).
- Un `minizinc.Model` est reconstruit à chaque appel (aplatissement à chaque fois, de l'ordre de 0,1 à 0,4 s) : simple et sans état partagé (D7). À optimiser seulement si le profilage le désigne.
- `MiniZincNotFoundError` et `SolverNotAvailableError` sont propagées telles quelles depuis `minizinc_env` : ce sont des erreurs d'environnement, pas des pannes de résolution.
- La reproductibilité sous limite déterministe suppose un seul thread : avec plusieurs threads, CP-SAT ne l'est plus. C'est documenté, pas imposé.

**Tests** : `tests/test_solver.py`, 23 tests verts.
- sans solveur : validation des limites et des options, traduction des options pour les deux limites, limite non supportée, adaptateur abstrait, traduction de chaque `minizinc.Status`, extraction des statistiques ;
- avec CP-SAT : optimum 94 de bench_1 prouvé, sous les deux limites ; variables ⇒ `Horaire` de même coût et faisable (validation croisée avec `CostEvaluator`) ; statistiques présentes ; reproductibilité (même solution, mêmes `failures` et `propagations`) ; contrainte ajoutée respectée ; contrainte impossible ⇒ `UNSATISFIABLE` ; contrainte mal formée ⇒ `SolverFailureError` ; budget de 0,5 unité sur bench_5 ⇒ `NO_SOLUTION`.
- Mutants vérifiés sur une copie du dépôt, tous détectés : première solution au lieu de la dernière, contraintes ajoutées ignorées, `UNKNOWN` traduit en `FEASIBLE`, graine non transmise, `MiniZincError` non enveloppée.
- Suite complète : 187 tests verts.

**Suite** : 5b, scaffold du `LocalSolver`.

## 2026-11-09 — Discussion : parler directement à CP-SAT ?

Question de Pascal : est-on obligés de passer par MiniZinc ? Non : OR-Tools a une API Python (`cp_model`).
- Ce qui manque : le modèle réécrit en `CpModel` (le canal `total[p, a]` par contraintes réifiées, l'objectif avec `max(0, …)`), une validation croisée contre `horaire.mzn`, la dépendance `ortools` (dont la version peut différer du CP-SAT 9.15 de MiniZinc), et surtout une interface `SolverAdapter.solve` neutre : aujourd'hui, elle reçoit des chaînes MiniZinc (`extra_constraints`).
- Gains : modèle construit une fois par instance (plus d'aplatissement à chaque appel), `AddHint` pour démarrer à chaud, `deterministic_time` consommé rapporté (D10).
- Pertes : indépendance du solveur (D2), et deux modèles à garder identiques.

**Décision (Pascal)** : on garde le cap avec MiniZinc. On refactorisera vers l'API à la fin du projet, si le besoin se fait sentir (mesures du temps d'aplatissement). Consigné dans TODO.md, étape 10. L'interface de 5a reste telle quelle pour l'instant.

## 2026-11-09 — Passage au travail en équipe et scaffold commun (Claude)

**Contexte** : trois membres (Mély, Tristan, Xavier) rejoignent Pascal sur le dépôt. Les étapes 5b, 6, 7a et 7b avancent en parallèle cette semaine, chacune sur sa branche.

**Fait (C)**
- `TEAM.md` : règles communes (une branche par sous-étape, fusion par *pull request* seulement avec une suite verte, relecture par un autre membre, interfaces partagées modifiées seulement après concertation, entrées du DEVLOG signées et ajoutées à la fin), puis une fiche par membre : fichiers, classes, dépendances, commande de test.
- `CLAUDE.md` : la règle 0 (pédagogie) vaut pour chaque membre ; nouvelle règle 7 (travail en équipe) : les règles 3 et 5 s'appliquent par personne et par branche. Arbre cible : `initialization.py`, `selection.py` et `registry.py` ajoutés dans `src/ga/`.
- `TODO.md` : légende généralisée (« le membre responsable ») ; étape 6 détaillée ; étape 7 découpée en 7a (sélection et registre) et 7b (variation) ; nouvelle section « Travail en équipe ».
- CI : déclenchée aussi par les *pull requests* vers `main`.
- **Scaffold commun** : interfaces, classes concrètes en squelette (`raise NotImplementedError`, suivi d'un commentaire qui nomme l'étape et le membre), exceptions et gabarits de messages :
  - `src/memetic/local_search.py` (5b) : `Neighborhood`, `LocalSolver`, `LocalSearchResult`, `LocalSearchConstraints` (gabarits des contraintes MiniZinc), `RandomEmployeesNeighborhood` (validation de `size` écrite), `MiniZincLocalSolver` ;
  - `src/ga/initialization.py` (6) : `PopulationInitializer[G]`, `RandomBlockInitializer` ;
  - `src/ga/operators.py` (7b) : `VariationOperator[G]` (`encoding_type`, `is_compatible_with` écrit), `Crossover[G]`, `Mutation[G]`, `UniformGeneCrossover`, `ShiftStartMutation`, `BlockBoundaryMutation`, `ActivityMutation` ;
  - `src/ga/selection.py` (7a) : `ParentSelector[G]`, `MutableSelector[G]`, `check_selectable` (vérifications communes, écrites), `TournamentSelector` (validation de `size` écrite), `UniformMutableSelector` ;
  - `src/ga/registry.py` (7a) : `OperatorRegistry`, `IncompatibleOperatorError`, `DuplicateOperatorError`, `UnknownOperatorError`.
- Tests : `tests/fixtures.py` (outil commun : `evaluated_individual`, `cost_with_total`, `reference_genome`, `FakeLocalSolver`) et un squelette de tests par module. Chaque squelette contient les tests de contrat du scaffold (verts) et, en tête de fichier, la liste des cas à couvrir.

**Décisions de forme**
- Les opérateurs de variation manipulent des **génomes**, pas des individus : le moteur construit et évalue les individus. Un opérateur ne dépend ainsi que de son encodage (D5).
- Les sélecteurs tirent par lot (`select(population, count, rng)`, D7), avec remise, sur `cost.total`. La population doit être évaluée.
- Un initialiseur rend des individus **non évalués** : l'évaluation reste la responsabilité du moteur.
- La sélection est sortie de `operators.py` (`selection.py`, `registry.py`), pour que les membres des étapes 7a et 7b ne modifient jamais le même fichier.
- `NotImplementedError` sans message : la règle « les messages sont des constantes » ne justifie pas une classe de messages pour du code temporaire.
- Sur `main`, aucun test ne vise les squelettes : la suite reste verte. Les tests complets de 5b (C) seront écrits sur la branche de Pascal ; ceux de 6, 7a et 7b sont écrits par leurs auteurs (P), guidés par la liste en tête de chaque fichier.

**Correctif** : `docs/PROJECT_STRUCT.md` ne listait pas `tests/test_solver.py`. Mon remplacement de l'étape 5a visait une ligne `├──`, alors que la dernière ligne de l'arbre commence par `└──`, et il ne l'a pas signalé. Le bloc des tests est réécrit dans l'ordre alphabétique.

**Tests** : 21 tests de contrat, instantanés ; suite complète : 208 tests verts, y compris avec `-W error::DeprecationWarning` comme dans la CI.

**Suite** : commit du scaffold sur `main`, puis création des quatre branches.

## 2026-11-09 — Étape 5b : tests du `LocalSolver` (Claude, branche `etape-5b-local-solver`)

**Fait (C)** : `tests/test_local_search.py`, 26 tests, qui servent de cahier des charges à l'implémentation de Pascal.
- Contrat du scaffold (5 tests, verts dès maintenant) : interfaces abstraites, résultat figé, gabarits des contraintes, validation de `size`.
- `RandomEmployeesNeighborhood`, sans MiniZinc (instance synthétique, trois employés) : exactement `size` employés libérés quand tous sont faisables, numéros dans 1..n ; `size` au-delà du nombre d'employés ⇒ tous libérés ; un employé infaisable toujours libéré, **en plus** des `size` employés tirés parmi les faisables ; même graine ⇒ même sélection ; sur 200 graines, chaque employé finit par être libéré.
- `fixing_constraints` et `cost_bound_constraints`, sans MiniZinc (optimum de bench_1) : neuf contraintes par employé fixé (cinq jalons, quatre activités) ; aucune si tout le monde est libéré ; borne = coût de couverture (94) pour une entrée faisable ; aucune borne pour une entrée structurellement infaisable, ni pour une entrée qui viole la contrainte « au moins 1 ».
- `improve` avec un adaptateur scénarisé (`ScriptedAdapter`, sans MiniZinc) : la solution devient le résultat ; sans solution (`UNSATISFIABLE`, `NO_SOLUTION`), l'entrée est rendue telle quelle (même objet) ; issue, employés libérés et statistiques transmis ; le solveur reçoit les contraintes de fixation et la borne ; le voisinage reçoit le générateur.
- `improve` avec CP-SAT : sur bench_1, jamais pire que l'entrée et employés non libérés inchangés ; réparation d'un employé dégénéré (résultat faisable, de coût 94) ; tout le monde libéré ⇒ optimum 94 ; trois quarts identiques avec personne de libéré ⇒ `UNSATISFIABLE` et entrée rendue ; bench_5 avec un budget de 0,5 unité ⇒ `NO_SOLUTION` et entrée rendue ; même graine ⇒ même résultat et mêmes statistiques.

**Validation des tests** : sur une copie du dépôt, hors de la branche, contre une implémentation de référence jetable : 26 tests verts. Quatre mutants de la référence sont tous détectés : borne ajoutée même à une entrée infaisable, tirage parmi tous les employés au lieu des faisables, employés infaisables non libérés, fixation des employés libérés au lieu des autres. Un cinquième, une borne sur `cost.total` au lieu de `coverage_cost`, est équivalent : la borne ne s'applique qu'aux entrées faisables, dont les pénalités sont nulles.

**État de la branche** : 5 tests verts, 21 en erreur (`NotImplementedError`), comme prévu. La suite complète n'y redeviendra verte qu'avec l'implémentation ; la branche ne sera pas fusionnée avant.

**Suite** : implémentation par Pascal de `fixing_constraints`, `cost_bound_constraints`, `RandomEmployeesNeighborhood.select`, puis `improve`.

## 2026-11-10 — Étape 5b : `LocalSolver` validé (Pascal, revue par Claude)

**Fait (P)** : `RandomEmployeesNeighborhood.select`, `MiniZincLocalSolver.improve`, `fixing_constraints` et `cost_bound_constraints` dans `src/memetic/local_search.py`.

**Blocage : signification de `size`.** La première version lisait `size` comme le **total** des employés libérés, infaisables compris, et tronquait la liste à `size` éléments. `test_infeasible_employee_is_always_freed` (avec `size = 0`) échouait. Le contrat de D11 est : `size` employés tirés **parmi les faisables**, **plus** tous les infaisables. La troncature était le vrai danger : quelle que soit la lecture de `size`, un employé infaisable fixé rend le sous-problème insatisfiable d'emblée (jalons hors domaine), et le `LocalSolver` ne répare plus.

**Correctifs après revue**
- `cost_bound_constraints` : une seule évaluation ; plus de `FeasibilityChecker` en double (`CostBreakdown.is_feasible` couvre déjà les violations structurelles et la contrainte « au moins 1 ») ; borne sur `coverage_cost` plutôt que `total`. Les deux valeurs sont égales pour une entrée faisable (mutant équivalent, voir l'entrée du 2026-11-09), mais `cout_total` du modèle est exactement le coût de couverture : la borne ne doit pas dépendre du fait implicite que les pénalités sont nulles.
- `fixing_constraints` : `ModelIndexing.FIRST_INDEX` au lieu de `1` ; `enumerate` sur les activités, sans indices ; jalons parcourus comme une séquence de paires (variable, valeur).
- Tirage reproductible : candidats triés avant `rng.sample`, plutôt que l'ordre d'itération d'un `set`.
- Choix de Pascal : l'expression conditionnelle qui choisit l'horaire rendu dans `improve` est gardée, son intention étant explicite sur une ligne.

**Tests** : 26 tests de `tests/test_local_search.py` verts ; suite complète : 228 tests verts, y compris avec `-W error::DeprecationWarning`.
- `test_unsatisfiable_subproblem_returns_the_input` affichait `MiniZincWarning: model inconsistency detected` : toutes les variables étant fixées, MiniZinc détecte l'incohérence dès l'aplatissement. L'avertissement est attendu ; il est désormais ignoré dans ce test, comme dans `test_solver.py` (oubli de Claude). Le traitement de cet avertissement dans `SolverAdapter.solve` lui-même est noté dans TODO.md (5a), à discuter en équipe.

**Suite** : *pull request* de `etape-5b-local-solver` vers `main`. Après la fusion, l'option `LocalSolver` de l'étape 6 (Mély) pourra être branchée sur `MiniZincLocalSolver`.

## 2026-11-13 — Étape 6 : Initialisation de la population (Mély)

**Fait (P)** : Implémentation de `RandomBlockInitializer.initialize`, `random_genome`, `random_gene`
dans `src/ga/initialization.py`.

**Génération des génomes**
- Chaque employé possède quatre blocs d'Activités, d'une durée minimale de 4 périodes.
- La durée totale des blocs est tirée aléatoirement entre 22 et 30 périodes, selon la plage utile disponible.
- Les périodes restantes sont réparties aléatoirement entre les quatre blocs.
- Les activités et la période de début sont tirées aléatoirement dans leurs domaines respectifs.
- Le générateur `rng` est utilisé pour assurer la reproductibilité.

**Option `LocalSolver`** : Si un solveur local est fourni, chaque horaire généré lui est transmis. L'horaire retourné est réencodé avec `BlockEncoding` pour construire un nouvel individu non évalué.

**Tests** : 11 tests de `tests/test_initialization.py` verts ; suite complète : 236 tests verts. Vérification de la taille de population, de la faisabilité structurelle, de la reproductibilité, de la diversité, des tailles invalides et de l'intégration d'un faux solveur local. Les cinq benchmarks ont également été testés.

**Suite** : Mettre à jour `TODO.md`, puis préparer la *pull request* de `etape-6-initialisation` vers `main` après validation finale.










## 2026-11-13 — Étape 6 : initialisation contre le vrai solveur (Pascal)

**Fait (C)** : `TestInitializationWithCpSat` dans `tests/test_initialization.py`. `RandomBlockInitializer` est branché sur `MiniZincLocalSolver` (CP-SAT, `DeterministicTimeLimit(5.0)`), par l'intermédiaire d'un `RecordingLocalSolver` qui note chaque paire (horaire tiré, résultat). Invariants vérifiés pour chaque individu : faisabilité structurelle, horaire rendu ré-encodé sans perte par `BlockEncoding`, entrée gardée telle quelle si le solveur ne trouve pas de solution, coût de couverture jamais pire qu'une entrée déjà faisable.

**Mesures (graine 0, 6 individus)**

| Instance | Employés libérés | Issues | Individus faisables | Temps |
|---|---|---|---|---|
| bench_1 | 1 | 6 × OPTIMAL | 6 / 6 (coûts 116 à ≈ 2·10⁶, cellules quasi dures sous-couvertes) | 2,8 s |
| bench_1 | 3 (tous) | 6 × OPTIMAL | 6 / 6, tous à l'optimum 94 | 4,1 s |
| bench_3 | 2 | 6 × UNSATISFIABLE | 0 / 6 | 3,2 s |
| bench_5 | 2 | 6 × UNSATISFIABLE | 0 / 6 | 3,9 s |
| bench_5 | 8 (tous) | 6 × NO_SOLUTION (budget épuisé) | 0 / 6 | 25,8 s |

**Constats à discuter en équipe**
- **Asymétrie pénalité / contrainte dure** (relevée par Pascal) : l'évaluation (étape 4) traite « au moins 1 employé si demande > 0 » comme une **pénalité** ; le `LocalSolver` résout `horaire.mzn`, où c'est une **contrainte dure** (ligne 154), qu'on ne peut pas relâcher en ajoutant des contraintes.
- Les horaires tirés au hasard violent presque toujours « au moins 1 ». Sur bench_3 et bench_5, avec 2 employés libérés, les UNSATISFIABLE sont un **artefact de cette contrainte dure** : un sous-problème pénalisé aurait rendu la solution la moins pénalisée du voisinage, donc une amélioration. Ces individus ne sont pas perdus pour autant : du point de vue de l'algorithme génétique, ils ont un coût pénalisé fini (4·10⁷ à 10⁸) et participent à la sélection ; seule l'amélioration par le `LocalSolver` leur échappe. Décision D12 ajoutée à TODO.md.
- Tout libérer sur bench_1 fait converger toute la population vers l'optimum : elle perd toute diversité dès l'initialisation. Ce constat vient de la taille du voisinage, pas de la contrainte dure. Sur bench_5, le budget de 5 unités ne suffit même pas pour trouver une première solution.
- Pistes pour la diversité : réparer seulement une partie de la population ; voisinage plus petit à l'initialisation ; tirage guidé par la demande. À trancher avant l'étape 8 (convergence et restart).

**Tests** : 15 tests de `tests/test_initialization.py` verts (environ 19 s, dont 4 qui appellent CP-SAT).

**Environnement** : `.venv` local (Python 3.14, MiniZinc 2.10 du bundle MiniZincIDE trouvé automatiquement), alors que le README demande Python 3.13.

## 2026-11-13 — Étape 7a : Sélection et registre des opérateurs (Tristan, tests générés par claude)

Fait (P) : Implémentation de `TournamentSelector.select` et `UniformMutableSelector.select` dans `src/ga/selection.py`, et de `OperatorRegistry` (`register`, `names`, `create`, `check_compatibility`) avec ses trois erreurs dans `src/ga/registry.py`.

Sélection

* Les deux sélecteurs appellent d'abord `check_selectable` (`count` invalide, population vide, individu non évalué).
* Tirage par lot avec remise (D7) : `select` rend un `tuple` d'exactement `count` individus tirés dans la population, sans jamais la modifier.
* Tournoi : pour chaque parent, `size` individus sont tirés avec `rng.choices(..., k=size)`, puis on retient celui de plus faible `cost.total` (`min`). En cas d'égalité, le premier candidat tiré l'emporte. Un tournoi de taille 1 équivaut à un tirage uniforme.
* `UniformMutableSelector` : `rng.choices(..., k=count)`, sans regard au coût.
* Le seul aléa provient du `random.Random` passé en paramètre (D5).

Registre

* `register` associe un nom à une fabrique (classe ou fonction) et lève `DuplicateOperatorError` si le nom existe déjà ; le registre reste inchangé après l'erreur.
* `names` rend les noms triés ; `create` appelle la fabrique avec `**parameters` et rend une nouvelle instance à chaque appel.
* `check_compatibility` utilise `VariationOperator.is_compatible_with` et lève `IncompatibleOperatorError` sinon. Le registre dépend de la base commune `VariationOperator` (`src/ga/operators.py`), et non seulement de `Crossover[G]` et `Mutation[G]`.
* Les trois erreurs construisent leur message depuis `RegistryMessages` et conservent les valeurs en attributs (`registry_name`, `operator_name`, `known` trié, `operator_class`, `expected_encoding`, `actual_encoding`).
* Changement d'interface à signaler en revue : les erreurs scaffoldées comme classes vides ont maintenant un `__init__` avec paramètres (le site d'appel passe les données brutes, pas le message).

Tests : 36 tests dans `tests/test_selection.py` et 19 dans `tests/test_registry.py`.

* Sélection : contrat commun aux deux sélecteurs (taille, tuple, provenance, population d'un seul individu, population non modifiée), erreurs de `check_selectable`, tests statistiques à graine fixée (le meilleur gagne un grand tournoi, un meilleur individu est tiré plus souvent, chaque individu finit par être tiré), et tests écrits à la main avec un `ScriptedRandom` (tirages écrits d'avance : vainqueur exact de chaque tournoi, règle d'égalité, table des 9 paires ordonnées dont les victoires sont 5, 3 et 1).
* Registre : `register` puis `create` (type, paramètres, fabrique fonction, nouvelle instance), `names` (vide, trié), doublon et nom inconnu (noms cités dans le message, noms connus triés), compatibilité avec le vrai `BlockEncoding` et un encodage factice.
* Aucun test n'appelle `select` deux fois pour comparer les résultats ; la reproductibilité est vérifiée par une seule exécution contre une valeur attendue.

Suite : Mettre à jour `TODO.md`, relancer la suite complète (`python -m unittest discover`, 286 tests, 1 ignoré, tous verts), puis préparer la pull request de `etape-7a-selection` vers `main` après validation finale.

## 2026-11-14 — suivi étape 7a : Sélection et registre des opérateurs (Tristan, tests générés par claude)

Fait (P) : Correction d'erreurs trouvées suite au merge de la [`PR #4`](https://github.com/pascalcharp/memetic_pipeline/pull/4).

Sélection

* Création de `_play_tournament_round` dans `TournamentSelector` pour améliorer la lisibilité du code ; la méthode est privée (préfixe `_`).

Registre

* `self.operators` renommé `self._factories`, avec l'annotation `dict[str, Callable[..., Any]]` : le dictionnaire contient des fabriques (classes ou fonctions), pas des `VariationOperator`. L'attribut privé empêche de contourner le contrôle des doublons ; `names()` sert à le consulter.
* `register` : le bloc if-else est remplacé par une clause de garde.

Documentation

* `TODO.md` : cases de 7a cochées
* `TEAM.md` : ligne `Étape 7a` cochée
* `DEVLOG.md` : cinq lignes vides retirées avant l'entrée du 2026-11-13 et saut de ligne ajouté en fin de fichier.

Tests : 2 nouveaux tests dans `tests/test_registry.py` (21 au total), et nettoyage des deux fichiers de tests.

* Nouveaux tests : deux registres distincts ne partagent pas leurs fabriques ; un registre vide lève `UnknownOperatorError` dont `known` est vide.
* Le test de la valeur par défaut du tournoi compare `size` à `SelectionDefaults.TOURNAMENT_SIZE`, au lieu de construire un second `TournamentSelector()`.
* Nombres magiques retirés. Dans `test_selection.py`, constantes de module (`CONTRACT_COUNT`, `BEST_ALWAYS_WINS_COUNT`, `UNIFORM_TOLERANCE_RATIO`, `MIDDLE_TOTAL`) et variables locales `count` / `size` dans chaque test, pour que le rôle de chaque nombre soit lisible. Dans `test_registry.py`, noms d'opérateurs en constantes et noms de classes tirés de `__name__`.
* Les deux tests de contrat de `test_registry.py` sont renommés selon la convention given_when_then.
* La docstring de `ScriptedRandom` note que les tests sont liés à l'emploi de `rng.choices` dans le tournoi : une réécriture avec `randrange` ou `sample` les casserait, même si le comportement restait correct (compromis accepté).

## 2026-11-16 — Étape 7b : opérateurs de variation pour `BlockEncoding` (Xavier ; revue et corrections avec Pascal)

Fait (P), par Xavier, branche `feature/block-encoding` (PR #7) : `UniformGeneCrossover` (masque uniforme gène par gène, d'après Syswerda 1989), `ShiftStartMutation`, `BlockBoundaryMutation` et `ActivityMutation` dans `src/ga/operators.py`, avec leurs tests ; un `.editorconfig` (indentation Python à 4 espaces).

Revue (Pascal, 2026-11-16). La CI était verte, mais les tests remplaçaient le générateur aléatoire par des `mock`, qui rendaient la valeur attendue et masquaient des bogues. Appliquées avec un vrai `random.Random` à 200 génomes faisables de bench_5, les mutations donnaient : `ActivityMutation`, 52 activités invalides ; `ShiftStartMutation`, 59 génomes inchangés et 8 infaisables ; `BlockBoundaryMutation`, 2 blocs de moins de 4 périodes. Corrections faites par Pascal sur la branche de Xavier, avec son accord, une à une : un test qui échoue d'abord (écrit par Claude), puis la correction.

Bogues corrigés

* `ActivityMutation` tirait un indice dans la liste des activités de remplacement au lieu d'une activité (`randrange(len(...))`) : activité 0 inexistante, activité d'origine retirée par hasard, activité la plus haute jamais tirée. Correction : `rng.choice(new_activities)`.
* `BlockBoundaryMutation` modifiait le mauvais gène dès qu'un gène avait été écarté : les blocs étaient choisis dans `genes_to_try[index]`, mais écrits dans `mutated[index]`.
* `BlockBoundaryMutation` levait `GenomeCannotMutate` en pleine exécution quand aucun gène ne pouvait céder le transfert tiré (par exemple un quart faisable de durées 6, 6, 5, 5 avec un transfert de 3). Elle rend maintenant le génome inchangé, comme `ActivityMutation` sur une instance à une seule activité.
* `BlockBoundaryMutation` déplaçait du temps entre deux blocs quelconques, au lieu de deux blocs voisins comme le demandent la docstring et le plan. Correction : tirage parmi les paires (bloc qui reçoit, bloc qui cède) de blocs consécutifs, dans les deux sens, où le bloc qui cède a assez de marge.
* `ShiftStartMutation` tirait un décalage nul une fois sur quatre (`randrange(4)`), et ne ramenait le début que dans la fenêtre de début : un quart long pouvait finir après la fenêtre de fin (toutes les violations observées étaient des `END_WINDOW`). Le début est maintenant ramené entre `windows.start.earliest` et `min(windows.start.latest, windows.end.latest − longueur du quart)`, la longueur valant `Σd + 2 × BREAK_DURATION + LUNCH_DURATION − INCLUSIVE_BOUNDS_CORRECTION`.

Décisions et nettoyage

* « If it works, don't fix it » : la logique de Xavier est gardée (boucle de `BlockBoundaryMutation` qui écarte les gènes un à un, masque généré du croisement) ; seuls les défauts ont été corrigés.
* `Encoding.clone` retiré (interface et implémentations) : `src/ga/chromosome.py` est un module partagé validé, et les génomes sont immuables (D7), donc partageables sans copie. `encode(decode(g))` ne garantissait pas non plus de rendre le même génome pour un génome infaisable. `chromosome.py` et `tests/test_individual.py` sont revenus à leur état de `main`.
* Nombres magiques déplacés dans `OperatorDefaults` : `MIN/MAX_BOUNDARY_TRANSFER`, `MIN/MAX_SHIFT_AMPLITUDE`, `SHIFT_DIRECTIONS`, `MIN_ACTIVITY_COUNT_TO_MUTATE` ; indices d'activité à partir de `ModelIndexing.FIRST_INDEX`. Nouvelle méthode `BlockBoundaryMutation.get_transfer_bounds(genome)`, qui rend pour l'instant les bornes fixes et prépare une amplitude calculée (suggestion de Xavier, reportée dans TODO.md, 7b).
* Messages d'erreur : toutes les exceptions sont levées avec un gabarit de `OperatorMessages` (`WRONG_PARENT_COUNT`, `PARENT_LENGTH_MISMATCH`, `EMPTY_GENOME`, `GENE_CANNOT_GIVE`), formaté par le code qui lève l'exception (convention commune, comme `selection.py` ; la forme du registre attend D14).
* `GenomeNoGeneToMutateError` et `GenomeCannotMutate` réunies en `EmptyGenomeError`, levée par les trois mutations pour un génome vide (erreur d'appel). `ActivityMutation` levait jusque-là une `ValueError` de Python.
* Fautes de frappe et noms corrigés (`GeneCannotMutateBoundaryError`, `length`, `minimum_duration`, `*_MUTATION`, neuf noms de tests). Le franglais des noms de variables est toléré pour l'instant.

Tests : 41 tests dans `tests/test_operators.py` (tests écrits par Claude pour les corrections).

* Nouveaux tests avec un vrai `Random` à graine fixée, qui vérifient des propriétés sur beaucoup de mutations, sur des génomes construits à la main et sur 50 génomes faisables de bench_5 tirés par `RandomBlockInitializer` : activité valide et différente, toutes les activités tirées ; un seul gène modifié, Σd conservée, durées ≥ 4, blocs voisins ; décalage jamais nul, quart décalé faisable selon `FeasibilityChecker` (qui sert d'oracle : les tests ne recalculent pas les fenêtres) ; génome rendu inchangé quand rien n'est mutable ; entrées jamais modifiées ; reproductibilité.
* Cas construits pour révéler les bogues : gène dont tous les blocs sont à la durée minimale placé avant un gène mutable (bogue du mauvais gène) ; quart de 8 heures au début faisable le plus tardif (fenêtre de fin).
* Supprimés, car ils décrivaient les comportements fautifs ou testaient une méthode privée devenue obsolète : six tests à base de mock. Les autres tests de Xavier sont gardés, deux avec un mock adapté (`rng.randint`).
* Messages : un test par exception vérifie que le message contient l'information utile (opérateur, nombres reçus et attendus, longueurs, transfert).

Leçon : un mock du générateur aléatoire rend la valeur que le test attend ; il peut cacher un indice pris pour une valeur (bogue 1) ou ne jamais emprunter le chemin fautif (bogue 2, invisible sur des génomes d'un seul gène). Les propriétés vérifiées avec un vrai générateur ont trouvé les quatre bogues.

Suite complète : 326 tests, tous verts.

Reste avant la fusion : relecture par Xavier ; `git push` ; description de la PR #7 (elle recopie l'énoncé de la tâche) ; la branche s'appelle `feature/block-encoding` au lieu de `etape-7b-variation`. TEAM.md sera coché à la fusion.

## 2026-11-16 — Planification de la semaine du 16 novembre, D4 et scaffold commun des étapes 8, 8b et 9 (Pascal et Claude)

**D4 tranchée** (Pascal et Claude) : remplacement (μ+λ) sans doublons ; convergence par stagnation du meilleur pendant G générations ; restart en gardant une élite de k individus et en régénérant le reste avec l'initialiseur de l'étape 6 ; variante « peine de mort » complétée par les meilleurs infaisables quand les faisables manquent. Valeurs par défaut : G = 10, k = 1. Ajout de Claude, à confirmer en équipe : s'il y a moins de μ génomes distincts, on complète avec des doublons dans l'ordre des coûts. Détail dans TODO.md (D4).

**Répartition** (TEAM.md, semaine du 16 novembre) : Pascal, 5c (D12) puis 9-intégration ; Tristan, 8 ; Mély, 8b (collecteurs) ; Xavier, 9. D13, D14 et l'entrée 5c, jusque-là seulement sur la branche `etape-5c-couverture-souple`, arrivent sur `main` avec la planification. TEAM.md : lignes 5b, 6, 7b et D4 cochées.

**Scaffold commun** (Claude), en un seul commit sur `main`, avant la création des branches :
- étape 8 (`src/ga/population.py`) : interfaces `SurvivorSelector`, `ConvergenceCriterion`, `RestartPolicy` ; squelettes de `PlusSurvivorSelector`, `DeathPenaltySurvivorSelector`, `StagnationCriterion`, `EliteRestart` (validation des paramètres écrite) ; `PopulationDefaults`, messages, exceptions ;
- étape 8b (`src/observability/`) : infrastructure écrite et testée — événements typés de D8 et `make_record` (`events.py`), destinations (`sinks.py`), `ObservationHub` (`hub.py`), `configure_logging` et `get_logger` (`logging_config.py`), `RunDirectory` et `config.json` (`run_directory.py`) ; `results/` ajouté au `.gitignore`. Dans `collectors.py` : interface `MetricCollector` et squelettes des quatre collecteurs ;
- étape 9 (`src/memetic/`) : `Executor` et `SequentialExecutor` écrits et testés (`executor.py`) ; `TerminationCriterion` et squelette de `GenerationLimit` (`termination.py`) ; `SeedStreams` et squelette de `derive_task_seeds` (`seeds.py`) ; champs de `MemeticConfig` et squelette de `validate` (`config.py`) ; `MemeticResult` et squelette de `Memetic`, dont la docstring décrit le déroulement attendu et les points d'émission des événements (`engine.py`) ;
- tests : contrats des scaffolds (`test_population.py`, `test_collectors.py`, `test_engine.py`, avec les cas à couvrir en tête de fichier), infrastructure (`test_observability.py`, `test_executor.py`) ; faux objets du moteur ajoutés à `tests/fixtures.py`.

**Choix de conception du scaffold** :
- les événements sont des dataclasses figées, une par type (`RunStarted`, `LocalSearchDone`, …), qui portent des objets du domaine ; les enregistrements sont des dictionnaires de valeurs simples, construits par les collecteurs. Ainsi le moteur n'a rien à sérialiser, et les collecteurs choisissent ce qu'ils mesurent ;
- `LocalSearchDone` porte le coût avant et après la recherche locale, et le nom de l'opérateur : de quoi mesurer le taux de faisabilité par opérateur avant et après réparation (première expérience de l'étape 10) ;
- les destinations refusent les types numpy (`json` de la bibliothèque standard) au lieu de les convertir en silence ;
- les exceptions suivent la convention commune (le code qui lève formate le gabarit), en attendant D14.

Suite complète verte.

## 2026-11-19 — Étape 8b : collecteurs (Mély)

Fait (M), par Mély, branche `etape-8b-observabilite` : implémentation des quatre collecteurs de mesures dans `src/observability/collectors.py`, conformément à la décision D8.

Collecteurs implémentés

- `CostStatisticsCollector` : statistiques des coûts à chaque fin de génération (minimum, moyenne, médiane, maximum, écart-type, nombre d'individus faisables et moyennes des coûts décomposés).
- `DiversityCollector` : diversité génotypique et phénotypique, ainsi que nombre de coûts distincts. Fréquence de mesure configurable.
- `FeasibilityRateCollector` : taux de faisabilité avant et après le `LocalSolver`, regroupés par origine et opérateur, pour chaque génération et pour toute l'exécution.
- `SolverEffortCollector` : nombre d'appels et charge du solveur (nœuds, échecs, propagations et temps de résolution), par génération et cumulée.

Revue (Pascal, 2026-11-19). La logique des quatre collecteurs a été validée. Les tests existants passaient, mais plusieurs ajustements étaient nécessaires pour respecter les conventions de `CLAUDE.md`.

Corrections apportées

- Création de `InvalidPopulationError`, dérivée de `CollectorError`, et ajout d'un message centralisé dans `CollectorMessages`. Les collecteurs de coûts et de diversité lèvent maintenant la même exception lorsqu'une population est vide ou contient un individu non évalué.
- Conservation de `total_min` et `total_max` en `int`, plutôt qu'en `float`. Ajout d'assertions vérifiant explicitement ces types.
- Remplacement des listes de compteurs et des indices numériques dans `FeasibilityRateCollector` par la dataclass `_FeasibilityCounts`.
- Remplacement des listes de statistiques et des `getattr()` dans `SolverEffortCollector` par la dataclass `_SolverEffortCounts`, qui accumule directement les valeurs rapportées.
- Remise à zéro des compteurs des deux collecteurs avec état à la réception de `RunStarted`.
- Simplification de la diversité génotypique avec `Counter` et `frozenset`, sans tenir compte de la permutation des employés, et de la diversité phénotypique avec `grid.tolist()`.
- Nettoyage du code : suppression des conversions et commentaires inutiles, ajout d'annotations de types, organisation des imports et ajustements de mise en forme.

Tests

- 24 tests unitaires des collecteurs réussis avec Python 3.13 après les corrections.
- Vérification des types `int` de `total_min` et `total_max`.
- Les tests spécifiques aux populations invalides et à la remise à zéro entre deux exécutions restent à ajouter.

Reste avant la fusion : ajouter les tests spécifiques manquants, compléter `TODO.md` et `TEAM.md`, relancer la suite complète et faire réviser les corrections dans la Pull Request.

## 2026-11-20 — Étape 8b : seconde revue et fusion de la PR #8 (Pascal et Claude)

Seconde relecture de la PR #8 après les corrections de Mély (commit `56f823f`), puis fusion dans `main` (`979fd57`).

- Les points « à corriger » de la première revue (2026-11-19, commentaire sur la PR) sont tous réglés : `InvalidPopulationError` avec son gabarit dans `CollectorMessages`, même règle dans les deux collecteurs qui lisent la population ; `total_min` et `total_max` en `int` ; dataclasses `_FeasibilityCounts` et `_SolverEffortCounts` à la place des indices et des `getattr` ; remise à zéro au `RunStarted`.
- Les tests annoncés comme « restant à ajouter » dans l'entrée du 2026-11-19 ont été écrits sur la branche avant la fusion : populations vides ou non évaluées (les deux collecteurs) et remise à zéro entre deux exécutions (les deux collecteurs avec état). `tests.test_collectors` compte maintenant 28 tests.
- Les journaux de Mély avaient été poussés directement sur `main` (`0df9f44`, `3d65b08`) avant la fin de la PR ; ce commit les complète (cases de TODO.md et de TEAM.md) sans modifier son entrée.
- Détails mineurs laissés à sa discrétion, sans bloquer la fusion : espaces en fin de ligne dans les imports de `collectors.py`, lignes vides entre les classes, message `INVALID_POPULATION` sans espace réservé (par exemple `{generation}`) pour le diagnostic, `96` et `42` écrits en dur dans les nouveaux tests.

Suite complète verte sur `main` après la fusion.

## 2026-11-20 — Étape 5c : D12 tranchée, plan du modèle assoupli (Pascal et Claude)

**Décision D12 : deux fichiers.**
- `src/model/horaire_assoupli.mzn` (nouveau) : la couverture « au moins 1 » devient le compteur `violations_couverture`, et l'objectif `cout_penalise = cout_total + POIDS_COUVERTURE × violations_couverture`. C'est le modèle du pipeline : il minimise la même fonction de coût que `CostEvaluator.total`, avec le poids fourni par Python (`PenaltyWeights.coverage_violation`).
- `src/model/horaire.mzn` : le modèle original fourni, gardé **inchangé** comme référence (couverture dure). Il sert aux comparaisons (résolution complète, variante « peine de mort ») et reste la spécification d'origine du problème.

**Pourquoi deux fichiers plutôt qu'un modèle paramétré (`COUVERTURE_DURE: bool`)** : le modèle fourni reste intact et lisible tel quel, et chaque fichier a un seul objectif. Le prix : la logique commune existe en deux copies MiniZinc, à garder alignées (lien avec D13, à reprendre après 5c).

**Conséquence sur l'architecture** : le `SolverAdapter` reçoit le modèle à résoudre (Stratégie, D5) ; une variante décrit le fichier, le nom de son objectif et si elle attend le poids de la pénalité. La borne de coût du `LocalSolver` dépend de la variante : avec le modèle assoupli, elle porte sur `cout_penalise` et se pose dès que l'entrée n'a aucune violation structurelle.

Plan détaillé dans TODO.md, 5c. Prochaine tâche : scaffold et tests (Claude), puis le modèle, l'adaptateur et la borne (Pascal).

## 2026-11-20 — Étape 5c : scaffold et tests du modèle assoupli (Claude)

**Fait (C)**, branche `etape-5c-couverture-souple` :
- `ProjectPaths` : `REFERENCE_MODEL_FILE` (`horaire.mzn`) et `RELAXED_MODEL_FILE` (`horaire_assoupli.mzn`) remplacent `MODEL_FILE` (sonde MiniZinc et test de fumée : modèle de référence).
- `solver.py` : `ModelVariant` (nom, fichier, objectif, `penalizes_coverage`) avec `parameters(weights)` en squelette ; `ModelVariants.REFERENCE` et `ModelVariants.RELAXED` ; `ModelObjective.PENALIZED_COST` ; `RelaxedModelNames` (`POIDS_COUVERTURE`, `violations_couverture`). Le `SolverAdapter` reçoit `model` (`RELAXED` par défaut) et `weights` ; `solve` résout encore le modèle de référence, en attendant l'implémentation.
- `local_search.py` : contrat de `cost_bound_constraints` selon la variante (docstring) ; le corps garde la règle d'avant 5c.
- `horaire_assoupli.mzn` : copie exacte de `horaire.mzn`, avec en tête la liste des changements à faire.
- Tests : `tests/test_relaxed_model.py` (nouveau, appelle MiniZinc : empreinte de `horaire.mzn`, optimum de bench_1 avec les deux modèles, validation croisée terme par terme sur quatre horaires fixés dont trois qui violent « au moins 1 », instance à couverture impossible, poids transmis par Python) ; `test_solver.py` (variantes et paramètres, sans MiniZinc ; modèle et poids de l'adaptateur) ; `test_local_search.py` (bornes du modèle assoupli, sans MiniZinc ; CP-SAT : plus d'UNSAT avec le modèle assoupli, l'ancien cas UNSAT passe au modèle de référence).

**État** : 12 tests rouges (7 échecs, 5 erreurs), tous les autres verts. Validés contre une implémentation de référence jetable, hors du dépôt : suite complète verte (416 tests).

**Découverte en validant** : dès qu'une variable porte `::add_to_output`, minizinc-python ne rend plus que les variables annotées. Le modèle assoupli doit donc annoter aussi les six variables de décision, sinon le `SolverAdapter` échoue (`'Solution' object has no attribute 'debut'`). Ajouté à l'en-tête du modèle et à TODO.md.

**À surveiller** : avec l'implémentation jetable, la suite complète a pris environ deux fois plus de temps (116 s au lieu de 56 s), le modèle assoupli devenant celui du pipeline. C'est le point « effet du poids sur la propagation et le temps de CP-SAT » du plan : à mesurer par module.

**Limite connue** : `test_relaxed_model_improves_a_coverage_violation_with_two_freed_employees` passe déjà avec le modèle de référence sur bench_1 (deux employés libérés sur trois suffisent à couvrir). Le cas qui distingue vraiment les deux modèles (bench_3 et bench_5, 6 cas sur 6 en UNSAT le 2026-11-13) relève des mesures prévues au plan.

## 2026-11-20 — Étape 5c : modèle assoupli comparé au modèle de référence en résolution complète (Pascal et Claude)

**Fait (P)** : `horaire_assoupli.mzn` écrit par Pascal (paramètre `POIDS_COUVERTURE`, compteur `violations_couverture`, objectif `cout_penalise`, annotations `::add_to_output`). Correctif après revue : l'annotation se place avant le `=` (`var int: x :: add_to_output = expr;`) ; placée après l'expression, elle annote l'expression, MiniZinc l'accepte sans rien dire et la variable n'est pas rendue. La validation croisée Python / MiniZinc (`TestCrossValidation`) est verte : mêmes `violations_couverture`, `cout_total` et `cout_penalise` que `CostEvaluator` sur les quatre horaires.

**Mesures (C)** : résolution complète des deux modèles sur les cinq bench, CP-SAT, poids de 1 000 000. Scripts jetables, hors du dépôt.

Série 1 — 1 thread, graine 0, 120 unités déterministes (les conditions du pipeline, D7 et D10) :

| Bench | Référence : objectif (violations) | Assoupli : objectif (violations) |
|---|---|---|
| bench_1 | 94, optimum prouvé (0) | 94, optimum prouvé (0) |
| bench_2 | 38 (0) | 38 (0) |
| bench_3 | 9 000 080 (0) | 93 000 118 (45) |
| bench_4 | aucune solution (budget épuisé, statut `UNKNOWN`, pas un UNSAT) | 154 000 178 (73) |
| bench_5 | 32 000 343 (0) | 151 000 463 (96) |

Série 2 — 8 threads, au plus 180 s de temps mural ; tous les optimums sont prouvés :

| Bench | Optimum | Référence : 1ʳᵉ solution / optimum prouvé | Assoupli : 1ʳᵉ solution / optimum prouvé |
|---|---|---|---|
| bench_1 | 94 | 0,16 s / 0,18 s | 0,14 s / 0,16 s |
| bench_2 | 38 | 0,14 s / 1,1 s | 0,16 s / 0,9 s |
| bench_3 | 16 | 0,45 s / 2,0 s | 0,41 s / 1,5 s |
| bench_4 | 10 | 0,55 s / 1,6 s | 0,58 s / 2,0 s |
| bench_5 | 267 | 0,77 s / 48,9 s | 0,83 s / 40,7 s |

**Conclusions**
- Le modèle assoupli prouve les mêmes optimums que le modèle de référence, sans violation à l'optimum. En multithread, les temps sont équivalents : écarts de −20 % à +25 % dans les deux sens, sur une seule mesure chacun, donc du bruit.
- En monothread et à budget égal, l'assoupli est nettement moins bon sur bench_3 à bench_5 : la contrainte dure élimine d'emblée les horaires qui laissent une cellule vide, la pénalité ne propage rien. Ses premières solutions ont beaucoup de violations (88 000 097 contre 21 000 083 sur bench_3, en multithread aussi) ; avec 8 threads, CP-SAT les élimine en moins d'une seconde, avec 1 thread il n'y arrive pas en 120 unités. En contrepartie, il trouve toujours une solution (bench_4 : aucune avec la contrainte dure).
- Le modèle de référence reste le bon outil pour une résolution complète ; il est gardé pour cela (D12).
- La mesure décisive reste celle du `LocalSolver` (1 thread, 2 employés libérés, bench_3 et bench_5 ; 6 cas sur 6 en UNSAT avec la contrainte dure le 2026-11-13), où la borne de coût élague dès le départ. À faire quand `solve` et la borne seront écrits.
- Ne pas baisser le poids pour compenser : la lenteur vient de l'absence de propagation, pas de la taille du poids ; un poids plus faible ferait seulement préférer des violations à une sous-couverture coûteuse.

## 2026-11-20 — Étape 5c : `SolverAdapter` et borne du `LocalSolver` validés ; mesure sur bench_5 (Pascal, revue par Claude)

**Fait (P)** : `ModelVariant.parameters`, `SolverAdapter.solve` (résout `self.model.path`, transmet `POIDS_COUVERTURE`), `MiniZincLocalSolver.cost_bound_constraints` selon la variante, docstring du module.

**Correctifs après revue**
- `solve` : le poids était ajouté au modèle comme une nouvelle déclaration (`add_string("var int POIDS_COUVERTURE = …")`) : erreur de syntaxe, et, corrigée, une double déclaration d'une variable de décision. Le paramètre déjà déclaré reçoit une valeur, comme les données de l'instance : `minizinc_instance[name] = value`.
- Borne : d'abord posée seulement pour une entrée faisable, avec `coverage_cost`, puis conditionnée à `coverage_violations == 0`. La règle de D12 est `structural_violations == 0`, avec `total` comme borne : une entrée qui viole « au moins 1 » est une solution du sous-problème assoupli, et `coverage_cost` seul (160 au lieu de 21 000 160 dans le test) rendrait ce sous-problème insatisfiable. L'objectif vient de `self.adapter.model.objective`, plus de nom écrit en dur.

**Mesure décisive (C) : le `LocalSolver` sur bench_5**, le cas qui a motivé D12. Initialisation de 6 individus tirés au hasard, 2 employés libérés, 1 thread, 5 unités par appel (ancien `test_unrepairable_samples_enter_unchanged_on_bench_5`) :

| Appel | Issue | Coût total avant (violations) | Coût total après (violations) |
|---|---|---|---|
| 1 | solution | 101 000 373 (54) | 86 000 396 (47) |
| 2 | solution | 86 000 399 (55) | 71 000 398 (44) |
| 3 | solution | 84 000 362 (40) | 55 000 387 (30) |
| 4 | budget épuisé | 80 000 359 (45) | inchangé |
| 5 | solution | 83 000 362 (43) | 64 000 375 (29) |
| 6 | solution | 76 000 396 (44) | 66 000 411 (46) |

Avec la contrainte dure : 6 UNSAT sur 6 (2026-11-13). Avec le modèle assoupli : 5 améliorations sur 6, coût total en baisse de 12 à 35 %, plus aucun UNSAT. L'appel 6 finit avec deux violations de plus mais un coût total plus bas : c'est bien le coût pénalisé qui est minimisé. L'appel 4 épuise son budget sans solution alors que l'entrée en est une : CP-SAT ne la reçoit pas comme point de départ. Piste pour plus tard : la lui fournir comme indice (*warm start*).

**Test d'initialisation revu (C)** : le test bench_5 de `TestInitializationWithCpSat` prenait 55 s, parce que les sous-problèmes autrefois insatisfiables dès l'aplatissement sont maintenant vraiment résolus. Son idée de départ (sans solution à cause de la contrainte dure) ne tenait plus ; il passait encore seulement grâce à l'appel 4. Remplacé par deux tests, sur 3 individus et 1 unité :
- `test_reference_model_leaves_unrepairable_samples_unchanged_on_bench_5` : avec le modèle de référence, au moins un UNSAT, l'horaire tiré gardé tel quel (1,4 s) ;
- `test_relaxed_model_improves_samples_on_bench_5` : avec le modèle assoupli, aucun UNSAT et au moins un horaire strictement amélioré (3,5 s ; les trois le sont).
- `assert_common_invariants` vérifie la borne selon la variante : `total` jamais pire dès que l'horaire tiré n'a pas de violation structurelle (assoupli), `coverage_cost` jamais pire s'il est faisable (référence).

Suite complète verte : 417 tests en 67 s (116 s avant la révision du test, 56 s avant 5c).

Sortie JSON du modèle assoupli : `violations_couverture` et `cout_penalise` ajoutés (Pascal) ; correctif après revue, les virgules entre les champs, que `json.loads` refusait (minizinc-python n'utilise pas cet item `output`, les tests ne pouvaient pas le voir). Vérifiée sur bench_1 : `Cout` = 94, `violations_couverture` = 0, `cout_penalise` = 94. L'en-tête du fichier, qui liste les changements de 5c, est gardé tel quel.

**Reste pour 5c** : la même mesure sur bench_3 ; suivi (`docs/PROBLEME.md`, `docs/PROJECT_STRUCT.md`, arbre de CLAUDE.md).

## 2026-11-20 — Étape 5c : mesure du `LocalSolver` sur bench_3 (Claude)

Même protocole que le 2026-11-13 : graine 0, 6 horaires tirés au hasard par `RandomBlockInitializer`, 2 employés libérés, CP-SAT 1 thread, 5 unités déterministes par appel. Les deux modèles sur les mêmes horaires tirés.

| Appel | Coût total tiré (violations) | Référence | Assoupli : coût après (violations) | Baisse |
|---|---|---|---|---|
| 1 | 40 000 090 (16) | UNSAT | 25 000 085 (9) | 37 % |
| 2 | 45 000 067 (19) | UNSAT | 31 000 054 (9) | 31 % |
| 3 | 99 000 051 (39) | UNSAT | 51 000 047 (17) | 48 % |
| 4 | 57 000 114 (23) | UNSAT | 37 000 068 (11) | 35 % |
| 5 | 88 000 123 (39) | UNSAT | 47 000 097 (20) | 47 % |
| 6 | 83 000 110 (35) | UNSAT | 51 000 090 (22) | 39 % |

- Modèle de référence : 6 UNSAT sur 6, comme le 2026-11-13 (2,5 s en tout).
- Modèle assoupli : 6 solutions sur 6 (budget épuisé, optimalité non prouvée), coût total en baisse de 31 à 48 %, violations de couverture divisées par deux environ ; aucune violation structurelle (24,4 s en tout, 3,3 à 4,0 s par appel).
- Avec bench_5 (5 améliorations sur 6, un budget épuisé sans solution), D12 atteint son objectif : le `LocalSolver` améliore les horaires qui violent « au moins 1 », au lieu de les rendre inchangés.
- Coût : chaque appel utilise maintenant son budget (environ 4 s pour 5 unités), au lieu d'échouer en quelques millisecondes. Le budget par appel devient un vrai paramètre d'expérience (étape 10), à mettre en balance avec le nombre d'appels par génération (NR, NM).

Toutes les cases de 5c sont cochées, sauf le suivi de la documentation.
