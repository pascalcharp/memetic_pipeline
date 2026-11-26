# Analyse de la recherche locale initiale sur bench_3

## 1. Objectif

Evaluer l'influence de l'activation de la recherche
locale a l'initialisation et aux redemarrages.

Verifier si le choix effectue sur bench_2
demeure pertinent sur bench_3.

L'optimum documente de bench_3 est de 16.

## 2. Protocole experimental

Deux configurations sont comparees :

- initial_local_search = True
- initial_local_search = False

Chaque configuration est evaluee avec les graines 0 a 20.

La desactivation concerne la recherche locale
a l'initialisation et aux redemarrages, mais pas
apres les croisements et les mutations.

Parametres fixes :

- Population : 18.
- Generations : 26.
- NR : 3.
- NM : 12.
- Voisinage : 1.
- Stagnation : 10.
- Budget deterministe : 5.
- Taille du tournoi : 2.
- Nombre d'elites : 1.
- Croisement : uniform_gene.
- Mutation : shift_start.

Le budget nominal est de 486 individus,
hors redemarrages.

La serie comprend 42 executions, dont 21 nouvelles
executions et 21 references reutilisees.

## 3. Qualite des solutions finales

| Recherche locale initiale | Faisables | Sans violation quasi stricte | Optimales |
|---|---:|---:|---:|
| True | 21/21 | 21/21 | 0/21 |
| False | 21/21 | 19/21 | 0/21 |

### Couts globaux

| Configuration | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---|---:|---:|---:|---:|---:|
| True | 37.6667 | 38 | 22 | 51 | 8.8712 |
| False | 95276.3810 | 41 | 29 | 1000034 | 293541.8091 |

### Couts conditionnels aux solutions faisables sans violation quasi stricte

| Configuration | Nombre | Moyenne | Mediane | Minimum | Maximum | Ecart-type |
|---|---:|---:|---:|---:|---:|---:|
| True | 21 | 37.6667 | 38 | 22 | 51 | 8.8712 |
| False | 19 | 38.8421 | 40 | 29 | 48 | 5.5180 |

La desactivation produit deux solutions finales
avec violation quasi stricte.

La configuration True obtient egalement un meilleur
cout moyen conditionnel, mais les moyennes ne
portent pas sur les memes ensembles de graines.

### Violations moyennes

| Configuration | Cellules quasi strictes | Violations de couverture | Violations structurelles |
|---|---:|---:|---:|
| True | 0 | 0 | 0 |
| False | 0.0952 | 0 | 0 |

### Decomposition moyenne des couts

| Configuration | Sous-couverture | Surcouverture | Penalites |
|---|---:|---:|---:|
| True | 34.0000 | 3.6667 | 0 |
| False | 95273.8095 | 2.5714 | 0 |

### Ecarts conditionnels a l'optimum

| Configuration | Ecart absolu moyen | Ecart relatif moyen (%) |
|---|---:|---:|
| True | 21.6667 | 135.42 |
| False | 22.8421 | 142.76 |

Aucun optimum n'est atteint.

## 4. Effort du solveur

| Configuration | Redemarrages moyens | Appels moyens | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|---:|
| True | 0.29 | 490.8571 | 296002741.3810 | 147.3328 |
| False | 0.38 | 468.0000 | 277091944.4286 | 135.9705 |

La desactivation permet de reduire :

- Les appels solveur de 4.66 %.
- Les propagations de 6.39 %.
- Le temps solveur cumule de 7.71 %.

Ces economies s'accompagnent cependant d'une
deterioration de la qualite globale des solutions.

## 5. Convergence

| Configuration | Executions ayant observe un individu faisable | Premiere faisabilite moyenne | Mediane | Minimum | Maximum |
|---|---:|---:|---:|---:|---:|
| True | 21/21 | 1.76 | 2 | 1 | 4 |
| False | 21/21 | 2.57 | 2 | 1 | 5 |

La recherche locale initiale permet d'atteindre
une premiere solution faisable plus tot en moyenne.

## 6. Diversite

| Configuration | Genotypique initiale | Genotypique finale | Phenotypique initiale | Phenotypique finale |
|---|---:|---:|---:|---:|
| True | 1 | 0.9947 | 1 | 1 |
| False | 1 | 1 | 1 | 1 |

La diversite demeure tres elevee pour les
deux configurations selon les indicateurs utilises.

## 7. Effet de la recherche locale

### Initialisation et redemarrage

Avec True, les taux de faisabilite avant et apres
la recherche locale sont nuls a l'initialisation
et aux redemarrages.

Avec False, ces appels de recherche locale
sont absents.

L'absence de solutions faisables a l'initialisation
ne signifie pas necessairement que la recherche
locale est inutile.

Elle pourrait ameliorer les individus sans les
rendre faisables, facilitant ainsi leur evolution
dans les generations suivantes.

Cette hypothese n'est pas directement verifiee
par les indicateurs disponibles.

### Croisement

| Configuration | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| True | 44.90 | 58.52 | 13.61 |
| False | 41.79 | 57.11 | 15.32 |

### Mutation

| Configuration | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| True | 35.07 | 53.69 | 18.62 |
| False | 34.87 | 52.72 | 17.84 |

Ces taux agreges dependent des populations
rencontrees au cours des executions.

## 8. Comparaison avec bench_2

Effets de la desactivation de la recherche locale
initiale relativement a son activation :

| Indicateur | Bench_2 | Bench_3 |
|---|---:|---:|
| Reduction des appels solveur (%) | 9.29 | 4.66 |
| Reduction des propagations (%) | 19.92 | 6.39 |
| Reduction du temps solveur (%) | 14.61 | 7.71 |

Sur bench_2, la desactivation reduit l'effort
computationnel sans compromettre l'optimalite
des solutions finales.

Sur bench_3, la desactivation reduit egalement
l'effort computationnel, mais produit deux
solutions finales avec violation quasi stricte.

Le choix du parametre depend donc de l'instance
et du compromis recherche entre qualite et effort.

## 9. Conclusion

La configuration initial_local_search = True
est retenue sur bench_3.

Elle offre une meilleure robustesse observee,
un meilleur cout moyen global et une convergence
plus rapide vers une premiere solution faisable.

La configuration False demeure interessante
pour reduire l'effort computationnel.

Contrairement a bench_2, cette reduction ne
justifie pas la perte de qualite observee
lorsque la robustesse est prioritaire.

## 10. Limites

- Aucun optimum n'est atteint sur bench_3.
- Les couts conditionnels portent sur des
  sous-ensembles differents de graines.
- Les effets de la recherche locale a
  l'initialisation et aux redemarrages ne
  sont pas isoles.
- Les interactions avec les autres parametres
  ne sont pas etudiees dans cette serie.
- Aucun test statistique inferentiel n'est realise.
- Les conclusions concernent les configurations
  et les instances etudiees.

## 11. Reproductibilite

- True : 91aa95633017c9c6cc8001da885f1e595be8c4cd.
- False : f6df7af9769ea6386c39b78cf7713705410dac90.
- Git dirty : False.
- Python : 3.13.18.
- Paquet Python minizinc : 0.10.0.
- NumPy : 2.5.5.
- Configurations : experiments/config/bench3_initial_ls/.

Commande de reproduction :

    python3 experiments/analysis/analyze_bench3_initial_ls.py
