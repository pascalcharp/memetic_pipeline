# Mémétique contre CP-SAT seul sur bench_3, à effort égal (étape 10g)

## 1. Question

Question de Pascal (2026-11-26) : avec les configurations retenues par Mély, le mémétique réduit-il l'effort du
solveur par rapport à CP-SAT seul sur bench_3 (optimum 16) ?

Le chiffre du TP (16 prouvé en 1,9 s, 10,6 unités déterministes) vient de CP-SAT avec **8 threads**, dont le
portefeuille de stratégies (recherche à grand voisinage, LP, etc.) tourne en parallèle. Les sous-problèmes du
mémétique sont résolus avec **1 thread**. Pour comparer à conditions égales, il faut un témoin CP-SAT seul,
monothread, sous limite déterministe.

## 2. Protocole

- Driver `experiments/drivers/run_cpsat_alone.py` : instance complète, 1 thread, `max_deterministic_time` 5400,
  graine fixée ; toutes les solutions intermédiaires sont gardées, chacune avec l'effort (propagations,
  `solveTime`) dépensé jusqu'à elle.
- Deux modèles : `reference` (`horaire.mzn`, couverture « au moins 1 » dure, celui du TP) et `relaxed`
  (`horaire_assoupli.mzn`, couverture pénalisée, celui des sous-problèmes du mémétique). Graines 0, 1 et 2.
- Mémétique : les 21 configurations de bench_3 de Mély (21 graines chacune, `synthese_bench2_bench3.md`).
- Comparaison : pour chaque configuration du mémétique, effort médian ; puis meilleur coût de CP-SAT seul au même
  effort. Script : `experiments/analysis/analyze_bench3_cpsat_alone.py`.
- Les coûts sont ceux de l'évaluateur : chaque cellule quasi stricte violée coûte 10⁶ (et, dans le modèle assoupli,
  chaque violation de couverture aussi). Un coût de l'ordre de 4 000 020 signifie donc 4 cellules en violation.

**Mesure d'effort principale : les propagations**, qui ne dépendent ni de la machine ni de sa charge. Le `solveTime`
n'est pas fiable ici : il dépasse la durée réelle des runs (par exemple 4608 s rapportées pour 3274 s écoulées,
référence graine 0), et le CPU était partagé (environ 56 % d'un cœur par processus au début). Il est donné à titre
indicatif seulement.

## 3. CP-SAT seul (1 thread, 5400 unités)

| Modèle | Graine | Première solution | Meilleur coût à 280 M propagations | Meilleur coût final | Propagations finales (M) | Prouvé |
|---|---:|---:|---:|---:|---:|---|
| reference | 0 | 20 000 100 | 6 000 070 | 4 000 020 | 887 | non |
| reference | 1 | 20 000 100 | 7 000 060 | 2 000 030 | 1 369 | non |
| reference | 2 | 20 000 100 | 9 000 060 | 6 000 020 | 1 095 | non |
| relaxed | 0 | 176 000 000 | 70 000 100 | 3 000 030 | 1 930 | non |
| relaxed | 1 | 176 000 000 | 79 000 100 | 14 000 000 | 2 102 | non |
| relaxed | 2 | 176 000 000 | 75 000 100 | 4 000 030 | 2 825 | non |

Aucune des six résolutions ne trouve une solution sans violation quasi stricte, même après environ 1 h de calcul
(5400 unités déterministes). La borne inférieure prouvée reste à 8–12 (modèle de référence), 0 (modèle assoupli).

## 4. À effort égal

Extraits (tableau complet : sortie du script).

| Configuration du mémétique | Coût médian (min) | Propagations médianes (M) | CP-SAT reference au même effort | CP-SAT relaxed au même effort |
|---|---:|---:|---|---|
| économique (3/12, voisinage 1, budget 5) | 38 (22) | 280 | 6 à 9 × 10⁶ | 7 à 8 × 10⁷ |
| pop 6, 80 gén. | 39 (27) | 248 | 6 à 9 × 10⁶ | 8 à 9 × 10⁷ |
| 8/2, voisinage 1 | 35 (21) | 355 | 5 à 8 × 10⁶ | 5 à 7 × 10⁷ |
| voisinage 2, budget 5 | 22 (17) | 4 964 | ≥ 2 à 6 × 10⁶ (fin du run) | ≥ 3 à 14 × 10⁶ (fin du run) |
| qualité (6/6, voisinage 2, budget 10) | 21 (17) | 8 162 | ≥ 2 à 6 × 10⁶ (fin du run) | ≥ 3 à 14 × 10⁶ (fin du run) |

« Fin du run » : le run de CP-SAT s'est arrêté avant cet effort ; son coût est celui de la fin du run. En
`solveTime` (indicatif), les runs couvrent l'effort de la configuration qualité (3600 s) : CP-SAT est alors à
2 à 14 × 10⁶.

**Effort de CP-SAT seul pour atteindre le coût médian du mémétique** : jamais, pour toutes les configurations dont
le coût médian est sans violation quasi stricte (de 21 à 50), sur les six résolutions. CP-SAT n'atteint que les
coûts médians des configurations qui échouent elles-mêmes (population 162 ; voisinages 3 et 4 ; voisinage 2 avec
budget 1).

## 5. Conclusion

- **Face à CP-SAT seul monothread, le mémétique réduit très fortement l'effort sur bench_3.** Avec 280 M de
  propagations, la configuration économique atteint un coût médian de 38 (min 22), sans violation quasi stricte
  sur les 21 graines ; CP-SAT seul, avec le même effort, a encore 6 à 9 cellules en violation (modèle de référence).
  Avec 3 à 10 fois plus d'effort (887 à 2 825 M), CP-SAT seul n'a toujours aucune solution sans violation.
- **L'objectif 2 de l'étape 10 est atteint sur bench_3**, dans les conditions définies : monothread, limite
  déterministe, effort mesuré par le solveur.
- **Le TP reste meilleur en temps écoulé** (16 prouvé en 1,9 s), mais avec 8 threads : la force de CP-SAT sur cette
  instance vient de son portefeuille parallèle (dont sa propre recherche à grand voisinage), pas de la recherche
  monothread par défaut. Le mémétique joue ici un rôle comparable à cette recherche à grand voisinage.
- Le modèle de référence fait mieux que le modèle assoupli pour CP-SAT seul, à propagations égales (la couverture
  dure élague) ; aucun des deux n'approche le mémétique.

## 6. Limites

- 3 graines par modèle pour CP-SAT seul (contre 21 pour le mémétique) ; l'écart est de plusieurs ordres de
  grandeur, ce qui suffit à conclure sans test statistique.
- Les séries de Mély ont tourné sur une autre machine : seule la comparaison en propagations est rigoureuse.
- Comparaison non faite : CP-SAT avec 8 threads à effort total égal (somme des threads). Elle demanderait une mesure
  d'effort multi-thread comparable (le temps déterministe de CP-SAT n'est pas rapporté par MiniZinc, D10).
- Les configurations à voisinage 2 dépensent plus de propagations que les runs CP-SAT n'en ont fait (ratio de
  propagations par seconde différent) ; pour elles, la comparaison en propagations est une borne.
