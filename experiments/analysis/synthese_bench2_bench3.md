# Synthese comparative des experimentations sur bench_2 et bench_3

## 1. Objectif

Cette campagne experimentale vise a etudier l'influence
des principaux parametres de l'algorithme memetique
sur la qualite des solutions, la convergence,
la robustesse et l'effort computationnel.

La reproduction des experiences sur bench_3 permet
d'evaluer dans quelle mesure les observations
effectuees sur bench_2 se retrouvent sur une
instance plus complexe.

## 2. Instances etudiees

| Instance | Employes | Activites | Periodes | Optimum documente |
|---|---:|---:|---:|---:|
| bench_2 | 4 | 2 | 96 | 38 |
| bench_3 | 6 | 3 | 48 | 16 |

Bench_3 comporte davantage d'employes et d'activites,
mais moins de periodes.

Les resultats experimentaux montrent que cette
instance est plus difficile pour les configurations
de l'algorithme memetique etudiees.

## 3. Campagne experimentale

| Serie | Nouvelles executions bench_2 | Nouvelles executions bench_3 |
|---|---:|---:|
| Population et generations | 63 | 84 |
| Taille du voisinage | 63 | 63 |
| Seuil de stagnation | 63 | 63 |
| Budget deterministe | 63 | 63 |
| Interaction voisinage-budget | 0 | 63 |
| Ratio NR/NM | 42 | 42 |
| Validation des strategies | 21 | 21 |
| Operateurs de mutation | 42 | 42 |
| Recherche locale initiale | 21 | 21 |
| Total | 378 | 462 |

La campagne comprend 840 nouvelles executions,
auxquelles s'ajoutent les 21 executions de
reference initiales sur bench_2.

Chaque configuration est evaluee sur les graines
0 a 20.

Les experiences de reference sont reutilisees
entre les series lorsque les parametres correspondent.

Les comparaisons sont principalement realisees
en faisant varier un parametre a la fois.

Une serie supplementaire etudie l'interaction
entre le voisinage et le budget deterministe.

## 4. Indicateurs de performance

Les principaux indicateurs utilises sont :

- Cout final moyen, median, minimal et maximal.
- Ecart-type des couts.
- Taux de solutions optimales.
- Taux de solutions faisables.
- Taux de solutions sans violation quasi stricte.
- Generation de premiere faisabilite.
- Generation de premiere optimalite.
- Nombre de redemarrages.
- Nombre d'appels au solveur.
- Nombre de propagations.
- Temps solveur cumule.
- Diversite genotypique et phenotypique.
- Taux de faisabilite avant et apres recherche locale.

### Distinction entre faisabilite et violations quasi strictes

Une solution peut etre consideree comme faisable
par l'evaluateur tout en comportant des cellules
en violation quasi stricte.

Ces violations peuvent produire des couts
particulierement eleves.

Il est donc important de distinguer :

- La faisabilite selon l'evaluateur.
- La faisabilite sans violation quasi stricte.
- Le cout global.
- Le cout conditionnel aux solutions sans violation.

Les moyennes conditionnelles peuvent porter
sur des sous-ensembles differents de graines.

## 5. Population et nombre de generations

Le budget nominal est maintenu constant :

    Population + G * (2*NR + NM) = 486

Les redemarrages ne sont pas inclus dans ce budget.

Configurations comparees :

| Population | Generations | NR | NM |
|---:|---:|---:|---:|
| 6 | 80 | 2 | 2 |
| 18 | 26 | 6 | 6 |
| 54 | 8 | 18 | 18 |
| 162 | 2 | 54 | 54 |

### Bench_2

| Population | Optimums | Cout moyen | Temps solveur moyen (s) |
|---:|---:|---:|---:|
| 6 | 21/21 | 38.0000 | 3.3304 |
| 18 | 21/21 | 38.0000 | 4.5310 |
| 54 | 21/21 | 38.0000 | 4.9239 |
| 162 | 19/21 | 38.0952 | 6.5380 |

La population de 18 offre un compromis favorable
entre la convergence et l'effort computationnel.

La population de 6 demeure interessante pour
son faible effort solveur.

Les mesures temporelles de la population de 6
proviennent toutefois d'un environnement different.

### Bench_3

| Population | Faisables | Sans violation quasi stricte | Cout median | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|
| 6 | 21/21 | 20/21 | 39 | 125.1415 |
| 18 | 21/21 | 21/21 | 41 | 169.1851 |
| 54 | 21/21 | 19/21 | 50 | 311.8906 |
| 162 | 9/21 | 1/21 | 3000043 | 421.3081 |

Aucun optimum n'est atteint.

La population de 18 est la seule a produire
21 solutions finales sans violation quasi stricte.

La population de 6 obtient cependant un meilleur
cout median et un effort solveur inferieur.

### Conclusion comparative

Les populations tres grandes, associees a un
faible nombre de generations, sont moins
interessantes dans les conditions etudiees.

La population de 18 et les 26 generations
sont conservees comme configuration de reference.

Ce choix ne constitue pas une preuve
d'optimalite du couple population-generations.

## 6. Taille du voisinage

### Bench_2

| Voisinage | Optimums | Temps solveur moyen (s) |
|---:|---:|---:|
| 1 | 21/21 | 4.5310 |
| 2 | 21/21 | 48.9900 |
| 3 | 21/21 | 2691.4586 |
| 4 | 21/21 | 4547.1664 |

L'augmentation du voisinage ne permet pas
d'ameliorer la qualite finale, puisque toutes
les configurations atteignent l'optimum.

Elle augmente considerablement l'effort solveur.

Le voisinage de 1 est retenu.

### Bench_3

| Voisinage | Faisables | Sans violation quasi stricte | Cout moyen global | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|
| 1 | 21/21 | 21/21 | 41.2857 | 169.1851 |
| 2 | 21/21 | 21/21 | 23.1429 | 2166.1105 |
| 3 | 2/21 | 0/21 | 12285777.9048 | 2844.3828 |
| 4 | 0/21 | 0/21 | 19761964.8571 | 3196.1653 |

Le voisinage de 2 reduit le cout moyen de
43.95 % relativement au voisinage de 1.

Il multiplie toutefois le nombre de propagations
par environ 14.7 et le temps solveur par 12.8.

Les voisinages de 3 et 4 obtiennent de mauvais
resultats avec le budget deterministe etudie.

### Conclusion comparative

Le voisinage constitue un parametre majeur
de l'algorithme memetique.

Sur bench_2, le voisinage de 1 suffit.

Sur bench_3, le voisinage de 2 permet
d'ameliorer considerablement la qualite finale.

Le choix depend donc du compromis recherche
entre qualite et effort computationnel.

## 7. Seuil de stagnation

### Bench_2

| Stagnation | Optimums | Redemarrages moyens | Temps solveur moyen (s) |
|---:|---:|---:|---:|
| 3 | 21/21 | 5.71 | 6.4581 |
| 5 | 21/21 | 3.67 | 5.5892 |
| 10 | 21/21 | 1.67 | 4.5310 |
| 15 | 21/21 | 1.00 | 4.1674 |

### Bench_3

| Stagnation | Cout moyen | Redemarrages moyens | Temps solveur moyen (s) |
|---:|---:|---:|---:|
| 3 | 44.0476 | 2.95 | 288.0006 |
| 5 | 42.8571 | 1.62 | 230.8113 |
| 10 | 41.2857 | 0.43 | 169.1851 |
| 15 | 41.9524 | 0.05 | 150.8308 |

Toutes les configurations de cette serie sur
bench_3 produisent 21 solutions sans violation
quasi stricte.

### Conclusion comparative

Les seuils faibles provoquent davantage
de redemarrages et augmentent l'effort solveur.

Cette augmentation ne se traduit pas par une
amelioration systematique de la qualite finale.

Le seuil de 10 demeure un compromis favorable
sur les deux instances.

Le seuil de 15 constitue une alternative
interessante lorsque la reduction de l'effort
computationnel est prioritaire.

## 8. Budget deterministe

### Bench_2

Les budgets de 1, 2.5, 5 et 10 produisent
des resultats algorithmiques identiques
pour chacune des 21 graines avec le voisinage de 1.

Les mesures temporelles sont exclues
de cette equivalence.

Cela suggere que le budget de 1 est deja
suffisant pour cette configuration.

### Bench_3 avec voisinage de 1

| Budget | Sans violation quasi stricte | Cout median | Temps solveur moyen (s) |
|---:|---:|---:|---:|
| 1 | 19/21 | 38 | 153.1863 |
| 2.5 | 20/21 | 37 | 167.3158 |
| 5 | 21/21 | 41 | 169.1851 |
| 10 | 20/21 | 41 | 168.8520 |

Le budget de 5 est le seul a produire
21 solutions sans violation quasi stricte.

Les differences d'effort solveur restent
relativement faibles.

Contrairement a bench_2, les resultats
algorithmiques ne sont pas tous identiques
entre les budgets.

### Conclusion comparative

L'effet du budget deterministe depend
de l'instance et du voisinage.

Un budget de 5 constitue une valeur
de reference raisonnable, sans garantir
une meilleure performance dans tous les cas.

## 9. Interaction voisinage-budget sur bench_3

Une serie supplementaire est realisee
avec un voisinage de 2.

| Budget | Faisables | Sans violation quasi stricte | Cout moyen global | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|
| 1 | 2/21 | 0/21 | 12619114.1429 | 592.3647 |
| 2.5 | 20/21 | 17/21 | 476228.7619 | 1327.7831 |
| 5 | 21/21 | 21/21 | 23.1429 | 2166.1105 |
| 10 | 21/21 | 21/21 | 20.7619 | 3574.7291 |

Le passage du budget de 5 au budget de 10 :

- Reduit le cout moyen de 10.29 %.
- Reduit l'ecart absolu moyen a l'optimum de 33.33 %.
- Augmente les propagations de 65.52 %.
- Augmente le temps solveur de 65.03 %.

### Compromis qualite-effort

| Voisinage | Budget | Cout moyen | Ecart relatif moyen a l'optimum (%) | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|
| 1 | 5 | 41.2857 | 158.04 | 169.1851 |
| 2 | 5 | 23.1429 | 44.64 | 2166.1105 |
| 2 | 10 | 20.7619 | 29.76 | 3574.7291 |

Les trois configurations produisent 21 solutions
sans violation quasi stricte.

Le budget deterministe exerce une influence
beaucoup plus importante avec un voisinage de 2.

Cette interaction montre les limites d'une
analyse faisant varier un seul parametre a la fois.

L'hypothese selon laquelle les voisinages de
3 et 4 necessiteraient des budgets plus importants
reste a verifier.

## 10. Ratio entre croisements et mutations

Le nombre d'individus produits par generation
est maintenu constant :

    2*NR + NM = 18

### Bench_2

| NR/NM | Optimums | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|
| 3/12 | 21/21 | 4504181 | 4.0011 |
| 6/6 | 21/21 | 5982586 | 4.5310 |
| 8/2 | 21/21 | 6811474 | 5.0627 |

### Bench_3

| NR/NM | Sans violation quasi stricte | Cout moyen global | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|---:|
| 3/12 | 21/21 | 37.6667 | 296002741 | 147.3328 |
| 6/6 | 21/21 | 41.2857 | 338203861 | 169.1851 |
| 8/2 | 20/21 | 47654.5238 | 382996435 | 191.3800 |

### Conclusion comparative

Le ratio 3/12 reduit les propagations
sur les deux instances :

- Bench_2 : reduction de 24.7 %.
- Bench_3 : reduction de 12.5 %.

Il ameliore egalement le cout moyen global
de 8.77 % sur bench_3 relativement au ratio 6/6.

Le ratio 3/12 est retenu pour son compromis
entre qualite, robustesse et effort solveur.

Il constitue l'un des resultats les plus
coherents entre les deux instances.

## 11. Validation des strategies configurables

Sur bench_2, la validation compare les
resultats de reference avec ceux obtenus
apres l'introduction de l'architecture configurable.

Sur bench_3, la validation compare les strategies
implicites et explicites au sein de cette architecture.

| Instance | Paires identiques sur les champs compares |
|---|---:|
| bench_2 | 21/21 |
| bench_3 | 21/21 |

Aucune difference algorithmique n'est observee
sur les indicateurs compares.

Les mesures temporelles et les metadonnees
sont exclues.

Les strategies explicites sont conservees
pour faciliter la reproductibilite.

## 12. Operateurs de mutation

### Bench_2

| Mutation | Optimums | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|
| shift_start | 21/21 | 4504181 | 3.9497 |
| block_boundary | 21/21 | 4501841 | 4.1513 |
| activity | 21/21 | 6173928 | 4.7598 |

### Bench_3

| Mutation | Sans violation quasi stricte | Cout moyen global | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|---:|
| shift_start | 21/21 | 37.6667 | 296002741 | 147.3328 |
| block_boundary | 18/21 | 142893.0952 | 229880586 | 114.2875 |
| activity | 19/21 | 142893.3333 | 333750182 | 161.2507 |

### Conclusion comparative

Shift_start demeure le choix retenu.

Sur bench_2, il presente des performances
comparables a block_boundary.

Sur bench_3, il est le seul operateur
produisant 21 solutions sans violation quasi stricte.

Block_boundary reduit les propagations
de 22.34 % sur bench_3, mais presente
une robustesse finale inferieure.

Activity augmente l'effort solveur
sur les deux instances.

La comparaison d'une combinaison de plusieurs
operateurs de mutation reste une piste future.

## 13. Recherche locale initiale

Le parametre initial_local_search controle
la recherche locale a l'initialisation
et aux redemarrages.

Il ne desactive pas la recherche locale
apres les croisements et les mutations.

### Bench_2

| Configuration | Optimums | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|
| True | 21/21 | 4504181 | 3.9497 |
| False | 21/21 | 3606994 | 3.3728 |

### Bench_3

| Configuration | Sans violation quasi stricte | Cout moyen global | Propagations moyennes | Temps solveur moyen (s) |
|---|---:|---:|---:|---:|
| True | 21/21 | 37.6667 | 296002741 | 147.3328 |
| False | 19/21 | 95276.3810 | 277091944 | 135.9705 |

### Conclusion comparative

La desactivation reduit l'effort solveur
sur les deux instances.

Sur bench_2, elle ne compromet pas
l'optimalite finale.

Sur bench_3, elle produit deux solutions
avec violation quasi stricte et retarde
la premiere faisabilite en moyenne.

Le choix retenu est donc :

- Bench_2 : False.
- Bench_3 : True.

L'utilite de la recherche locale initiale
semble dependre de la difficulte de l'instance.

## 14. Observations transversales

### Qualite et effort computationnel

Une augmentation de l'effort solveur
ne garantit pas une meilleure qualite finale.

Les grands voisinages, les grandes populations
et les redemarrages frequents peuvent augmenter
considerablement l'effort sans ameliorer
les solutions.

Cependant, sur bench_3, l'augmentation
du voisinage de 1 a 2 avec un budget suffisant
permet une amelioration importante de la qualite.

### Diversite

La diversite demeure generalement elevee
pour les configurations etudiees.

Une diversite elevee ne garantit toutefois
ni la faisabilite ni l'optimalite.

### Recherche locale

La recherche locale apres croisement
et mutation ameliore generalement les
taux de faisabilite observes.

Les taux agreges dependent des populations
rencontrees pendant les executions.

Ils ne permettent pas d'isoler directement
l'efficacite intrinseque des operateurs.

### Robustesse

Les violations quasi strictes jouent un role
majeur dans l'evaluation des configurations
sur bench_3.

Le cout median et les couts conditionnels
doivent etre interpretes conjointement
avec la frequence des violations.

## 15. Recommandations

### Parametres communs retenus

| Parametre | Valeur de reference |
|---|---|
| Population | 18 |
| Generations | 26 |
| NR | 3 |
| NM | 12 |
| Stagnation | 10 |
| Taille du tournoi | 2 |
| Nombre d'elites | 1 |
| Croisement | uniform_gene |
| Mutation | shift_start |

Les valeurs de tournoi et d'elites sont
des parametres fixes du protocole et non
des valeurs optimisees experimentalement.

### Parametres dependant de l'instance

| Parametre | Bench_2 | Bench_3 |
|---|---|---|
| Voisinage | 1 | 1 ou 2 |
| Budget deterministe | 5 | 5 ou 10 selon le voisinage |
| Recherche locale initiale | False | True |

### Configuration economique validee sur bench_3

- Population : 18.
- Generations : 26.
- NR : 3.
- NM : 12.
- Voisinage : 1.
- Budget deterministe : 5.
- Stagnation : 10.
- Mutation : shift_start.
- Recherche locale initiale : True.

Resultats observes :

- 21/21 solutions sans violation quasi stricte.
- Cout moyen : 37.6667.
- Cout minimal : 22.
- Temps solveur moyen : 147.3328 secondes.

### Configuration orientee qualite validee sur bench_3

- Population : 18.
- Generations : 26.
- NR : 6.
- NM : 6.
- Voisinage : 2.
- Budget deterministe : 10.
- Stagnation : 10.
- Mutation : shift_start.
- Recherche locale initiale : True.

Resultats observes :

- 21/21 solutions sans violation quasi stricte.
- Cout moyen : 20.7619.
- Cout minimal : 17.
- Temps solveur moyen : 3574.7291 secondes.

Cette configuration presente le meilleur cout
moyen parmi les configurations etudiees sur bench_3.

La combinaison du voisinage de 2, du budget de 10
et du ratio 3/12 n'a pas ete testee conjointement.

Elle constitue une configuration candidate,
et non une configuration validee.

## 16. Limites de la campagne experimentale

- Seulement deux instances sont etudiees.
- Chaque configuration est evaluee sur 21 graines.
- Aucun optimum n'est atteint sur bench_3.
- Les comparaisons sont principalement unifactorielles.
- Le budget nominal exclut les redemarrages.
- Les interactions entre tous les parametres
  ne sont pas etudiees.
- Aucun test statistique inferentiel n'est realise.
- Les mesures temporelles peuvent dependre
  de l'environnement et de la charge machine.
- Le temps solveur cumule ne correspond pas
  necessairement au temps total d'execution.
- Les couts conditionnels peuvent porter sur
  des sous-ensembles differents de graines.
- Les effets de la recherche locale initiale
  et aux redemarrages ne sont pas isoles.

Les recommandations constituent des choix
experimentaux pour les conditions etudiees.

Elles ne garantissent pas l'optimalite
globale du parametrage.

## 17. Pistes d'experimentations futures

- Evaluer les configurations retenues sur bench_4
  et bench_5.
- Combiner le ratio 3/12 avec le voisinage de 2
  et un budget deterministe suffisant.
- Etudier des voisinages adaptatifs.
- Etudier des budgets deterministes adaptatifs.
- Combiner plusieurs operateurs de mutation.
- Etudier separement la recherche locale
  a l'initialisation et aux redemarrages.
- Comparer les configurations sous un budget
  computationnel total commun.
- Etudier le temps necessaire pour atteindre
  une qualite de solution donnee.

## 18. Reproductibilite

Les configurations, resultats JSON, scripts
d'analyse et rapports sont conserves dans
le depot Git.

Le journal experiments/EXPLOG.md documente
les executions et les syntheses des series.

La verification d'integrite sur bench_3 confirme :

- 462 configurations.
- 462 fichiers de resultats.
- Un resultat unique par configuration.
- Correspondance des graines et generations.
- Aucune erreur de lecture detectee.

Cette verification ne constitue pas une
reexecution des experiences.

Les rapports individuels fournissent les
details des parametres et des commits utilises.

## 19. Conclusion generale

Les experimentations montrent que certains
choix de parametrage restent pertinents
sur les deux instances, notamment le ratio
NR/NM de 3/12, le seuil de stagnation de 10
et l'operateur shift_start.

D'autres parametres, particulierement
le voisinage, le budget deterministe
et la recherche locale initiale, doivent
etre adaptes a l'instance et aux objectifs.

L'interaction voisinage-budget constitue
un resultat important de la campagne.

Elle montre qu'un parametre ne peut pas
toujours etre optimise independamment
des autres.

Les resultats permettent ainsi de proposer
des configurations de reference et des
compromis entre qualite et effort solveur,
tout en identifiant les limites de leur
generalisation.
