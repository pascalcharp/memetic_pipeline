# Comparaison des budgets deterministes sur bench_3

## 1. Objectif

Evaluer l'influence du budget deterministe sur la qualite
des solutions et l'effort du solveur, en reproduisant
le protocole experimental de bench_2.

L'optimum documente de bench_3 est de 16.

## 2. Protocole experimental

Les budgets 1, 2.5, 5 et 10 sont compares avec les
memes graines, de 0 a 20.

Les 21 executions du budget 5 proviennent de la serie
population-generations. Les 63 autres sont nouvelles.

Parametres fixes :

- Population : 18.
- Generations : 26.
- NR : 6.
- NM : 6.
- Voisinage : 1.
- Stagnation : 10.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Mutation : shift_start.
- Recherche locale initiale : activee.

Le budget nominal est de 486 individus, hors redemarrages.

## 3. Qualite des solutions finales

| Budget | Faisables | Faisables sans violation quasi stricte | Optimales |
|---:|---:|---:|---:|
| 1 | 21/21 | 19/21 | 0/21 |
| 2.5 | 21/21 | 20/21 | 0/21 |
| 5 | 21/21 | 21/21 | 0/21 |
| 10 | 21/21 | 20/21 | 0/21 |

### Couts globaux

| Budget | Minimum | Maximum | Moyenne | Mediane | Ecart-type |
|---:|---:|---:|---:|---:|---:|
| 1 | 23 | 1000038 | 95275.6667 | 38 | 293543.3386 |
| 2.5 | 28 | 1000030 | 47658.9524 | 37 | 212956.6406 |
| 5 | 28 | 88 | 41.2857 | 41 | 12.2130 |
| 10 | 28 | 1000033 | 47659.7619 | 41 | 212957.1304 |

### Couts conditionnels aux solutions faisables sans violation quasi stricte

| Budget | Nombre | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 19 | 37.6316 | 37 | 23 | 48 | 6.9374 |
| 2.5 | 20 | 40.4000 | 36.5 | 28 | 88 | 12.7844 |
| 5 | 21 | 41.2857 | 41 | 28 | 88 | 12.2130 |
| 10 | 20 | 41.1000 | 39.5 | 28 | 88 | 12.4856 |

Les couts conditionnels portent sur des sous-ensembles
differents de graines et ne permettent pas une comparaison
appariee directe.

### Violations moyennes

| Budget | Cellules quasi strictes | Violations de couverture | Violations structurelles |
|---:|---:|---:|---:|
| 1 | 0.0952 | 0 | 0 |
| 2.5 | 0.0476 | 0 | 0 |
| 5 | 0 | 0 | 0 |
| 10 | 0.0476 | 0 | 0 |

### Decomposition moyenne des couts

| Budget | Sous-couverture | Surcouverture | Penalites |
|---:|---:|---:|---:|
| 1 | 95273.1429 | 2.5238 | 0 |
| 2.5 | 47654.0476 | 4.9048 | 0 |
| 5 | 35.3333 | 5.9524 | 0 |
| 10 | 47654.0000 | 5.7619 | 0 |

Le budget 5 est le seul a produire 21 solutions finales
faisables sans violation quasi stricte.

## 4. Effort du solveur

| Budget | Redemarrages moyens | Appels moyens | Propagations moyennes | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|
| 1 | 0.43 | 493.2857 | 304276546.8095 | 153.1863 |
| 2.5 | 0.48 | 494.0952 | 328179108.5238 | 167.3158 |
| 5 | 0.43 | 493.2857 | 338203861.1429 | 169.1851 |
| 10 | 0.48 | 494.0952 | 341126146.5714 | 168.8520 |

Par rapport au budget 5, le budget 1 reduit les
propagations d'environ 10.0 %.

Le budget 10 augmente les propagations de seulement
0.86 % par rapport au budget 5.

L'effet marginal du budget sur l'effort observe diminue
lorsque le budget augmente.

## 5. Convergence

| Budget | Executions ayant observe un individu faisable | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---:|---:|---:|---:|---:|---:|
| 1 | 21/21 | 2.48 | 2 | 1 | 4 |
| 2.5 | 21/21 | 2.38 | 2 | 1 | 4 |
| 5 | 21/21 | 2.38 | 2 | 1 | 4 |
| 10 | 21/21 | 2.38 | 2 | 1 | 4 |

Les statistiques de premiere faisabilite sont proches.

Aucune configuration n'atteint l'optimum de 16.

## 6. Diversite

| Budget | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---:|---:|---:|---:|---:|
| 1 | 1 | 0.9974 | 1 | 1 |
| 2.5 | 1 | 1 | 1 | 1 |
| 5 | 1 | 1 | 1 | 1 |
| 10 | 1 | 1 | 1 | 1 |

La diversite initiale et finale est peu influencee
par le budget selon les indicateurs agreges.

## 7. Effet de la recherche locale

### Initialisation

Les taux de faisabilite avant et apres la recherche locale
initiale sont nuls pour les quatre configurations.

### Croisement

| Budget | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 1 | 48.92 | 61.87 | 12.96 |
| 2.5 | 46.81 | 60.42 | 13.61 |
| 5 | 46.17 | 59.57 | 13.40 |
| 10 | 46.26 | 59.63 | 13.37 |

### Mutation

| Budget | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 1 | 35.74 | 53.36 | 17.61 |
| 2.5 | 34.58 | 54.21 | 19.63 |
| 5 | 34.92 | 54.95 | 20.02 |
| 10 | 34.92 | 55.10 | 20.18 |

### Redemarrage

| Budget | Avant (%) | Apres (%) |
|---:|---:|---:|
| 1 | 0 | 0 |
| 2.5 | 0 | 0.59 |
| 5 | 0 | 0.65 |
| 10 | 0 | 0.59 |

Les taux agreges dependent des populations rencontrees
pendant les executions.

## 8. Comparaison individuelle des graines

Nombre de graines presentant une difference par rapport
au budget de reference 5, sur 21 graines :

| Champ | Budget 1 | Budget 2.5 | Budget 10 |
|---|---:|---:|---:|
| best | 21 | 8 | 1 |
| generations | 0 | 0 | 0 |
| restarts | 10 | 5 | 1 |
| cost_statistics | 21 | 10 | 2 |
| diversity | 21 | 8 | 1 |
| feasibility_rates | 21 | 8 | 1 |
| solver_effort.calls | 10 | 5 | 1 |
| solver_effort.nodes | 0 | 0 | 0 |
| solver_effort.failures | 21 | 14 | 3 |
| solver_effort.propagations | 21 | 14 | 3 |

Les mesures temporelles sont exclues de cette comparaison.

Les budgets 5 et 10 produisent des resultats tres proches,
mais ne sont pas strictement equivalents.

Une difference du champ best ne signifie pas necessairement
une difference du cout final.

## 9. Comparaison avec bench_2

Sur bench_2, aucune difference non temporelle n'avait
ete observee entre les budgets testes.

Sur bench_3, le budget influence les trajectoires,
les solutions finales et l'effort du solveur.

Les differences deviennent moins frequentes lorsque
le budget se rapproche de 5 ou le depasse.

Ces observations suggerent une saturation progressive
du budget, sans toutefois demontrer que le solveur
termine systematiquement avant la limite imposee.

## 10. Conclusion

Le budget deterministe 5 est conserve comme reference
pour le voisinage de taille 1.

Il est le seul a produire des solutions finales faisables
sans violation quasi stricte pour les 21 graines.

Le budget 1 reduit l'effort solveur, mais introduit
un risque observe de violations quasi strictes.

Le budget 10 n'apporte pas d'amelioration globale
observable par rapport au budget 5.

Une serie supplementaire est proposee avec un voisinage
de taille 2 afin d'etudier l'interaction entre les
deux parametres.

## 11. Limites

- Le budget nominal exclut les redemarrages.
- Les raisons d'arret du solveur ne sont pas analysees.
- Les moyennes conditionnelles portent sur des
  sous-ensembles differents de graines.
- Le temps solveur cumule ne mesure pas le temps
  avant l'obtention d'une solution de qualite donnee.
- Les conditions de parallelisation peuvent influencer
  les mesures temporelles.
- Aucun test statistique inferentiel n'a ete realise.

## 12. Reproductibilite

- Reference budget 5 : daaffa732dc66bc8a2273934aa47bdcc65b5d503.
- Budgets 1, 2.5 et 10 : 16daf977ef0070f6a48d5394ac76696727f710fb.
- Git dirty : False pour toutes les executions.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_deterministic_time/.
- Script : experiments/analysis/analyze_bench3_deterministic_time.py.

Commande de reproduction :

    python3 experiments/analysis/analyze_bench3_deterministic_time.py
