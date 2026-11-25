# Analyse comparative des operateurs de mutation sur bench_2

## 1. Objectif

Comparer l'influence des trois operateurs de mutation
disponibles dans l'architecture configurable sur la qualite
des solutions, la convergence, la diversite et l'effort
du solveur.

## 2. Protocole experimental

Les parametres suivants sont fixes :

| Parametre | Valeur |
|---|---|
| Instance | bench_2 |
| Population | 18 |
| Generations | 26 |
| NR | 3 |
| NM | 12 |
| Voisinage | 1 |
| Stagnation | 10 |
| Budget deterministe | 5 |
| Taille du tournoi | 2 |
| Nombre d'elites | 1 |
| Recherche locale initiale | Activee |
| Croisement | uniform_gene |
| Graines | 0 a 20 |

Trois operateurs sont compares :

- shift_start : deplacement du quart entier.
- block_boundary : modification de la frontiere entre
  deux blocs consecutifs.
- activity : modification de l'activite d'un bloc.

Chaque configuration est executee avec 21 graines.

Les 21 executions de validation de l'architecture configurable
sont reutilisees comme reference pour shift_start.

Au total, 63 executions sont analysees, dont 42 nouvelles.

Le budget nominal est identique pour les trois configurations :

18 + 26 * (2 * 3 + 12) = 486 individus.

Ce budget exclut les individus generes lors des redemarrages.

## 3. Qualite des solutions et effort du solveur

| Indicateur | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Executions | 21 | 21 | 21 |
| Solutions optimales | 21 | 21 | 21 |
| Taux de succes (%) | 100 | 100 | 100 |
| Cout moyen | 38 | 38 | 38 |
| Cout median | 38 | 38 | 38 |
| Ecart-type | 0 | 0 | 0 |
| Redemarrages moyens | 1.76 | 1.71 | 1.52 |
| Appels moyens au solveur | 515.95 | 515.14 | 511.90 |
| Propagations moyennes | 4504181.14 | 4501841.05 | 6173928.29 |
| Temps solveur moyen (s) | 3.9497 | 4.1513 | 4.7598 |

Les trois operateurs atteignent systematiquement
l'optimum connu de 38.

Les operateurs shift_start et block_boundary presentent
un effort de propagation pratiquement identique.

Activity necessite environ 37.1 % plus de propagations
que shift_start, malgre un nombre legerement inferieur
d'appels au solveur.

Le temps de resolution cumule est egalement plus eleve
pour activity.

## 4. Convergence

### Premiere generation faisable

| Indicateur | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Moyenne | 1.14 | 1.05 | 1.10 |
| Mediane | 1 | 1 | 1 |
| Minimum | 0 | 0 | 0 |
| Maximum | 2 | 2 | 2 |

### Premiere generation optimale

| Indicateur | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Moyenne | 4.24 | 4.24 | 5.29 |
| Mediane | 4 | 4 | 4 |
| Minimum | 1 | 1 | 2 |
| Maximum | 8 | 9 | 13 |

### Budget nominal avant le premier optimum observe

| Indicateur | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Moyenne | 94.29 | 94.29 | 113.14 |
| Mediane | 90 | 90 | 90 |
| Minimum | 36 | 36 | 54 |
| Maximum | 162 | 180 | 252 |

Shift_start et block_boundary presentent une convergence
moyenne identique.

Activity necessite environ 20 % plus d'individus selon
le budget nominal moyen avant le premier optimum observe.

Shift_start presente le meilleur pire cas observe,
avec un optimum atteint au plus tard a la generation 8.

## 5. Diversite

| Indicateur | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Genotypique initiale | 1.0000 | 1.0000 | 1.0000 |
| Genotypique finale | 0.9735 | 0.9894 | 0.9841 |
| Phenotypique initiale | 1.0000 | 1.0000 | 1.0000 |
| Phenotypique finale | 1.0000 | 1.0000 | 1.0000 |

Les trois operateurs maintiennent une diversite elevee.

Block_boundary presente la diversite genotypique finale
la plus importante, sans amelioration observee du cout final.

## 6. Faisabilite et recherche locale

Les taux sont calcules en regroupant les individus
observes sur les 21 executions de chaque configuration.

### Initialisation

| Indicateur (%) | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Avant recherche locale | 0.00 | 0.00 | 0.00 |
| Apres recherche locale | 0.53 | 0.53 | 0.53 |

### Croisement

| Indicateur | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Avant (%) | 29.18 | 37.64 | 31.17 |
| Apres (%) | 48.53 | 57.97 | 52.47 |
| Gain (points) | 19.35 | 20.33 | 21.31 |

### Mutation

| Indicateur | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Avant (%) | 67.37 | 36.81 | 27.17 |
| Apres (%) | 75.69 | 59.68 | 56.24 |
| Gain (points) | 8.32 | 22.86 | 29.08 |

### Redemarrage

| Indicateur (%) | shift_start | block_boundary | activity |
|---|---:|---:|---:|
| Avant recherche locale | 0.00 | 0.00 | 0.00 |
| Apres recherche locale | 1.11 | 0.82 | 0.74 |

Shift_start presente les meilleurs taux de faisabilite
avant et apres la recherche locale appliquee aux mutations.

Block_boundary et activity beneficient davantage de
la recherche locale en termes de gain absolu.

Cependant, leurs taux apres recherche locale restent
inferieurs a celui de shift_start.

Ces observations ne permettent pas d'isoler completement
l'effet propre de chaque mutation, puisque les populations
evoluent differemment au fil des generations.

## 7. Interpretation

Les operateurs shift_start et block_boundary offrent
des performances globalement similaires sur bench_2.

Block_boundary modifie la repartition temporelle des blocs.
Cette modification peut notamment deplacer les pauses
ou le diner hors de leurs fenetres autorisees.

Shift_start conserve les durees des blocs et borne
le deplacement du quart selon les contraintes de debut
et de fin de l'instance.

Activity conserve les jalons temporels, mais modifie
la repartition des activites et donc potentiellement
la couverture des besoins.

Ces differences constituent des pistes d'explication
des resultats observes, sans etablir de lien causal
direct avec l'effort du solveur.

## 8. Conclusion

L'operateur shift_start est retenu provisoirement pour
la suite des experimentations.

Ce choix repose sur :

- Un taux d'optimalite de 100 %.
- Une convergence moyenne parmi les meilleures.
- Le meilleur pire cas de convergence observe.
- Un faible effort de propagation.
- Les meilleurs taux de faisabilite des mutations
  avant et apres recherche locale.

Block_boundary constitue toutefois une alternative
competitive sur cette instance.

Activity presente un effort solveur plus important
et une convergence moyenne moins rapide.

## 9. Limites

- Une seule instance est etudiee.
- Chaque configuration utilise 21 graines.
- Aucun test de significativite statistique n'est effectue.
- Les temps de resolution sont sensibles aux conditions
  d'execution et a la contention des ressources.
- L'effort solveur est cumule sur toute l'execution,
  et non uniquement jusqu'au premier optimum.
- Le budget nominal exclut les redemarrages.
- Les taux de faisabilite cumules dependent aussi
  de l'evolution des populations.
- Les resultats ne permettent pas de conclure sur
  une combinaison de plusieurs operateurs de mutation.

## 10. Reproductibilite

- Reference shift_start : commit c833032.
- Nouvelles mutations : commit 4478121.
- Python : 3.13.18.
- MiniZinc (paquet Python) : 0.10.0.
- NumPy : 2.5.5.
- Git dirty : false pour les 63 executions.

Aucune difference entre les deux commits dans src/,
data/, requirements.txt, experiments/drivers/ et Dockerfile.

Configurations :

- experiments/config/bench2_validation/
- experiments/config/bench2_mutation/

Script d'analyse :

    python3 experiments/analysis/analyze_mutation.py
