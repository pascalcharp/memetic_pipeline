# TASKS — Expériences et amélioration de l'algorithme

Le cœur est écrit : modèle, algorithme génétique, recherche locale, moteur mémétique, observabilité et driver d'expériences. Le plan qui a servi à le concevoir et à le programmer, avec les décisions de conception D1 à D14, est archivé dans [`docs/archive/TODO.md`](docs/archive/TODO.md). Ce fichier-ci porte le travail qui reste à faire, **rangé par ordre de priorité**.

Légende :
- `[ ]` à faire · `[~]` en cours · `[x]` validé (tests verts)
- **(C)** Claude écrit · **(P)** le membre responsable écrit, Claude vérifie · **(C→P)** Claude scaffolde, le membre responsable implémente

Règles : celles de [`CLAUDE.md`](CLAUDE.md) et de [`TEAM.md`](TEAM.md).
- **Une tâche à la fois**, par personne et par branche.
- **Branches :** chaque tâche a sa branche `etape-<identifiant>-<sujet>`.
- **Fusion :** on fusionne par *pull request* quand la suite complète est verte.
- **Journaux :** une entrée dans `DEVLOG.md` par tâche. Chaque exécution d'expérience a son entrée dans `experiments/EXPLOG.md` ; on ne lance pas une série avec une copie de travail modifiée.
- **Identifiants :** les tâches gardent leur identifiant d'origine (10h, 10j…), cité dans les branches, le DEVLOG, l'EXPLOG et les rapports.

Objectifs (Pascal, 2026-11-21) : montrer, sur au moins quelques instances, que le mémétique (1) bat une marche aléatoire, et (2) réduit la charge du solveur par rapport à CP-SAT seul. L'effort se mesure en propagations ou en temps de résolution, jamais en temps réel.

---

## Où on en est (2026-11-27)

- **bench_2** : le mémétique trouve l'optimum (38).
  - Il bat nettement les individus aléatoires réparés par la recherche locale (10d : 21 graines sur 21 contre 1 sur 21).
  - Il bat aussi la recherche locale itérée (10e, sur la branche `etape-10e-temoin-fort` : 21 sur 21 contre 5 sur 21).
  - Il bat CP-SAT seul.
- **bench_3** : le mémétique ne trouve jamais l'optimum (16). Il bat CP-SAT seul à 1 thread (10g), mais ce témoin est faible.
  - CP-SAT avec son portefeuille de stratégies (8 threads, un seul essai) trouve 16 vers 31 s et consomme 318 s de CPU en tout ; la configuration économique du mémétique dépense environ 140 s et finit à 38.
  - La recherche locale est le goulot, et les exécutions sont tronquées à 26 générations (voir DEVLOG du 2026-11-27).
- **Rapports :**
  - réglages de Mély sur bench_2 et bench_3 : [`experiments/analysis/synthese_bench2_bench3.md`](experiments/analysis/synthese_bench2_bench3.md) ;
  - témoin aléatoire : [`bench2_temoin_aleatoire.md`](experiments/analysis/bench2_temoin_aleatoire.md) ;
  - CP-SAT seul : [`bench3_cpsat_alone.md`](experiments/analysis/bench3_cpsat_alone.md).

Récit visé pour le rapport : sur bench_2, le croisement fait la différence (le croisement est un compromis entre la distance aux parents et la réparabilité). Sur bench_3, la limite devient la recherche locale : on montre de combien la renforcer comble l'écart avec le portefeuille de CP-SAT.

---

## Priorité 1a — 10h : protocole de Mély sur bench_4 et bench_5 **(C)** — Pascal et Claude
Décision de Pascal (2026-11-26) : Mély prend une pause, on termine son protocole. Mené en parallèle de 10j, avec qui il partage la calibration et le script d'analyse.

Référence : `experiments/analysis/synthese_bench2_bench3.md` (sections 15 et 17).

Coût : une exécution de bench_3 avec le voisinage 1 prend environ 400 s de temps réel (médiane), et le protocole complet de Mély compte environ 460 exécutions par instance. bench_4 (8 × 4 × 44) et bench_5 (8 × 5 × 48) sont plus gros : le protocole complet coûterait plusieurs centaines d'heures de calcul. On le **réduit** aux facteurs qui ont changé d'une instance à l'autre. On ne refait les autres que si les résultats contredisent bench_2 et bench_3.
- [ ] **Lanceur de séries** (`experiments/drivers/`) :
  - exécuter un répertoire de configurations en parallèle, avec le nombre de processus en paramètre. Par défaut 4, un par cœur performant, pour ne pas fausser `solveTime` ;
  - une entrée d'EXPLOG.md par exécution, sans écritures concurrentes ;
  - reprise possible : sauter les configurations qui ont déjà un résultat ;
  - générateur des configurations d'une série (instance × réglage × graines) ;
  - tests.
- [ ] **Calibration :**
  - la configuration économique, graine 0, sur bench_4 et bench_5 : temps réel, `solveTime`, propagations, coût ;
  - les témoins CP-SAT seul sur les deux instances : 1 thread (10g : deux modèles, 3 graines) et portefeuille (10j) ;
  - estimer le coût de chaque série et fixer le nombre de graines : 21 si c'est abordable, sinon 11, noté dans EXPLOG.md.
- [ ] **Configurations recommandées**, sur les deux instances :
  - économique : population 18, 26 générations, NR/NM 3/12, voisinage 1, budget 5, stagnation 10, `shift_start`, recherche locale initiale ;
  - qualité : NR/NM 6/6, voisinage 2, budget 10 ;
  - la candidate jamais testée : NR/NM 3/12, voisinage 2, budget 10 (section 17).
- [ ] **Facteurs dépendants de l'instance** (section 15) :
  - voisinage {1, 2} × budget {5, 10} ;
  - recherche locale initiale {vraie, fausse}, avec la configuration économique.
- [ ] **Facteurs stables sur bench_2 et bench_3** (ratio NR/NM, stagnation, mutation, population) : non refaits, sauf contradiction ci-dessus.
- [ ] **Comparaison avec CP-SAT seul à effort égal :** elle utilise le script d'analyse généralisé en 10j, et compare aux deux témoins (1 thread et portefeuille).
- [ ] **Rapports :** `experiments/analysis/bench4_*.md` et `bench5_*.md`, et la synthèse mise à jour (bench_2 à bench_5). EXPLOG.md, DEVLOG.

## Priorité 1b — 10j : témoin fort, CP-SAT avec son portefeuille **(C)** — Pascal et Claude
Décision de Pascal (2026-11-27). Le témoin de 10g (CP-SAT 1 thread) est faible, parce qu'il est privé du portefeuille, dont la recherche à grand voisinage. Il faut mesurer la vraie barre avant de juger une amélioration.
- [ ] **Driver `run_cpsat_alone.py` :**
  - clé facultative `threads`, 1 par défaut ;
  - effort mesuré en **temps CPU total** du processus enfant (`resource.getrusage(RUSAGE_CHILDREN)`, utilisateur + système), à côté des propagations et du `solveTime` ;
  - vérifier d'abord si les propagations rapportées couvrent tous les workers ou un seul ;
  - tests.
- [ ] **Portefeuille monothread :** vérifier s'il en existe un, vraiment monothread et déterministe, par MiniZinc. `interleave_search:true` a encore utilisé environ 4 cœurs, parce que `num_workers:8` l'emporte sur `-p 1`. Si on en trouve un, l'ajouter comme troisième témoin.
- [ ] **Configurations :**
  - bench_2 et bench_3, modèle de référence, 8 threads ;
  - 5 répétitions, parce que le portefeuille n'est pas déterministe ;
  - limite en temps assez large pour la preuve ;
  - bench_4 et bench_5 avec 10h.
- [ ] **Analyse :** comparer au mémétique à effort CPU égal.
  - L'effort du mémétique est le `solveTime` cumulé de sous-problèmes monothread, donc environ son temps CPU de solveur. Le temps hors solveur (lancement, compilation) est exclu des deux côtés.
  - Généraliser `analyze_bench3_cpsat_alone.py`, avec l'instance, l'optimum et le témoin en paramètres.
- [ ] **Rapport :** `experiments/analysis/temoin_portefeuille.md`. EXPLOG.md, DEVLOG.

## Priorité 2 — 10k : recherche locale renforcée sur bench_3 **(C)** — Pascal et Claude ; après 10j
**Constats :**
- La recherche locale est le facteur le plus fort des séries de Mély : passer du voisinage 1 au voisinage 2 fait baisser le coût de 41 à 23.
- Les voisinages 3 et 4 s'effondrent, parce que CP-SAT monothread ne résout plus les sous-problèmes dans le budget.
- Les exécutions sont **tronquées** : la dernière amélioration arrive en médiane aux générations 21 à 24 sur 26.

**Protocole :**
- On part de la configuration économique, avec 21 graines.
- On teste **un levier à la fois** et on le compare à la base par un test de Wilcoxon apparié sur les graines (coût final, effort pour atteindre un coût).
- On situe chaque résultat par rapport à la barre de 10j.
- Chaque levier comprend ses tests, son entrée au catalogue s'il est configurable, sa série et son rapport.

**Leviers, dans l'ordre :**
- [ ] **Base prolongée :** la configuration économique avec 80 générations, et l'effort par génération enregistré. Ça donne la courbe coût / effort au-delà de 26 générations et tranche la question de la troncature.
- [ ] **Arrêt à l'effort :** un `TerminationCriterion` sur l'effort cumulé (propagations ou temps déterministe) au lieu de `GenerationLimit`. Les budgets s'expriment comme ceux des témoins.
- [ ] **Modèle dur sur les individus faisables :**
  - `LocalSolver` choisit le `ModelVariant` de référence quand l'individu n'a aucune violation de couverture ;
  - le sous-problème reste satisfiable, puisque l'individu courant en est une solution ;
  - le modèle assoupli ne sert plus qu'à la réparation des enfants infaisables ;
  - mesurer la part des appels faits sur des individus faisables.
- [ ] **Voisinages structurés :** nouveau rôle `neighborhood` au catalogue, avec `RandomEmployeesNeighborhood` comme base.
  - Fenêtre temporelle : libérer les employés dont le quart chevauche une plage de périodes. Le design de `TimeWindowNeighborhood` est dans l'archive, étape 5b : choix de la fenêtre, plafond, coût par période à exposer dans `evaluation.py`.
  - Guidé par la couverture : libérer les employés présents sur les périodes les plus mal couvertes.
  - Taille adaptative : augmenter k en cas de stagnation, le ramener en cas d'amélioration.
- [ ] **Portefeuille dans les sous-problèmes :**
  - `threads` > 1 dans `SolverAdapter`, avec l'effort compté en CPU ;
  - ça rendrait peut-être les voisinages 3 et 4 utilisables ;
  - reproductibilité à vérifier, sinon la noter dans le rapport.
- [ ] **Petites idées**, si le temps le permet :
  - briser la symétrie entre les employés libérés, qui sont interchangeables ;
  - partir de la solution courante avec `warm_start` (prise en charge par `fzn-cp-sat` à vérifier).
- [ ] **Synthèse :** `experiments/analysis/bench3_recherche_locale.md`. Reprendre ensuite la meilleure combinaison sur bench_2, pour vérifier qu'elle ne dégrade rien.

## Priorité 3 — 10i : explorer d'autres croisements **(C)** — proposition de Pascal, 2026-11-26 ; après 10k
**Intuition de Pascal :** c'est le croisement qui reste à exploiter pour tirer plus de l'algorithme.

**Cadre :** la thèse de 10f, selon laquelle le croisement est un compromis entre la **distance** aux parents et la **réparabilité**.
- Un seul croisement existe (`uniform_gene`), et il ignore la permutation des employés (limite D3).
- Chaque nouveau croisement entre au catalogue et se compare à `uniform_gene` sur bench_2 et bench_3, avec la configuration économique (21 graines).
- Critères de comparaison : coût, effort cumulé, et distance et réparabilité des enfants.

**Travail, dans l'ordre :**
- [ ] **Mesure d'abord :** distance des enfants à leurs parents, et faisabilité avant et après la recherche locale, par opérateur. C'est la deuxième expérience de 10f, et le critère qui permet de comparer les croisements autrement que par le coût final.
- [ ] **Croisement avec alignement des employés (D3) :**
  - apparier les employés des deux parents avant l'échange uniforme, par une affectation de coût minimal sur la distance des grilles employé × période ;
  - les enfants restent plus près de leurs deux parents ;
  - c'est le croisement le plus simple qui corrige un défaut connu.
- [ ] **Croisement glouton guidé par la couverture :**
  - les employés sont interchangeables, donc on dispose de 2E gènes chez les deux parents ;
  - on en choisit E, un à un, en minimisant le coût de couverture ;
  - ce croisement exploite la structure du problème.
- [ ] **Croisement temporel :**
  - pour chaque employé, une coupe dans le temps : le début du quart vient d'un parent, la fin de l'autre ;
  - la recherche locale répare ensuite ;
  - c'est plus fin que l'échange de gènes entiers.
- [ ] **Recombinaison optimale par CP :**
  - fixer ce que les parents alignés ont en commun, et laisser CP-SAT choisir le reste parmi les valeurs des parents ;
  - le croisement et la recherche locale fusionnent : comparer à effort cumulé égal, pas par appel ;
  - en dernier, parce que c'est le plus coûteux à écrire.
- [ ] **Croisement par interpolation :**
  - c'est un bouton de réglage de la distance ;
  - le design est dans l'archive (7c) et dans 10f.
- [ ] Pour chaque croisement : tests, catalogue, AVAILABLE_STRATEGIES.md, série, rapport.

---

## En attente (décision de Pascal)

- **10e et 10f**, sur la branche `etape-10e-temoin-fort`.
  - 10e, le témoin « recherche locale itérée (1+1) », est exécutée.
  - 10f, le croisement comme compromis entre distance et réparabilité, est planifiée.
  - Pas de PR pour l'instant (2026-11-27). À sa fusion, ses sections iront ici, et le TODO de la branche ira à l'archive.
- **Série « population » de Xavier** (`experiments/config/xavier_bench_c*.json`, 500 configurations dont 100 exécutées) : Pascal en discute avec Xavier.

## Plus tard (reporté depuis l'archive)

Le détail de chaque tâche est dans [`docs/archive/TODO.md`](docs/archive/TODO.md).
- [ ] Consigner les versions de MiniZinc et de CP-SAT dans le fichier de résultats (suite de 12-0).
- [ ] README : construction Docker, lancement des tests, lancement des expériences (ancienne étape 11).
- [ ] 10b : `CostDistributionCollector`, qui donne la distribution des coûts de la population par génération.
- [ ] Variantes d'encodage (D1, D3) : `DirectEncoding`, `SortedBlockEncoding`.
- [ ] `BlockBoundaryMutation` : une amplitude calculée à partir des contraintes du quart (7b).
- [ ] Pénalité (étape 4) contre peine de mort (étape 8), sur les mesures de faisabilité.
- [ ] Si l'aplatissement par MiniZinc domine le temps : `CpSatApiAdapter`, qui parle directement à OR-Tools (ancienne étape 10a).
- [ ] Décisions ouvertes :
  - D13, la redondance entre `horaire.mzn` et le pipeline ;
  - D14, les exceptions qui construisent leur propre message ;
  - D9, MongoDB, reportée.
