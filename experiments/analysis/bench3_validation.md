# Validation des strategies implicites et explicites sur bench_3

## 1. Objectif

Verifier que les strategies implicites et explicites
produisent les memes resultats au sein de la nouvelle
architecture.

Contrairement a la validation sur bench_2, cette
experience ne compare pas deux versions de l'architecture.

## 2. Protocole

Comparaison de 21 paires d'executions, avec les
graines 0 a 20.

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
- Recherche locale initiale : activee.

La configuration explicite utilise :

- Croisement : uniform_gene.
- Mutation : shift_start.

La configuration implicite omet le champ strategies
et utilise les strategies par defaut.

La serie comprend 21 nouvelles executions et
21 references reutilisees.

## 3. Resultats

| Indicateur | Paires differentes |
|---|---:|
| Parametres effectifs | 0/21 |
| Meilleure solution | 0/21 |
| Generations | 0/21 |
| Redemarrages | 0/21 |
| Statistiques des couts | 0/21 |
| Diversite | 0/21 |
| Taux de faisabilite | 0/21 |
| Appels solveur | 0/21 |
| Noeuds | 0/21 |
| Echecs | 0/21 |
| Propagations | 0/21 |

Les 21 paires sont identiques sur tous les
indicateurs compares.

## 4. Conclusion

L'equivalence entre les strategies implicites
et explicites est confirmee pour les 21 graines
et la configuration etudiee.

Les prochaines experiences utiliseront des
strategies explicites afin de faciliter
la reproductibilite.

## 5. Limites

- Les mesures temporelles et les metadonnees
  sont exclues de la comparaison.
- Une seule configuration algorithmique est testee.
- Cette validation ne compare pas l'ancienne
  architecture avec la nouvelle.

## 6. Reproductibilite

Configurations de reference :
experiments/config/bench3_ratio/.

Nouvelles configurations :
experiments/config/bench3_validation/.

Commande de reproduction :

    python3 experiments/analysis/analyze_bench3_validation.py
