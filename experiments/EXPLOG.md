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
