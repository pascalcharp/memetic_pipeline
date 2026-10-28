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
