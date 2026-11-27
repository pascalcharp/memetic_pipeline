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

## 2026-11-26 16:22 — xavier_bench_p1_1

Série de tests de Xavier avec la population d isolée: Population: 1;

- Configuration : `experiments/config/xavier_bench_p1_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p1_1_162209.json`
- Instance : bench_1 ; graine 97 ; population 1, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 301 appels ; failures 827 ; propagations 1145802 ; nodes non rapporté ; temps de résolution 1.9 s (non déterministe)
- Durée de l'exécution : 77.4 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:23 — xavier_bench_p2_1

Série de tests de Xavier avec la population d isolée: Population: 2;

- Configuration : `experiments/config/xavier_bench_p2_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p2_1_162327.json`
- Instance : bench_1 ; graine 97 ; population 2, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 306 appels ; failures 1174 ; propagations 1704200 ; nodes non rapporté ; temps de résolution 2.3 s (non déterministe)
- Durée de l'exécution : 78.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:24 — xavier_bench_p3_1

Série de tests de Xavier avec la population d isolée: Population: 3;

- Configuration : `experiments/config/xavier_bench_p3_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p3_1_162446.json`
- Instance : bench_1 ; graine 97 ; population 3, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 313 appels ; failures 1786 ; propagations 1635010 ; nodes non rapporté ; temps de résolution 2.4 s (non déterministe)
- Durée de l'exécution : 79.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:26 — xavier_bench_p4_1

Série de tests de Xavier avec la population d isolée: Population: 4;

- Configuration : `experiments/config/xavier_bench_p4_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p4_1_162607.json`
- Instance : bench_1 ; graine 97 ; population 4, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 319 appels ; failures 1413 ; propagations 1806230 ; nodes non rapporté ; temps de résolution 2.4 s (non déterministe)
- Durée de l'exécution : 79.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:27 — xavier_bench_p5_1

Série de tests de Xavier avec la population d isolée: Population: 5;

- Configuration : `experiments/config/xavier_bench_p5_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p5_1_162726.json`
- Instance : bench_1 ; graine 97 ; population 5, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 325 appels ; failures 1291 ; propagations 1789961 ; nodes non rapporté ; temps de résolution 2.4 s (non déterministe)
- Durée de l'exécution : 78.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:28 — xavier_bench_p6_1

Série de tests de Xavier avec la population d isolée: Population: 6;

- Configuration : `experiments/config/xavier_bench_p6_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p6_1_162846.json`
- Instance : bench_1 ; graine 97 ; population 6, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 326 appels ; failures 1382 ; propagations 1791572 ; nodes non rapporté ; temps de résolution 2.4 s (non déterministe)
- Durée de l'exécution : 80.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:30 — xavier_bench_p7_1

Série de tests de Xavier avec la population d isolée: Population: 7;

- Configuration : `experiments/config/xavier_bench_p7_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p7_1_163007.json`
- Instance : bench_1 ; graine 97 ; population 7, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 337 appels ; failures 1731 ; propagations 2175018 ; nodes non rapporté ; temps de résolution 2.8 s (non déterministe)
- Durée de l'exécution : 84.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:31 — xavier_bench_p8_1

Série de tests de Xavier avec la population d isolée: Population: 8;

- Configuration : `experiments/config/xavier_bench_p8_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p8_1_163132.json`
- Instance : bench_1 ; graine 97 ; population 8, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 336 appels ; failures 1712 ; propagations 2197657 ; nodes non rapporté ; temps de résolution 2.8 s (non déterministe)
- Durée de l'exécution : 84.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:32 — xavier_bench_p9_1

Série de tests de Xavier avec la population d isolée: Population: 9;

- Configuration : `experiments/config/xavier_bench_p9_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p9_1_163257.json`
- Instance : bench_1 ; graine 97 ; population 9, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 349 appels ; failures 2026 ; propagations 2495484 ; nodes non rapporté ; temps de résolution 3.0 s (non déterministe)
- Durée de l'exécution : 86.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:34 — xavier_bench_p10_1

Série de tests de Xavier avec la population d isolée: Population: 10;

- Configuration : `experiments/config/xavier_bench_p10_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p10_1_163423.json`
- Instance : bench_1 ; graine 97 ; population 10, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 355 appels ; failures 1968 ; propagations 2638879 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 88.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:35 — xavier_bench_p11_1

Série de tests de Xavier avec la population d isolée: Population: 11;

- Configuration : `experiments/config/xavier_bench_p11_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p11_1_163553.json`
- Instance : bench_1 ; graine 97 ; population 11, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 361 appels ; failures 1704 ; propagations 2504295 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 92.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:37 — xavier_bench_p12_1

Série de tests de Xavier avec la population d isolée: Population: 12;

- Configuration : `experiments/config/xavier_bench_p12_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p12_1_163726.json`
- Instance : bench_1 ; graine 97 ; population 12, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 367 appels ; failures 1979 ; propagations 2683520 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 94.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:39 — xavier_bench_p13_1

Série de tests de Xavier avec la population d isolée: Population: 13;

- Configuration : `experiments/config/xavier_bench_p13_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p13_1_163901.json`
- Instance : bench_1 ; graine 97 ; population 13, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 373 appels ; failures 2012 ; propagations 2698198 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 95.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:40 — xavier_bench_p14_1

Série de tests de Xavier avec la population d isolée: Population: 14;

- Configuration : `experiments/config/xavier_bench_p14_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p14_1_164037.json`
- Instance : bench_1 ; graine 97 ; population 14, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 366 appels ; failures 2147 ; propagations 2644107 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 95.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:42 — xavier_bench_p15_1

Série de tests de Xavier avec la population d isolée: Population: 15;

- Configuration : `experiments/config/xavier_bench_p15_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p15_1_164213.json`
- Instance : bench_1 ; graine 97 ; population 15, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 385 appels ; failures 2151 ; propagations 2750454 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 101.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:43 — xavier_bench_p16_1

Série de tests de Xavier avec la population d isolée: Population: 16;

- Configuration : `experiments/config/xavier_bench_p16_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p16_1_164355.json`
- Instance : bench_1 ; graine 97 ; population 16, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 391 appels ; failures 1992 ; propagations 2900043 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 100.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:45 — xavier_bench_p17_1

Série de tests de Xavier avec la population d isolée: Population: 17;

- Configuration : `experiments/config/xavier_bench_p17_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p17_1_164537.json`
- Instance : bench_1 ; graine 97 ; population 17, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 397 appels ; failures 2259 ; propagations 2966662 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 100.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:47 — xavier_bench_p18_1

Série de tests de Xavier avec la population d isolée: Population: 18;

- Configuration : `experiments/config/xavier_bench_p18_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p18_1_164717.json`
- Instance : bench_1 ; graine 97 ; population 18, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 403 appels ; failures 2219 ; propagations 2840912 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 101.4 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:49 — xavier_bench_p19_1

Série de tests de Xavier avec la population d isolée: Population: 19;

- Configuration : `experiments/config/xavier_bench_p19_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p19_1_164900.json`
- Instance : bench_1 ; graine 97 ; population 19, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 409 appels ; failures 2172 ; propagations 2969580 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 87.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:50 — xavier_bench_p20_1

Série de tests de Xavier avec la population d isolée: Population: 20;

- Configuration : `experiments/config/xavier_bench_p20_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p20_1_165028.json`
- Instance : bench_1 ; graine 97 ; population 20, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 415 appels ; failures 2252 ; propagations 3073967 ; nodes non rapporté ; temps de résolution 2.8 s (non déterministe)
- Durée de l'exécution : 80.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:51 — xavier_bench_p21_1

Série de tests de Xavier avec la population d isolée: Population: 21;

- Configuration : `experiments/config/xavier_bench_p21_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p21_1_165149.json`
- Instance : bench_1 ; graine 97 ; population 21, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 421 appels ; failures 2329 ; propagations 3139115 ; nodes non rapporté ; temps de résolution 2.8 s (non déterministe)
- Durée de l'exécution : 83.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:53 — xavier_bench_p22_1

Série de tests de Xavier avec la population d isolée: Population: 22;

- Configuration : `experiments/config/xavier_bench_p22_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p22_1_165314.json`
- Instance : bench_1 ; graine 97 ; population 22, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 427 appels ; failures 2178 ; propagations 3204058 ; nodes non rapporté ; temps de résolution 2.9 s (non déterministe)
- Durée de l'exécution : 81.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:54 — xavier_bench_p23_1

Série de tests de Xavier avec la population d isolée: Population: 23;

- Configuration : `experiments/config/xavier_bench_p23_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p23_1_165436.json`
- Instance : bench_1 ; graine 97 ; population 23, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 411 appels ; failures 2308 ; propagations 3057328 ; nodes non rapporté ; temps de résolution 2.7 s (non déterministe)
- Durée de l'exécution : 75.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:55 — xavier_bench_p24_1

Série de tests de Xavier avec la population d isolée: Population: 24;

- Configuration : `experiments/config/xavier_bench_p24_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p24_1_165552.json`
- Instance : bench_1 ; graine 97 ; population 24, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 416 appels ; failures 2476 ; propagations 3296180 ; nodes non rapporté ; temps de résolution 2.8 s (non déterministe)
- Durée de l'exécution : 76.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:57 — xavier_bench_p25_1

Série de tests de Xavier avec la population d isolée: Population: 25;

- Configuration : `experiments/config/xavier_bench_p25_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p25_1_165709.json`
- Instance : bench_1 ; graine 97 ; population 25, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 421 appels ; failures 2563 ; propagations 3199268 ; nodes non rapporté ; temps de résolution 2.7 s (non déterministe)
- Durée de l'exécution : 76.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:58 — xavier_bench_p26_1

Série de tests de Xavier avec la population d isolée: Population: 26;

- Configuration : `experiments/config/xavier_bench_p26_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p26_1_165826.json`
- Instance : bench_1 ; graine 97 ; population 26, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 426 appels ; failures 2620 ; propagations 3437186 ; nodes non rapporté ; temps de résolution 2.8 s (non déterministe)
- Durée de l'exécution : 76.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 16:59 — xavier_bench_p27_1

Série de tests de Xavier avec la population d isolée: Population: 27;

- Configuration : `experiments/config/xavier_bench_p27_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p27_1_165943.json`
- Instance : bench_1 ; graine 97 ; population 27, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 431 appels ; failures 2559 ; propagations 3479316 ; nodes non rapporté ; temps de résolution 2.9 s (non déterministe)
- Durée de l'exécution : 78.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:01 — xavier_bench_p28_1

Série de tests de Xavier avec la population d isolée: Population: 28;

- Configuration : `experiments/config/xavier_bench_p28_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p28_1_170102.json`
- Instance : bench_1 ; graine 97 ; population 28, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 436 appels ; failures 2610 ; propagations 3537796 ; nodes non rapporté ; temps de résolution 2.9 s (non déterministe)
- Durée de l'exécution : 78.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:02 — xavier_bench_p29_1

Série de tests de Xavier avec la population d isolée: Population: 29;

- Configuration : `experiments/config/xavier_bench_p29_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p29_1_170221.json`
- Instance : bench_1 ; graine 97 ; population 29, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 469 appels ; failures 2529 ; propagations 3701970 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 84.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:03 — xavier_bench_p30_1

Série de tests de Xavier avec la population d isolée: Population: 30;

- Configuration : `experiments/config/xavier_bench_p30_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p30_1_170346.json`
- Instance : bench_1 ; graine 97 ; population 30, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 475 appels ; failures 2667 ; propagations 3737843 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 89.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:05 — xavier_bench_p31_1

Série de tests de Xavier avec la population d isolée: Population: 31;

- Configuration : `experiments/config/xavier_bench_p31_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p31_1_170516.json`
- Instance : bench_1 ; graine 97 ; population 31, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 481 appels ; failures 2726 ; propagations 3915793 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 88.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:06 — xavier_bench_p32_1

Série de tests de Xavier avec la population d isolée: Population: 32;

- Configuration : `experiments/config/xavier_bench_p32_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p32_1_170646.json`
- Instance : bench_1 ; graine 97 ; population 32, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 487 appels ; failures 2950 ; propagations 4235797 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 87.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:08 — xavier_bench_p33_1

Série de tests de Xavier avec la population d isolée: Population: 33;

- Configuration : `experiments/config/xavier_bench_p33_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p33_1_170814.json`
- Instance : bench_1 ; graine 97 ; population 33, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 493 appels ; failures 2826 ; propagations 4041723 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 87.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:09 — xavier_bench_p34_1

Série de tests de Xavier avec la population d isolée: Population: 34;

- Configuration : `experiments/config/xavier_bench_p34_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p34_1_170942.json`
- Instance : bench_1 ; graine 97 ; population 34, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 499 appels ; failures 2846 ; propagations 3998346 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 89.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:11 — xavier_bench_p35_1

Série de tests de Xavier avec la population d isolée: Population: 35;

- Configuration : `experiments/config/xavier_bench_p35_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p35_1_171112.json`
- Instance : bench_1 ; graine 97 ; population 35, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 471 appels ; failures 2861 ; propagations 3888868 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 83.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:12 — xavier_bench_p36_1

Série de tests de Xavier avec la population d isolée: Population: 36;

- Configuration : `experiments/config/xavier_bench_p36_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p36_1_171236.json`
- Instance : bench_1 ; graine 97 ; population 36, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 2843 ; propagations 4168770 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 90.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:14 — xavier_bench_p37_1

Série de tests de Xavier avec la population d isolée: Population: 37;

- Configuration : `experiments/config/xavier_bench_p37_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p37_1_171408.json`
- Instance : bench_1 ; graine 97 ; population 37, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 481 appels ; failures 3040 ; propagations 4048187 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 85.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:15 — xavier_bench_p38_1

Série de tests de Xavier avec la population d isolée: Population: 38;

- Configuration : `experiments/config/xavier_bench_p38_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p38_1_171534.json`
- Instance : bench_1 ; graine 97 ; population 38, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 2909 ; propagations 3976950 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 86.4 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:17 — xavier_bench_p39_1

Série de tests de Xavier avec la population d isolée: Population: 39;

- Configuration : `experiments/config/xavier_bench_p39_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p39_1_171701.json`
- Instance : bench_1 ; graine 97 ; population 39, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 491 appels ; failures 2735 ; propagations 3922403 ; nodes non rapporté ; temps de résolution 3.2 s (non déterministe)
- Durée de l'exécution : 83.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:18 — xavier_bench_p40_1

Série de tests de Xavier avec la population d isolée: Population: 40;

- Configuration : `experiments/config/xavier_bench_p40_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p40_1_171825.json`
- Instance : bench_1 ; graine 97 ; population 40, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 496 appels ; failures 2689 ; propagations 3967896 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 88.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:19 — xavier_bench_p41_1

Série de tests de Xavier avec la population d isolée: Population: 41;

- Configuration : `experiments/config/xavier_bench_p41_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p41_1_171954.json`
- Instance : bench_1 ; graine 97 ; population 41, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 501 appels ; failures 2990 ; propagations 4242803 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 89.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:21 — xavier_bench_p42_1

Série de tests de Xavier avec la population d isolée: Population: 42;

- Configuration : `experiments/config/xavier_bench_p42_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p42_1_172124.json`
- Instance : bench_1 ; graine 97 ; population 42, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 2946 ; propagations 4244689 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 89.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:22 — xavier_bench_p43_1

Série de tests de Xavier avec la population d isolée: Population: 43;

- Configuration : `experiments/config/xavier_bench_p43_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p43_1_172254.json`
- Instance : bench_1 ; graine 97 ; population 43, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 3061 ; propagations 4394877 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 91.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:24 — xavier_bench_p44_1

Série de tests de Xavier avec la population d isolée: Population: 44;

- Configuration : `experiments/config/xavier_bench_p44_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p44_1_172426.json`
- Instance : bench_1 ; graine 97 ; population 44, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 2866 ; propagations 4139477 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 91.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:25 — xavier_bench_p45_1

Série de tests de Xavier avec la population d isolée: Population: 45;

- Configuration : `experiments/config/xavier_bench_p45_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p45_1_172558.json`
- Instance : bench_1 ; graine 97 ; population 45, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 521 appels ; failures 3102 ; propagations 4395948 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 92.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:27 — xavier_bench_p46_1

Série de tests de Xavier avec la population d isolée: Population: 46;

- Configuration : `experiments/config/xavier_bench_p46_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p46_1_172731.json`
- Instance : bench_1 ; graine 97 ; population 46, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 526 appels ; failures 2937 ; propagations 4289692 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 93.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:29 — xavier_bench_p47_1

Série de tests de Xavier avec la population d isolée: Population: 47;

- Configuration : `experiments/config/xavier_bench_p47_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p47_1_172906.json`
- Instance : bench_1 ; graine 97 ; population 47, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 531 appels ; failures 3070 ; propagations 4481574 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 94.4 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:30 — xavier_bench_p48_1

Série de tests de Xavier avec la population d isolée: Population: 48;

- Configuration : `experiments/config/xavier_bench_p48_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p48_1_173041.json`
- Instance : bench_1 ; graine 97 ; population 48, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 536 appels ; failures 3020 ; propagations 4471477 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 95.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:32 — xavier_bench_p49_1

Série de tests de Xavier avec la population d isolée: Population: 49;

- Configuration : `experiments/config/xavier_bench_p49_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p49_1_173217.json`
- Instance : bench_1 ; graine 97 ; population 49, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 541 appels ; failures 3155 ; propagations 4605306 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 96.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:33 — xavier_bench_p50_1

Série de tests de Xavier avec la population d isolée: Population: 50;

- Configuration : `experiments/config/xavier_bench_p50_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p50_1_173354.json`
- Instance : bench_1 ; graine 97 ; population 50, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 546 appels ; failures 3297 ; propagations 4769830 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 97.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:35 — xavier_bench_p51_1

Série de tests de Xavier avec la population d isolée: Population: 51;

- Configuration : `experiments/config/xavier_bench_p51_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p51_1_173532.json`
- Instance : bench_1 ; graine 97 ; population 51, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 551 appels ; failures 3130 ; propagations 4704910 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 98.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:37 — xavier_bench_p52_1

Série de tests de Xavier avec la population d isolée: Population: 52;

- Configuration : `experiments/config/xavier_bench_p52_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p52_1_173711.json`
- Instance : bench_1 ; graine 97 ; population 52, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 556 appels ; failures 3209 ; propagations 4774321 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 99.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:38 — xavier_bench_p53_1

Série de tests de Xavier avec la population d isolée: Population: 53;

- Configuration : `experiments/config/xavier_bench_p53_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p53_1_173851.json`
- Instance : bench_1 ; graine 97 ; population 53, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 561 appels ; failures 3428 ; propagations 4935714 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 99.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:40 — xavier_bench_p54_1

Série de tests de Xavier avec la population d isolée: Population: 54;

- Configuration : `experiments/config/xavier_bench_p54_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p54_1_174031.json`
- Instance : bench_1 ; graine 97 ; population 54, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 566 appels ; failures 3376 ; propagations 4924449 ; nodes non rapporté ; temps de résolution 4.0 s (non déterministe)
- Durée de l'exécution : 99.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:42 — xavier_bench_p55_1

Série de tests de Xavier avec la population d isolée: Population: 55;

- Configuration : `experiments/config/xavier_bench_p55_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p55_1_174211.json`
- Instance : bench_1 ; graine 97 ; population 55, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 571 appels ; failures 3520 ; propagations 4934233 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 126.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:44 — xavier_bench_p56_1

Série de tests de Xavier avec la population d isolée: Population: 56;

- Configuration : `experiments/config/xavier_bench_p56_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p56_1_174418.json`
- Instance : bench_1 ; graine 97 ; population 56, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 576 appels ; failures 3497 ; propagations 4976486 ; nodes non rapporté ; temps de résolution 5.3 s (non déterministe)
- Durée de l'exécution : 140.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:46 — xavier_bench_p57_1

Série de tests de Xavier avec la population d isolée: Population: 57;

- Configuration : `experiments/config/xavier_bench_p57_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p57_1_174639.json`
- Instance : bench_1 ; graine 97 ; population 57, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 581 appels ; failures 3428 ; propagations 5016157 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 141.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:49 — xavier_bench_p58_1

Série de tests de Xavier avec la population d isolée: Population: 58;

- Configuration : `experiments/config/xavier_bench_p58_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p58_1_174901.json`
- Instance : bench_1 ; graine 97 ; population 58, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 586 appels ; failures 3411 ; propagations 5010277 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 142.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:51 — xavier_bench_p59_1

Série de tests de Xavier avec la population d isolée: Population: 59;

- Configuration : `experiments/config/xavier_bench_p59_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p59_1_175124.json`
- Instance : bench_1 ; graine 97 ; population 59, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 591 appels ; failures 3446 ; propagations 5175366 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 144.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:53 — xavier_bench_p60_1

Série de tests de Xavier avec la population d isolée: Population: 60;

- Configuration : `experiments/config/xavier_bench_p60_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p60_1_175350.json`
- Instance : bench_1 ; graine 97 ; population 60, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 596 appels ; failures 3421 ; propagations 5203874 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 143.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:56 — xavier_bench_p61_1

Série de tests de Xavier avec la population d isolée: Population: 61;

- Configuration : `experiments/config/xavier_bench_p61_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p61_1_175614.json`
- Instance : bench_1 ; graine 97 ; population 61, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 661 appels ; failures 3863 ; propagations 5831128 ; nodes non rapporté ; temps de résolution 4.9 s (non déterministe)
- Durée de l'exécution : 129.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 17:58 — xavier_bench_p62_1

Série de tests de Xavier avec la population d isolée: Population: 62;

- Configuration : `experiments/config/xavier_bench_p62_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p62_1_175824.json`
- Instance : bench_1 ; graine 97 ; population 62, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 606 appels ; failures 3433 ; propagations 5209528 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 108.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:00 — xavier_bench_p63_1

Série de tests de Xavier avec la population d isolée: Population: 63;

- Configuration : `experiments/config/xavier_bench_p63_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p63_1_180013.json`
- Instance : bench_1 ; graine 97 ; population 63, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 611 appels ; failures 3656 ; propagations 5383390 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 108.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:02 — xavier_bench_p64_1

Série de tests de Xavier avec la population d isolée: Population: 64;

- Configuration : `experiments/config/xavier_bench_p64_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p64_1_180202.json`
- Instance : bench_1 ; graine 97 ; population 64, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 616 appels ; failures 3673 ; propagations 5490186 ; nodes non rapporté ; temps de résolution 4.4 s (non déterministe)
- Durée de l'exécution : 108.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:03 — xavier_bench_p65_1

Série de tests de Xavier avec la population d isolée: Population: 65;

- Configuration : `experiments/config/xavier_bench_p65_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p65_1_180351.json`
- Instance : bench_1 ; graine 97 ; population 65, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 621 appels ; failures 3571 ; propagations 5437290 ; nodes non rapporté ; temps de résolution 4.3 s (non déterministe)
- Durée de l'exécution : 109.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:05 — xavier_bench_p66_1

Série de tests de Xavier avec la population d isolée: Population: 66;

- Configuration : `experiments/config/xavier_bench_p66_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p66_1_180541.json`
- Instance : bench_1 ; graine 97 ; population 66, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 626 appels ; failures 3735 ; propagations 5675131 ; nodes non rapporté ; temps de résolution 5.3 s (non déterministe)
- Durée de l'exécution : 133.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:07 — xavier_bench_p67_1

Série de tests de Xavier avec la population d isolée: Population: 67;

- Configuration : `experiments/config/xavier_bench_p67_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p67_1_180755.json`
- Instance : bench_1 ; graine 97 ; population 67, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 697 appels ; failures 4164 ; propagations 6300312 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 170.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:10 — xavier_bench_p68_1

Série de tests de Xavier avec la population d isolée: Population: 68;

- Configuration : `experiments/config/xavier_bench_p68_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p68_1_181047.json`
- Instance : bench_1 ; graine 97 ; population 68, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 636 appels ; failures 3595 ; propagations 5569172 ; nodes non rapporté ; temps de résolution 5.9 s (non déterministe)
- Durée de l'exécution : 152.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:13 — xavier_bench_p69_1

Série de tests de Xavier avec la population d isolée: Population: 69;

- Configuration : `experiments/config/xavier_bench_p69_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p69_1_181321.json`
- Instance : bench_1 ; graine 97 ; population 69, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 641 appels ; failures 3719 ; propagations 5724275 ; nodes non rapporté ; temps de résolution 4.7 s (non déterministe)
- Durée de l'exécution : 116.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:15 — xavier_bench_p70_1

Série de tests de Xavier avec la population d isolée: Population: 70;

- Configuration : `experiments/config/xavier_bench_p70_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p70_1_181518.json`
- Instance : bench_1 ; graine 97 ; population 70, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 646 appels ; failures 3736 ; propagations 5654249 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 113.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:17 — xavier_bench_p71_1

Série de tests de Xavier avec la population d isolée: Population: 71;

- Configuration : `experiments/config/xavier_bench_p71_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p71_1_181712.json`
- Instance : bench_1 ; graine 97 ; population 71, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 721 appels ; failures 4347 ; propagations 6558314 ; nodes non rapporté ; temps de résolution 5.3 s (non déterministe)
- Durée de l'exécution : 126.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:19 — xavier_bench_p72_1

Série de tests de Xavier avec la population d isolée: Population: 72;

- Configuration : `experiments/config/xavier_bench_p72_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p72_1_181920.json`
- Instance : bench_1 ; graine 97 ; population 72, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 656 appels ; failures 3910 ; propagations 5878804 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 136.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:21 — xavier_bench_p73_1

Série de tests de Xavier avec la population d isolée: Population: 73;

- Configuration : `experiments/config/xavier_bench_p73_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p73_1_182137.json`
- Instance : bench_1 ; graine 97 ; population 73, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 661 appels ; failures 3868 ; propagations 5984051 ; nodes non rapporté ; temps de résolution 6.4 s (non déterministe)
- Durée de l'exécution : 162.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:24 — xavier_bench_p74_1

Série de tests de Xavier avec la population d isolée: Population: 74;

- Configuration : `experiments/config/xavier_bench_p74_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p74_1_182421.json`
- Instance : bench_1 ; graine 97 ; population 74, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 666 appels ; failures 3861 ; propagations 5927290 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 163.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:27 — xavier_bench_p75_1

Série de tests de Xavier avec la population d isolée: Population: 75;

- Configuration : `experiments/config/xavier_bench_p75_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p75_1_182705.json`
- Instance : bench_1 ; graine 97 ; population 75, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 745 appels ; failures 4384 ; propagations 6737330 ; nodes non rapporté ; temps de résolution 7.3 s (non déterministe)
- Durée de l'exécution : 183.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:30 — xavier_bench_p76_1

Série de tests de Xavier avec la population d isolée: Population: 76;

- Configuration : `experiments/config/xavier_bench_p76_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p76_1_183008.json`
- Instance : bench_1 ; graine 97 ; population 76, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 676 appels ; failures 4024 ; propagations 6088364 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 162.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:32 — xavier_bench_p77_1

Série de tests de Xavier avec la population d isolée: Population: 77;

- Configuration : `experiments/config/xavier_bench_p77_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p77_1_183252.json`
- Instance : bench_1 ; graine 97 ; population 77, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 681 appels ; failures 3905 ; propagations 6057302 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 129.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:35 — xavier_bench_p78_1

Série de tests de Xavier avec la population d isolée: Population: 78;

- Configuration : `experiments/config/xavier_bench_p78_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p78_1_183502.json`
- Instance : bench_1 ; graine 97 ; population 78, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 686 appels ; failures 4055 ; propagations 6203543 ; nodes non rapporté ; temps de résolution 5.0 s (non déterministe)
- Durée de l'exécution : 123.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:37 — xavier_bench_p79_1

Série de tests de Xavier avec la population d isolée: Population: 79;

- Configuration : `experiments/config/xavier_bench_p79_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p79_1_183706.json`
- Instance : bench_1 ; graine 97 ; population 79, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 691 appels ; failures 4109 ; propagations 6351633 ; nodes non rapporté ; temps de résolution 5.1 s (non déterministe)
- Durée de l'exécution : 121.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:39 — xavier_bench_p80_1

Série de tests de Xavier avec la population d isolée: Population: 80;

- Configuration : `experiments/config/xavier_bench_p80_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p80_1_183908.json`
- Instance : bench_1 ; graine 97 ; population 80, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 696 appels ; failures 4157 ; propagations 6372500 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 137.4 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:41 — xavier_bench_p81_1

Série de tests de Xavier avec la population d isolée: Population: 81;

- Configuration : `experiments/config/xavier_bench_p81_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p81_1_184126.json`
- Instance : bench_1 ; graine 97 ; population 81, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 701 appels ; failures 4024 ; propagations 6114172 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 170.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:44 — xavier_bench_p82_1

Série de tests de Xavier avec la population d isolée: Population: 82;

- Configuration : `experiments/config/xavier_bench_p82_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p82_1_184418.json`
- Instance : bench_1 ; graine 97 ; population 82, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 706 appels ; failures 4347 ; propagations 6496674 ; nodes non rapporté ; temps de résolution 6.5 s (non déterministe)
- Durée de l'exécution : 165.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:47 — xavier_bench_p83_1

Série de tests de Xavier avec la population d isolée: Population: 83;

- Configuration : `experiments/config/xavier_bench_p83_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p83_1_184704.json`
- Instance : bench_1 ; graine 97 ; population 83, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 711 appels ; failures 4163 ; propagations 6399227 ; nodes non rapporté ; temps de résolution 5.2 s (non déterministe)
- Durée de l'exécution : 126.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:49 — xavier_bench_p84_1

Série de tests de Xavier avec la population d isolée: Population: 84;

- Configuration : `experiments/config/xavier_bench_p84_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p84_1_184911.json`
- Instance : bench_1 ; graine 97 ; population 84, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 799 appels ; failures 4897 ; propagations 7525404 ; nodes non rapporté ; temps de résolution 5.9 s (non déterministe)
- Durée de l'exécution : 141.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:51 — xavier_bench_p85_1

Série de tests de Xavier avec la population d isolée: Population: 85;

- Configuration : `experiments/config/xavier_bench_p85_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p85_1_185133.json`
- Instance : bench_1 ; graine 97 ; population 85, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 721 appels ; failures 4152 ; propagations 6482824 ; nodes non rapporté ; temps de résolution 5.2 s (non déterministe)
- Durée de l'exécution : 126.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:53 — xavier_bench_p86_1

Série de tests de Xavier avec la population d isolée: Population: 86;

- Configuration : `experiments/config/xavier_bench_p86_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p86_1_185340.json`
- Instance : bench_1 ; graine 97 ; population 86, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 726 appels ; failures 4530 ; propagations 6740024 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 128.3 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:55 — xavier_bench_p87_1

Série de tests de Xavier avec la population d isolée: Population: 87;

- Configuration : `experiments/config/xavier_bench_p87_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p87_1_185549.json`
- Instance : bench_1 ; graine 97 ; population 87, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 817 appels ; failures 4902 ; propagations 7649901 ; nodes non rapporté ; temps de résolution 6.0 s (non déterministe)
- Durée de l'exécution : 143.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 18:58 — xavier_bench_p88_1

Série de tests de Xavier avec la population d isolée: Population: 88;

- Configuration : `experiments/config/xavier_bench_p88_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p88_1_185814.json`
- Instance : bench_1 ; graine 97 ; population 88, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 736 appels ; failures 4562 ; propagations 6764801 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 129.5 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:00 — xavier_bench_p89_1

Série de tests de Xavier avec la population d isolée: Population: 89;

- Configuration : `experiments/config/xavier_bench_p89_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p89_1_190024.json`
- Instance : bench_1 ; graine 97 ; population 89, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 741 appels ; failures 4475 ; propagations 6695019 ; nodes non rapporté ; temps de résolution 5.4 s (non déterministe)
- Durée de l'exécution : 130.6 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:02 — xavier_bench_p90_1

Série de tests de Xavier avec la population d isolée: Population: 90;

- Configuration : `experiments/config/xavier_bench_p90_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p90_1_190235.json`
- Instance : bench_1 ; graine 97 ; population 90, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 746 appels ; failures 4530 ; propagations 6887374 ; nodes non rapporté ; temps de résolution 5.5 s (non déterministe)
- Durée de l'exécution : 131.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:04 — xavier_bench_p91_1

Série de tests de Xavier avec la population d isolée: Population: 91;

- Configuration : `experiments/config/xavier_bench_p91_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p91_1_190448.json`
- Instance : bench_1 ; graine 97 ; population 91, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 751 appels ; failures 4468 ; propagations 6677320 ; nodes non rapporté ; temps de résolution 5.5 s (non déterministe)
- Durée de l'exécution : 136.2 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:07 — xavier_bench_p92_1

Série de tests de Xavier avec la population d isolée: Population: 92;

- Configuration : `experiments/config/xavier_bench_p92_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p92_1_190704.json`
- Instance : bench_1 ; graine 97 ; population 92, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 756 appels ; failures 4722 ; propagations 6987590 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 133.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:09 — xavier_bench_p93_1

Série de tests de Xavier avec la population d isolée: Population: 93;

- Configuration : `experiments/config/xavier_bench_p93_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p93_1_190919.json`
- Instance : bench_1 ; graine 97 ; population 93, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 853 appels ; failures 5167 ; propagations 8049954 ; nodes non rapporté ; temps de résolution 6.4 s (non déterministe)
- Durée de l'exécution : 150.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:11 — xavier_bench_p94_1

Série de tests de Xavier avec la population d isolée: Population: 94;

- Configuration : `experiments/config/xavier_bench_p94_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p94_1_191150.json`
- Instance : bench_1 ; graine 97 ; population 94, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 859 appels ; failures 5183 ; propagations 8095498 ; nodes non rapporté ; temps de résolution 6.4 s (non déterministe)
- Durée de l'exécution : 151.4 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:14 — xavier_bench_p95_1

Série de tests de Xavier avec la population d isolée: Population: 95;

- Configuration : `experiments/config/xavier_bench_p95_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p95_1_191422.json`
- Instance : bench_1 ; graine 97 ; population 95, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 771 appels ; failures 4532 ; propagations 7098197 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 136.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:16 — xavier_bench_p96_1

Série de tests de Xavier avec la population d isolée: Population: 96;

- Configuration : `experiments/config/xavier_bench_p96_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p96_1_191639.json`
- Instance : bench_1 ; graine 97 ; population 96, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 776 appels ; failures 4530 ; propagations 7013911 ; nodes non rapporté ; temps de résolution 5.6 s (non déterministe)
- Durée de l'exécution : 137.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:18 — xavier_bench_p97_1

Série de tests de Xavier avec la population d isolée: Population: 97;

- Configuration : `experiments/config/xavier_bench_p97_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p97_1_191857.json`
- Instance : bench_1 ; graine 97 ; population 97, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 877 appels ; failures 5371 ; propagations 8407417 ; nodes non rapporté ; temps de résolution 6.6 s (non déterministe)
- Durée de l'exécution : 155.0 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:21 — xavier_bench_p98_1

Série de tests de Xavier avec la population d isolée: Population: 98;

- Configuration : `experiments/config/xavier_bench_p98_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p98_1_192132.json`
- Instance : bench_1 ; graine 97 ; population 98, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 786 appels ; failures 4510 ; propagations 7169695 ; nodes non rapporté ; temps de résolution 5.7 s (non déterministe)
- Durée de l'exécution : 138.9 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:23 — xavier_bench_p99_1

Série de tests de Xavier avec la population d isolée: Population: 99;

- Configuration : `experiments/config/xavier_bench_p99_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p99_1_192352.json`
- Instance : bench_1 ; graine 97 ; population 99, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 791 appels ; failures 4629 ; propagations 7359624 ; nodes non rapporté ; temps de résolution 5.8 s (non déterministe)
- Durée de l'exécution : 139.8 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:26 — xavier_bench_p100_1

Série de tests de Xavier avec la population d isolée: Population: 100;

- Configuration : `experiments/config/xavier_bench_p100_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_p100_1_192612.json`
- Instance : bench_1 ; graine 97 ; population 100, NR = 10, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 5 restart(s)
- **Effort cumulé du solveur** : 895 appels ; failures 5311 ; propagations 8453477 ; nodes non rapporté ; temps de résolution 6.7 s (non déterministe)
- Durée de l'exécution : 158.1 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:28 — xavier_bench_c0_1

Série de tests de Xavier avec le crossover d isolée: Crossover: 0;

- Configuration : `experiments/config/xavier_bench_c0_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_c0_1_192851.json`
- Instance : bench_1 ; graine 97 ; population 100, NR = 0, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 95** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 596 appels ; failures 3656 ; propagations 5909837 ; nodes non rapporté ; temps de résolution 4.6 s (non déterministe)
- Durée de l'exécution : 105.4 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**

## 2026-11-26 19:30 — xavier_bench_c1_1

Série de tests de Xavier avec le crossover d isolée: Crossover: 1;

- Configuration : `experiments/config/xavier_bench_c1_1.json`
- Résultats : `experiments/results/2026-11-26/xavier_bench_c1_1_193037.json`
- Instance : bench_1 ; graine 97 ; population 100, NR = 1, NM = 10, 10 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 94** (faisable) ; 10 générations, 4 restart(s)
- **Effort cumulé du solveur** : 616 appels ; failures 3735 ; propagations 6133114 ; nodes non rapporté ; temps de résolution 4.8 s (non déterministe)
- Durée de l'exécution : 108.7 s ; commit `25afb1e0e5c36224c4d3bcd2d80ca8de996ddaa3` — **copie de travail modifiée : ce résultat ne peut pas être reproduit à partir de ce seul commit**
