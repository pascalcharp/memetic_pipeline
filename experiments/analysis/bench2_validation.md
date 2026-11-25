# Validation de l'architecture configurable sur bench_2

## Objectif

Verifier que l'introduction des strategies configurables
(etape 10c) preserve le comportement algorithmique de
la configuration de reference retenue.

## Protocole

- Population : 18.
- Generations : 26.
- NR : 3.
- NM : 12.
- Voisinage : 1.
- Stagnation : 10.
- Budget deterministe : 5.
- Croisement : uniform_gene.
- Mutation : shift_start.
- Graines : 0 a 20.

Les 21 executions sont comparees graine par graine
aux resultats de la serie sur les ratios NR et NM.

## Resultats

| Indicateur | Nombre de differences |
|---|---:|
| Parametres | 0 |
| Meilleure solution | 0 |
| Generations | 0 |
| Redemarrages | 0 |
| Statistiques de cout | 0 |
| Diversite | 0 |
| Taux de faisabilite | 0 |
| Appels au solveur | 0 |
| Noeuds | 0 |
| Echecs | 0 |
| Propagations | 0 |

Les 21 executions atteignent l'optimum 38 avant et apres
l'introduction de la nouvelle architecture.

Les 21 paires d'executions sont identiques sur l'ensemble
des indicateurs compares.

Les temps de resolution et les metadonnees variables
sont exclus de la comparaison.

## Reproductibilite

- Ancien commit : 38872e8
- Nouveau commit : c833032
- Python : 3.13.18
- MiniZinc (paquet Python) : 0.10.0
- NumPy : 2.5.5
- Git dirty : false pour toutes les executions.

## Conclusion

L'architecture configurable preserve le comportement
algorithmique de la configuration de reference sur
bench_2 pour les 21 graines etudiees.

Les nouveaux resultats peuvent servir de reference
pour la comparaison des operateurs de mutation.

Cette validation ne constitue pas une preuve
d'equivalence pour toutes les instances et configurations.
