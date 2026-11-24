# Influence de la taille de la population et du nombre de générations

## 1. Objectif

Étudier l'influence de la répartition du budget de calcul entre
la taille de la population et le nombre de générations sur
les performances de l'algorithme mémétique pour bench_2.

L'optimum connu de cette instance est de 38.

## 2. Protocole expérimental

Quatre configurations sont comparées, chacune sur 21 graines
identiques (0 à 20), pour un total de 84 exécutions.

| Population | Générations | NR | NM | Budget nominal |
|---:|---:|---:|---:|---:|
| 6 | 80 | 2 | 2 | 486 |
| 18 | 26 | 6 | 6 | 486 |
| 54 | 8 | 18 | 18 | 486 |
| 162 | 2 | 54 | 54 | 486 |

Le budget nominal est défini par :

B = population + générations * (2 * NR + NM)

Les autres paramètres sont maintenus constants, notamment
la taille du voisinage (1) et le seuil de stagnation (10).

Les redémarrages ne sont pas inclus dans le budget nominal.

## 3. Performances globales

| Critère | Pop. 6 | Pop. 18 | Pop. 54 | Pop. 162 |
|---|---:|---:|---:|---:|
| Optimums atteints | 21/21 | 21/21 | 21/21 | 19/21 |
| Taux de succès (%) | 100 | 100 | 100 | 90,48 |
| Coût moyen | 38 | 38 | 38 | 38,0952 |
| Coût médian | 38 | 38 | 38 | 38 |
| Écart-type du coût | 0 | 0 | 0 | 0,2935 |
| Appels moyens au solveur | 517,19 | 514,33 | 486 | 486 |
| Propagations moyennes | 4124708 | 5982586 | 6785041 | 9786403 |
| Temps solveur moyen (s) | 3,3304 | 4,5310 | 4,9239 | 6,5380 |
| Redémarrages moyens | 6,24 | 1,67 | 0 | 0 |

Les populations de 6, 18 et 54 individus atteignent
systématiquement l'optimum sur les graines testées.

La population de 162 individus échoue à atteindre l'optimum
dans deux exécutions, malgré un budget nominal identique.

Le nombre de propagations augmente avec la taille de la
population. Un nombre inférieur d'appels au solveur ne
signifie donc pas nécessairement un effort de calcul inférieur.

## 4. Convergence

| Critère | Pop. 6 | Pop. 18 | Pop. 54 | Pop. 162 |
|---|---:|---:|---:|---:|
| Première génération réalisable moyenne | 1,67 | 1,00 | 0,76 | 0,33 |
| Première génération optimale moyenne | 18,43 | 4,48 | 2,14 | 1,42 |
| Première génération optimale médiane | 8 | 3 | 2 | 1 |
| Première génération optimale minimale | 2 | 1 | 1 | 1 |
| Première génération optimale maximale | 68 | 17 | 6 | 2 |
| Budget nominal moyen avant optimum | 116,57 | 98,57 | 169,71 | 392,21 |
| Budget nominal médian avant optimum | 54 | 72 | 162 | 324 |

Les statistiques relatives à l'optimum sont calculées
uniquement sur les exécutions ayant atteint le coût de 38.

La population de 18 individus minimise le budget nominal
moyen nécessaire pour atteindre l'optimum.

Comparativement à la population de 6 individus, elle réduit
ce budget moyen d'environ 15,4 %. La population de 6 conserve
cependant un meilleur budget médian.

Les grandes populations atteignent plus rapidement une
solution réalisable en nombre de générations, mais chaque
génération mobilise davantage d'individus.

## 5. Diversité

| Critère | Pop. 6 | Pop. 18 | Pop. 54 | Pop. 162 |
|---|---:|---:|---:|---:|
| Diversité génotypique initiale | 1 | 1 | 1 | 1 |
| Diversité génotypique finale | 0,9683 | 0,9762 | 0,9400 | 0,9985 |
| Diversité phénotypique initiale | 1 | 1 | 1 | 1 |
| Diversité phénotypique finale | 1 | 1 | 1 | 1 |

Toutes les configurations conservent une diversité élevée.

La population de 162 présente la diversité génotypique
finale la plus élevée, mais le taux d'optimalité le plus faible.

Une diversité élevée ne garantit donc pas à elle seule
l'obtention de meilleures solutions.

## 6. Influence de la recherche locale

Les taux suivants sont agrégés sur les 21 exécutions
de chaque configuration.

### Croisement

| Population | Avant (%) | Après (%) | Gain (points) |
|---:|---:|---:|---:|
| 6 | 53,05 | 69,18 | 16,13 |
| 18 | 29,35 | 50,64 | 21,29 |
| 54 | 17,49 | 39,63 | 22,14 |
| 162 | 2,29 | 14,18 | 11,88 |

### Mutation

| Population | Avant (%) | Après (%) | Gain (points) |
|---:|---:|---:|---:|
| 6 | 72,77 | 79,40 | 6,64 |
| 18 | 63,58 | 71,95 | 8,36 |
| 54 | 53,47 | 64,98 | 11,51 |
| 162 | 9,30 | 27,12 | 17,81 |

La recherche locale améliore les taux de faisabilité
agrégés des individus issus du croisement et de la mutation
pour toutes les configurations.

Les configurations comportant davantage de générations
présentent des taux de faisabilité supérieurs. Cela pourrait
s'expliquer par l'amélioration progressive des populations.

Ces taux étant cumulatifs, ils dépendent également du nombre
de générations passées dans un état réalisable.

## 7. Conclusion

À budget nominal équivalent, une augmentation importante
de la taille de la population ne garantit pas une amélioration
des performances de l'algorithme mémétique.

La population de 18 individus avec 26 générations constitue
un compromis intéressant : elle atteint l'optimum dans les
21 exécutions et minimise le budget nominal moyen avant
son atteinte.

La population de 6 individus demeure intéressante puisqu'elle
présente le plus faible effort cumulé en propagations et
le meilleur budget médian avant optimum.

La configuration de 18 individus est retenue provisoirement
pour les prochaines expériences.

## 8. Limites expérimentales

- Les conclusions portent uniquement sur bench_2.
- La taille de la population, le nombre de générations et
  les nombres de croisements et de mutations varient ensemble.
  L'effet individuel de chaque paramètre ne peut être isolé.
- Les redémarrages entraînent des différences entre les
  budgets nominaux et les efforts réellement observés.
- Les configurations de 54 et 162 individus ne disposent pas
  d'assez de générations pour déclencher un redémarrage avec
  le seuil de stagnation fixé à 10.
- Le budget avant optimum est évalué à la génération où
  l'optimum est observé, sans inclure les redémarrages.
- Les statistiques de convergence excluent les exécutions
  n'ayant pas atteint l'optimum.
- Les temps de résolution sont indicatifs, puisque les
  environnements et conditions d'exécution diffèrent.

## 9. Reproductibilité

Configuration de référence (population 6) :
- Commit : e522073fce238287319580bb63634658e8524698
- Python : 3.13.3
- NumPy : 2.5.4
- Paquet Python MiniZinc : 0.10.0

Nouvelles configurations (populations 18, 54 et 162) :
- Commit : b242161e12089537eae14553a65dd4d3a7cdd9d0
- Python : 3.13.18
- NumPy : 2.5.5
- Paquet Python MiniZinc : 0.10.0

Aucune différence n'a été détectée entre les deux commits
dans les chemins src/, data/, requirements.txt et
experiments/drivers/.

Toutes les exécutions ont été effectuées avec git_dirty=False.

Les statistiques peuvent être reproduites depuis la racine
du dépôt avec la commande :

    python3 experiments/analysis/analyze_population.py

