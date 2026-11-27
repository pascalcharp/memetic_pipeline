# Analyse comparative des operateurs de mutation sur bench_3

## 1. Objectif

Evaluer l'influence des operateurs de mutation
sur la qualite des solutions, la convergence
et l'effort computationnel.

Verifier si le choix effectue sur bench_2
demeure pertinent sur bench_3.

L'optimum documente de bench_3 est de 16.

## 2. Protocole experimental

Trois operateurs sont compares :

- shift_start
- block_boundary
- activity

Chaque operateur est evalue avec les graines 0 a 20.

Parametres fixes :

- Population : 18.
- Generations : 26.
- NR : 3.
- NM : 12.
- Voisinage : 1.
- Stagnation : 10.
- Budget deterministe : 5.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Recherche locale initiale : activee.

Le budget nominal est de 486 individus,
hors redemarrages.

La serie comprend 63 executions, dont 42 nouvelles
executions et 21 references reutilisees.

## 3. Qualite des solutions finales

| Mutation | Faisables | Sans violation quasi stricte | Optimales |
|---|---:|---:|---:|
| shift_start | 21/21 | 21/21 | 0/21 |
| block_boundary | 21/21 | 18/21 | 0/21 |
| activity | 21/21 | 19/21 | 0/21 |

### Couts globaux

| Mutation | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---|---:|---:|---:|---:|---:|
| shift_start | 37.6667 | 38 | 22 | 51 | 8.8712 |
| block_boundary | 142893.0952 | 36 | 24 | 1000041 | 349926.8535 |
| activity | 142893.3333 | 36 | 24 | 2000033 | 466568.1918 |

### Couts conditionnels aux solutions faisables sans violation quasi stricte

| Mutation | Nombre | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---|---:|---:|---:|---:|---:|---:|
| shift_start | 21 | 37.6667 | 38 | 22 | 51 | 8.8712 |
| block_boundary | 18 | 36.0556 | 36 | 24 | 49 | 7.1217 |
| activity | 19 | 36.6842 | 36 | 24 | 55 | 8.8915 |

Les operateurs block_boundary et activity obtiennent
des couts conditionnels legerement inferieurs.

Cependant, shift_start est le seul operateur
produisant des solutions sans violation quasi stricte
pour les 21 graines.

Les moyennes conditionnelles ne portent pas
sur les memes ensembles de graines.

### Violations moyennes

| Mutation | Cellules quasi strictes | Violations de couverture | Violations structurelles |
|---|---:|---:|---:|
| shift_start | 0 | 0 | 0 |
| block_boundary | 0.1429 | 0 | 0 |
| activity | 0.1429 | 0 | 0 |

### Decomposition moyenne des couts

| Mutation | Sous-couverture | Surcouverture | Penalites |
|---|---:|---:|---:|
| shift_start | 34.0000 | 3.6667 | 0 |
| block_boundary | 142890.0000 | 3.0952 | 0 |
| activity | 142890.4286 | 2.9048 | 0 |

### Ecarts conditionnels a l'optimum

| Mutation | Ecart absolu moyen | Ecart relatif moyen (%) |
|---|---:|---:|
| shift_start | 21.6667 | 135.42 |
| block_boundary | 20.0556 | 125.35 |
| activity | 20.6842 | 129.28 |

Aucun optimum n'est atteint.

## 4. Effort du solveur

| Mutation | Redemarrages moyens | Appels moyens | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|---:|
| shift_start | 0.29 | 490.8571 | 296002741.3810 | 147.3328 |
| block_boundary | 0.19 | 489.2381 | 229880585.6190 | 114.2875 |
| activity | 0.14 | 488.4286 | 333750181.9524 | 161.2507 |

Comparativement a shift_start, block_boundary :

- Reduit les propagations de 22.34 %.
- Reduit le temps solveur cumule de 22.43 %.

Comparativement a shift_start, activity :

- Augmente les propagations de 12.75 %.
- Augmente le temps solveur cumule de 9.45 %.

Block_boundary presente le plus faible effort
solveur parmi les trois operateurs testes.

## 5. Convergence

| Mutation | Executions ayant observe un individu faisable | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---|---:|---:|---:|---:|---:|
| shift_start | 21/21 | 1.76 | 2 | 1 | 4 |
| block_boundary | 21/21 | 1.67 | 2 | 1 | 4 |
| activity | 21/21 | 1.71 | 2 | 1 | 3 |

Les differences de convergence vers une premiere
solution faisable sont relativement faibles.

## 6. Diversite

| Mutation | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---|---:|---:|---:|---:|
| shift_start | 1 | 0.9947 | 1 | 1 |
| block_boundary | 1 | 1 | 1 | 1 |
| activity | 1 | 1 | 1 | 1 |

La diversite demeure tres elevee pour les
trois operateurs selon les indicateurs utilises.

## 7. Effet de la recherche locale

### Initialisation

Les taux de faisabilite avant et apres la
recherche locale initiale sont nuls pour
les trois operateurs.

### Croisement

| Mutation | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| shift_start | 44.90 | 58.52 | 13.61 |
| block_boundary | 53.54 | 66.94 | 13.40 |
| activity | 41.51 | 58.42 | 16.91 |

### Mutation

| Mutation | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| shift_start | 35.07 | 53.69 | 18.62 |
| block_boundary | 56.49 | 70.15 | 13.66 |
| activity | 36.97 | 61.02 | 24.05 |

Block_boundary presente le meilleur taux de
faisabilite apres mutation et recherche locale.

Activity presente le gain le plus important.

### Redemarrage

| Mutation | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| shift_start | 0 | 0 | 0 |
| block_boundary | 0 | 1.47 | 1.47 |
| activity | 0 | 0 | 0 |

Ces taux agreges dependent des populations
rencontrees au cours des executions.

Ils ne permettent pas d'isoler directement
l'efficacite intrinseque des operateurs.

## 8. Comparaison avec bench_2

Sur bench_2, les trois operateurs atteignent
systematiquement l'optimum.

Shift_start et block_boundary presentent
des performances proches.

Sur bench_3, block_boundary reduit davantage
l'effort solveur, mais produit trois solutions
avec violation quasi stricte.

Activity necessite un effort solveur superieur
a shift_start sur les deux instances.

Shift_start demeure le choix retenu, mais
pour des raisons differentes selon l'instance.

## 9. Conclusion

L'operateur shift_start est conserve pour
sa robustesse observee sur bench_3.

Il est le seul a produire 21 solutions finales
sans violation quasi stricte.

Block_boundary constitue une alternative
interessante pour reduire l'effort computationnel.

Activity ne presente pas d'avantage global
suffisant pour etre retenu dans les conditions
etudiees.

## 10. Limites

- Aucun optimum n'est atteint.
- Seulement trois operateurs sont compares.
- Les couts conditionnels peuvent porter sur
  des sous-ensembles differents de graines.
- Les interactions entre les mutations et
  les autres parametres ne sont pas etudiees.
- Aucun test statistique inferentiel n'est realise.
- Les conclusions concernent les instances
  et les configurations etudiees.

## 11. Reproductibilite

- Shift_start : 91aa95633017c9c6cc8001da885f1e595be8c4cd.
- Block_boundary et activity : 55a4b7e2092174a313780b75518ce62530bee892.
- Git dirty : False.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_mutation/.

Commande de reproduction :

    python3 experiments/analysis/analyze_bench3_mutation.py
