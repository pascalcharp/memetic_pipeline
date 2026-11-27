# Analyse comparative des ratios NR/NM sur bench_3

## 1. Objectif

Evaluer l'influence de la repartition entre les
croisements et les mutations sur les performances
de l'algorithme memetique.

Verifier si le ratio retenu sur bench_2 demeure
interessant sur bench_3.

L'optimum documente de bench_3 est de 16.

## 2. Protocole experimental

Trois ratios sont compares sur les graines 0 a 20.

| NR | NM | Individus issus du croisement | Individus issus de la mutation |
|---:|---:|---:|---:|
| 3 | 12 | 6 | 12 |
| 6 | 6 | 12 | 6 |
| 8 | 2 | 16 | 2 |

Le nombre d'individus produits par generation
est constant : 2*NR + NM = 18.

Parametres fixes :

- Population : 18.
- Generations : 26.
- Voisinage : 1.
- Stagnation : 10.
- Budget deterministe : 5.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Mutation : shift_start.
- Recherche locale initiale : activee.

Le budget nominal est de 486 individus,
hors redemarrages.

La serie comprend 63 executions, dont 42 nouvelles
executions et 21 references reutilisees.

## 3. Qualite des solutions finales

| NR/NM | Faisables | Sans violation quasi stricte | Optimales |
|---|---:|---:|---:|
| 3/12 | 21/21 | 21/21 | 0/21 |
| 6/6 | 21/21 | 21/21 | 0/21 |
| 8/2 | 21/21 | 20/21 | 0/21 |

### Couts globaux

| NR/NM | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---|---:|---:|---:|---:|---:|
| 3/12 | 37.6667 | 38 | 22 | 51 | 8.8712 |
| 6/6 | 41.2857 | 41 | 28 | 88 | 12.2130 |
| 8/2 | 47654.5238 | 35 | 21 | 1000037 | 212959.1958 |

### Couts conditionnels aux solutions faisables sans violation quasi stricte

| NR/NM | Nombre | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---|---:|---:|---:|---:|---:|---:|
| 3/12 | 21 | 37.6667 | 38 | 22 | 51 | 8.8712 |
| 6/6 | 21 | 41.2857 | 41 | 28 | 88 | 12.2130 |
| 8/2 | 20 | 35.4000 | 34.5 | 21 | 46 | 6.2642 |

Le ratio 8/2 obtient le meilleur cout moyen
conditionnel, mais une execution presente une
violation quasi stricte.

Les moyennes conditionnelles ne portent donc
pas toutes sur les memes ensembles de graines.

Le ratio 3/12 obtient le meilleur cout moyen global
et conserve un taux de solutions sans violation
quasi stricte de 100 %.

### Violations moyennes

| NR/NM | Cellules quasi strictes | Violations de couverture | Violations structurelles |
|---|---:|---:|---:|
| 3/12 | 0 | 0 | 0 |
| 6/6 | 0 | 0 | 0 |
| 8/2 | 0.0476 | 0 | 0 |

### Decomposition moyenne des couts

| NR/NM | Sous-couverture | Surcouverture | Penalites |
|---|---:|---:|---:|
| 3/12 | 34.0000 | 3.6667 | 0 |
| 6/6 | 35.3333 | 5.9524 | 0 |
| 8/2 | 47652.3333 | 2.1905 | 0 |

### Ecarts conditionnels a l'optimum

| NR/NM | Ecart absolu moyen | Ecart relatif moyen (%) |
|---|---:|---:|
| 3/12 | 21.6667 | 135.42 |
| 6/6 | 25.2857 | 158.04 |
| 8/2 | 19.4000 | 121.25 |

Aucun optimum n'est atteint.

## 4. Effort du solveur

| NR/NM | Redemarrages moyens | Appels moyens | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|---:|
| 3/12 | 0.29 | 490.8571 | 296002741.3810 | 147.3328 |
| 6/6 | 0.43 | 493.2857 | 338203861.1429 | 169.1851 |
| 8/2 | 0.62 | 496.5238 | 382996435.0000 | 191.3800 |

Comparativement au ratio 6/6, le ratio 3/12 :

- Reduit le cout moyen global de 8.77 %.
- Reduit les propagations de 12.48 %.
- Reduit le temps solveur cumule de 12.92 %.
- Reduit l'ecart-type des couts de 27.36 %.

Le ratio 3/12 presente le plus faible effort
solveur parmi les trois ratios testes.

## 5. Convergence

| NR/NM | Executions ayant observe un individu faisable | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---|---:|---:|---:|---:|---:|
| 3/12 | 21/21 | 1.76 | 2 | 1 | 4 |
| 6/6 | 21/21 | 2.38 | 2 | 1 | 4 |
| 8/2 | 21/21 | 2.24 | 2 | 1 | 4 |

Le ratio 3/12 atteint une premiere solution
faisable plus tot en moyenne en generations.

## 6. Diversite

| NR/NM | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---|---:|---:|---:|---:|
| 3/12 | 1 | 0.9947 | 1 | 1 |
| 6/6 | 1 | 1 | 1 | 1 |
| 8/2 | 1 | 1 | 1 | 1 |

La diversite demeure tres elevee pour les
trois ratios selon les indicateurs utilises.

## 7. Effet de la recherche locale

### Initialisation

Les taux de faisabilite avant et apres
la recherche locale initiale sont nuls
pour les trois ratios.

### Croisement

| NR/NM | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| 3/12 | 44.90 | 58.52 | 13.61 |
| 6/6 | 46.17 | 59.57 | 13.40 |
| 8/2 | 42.32 | 57.12 | 14.80 |

### Mutation

| NR/NM | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| 3/12 | 35.07 | 53.69 | 18.62 |
| 6/6 | 34.92 | 54.95 | 20.02 |
| 8/2 | 30.13 | 49.54 | 19.41 |

### Redemarrage

| NR/NM | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| 3/12 | 0 | 0 | 0 |
| 6/6 | 0 | 0.65 | 0.65 |
| 8/2 | 0 | 0 | 0 |

Ces taux agreges dependent des populations
rencontrees au cours des executions.

Ils ne permettent pas d'isoler directement
l'efficacite intrinseque des operateurs.

## 8. Comparaison avec bench_2

Effets du ratio 3/12 relativement au ratio 6/6 :

| Indicateur | Bench_2 | Bench_3 |
|---|---:|---:|
| Reduction des propagations (%) | 24.7 | 12.5 |
| Reduction du temps solveur (%) | 11.7 | 12.9 |
| Reduction du cout moyen (%) | 0 | 8.8 |

Le ratio 3/12 reduit l'effort solveur
sur les deux instances.

Sur bench_2, les trois ratios atteignent
systematiquement l'optimum.

Sur bench_3, le ratio 3/12 ameliore egalement
le cout moyen global par rapport au ratio 6/6.

## 9. Conclusion

Le ratio NR=3 et NM=12 est retenu.

Il offre un compromis favorable entre qualite,
robustesse observee et effort computationnel.

Ce choix est coherent avec les resultats
obtenus precedemment sur bench_2.

Le ratio 8/2 reste interessant pour la qualite
conditionnelle de ses solutions, mais presente
un effort solveur superieur et une execution
avec violation quasi stricte.

## 10. Limites

- Aucun optimum n'est atteint sur bench_3.
- Seulement trois ratios sont compares.
- Le budget nominal exclut les redemarrages.
- Les couts conditionnels peuvent porter sur
  des sous-ensembles differents de graines.
- Aucun test statistique inferentiel n'est realise.
- Les conclusions ne garantissent pas la
  generalisation a toutes les instances.

## 11. Reproductibilite

- Ratio 6/6 : daaffa732dc66bc8a2273934aa47bdcc65b5d503.
- Ratios 3/12 et 8/2 : 91aa95633017c9c6cc8001da885f1e595be8c4cd.
- Git dirty : False.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_ratio/.

Commande de reproduction :

    python3 experiments/analysis/analyze_bench3_ratio.py
