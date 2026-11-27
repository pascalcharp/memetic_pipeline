# Influence de la recherche locale initiale sur bench_2

## 1. Objectif

Evaluer l'influence du parametre initial_local_search
sur la qualite des solutions, la convergence, la diversite
et l'effort du solveur.

Ce parametre controle la recherche locale appliquee
aux individus generes lors de l'initialisation et
des redemarrages.

La recherche locale appliquee apres les croisements
et les mutations demeure active dans les deux configurations.

## 2. Protocole experimental

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
| Croisement | uniform_gene |
| Mutation | shift_start |
| Graines | 0 a 20 |

Deux configurations sont comparees :

- initial_local_search = True.
- initial_local_search = False.

Les 21 executions de validation des strategies configurables
sont reutilisees comme reference.

Au total, 42 executions sont analysees, dont 21 nouvelles.

Le budget nominal est de 486 individus dans les deux cas,
sans compter les individus generes lors des redemarrages.

## 3. Qualite des solutions et effort du solveur

| Indicateur | True | False |
|---|---:|---:|
| Executions | 21 | 21 |
| Solutions optimales | 21 | 21 |
| Taux de succes (%) | 100 | 100 |
| Cout moyen | 38 | 38 |
| Cout median | 38 | 38 |
| Ecart-type | 0 | 0 |
| Redemarrages moyens | 1.76 | 1.62 |
| Appels moyens au solveur | 515.95 | 468.00 |
| Propagations moyennes | 4504181.14 | 3606994.43 |
| Temps solveur moyen (s) | 3.9497 | 3.3728 |

Les deux configurations atteignent systematiquement
l'optimum connu de 38.

La desactivation de la recherche locale initiale
entraine les reductions suivantes :

- Appels au solveur : 9.3 %.
- Propagations : 19.9 %.
- Temps de resolution cumule : 14.6 %.

Aucune degradation de la qualite finale des solutions
n'est observee sur les 21 graines.

## 4. Convergence

### Premiere generation faisable

| Indicateur | True | False |
|---|---:|---:|
| Moyenne | 1.14 | 1.43 |
| Mediane | 1 | 1 |
| Minimum | 0 | 1 |
| Maximum | 2 | 2 |

### Premiere generation optimale

| Indicateur | True | False |
|---|---:|---:|
| Moyenne | 4.24 | 4.62 |
| Mediane | 4 | 4 |
| Minimum | 1 | 2 |
| Maximum | 8 | 8 |

### Budget nominal avant le premier optimum observe

| Indicateur | True | False |
|---|---:|---:|
| Moyenne | 94.29 | 101.14 |
| Mediane | 90 | 90 |
| Minimum | 36 | 54 |
| Maximum | 162 | 162 |

La recherche locale initiale permet une convergence
legerement plus rapide en moyenne.

Cependant, les deux configurations presentent la meme
generation optimale mediane et le meme pire cas observe.

Toutes les executions atteignent l'optimum au plus tard
a la generation 8.

## 5. Diversite

| Indicateur | True | False |
|---|---:|---:|
| Genotypique initiale | 1.0000 | 1.0000 |
| Genotypique finale | 0.9735 | 0.9656 |
| Phenotypique initiale | 1.0000 | 1.0000 |
| Phenotypique finale | 1.0000 | 1.0000 |

Les deux configurations maintiennent une diversite elevee.

La desactivation de la recherche locale initiale
n'ameliore pas la diversite initiale mesuree.

## 6. Faisabilite et recherche locale

Les taux sont calcules en regroupant les individus
observes sur les 21 executions de chaque configuration.

### Initialisation

| Indicateur (%) | True | False |
|---|---:|---:|
| Avant recherche locale | 0.00 | N/A |
| Apres recherche locale | 0.53 | N/A |

### Croisement

| Indicateur | True | False |
|---|---:|---:|
| Avant (%) | 29.18 | 28.75 |
| Apres (%) | 48.53 | 48.02 |
| Gain (points) | 19.35 | 19.26 |

### Mutation

| Indicateur | True | False |
|---|---:|---:|
| Avant (%) | 67.37 | 62.61 |
| Apres (%) | 75.69 | 69.86 |
| Gain (points) | 8.32 | 7.25 |

### Redemarrage

| Indicateur (%) | True | False |
|---|---:|---:|
| Avant recherche locale | 0.00 | N/A |
| Apres recherche locale | 1.11 | N/A |

N/A indique l'absence d'evenements de recherche locale
pour cette origine, et non un taux de faisabilite nul.

La recherche locale initiale est associee a des taux
de faisabilite plus eleves apres mutation.

Les differences observees apres croisement sont faibles.

## 7. Interpretation

Le parametre initial_local_search controle la recherche
locale appliquee aux individus initiaux et a ceux
generes lors des redemarrages.

Ce comportement est documente dans docs/HOWTO.md
et confirme par src/memetic/assembly.py, qui utilise
le meme initialiseur pour le moteur et le redemarrage.

Les economies observees ne proviennent donc pas
uniquement de la suppression de la recherche locale
a la generation initiale.

Le nombre de redemarrages varie egalement entre
les deux configurations.

La recherche locale apres croisement et mutation
semble suffisante pour atteindre l'optimum sur bench_2,
meme sans recherche locale lors de l'initialisation
et des redemarrages.

## 8. Conclusion

La configuration initial_local_search = False est
retenue provisoirement pour la suite des experimentations.

Ce choix repose sur :

- Un taux d'optimalite de 100 %.
- Une reduction de 19.9 % des propagations.
- Une reduction de 9.3 % des appels au solveur.
- Une reduction du temps de resolution cumule.
- Une convergence mediane identique.
- Le meme pire cas de convergence observe.

L'activation de la recherche locale initiale demeure
une alternative pertinente lorsque la rapidite de
convergence en nombre de generations est prioritaire.

## 9. Limites

- Une seule instance est etudiee.
- Chaque configuration utilise 21 graines.
- Aucun test de significativite statistique n'est effectue.
- Les effets de la recherche locale a l'initialisation
  et aux redemarrages ne sont pas isoles.
- Les temps de resolution sont sensibles aux conditions
  d'execution et a la contention des ressources.
- L'effort solveur est mesure sur l'execution complete,
  et non jusqu'au premier optimum.
- Le budget nominal exclut les redemarrages.
- Les taux de faisabilite cumules dependent aussi
  de l'evolution des populations.

## 10. Reproductibilite

- Reference True : commit c833032.
- Configuration False : commit 9440573.
- Python : 3.13.18.
- MiniZinc (paquet Python) : 0.10.0.
- NumPy : 2.5.5.
- Git dirty : false pour les 42 executions.

Aucune difference dans src/, data/, requirements.txt,
experiments/drivers/ et Dockerfile entre la reference
et le HEAD utilise lors de la verification.

Configurations :

- experiments/config/bench2_validation/
- experiments/config/bench2_initial_ls/

Script d'analyse :

    python3 experiments/analysis/analyze_initial_ls.py
