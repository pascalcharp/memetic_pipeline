# Journal des expériences

Une entrée par exécution de `python -m experiments.drivers.run_experiment`, ajoutée automatiquement. Les fichiers de résultats complets sont dans `experiments/results/<date>/`.

## 2026-11-22 15:16 — integration_bench1

Configuration de base : les réglages de la 9-intégration sur bench_1 (6 individus, NR = 2, NM = 2, 4 générations, stagnation d'une génération, graine 7). Sert de référence pour vérifier que le pipeline d'expériences fonctionne ; la 9-intégration y atteint l'optimum 94 avec un restart.

- Configuration : `experiments/config/integration_bench1.json`
- Résultats : `experiments/results/2026-11-22/integration_bench1_151611.json`
- Instance : bench_1 ; graine 7 ; population 6, NR = 2, NM = 2, 4 générations
- **Coût obtenu : 94** (faisable) ; 4 générations, 1 restart(s)
- **Effort cumulé du solveur** : 35 appels ; failures 118 ; propagations 237945 ; nodes non rapporté ; temps de résolution 0.2 s (non déterministe)
- Durée de l'exécution : 12.7 s ; commit `f3c2f3caeb7240689ee386c32eacd7522159f196`

## 2026-11-23 20:15 — bench2_seuil_s00

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 0. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s00.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s00_201535.json`
- Instance : bench_2 ; graine 0 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 7 restart(s)
- **Effort cumulé du solveur** : 521 appels ; failures 5372 ; propagations 3411080 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 251.4 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:15 — bench2_seuil_s01

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 1. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s01.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s01_201535.json`
- Instance : bench_2 ; graine 1 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 6181 ; propagations 4412334 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 249.3 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:15 — bench2_seuil_s02

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 2. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s02.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s02_201535.json`
- Instance : bench_2 ; graine 2 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 7118 ; propagations 4559906 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 249.9 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:15 — bench2_seuil_s03

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 3. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s03.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s03_201535.json`
- Instance : bench_2 ; graine 3 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 6604 ; propagations 3758691 ; nodes non rapporté ; temps de résolution 3.2 s (non déterministe)
- Durée de l'exécution : 249.3 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:15 — bench2_seuil_s04

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 4. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s04.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s04_201535.json`
- Instance : bench_2 ; graine 4 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 7 restart(s)
- **Effort cumulé du solveur** : 521 appels ; failures 6143 ; propagations 4331199 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 251.4 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:15 — bench2_seuil_s05

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 5. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s05.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s05_201535.json`
- Instance : bench_2 ; graine 5 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 7291 ; propagations 4785045 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 249.3 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:19 — bench2_seuil_s06

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 6. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s06.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s06_201945.json`
- Instance : bench_2 ; graine 6 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 5858 ; propagations 4104491 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 260.9 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:19 — bench2_seuil_s07

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 7. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s07.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s07_201945.json`
- Instance : bench_2 ; graine 7 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 7 restart(s)
- **Effort cumulé du solveur** : 521 appels ; failures 6208 ; propagations 4705421 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 263.4 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:19 — bench2_seuil_s08

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 8. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s08.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s08_201945.json`
- Instance : bench_2 ; graine 8 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 5876 ; propagations 3648608 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 260.9 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:19 — bench2_seuil_s09

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 9. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s09.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s09_201945.json`
- Instance : bench_2 ; graine 9 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 5746 ; propagations 3639031 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 261.2 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:19 — bench2_seuil_s10

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 10. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s10.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s10_201947.json`
- Instance : bench_2 ; graine 10 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 7520 ; propagations 4857123 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 261.6 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:19 — bench2_seuil_s11

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 11. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s11.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s11_201947.json`
- Instance : bench_2 ; graine 11 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 7125 ; propagations 4572259 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 258.6 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:24 — bench2_seuil_s12

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 12. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s12.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s12_202406.json`
- Instance : bench_2 ; graine 12 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 5329 ; propagations 3792868 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 261.3 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:24 — bench2_seuil_s13

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 13. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s13.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s13_202406.json`
- Instance : bench_2 ; graine 13 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 7 restart(s)
- **Effort cumulé du solveur** : 521 appels ; failures 6047 ; propagations 3751748 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 264.1 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:24 — bench2_seuil_s14

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 14. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s14.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s14_202406.json`
- Instance : bench_2 ; graine 14 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 7935 ; propagations 4286958 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 262.2 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:24 — bench2_seuil_s15

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 15. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s15.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s15_202407.json`
- Instance : bench_2 ; graine 15 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 7039 ; propagations 3424166 ; nodes non rapporté ; temps de résolution 3.2 s (non déterministe)
- Durée de l'exécution : 261.6 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:24 — bench2_seuil_s16

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 16. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s16.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s16_202409.json`
- Instance : bench_2 ; graine 16 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 7 restart(s)
- **Effort cumulé du solveur** : 521 appels ; failures 6347 ; propagations 4082735 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 263.8 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:24 — bench2_seuil_s17

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 17. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s17.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s17_202409.json`
- Instance : bench_2 ; graine 17 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 7 restart(s)
- **Effort cumulé du solveur** : 521 appels ; failures 5683 ; propagations 3641153 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 263.7 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:28 — bench2_seuil_s18

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 18. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s18.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s18_202828.json`
- Instance : bench_2 ; graine 18 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 5540 ; propagations 4290479 ; nodes non rapporté ; temps de résolution 2.7 s (non déterministe)
- Durée de l'exécution : 199.7 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:28 — bench2_seuil_s19

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 19. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s19.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s19_202829.json`
- Instance : bench_2 ; graine 19 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 5523 ; propagations 3747911 ; nodes non rapporté ; temps de résolution 2.5 s (non déterministe)
- Durée de l'exécution : 199.5 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 20:28 — bench2_seuil_s20

Seuil générationnel sur bench_2 (optimum prouvé 38) : réglages par défaut de l'assemblage (population 6, NR = 2, NM = 2, stagnation 10, voisinage 1), 80 générations, graine 20. On lit la première génération où le meilleur coût atteint 38 dans cost_statistics.

- Configuration : `experiments/config/bench2_seuil/bench2_seuil_s20.json`
- Résultats : `experiments/results/2026-11-23/bench2_seuil_s20_202829.json`
- Instance : bench_2 ; graine 20 ; population 6, NR = 2, NM = 2, 80 générations
- **Coût obtenu : 38** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 6525 ; propagations 4815654 ; nodes non rapporté ; temps de résolution 2.9 s (non déterministe)
- Durée de l'exécution : 199.3 s ; commit `e522073fce238287319580bb63634658e8524698`

## 2026-11-23 — Synthèse : seuil générationnel sur bench_2

Série `experiments/config/bench2_seuil/` (21 graines, 0 à 20 ; réglages par défaut : population 6, NR = 2, NM = 2, stagnation 10, voisinage 1 ; 80 générations ; commit `e522073`, copie de travail propre). Question (Mély, Pascal) : combien de générations faut-il pour atteindre l'optimum prouvé, 38 ? Mesure : la première génération où `total_min` de `cost_statistics` vaut 38. Comme une exécution est déterministe et que le nombre de générations n'en change pas le début, cette génération est aussi celle d'un essai plus court (vérifié sur les 21 graines contre des essais exploratoires à 6, 40 et 60 générations).

| Générations G | 2 | 4 | 6 | 8 | 10 | 15 | 20 | 30 | 40 | 60 | 80 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Graines ayant atteint 38 | 1 | 6 | 8 | 11 | 11 | 12 | 14 | 17 | 18 | 19 | 21 |

- **Les 21 graines atteignent l'optimum 38**, mais il n'y a pas de seuil net : génération du succès min 2, médiane 8, max 68 (graines 8, 11, 19 : 41, 62, 68). Environ 40 % de succès à 6 générations, 80 % à 30 : cohérent avec l'observation de Mély (échec à 6, succès à 30).
- **La faisabilité n'est pas en cause** : un horaire faisable apparaît dès la génération 0 à 4 pour toutes les graines. Les échecs temporaires sont des plateaux juste au-dessus de l'optimum (39, 40), qui durent jusqu'à 35 générations malgré 5 à 7 restarts (l'élite gardée au restart garde l'optimum local).
- **Effort cumulé du solveur pour 80 générations** : 511 à 521 appels, 2,5 à 3,8 s de temps de résolution, 3,4 à 4,9 M propagations. À comparer à CP-SAT seul sur le modèle dur : en monothread, pas de preuve en 200 unités déterministes (environ 150 s, 240 M propagations, meilleure solution 38) ; avec 8 threads (réglage du TP précédent), preuve en 1,0 à 1,5 s.
- Pistes : stagnation plus courte (3 ou 5), `neighborhood_size = 2`, puis population contre générations à nombre égal d'individus traités.

## 2026-11-24 16:03 — bench2_pop18_s00

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s00_160347.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8784 ; propagations 6596583 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 156.2 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s01

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s01_161045.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8940 ; propagations 6710191 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 198.2 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s02

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s02_161045.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8950 ; propagations 5922095 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 203.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s03

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s03_161046.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7401 ; propagations 5225477 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 197.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s04

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s04_161046.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7575 ; propagations 5051174 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 196.9 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s05

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s05_161045.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8436 ; propagations 6244840 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 204.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s06

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s06_161045.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7277 ; propagations 5001464 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 198.2 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s07

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s07_161046.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8945 ; propagations 6509362 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 204.7 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s08

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s08_161045.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8788 ; propagations 6354606 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 206.4 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s09

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s09_161046.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8118 ; propagations 5414001 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 205.4 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s10

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s10_161045.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9532 ; propagations 6757795 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 205.6 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s11

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s11_161046.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5939 ; propagations 4069242 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 196.7 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s12

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s12_161045.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8775 ; propagations 6157587 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 204.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s13

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s13_161046.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9203 ; propagations 6510006 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 204.9 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s14

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s14_161046.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9221 ; propagations 6769722 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 205.8 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s15

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s15_161045.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7205 ; propagations 4973883 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 198.3 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s16

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s16_161046.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8337 ; propagations 5892877 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 203.0 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s17

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s17_161046.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8001 ; propagations 5856102 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 204.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s18

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s18_161046.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8893 ; propagations 6357625 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 205.2 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s19

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s19_161045.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9625 ; propagations 6731378 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 206.6 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:10 — bench2_pop18_s20

Comparaison population-generations sur bench_2 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench2_population/bench2_pop18_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop18_s20_161045.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8304 ; propagations 6528298 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 204.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s00

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s00_161404.json`
- Instance : bench_2 ; graine 0 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9279 ; propagations 6819488 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 192.9 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s01

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s01_161404.json`
- Instance : bench_2 ; graine 1 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9639 ; propagations 6974773 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 194.4 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s02

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s02_161404.json`
- Instance : bench_2 ; graine 2 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9850 ; propagations 7158326 ; nodes non rapporté ; temps de résolution 5.2 s (non déterministe)
- Durée de l'exécution : 192.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s03

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s03_161404.json`
- Instance : bench_2 ; graine 3 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9475 ; propagations 6559113 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 192.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s04

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s04_161405.json`
- Instance : bench_2 ; graine 4 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9772 ; propagations 6897807 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 192.6 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s05

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s05_161405.json`
- Instance : bench_2 ; graine 5 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 8349 ; propagations 6261331 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 192.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s06

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s06_161409.json`
- Instance : bench_2 ; graine 6 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9665 ; propagations 6674371 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 192.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s07

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s07_161410.json`
- Instance : bench_2 ; graine 7 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9408 ; propagations 7184173 ; nodes non rapporté ; temps de résolution 5.2 s (non déterministe)
- Durée de l'exécution : 194.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s08

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s08_161411.json`
- Instance : bench_2 ; graine 8 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 7899 ; propagations 6233777 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 192.2 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s09

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s09_161411.json`
- Instance : bench_2 ; graine 9 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 8718 ; propagations 6579580 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 192.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s10

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s10_161411.json`
- Instance : bench_2 ; graine 10 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9369 ; propagations 6656463 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 193.8 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s11

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s11_161412.json`
- Instance : bench_2 ; graine 11 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9824 ; propagations 7326776 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 193.7 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s12

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s12_161412.json`
- Instance : bench_2 ; graine 12 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9056 ; propagations 6685402 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 192.7 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s13

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s13_161412.json`
- Instance : bench_2 ; graine 13 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 10118 ; propagations 7201430 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 192.3 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s14

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s14_161412.json`
- Instance : bench_2 ; graine 14 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 8522 ; propagations 6647124 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 193.0 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s15

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s15_161412.json`
- Instance : bench_2 ; graine 15 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9047 ; propagations 6595509 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 193.4 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s16

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s16_161413.json`
- Instance : bench_2 ; graine 16 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9606 ; propagations 6844514 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 193.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s17

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s17_161413.json`
- Instance : bench_2 ; graine 17 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 9753 ; propagations 6674927 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 191.9 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s18

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s18_161413.json`
- Instance : bench_2 ; graine 18 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 8866 ; propagations 6518776 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 192.7 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:14 — bench2_pop54_s19

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s19_161413.json`
- Instance : bench_2 ; graine 19 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 8722 ; propagations 6342271 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 191.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s00

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s00_161718.json`
- Instance : bench_2 ; graine 0 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11835 ; propagations 10198467 ; nodes non rapporté ; temps de résolution 6.8 s (non déterministe)
- Durée de l'exécution : 195.2 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s01

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s01_161718.json`
- Instance : bench_2 ; graine 1 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11797 ; propagations 9851204 ; nodes non rapporté ; temps de résolution 6.6 s (non déterministe)
- Durée de l'exécution : 195.8 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s02

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s02_161718.json`
- Instance : bench_2 ; graine 2 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11785 ; propagations 9846686 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 195.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s03

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s03_161718.json`
- Instance : bench_2 ; graine 3 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11298 ; propagations 9642380 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 194.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s04

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s04_161719.json`
- Instance : bench_2 ; graine 4 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 39** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 10980 ; propagations 9584517 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 194.3 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s05

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s05_161722.json`
- Instance : bench_2 ; graine 5 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11090 ; propagations 9893092 ; nodes non rapporté ; temps de résolution 7.0 s (non déterministe)
- Durée de l'exécution : 194.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s06

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s06_161724.json`
- Instance : bench_2 ; graine 6 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 10382 ; propagations 9330389 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 195.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s07

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s07_161724.json`
- Instance : bench_2 ; graine 7 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11483 ; propagations 9607367 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 194.6 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s08

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s08_161725.json`
- Instance : bench_2 ; graine 8 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11944 ; propagations 9989133 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 193.9 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s09

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s09_161726.json`
- Instance : bench_2 ; graine 9 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11415 ; propagations 10106851 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 194.3 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s10

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s10_161726.json`
- Instance : bench_2 ; graine 10 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11495 ; propagations 9454050 ; nodes non rapporté ; temps de résolution 6.6 s (non déterministe)
- Durée de l'exécution : 193.6 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s11

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s11_161726.json`
- Instance : bench_2 ; graine 11 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11089 ; propagations 9187454 ; nodes non rapporté ; temps de résolution 6.3 s (non déterministe)
- Durée de l'exécution : 194.6 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s12

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s12_161726.json`
- Instance : bench_2 ; graine 12 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 12158 ; propagations 9974083 ; nodes non rapporté ; temps de résolution 6.8 s (non déterministe)
- Durée de l'exécution : 194.8 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s13

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s13_161726.json`
- Instance : bench_2 ; graine 13 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 39** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11786 ; propagations 9914628 ; nodes non rapporté ; temps de résolution 6.6 s (non déterministe)
- Durée de l'exécution : 194.5 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s14

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s14_161727.json`
- Instance : bench_2 ; graine 14 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 12151 ; propagations 9792411 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 194.8 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s15

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s15_161727.json`
- Instance : bench_2 ; graine 15 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11525 ; propagations 9795331 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 193.3 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s16

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s16_161727.json`
- Instance : bench_2 ; graine 16 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11664 ; propagations 9918035 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 193.3 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s17

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s17_161727.json`
- Instance : bench_2 ; graine 17 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 13067 ; propagations 10578509 ; nodes non rapporté ; temps de résolution 7.1 s (non déterministe)
- Durée de l'exécution : 194.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop162_s18

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s18_161727.json`
- Instance : bench_2 ; graine 18 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11855 ; propagations 9819782 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 194.7 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:17 — bench2_pop54_s20

Comparaison population-generations sur bench_2 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench2_population/bench2_pop54_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop54_s20_161718.json`
- Instance : bench_2 ; graine 20 ; population 54, NR = 18, NM = 18, 8 générations
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 10336 ; propagations 7649927 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 193.1 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:20 — bench2_pop162_s19

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s19_162032.json`
- Instance : bench_2 ; graine 19 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11433 ; propagations 9286755 ; nodes non rapporté ; temps de résolution 5.2 s (non déterministe)
- Durée de l'exécution : 147.8 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 16:20 — bench2_pop162_s20

Comparaison population-generations sur bench_2 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench2_population/bench2_pop162_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_pop162_s20_162033.json`
- Instance : bench_2 ; graine 20 ; population 162, NR = 54, NM = 54, 2 générations
- **Coût obtenu : 38** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 11176 ; propagations 9743346 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 147.4 s ; commit `b242161e12089537eae14553a65dd4d3a7cdd9d0`

## 2026-11-24 — Synthèse : population contre générations sur bench_2

Série `experiments/config/bench2_population/` : 63 nouvelles
exécutions sur les graines 0 à 20, comparées aux 21 exécutions
de référence de `experiments/config/bench2_seuil/`.

Les quatre configurations disposent du même budget nominal
de 486 individus traités, hors redémarrages.

| Population | Générations | Optimums | Appels moyens | Budget nominal moyen avant optimum |
|---:|---:|---:|---:|---:|
| 6 | 80 | 21/21 | 517,19 | 116,57 |
| 18 | 26 | 21/21 | 514,33 | 98,57 |
| 54 | 8 | 21/21 | 486 | 169,71 |
| 162 | 2 | 19/21 | 486 | 392,21 |

- La population de 18 minimise le budget nominal moyen avant
  l'atteinte de l'optimum parmi les configurations testées.
- La population de 6 présente le plus faible nombre moyen
  de propagations et le meilleur budget nominal médian avant optimum.
- La population de 162 conserve une diversité élevée, mais
  échoue à atteindre l'optimum pour deux graines (4 et 13).
- La recherche locale améliore les taux de faisabilité agrégés
  après croisement et mutation pour toutes les configurations.
- Les redémarrages et les différences d'environnement limitent
  la comparaison directe de l'effort réel et des temps.

La configuration de population 18 est retenue provisoirement
pour les prochaines expériences.

Analyse détaillée : `experiments/analysis/bench2_population.md`.

Script de reproduction : `experiments/analysis/analyze_population.py`.

## 2026-11-24 16:46 — bench2_vois2_s00

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 0.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s00_164605.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 289255 ; propagations 79148485 ; nodes non rapporté ; temps de résolution 46.9 s (non déterministe)
- Durée de l'exécution : 250.1 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s01

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 1.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s01_164606.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 328030 ; propagations 83970606 ; nodes non rapporté ; temps de résolution 48.8 s (non déterministe)
- Durée de l'exécution : 252.2 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s02

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 2.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s02_164606.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 254001 ; propagations 74849242 ; nodes non rapporté ; temps de résolution 44.2 s (non déterministe)
- Durée de l'exécution : 247.7 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s03

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 3.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s03_164606.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 327814 ; propagations 80182584 ; nodes non rapporté ; temps de résolution 48.0 s (non déterministe)
- Durée de l'exécution : 249.7 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s04

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 4.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s04_164606.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 383202 ; propagations 91932428 ; nodes non rapporté ; temps de résolution 54.2 s (non déterministe)
- Durée de l'exécution : 256.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s05

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 5.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s05_164606.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 277696 ; propagations 77129158 ; nodes non rapporté ; temps de résolution 46.5 s (non déterministe)
- Durée de l'exécution : 249.1 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s06

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 6.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s06_164607.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 272476 ; propagations 77074438 ; nodes non rapporté ; temps de résolution 46.1 s (non déterministe)
- Durée de l'exécution : 248.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s07

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 7.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s07_164606.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 299417 ; propagations 81155342 ; nodes non rapporté ; temps de résolution 48.9 s (non déterministe)
- Durée de l'exécution : 252.0 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s08

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 8.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s08_164606.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 326601 ; propagations 84055502 ; nodes non rapporté ; temps de résolution 49.6 s (non déterministe)
- Durée de l'exécution : 252.5 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s09

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 9.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s09_164606.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 324161 ; propagations 82187865 ; nodes non rapporté ; temps de résolution 49.1 s (non déterministe)
- Durée de l'exécution : 251.7 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s10

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 10.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s10_164607.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 300361 ; propagations 80790020 ; nodes non rapporté ; temps de résolution 48.3 s (non déterministe)
- Durée de l'exécution : 251.0 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s11

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 11.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s11_164606.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 282111 ; propagations 80606276 ; nodes non rapporté ; temps de résolution 48.7 s (non déterministe)
- Durée de l'exécution : 251.7 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s12

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 12.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s12_164606.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 313169 ; propagations 78999640 ; nodes non rapporté ; temps de résolution 46.0 s (non déterministe)
- Durée de l'exécution : 248.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s13

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 13.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s13_164605.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 331805 ; propagations 81150415 ; nodes non rapporté ; temps de résolution 48.6 s (non déterministe)
- Durée de l'exécution : 250.0 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s14

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 14.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s14_164606.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 266432 ; propagations 77842569 ; nodes non rapporté ; temps de résolution 46.8 s (non déterministe)
- Durée de l'exécution : 249.6 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s15

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 15.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s15_164606.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 330060 ; propagations 82524095 ; nodes non rapporté ; temps de résolution 48.2 s (non déterministe)
- Durée de l'exécution : 250.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s16

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 16.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s16_164606.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 292519 ; propagations 81134592 ; nodes non rapporté ; temps de résolution 50.2 s (non déterministe)
- Durée de l'exécution : 252.3 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s17

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 17.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s17_164606.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 308919 ; propagations 81143372 ; nodes non rapporté ; temps de résolution 48.4 s (non déterministe)
- Durée de l'exécution : 251.8 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s18

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 18.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s18_164606.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 319454 ; propagations 80261113 ; nodes non rapporté ; temps de résolution 46.6 s (non déterministe)
- Durée de l'exécution : 249.1 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:46 — bench2_vois2_s19

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 19.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s19_164605.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 349114 ; propagations 86720784 ; nodes non rapporté ; temps de résolution 51.4 s (non déterministe)
- Durée de l'exécution : 253.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois2_s20

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 2, graine 20.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois2_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois2_s20_165015.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 316614 ; propagations 87908347 ; nodes non rapporté ; temps de résolution 63.1 s (non déterministe)
- Durée de l'exécution : 296.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s00

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 0.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s00_165016.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26628444 ; propagations 3855683424 ; nodes non rapporté ; temps de résolution 2623.9 s (non déterministe)
- Durée de l'exécution : 2849.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s01

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 1.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s01_165016.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 28385806 ; propagations 4034044064 ; nodes non rapporté ; temps de résolution 2749.5 s (non déterministe)
- Durée de l'exécution : 2975.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s02

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 2.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s02_165016.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 27847802 ; propagations 4007818009 ; nodes non rapporté ; temps de résolution 2696.7 s (non déterministe)
- Durée de l'exécution : 2924.5 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s03

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 3.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s03_165017.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 27071074 ; propagations 3916600946 ; nodes non rapporté ; temps de résolution 2680.5 s (non déterministe)
- Durée de l'exécution : 2907.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s04

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 4.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s04_165017.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 28393376 ; propagations 4098206581 ; nodes non rapporté ; temps de résolution 2762.1 s (non déterministe)
- Durée de l'exécution : 2988.5 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s05

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 5.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s05_165017.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 28201536 ; propagations 4033315998 ; nodes non rapporté ; temps de résolution 2751.5 s (non déterministe)
- Durée de l'exécution : 2976.3 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s06

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 6.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s06_165017.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26784151 ; propagations 3876917065 ; nodes non rapporté ; temps de résolution 2641.8 s (non déterministe)
- Durée de l'exécution : 2868.0 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s07

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 7.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s07_165017.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 27423165 ; propagations 3960506849 ; nodes non rapporté ; temps de résolution 2698.2 s (non déterministe)
- Durée de l'exécution : 2924.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s08

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 8.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s08_165018.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 27832209 ; propagations 3885567379 ; nodes non rapporté ; temps de résolution 2596.9 s (non déterministe)
- Durée de l'exécution : 2824.2 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s09

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 9.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s09_165019.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26831157 ; propagations 3917051213 ; nodes non rapporté ; temps de résolution 2699.3 s (non déterministe)
- Durée de l'exécution : 2924.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s10

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 10.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s10_165019.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 28170737 ; propagations 3996738761 ; nodes non rapporté ; temps de résolution 2705.9 s (non déterministe)
- Durée de l'exécution : 2931.2 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s11

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 11.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s11_165019.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 28016439 ; propagations 4090470500 ; nodes non rapporté ; temps de résolution 2767.1 s (non déterministe)
- Durée de l'exécution : 2991.7 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s12

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 12.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s12_165019.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 28023522 ; propagations 3865711777 ; nodes non rapporté ; temps de résolution 2634.8 s (non déterministe)
- Durée de l'exécution : 2860.8 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s13

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 13.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s13_165019.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26839675 ; propagations 3820709288 ; nodes non rapporté ; temps de résolution 2600.4 s (non déterministe)
- Durée de l'exécution : 2826.5 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s14

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 14.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s14_165020.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26787545 ; propagations 3882419415 ; nodes non rapporté ; temps de résolution 2658.1 s (non déterministe)
- Durée de l'exécution : 2884.5 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s15

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 15.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s15_165020.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26266358 ; propagations 3730851180 ; nodes non rapporté ; temps de résolution 2554.4 s (non déterministe)
- Durée de l'exécution : 2781.5 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s16

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 16.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s16_165020.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 29336417 ; propagations 4204445347 ; nodes non rapporté ; temps de résolution 2883.2 s (non déterministe)
- Durée de l'exécution : 3111.2 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s17

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 17.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s17_165020.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26866571 ; propagations 3875413557 ; nodes non rapporté ; temps de résolution 2685.2 s (non déterministe)
- Durée de l'exécution : 2911.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:50 — bench2_vois3_s18

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 18.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s18_165024.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 27286914 ; propagations 3961060569 ; nodes non rapporté ; temps de résolution 2710.7 s (non déterministe)
- Durée de l'exécution : 2934.5 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 16:55 — bench2_vois3_s19

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 19.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s19_165513.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26857874 ; propagations 3922679482 ; nodes non rapporté ; temps de résolution 2681.2 s (non déterministe)
- Durée de l'exécution : 2906.3 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois3_s20

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 3, graine 20.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois3_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois3_s20_184658.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 26654200 ; propagations 3953738400 ; nodes non rapporté ; temps de résolution 2739.1 s (non déterministe)
- Durée de l'exécution : 2968.1 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s00

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 0.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s00_184659.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36534927 ; propagations 3686234706 ; nodes non rapporté ; temps de résolution 4693.1 s (non déterministe)
- Durée de l'exécution : 4923.2 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s01

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 1.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s01_184659.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 35117683 ; propagations 3624289928 ; nodes non rapporté ; temps de résolution 4568.8 s (non déterministe)
- Durée de l'exécution : 4798.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s02

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 2.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s02_184658.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36851694 ; propagations 3648527068 ; nodes non rapporté ; temps de résolution 4708.9 s (non déterministe)
- Durée de l'exécution : 4939.0 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s03

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 3.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s03_184659.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36591727 ; propagations 3663427655 ; nodes non rapporté ; temps de résolution 4647.2 s (non déterministe)
- Durée de l'exécution : 4878.8 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s04

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 4.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s04_184659.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36252910 ; propagations 3668998604 ; nodes non rapporté ; temps de résolution 4688.3 s (non déterministe)
- Durée de l'exécution : 4915.2 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s05

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 5.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s05_184659.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 37357946 ; propagations 3635215844 ; nodes non rapporté ; temps de résolution 4523.7 s (non déterministe)
- Durée de l'exécution : 4757.3 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s06

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 6.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s06_184659.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 37941857 ; propagations 3733565282 ; nodes non rapporté ; temps de résolution 4760.8 s (non déterministe)
- Durée de l'exécution : 4987.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s07

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 7.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s07_184659.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 37719003 ; propagations 3638184426 ; nodes non rapporté ; temps de résolution 4621.6 s (non déterministe)
- Durée de l'exécution : 4849.7 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s08

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 8.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s08_184659.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 37175838 ; propagations 3633379944 ; nodes non rapporté ; temps de résolution 4637.1 s (non déterministe)
- Durée de l'exécution : 4866.3 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s09

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 9.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s09_184659.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 35630861 ; propagations 3625727720 ; nodes non rapporté ; temps de résolution 4552.0 s (non déterministe)
- Durée de l'exécution : 4781.0 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s10

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 10.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s10_184659.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36552679 ; propagations 3658200647 ; nodes non rapporté ; temps de résolution 4679.6 s (non déterministe)
- Durée de l'exécution : 4908.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s11

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 11.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s11_184658.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36561118 ; propagations 3661840457 ; nodes non rapporté ; temps de résolution 4615.0 s (non déterministe)
- Durée de l'exécution : 4843.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s12

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 12.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s12_184659.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 38065614 ; propagations 3711709827 ; nodes non rapporté ; temps de résolution 4739.3 s (non déterministe)
- Durée de l'exécution : 4966.8 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s13

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 13.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s13_184659.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 37023059 ; propagations 3626752788 ; nodes non rapporté ; temps de résolution 4559.1 s (non déterministe)
- Durée de l'exécution : 4790.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s14

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 14.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s14_184659.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36319487 ; propagations 3623225551 ; nodes non rapporté ; temps de résolution 4607.9 s (non déterministe)
- Durée de l'exécution : 4835.8 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s15

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 15.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s15_184659.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 37066590 ; propagations 3686151440 ; nodes non rapporté ; temps de résolution 4721.3 s (non déterministe)
- Durée de l'exécution : 4949.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s16

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 16.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s16_184659.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 34480265 ; propagations 3614515794 ; nodes non rapporté ; temps de résolution 4678.0 s (non déterministe)
- Durée de l'exécution : 4907.1 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s17

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 17.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s17_184659.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36870051 ; propagations 3595851066 ; nodes non rapporté ; temps de résolution 4586.3 s (non déterministe)
- Durée de l'exécution : 4817.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 18:46 — bench2_vois4_s18

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 18.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s18_184659.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36589526 ; propagations 3650406291 ; nodes non rapporté ; temps de résolution 4659.8 s (non déterministe)
- Durée de l'exécution : 4889.0 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 19:36 — bench2_vois4_s19

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 19.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s19_193628.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 36909593 ; propagations 3659253013 ; nodes non rapporté ; temps de résolution 3851.7 s (non déterministe)
- Durée de l'exécution : 4036.9 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 20:06 — bench2_vois4_s20

Comparaison des tailles de voisinage sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 4, graine 20.

- Configuration : `experiments/config/bench2_voisinage/bench2_vois4_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_vois4_s20_200618.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 35873624 ; propagations 3632236450 ; nodes non rapporté ; temps de résolution 3390.9 s (non déterministe)
- Durée de l'exécution : 3548.4 s ; commit `94989faaf4ace2a42ab0059cb5d81d7840ff1b0e`

## 2026-11-24 — Synthese : taille du voisinage sur bench_2

Comparaison de quatre tailles de voisinage avec une population
de 18, 26 generations, 6 croisements et 6 mutations.
Chaque configuration est evaluee sur les graines 0 a 20.

Les 21 executions du voisinage 1 sont reutilisees.
Les 63 autres executions sont nouvelles.

| Voisinage | Optimums | Generation optimale moyenne | Propagations moyennes | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|
| 1 | 21/21 | 4.48 | 5982586 | 4.531 |
| 2 | 21/21 | 0.76 | 81465089 | 48.990 |
| 3 | 21/21 | 0 | 3947140467 | 2691.459 |
| 4 | 21/21 | 0.14 | 3651318786 | 4547.166 |

Toutes les configurations atteignent l'optimum de 38.

Les grands voisinages accelerent la convergence en nombre
de generations, mais augmentent fortement l'effort du solveur.

Le voisinage 3 atteint systematiquement l'optimum des
l'initialisation et obtient les meilleurs taux de faisabilite
apres recherche locale.

Le voisinage 1 est retenu provisoirement pour la suite,
car il atteint le meme optimum avec un effort cumule
nettement inferieur sur les executions completes.

Les temps cumules ne mesurent pas directement le temps
necessaire pour atteindre le premier optimum.

Analyse detaillee : `experiments/analysis/bench2_voisinage.md`.

Script reproductible : `experiments/analysis/analyze_neighborhood.py`.

## 2026-11-24 21:26 — bench2_stag15_s00

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 0.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s00_212657.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8133 ; propagations 5841764 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 200.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:26 — bench2_stag15_s01

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 1.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s01_212659.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8393 ; propagations 6337086 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 201.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s02

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 2.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s02_212700.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7255 ; propagations 4911207 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 199.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s03

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 3.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s03_212700.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7558 ; propagations 5485469 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 201.4 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s04

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 4.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s04_212700.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6642 ; propagations 4696396 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 200.7 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s05

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 5.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s05_212700.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7660 ; propagations 5121550 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 197.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s06

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 6.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s06_212705.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7768 ; propagations 5057950 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 199.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s07

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 7.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s07_212705.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7520 ; propagations 5448959 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 200.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s08

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 8.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s08_212705.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7722 ; propagations 5326670 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 199.3 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s09

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 9.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s09_212706.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7136 ; propagations 4427147 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 199.1 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s10

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 10.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s10_212706.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7993 ; propagations 5500665 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 200.7 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s11

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 11.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s11_212707.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6786 ; propagations 5003899 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 198.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s12

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 12.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s12_212707.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8364 ; propagations 5663332 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 201.7 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s13

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 13.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s13_212707.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8137 ; propagations 5808057 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 198.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s14

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 14.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s14_212707.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8423 ; propagations 6108780 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 200.3 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s15

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 15.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s15_212707.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7532 ; propagations 5363407 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 199.1 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s16

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 16.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s16_212708.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8283 ; propagations 5984758 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 199.2 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:27 — bench2_stag15_s17

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 17.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s17_212708.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5889 ; propagations 4362082 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 198.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:30 — bench2_stag15_s18

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 18.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s18_213019.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7939 ; propagations 5421064 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 155.0 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:30 — bench2_stag15_s19

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 19.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s19_213019.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7950 ; propagations 5485504 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 155.1 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:30 — bench2_stag15_s20

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 15, graine 20.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag15_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag15_s20_213021.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8417 ; propagations 6297485 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 154.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s00

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 0.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s00_211928.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11054 ; propagations 9237542 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 234.2 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s01

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 1.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s01_211929.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 5 restart(s)
- **Effort cumulé du solveur** : 571 appels ; failures 10936 ; propagations 8842743 ; nodes non rapporté ; temps de résolution 6.2 s (non déterministe)
- Durée de l'exécution : 227.3 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s02

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 2.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s02_211929.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 10876 ; propagations 8712768 ; nodes non rapporté ; temps de résolution 6.2 s (non déterministe)
- Durée de l'exécution : 233.3 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s03

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 3.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s03_211928.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 5 restart(s)
- **Effort cumulé du solveur** : 571 appels ; failures 10793 ; propagations 8267214 ; nodes non rapporté ; temps de résolution 5.9 s (non déterministe)
- Durée de l'exécution : 225.2 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s04

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 4.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s04_211929.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11859 ; propagations 8699176 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 232.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s05

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 5.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s05_211928.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11462 ; propagations 8496026 ; nodes non rapporté ; temps de résolution 6.3 s (non déterministe)
- Durée de l'exécution : 233.3 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s06

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 6.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s06_211928.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 5 restart(s)
- **Effort cumulé du solveur** : 571 appels ; failures 10343 ; propagations 8069284 ; nodes non rapporté ; temps de résolution 5.9 s (non déterministe)
- Durée de l'exécution : 228.1 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s07

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 7.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s07_211928.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11790 ; propagations 9328286 ; nodes non rapporté ; temps de résolution 6.8 s (non déterministe)
- Durée de l'exécution : 233.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s08

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 8.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s08_211929.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 12263 ; propagations 9003349 ; nodes non rapporté ; temps de résolution 6.6 s (non déterministe)
- Durée de l'exécution : 233.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s09

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 9.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s09_211929.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11616 ; propagations 8958828 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 231.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s10

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 10.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s10_211928.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 12459 ; propagations 9362645 ; nodes non rapporté ; temps de résolution 6.9 s (non déterministe)
- Durée de l'exécution : 233.5 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s11

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 11.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s11_211929.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 5 restart(s)
- **Effort cumulé du solveur** : 571 appels ; failures 11975 ; propagations 9298472 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 227.7 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s12

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 12.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s12_211928.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11069 ; propagations 8384676 ; nodes non rapporté ; temps de résolution 6.2 s (non déterministe)
- Durée de l'exécution : 232.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s13

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 13.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s13_211929.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11944 ; propagations 9059915 ; nodes non rapporté ; temps de résolution 6.3 s (non déterministe)
- Durée de l'exécution : 233.0 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s14

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 14.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s14_211928.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 12644 ; propagations 9248776 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 234.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s15

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 15.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s15_211929.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11469 ; propagations 8974067 ; nodes non rapporté ; temps de résolution 6.6 s (non déterministe)
- Durée de l'exécution : 233.4 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s16

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 16.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s16_211928.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 5 restart(s)
- **Effort cumulé du solveur** : 571 appels ; failures 11789 ; propagations 8801603 ; nodes non rapporté ; temps de résolution 6.3 s (non déterministe)
- Durée de l'exécution : 228.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s17

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 17.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s17_211928.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 11350 ; propagations 8749954 ; nodes non rapporté ; temps de résolution 6.4 s (non déterministe)
- Durée de l'exécution : 234.2 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s18

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 18.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s18_211929.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 12793 ; propagations 9511121 ; nodes non rapporté ; temps de résolution 6.8 s (non déterministe)
- Durée de l'exécution : 234.5 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:19 — bench2_stag3_s19

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 19.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s19_211929.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 6 restart(s)
- **Effort cumulé du solveur** : 588 appels ; failures 12266 ; propagations 9628034 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 232.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag3_s20

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 3, graine 20.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag3_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag3_s20_212315.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 5 restart(s)
- **Effort cumulé du solveur** : 571 appels ; failures 11832 ; propagations 9439417 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 228.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s00

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 0.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s00_212317.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 9830 ; propagations 7504942 ; nodes non rapporté ; temps de résolution 5.7 s (non déterministe)
- Durée de l'exécution : 221.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s01

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 1.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s01_212317.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 9606 ; propagations 7488890 ; nodes non rapporté ; temps de résolution 5.5 s (non déterministe)
- Durée de l'exécution : 215.2 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s02

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 2.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s02_212318.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 9359 ; propagations 7303749 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 220.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s03

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 3.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s03_212318.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 10038 ; propagations 7599306 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 213.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s04

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 4.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s04_212322.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 9922 ; propagations 7038058 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 214.4 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s05

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 5.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s05_212322.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 10841 ; propagations 7549489 ; nodes non rapporté ; temps de résolution 5.7 s (non déterministe)
- Durée de l'exécution : 221.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s06

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 6.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s06_212322.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 9319 ; propagations 6921357 ; nodes non rapporté ; temps de résolution 5.2 s (non déterministe)
- Durée de l'exécution : 215.8 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s07

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 7.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s07_212323.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 10115 ; propagations 8137927 ; nodes non rapporté ; temps de résolution 6.0 s (non déterministe)
- Durée de l'exécution : 222.0 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s08

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 8.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s08_212324.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 10522 ; propagations 7630798 ; nodes non rapporté ; temps de résolution 5.7 s (non déterministe)
- Durée de l'exécution : 221.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s09

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 9.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s09_212324.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 9340 ; propagations 7176353 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 220.4 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s10

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 10.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s10_212324.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 9624 ; propagations 7833069 ; nodes non rapporté ; temps de résolution 5.8 s (non déterministe)
- Durée de l'exécution : 223.2 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s11

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 11.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s11_212324.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 10577 ; propagations 7518063 ; nodes non rapporté ; temps de résolution 5.8 s (non déterministe)
- Durée de l'exécution : 221.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s12

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 12.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s12_212324.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 10188 ; propagations 7457942 ; nodes non rapporté ; temps de résolution 5.8 s (non déterministe)
- Durée de l'exécution : 220.6 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s13

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 13.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s13_212324.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 10464 ; propagations 7379360 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 221.4 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s14

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 14.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s14_212324.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 10261 ; propagations 7533679 ; nodes non rapporté ; temps de résolution 5.7 s (non déterministe)
- Durée de l'exécution : 221.0 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s15

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 15.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s15_212324.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 8853 ; propagations 6334036 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 215.0 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s16

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 16.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s16_212325.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 10028 ; propagations 7187221 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 214.5 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s17

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 17.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s17_212325.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 9002 ; propagations 7053604 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 220.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:23 — bench2_stag5_s18

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 18.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s18_212325.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 11080 ; propagations 8056232 ; nodes non rapporté ; temps de résolution 5.9 s (non déterministe)
- Durée de l'exécution : 221.9 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:26 — bench2_stag5_s19

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 19.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s19_212653.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 11186 ; propagations 8238916 ; nodes non rapporté ; temps de résolution 5.8 s (non déterministe)
- Durée de l'exécution : 220.2 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 21:26 — bench2_stag5_s20

Comparaison des seuils de stagnation sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 5, graine 20.

- Configuration : `experiments/config/bench2_stagnation/bench2_stag5_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_stag5_s20_212654.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 9680 ; propagations 7346464 ; nodes non rapporté ; temps de résolution 5.5 s (non déterministe)
- Durée de l'exécution : 214.4 s ; commit `a2ff03f18937a644776a20e33ceccdeebee02b1e`

## 2026-11-24 — Synthese : seuil de stagnation sur bench_2

Comparaison des seuils de stagnation 3, 5, 10 et 15
avec une population de 18, 26 generations, 6 croisements,
6 mutations et un voisinage de taille 1.

Chaque configuration est evaluee sur les graines 0 a 20.
Les 21 executions du seuil 10 sont reutilisees.
Les 63 autres executions sont nouvelles.

| Seuil | Optimums | Generation optimale moyenne | Redemarrages moyens | Propagations moyennes | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|---:|
| 3 | 21/21 | 5.10 | 5.71 | 8955900 | 6.4581 |
| 5 | 21/21 | 4.52 | 3.67 | 7442355 | 5.5892 |
| 10 | 21/21 | 4.48 | 1.67 | 5982586 | 4.531 |
| 15 | 21/21 | 4.71 | 1 | 5412059 | 4.1674 |

Toutes les configurations atteignent l'optimum de 38.

Les redemarrages frequents augmentent la diversite
genotypique finale, mais egalement l'effort du solveur,
sans ameliorer le taux de succes.

Le seuil 10 presente la meilleure convergence moyenne.
Le seuil 15 presente le plus faible effort cumule.

Le seuil 10 est retenu provisoirement comme compromis
entre convergence, diversite et effort de resolution.

Les differences de convergence entre les seuils 5,
10 et 15 restent faibles et leur significativite
statistique n'est pas etablie.

Analyse detaillee : `experiments/analysis/bench2_stagnation.md`.

Script reproductible : `experiments/analysis/analyze_stagnation.py`.

<!-- Entrees reconstruites a partir des JSON originaux avec la fonction officielle explog_entry. -->

## 2026-11-24 22:09 — bench2_dt10_s00

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 0.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s00_220955.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8784 ; propagations 6596583 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 207.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s01

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 1.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s01_221000.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8940 ; propagations 6710191 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 200.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s02

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 2.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s02_221001.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8950 ; propagations 5922095 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 206.7 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s03

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 3.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s03_221002.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7401 ; propagations 5225477 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 200.9 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s04

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 4.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s04_221002.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7575 ; propagations 5051174 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 200.8 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s05

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 5.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s05_221002.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8436 ; propagations 6244840 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 209.0 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s06

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 6.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s06_221004.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7277 ; propagations 5001464 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 200.4 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s07

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 7.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s07_221004.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8945 ; propagations 6509362 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 208.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s08

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 8.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s08_221004.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8788 ; propagations 6354606 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 208.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s09

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 9.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s09_221008.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8118 ; propagations 5414001 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 205.8 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s10

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 10.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s10_221010.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9532 ; propagations 6757795 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 208.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s11

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 11.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s11_221010.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5939 ; propagations 4069242 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 199.7 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s12

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 12.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s12_221010.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8775 ; propagations 6157587 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 207.5 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s13

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 13.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s13_221010.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9203 ; propagations 6510006 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s14

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 14.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s14_221011.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9221 ; propagations 6769722 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 207.5 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s15

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 15.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s15_221011.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7205 ; propagations 4973883 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 200.4 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s16

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 16.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s16_221012.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8337 ; propagations 5892877 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 200.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:10 — bench2_dt10_s17

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 17.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s17_221012.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8001 ; propagations 5856102 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 206.4 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:13 — bench2_dt10_s18

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 18.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s18_221322.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8893 ; propagations 6357625 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 162.0 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:13 — bench2_dt10_s19

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 19.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s19_221324.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9625 ; propagations 6731378 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 161.4 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:13 — bench2_dt10_s20

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 10.0, graine 20.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt10_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt10_s20_221324.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8304 ; propagations 6528298 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 161.3 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s00

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 0.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s00_220314.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8784 ; propagations 6596583 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 207.0 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s01

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 1.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s01_220313.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8940 ; propagations 6710191 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 199.7 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s02

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 2.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s02_220313.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8950 ; propagations 5922095 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 207.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s03

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 3.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s03_220314.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7401 ; propagations 5225477 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 198.5 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s04

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 4.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s04_220314.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7575 ; propagations 5051174 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 199.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s05

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 5.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s05_220314.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8436 ; propagations 6244840 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 205.7 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s06

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 6.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s06_220314.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7277 ; propagations 5001464 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 198.9 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s07

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 7.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s07_220313.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8945 ; propagations 6509362 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.7 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s08

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 8.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s08_220314.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8788 ; propagations 6354606 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.0 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s09

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 9.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s09_220314.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8118 ; propagations 5414001 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 205.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s10

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 10.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s10_220314.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9532 ; propagations 6757795 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 207.5 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s11

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 11.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s11_220313.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5939 ; propagations 4069242 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 198.5 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s12

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 12.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s12_220314.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8775 ; propagations 6157587 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 206.4 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s13

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 13.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s13_220313.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9203 ; propagations 6510006 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 206.8 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s14

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 14.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s14_220313.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9221 ; propagations 6769722 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 207.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s15

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 15.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s15_220314.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7205 ; propagations 4973883 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 199.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s16

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 16.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s16_220314.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8337 ; propagations 5892877 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 200.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s17

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 17.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s17_220314.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8001 ; propagations 5856102 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 207.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s18

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 18.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s18_220314.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8893 ; propagations 6357625 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 205.9 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:03 — bench2_dt1_s19

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 19.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s19_220314.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9625 ; propagations 6731378 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 207.3 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt1_s20

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 1.0, graine 20.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt1_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt1_s20_220633.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8304 ; propagations 6528298 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 207.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s00

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 0.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s00.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s00_220634.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8784 ; propagations 6596583 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 207.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s01

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 1.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s01.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s01_220634.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8940 ; propagations 6710191 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 200.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s02

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 2.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s02.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s02_220634.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8950 ; propagations 5922095 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 205.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s03

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 3.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s03.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s03_220634.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7401 ; propagations 5225477 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 198.3 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s04

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 4.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s04.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s04_220635.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7575 ; propagations 5051174 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 199.5 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s05

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 5.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s05.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s05_220635.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8436 ; propagations 6244840 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 207.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s06

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 6.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s06.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s06_220640.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7277 ; propagations 5001464 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 199.8 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s07

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 7.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s07.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s07_220640.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8945 ; propagations 6509362 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 208.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s08

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 8.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s08.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s08_220641.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8788 ; propagations 6354606 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.8 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s09

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 9.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s09.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s09_220641.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8118 ; propagations 5414001 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 206.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s10

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 10.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s10.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s10_220641.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9532 ; propagations 6757795 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 207.9 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s11

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 11.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s11.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s11_220641.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5939 ; propagations 4069242 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 199.9 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s12

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 12.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s12.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s12_220642.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8775 ; propagations 6157587 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 207.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s13

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 13.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s13.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s13_220643.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9203 ; propagations 6510006 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.6 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s14

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 14.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s14.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s14_220642.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9221 ; propagations 6769722 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 208.2 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s15

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 15.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s15.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s15_220643.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7205 ; propagations 4973883 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 200.0 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s16

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 16.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s16.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s16_220643.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8337 ; propagations 5892877 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 199.8 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s17

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 17.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s17.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s17_220643.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8001 ; propagations 5856102 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 207.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:06 — bench2_dt2p5_s18

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 18.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s18.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s18_220643.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8893 ; propagations 6357625 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 208.1 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:09 — bench2_dt2p5_s19

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 19.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s19.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s19_220954.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9625 ; propagations 6731378 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 208.5 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 22:09 — bench2_dt2p5_s20

Comparaison du temps deterministe sur bench_2 : population 18, 26 generations, NR=6, NM=6, voisinage 1, stagnation 10, temps deterministe 2.5, graine 20.

- Configuration : `experiments/config/bench2_deterministic_time/bench2_dt2p5_s20.json`
- Résultats : `experiments/results/2026-11-24/bench2_dt2p5_s20_220955.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8304 ; propagations 6528298 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 208.3 s ; commit `405eb47b22bbad8f6d59d0e7214c5f1788438338`

## 2026-11-24 — Synthese : temps deterministe sur bench_2

Comparaison des budgets deterministes 1, 2.5, 5 et 10
avec une population de 18, 26 generations, 6 croisements,
6 mutations, un voisinage de taille 1 et un seuil
de stagnation de 10.

Chaque configuration est evaluee sur les graines 0 a 20.
Les 21 executions du budget 5 sont reutilisees.
Les 63 autres executions sont nouvelles.

| Budget | Optimums | Generation optimale moyenne | Appels moyens | Propagations moyennes | Temps solveur moyen (s) |
|---:|---:|---:|---:|---:|---:|
| 1 | 21/21 | 4.48 | 514.33 | 5982586 | 4.6266 |
| 2.5 | 21/21 | 4.48 | 514.33 | 5982586 | 4.6417 |
| 5 | 21/21 | 4.48 | 514.33 | 5982586 | 4.5310 |
| 10 | 21/21 | 4.48 | 514.33 | 5982586 | 4.4983 |

Toutes les configurations atteignent l'optimum de 38.

La comparaison individuelle des 21 graines ne revele
aucune difference sur les indicateurs compares,
a l'exception des temps mesures en secondes, exclus
de cette comparaison.

Le budget deterministe ne semble pas contraignant
dans les conditions experimentales testees.
Les motifs d'arret individuels du solveur n'ont
toutefois pas ete verifies.

Le budget de 5 est conserve provisoirement.

Les 63 entrees individuelles du journal ont ete
reconstruites a partir des fichiers JSON originaux
avec la fonction officielle explog_entry, puisque
les journaux temporaires n'etaient plus disponibles.

Analyse detaillee : `experiments/analysis/bench2_deterministic_time.md`.

Script reproductible : `experiments/analysis/analyze_deterministic_time.py`.

## 2026-11-25 17:31 — bench2_nr3_nm12_s00

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s00.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s00_173109.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7803 ; propagations 5112379 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 205.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s01

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s01.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s01_173109.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6829 ; propagations 4553453 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 199.0 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s02

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s02.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s02_173108.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7323 ; propagations 4925590 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 205.7 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s03

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s03.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s03_173109.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6189 ; propagations 3724284 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 196.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s04

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s04.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s04_173109.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6860 ; propagations 4544181 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.5 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s05

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s05.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s05_173108.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5647 ; propagations 3618497 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 198.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s06

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s06.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s06_173108.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7277 ; propagations 5034749 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 204.5 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s07

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s07.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s07_173109.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6730 ; propagations 4557849 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 210.0 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s08

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s08.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s08_173109.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5830 ; propagations 3852412 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 197.9 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s09

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s09.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s09_173108.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7028 ; propagations 4763969 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.8 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s10

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s10.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s10_173108.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7991 ; propagations 5492029 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 206.5 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s11

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s11.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s11_173108.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6353 ; propagations 4183291 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 205.1 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s12

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s12.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s12_173108.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 5971 ; propagations 4073492 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 204.7 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s13

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s13.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s13_173108.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6750 ; propagations 4657267 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 204.2 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s14

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s14.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s14_173109.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6446 ; propagations 4406032 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 208.1 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s15

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s15.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s15_173108.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6191 ; propagations 3642661 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 204.7 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s16

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s16.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s16_173108.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7829 ; propagations 4795852 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.4 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s17

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s17.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s17_173108.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6703 ; propagations 4824181 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s18

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s18.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s18_173109.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6878 ; propagations 4847615 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 204.8 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:31 — bench2_nr3_nm12_s19

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s19.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s19_173109.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6833 ; propagations 4805958 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 206.0 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr3_nm12_s20

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench2_ratio/bench2_nr3_nm12_s20.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr3_nm12_s20_173426.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6221 ; propagations 4172063 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 206.0 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s00

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s00.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s00_173428.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9826 ; propagations 7481201 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 213.5 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s01

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s01.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s01_173428.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9847 ; propagations 7334199 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 213.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s02

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s02.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s02_173429.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 10060 ; propagations 6864703 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 207.8 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s03

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s03.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s03_173433.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 7482 ; propagations 4908161 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.7 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s04

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s04.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s04_173434.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9808 ; propagations 6969070 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 214.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s05

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s05.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s05_173434.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8617 ; propagations 5944199 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 206.7 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s06

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s06.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s06_173434.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 11103 ; propagations 7381081 ; nodes non rapporté ; temps de résolution 5.7 s (non déterministe)
- Durée de l'exécution : 215.7 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s07

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s07.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s07_173435.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8613 ; propagations 6630605 ; nodes non rapporté ; temps de résolution 5.3 s (non déterministe)
- Durée de l'exécution : 207.4 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s08

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s08.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s08_173435.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 10189 ; propagations 6787308 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 214.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s09

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s09.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s09_173435.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 10401 ; propagations 7697341 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 215.5 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s10

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s10.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s10_173435.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9321 ; propagations 7057019 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 213.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s11

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s11.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s11_173435.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 9029 ; propagations 6402980 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 206.7 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s12

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s12.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s12_173436.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8444 ; propagations 6665474 ; nodes non rapporté ; temps de résolution 5.2 s (non déterministe)
- Durée de l'exécution : 213.9 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s13

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s13.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s13_173436.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9933 ; propagations 7195911 ; nodes non rapporté ; temps de résolution 5.3 s (non déterministe)
- Durée de l'exécution : 214.6 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s14

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s14.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s14_173436.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 10351 ; propagations 7064516 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 208.0 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s15

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s15.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s15_173436.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5881 ; propagations 4066673 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 206.3 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s16

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s16.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s16_173436.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9331 ; propagations 6812091 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 214.4 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s17

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s17.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s17_173438.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9885 ; propagations 6975688 ; nodes non rapporté ; temps de résolution 5.3 s (non déterministe)
- Durée de l'exécution : 213.2 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:34 — bench2_nr8_nm2_s18

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s18.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s18_173440.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9967 ; propagations 7510691 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 213.1 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:37 — bench2_nr8_nm2_s19

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s19.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s19_173754.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 10211 ; propagations 6906295 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 155.1 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 17:37 — bench2_nr8_nm2_s20

Comparaison du ratio croisement-mutation sur bench_2 : population 18, 26 generations, NR=8, NM=2, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench2_ratio/bench2_nr8_nm2_s20.json`
- Résultats : `experiments/results/2026-11-25/bench2_nr8_nm2_s20_173758.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 8, NM = 2, 26 générations
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 11156 ; propagations 8385743 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 159.4 s ; commit `38872e8ac23f13594d8ddff86337d26072c27e93`

## 2026-11-25 — Synthèse : ratio croisement-mutation sur bench_2

Comparaison de trois couples (NR, NM) : (3, 12), (6, 6) et (8, 2),
avec un budget nominal constant de 486 individus et 21 graines
par configuration.

Les trois configurations atteignent systématiquement l'optimum 38.
Le couple (3, 12) réduit de 24,7 % le nombre moyen de propagations
par rapport à la référence (6, 6), avec une convergence moyenne
légèrement meilleure.

Le couple (3, 12) est retenu provisoirement pour la suite des
expériences. Les conclusions restent propres à l'instance étudiée.

- Analyse : `experiments/analysis/bench2_ratio.md`
- Script : `experiments/analysis/analyze_ratio.py`
- Configurations : `experiments/config/bench2_ratio/`
- Nouvelles exécutions : 42.

## 2026-11-25 20:35 — bench2_validation_s00

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 0.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s00.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s00_203516.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7803 ; propagations 5112379 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 205.7 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s01

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 1.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s01.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s01_203516.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6829 ; propagations 4553453 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 199.0 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s02

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 2.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s02.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s02_203515.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7323 ; propagations 4925590 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.2 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s03

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 3.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s03.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s03_203515.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6189 ; propagations 3724284 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 198.2 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s04

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 4.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s04.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s04_203515.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6860 ; propagations 4544181 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 204.9 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s05

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 5.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s05.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s05_203515.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5647 ; propagations 3618497 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 198.1 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s06

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 6.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s06.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s06_203515.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7277 ; propagations 5034749 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 206.7 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s07

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 7.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s07.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s07_203515.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6730 ; propagations 4557849 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.4 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s08

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 8.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s08.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s08_203516.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5830 ; propagations 3852412 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 198.5 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s09

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 9.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s09.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s09_203516.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7028 ; propagations 4763969 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 206.3 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s10

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 10.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s10.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s10_203515.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7991 ; propagations 5492029 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 206.3 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s11

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 11.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s11.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s11_203515.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6353 ; propagations 4183291 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 205.5 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s12

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 12.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s12.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s12_203515.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 5971 ; propagations 4073492 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 204.1 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s13

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 13.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s13.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s13_203515.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6750 ; propagations 4657267 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 206.3 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s14

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 14.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s14.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s14_203515.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6446 ; propagations 4406032 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 206.1 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s15

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 15.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s15.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s15_203516.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6191 ; propagations 3642661 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 205.5 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s16

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 16.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s16.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s16_203515.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7829 ; propagations 4795852 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 206.0 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s17

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 17.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s17.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s17_203515.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6703 ; propagations 4824181 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 206.4 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s18

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 18.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s18.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s18_203515.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6878 ; propagations 4847615 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.6 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:35 — bench2_validation_s19

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 19.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s19.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s19_203515.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6833 ; propagations 4805958 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.7 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 20:38 — bench2_validation_s20

Validation de l'architecture configurable sur bench_2 : population 18, 26 generations, NR=3, NM=12, croisement uniform_gene, mutation shift_start, graine 20.

- Configuration : `experiments/config/bench2_validation/bench2_validation_s20.json`
- Résultats : `experiments/results/2026-11-25/bench2_validation_s20_203834.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6221 ; propagations 4172063 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 155.0 s ; commit `c83303203eee69756b04f491783f360f5f882c76`

## 2026-11-25 — Synthèse : validation des stratégies configurables

Validation de l'architecture introduite à l'étape 10c,
avec les stratégies uniform_gene et shift_start.

Les 21 nouvelles exécutions reproduisent exactement les
résultats algorithmiques comparés de la configuration
NR=3 et NM=12 sur bench_2.

Aucune différence observée dans les solutions, la convergence,
la diversité, la faisabilité et les compteurs du solveur.
Les mesures de temps sont exclues de la comparaison.

Cette validation permet de disposer d'une référence pour
la comparaison des opérateurs de mutation.

- Rapport : `experiments/analysis/bench2_validation.md`
- Script : `experiments/analysis/analyze_validation.py`
- Configurations : `experiments/config/bench2_validation/`
- Nouvelles exécutions : 21.

## 2026-11-25 20:44 — bench2_mut_block_boundary_s00

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 0.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s00.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s00_204456.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7752 ; propagations 4859721 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 203.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s01

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 1.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s01.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s01_204457.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6439 ; propagations 4319758 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 206.2 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s02

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 2.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s02.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s02_204456.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5747 ; propagations 3614163 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 199.6 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s03

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 3.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s03.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s03_204456.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6948 ; propagations 4346201 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 206.1 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s04

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 4.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s04.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s04_204456.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5373 ; propagations 3542184 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 199.6 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s05

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 5.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s05.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s05_204456.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6335 ; propagations 4089048 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 199.2 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s06

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 6.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s06.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s06_204456.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8040 ; propagations 5088662 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 206.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s07

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 7.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s07.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s07_204456.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7086 ; propagations 4873842 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 207.2 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s08

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 8.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s08.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s08_204456.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8275 ; propagations 4954380 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 206.5 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s09

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 9.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s09.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s09_204457.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6287 ; propagations 4092846 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 204.6 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s10

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 10.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s10.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s10_204457.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8133 ; propagations 5387963 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 206.1 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s11

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 11.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s11.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s11_204456.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7657 ; propagations 4929705 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 205.8 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s12

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 12.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s12.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s12_204456.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8087 ; propagations 5124221 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 206.5 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s13

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 13.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s13.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s13_204456.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7096 ; propagations 4987058 ; nodes non rapporté ; temps de résolution 4.2 s (non déterministe)
- Durée de l'exécution : 206.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s14

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 14.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s14.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s14_204456.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 6728 ; propagations 4392641 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 205.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s15

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 15.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s15.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s15_204457.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6109 ; propagations 3680036 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 198.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s16

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 16.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s16.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s16_204456.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8318 ; propagations 5134224 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 209.3 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s17

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 17.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s17.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s17_204456.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 5329 ; propagations 3208146 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 198.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s18

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 18.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s18.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s18_204456.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7180 ; propagations 4547709 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 207.0 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:44 — bench2_mut_block_boundary_s19

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 19.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s19.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s19_204456.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 7803 ; propagations 4992542 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 207.5 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s00

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 0.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s00.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s00_204817.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9180 ; propagations 6313892 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 207.5 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s01

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 1.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s01.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s01_204817.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8944 ; propagations 5778809 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 201.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s02

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 2.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s02.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s02_204817.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9756 ; propagations 6518096 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.0 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s03

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 3.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s03.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s03_204817.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9390 ; propagations 6545481 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 208.4 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s04

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 4.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s04.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s04_204821.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 9037 ; propagations 5792064 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 201.1 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s05

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 5.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s05.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s05_204822.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 9072 ; propagations 5903416 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 200.0 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s06

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 6.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s06.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s06_204823.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8011 ; propagations 5728516 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 202.0 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s07

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 7.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s07.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s07_204823.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9639 ; propagations 6763826 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 208.3 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s08

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 8.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s08.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s08_204823.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9186 ; propagations 6276316 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 208.4 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s09

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 9.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s09.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s09_204824.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9418 ; propagations 6471437 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 208.3 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s10

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 10.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s10.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s10_204824.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 10740 ; propagations 7099225 ; nodes non rapporté ; temps de résolution 5.3 s (non déterministe)
- Durée de l'exécution : 208.4 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s11

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 11.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s11.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s11_204824.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 8367 ; propagations 5569443 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 200.6 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s12

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 12.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s12.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s12_204824.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9656 ; propagations 6511133 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.4 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s13

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 13.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s13.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s13_204825.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 8906 ; propagations 5888689 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 206.8 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s14

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 14.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s14.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s14_204825.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9749 ; propagations 6457838 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 207.6 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s15

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 15.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s15.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s15_204825.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 9244 ; propagations 5479272 ; nodes non rapporté ; temps de résolution 4.5 s (non déterministe)
- Durée de l'exécution : 200.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s16

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 16.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s16.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s16_204825.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 9738 ; propagations 5598967 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 201.8 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s17

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 17.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s17.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s17_204825.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 9896 ; propagations 6262093 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 207.2 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_activity_s18

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 18.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s18.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s18_204827.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 9514 ; propagations 6177342 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 200.6 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:48 — bench2_mut_block_boundary_s20

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation block_boundary, graine 20.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_block_boundary_s20.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_block_boundary_s20_204816.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 6053 ; propagations 4373612 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 199.9 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:51 — bench2_mut_activity_s19

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 19.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s19.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s19_205137.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 9254 ; propagations 6469748 ; nodes non rapporté ; temps de résolution 4.1 s (non déterministe)
- Durée de l'exécution : 152.7 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 20:51 — bench2_mut_activity_s20

Comparaison des operateurs de mutation sur bench_2 : population 18, 26 generations, NR=3, NM=12, mutation activity, graine 20.

- Configuration : `experiments/config/bench2_mutation/bench2_mut_activity_s20.json`
- Résultats : `experiments/results/2026-11-25/bench2_mut_activity_s20_205140.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 10178 ; propagations 6046891 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 151.6 s ; commit `4478121565a0c4317fe59d1034c8ff7a0d2532c8`

## 2026-11-25 — Synthèse : comparaison des opérateurs de mutation sur bench_2

Comparaison de shift_start, block_boundary et activity,
avec une population de 18, 26 générations, NR=3 et NM=12.

Les trois opérateurs atteignent l'optimum 38 pour les
21 graines étudiées.

Shift_start et block_boundary présentent une convergence
moyenne identique et un effort de propagation comparable.

Activity nécessite environ 37.1 % plus de propagations
que shift_start et converge moins rapidement en moyenne.

Shift_start présente les meilleurs taux de faisabilité
des mutations avant et après recherche locale.

Shift_start est retenu provisoirement pour la suite.
Block_boundary demeure une alternative compétitive.
Aucune supériorité générale ne peut être établie sur
la base de cette seule instance.

- Rapport : `experiments/analysis/bench2_mutation.md`
- Script : `experiments/analysis/analyze_mutation.py`
- Configurations : `experiments/config/bench2_mutation/`
- Nouvelles exécutions : 42.
- Exécutions de référence réutilisées : 21.
