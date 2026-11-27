# Comparaison des tailles de voisinage sur bench_3

## 1. Objectif

Evaluer l'influence de la taille du voisinage de la recherche
locale sur la qualite des solutions et l'effort du solveur,
en reproduisant le protocole experimental de bench_2.

L'optimum documente de bench_3 est de 16.

## 2. Protocole experimental

Les tailles de voisinage 1, 2, 3 et 4 sont comparees avec
les memes graines, de 0 a 20.

Les 21 executions du voisinage 1 proviennent de la serie
population-generations. Les 63 autres executions sont nouvelles.

Parametres fixes :

- Population : 18.
- Generations : 26.
- NR : 6.
- NM : 6.
- Stagnation : 10.
- Budget deterministe : 5.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Mutation : shift_start.
- Recherche locale initiale : activee.

Le budget nominal est de 486 individus, hors redemarrages.

## 3. Qualite des solutions finales

| Voisinage | Faisables | Faisables sans violation quasi stricte | Optimales |
|---:|---:|---:|---:|
| 1 | 21/21 | 21/21 | 0/21 |
| 2 | 21/21 | 21/21 | 0/21 |
| 3 | 2/21 | 0/21 | 0/21 |
| 4 | 0/21 | 0/21 | 0/21 |

La faisabilite correspond a CostBreakdown.is_feasible.
Les cellules quasi strictes sont comptabilisees separement.

### Couts globaux

| Voisinage | Minimum | Maximum | Moyenne | Mediane | Ecart-type |
|---:|---:|---:|---:|---:|---:|
| 1 | 28 | 88 | 41.2857 | 41 | 12.2130 |
| 2 | 17 | 29 | 23.1429 | 22 | 3.3705 |
| 3 | 4000056 | 21000052 | 12285777.9048 | 12000064 | 4277771.0755 |
| 4 | 10000050 | 37000079 | 19761964.8571 | 19000079 | 5919346.2508 |

### Couts conditionnels aux solutions faisables sans violation quasi stricte

| Voisinage | Nombre | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 21 | 41.2857 | 41 | 28 | 88 | 12.2130 |
| 2 | 21 | 23.1429 | 22 | 17 | 29 | 3.3705 |
| 3 | 0 | N/A | N/A | N/A | N/A | N/A |
| 4 | 0 | N/A | N/A | N/A | N/A | N/A |

Le voisinage 2 reduit le cout moyen de 43.95 % par rapport
au voisinage 1.

L'ecart relatif moyen a l'optimum passe de 158.04 % a 44.64 %.

### Violations moyennes

| Voisinage | Cellules quasi strictes | Violations de couverture | Violations structurelles |
|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 |
| 2 | 0 | 0 | 0 |
| 3 | 6.1429 | 3.6190 | 0 |
| 4 | 8.0952 | 7.7143 | 0 |

Les voisinages 3 et 4 produisent des solutions de qualite
nettement inferieure, principalement en raison des violations
de couverture et des cellules quasi strictes.

## 4. Effort du solveur

| Voisinage | Appels moyens | Propagations moyennes | Temps solveur moyen (s) | Redemarrages moyens |
|---:|---:|---:|---:|---:|
| 1 | 493.2857 | 338203861.1429 | 169.1851 | 0.43 |
| 2 | 486 | 4971934465.0476 | 2166.1105 | 0 |
| 3 | 486 | 5236501221.9048 | 2844.3828 | 0 |
| 4 | 487.6190 | 3928304613.8095 | 3196.1653 | 0.10 |

Le voisinage 2 necessite environ 14.7 fois plus de propagations
et 12.8 fois plus de temps solveur que le voisinage 1.

Le nombre d'appels reste relativement stable. L'augmentation
de l'effort provient donc principalement du cout des appels.

Le voisinage 4 effectue moins de propagations que les
voisinages 2 et 3, mais son temps solveur est superieur.
Le nombre de propagations ne suffit donc pas a expliquer
integralement le temps de resolution.

## 5. Convergence

| Voisinage | Executions ayant observe un individu faisable | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---:|---:|---:|---:|---:|---:|
| 1 | 21/21 | 2.38 | 2 | 1 | 4 |
| 2 | 21/21 | 6.57 | 6 | 3 | 12 |
| 3 | 3/21 | 21.33 | 21 | 18 | 25 |
| 4 | 0/21 | N/A | N/A | N/A | N/A |

Le voisinage 1 atteint plus rapidement la faisabilite en
nombre de generations, mais le voisinage 2 produit de
meilleures solutions finales.

Les statistiques de premiere faisabilite sont conditionnelles
aux executions ayant observe au moins un individu faisable.

Aucune configuration n'atteint l'optimum.

## 6. Diversite

| Voisinage | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 | 1 |
| 2 | 1 | 0.7804 | 1 | 1 |
| 3 | 1 | 0.9947 | 1 | 1 |
| 4 | 1 | 0.9974 | 1 | 1 |

Le voisinage 2 presente une diminution plus importante
de la diversite genotypique, tout en conservant une
diversite phenotypique maximale selon le collecteur.

Cette observation ne permet pas d'etablir une relation
causale entre diversite et qualite des solutions.

## 7. Effet de la recherche locale

### Initialisation

Les taux de faisabilite avant et apres la recherche locale
initiale sont nuls pour les quatre configurations.

### Croisement

| Voisinage | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 1 | 46.17 | 59.57 | 13.40 |
| 2 | 18.96 | 26.11 | 7.16 |
| 3 | 0.11 | 0.06 | -0.05 |
| 4 | 0 | 0 | 0 |

### Mutation

| Voisinage | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 1 | 34.92 | 54.95 | 20.02 |
| 2 | 23.81 | 40.26 | 16.45 |
| 3 | 0.15 | 0.21 | 0.06 |
| 4 | 0 | 0 | 0 |

### Redemarrage

| Voisinage | Avant (%) | Apres (%) |
|---:|---:|---:|
| 1 | 0 | 0.65 |
| 2 | N/A | N/A |
| 3 | N/A | N/A |
| 4 | 0 | 0 |

Les taux agreges dependent des populations rencontrees
pendant les executions.

## 8. Comparaison avec bench_2

Sur bench_2, les quatre tailles de voisinage atteignent
l'optimum pour les 21 graines.

Sur bench_3, aucune configuration n'atteint l'optimum.

Contrairement a bench_2, le voisinage 2 apporte une
amelioration importante de la qualite finale par rapport
au voisinage 1.

Les voisinages 3 et 4 degradent fortement la qualite
des solutions sur bench_3.

Une hypothese est que la complexite des sous-problemes
associes aux grands voisinages est trop importante
pour le budget deterministe utilise.

Cette hypothese necessite des verifications supplementaires.

## 9. Conclusion

Le voisinage 2 produit les meilleures solutions finales
parmi les configurations testees sur bench_3.

Le voisinage 1 reste nettement moins couteux en effort solveur.

Le choix entre les deux depend donc du compromis recherche
entre qualite des solutions et ressources de calcul.

Les voisinages 3 et 4 ne sont pas recommandes avec
les parametres experimentaux actuels.

Le voisinage 1 est conserve pour les prochaines series
afin de reproduire le protocole de bench_2.

## 10. Limites

- Le budget nominal exclut les redemarrages.
- Le temps solveur cumule ne mesure pas le temps avant
  l'obtention d'une solution de qualite donnee.
- Les raisons d'arret du solveur ne sont pas analysees.
- Les interactions entre voisinage et budget deterministe
  ne sont pas etudiees dans cette serie.
- Les conditions de parallelisation peuvent influencer
  les mesures temporelles.
- Aucun test statistique inferentiel n'a ete realise.

## 11. Reproductibilite

- Reference voisinage 1 : daaffa732dc66bc8a2273934aa47bdcc65b5d503.
- Voisinages 2, 3 et 4 : ab977345a09a06a59be7d7ecd20be8b84f010672.
- Git dirty : False pour toutes les executions.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_voisinage/.
- Script : experiments/analysis/analyze_bench3_neighborhood.py.

Commande de reproduction :

    python3 experiments/analysis/analyze_bench3_neighborhood.py
