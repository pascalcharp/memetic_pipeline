# Analyse comparative du temps deterministe sur bench_2

## 1. Objectif

Evaluer l'influence du budget de temps deterministe
accorde au solveur CP-SAT lors de chaque recherche locale.

L'objectif est de determiner si une augmentation de ce
budget ameliore la qualite des solutions, la convergence
ou la faisabilite des individus.

## 2. Protocole experimental

Les parametres suivants sont maintenus constants :

| Parametre | Valeur |
|---|---:|
| Instance | bench_2 |
| Population | 18 |
| Generations | 26 |
| Croisements | 6 |
| Mutations | 6 |
| Taille du voisinage | 1 |
| Seuil de stagnation | 10 |
| Graines | 0 a 20 |

Les budgets deterministes compares sont 1, 2.5, 5 et 10.

Le temps deterministe est une mesure interne de l'effort
de calcul de CP-SAT et ne correspond pas directement
a une duree en secondes.

Les 21 executions du budget 5 sont reutilisees de la
serie population-generations.

Les 63 autres executions sont nouvelles, pour un total
de 84 executions analysees.

## 3. Performance globale

| Indicateur | TD 1 | TD 2.5 | TD 5 | TD 10 |
|---|---:|---:|---:|---:|
| Executions | 21 | 21 | 21 | 21 |
| Optimums | 21 | 21 | 21 | 21 |
| Taux de succes (%) | 100 | 100 | 100 | 100 |
| Cout moyen | 38 | 38 | 38 | 38 |
| Cout median | 38 | 38 | 38 | 38 |
| Ecart-type du cout | 0 | 0 | 0 | 0 |
| Redemarrages moyens | 1.67 | 1.67 | 1.67 | 1.67 |
| Appels moyens au solveur | 514.33 | 514.33 | 514.33 | 514.33 |
| Propagations moyennes | 5982586 | 5982586 | 5982586 | 5982586 |
| Temps solveur moyen (s) | 4.6266 | 4.6417 | 4.5310 | 4.4983 |

Toutes les configurations atteignent systematiquement
l'optimum connu de 38.

Le nombre d'appels, le nombre de propagations et le
nombre de redemarrages sont identiques pour les quatre
configurations.

Les faibles variations du temps de resolution mesure
ne s'accompagnent d'aucune difference dans les autres
indicateurs d'effort.

## 4. Convergence

Les statistiques suivantes sont identiques pour les
quatre budgets deterministes.

| Indicateur | Moyenne | Mediane | Minimum | Maximum |
|---|---:|---:|---:|---:|
| Premiere generation realisable | 1 | 1 | 0 | 2 |
| Premiere generation optimale | 4.48 | 3 | 1 | 17 |
| Budget nominal avant optimum | 98.57 | 72 | 36 | 324 |

Le budget nominal est calcule a partir du nombre
d'individus generes, sans inclure les redemarrages.

L'augmentation du temps deterministe n'ameliore donc
pas la vitesse de convergence observee.

## 5. Diversite

| Indicateur | TD 1 | TD 2.5 | TD 5 | TD 10 |
|---|---:|---:|---:|---:|
| Diversite genotypique initiale | 1 | 1 | 1 | 1 |
| Diversite genotypique finale | 0.9762 | 0.9762 | 0.9762 | 0.9762 |
| Diversite phenotypique initiale | 1 | 1 | 1 | 1 |
| Diversite phenotypique finale | 1 | 1 | 1 | 1 |

Aucune influence du budget deterministe sur la
diversite des populations n'est observee.

## 6. Effet de la recherche locale

Les taux de faisabilite agreges sont identiques pour
les quatre configurations.

| Origine | Avant (%) | Apres (%) | Gain (points) |
|---|---:|---:|---:|
| Initialisation | 0 | 0.53 | 0.53 |
| Croisement | 29.35 | 50.64 | 21.29 |
| Mutation | 63.58 | 71.95 | 8.36 |
| Redemarrage | 0 | 0.84 | 0.84 |

L'augmentation du budget deterministe n'ameliore pas
la capacite observee de la recherche locale a produire
des individus realisables.

## 7. Verification individuelle

Une comparaison par graine a ete effectuee entre
chacun des budgets 1, 2.5 et 10 et le budget de
reference 5.

Les champs compares sont :

- meilleure solution ;
- nombre de generations ;
- nombre de redemarrages ;
- historique des statistiques de cout ;
- historique de diversite ;
- historique des taux de faisabilite ;
- nombre d'appels au solveur ;
- nombre de noeuds, lorsque disponible ;
- nombre d'echecs ;
- nombre de propagations.

| Comparaison | Graines comparees | Differences |
|---|---:|---:|
| TD 1 contre TD 5 | 21 | 0 |
| TD 2.5 contre TD 5 | 21 | 0 |
| TD 10 contre TD 5 | 21 | 0 |

L'identite des resultats ne se limite donc pas aux
statistiques agregees.

Le code source confirme egalement que le parametre
deterministic_time_units est transmis a
DeterministicTimeLimit lors de la construction du
solveur CP-SAT.

## 8. Interpretation et conclusion

Pour bench_2, avec un voisinage de taille 1, aucune
influence du temps deterministe n'est observee dans
l'intervalle teste.

Une explication probable est que les recherches locales
se terminent avant d'epuiser le budget deterministe,
meme lorsque celui-ci vaut 1.

Cette hypothese n'est toutefois pas directement
confirmee par les motifs d'arret individuels du solveur.

Le budget de 5 est conserve provisoirement pour les
experiences suivantes. Sa diminution ne procure aucun
gain mesurable sur les indicateurs d'effort observes.

Cette valeur conserve egalement une marge de calcul
pour des recherches locales potentiellement plus
complexes.

## 9. Limites

Les conclusions sont propres a bench_2, au voisinage
de taille 1 et aux autres parametres fixes.

Des voisinages plus grands ou des instances plus
complexes pourraient rendre le budget deterministe
plus contraignant.

Les valeurs inferieures a 1 n'ont pas ete testees.

Les differences de temps de resolution en secondes
peuvent notamment dependre des conditions d'execution
et de la charge du serveur.

## 10. Reproductibilite

- Commit de reference : b242161e12089537eae14553a65dd4d3a7cdd9d0
- Commit des nouvelles configurations : 405eb47b22bbad8f6d59d0e7214c5f1788438338
- Python : 3.13.18
- MiniZinc Python : 0.10.0
- NumPy : 2.5.5
- Git dirty : False pour toutes les executions

Aucune difference n'a ete detectee entre les deux
commits dans les chemins src/, data/, requirements.txt
et experiments/drivers/.

Les journaux individuels temporaires des 63 nouvelles
executions ne sont plus disponibles. Les fichiers JSON
originaux ont toutefois ete conserves et analyses.

Script d'analyse :

    python3 experiments/analysis/analyze_deterministic_time.py

