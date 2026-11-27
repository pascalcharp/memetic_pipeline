# Interaction entre voisinage et budget deterministe sur bench_3

## 1. Objectif

Etudier l'interaction entre la taille du voisinage et
le budget deterministe de la recherche locale.

Cette serie supplementaire vise a verifier si l'influence
du budget depend de la complexite du voisinage.

L'optimum documente de bench_3 est de 16.

## 2. Protocole experimental

Deux tailles de voisinage (1 et 2) et quatre budgets
deterministes (1, 2.5, 5 et 10) sont compares.

Chaque combinaison est evaluee avec les graines 0 a 20.

Le plan comprend 168 executions distinctes, dont
105 references reutilisees et 63 nouvelles executions.

Parametres fixes :

- Population : 18.
- Generations : 26.
- NR : 6.
- NM : 6.
- Stagnation : 10.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Mutation : shift_start.
- Recherche locale initiale : activee.

Le budget nominal est de 486 individus, hors redemarrages.

## 3. Qualite des solutions finales

| Voisinage | Budget | Faisables | Sans violation quasi stricte | Optimales |
|---:|---:|---:|---:|---:|
| 1 | 1 | 21/21 | 19/21 | 0/21 |
| 1 | 2.5 | 21/21 | 20/21 | 0/21 |
| 1 | 5 | 21/21 | 21/21 | 0/21 |
| 1 | 10 | 21/21 | 20/21 | 0/21 |
| 2 | 1 | 2/21 | 0/21 | 0/21 |
| 2 | 2.5 | 20/21 | 17/21 | 0/21 |
| 2 | 5 | 21/21 | 21/21 | 0/21 |
| 2 | 10 | 21/21 | 21/21 | 0/21 |

### Couts globaux pour le voisinage 2

| Budget | Minimum | Maximum | Moyenne | Mediane | Ecart-type |
|---:|---:|---:|---:|---:|---:|
| 1 | 4000048 | 27000108 | 12619114.1429 | 13000048 | 5584648.9481 |
| 2.5 | 17 | 7000058 | 476228.7619 | 39 | 1499814.8700 |
| 5 | 17 | 29 | 23.1429 | 22 | 3.3705 |
| 10 | 17 | 27 | 20.7619 | 21 | 2.5431 |

### Couts conditionnels aux solutions faisables sans violation quasi stricte

| Voisinage | Budget | Nombre | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 19 | 37.6316 | 37 | 23 | 48 | 6.9374 |
| 1 | 2.5 | 20 | 40.4000 | 36.5 | 28 | 88 | 12.7844 |
| 1 | 5 | 21 | 41.2857 | 41 | 28 | 88 | 12.2130 |
| 1 | 10 | 20 | 41.1000 | 39.5 | 28 | 88 | 12.4856 |
| 2 | 1 | 0 | N/A | N/A | N/A | N/A | N/A |
| 2 | 2.5 | 17 | 38.1176 | 36 | 17 | 99 | 18.0094 |
| 2 | 5 | 21 | 23.1429 | 22 | 17 | 29 | 3.3705 |
| 2 | 10 | 21 | 20.7619 | 21 | 17 | 27 | 2.5431 |

Les moyennes conditionnelles doivent etre interpretees
conjointement avec les taux de solutions admissibles.

### Violations moyennes pour le voisinage 2

| Budget | Cellules quasi strictes | Violations de couverture | Violations structurelles |
|---:|---:|---:|---:|
| 1 | 6.2381 | 4.0000 | 0 |
| 2.5 | 0.3810 | 0.0476 | 0 |
| 5 | 0 | 0 | 0 |
| 10 | 0 | 0 | 0 |

### Decomposition moyenne des couts pour le voisinage 2

| Budget | Sous-couverture | Surcouverture | Penalites |
|---:|---:|---:|---:|
| 1 | 8619099.6190 | 14.5238 | 4000000 |
| 2.5 | 428605.3810 | 4.3333 | 47619.0476 |
| 5 | 22.9524 | 0.1905 | 0 |
| 10 | 20.6667 | 0.0952 | 0 |

### Ecarts conditionnels a l'optimum pour le voisinage 2

| Budget | Ecart absolu moyen | Ecart relatif moyen (%) |
|---:|---:|---:|
| 1 | N/A | N/A |
| 2.5 | 22.1176 | 138.24 |
| 5 | 7.1429 | 44.64 |
| 10 | 4.7619 | 29.76 |

Aucun optimum n'est atteint.

Le meilleur cout moyen est obtenu avec le voisinage 2
et le budget 10.

## 4. Effort du solveur

| Voisinage | Budget | Redemarrages moyens | Appels moyens | Propagations moyennes | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 0.43 | 493.2857 | 304276546.8095 | 153.1863 |
| 1 | 2.5 | 0.48 | 494.0952 | 328179108.5238 | 167.3158 |
| 1 | 5 | 0.43 | 493.2857 | 338203861.1429 | 169.1851 |
| 1 | 10 | 0.48 | 494.0952 | 341126146.5714 | 168.8520 |
| 2 | 1 | 0 | 486 | 1392993465.5238 | 592.3647 |
| 2 | 2.5 | 0 | 486 | 3015843406.5238 | 1327.7831 |
| 2 | 5 | 0 | 486 | 4971934465.0476 | 2166.1105 |
| 2 | 10 | 0.10 | 487.6190 | 8229513633.8095 | 3574.7291 |

Pour le voisinage 2, le passage du budget 5 au budget 10 :

- Reduit le cout moyen de 10.29 %.
- Reduit l'ecart moyen a l'optimum de 33.33 %.
- Augmente les propagations de 65.52 %.
- Augmente le temps solveur cumule de 65.03 %.

L'influence du budget sur l'effort solveur est beaucoup
plus prononcee avec le voisinage 2.

## 5. Convergence

| Voisinage | Budget | Executions ayant observe un individu faisable | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 21/21 | 2.48 | 2 | 1 | 4 |
| 1 | 2.5 | 21/21 | 2.38 | 2 | 1 | 4 |
| 1 | 5 | 21/21 | 2.38 | 2 | 1 | 4 |
| 1 | 10 | 21/21 | 2.38 | 2 | 1 | 4 |
| 2 | 1 | 3/21 | 25 | 25 | 24 | 26 |
| 2 | 2.5 | 21/21 | 15.29 | 15 | 8 | 26 |
| 2 | 5 | 21/21 | 6.57 | 6 | 3 | 12 |
| 2 | 10 | 21/21 | 3.05 | 3 | 1 | 6 |

Pour le voisinage 2, la premiere faisabilite intervient
plus tot en nombre de generations lorsque le budget augmente.

Pour le budget 1, cette statistique porte uniquement
sur les trois executions ayant observe un individu faisable.

Une convergence plus rapide en generations ne signifie
pas necessairement une convergence plus rapide en temps reel.

## 6. Diversite

| Voisinage | Budget | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 0.9974 | 1 | 1 |
| 1 | 2.5 | 1 | 1 | 1 | 1 |
| 1 | 5 | 1 | 1 | 1 | 1 |
| 1 | 10 | 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 1 | 1 | 1 |
| 2 | 2.5 | 1 | 0.9180 | 1 | 1 |
| 2 | 5 | 1 | 0.7804 | 1 | 1 |
| 2 | 10 | 1 | 0.6984 | 1 | 1 |

Pour le voisinage 2, la diversite genotypique finale
diminue lorsque le budget augmente.

La diversite phenotypique reste maximale selon
l'indicateur utilise.

Cette association ne suffit pas a etablir un lien causal
entre la diversite et la qualite des solutions.

## 7. Effet de la recherche locale pour le voisinage 2

### Initialisation

Les taux de faisabilite avant et apres la recherche
locale initiale sont nuls pour tous les budgets.

### Croisement

| Budget | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 1 | 0.02 | 0.06 | 0.05 |
| 2.5 | 9.46 | 11.84 | 2.38 |
| 5 | 18.96 | 26.11 | 7.16 |
| 10 | 22.97 | 37.99 | 15.02 |

### Mutation

| Budget | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 1 | 0.03 | 0.03 | 0 |
| 2.5 | 10.78 | 15.93 | 5.16 |
| 5 | 23.81 | 40.26 | 16.45 |
| 10 | 31.38 | 58.39 | 27.01 |

### Redemarrage

Aucun redemarrage n'est observe pour les budgets
1, 2.5 et 5.

Pour le budget 10, les taux de faisabilite avant
et apres la recherche locale de redemarrage sont nuls.

Les taux de faisabilite apres croisement et mutation
augmentent avec le budget.

Ces taux agreges dependent egalement des populations
rencontrees au cours des executions.

## 8. Interaction entre les parametres

Avec le voisinage 1, les quatre budgets produisent
des taux de faisabilite finale de 100 %.

Avec le voisinage 2, le taux de faisabilite finale
passe de 9.52 % pour le budget 1 a 100 % pour les
budgets 5 et 10.

Le voisinage 2 est donc beaucoup plus sensible
au budget deterministe dans les conditions etudiees.

Ces resultats suggerent que les mauvais resultats
obtenus avec les voisinages 3 et 4 pourraient etre
lies en partie a un budget insuffisant.

Cette hypothese n'est toutefois pas directement
verifiee pour ces deux tailles de voisinage.

## 9. Compromis qualite-effort

| Configuration | Cout moyen | Solutions sans violation quasi stricte | Temps solveur moyen (s) |
|---|---:|---:|---:|
| Voisinage 1, budget 5 | 41.2857 | 21/21 | 169.1851 |
| Voisinage 2, budget 5 | 23.1429 | 21/21 | 2166.1105 |
| Voisinage 2, budget 10 | 20.7619 | 21/21 | 3574.7291 |

Ces trois configurations illustrent des compromis
differents entre qualite et effort computationnel.

## 10. Conclusion

Une interaction importante est observee entre
la taille du voisinage et le budget deterministe.

Le voisinage 2 avec un budget 10 obtient la meilleure
qualite moyenne parmi les configurations testees,
mais necessite un effort solveur considerable.

Le voisinage 2 avec un budget 5 constitue une
alternative intermediaire.

Le voisinage 1 avec un budget 5 reste la configuration
de reference pour les prochaines series afin de
preserver la comparabilite avec bench_2.

## 11. Limites

- Aucun optimum n'est atteint.
- Le budget nominal exclut les redemarrages.
- Les raisons d'arret du solveur ne sont pas analysees.
- Les voisinages 3 et 4 ne sont pas etudies avec
  des budgets supplementaires.
- Les couts conditionnels peuvent porter sur des
  sous-ensembles differents de graines.
- Le temps solveur cumule ne mesure pas le temps
  avant l'obtention d'une solution de qualite donnee.
- Aucun test statistique inferentiel de l'interaction
  n'a ete realise.
- Les conclusions concernent les configurations
  et l'instance etudiees.

## 12. Reproductibilite

- Voisinage 1, budget 5 : daaffa732dc66bc8a2273934aa47bdcc65b5d503.
- Voisinage 1, autres budgets : 16daf977ef0070f6a48d5394ac76696727f710fb.
- Voisinage 2, budget 5 : ab977345a09a06a59be7d7ecd20be8b84f010672.
- Voisinage 2, autres budgets : 96c603cc45b5bcc1a6198bdd354b20c7763a9b57.
- Git dirty : False pour toutes les executions.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_voisinage_budget/.

Commandes de reproduction :

    python3 experiments/analysis/analyze_bench3_deterministic_time.py
    python3 experiments/analysis/analyze_bench3_neighborhood_budget.py
