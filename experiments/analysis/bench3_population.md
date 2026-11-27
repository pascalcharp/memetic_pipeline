# Comparaison population-generations sur bench_3

## 1. Objectif

Reproduire le protocole experimental realise sur bench_2 afin
d'evaluer l'influence de la repartition du budget entre la taille
de population et le nombre de generations sur une autre instance.

L'instance bench_3 comporte 6 employes, 3 activites et 48 periodes.
Son optimum documente est de 16.

## 2. Protocole experimental

Les quatre configurations utilisent un budget nominal identique :

    B = population + generations * (2 * NR + NM) = 486

| Population | Generations | NR | NM | Budget nominal |
|---:|---:|---:|---:|---:|
| 6 | 80 | 2 | 2 | 486 |
| 18 | 26 | 6 | 6 | 486 |
| 54 | 8 | 18 | 18 | 486 |
| 162 | 2 | 54 | 54 | 486 |

Chaque configuration est evaluee avec les graines 0 a 20,
pour un total de 84 executions.

Les autres parametres sont fixes :

- Taille du voisinage : 1.
- Seuil de stagnation : 10.
- Budget deterministe : 5.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Mutation : shift_start.
- Recherche locale initiale : activee.

Le budget nominal exclut les individus generes lors des
redemarrages.

## 3. Qualite des solutions finales

La faisabilite correspond a l'absence de violations structurelles
et de violations de couverture au sens de CostBreakdown.is_feasible.

Les cellules quasi strictes sont comptabilisees separement.
Une solution peut etre declaree faisable tout en presentant
un cout tres eleve en raison de ces cellules.

| Population | Faisables | Faisables sans violation quasi stricte | Optimales |
|---:|---:|---:|---:|
| 6 | 21/21 | 20/21 | 0/21 |
| 18 | 21/21 | 21/21 | 0/21 |
| 54 | 21/21 | 19/21 | 0/21 |
| 162 | 9/21 | 1/21 | 0/21 |

### Couts globaux

| Population | Minimum | Maximum | Moyenne | Mediane | Ecart-type |
|---:|---:|---:|---:|---:|---:|
| 6 | 27 | 1000041 | 47658.05 | 39 | 212959.30 |
| 18 | 28 | 88 | 41.29 | 41 | 12.21 |
| 54 | 33 | 1000052 | 95286.76 | 50 | 293543.15 |
| 162 | 46 | 4000077 | 2619117.38 | 3000043 | 1045451.22 |

### Couts conditionnels aux solutions faisables sans violation quasi stricte

| Population | Nombre | Minimum | Maximum | Moyenne | Mediane | Ecart-type |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 20 | 27 | 47 | 38.90 | 38.5 | 5.86 |
| 18 | 21 | 28 | 88 | 41.29 | 41 | 12.21 |
| 54 | 19 | 33 | 71 | 48.79 | 46 | 8.62 |
| 162 | 1 | 46 | 46 | 46.00 | 46 | 0.00 |

Ces statistiques sont conditionnelles et ne portent pas
necessairement sur les memes graines.

L'ecart-type nul de la population 162 resulte de la presence
d'une seule solution satisfaisant les criteres.

### Violations moyennes

| Population | Cellules quasi strictes | Violations de couverture | Violations structurelles |
|---:|---:|---:|---:|
| 6 | 0.0476 | 0 | 0 |
| 18 | 0 | 0 | 0 |
| 54 | 0.0952 | 0 | 0 |
| 162 | 1.9524 | 0.6667 | 0 |

## 4. Effort du solveur

| Population | Appels moyens | Propagations moyennes | Temps solveur moyen (s) | Redemarrages moyens |
|---:|---:|---:|---:|---:|
| 6 | 508.14 | 256154316.48 | 125.14 | 4.43 |
| 18 | 493.29 | 338203861.14 | 169.19 | 0.43 |
| 54 | 486 | 617073541.29 | 311.89 | 0 |
| 162 | 486 | 836418418.90 | 421.31 | 0 |

La population 6 necessite environ 24.3 % moins de propagations
que la population 18, malgre un nombre moyen d'appels superieur.

Les configurations de grande population necessitent davantage
d'effort par appel en moyenne.

## 5. Convergence

| Population | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---:|---:|---:|---:|---:|
| 6 | 2.86 | 3 | 1 | 6 |
| 18 | 2.38 | 2 | 1 | 4 |
| 54 | 1.14 | 1 | 1 | 2 |
| 162 | 1.00 | 1 | 0 | 2 |

Toutes les executions ont observe au moins un individu faisable
dans la population.

Cependant, seulement 9 meilleures solutions finales sur 21
sont faisables pour la population 162.

La presence d'un individu faisable dans la population ne
garantit donc pas que la meilleure solution finale selon le
cout total soit faisable.

Aucune configuration n'atteint l'optimum de 16.
Les statistiques de premiere generation optimale et de budget
avant optimum ne sont donc pas disponibles.

## 6. Diversite

| Population | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---:|---:|---:|---:|---:|
| 6 | 1 | 0.9921 | 1 | 1 |
| 18 | 1 | 1 | 1 | 1 |
| 54 | 1 | 1 | 1 | 1 |
| 162 | 1 | 1 | 1 | 1 |

La diversite demeure elevee pour toutes les configurations.
Elle ne suffit toutefois pas a garantir la qualite des solutions.

## 7. Effet de la recherche locale

Les taux suivants correspondent a la faisabilite au sens de
CostBreakdown.is_feasible.

### Initialisation

| Population | Avant (%) | Apres (%) |
|---:|---:|---:|
| 6 | 0 | 0 |
| 18 | 0 | 0 |
| 54 | 0 | 0 |
| 162 | 0 | 0.03 |

### Croisement

| Population | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 6 | 65.34 | 73.38 | 8.04 |
| 18 | 46.17 | 59.57 | 13.40 |
| 54 | 5.37 | 17.54 | 12.17 |
| 162 | 0.22 | 3.17 | 2.95 |

### Mutation

| Population | Avant (%) | Apres (%) | Gain (points) |
|---:|---:|---:|---:|
| 6 | 37.11 | 56.58 | 19.46 |
| 18 | 34.92 | 54.95 | 20.02 |
| 54 | 11.84 | 26.42 | 14.58 |
| 162 | 0.79 | 5.91 | 5.11 |

### Redemarrage

| Population | Avant (%) | Apres (%) |
|---:|---:|---:|
| 6 | 0 | 0 |
| 18 | 0 | 0.65 |
| 54 | N/A | N/A |
| 162 | N/A | N/A |

Les taux agreges dependent des populations rencontrees au cours
des generations. Ils ne permettent pas d'isoler completement
l'efficacite propre de la recherche locale.

## 8. Comparaison avec bench_2

| Population | Optimalite bench_2 (%) | Optimalite bench_3 (%) |
|---:|---:|---:|
| 6 | 100 | 0 |
| 18 | 100 | 0 |
| 54 | 100 | 0 |
| 162 | 90.48 | 0 |

Contrairement a bench_2, aucune configuration n'atteint
l'optimum sur bench_3 avec le budget nominal de 486.

Les configurations de petite population et de grand nombre
de generations obtiennent globalement de meilleurs resultats
que celles de grande population.

La population 6 presente le meilleur cout individuel,
le meilleur cout median global et le plus faible effort solveur.

La population 18 est la seule a produire systematiquement
des solutions faisables sans violation quasi stricte.

## 9. Conclusion

La population 18 est conservee comme reference pour les
prochaines series afin de reproduire le protocole de bench_2.

La population 6 constitue toutefois une alternative interessante
sur bench_3 en raison de son effort solveur inferieur et de
la qualite des solutions obtenues.

Les conclusions ne permettent pas d'affirmer qu'une
configuration domine toutes les autres sur tous les criteres.

## 10. Limites

- Le budget nominal exclut les redemarrages.
- La population, les generations, NR et NM varient conjointement.
- Les configurations de 8 et 2 generations ne peuvent pas
  atteindre le seuil de stagnation de 10 generations.
- Les moyennes globales sont fortement influencees par les
  violations et les couts quasi stricts.
- Les moyennes conditionnelles reposent sur des sous-ensembles
  de tailles differentes.
- Le temps solveur cumule ne correspond pas au temps necessaire
  pour atteindre une solution de qualite donnee.
- Aucun test statistique inferentiel n'a ete realise.
- Les conclusions restent propres aux configurations testees.

## 11. Reproductibilite

- Commit experimental : daaffa732dc66bc8a2273934aa47bdcc65b5d503.
- Git dirty : False pour les 84 executions.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_population/.
- Script : experiments/analysis/analyze_bench3_population.py.

Commande de reproduction de l'analyse :

    python3 experiments/analysis/analyze_bench3_population.py
