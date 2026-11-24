# Influence du seuil de stagnation sur bench_2

## 1. Objectif

Etudier l'influence de la frequence des redemarrages
sur la convergence, la diversite, la faisabilite
et l'effort de resolution de l'algorithme memetique.

## 2. Protocole experimental

Quatre seuils de stagnation sont compares : 3, 5, 10 et 15.

Les autres parametres sont conserves :

- Instance : bench_2.
- Population : 18.
- Generations : 26.
- Croisements : 6.
- Mutations : 6.
- Voisinage : 1.
- Nombre d'elites : 1.
- Taille du tournoi : 2.
- Temps deterministe : 5.
- Recherche locale a l'initialisation : activee.
- Graines : 0 a 20.
- Budget nominal : 486 individus, hors redemarrages.

Les 21 executions du seuil 10 sont reutilisees.
Les 63 autres executions sont nouvelles.

Au total, 84 executions sont analysees.

## 3. Performance finale

| Indicateur | S3 | S5 | S10 | S15 |
|---|---:|---:|---:|---:|
| Executions | 21 | 21 | 21 | 21 |
| Solutions realisables | 21 | 21 | 21 | 21 |
| Optimums | 21 | 21 | 21 | 21 |
| Taux de succes (%) | 100 | 100 | 100 | 100 |
| Cout moyen | 38 | 38 | 38 | 38 |
| Cout median | 38 | 38 | 38 | 38 |
| Ecart-type | 0 | 0 | 0 | 0 |
| Redemarrages moyens | 5.71 | 3.67 | 1.67 | 1 |
| Appels moyens | 583.14 | 548.33 | 514.33 | 503 |
| Propagations moyennes | 8955900 | 7442355 | 5982586 | 5412059 |
| Temps solveur moyen (s) | 6.4581 | 5.5892 | 4.531 | 4.1674 |

Toutes les configurations atteignent l'optimum de 38.

Les seuils faibles augmentent le nombre de redemarrages
et, par consequent, le nombre d'appels au solveur.

Le seuil 15 presente le plus faible effort cumule
sur les executions completes.

## 4. Convergence

| Indicateur | S3 | S5 | S10 | S15 |
|---|---:|---:|---:|---:|
| Premiere faisabilite moyenne | 1 | 1 | 1 | 1 |
| Premiere faisabilite mediane | 1 | 1 | 1 | 1 |
| Premiere generation optimale moyenne | 5.10 | 4.52 | 4.48 | 4.71 |
| Premiere generation optimale mediane | 3 | 3 | 3 | 3 |
| Premiere generation optimale minimale | 1 | 1 | 1 | 1 |
| Premiere generation optimale maximale | 20 | 15 | 17 | 22 |
| Budget nominal moyen avant optimum | 109.71 | 99.43 | 98.57 | 102.86 |
| Budget nominal median avant optimum | 72 | 72 | 72 | 72 |

Le seuil 10 obtient la meilleure convergence moyenne.

Le seuil 5 obtient le meilleur resultat dans le pire
cas observe, avec un optimum atteint au plus tard
a la generation 15.

Le seuil 3 ne presente pas d'avantage de convergence
malgre ses redemarrages plus frequents.

Les differences entre les seuils 5, 10 et 15 restent
faibles et leur significativite statistique n'est
pas etablie.

Le budget nominal exclut les individus generes
lors des redemarrages.

## 5. Diversite

| Indicateur | S3 | S5 | S10 | S15 |
|---|---:|---:|---:|---:|
| Genotypique initiale | 1 | 1 | 1 | 1 |
| Genotypique finale | 0.9974 | 0.9894 | 0.9762 | 0.9418 |
| Phenotypique initiale | 1 | 1 | 1 | 1 |
| Phenotypique finale | 1 | 1 | 1 | 1 |

Les seuils faibles maintiennent une diversite
genotypique finale plus elevee.

Les redemarrages frequents favorisent le renouvellement
de la population, sans ameliorer le taux de succes
sur cette instance.

La diversite phenotypique reste maximale pour
toutes les configurations.

## 6. Effet de la recherche locale

Pourcentage de solutions realisables apres recherche locale :

| Origine | S3 | S5 | S10 | S15 |
|---|---:|---:|---:|---:|
| Initialisation | 0.53 | 0.53 | 0.53 | 0.53 |
| Croisement | 33.67 | 43.09 | 50.64 | 54.50 |
| Mutation | 47.77 | 61.39 | 71.95 | 76.04 |
| Redemarrage | 1.08 | 0.84 | 0.84 | 0.28 |

Gain de faisabilite en points de pourcentage :

| Origine | S3 | S5 | S10 | S15 |
|---|---:|---:|---:|---:|
| Initialisation | 0.53 | 0.53 | 0.53 | 0.53 |
| Croisement | 17.41 | 19.61 | 21.29 | 21.43 |
| Mutation | 14.04 | 11.63 | 8.36 | 7.84 |
| Redemarrage | 1.08 | 0.84 | 0.84 | 0.28 |

Les seuils eleves sont associes a de meilleurs taux
de faisabilite apres croisement et mutation.

Une explication possible est que les redemarrages
frequents interrompent davantage l'exploitation
des solutions realisables deja presentes.

Les taux sont cumules sur l'ensemble des evenements.
Ils dependent donc aussi de l'etat des populations
avant chaque recherche locale.

## 7. Conclusion

Les quatre seuils permettent d'atteindre l'optimum
dans toutes les executions.

Les redemarrages frequents augmentent la diversite,
mais egalement l'effort de resolution.

Le seuil 10 est retenu provisoirement pour la suite,
car il offre un compromis entre convergence,
diversite et effort du solveur.

Le seuil 15 constitue une alternative interessante
pour reduire l'effort cumule des executions completes.

## 8. Limites

- Une seule instance est etudiee.
- Le nombre de generations est fixe.
- Le nombre reel d'individus generes varie selon
  le nombre de redemarrages.
- Le budget nominal exclut les redemarrages.
- Le temps cumule ne mesure pas directement le temps
  necessaire pour atteindre le premier optimum.
- Les conditions de concurrence sur le serveur peuvent
  influencer les mesures temporelles.
- Aucun test de significativite statistique n'est realise.
- Les conclusions doivent etre validees sur d'autres
  instances.

## 9. Reproductibilite

Script d'analyse :

    python3 experiments/analysis/analyze_stagnation.py

Configurations :

    experiments/config/bench2_population/
    experiments/config/bench2_stagnation/

Commits experimentaux :

- S10 : b242161e12089537eae14553a65dd4d3a7cdd9d0
- S3, S5 et S15 : a2ff03f18937a644776a20e33ceccdeebee02b1e

Environnement commun declare :

- Python 3.13.18.
- MiniZinc (paquet Python) 0.10.0.
- NumPy 2.5.5.
- Git dirty : False pour toutes les executions.

