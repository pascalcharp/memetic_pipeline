# Influence de la taille du voisinage sur bench_2

## 1. Objectif

Etudier l'influence du nombre d'employes reoptimises lors
de la recherche locale sur la qualite des solutions,
la convergence, la diversite et l'effort du solveur.

## 2. Protocole experimental

Quatre tailles de voisinage sont comparees : 1, 2, 3 et 4.

Les autres parametres sont conserves :

- Instance : bench_2.
- Population : 18.
- Generations : 26.
- Croisements : 6.
- Mutations : 6.
- Seuil de stagnation : 10.
- Nombre d'elites : 1.
- Taille du tournoi : 2.
- Temps deterministe : 5.
- Recherche locale a l'initialisation : activee.
- Graines : 0 a 20.
- Budget nominal : 486 individus, hors redemarrages.

Les 21 executions du voisinage 1 proviennent de la serie
population-generations. Les 63 autres executions ont ete
realisees pour cette comparaison.

Au total, 84 executions sont analysees.

## 3. Performance finale

| Indicateur | V1 | V2 | V3 | V4 |
|---|---:|---:|---:|---:|
| Executions | 21 | 21 | 21 | 21 |
| Solutions realisables | 21 | 21 | 21 | 21 |
| Optimums | 21 | 21 | 21 | 21 |
| Taux de succes (%) | 100 | 100 | 100 | 100 |
| Cout moyen | 38 | 38 | 38 | 38 |
| Cout median | 38 | 38 | 38 | 38 |
| Ecart-type | 0 | 0 | 0 | 0 |
| Redemarrages moyens | 1.67 | 2 | 2 | 2 |
| Appels moyens | 514.33 | 520 | 520 | 520 |
| Propagations moyennes | 5982586 | 81465089 | 3947140467 | 3651318786 |
| Temps solveur moyen (s) | 4.531 | 48.990 | 2691.459 | 4547.166 |

Toutes les configurations atteignent l'optimum connu de 38.

Par rapport au voisinage 1, le temps cumule moyen du solveur
est multiplie par environ 10.8, 594 et 1004 pour les
voisinages 2, 3 et 4 respectivement.

Le nombre de propagations augmente egalement fortement,
bien que celui du voisinage 4 soit inferieur a celui du
voisinage 3.

## 4. Convergence

| Indicateur | V1 | V2 | V3 | V4 |
|---|---:|---:|---:|---:|
| Premiere faisabilite moyenne | 1 | 0 | 0 | 0 |
| Premiere faisabilite mediane | 1 | 0 | 0 | 0 |
| Premiere generation optimale moyenne | 4.48 | 0.76 | 0 | 0.14 |
| Premiere generation optimale mediane | 3 | 1 | 0 | 0 |
| Premiere generation optimale maximale | 17 | 2 | 0 | 1 |
| Budget nominal moyen avant optimum | 98.57 | 31.71 | 18 | 20.57 |
| Budget nominal median avant optimum | 72 | 36 | 18 | 18 |

Les voisinages 2, 3 et 4 produisent une solution realisable
des l'initialisation dans toutes les executions.

Le voisinage 3 atteint systematiquement l'optimum des
la generation 0.

Le voisinage 4 atteint l'optimum a la generation 0 dans
18 executions sur 21, et a la generation 1 dans les
trois autres.

Les grands voisinages accelerent donc la convergence
mesuree en generations et en individus generes.

Toutefois, le budget nominal ne tient pas compte du cout
de chaque appel au solveur ni des redemarrages.

## 5. Diversite

| Indicateur | V1 | V2 | V3 | V4 |
|---|---:|---:|---:|---:|
| Genotypique initiale | 1 | 1 | 0.9974 | 0.7407 |
| Genotypique finale | 0.9762 | 0.8386 | 0.9101 | 0.8677 |
| Phenotypique initiale | 1 | 1 | 1 | 0.7804 |
| Phenotypique finale | 1 | 1 | 1 | 1 |

Le voisinage 4 presente une diversite initiale plus faible.

Le voisinage 1 conserve la meilleure diversite genotypique
finale. La diversite phenotypique finale est maximale
pour les quatre configurations.

## 6. Effet de la recherche locale

Pourcentage de solutions realisables apres recherche locale :

| Origine | V1 | V2 | V3 | V4 |
|---|---:|---:|---:|---:|
| Initialisation | 0.53 | 22.49 | 70.11 | 20.11 |
| Croisement | 50.64 | 84.74 | 99.69 | 24.82 |
| Mutation | 71.95 | 95.42 | 99.24 | 31.47 |
| Redemarrage | 0.84 | 23.81 | 68.07 | 18.35 |

Gain de faisabilite en points de pourcentage :

| Origine | V1 | V2 | V3 | V4 |
|---|---:|---:|---:|---:|
| Initialisation | 0.53 | 22.49 | 70.11 | 20.11 |
| Croisement | 21.29 | 57.11 | 75.35 | 9.26 |
| Mutation | 8.36 | 7.78 | 1.71 | 0 |
| Redemarrage | 0.84 | 23.81 | 68.07 | 18.35 |

Le voisinage 3 obtient les meilleurs taux de faisabilite
apres recherche locale pour toutes les origines.

Le voisinage 4 est moins performant sur cet indicateur.
Une hypothese est que la limite de temps deterministe
restreint davantage la resolution des sous-problemes
les plus complexes. Cette hypothese reste a verifier.

Les taux sont cumules sur l'ensemble des evenements.
Ils dependent donc aussi de l'etat des populations
avant chaque recherche locale.

## 7. Conclusion

Augmenter la taille du voisinage accelere la convergence
en nombre de generations, mais augmente considerablement
l'effort cumule du solveur.

Le voisinage 1 atteint le meme optimum que les autres
configurations avec un effort de resolution nettement
inferieur sur les executions completes.

Il est donc retenu provisoirement pour les prochaines
series experimentales sur bench_2.

Le voisinage 2 constitue une alternative interessante
pour accelerer la convergence en nombre de generations.

## 8. Limites

- Une seule instance est etudiee.
- Le nombre de generations est fixe.
- Le nombre reel d'appels varie avec les redemarrages.
- Le temps cumule du solveur ne correspond pas au temps
  necessaire pour atteindre le premier optimum.
- Les conditions de concurrence sur le serveur peuvent
  influencer les mesures temporelles.
- Les executions ne permettent pas de generaliser
  directement les conclusions aux instances plus grandes.
- La cause de la baisse de faisabilite du voisinage 4
  n'est pas demontree.

## 9. Reproductibilite

Script d'analyse :

    python3 experiments/analysis/analyze_neighborhood.py

Configurations :

    experiments/config/bench2_population/
    experiments/config/bench2_voisinage/

Commits experimentaux :

- V1 : b242161e12089537eae14553a65dd4d3a7cdd9d0
- V2 a V4 : 94989faaf4ace2a42ab0059cb5d81d7840ff1b0e

Environnement commun declare :

- Python 3.13.18.
- MiniZinc (paquet Python) 0.10.0.
- NumPy 2.5.5.
- Git dirty : False pour toutes les executions.

