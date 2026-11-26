# Mémétique contre recherche locale itérée (1+1) sur bench_2 (étape 10e)

## 1. Question

Le témoin fort garde ce qui fait marcher le mémétique dans la série 10d : l'**hérédité**, par la mutation, et le même LocalSolver. Il n'a ni population, ni croisement, ni sélection des parents, ni restart. On part d'un individu, on le mute (`shift_start`), on passe l'enfant au LocalSolver (voisinage 1), et on garde l'enfant s'il n'est **pas pire**. À coût égal, l'enfant remplace le parent, pour pouvoir se déplacer sur les plateaux. La population et le croisement apportent-ils quelque chose de plus ?

## 2. Protocole

- Instance : bench_2 (optimum prouvé 38), graines 0 à 20.
- **Témoin** (`experiments/config/bench2_ils/`) : population 1, NR = 0, NM = 1, 519 générations (1 + 519 = 520 appels), stagnation 1000 (aucun restart). Stratégies : mutation `shift_start`, sélection des survivants `plus` avec `prefer_newest` (nouveau rôle au catalogue, étape 10e). Commit `23f69d6`, copie de travail propre.
- **Mémétique** : la série `bench2_memetique_pop18` de 10d (population 18, 26 générations, NR = NM = 6, 486 à 520 appels, commit `9535bc7`).
- Comparaison au même nombre d'appels cumulés au LocalSolver, avec la même analyse qu'en 10d. Les deux séries utilisent la même mutation et le même LocalSolver.

Analyse : `python experiments/analysis/analyze_iterated_local_search.py`.

## 3. Meilleur coût en fonction des appels cumulés

Q1 / médiane / Q3 sur les 21 graines (2 000 000 ou plus : horaire qui viole « au moins 1 ») :

| Appels | Mémétique | (1+1) |
|---:|---:|---:|
| 18 | 2 000 049 / 2 000 055 / 4 000 050 | 39 / 40 / 42 |
| 50 | 40 / 43 / 46 | 39 / 40 / 41 |
| 72 | 38 / 38 / 39 | 39 / 40 / 41 |
| 100 | 38 / 38 / 39 | 39 / 40 / 41 |
| 200 | 38 / 38 / 38 | 39 / 40 / 41 |
| 520 | 38 / 38 / 38 | 39 / 40 / 41 |

## 4. Effort avant d'atteindre 38

| Indicateur | Mémétique | (1+1) |
|---|---:|---:|
| Exécutions qui atteignent 38 | 21/21 | 5/21 |
| Succès en 100 / 200 / 520 appels | 14 / 20 / 21 | 5 / 5 / 5 |
| Appels avant 38, exécutions réussies (médiane [Q1 ; Q3]) | 72 [54 ; 126] | 6 [4 ; 7] |
| Temps déterministe avant 38, exécutions réussies | 0,32 [0,30 ; 0,45] | 0,015 [0,012 ; 0,020] |
| Meilleur coût final (min ; médiane ; max) | 38 ; 38 ; 38 | 38 ; 40 ; 43 |
| Dernière amélioration (appels, médiane ; max) | — | 7 ; 19 |
| Temps déterministe par appel (médiane) | 0,0031 | 0,00019 |
| Propagations sur toute l'exécution (médiane) | 6,3 M | 0,15 M |

**Test de Wilcoxon apparié** (témoin moins mémétique, exécutions qui n'atteignent pas 38 censurées au-delà du budget) : le (1+1) dépense plus que le mémétique avant 38 dans 16 paires sur 21, celles où il n'atteint jamais 38. Dans les 5 autres, il l'atteint bien plus vite. W+ = 216, p = 1,2 × 10⁻⁴ pour les appels, les propagations et le temps déterministe.

## 5. Lecture

**Le (1+1) descend très vite, puis reste bloqué.** Parti d'un seul individu réparé, il trouve un horaire faisable dès le 4ᵉ appel environ. Il est à 40 en médiane après 18 appels, quand le mémétique n'a pas encore fini son initialisation. Mais sa dernière amélioration survient au plus tard au 19ᵉ appel (médiane 7). Les 500 appels suivants ne changent plus rien, même en acceptant l'enfant à coût égal. Il atteint un optimum local du voisinage « décaler un quart + réoptimiser un employé », souvent à 39, 40 ou 41. Il n'en sort pas, parce que passer de 39 à 38 demande de modifier deux quarts à la fois.

**Le mémétique sort de ces optimums locaux.** Ses individus sont plus lents à devenir faisables (initialisation de 18 individus, puis quelques générations). Mais la population garde plusieurs horaires de coûts proches, et le croisement combine les quarts de deux parents. C'est un déplacement à plusieurs employés que la mutation suivie d'une recherche locale à un employé ne fait pas. Il atteint 38 dans 21 cas sur 21.

**Une réserve sur l'équité du budget.** À nombre d'appels égal, le (1+1) ne dépense presque rien après sa convergence : environ 16 fois moins de temps déterministe par appel, et 40 fois moins de propagations sur l'exécution. Au même temps déterministe que le mémétique avant 38 (0,32 en médiane), un (1+1) **avec redémarrages** pourrait relancer une vingtaine de descentes. Comme une descente sur quatre environ atteint 38 (5 sur 21), il pourrait faire aussi bien, ou mieux. Ce n'est pas mesuré : avec une population de 1, `EliteRestart` garde au moins un individu (`MIN_RESTART_ELITE_COUNT = 1`), donc un restart ne remplace rien. Le tester demanderait d'autoriser une élite de 0, le meilleur restant suivi par le moteur.

## 6. Conclusion

À budget égal d'**appels** au LocalSolver, le mémétique bat le témoin fort : 21 succès sur 21 contre 5 sur 21 (p = 1,2 × 10⁻⁴). La population et le croisement permettent de sortir des optimums locaux où la recherche (1+1) se bloque après une vingtaine d'appels. En revanche, le (1+1) est bien meilleur dans les tout premiers appels, et chacun de ses appels coûte beaucoup moins cher. À budget égal de **temps déterministe**, la comparaison avec un (1+1) qui redémarre reste à faire avant de conclure sur l'objectif 2 (réduire la charge du solveur).
