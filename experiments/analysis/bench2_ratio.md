# Influence du ratio croisement-mutation sur bench_2

## 1. Objectif

Étudier l'influence du nombre de croisements (NR) et de mutations (NM)
sur la convergence, la qualité des solutions et l'effort du solveur,
en conservant la configuration retenue lors des séries précédentes.

## 2. Protocole expérimental

Les paramètres communs sont :

- Instance : bench_2, optimum connu de 38.
- Population : 18 individus.
- Nombre de générations : 26.
- Taille du voisinage : 1.
- Seuil de stagnation : 10.
- Budget déterministe : 5.
- Recherche locale à l'initialisation : activée.
- Graines : 0 à 20.

Trois configurations sont comparées :

| Configuration | NR | NM | Individus générés par génération |
|---|---:|---:|---:|
| Mutations favorisées | 3 | 12 | 18 |
| Référence | 6 | 6 | 18 |
| Croisements favorisés | 8 | 2 | 18 |

Le budget nominal est maintenu constant :

    2 * NR + NM = 18
    18 + 26 * 18 = 486

Chaque croisement produit deux individus et chaque mutation en produit un.
Les individus générés lors des redémarrages ne sont pas inclus dans
ce budget nominal.

Les valeurs étudiées sont exploratoires. Les 21 résultats de référence
sont repris de la série sur la population et le nombre de générations.
Cette série ajoute donc 42 nouvelles exécutions.

## 3. Qualité des solutions

| Indicateur | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Exécutions | 21 | 21 | 21 |
| Solutions optimales | 21 | 21 | 21 |
| Taux de succès | 100 % | 100 % | 100 % |
| Coût moyen | 38 | 38 | 38 |
| Coût médian | 38 | 38 | 38 |
| Écart-type | 0 | 0 | 0 |

Les trois configurations atteignent systématiquement l'optimum.
Le ratio croisement-mutation n'a donc pas d'effet observable sur
la qualité finale des solutions dans les conditions étudiées.

## 4. Convergence

### Première génération faisable

| Indicateur | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Moyenne | 1,14 | 1,00 | 1,05 |
| Médiane | 1 | 1 | 1 |
| Minimum | 0 | 0 | 0 |
| Maximum | 2 | 2 | 2 |

### Première génération optimale

| Indicateur | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Moyenne | 4,24 | 4,48 | 4,90 |
| Médiane | 4 | 3 | 4 |
| Minimum | 1 | 1 | 2 |
| Maximum | 8 | 17 | 11 |

La configuration favorisant les mutations atteint l'optimum légèrement
plus rapidement en moyenne. Elle présente également le meilleur
maximum observé sur les 21 graines.

La configuration de référence conserve toutefois la meilleure médiane.
Les différences moyennes restent relativement faibles.

### Budget nominal jusqu'au premier optimum observé

| Indicateur | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Moyenne | 94,29 | 98,57 | 106,29 |
| Médiane | 90 | 72 | 90 |
| Minimum | 36 | 36 | 54 |
| Maximum | 162 | 324 | 216 |

Ce budget est calculé à partir de la première génération où l'optimum
est observé. Il ne représente pas le nombre exact d'individus évalués
avant sa découverte, notamment en raison des redémarrages et de
l'observation en fin de génération.

## 5. Effort cumulé du solveur

| Indicateur moyen | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Appels au solveur | 515,95 | 514,33 | 513,52 |
| Propagations | 4 504 181 | 5 982 586 | 6 811 474 |
| Temps de résolution (s) | 4,0011 | 4,5310 | 5,0627 |
| Redémarrages | 1,76 | 1,67 | 1,62 |

Le nombre moyen d'appels au solveur varie très peu entre les
configurations.

En revanche, favoriser les mutations réduit le nombre moyen de
propagations de 24,7 % par rapport à la référence. Le temps cumulé
de résolution diminue également de 11,7 %.

Favoriser les croisements augmente l'effort moyen du solveur.

L'effet du ratio semble donc plus prononcé sur l'effort nécessaire
à la recherche locale que sur la qualité finale des solutions.

Ces mesures couvrent les 26 générations complètes et non uniquement
la période précédant la découverte du premier optimum.

## 6. Diversité

| Indicateur moyen | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Diversité génotypique initiale | 1 | 1 | 1 |
| Diversité génotypique finale | 0,9735 | 0,9762 | 0,9683 |
| Diversité phénotypique initiale | 1 | 1 | 1 |
| Diversité phénotypique finale | 1 | 1 | 1 |

La diversité demeure élevée pour les trois configurations.
Favoriser les mutations ne semble pas entraîner de perte importante
de diversité selon les indicateurs observés.

## 7. Influence de la recherche locale

Les taux suivants sont calculés en regroupant les individus observés
sur l'ensemble des 21 exécutions de chaque configuration.

### Faisabilité avant et après la recherche locale

| Origine | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Initialisation avant | 0 % | 0 % | 0 % |
| Initialisation après | 0,53 % | 0,53 % | 0,53 % |
| Croisement avant | 29,18 % | 29,35 % | 32,11 % |
| Croisement après | 48,53 % | 50,64 % | 53,37 % |
| Mutation avant | 67,37 % | 63,58 % | 60,71 % |
| Mutation après | 75,69 % | 71,95 % | 71,98 % |
| Restart avant | 0 % | 0 % | 0 % |
| Restart après | 1,11 % | 0,84 % | 0,35 % |

### Gain de faisabilité

| Origine | NR=3, NM=12 | NR=6, NM=6 | NR=8, NM=2 |
|---|---:|---:|---:|
| Initialisation | 0,53 pt | 0,53 pt | 0,53 pt |
| Croisement | 19,35 pts | 21,29 pts | 21,26 pts |
| Mutation | 8,32 pts | 8,36 pts | 11,26 pts |
| Restart | 1,11 pt | 0,84 pt | 0,35 pt |

Les individus issus des mutations présentent des taux de faisabilité
plus élevés avant et après la recherche locale que ceux issus des
croisements.

Cela pourrait contribuer à expliquer la réduction de l'effort du
solveur lorsque les mutations sont favorisées. Cette hypothèse
n'établit toutefois pas de relation causale.

Les taux agrégés dépendent également de l'évolution des populations
au cours des générations.

## 8. Conclusion

Les trois ratios étudiés permettent d'atteindre l'optimum dans
100 % des exécutions.

La configuration NR=3 et NM=12 présente plusieurs avantages :

- Le plus faible effort cumulé du solveur.
- Le meilleur budget nominal moyen jusqu'au premier optimum observé.
- La meilleure génération optimale moyenne.
- Le plus faible maximum observé pour la génération optimale.
- Une diversité comparable aux autres configurations.

La configuration de référence conserve néanmoins une meilleure
convergence médiane.

Le ratio NR=3 et NM=12 est donc retenu provisoirement pour la suite
des expériences.

Configuration retenue :

| Paramètre | Valeur |
|---|---:|
| Population | 18 |
| Générations | 26 |
| NR | 3 |
| NM | 12 |
| Voisinage | 1 |
| Stagnation | 10 |
| Budget déterministe | 5 |

## 9. Limites

- Une seule instance est étudiée.
- Seulement trois ratios sont comparés.
- Les effets individuels de NR et NM ne sont pas isolés, puisque
  les deux paramètres varient simultanément.
- Le budget nominal exclut les redémarrages.
- Le temps de résolution est une mesure non déterministe.
- L'effort cumulé ne mesure pas directement l'effort jusqu'au
  premier optimum.
- Aucun test statistique de significativité n'a été effectué.
- Les interactions avec les autres paramètres et opérateurs
  restent à étudier.

Les conclusions sont exploratoires et devront être validées
sur d'autres instances.

## 10. Reproductibilité

- Configurations : experiments/config/bench2_ratio/
- Référence : experiments/config/bench2_population/
- Résultats : experiments/results/
- Script : experiments/analysis/analyze_ratio.py
- Python : 3.13.18
- MiniZinc (paquet Python) : 0.10.0
- NumPy : 2.5.5
- Commit de référence : b242161
- Commit des nouvelles expériences : 38872e8
- Git dirty : false pour toutes les exécutions.

Aucune différence n'a été observée entre les deux commits dans
src/, data/, requirements.txt, experiments/drivers/ et Dockerfile.

Pour reproduire l'analyse :

    python3 experiments/analysis/analyze_ratio.py
