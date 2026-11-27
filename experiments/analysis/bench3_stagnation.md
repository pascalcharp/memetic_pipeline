# Comparaison des seuils de stagnation sur bench_3

## 1. Objectif

Evaluer l'influence du seuil de stagnation sur la qualite
des solutions, les redemarrages et l'effort du solveur,
en reproduisant le protocole experimental de bench_2.

L'optimum documente de bench_3 est de 16.

## 2. Protocole experimental

Les seuils de stagnation 3, 5, 10 et 15 sont compares
avec les memes graines, de 0 a 20.

Les 21 executions du seuil 10 proviennent de la serie
population-generations. Les 63 autres sont nouvelles.

Parametres fixes :

- Population : 18.
- Generations : 26.
- NR : 6.
- NM : 6.
- Voisinage : 1.
- Budget deterministe : 5.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Mutation : shift_start.
- Recherche locale initiale : activee.

Le budget nominal est de 486 individus, hors redemarrages.

## 3. Qualite des solutions finales

| Stagnation | Faisables | Faisables sans violation quasi stricte | Optimales |
|---:|---:|---:|---:|
| 3 | 21/21 | 21/21 | 0/21 |
| 5 | 21/21 | 21/21 | 0/21 |
| 10 | 21/21 | 21/21 | 0/21 |
| 15 | 21/21 | 21/21 | 0/21 |

Aucune solution finale ne presente de violation structurelle,
de violation de couverture ou de cellule quasi stricte violee.

### Couts globaux

| Stagnation | Minimum | Maximum | Moyenne | Mediane | Ecart-type |
|---:|---:|---:|---:|---:|---:|
| 3 | 34 | 88 | 44.0476 | 43 | 10.9652 |
| 5 | 28 | 88 | 42.8571 | 41 | 11.6794 |
| 10 | 28 | 88 | 41.2857 | 41 | 12.2130 |
| 15 | 28 | 88 | 41.9524 | 41 | 11.9023 |

Les statistiques conditionnelles aux solutions faisables
sans violation quasi stricte sont identiques aux statistiques
globales, puisque toutes les solutions satisfont ces criteres.

### Decomposition moyenne des couts

| Stagnation | Sous-couverture | Surcouverture | Penalites |
|---:|---:|---:|---:|
| 3 | 37.6190 | 6.4286 | 0 |
| 5 | 37.1905 | 5.6667 | 0 |
| 10 | 35.3333 | 5.9524 | 0 |
| 15 | 36.0000 | 5.9524 | 0 |

### Ecarts a l'optimum

| Stagnation | Ecart absolu moyen | Ecart relatif moyen (%) |
|---:|---:|---:|
| 3 | 28.0476 | 175.30 |
| 5 | 26.8571 | 167.86 |
| 10 | 25.2857 | 158.04 |
| 15 | 25.9524 | 162.20 |

Le seuil 10 obtient le meilleur cout moyen.
Le seuil 15 presente des resultats tres proches.

## 4. Effort du solveur

| Stagnation | Redemarrages moyens | Appels moyens | Propagations moyennes | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|
| 3 | 2.95 | 536.1905 | 570708256.3333 | 288.0006 |
| 5 | 1.62 | 513.5238 | 454710338.2857 | 230.8113 |
| 10 | 0.43 | 493.2857 | 338203861.1429 | 169.1851 |
| 15 | 0.05 | 486.8095 | 307431180.1429 | 150.8308 |

L'effort du solveur diminue lorsque le seuil de stagnation
augmente.

Par rapport au seuil 10, le seuil 3 necessite environ
68.7 % plus de propagations et 70.2 % plus de temps solveur.

Le seuil 15 reduit les propagations d'environ 9.1 %
par rapport au seuil 10, avec une augmentation du cout
moyen d'environ 1.6 %.

Les redemarrages frequents augmentent le budget reel
d'individus traites et modifient les trajectoires de recherche.

## 5. Convergence

| Stagnation | Executions ayant observe un individu faisable | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---:|---:|---:|---:|---:|---:|
| 3 | 21/21 | 2.38 | 2 | 1 | 4 |
| 5 | 21/21 | 2.38 | 2 | 1 | 4 |
| 10 | 21/21 | 2.38 | 2 | 1 | 4 |
| 15 | 21/21 | 2.38 | 2 | 1 | 4 |

Les statistiques agregees de premiere faisabilite sont
identiques pour les quatre configurations.

Aucune configuration n'atteint l'optimum de 16.

Les statistiques de premiere generation optimale et de
budget avant optimum ne sont donc pas disponibles.

## 6. Diversite

| Stagnation | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 1 | 1 |
| 5 | 1 | 1 | 1 | 1 |
| 10 | 1 | 1 | 1 | 1 |
| 15 | 1 | 1 | 1 | 1 |

La diversite initiale et finale est maximale selon les
indicateurs utilises, independamment du seuil.

Les redemarrages frequents n'apportent donc pas de gain
observable sur ces mesures initiales et finales.

## 7. Effet de la recherche locale

### Initialisation

Les taux de faisabilite avant et apres la recherche locale
initiale sont nuls pour les quatre configurations.

### Croisement

| Stagnation | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 3 | 24.10 | 37.33 | 13.23 |
| 5 | 33.62 | 47.44 | 13.81 |
| 10 | 46.17 | 59.57 | 13.40 |
| 15 | 48.63 | 61.89 | 13.26 |

### Mutation

| Stagnation | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 3 | 20.27 | 37.33 | 17.06 |
| 5 | 26.40 | 44.93 | 18.53 |
| 10 | 34.92 | 54.95 | 20.02 |
| 15 | 36.29 | 56.56 | 20.27 |

### Redemarrage

| Stagnation | Avant (%) | Apres (%) |
|---:|---:|---:|
| 3 | 0 | 0 |
| 5 | 0 | 0 |
| 10 | 0 | 0.65 |
| 15 | 0 | 0 |

Les taux de faisabilite apres croisement et mutation
augmentent avec le seuil de stagnation.

Ces taux sont toutefois influences par les populations
rencontrees pendant les executions et ne permettent pas
d'isoler l'efficacite propre des operateurs.

## 8. Comparaison avec bench_2

Sur bench_2, tous les seuils atteignent l'optimum pour
les 21 graines.

Sur bench_3, aucun seuil n'atteint l'optimum, mais toutes
les solutions finales sont faisables et sans violation
quasi stricte.

Dans les deux instances, les seuils faibles augmentent
le nombre de redemarrages et l'effort du solveur.

Sur bench_3, les seuils faibles n'apportent pas
d'amelioration du cout final moyen.

Le seuil 15 minimise les propagations sur les deux instances.

## 9. Conclusion

Le seuil de stagnation 10 est conserve comme reference.

Il obtient le meilleur cout moyen sur bench_3 et constitue
un compromis entre qualite des solutions et effort solveur.

Le seuil 15 constitue une alternative interessante
lorsque la reduction de l'effort solveur est prioritaire.

Les seuils 3 et 5 ne presentent pas d'avantage evident
dans les conditions experimentales etudiees.

## 10. Limites

- Le budget nominal exclut les redemarrages.
- Le nombre de generations est fixe a 26.
- Les interactions avec la taille du voisinage ne sont
  pas etudiees dans cette serie.
- Les statistiques agregees ne demontrent pas une
  equivalence des trajectoires pour chaque graine.
- Le temps solveur cumule ne mesure pas le temps avant
  l'obtention d'une solution de qualite donnee.
- Aucun test statistique inferentiel n'a ete realise.

## 11. Reproductibilite

- Reference seuil 10 : daaffa732dc66bc8a2273934aa47bdcc65b5d503.
- Seuils 3, 5 et 15 : f9376a7dbd6984b86138e4e045ca102d1a2bb52f.
- Git dirty : False pour toutes les executions.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_stagnation/.
- Script : experiments/analysis/analyze_bench3_stagnation.py.

Commande de reproduction :

    python3 experiments/analysis/analyze_bench3_stagnation.py
