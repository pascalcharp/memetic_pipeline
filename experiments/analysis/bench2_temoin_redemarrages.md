# Mémétique contre redémarrages aléatoires sur bench_2 (étape 10d)

## 1. Question

Le mémétique fait-il mieux que le hasard, à budget égal d'appels au LocalSolver ? Premier témoin, le plus simple : les **redémarrages aléatoires**. À chaque appel, un génome aléatoire neuf passe par le même LocalSolver ; on garde le meilleur.

## 2. Protocole

- Instance : bench_2 (optimum prouvé 38).
- Deux séries de 21 exécutions (graines 0 à 20), 80 générations, réglages par défaut de l'assemblage : population 6, NR = 2, NM = 2, stagnation 10, élite 1, tournoi 2, voisinage 1, budget de CP-SAT de 5 unités déterministes par appel, recherche locale à l'initialisation.
- **Mémétique** (`experiments/config/bench2_memetique_ref/`) : `uniform_gene` et `shift_start`.
- **Témoin** (`experiments/config/bench2_temoin_redemarrages/`) : croisement et mutation `random_genome`. Ces opérateurs ignorent les parents et rendent des génomes aléatoires neufs. Tout le reste est identique : moteur, LocalSolver, évaluation, sélection, restarts, mesure. Les deux séries font donc le même nombre d'appels au LocalSolver par génération (2·NR + NM = 6), et seule la variation diffère.
- Code : commit `c760577`, copie de travail propre pour les 42 exécutions.
- Le mémétique relancé redonne exactement la série `bench2_seuil` du 23 novembre (statistiques identiques pour les 21 graines). La réutilisation du modèle (12-0) et le journal du solveur (temps déterministe, 10d) ne changent donc pas les résultats.

Analyse : `python experiments/analysis/analyze_random_restarts.py`.

## 3. Succès

| Générations G | 2 | 4 | 6 | 8 | 10 | 15 | 20 | 30 | 40 | 60 | 80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mémétique : graines à 38 | 1 | 6 | 8 | 11 | 11 | 12 | 14 | 17 | 18 | 19 | 21 |
| Témoin : graines à 38 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

| Indicateur | Mémétique | Témoin |
|---|---:|---:|
| Optimum 38 atteint en 80 générations | 21/21 | 1/21 |
| Génération du succès (min ; médiane ; max) | 2 ; 8 ; 68 | 9 (une seule graine) |
| Meilleur coût final (min ; médiane ; max) | 38 ; 38 ; 38 | 38 ; 42 ; 54 |
| Première génération avec un horaire faisable (médiane) | 2 | 11 |

Meilleur coût de la population (médiane sur les graines). Un coût de 2 000 000 ou plus signale un horaire qui viole « au moins 1 » (pénalité de couverture du modèle assoupli) :

| G | 2 | 4 | 8 | 15 | 20 | 30 | 40 | 60 | 80 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Mémétique | 42 | 39 | 38 | 38 | 38 | 38 | 38 | 38 | 38 |
| Témoin | 2 000 066 | 2 000 047 | 2 000 040 | 55 | 54 | 45 | 45 | 43 | 42 |

## 4. Effort cumulé du solveur (80 générations)

Médiane [Q1 ; Q3] sur les 21 exécutions :

| Mesure | Mémétique | Témoin | Témoin / mémétique |
|---|---:|---:|---:|
| Appels | 516 [516 ; 521] | 516 [511 ; 516] | 1,0 |
| Échecs | 6 181 [5 746 ; 7 039] | 13 310 [13 160 ; 13 620] | 2,2 |
| Propagations | 4,10 M [3,75 ; 4,56] | 14,3 M [14,1 ; 14,6] | 3,5 |
| Temps déterministe | 1,07 [1,00 ; 1,17] | 3,82 [3,77 ; 3,86] | 3,6 |
| Temps déterministe par appel | 0,0021 | 0,0074 | 3,6 |
| Temps de résolution (s, non déterministe) | 3,9 | 9,4 | 2,4 |

## 5. Pourquoi : la faisabilité vient des opérateurs

Taux de faisabilité avant et après le LocalSolver (graine 0, cumulé sur 80 générations) :

| Origine | Mémétique avant → après | Témoin avant → après |
|---|---:|---:|
| Croisement | 60 % → 70 % | 0 % → 1 % |
| Mutation | 69 % → 76 % | 0 % → 1 % |
| Initialisation et restart | 0 % → 0 % | 0 % → 0 % |

Un génome aléatoire viole presque toujours « au moins 1 ». Avec un voisinage de 1, la recherche locale ne libère qu'un employé, plus les employés structurellement infaisables, et ne peut pas réparer la couverture. Le témoin ne trouve donc un horaire faisable que par chance (génération 11 en médiane). Ses recherches locales coûtent en plus 3,6 fois plus cher, parce qu'elles partent de loin. Les enfants du mémétique, eux, héritent de quarts qui couvrent déjà la demande : 60 à 70 % sont faisables avant même la recherche locale, qui n'a plus qu'à les affiner.

## 6. Conclusion

Sur bench_2, à budget égal d'appels au LocalSolver, **le mémétique bat nettement les redémarrages aléatoires**. Il atteint l'optimum dans 21 exécutions sur 21, contre 1 sur 21. Il le fait avec 3,6 fois moins de temps déterministe cumulé et 3,5 fois moins de propagations. La différence vient de la variation : hériter des parents garde la couverture, ce qu'un génome aléatoire, même réparé localement, n'obtient presque jamais.

Limites :
- Une seule instance.
- Un voisinage de 1 désavantage particulièrement le témoin : une recherche locale plus large réparerait mieux les génomes aléatoires, mais coûterait aussi plus cher par appel (voir `bench2_voisinage.md`).
- Le fichier de résultats ne garde que l'effort cumulé de toute l'exécution, pas l'effort au moment du succès.

Prochaine étape : le témoin plus sévère, la **marche aléatoire** (mutation + LocalSolver depuis l'individu courant, nouveau point toujours accepté). Il garde l'hérédité, mais sans population, sans croisement et sans sélection.
