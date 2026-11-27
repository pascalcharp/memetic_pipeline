# Mémétique contre individus aléatoires + LocalSolver sur bench_2, population 18 (étape 10d)

## 1. Question

Les opérateurs de variation font-ils mieux que des individus tirés au hasard, à budget égal d'appels au LocalSolver ? C'est le premier témoin de la « première expérience, avant la campagne » (TODO, étape 10). Il répond à l'objectif 1 de l'étape 10 : battre le hasard.

## 2. Protocole

- Instance : bench_2 (optimum prouvé 38).
- Réglages retenus par Mély (PR #15) : population 18, 26 générations, NR = 6, NM = 6, stagnation 10, élite 1, tournoi 2, voisinage 1, 5 unités déterministes par appel, recherche locale à l'initialisation. Graines 0 à 20.
- **Mémétique** (`experiments/config/bench2_memetique_pop18/`) : `uniform_gene` et `shift_start`. Ce sont les mêmes réglages que `bench2_pop18`, relancés pour mesurer le temps déterministe et l'effort par génération.
- **Témoin** (`experiments/config/bench2_temoin_aleatoire/`) : `random_genome` pour le croisement et la mutation. Ces opérateurs ignorent leurs entrées et tirent des génomes selon la loi de l'initialisation. Le reste de la boucle est identique : population, sélections, restarts, LocalSolver, graines. Chaque génération soumet donc 2 × NR + NM = 18 individus au solveur dans les deux séries.
- Code : commit `9535bc7`, copie de travail propre pour les 42 exécutions. Budget réalisé : 486 à 520 appels par exécution, restarts compris.
- Mesure de l'effort : `solver_effort_by_generation` (appels, propagations, temps déterministe de chaque génération), cumulé. L'effort « avant 38 » est celui de la fin de la première génération où 38 est atteint, à une génération près (18 appels).

Analyse : `python experiments/analysis/analyze_random_witness.py`.

## 3. Meilleur coût en fonction des appels cumulés

Q1 / médiane / Q3 sur les 21 graines. Un coût de 2 000 000 ou plus signale un horaire qui viole « au moins 1 ».

| Appels | Mémétique | Témoin |
|---:|---:|---:|
| 18 (initialisation) | 2 000 049 / 2 000 055 / 4 000 050 | 2 000 049 / 2 000 055 / 4 000 050 |
| 50 | 40 / 43 / 46 | 46 / 2 000 045 / 2 000 055 |
| 100 | 38 / 38 / 39 | 45 / 55 / 2 000 043 |
| 150 | 38 / 38 / 38 | 44 / 54 / 58 |
| 200 | 38 / 38 / 38 | 43 / 47 / 56 |
| 300 | 38 / 38 / 38 | 41 / 43 / 54 |
| 486 | 38 / 38 / 38 | 41 / 42 / 45 |

Les deux séries partent du même point : même graine, même initialisation. Le mémétique atteint l'optimum en médiane avant 100 appels. Le témoin, lui, a encore la moitié de ses exécutions infaisables à 50 appels et finit à 42 en médiane.

## 4. Effort avant d'atteindre 38

| Indicateur | Mémétique | Témoin |
|---|---:|---:|
| Exécutions qui atteignent 38 | 21/21 | 1/21 |
| Succès en 100 / 200 / 520 appels | 14 / 20 / 21 | 0 / 1 / 1 |
| Appels avant 38 (médiane [Q1 ; Q3]) | 72 [54 ; 126] | 180 (une seule exécution) |
| Propagations avant 38 | 1,19 M [1,08 ; 1,57] | 4,72 M (une seule) |
| Temps déterministe avant 38 | 0,32 [0,30 ; 0,45] | 1,30 (une seule) |
| Meilleur coût final (min ; médiane ; max) | 38 ; 38 ; 38 | 38 ; 42 ; 57 |

**Test de Wilcoxon apparié** (rangs signés, loi exacte, témoin moins mémétique). Une exécution qui n'atteint pas 38 est censurée au-delà du budget. Pour les appels, les propagations et le temps déterministe avant 38, le témoin dépense plus que le mémétique **dans les 21 paires de graines** : W+ = 231, p = 9,5 × 10⁻⁷.

## 5. Pourquoi : la faisabilité vient des opérateurs

Taux de faisabilité avant et après le LocalSolver, cumulé sur les 21 exécutions :

| Origine | Mémétique avant → après | Témoin avant → après |
|---|---:|---:|
| Initialisation | 0 % → 0,5 % | 0 % → 0,5 % |
| Croisement | 29 % → 51 % | 0 % → 0,9 % |
| Mutation | 64 % → 72 % | 0 % → 0,9 % |
| Restart | 0 % → 0,8 % | 0 % → 0,5 % |

Un génome aléatoire viole « au moins 1 » presque toujours. Avec un voisinage de 1, la recherche locale n'en répare que 0,5 à 0,9 %, comme la PR #15 l'avait prévu (0,53 %). Les enfants du mémétique héritent de quarts qui couvrent déjà la demande. Une fois qu'un individu faisable existe, la moitié des enfants du croisement et les trois quarts des mutants le sont aussi après la recherche locale.

## 6. Conclusion

Sur bench_2, avec les réglages de Mély et à budget égal d'appels au LocalSolver, **les opérateurs du mémétique battent nettement des individus aléatoires suivis de la même recherche locale** :
- 21 succès sur 21 contre 1 sur 21 ;
- effort avant l'optimum plus faible dans toutes les paires de graines (p < 10⁻⁶) ;
- environ 4 fois moins de temps déterministe avant l'optimum.

C'est cohérent avec la première série, faite avec les réglages par défaut (population 6, 80 générations, `bench2_temoin_redemarrages.md`) : 21/21 contre 1/21.

Limites :
- Une seule instance.
- Un voisinage de 1 désavantage particulièrement le témoin : une recherche locale plus large réparerait mieux les génomes aléatoires, mais trouverait aussi l'optimum seule dès V3 (PR #15). Les opérateurs n'y joueraient alors plus de rôle.
- L'effort avant 38 est connu à une génération près.

Suite : le témoin fort de 10e, une recherche locale itérée (1+1) avec acceptation « pas pire ». Il garde l'hérédité par la mutation, mais n'a ni population ni croisement.
