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

## 2026-11-25 20:59 — bench2_initial_ls_false_s00

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 0.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s00.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s00_205941.json`
- Instance : bench_2 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6341 ; propagations 4236861 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 185.5 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s01

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 1.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s01.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s01_205940.json`
- Instance : bench_2 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6132 ; propagations 3793375 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 184.9 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s02

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 2.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s02.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s02_205941.json`
- Instance : bench_2 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 4339 ; propagations 3090260 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 184.6 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s03

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 3.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s03.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s03_205941.json`
- Instance : bench_2 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6445 ; propagations 4076101 ; nodes non rapporté ; temps de résolution 3.8 s (non déterministe)
- Durée de l'exécution : 184.3 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s04

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 4.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s04.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s04_205941.json`
- Instance : bench_2 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 5120 ; propagations 2961186 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 184.2 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s05

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 5.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s05.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s05_205941.json`
- Instance : bench_2 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 5091 ; propagations 3168564 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 185.2 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s06

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 6.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s06.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s06_205941.json`
- Instance : bench_2 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 5431 ; propagations 3438716 ; nodes non rapporté ; temps de résolution 3.4 s (non déterministe)
- Durée de l'exécution : 183.8 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s07

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 7.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s07.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s07_205941.json`
- Instance : bench_2 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 5405 ; propagations 3368440 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 185.3 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s08

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 8.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s08.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s08_205941.json`
- Instance : bench_2 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 5242 ; propagations 3247419 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 184.8 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s09

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 9.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s09.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s09_205941.json`
- Instance : bench_2 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6747 ; propagations 4100116 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 184.8 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s10

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 10.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s10.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s10_205940.json`
- Instance : bench_2 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6453 ; propagations 3884679 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 185.4 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s11

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 11.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s11.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s11_205941.json`
- Instance : bench_2 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6382 ; propagations 3865359 ; nodes non rapporté ; temps de résolution 3.5 s (non déterministe)
- Durée de l'exécution : 185.5 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s12

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 12.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s12.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s12_205941.json`
- Instance : bench_2 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 4899 ; propagations 2988652 ; nodes non rapporté ; temps de résolution 3.1 s (non déterministe)
- Durée de l'exécution : 183.2 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s13

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 13.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s13.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s13_205941.json`
- Instance : bench_2 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 5349 ; propagations 3630449 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 184.5 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s14

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 14.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s14.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s14_205941.json`
- Instance : bench_2 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6052 ; propagations 4185780 ; nodes non rapporté ; temps de résolution 3.6 s (non déterministe)
- Durée de l'exécution : 184.7 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s15

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 15.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s15.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s15_205941.json`
- Instance : bench_2 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 4907 ; propagations 3145344 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 185.5 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s16

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 16.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s16.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s16_205940.json`
- Instance : bench_2 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6715 ; propagations 4196266 ; nodes non rapporté ; temps de résolution 3.7 s (non déterministe)
- Durée de l'exécution : 185.5 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s17

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 17.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s17.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s17_205941.json`
- Instance : bench_2 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6801 ; propagations 4724807 ; nodes non rapporté ; temps de résolution 3.9 s (non déterministe)
- Durée de l'exécution : 184.3 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s18

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 18.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s18.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s18_205941.json`
- Instance : bench_2 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 5511 ; propagations 3235218 ; nodes non rapporté ; temps de résolution 3.3 s (non déterministe)
- Durée de l'exécution : 185.5 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 20:59 — bench2_initial_ls_false_s19

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 19.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s19.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s19_205940.json`
- Instance : bench_2 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 3943 ; propagations 2331583 ; nodes non rapporté ; temps de résolution 2.8 s (non déterministe)
- Durée de l'exécution : 185.1 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 21:02 — bench2_initial_ls_false_s20

Influence de la recherche locale initiale sur bench_2 : population 18, 26 generations, NR=3, NM=12, recherche locale initiale desactivee, graine 20.

- Configuration : `experiments/config/bench2_initial_ls/bench2_initial_ls_false_s20.json`
- Résultats : `experiments/results/2026-11-25/bench2_initial_ls_false_s20_210245.json`
- Instance : bench_2 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 468 appels ; failures 6413 ; propagations 4077708 ; nodes non rapporté ; temps de résolution 2.9 s (non déterministe)
- Durée de l'exécution : 139.2 s ; commit `9440573a71ce20c9cbfbd68dfe648bc93b005d67`

## 2026-11-25 — Synthèse : recherche locale initiale sur bench_2

Comparaison de initial_local_search=True et False,
avec une population de 18, 26 générations, NR=3 et NM=12.

Les deux configurations atteignent l'optimum 38 pour
les 21 graines étudiées.

La désactivation de la recherche locale initiale réduit
les appels au solveur de 9.3 %, les propagations de 19.9 %
et le temps de résolution cumulé de 14.6 %.

La convergence moyenne est légèrement moins rapide,
mais la médiane et le pire cas observé sont identiques.

Ce paramètre contrôle la recherche locale à l'initialisation
et lors des redémarrages, sans désactiver celle appliquée
après les croisements et les mutations.

La configuration False est retenue provisoirement.
Une validation sur d'autres instances reste nécessaire.

- Rapport : `experiments/analysis/bench2_initial_ls.md`
- Script : `experiments/analysis/analyze_initial_ls.py`
- Configurations : `experiments/config/bench2_initial_ls/`
- Nouvelles exécutions : 21.
- Exécutions de référence réutilisées : 21.

## 2026-11-26 13:29 — bench3_pop162_s00

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s00_132907.json`
- Instance : bench_3 ; graine 0 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000077** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 194451 ; propagations 854345680 ; nodes non rapporté ; temps de résolution 434.0 s (non déterministe)
- Durée de l'exécution : 663.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s01

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s01_132908.json`
- Instance : bench_3 ; graine 1 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000068** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 191752 ; propagations 837907412 ; nodes non rapporté ; temps de résolution 428.8 s (non déterministe)
- Durée de l'exécution : 657.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s02

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s02_132915.json`
- Instance : bench_3 ; graine 2 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 3000049** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 207989 ; propagations 881432364 ; nodes non rapporté ; temps de résolution 456.0 s (non déterministe)
- Durée de l'exécution : 686.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s03

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s03_132920.json`
- Instance : bench_3 ; graine 3 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000084** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 201577 ; propagations 848187884 ; nodes non rapporté ; temps de résolution 438.0 s (non déterministe)
- Durée de l'exécution : 667.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s04

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s04_132924.json`
- Instance : bench_3 ; graine 4 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 3000092** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 189334 ; propagations 798922024 ; nodes non rapporté ; temps de résolution 414.2 s (non déterministe)
- Durée de l'exécution : 643.0 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s05

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s05_132926.json`
- Instance : bench_3 ; graine 5 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 3000067** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 190321 ; propagations 811362086 ; nodes non rapporté ; temps de résolution 419.5 s (non déterministe)
- Durée de l'exécution : 650.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s06

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s06_132928.json`
- Instance : bench_3 ; graine 6 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 3000069** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 190984 ; propagations 844294653 ; nodes non rapporté ; temps de résolution 430.5 s (non déterministe)
- Durée de l'exécution : 660.6 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s07

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s07_132934.json`
- Instance : bench_3 ; graine 7 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000062** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 181431 ; propagations 801419649 ; nodes non rapporté ; temps de résolution 404.9 s (non déterministe)
- Durée de l'exécution : 633.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop162_s08

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s08_132935.json`
- Instance : bench_3 ; graine 8 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000066** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 203890 ; propagations 866307651 ; nodes non rapporté ; temps de résolution 442.3 s (non déterministe)
- Durée de l'exécution : 671.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s09

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s09_133002.json`
- Instance : bench_3 ; graine 9 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000099** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 193994 ; propagations 823608855 ; nodes non rapporté ; temps de résolution 431.9 s (non déterministe)
- Durée de l'exécution : 662.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s10

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s10_133011.json`
- Instance : bench_3 ; graine 10 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 207311 ; propagations 873272893 ; nodes non rapporté ; temps de résolution 449.2 s (non déterministe)
- Durée de l'exécution : 677.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s11

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s11_133014.json`
- Instance : bench_3 ; graine 11 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 3000043** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 190044 ; propagations 829064643 ; nodes non rapporté ; temps de résolution 426.7 s (non déterministe)
- Durée de l'exécution : 656.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s12

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s12_133014.json`
- Instance : bench_3 ; graine 12 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000055** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 195043 ; propagations 859394286 ; nodes non rapporté ; temps de résolution 448.3 s (non déterministe)
- Durée de l'exécution : 677.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s13

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s13_133033.json`
- Instance : bench_3 ; graine 13 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000078** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 191520 ; propagations 836707376 ; nodes non rapporté ; temps de résolution 425.7 s (non déterministe)
- Durée de l'exécution : 656.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s14

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s14_133036.json`
- Instance : bench_3 ; graine 14 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 3000072** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 197191 ; propagations 821753950 ; nodes non rapporté ; temps de résolution 424.6 s (non déterministe)
- Durée de l'exécution : 652.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s15

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s15_133040.json`
- Instance : bench_3 ; graine 15 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000062** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 191717 ; propagations 801692179 ; nodes non rapporté ; temps de résolution 415.3 s (non déterministe)
- Durée de l'exécution : 644.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s16

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s16_133043.json`
- Instance : bench_3 ; graine 16 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000075** (infaisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 196540 ; propagations 852786665 ; nodes non rapporté ; temps de résolution 439.0 s (non déterministe)
- Durée de l'exécution : 665.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:30 — bench3_pop162_s17

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s17_133046.json`
- Instance : bench_3 ; graine 17 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000077** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 210819 ; propagations 875361699 ; nodes non rapporté ; temps de résolution 447.2 s (non déterministe)
- Durée de l'exécution : 670.6 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:35 — bench3_pop162_s18

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s18_133544.json`
- Instance : bench_3 ; graine 18 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000048** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 189250 ; propagations 807466556 ; nodes non rapporté ; temps de résolution 379.4 s (non déterministe)
- Durée de l'exécution : 579.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:38 — bench3_pop162_s19

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s19_133827.json`
- Instance : bench_3 ; graine 19 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000069** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 195185 ; propagations 813836359 ; nodes non rapporté ; temps de résolution 351.5 s (non déterministe)
- Durée de l'exécution : 540.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:40 — bench3_pop162_s20

Comparaison population-generations sur bench_3 : population 162, 2 generations, NR=54, NM=54, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench3_population/bench3_pop162_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop162_s20_134007.json`
- Instance : bench_3 ; graine 20 ; population 162, NR = 54, NM = 54, 2 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 2000107** (faisable) ; 2 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 197902 ; propagations 825661933 ; nodes non rapporté ; temps de résolution 340.3 s (non déterministe)
- Durée de l'exécution : 520.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s00

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s00_131327.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 73438 ; propagations 325403676 ; nodes non rapporté ; temps de résolution 167.4 s (non déterministe)
- Durée de l'exécution : 398.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s01

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s01_131335.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 44420 ; propagations 192093915 ; nodes non rapporté ; temps de résolution 95.9 s (non déterministe)
- Durée de l'exécution : 322.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s02

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s02_131343.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 61738 ; propagations 275871246 ; nodes non rapporté ; temps de résolution 135.3 s (non déterministe)
- Durée de l'exécution : 365.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s03

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s03_131347.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 80075 ; propagations 364838837 ; nodes non rapporté ; temps de résolution 185.6 s (non déterministe)
- Durée de l'exécution : 423.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s04

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s04_131348.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 112690 ; propagations 491727402 ; nodes non rapporté ; temps de résolution 244.2 s (non déterministe)
- Durée de l'exécution : 483.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s05

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s05_131348.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 69460 ; propagations 318486737 ; nodes non rapporté ; temps de résolution 158.4 s (non déterministe)
- Durée de l'exécution : 394.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s06

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s06_131350.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 76704 ; propagations 356005195 ; nodes non rapporté ; temps de résolution 177.5 s (non déterministe)
- Durée de l'exécution : 414.7 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:13 — bench3_pop18_s07

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s07_131357.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 52** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63965 ; propagations 281508326 ; nodes non rapporté ; temps de résolution 139.1 s (non déterministe)
- Durée de l'exécution : 369.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s08

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s08_131402.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 67955 ; propagations 302375771 ; nodes non rapporté ; temps de résolution 145.7 s (non déterministe)
- Durée de l'exécution : 377.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s09

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s09_131403.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 71746 ; propagations 298970724 ; nodes non rapporté ; temps de résolution 144.8 s (non déterministe)
- Durée de l'exécution : 372.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s10

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s10_131403.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 33** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52330 ; propagations 236122936 ; nodes non rapporté ; temps de résolution 118.4 s (non déterministe)
- Durée de l'exécution : 348.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s11

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s11_131403.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 77860 ; propagations 351567128 ; nodes non rapporté ; temps de résolution 173.7 s (non déterministe)
- Durée de l'exécution : 412.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s12

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s12_131408.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 85110 ; propagations 398299027 ; nodes non rapporté ; temps de résolution 199.2 s (non déterministe)
- Durée de l'exécution : 428.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s13

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s13_131411.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 98947 ; propagations 435310094 ; nodes non rapporté ; temps de résolution 223.3 s (non déterministe)
- Durée de l'exécution : 461.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s14

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s14_131415.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 88** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 87399 ; propagations 399283246 ; nodes non rapporté ; temps de résolution 202.2 s (non déterministe)
- Durée de l'exécution : 434.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s15

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s15_131416.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 75211 ; propagations 329094570 ; nodes non rapporté ; temps de résolution 163.4 s (non déterministe)
- Durée de l'exécution : 402.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s16

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s16_131419.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 94417 ; propagations 429995934 ; nodes non rapporté ; temps de résolution 218.2 s (non déterministe)
- Durée de l'exécution : 448.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s17

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s17_131420.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 58269 ; propagations 259728250 ; nodes non rapporté ; temps de résolution 132.3 s (non déterministe)
- Durée de l'exécution : 369.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s18

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s18_131428.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 72584 ; propagations 326350251 ; nodes non rapporté ; temps de résolution 160.4 s (non déterministe)
- Durée de l'exécution : 397.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:14 — bench3_pop18_s19

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s19_131454.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69485 ; propagations 297197700 ; nodes non rapporté ; temps de résolution 148.2 s (non déterministe)
- Durée de l'exécution : 377.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:18 — bench3_pop18_s20

Comparaison population-generations sur bench_3 : population 18, 26 generations, NR=6, NM=6, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench3_population/bench3_pop18_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop18_s20_131858.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 92471 ; propagations 432050119 ; nodes non rapporté ; temps de résolution 219.6 s (non déterministe)
- Durée de l'exécution : 451.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:19 — bench3_pop54_s00

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s00_131950.json`
- Instance : bench_3 ; graine 0 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 44** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 142060 ; propagations 628108424 ; nodes non rapporté ; temps de résolution 321.0 s (non déterministe)
- Durée de l'exécution : 551.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:19 — bench3_pop54_s01

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s01_131953.json`
- Instance : bench_3 ; graine 1 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 52** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 140878 ; propagations 646656763 ; nodes non rapporté ; temps de résolution 330.6 s (non déterministe)
- Durée de l'exécution : 560.7 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s02

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s02_132007.json`
- Instance : bench_3 ; graine 2 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 55** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 139565 ; propagations 611224377 ; nodes non rapporté ; temps de résolution 309.0 s (non déterministe)
- Durée de l'exécution : 539.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s03

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s03_132008.json`
- Instance : bench_3 ; graine 3 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 44** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 137635 ; propagations 609095016 ; nodes non rapporté ; temps de résolution 307.7 s (non déterministe)
- Durée de l'exécution : 538.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s04

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s04_132017.json`
- Instance : bench_3 ; graine 4 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 33** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 142708 ; propagations 624362342 ; nodes non rapporté ; temps de résolution 315.8 s (non déterministe)
- Durée de l'exécution : 546.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s05

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s05_132021.json`
- Instance : bench_3 ; graine 5 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 136936 ; propagations 620998082 ; nodes non rapporté ; temps de résolution 307.9 s (non déterministe)
- Durée de l'exécution : 538.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s06

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s06_132023.json`
- Instance : bench_3 ; graine 6 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 136212 ; propagations 609155644 ; nodes non rapporté ; temps de résolution 310.4 s (non déterministe)
- Durée de l'exécution : 541.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s07

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s07_132030.json`
- Instance : bench_3 ; graine 7 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 138771 ; propagations 620902473 ; nodes non rapporté ; temps de résolution 312.6 s (non déterministe)
- Durée de l'exécution : 543.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s08

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s08_132046.json`
- Instance : bench_3 ; graine 8 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 54** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 128992 ; propagations 585994708 ; nodes non rapporté ; temps de résolution 291.5 s (non déterministe)
- Durée de l'exécution : 521.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s09

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s09_132051.json`
- Instance : bench_3 ; graine 9 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 71** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 131705 ; propagations 575324415 ; nodes non rapporté ; temps de résolution 290.0 s (non déterministe)
- Durée de l'exécution : 521.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:20 — bench3_pop54_s10

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s10_132057.json`
- Instance : bench_3 ; graine 10 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 53** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 145852 ; propagations 654458586 ; nodes non rapporté ; temps de résolution 325.8 s (non déterministe)
- Durée de l'exécution : 555.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s11

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s11_132100.json`
- Instance : bench_3 ; graine 11 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 134185 ; propagations 606832862 ; nodes non rapporté ; temps de résolution 309.8 s (non déterministe)
- Durée de l'exécution : 541.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s12

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s12_132106.json`
- Instance : bench_3 ; graine 12 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000043** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 138691 ; propagations 619529966 ; nodes non rapporté ; temps de résolution 315.8 s (non déterministe)
- Durée de l'exécution : 546.6 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s13

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s13_132113.json`
- Instance : bench_3 ; graine 13 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 58** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 132233 ; propagations 607902451 ; nodes non rapporté ; temps de résolution 305.4 s (non déterministe)
- Durée de l'exécution : 536.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s14

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s14_132117.json`
- Instance : bench_3 ; graine 14 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 152512 ; propagations 655071974 ; nodes non rapporté ; temps de résolution 324.7 s (non déterministe)
- Durée de l'exécution : 554.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s15

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s15_132131.json`
- Instance : bench_3 ; graine 15 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 60** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 140003 ; propagations 628669585 ; nodes non rapporté ; temps de résolution 323.1 s (non déterministe)
- Durée de l'exécution : 554.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s16

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s16_132149.json`
- Instance : bench_3 ; graine 16 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 50** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 127117 ; propagations 583357795 ; nodes non rapporté ; temps de résolution 299.2 s (non déterministe)
- Durée de l'exécution : 530.0 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s17

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s17_132152.json`
- Instance : bench_3 ; graine 17 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 137409 ; propagations 594067866 ; nodes non rapporté ; temps de résolution 300.8 s (non déterministe)
- Durée de l'exécution : 530.5 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:21 — bench3_pop54_s18

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s18_132153.json`
- Instance : bench_3 ; graine 18 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 122239 ; propagations 574848546 ; nodes non rapporté ; temps de résolution 292.7 s (non déterministe)
- Durée de l'exécution : 521.6 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:26 — bench3_pop54_s19

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s19_132631.json`
- Instance : bench_3 ; graine 19 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 53** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 145686 ; propagations 647283577 ; nodes non rapporté ; temps de résolution 322.4 s (non déterministe)
- Durée de l'exécution : 552.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:29 — bench3_pop54_s20

Comparaison population-generations sur bench_3 : population 54, 8 generations, NR=18, NM=18, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench3_population/bench3_pop54_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop54_s20_132902.json`
- Instance : bench_3 ; graine 20 ; population 54, NR = 18, NM = 18, 8 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000052** (faisable) ; 8 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 145183 ; propagations 654698915 ; nodes non rapporté ; temps de résolution 333.3 s (non déterministe)
- Durée de l'exécution : 563.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:02 — bench3_pop6_s00

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 0.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s00_130255.json`
- Instance : bench_3 ; graine 0 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 50177 ; propagations 224121174 ; nodes non rapporté ; temps de résolution 84.7 s (non déterministe)
- Durée de l'exécution : 265.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s01

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 1.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s01_130756.json`
- Instance : bench_3 ; graine 1 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 44** (faisable) ; 80 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 50098 ; propagations 224361531 ; nodes non rapporté ; temps de résolution 107.4 s (non déterministe)
- Durée de l'exécution : 345.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s02

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 2.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s02_130756.json`
- Instance : bench_3 ; graine 2 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 58403 ; propagations 247654248 ; nodes non rapporté ; temps de résolution 123.9 s (non déterministe)
- Durée de l'exécution : 365.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s03

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 3.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s03_130756.json`
- Instance : bench_3 ; graine 3 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 61618 ; propagations 257131509 ; nodes non rapporté ; temps de résolution 127.7 s (non déterministe)
- Durée de l'exécution : 366.5 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s04

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 4.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s04_130756.json`
- Instance : bench_3 ; graine 4 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 47** (faisable) ; 80 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 47286 ; propagations 204029712 ; nodes non rapporté ; temps de résolution 100.3 s (non déterministe)
- Durée de l'exécution : 338.0 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s05

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 5.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s05_130755.json`
- Instance : bench_3 ; graine 5 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 32** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 57745 ; propagations 253485567 ; nodes non rapporté ; temps de résolution 125.9 s (non déterministe)
- Durée de l'exécution : 366.1 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s06

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 6.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s06_130756.json`
- Instance : bench_3 ; graine 6 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 67421 ; propagations 286775143 ; nodes non rapporté ; temps de résolution 142.1 s (non déterministe)
- Durée de l'exécution : 382.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s07

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 7.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s07_130756.json`
- Instance : bench_3 ; graine 7 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000041** (faisable) ; 80 générations, 2 restart(s)
- **Effort cumulé du solveur** : 496 appels ; failures 50523 ; propagations 244969094 ; nodes non rapporté ; temps de résolution 115.6 s (non déterministe)
- Durée de l'exécution : 349.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s08

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 8.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s08_130755.json`
- Instance : bench_3 ; graine 8 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 44** (faisable) ; 80 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 65411 ; propagations 283090224 ; nodes non rapporté ; temps de résolution 137.9 s (non déterministe)
- Durée de l'exécution : 374.5 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s09

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 9.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s09_130755.json`
- Instance : bench_3 ; graine 9 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 80 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 51412 ; propagations 231914456 ; nodes non rapporté ; temps de résolution 115.6 s (non déterministe)
- Durée de l'exécution : 351.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s10

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 10.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s10_130756.json`
- Instance : bench_3 ; graine 10 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 80 générations, 3 restart(s)
- **Effort cumulé du solveur** : 501 appels ; failures 48952 ; propagations 193405834 ; nodes non rapporté ; temps de résolution 95.8 s (non déterministe)
- Durée de l'exécution : 330.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s11

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 11.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s11_130756.json`
- Instance : bench_3 ; graine 11 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 39** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 56397 ; propagations 246091082 ; nodes non rapporté ; temps de résolution 119.4 s (non déterministe)
- Durée de l'exécution : 360.2 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s12

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 12.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s12_130756.json`
- Instance : bench_3 ; graine 12 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27** (faisable) ; 80 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 61652 ; propagations 284446631 ; nodes non rapporté ; temps de résolution 140.4 s (non déterministe)
- Durée de l'exécution : 378.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s13

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 13.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s13_130756.json`
- Instance : bench_3 ; graine 13 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 31** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 67222 ; propagations 282272240 ; nodes non rapporté ; temps de résolution 140.7 s (non déterministe)
- Durée de l'exécution : 382.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s14

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 14.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s14_130756.json`
- Instance : bench_3 ; graine 14 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 66062 ; propagations 312742935 ; nodes non rapporté ; temps de résolution 150.3 s (non déterministe)
- Durée de l'exécution : 390.5 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s15

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 15.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s15_130756.json`
- Instance : bench_3 ; graine 15 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 80 générations, 3 restart(s)
- **Effort cumulé du solveur** : 501 appels ; failures 58966 ; propagations 273458681 ; nodes non rapporté ; temps de résolution 135.3 s (non déterministe)
- Durée de l'exécution : 370.8 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s16

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 16.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s16_130756.json`
- Instance : bench_3 ; graine 16 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 80 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 64727 ; propagations 281757953 ; nodes non rapporté ; temps de résolution 139.9 s (non déterministe)
- Durée de l'exécution : 379.3 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s17

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 17.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s17_130755.json`
- Instance : bench_3 ; graine 17 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 39** (faisable) ; 80 générations, 6 restart(s)
- **Effort cumulé du solveur** : 516 appels ; failures 83273 ; propagations 351388482 ; nodes non rapporté ; temps de résolution 175.1 s (non déterministe)
- Durée de l'exécution : 417.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s18

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 18.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s18_130756.json`
- Instance : bench_3 ; graine 18 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 53861 ; propagations 221154104 ; nodes non rapporté ; temps de résolution 111.2 s (non déterministe)
- Durée de l'exécution : 350.0 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s19

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 19.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s19_130756.json`
- Instance : bench_3 ; graine 19 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 31** (faisable) ; 80 générations, 5 restart(s)
- **Effort cumulé du solveur** : 511 appels ; failures 48036 ; propagations 230204564 ; nodes non rapporté ; temps de résolution 111.5 s (non déterministe)
- Durée de l'exécution : 352.9 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## 2026-11-26 13:07 — bench3_pop6_s20

Comparaison population-generations sur bench_3 : population 6, 80 generations, NR=2, NM=2, budget nominal 486, graine 20.

- Configuration : `experiments/config/bench3_population/bench3_pop6_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_pop6_s20_130756.json`
- Instance : bench_3 ; graine 20 ; population 6, NR = 2, NM = 2, 80 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 80 générations, 4 restart(s)
- **Effort cumulé du solveur** : 506 appels ; failures 53502 ; propagations 244785482 ; nodes non rapporté ; temps de résolution 127.5 s (non déterministe)
- Durée de l'exécution : 366.4 s ; commit `daaffa732dc66bc8a2273934aa47bdcc65b5d503`

## Synthese - Population et generations sur bench_3

- 84 executions : 4 configurations, 21 graines chacune.
- Budget nominal identique de 486 individus.
- Aucun optimum atteint (optimum documente : 16).
- Population 6 : meilleur cout observe (27), meilleur cout
  median et plus faible effort solveur.
- Population 18 : 21/21 solutions faisables sans violation
  quasi stricte.
- Population 18 conservee pour reproduire le protocole bench_2.
- Rapport : experiments/analysis/bench3_population.md.
- Script : experiments/analysis/analyze_bench3_population.py.

## 2026-11-26 14:53 — bench3_vois2_s00

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s00_145328.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1014261 ; propagations 4963802393 ; nodes non rapporté ; temps de résolution 1707.1 s (non déterministe)
- Durée de l'exécution : 1882.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s01

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s01_154613.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 26** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 771807 ; propagations 4790810919 ; nodes non rapporté ; temps de résolution 2028.7 s (non déterministe)
- Durée de l'exécution : 2272.8 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s02

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s02_154613.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 841367 ; propagations 5205349634 ; nodes non rapporté ; temps de résolution 2208.1 s (non déterministe)
- Durée de l'exécution : 2455.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s03

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s03_154613.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 970279 ; propagations 5083786456 ; nodes non rapporté ; temps de résolution 2316.9 s (non déterministe)
- Durée de l'exécution : 2563.5 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s04

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s04_154614.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 811936 ; propagations 4907078961 ; nodes non rapporté ; temps de résolution 2092.5 s (non déterministe)
- Durée de l'exécution : 2335.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s05

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s05_154613.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 785596 ; propagations 4723913615 ; nodes non rapporté ; temps de résolution 2026.7 s (non déterministe)
- Durée de l'exécution : 2271.5 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s06

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s06_154613.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 26** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 956961 ; propagations 4883848857 ; nodes non rapporté ; temps de résolution 2159.2 s (non déterministe)
- Durée de l'exécution : 2404.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s07

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s07_154613.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1207194 ; propagations 5200525589 ; nodes non rapporté ; temps de résolution 2420.6 s (non déterministe)
- Durée de l'exécution : 2667.8 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s08

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s08_154612.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 998251 ; propagations 4956757444 ; nodes non rapporté ; temps de résolution 2230.6 s (non déterministe)
- Durée de l'exécution : 2474.8 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s09

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s09_154614.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 24** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 824482 ; propagations 4592771974 ; nodes non rapporté ; temps de résolution 2048.9 s (non déterministe)
- Durée de l'exécution : 2292.2 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s10

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s10_154612.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 929490 ; propagations 4814061621 ; nodes non rapporté ; temps de résolution 2112.4 s (non déterministe)
- Durée de l'exécution : 2355.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s11

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s11_154613.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 17** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 949021 ; propagations 5039270667 ; nodes non rapporté ; temps de résolution 2230.4 s (non déterministe)
- Durée de l'exécution : 2476.8 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s12

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s12_154613.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 718154 ; propagations 4634635363 ; nodes non rapporté ; temps de résolution 1980.9 s (non déterministe)
- Durée de l'exécution : 2225.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s13

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s13_154613.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 26** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 928426 ; propagations 4948228123 ; nodes non rapporté ; temps de résolution 2217.1 s (non déterministe)
- Durée de l'exécution : 2462.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s14

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s14_154613.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 966978 ; propagations 5336511249 ; nodes non rapporté ; temps de résolution 2343.4 s (non déterministe)
- Durée de l'exécution : 2588.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s15

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s15_154614.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 925052 ; propagations 5077946333 ; nodes non rapporté ; temps de résolution 2250.0 s (non déterministe)
- Durée de l'exécution : 2496.2 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s16

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s16_154613.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 924119 ; propagations 5011956555 ; nodes non rapporté ; temps de résolution 2187.2 s (non déterministe)
- Durée de l'exécution : 2431.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s17

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s17_154613.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 823845 ; propagations 4729015651 ; nodes non rapporté ; temps de résolution 2075.0 s (non déterministe)
- Durée de l'exécution : 2320.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s18

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s18_154614.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 992365 ; propagations 5120661124 ; nodes non rapporté ; temps de résolution 2224.9 s (non déterministe)
- Durée de l'exécution : 2468.5 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s19

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s19_154613.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1007473 ; propagations 5323367612 ; nodes non rapporté ; temps de résolution 2409.0 s (non déterministe)
- Durée de l'exécution : 2657.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 15:46 — bench3_vois2_s20

Comparaison des tailles de voisinage sur bench_3 : voisinage 2, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois2_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_s20_154613.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 939830 ; propagations 5066323626 ; nodes non rapporté ; temps de résolution 2218.7 s (non déterministe)
- Durée de l'exécution : 2462.1 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 14:53 — bench3_vois3_s00

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s00_145328.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 6000060** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1171483 ; propagations 5296663497 ; nodes non rapporté ; temps de résolution 2125.1 s (non déterministe)
- Durée de l'exécution : 2305.1 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:23 — bench3_vois3_s01

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s01_162319.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 12000044** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1080380 ; propagations 5196091374 ; nodes non rapporté ; temps de résolution 2704.7 s (non déterministe)
- Durée de l'exécution : 2973.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:24 — bench3_vois3_s02

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s02_162406.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 11000080** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1172080 ; propagations 5385441583 ; nodes non rapporté ; temps de résolution 2829.4 s (non déterministe)
- Durée de l'exécution : 3096.7 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:24 — bench3_vois3_s03

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s03_162407.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000056** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1223308 ; propagations 5347239345 ; nodes non rapporté ; temps de résolution 2844.1 s (non déterministe)
- Durée de l'exécution : 3114.5 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:24 — bench3_vois3_s04

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s04_162427.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 8000073** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1374508 ; propagations 5012063663 ; nodes non rapporté ; temps de résolution 2974.4 s (non déterministe)
- Durée de l'exécution : 3241.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:24 — bench3_vois3_s05

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s05_162455.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 15000044** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1052023 ; propagations 5350461159 ; nodes non rapporté ; temps de résolution 2713.8 s (non déterministe)
- Durée de l'exécution : 2985.5 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:25 — bench3_vois3_s06

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s06_162511.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 11000056** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1269967 ; propagations 5110400455 ; nodes non rapporté ; temps de résolution 2894.0 s (non déterministe)
- Durée de l'exécution : 3163.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:25 — bench3_vois3_s07

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s07_162529.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 13000066** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1380541 ; propagations 5330446951 ; nodes non rapporté ; temps de résolution 3008.8 s (non déterministe)
- Durée de l'exécution : 3277.7 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:26 — bench3_vois3_s08

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s08_162619.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 12000057** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1461202 ; propagations 5085347626 ; nodes non rapporté ; temps de résolution 3090.6 s (non déterministe)
- Durée de l'exécution : 3358.7 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:26 — bench3_vois3_s09

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s09_162645.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20000075** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1145009 ; propagations 5522461316 ; nodes non rapporté ; temps de résolution 2780.7 s (non déterministe)
- Durée de l'exécution : 3051.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:27 — bench3_vois3_s10

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s10_162710.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000082** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1217022 ; propagations 5148535699 ; nodes non rapporté ; temps de résolution 2856.9 s (non déterministe)
- Durée de l'exécution : 3123.5 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:27 — bench3_vois3_s11

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s11_162716.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 17000076** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1244291 ; propagations 5467765615 ; nodes non rapporté ; temps de résolution 2874.0 s (non déterministe)
- Durée de l'exécution : 3139.3 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:27 — bench3_vois3_s12

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s12_162717.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 12000064** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1447956 ; propagations 5113228220 ; nodes non rapporté ; temps de résolution 3085.4 s (non déterministe)
- Durée de l'exécution : 3359.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:27 — bench3_vois3_s13

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s13_162723.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 15000055** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1445639 ; propagations 5140565987 ; nodes non rapporté ; temps de résolution 3118.2 s (non déterministe)
- Durée de l'exécution : 3389.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:27 — bench3_vois3_s14

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s14_162728.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21000052** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1244855 ; propagations 5321153039 ; nodes non rapporté ; temps de résolution 2902.2 s (non déterministe)
- Durée de l'exécution : 3172.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:27 — bench3_vois3_s15

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s15_162731.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 10000084** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1154638 ; propagations 5233771362 ; nodes non rapporté ; temps de résolution 2809.2 s (non déterministe)
- Durée de l'exécution : 3081.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:27 — bench3_vois3_s16

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s16_162751.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 7000056** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1210552 ; propagations 5288718397 ; nodes non rapporté ; temps de résolution 2873.1 s (non déterministe)
- Durée de l'exécution : 3142.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:28 — bench3_vois3_s17

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s17_162858.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000053** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1052485 ; propagations 5314593143 ; nodes non rapporté ; temps de résolution 2713.1 s (non déterministe)
- Durée de l'exécution : 2984.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:29 — bench3_vois3_s18

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s18_162923.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 16000077** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1242060 ; propagations 5178113222 ; nodes non rapporté ; temps de résolution 2908.6 s (non déterministe)
- Durée de l'exécution : 3179.5 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:30 — bench3_vois3_s19

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s19_163031.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 7000065** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1146452 ; propagations 4977780470 ; nodes non rapporté ; temps de résolution 2759.7 s (non déterministe)
- Durée de l'exécution : 3030.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 16:30 — bench3_vois3_s20

Comparaison des tailles de voisinage sur bench_3 : voisinage 3, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois3_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois3_s20_163042.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 13000061** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1257811 ; propagations 5145683537 ; nodes non rapporté ; temps de résolution 2865.9 s (non déterministe)
- Durée de l'exécution : 3139.3 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 14:53 — bench3_vois4_s00

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s00_145328.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 16000034** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1139210 ; propagations 3934452547 ; nodes non rapporté ; temps de résolution 2268.7 s (non déterministe)
- Durée de l'exécution : 2454.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:12 — bench3_vois4_s01

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s01_171254.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27000092** (infaisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 1346240 ; propagations 4232021718 ; nodes non rapporté ; temps de résolution 3434.7 s (non déterministe)
- Durée de l'exécution : 3728.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:14 — bench3_vois4_s02

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s02_171442.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 16000052** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1116765 ; propagations 4079687073 ; nodes non rapporté ; temps de résolution 3055.9 s (non déterministe)
- Durée de l'exécution : 3340.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:15 — bench3_vois4_s03

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s03_171544.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28000093** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1318949 ; propagations 3608482918 ; nodes non rapporté ; temps de résolution 3382.1 s (non déterministe)
- Durée de l'exécution : 3660.8 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:16 — bench3_vois4_s04

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s04_171603.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22000060** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1163069 ; propagations 3739560571 ; nodes non rapporté ; temps de résolution 3159.0 s (non déterministe)
- Durée de l'exécution : 3448.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:17 — bench3_vois4_s05

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s05_171737.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19000051** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1207438 ; propagations 4090149796 ; nodes non rapporté ; temps de résolution 3150.9 s (non déterministe)
- Durée de l'exécution : 3436.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:17 — bench3_vois4_s06

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s06_171755.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 26000047** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1272454 ; propagations 3864074883 ; nodes non rapporté ; temps de résolution 3238.0 s (non déterministe)
- Durée de l'exécution : 3517.1 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:18 — bench3_vois4_s07

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s07_171830.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20000068** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1504887 ; propagations 3980325589 ; nodes non rapporté ; temps de résolution 3565.0 s (non déterministe)
- Durée de l'exécution : 3835.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:18 — bench3_vois4_s08

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s08_171844.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 10000050** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1197211 ; propagations 4130933270 ; nodes non rapporté ; temps de résolution 3181.5 s (non déterministe)
- Durée de l'exécution : 3463.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:18 — bench3_vois4_s09

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s09_171854.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000044** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1362793 ; propagations 3965427186 ; nodes non rapporté ; temps de résolution 3352.2 s (non déterministe)
- Durée de l'exécution : 3629.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:19 — bench3_vois4_s10

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s10_171915.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19000079** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1131197 ; propagations 4063302091 ; nodes non rapporté ; temps de résolution 3067.3 s (non déterministe)
- Durée de l'exécution : 3354.3 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:19 — bench3_vois4_s11

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s11_171937.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21000052** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1114556 ; propagations 3637044622 ; nodes non rapporté ; temps de résolution 3012.9 s (non déterministe)
- Durée de l'exécution : 3298.8 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:20 — bench3_vois4_s12

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s12_172007.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 17000048** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1489674 ; propagations 3393622388 ; nodes non rapporté ; temps de résolution 3442.7 s (non déterministe)
- Durée de l'exécution : 3713.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:20 — bench3_vois4_s13

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s13_172015.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 17000051** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1145381 ; propagations 4180098716 ; nodes non rapporté ; temps de résolution 3099.5 s (non déterministe)
- Durée de l'exécution : 3384.2 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:20 — bench3_vois4_s14

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s14_172023.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000058** (infaisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 1299153 ; propagations 4189295186 ; nodes non rapporté ; temps de résolution 3321.0 s (non déterministe)
- Durée de l'exécution : 3605.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:21 — bench3_vois4_s15

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s15_172102.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37000079** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1946784 ; propagations 3695404064 ; nodes non rapporté ; temps de résolution 4036.9 s (non déterministe)
- Durée de l'exécution : 4296.1 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:22 — bench3_vois4_s16

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s16_172219.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20000060** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1271730 ; propagations 3839634575 ; nodes non rapporté ; temps de résolution 3194.5 s (non déterministe)
- Durée de l'exécution : 3473.7 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:22 — bench3_vois4_s17

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s17_172224.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23000055** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1167489 ; propagations 3673595462 ; nodes non rapporté ; temps de résolution 3126.4 s (non déterministe)
- Durée de l'exécution : 3402.0 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:23 — bench3_vois4_s18

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s18_172303.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 15000061** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1085844 ; propagations 4251215860 ; nodes non rapporté ; temps de résolution 3009.5 s (non déterministe)
- Durée de l'exécution : 3290.4 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:23 — bench3_vois4_s19

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s19_172317.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20000079** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1235750 ; propagations 3714680641 ; nodes non rapporté ; temps de résolution 3147.1 s (non déterministe)
- Durée de l'exécution : 3423.9 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## 2026-11-26 17:23 — bench3_vois4_s20

Comparaison des tailles de voisinage sur bench_3 : voisinage 4, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_voisinage/bench3_vois4_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois4_s20_172354.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000049** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 988662 ; propagations 4231387734 ; nodes non rapporté ; temps de résolution 2873.7 s (non déterministe)
- Durée de l'exécution : 3157.6 s ; commit `ab977345a09a06a59be7d7ecd20be8b84f010672`

## Synthese - Taille du voisinage sur bench_3

- 63 nouvelles executions et 21 references reutilisees.
- Aucun optimum atteint (optimum documente : 16).
- Voisinage 2 : meilleur cout moyen (23.1429) et minimum (17).
- Reduction du cout moyen de 43.95 % par rapport au voisinage 1.
- Voisinage 2 : environ 14.7 fois plus de propagations.
- Voisinages 3 et 4 : forte degradation de la faisabilite.
- Voisinage 1 conserve pour reproduire le protocole bench_2.
- Rapport : experiments/analysis/bench3_voisinage.md.
- Script : experiments/analysis/analyze_bench3_neighborhood.py.

## 2026-11-26 19:05 — bench3_stag15_s00

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s00_190506.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 73438 ; propagations 325403676 ; nodes non rapporté ; temps de résolution 168.1 s (non déterministe)
- Durée de l'exécution : 403.5 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:05 — bench3_stag15_s01

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s01_190515.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 44420 ; propagations 192093915 ; nodes non rapporté ; temps de résolution 96.5 s (non déterministe)
- Durée de l'exécution : 327.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:05 — bench3_stag15_s02

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s02_190516.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 61738 ; propagations 275871246 ; nodes non rapporté ; temps de résolution 138.2 s (non déterministe)
- Durée de l'exécution : 376.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:05 — bench3_stag15_s03

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s03_190538.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 56182 ; propagations 255380403 ; nodes non rapporté ; temps de résolution 129.1 s (non déterministe)
- Durée de l'exécution : 364.5 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:05 — bench3_stag15_s04

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s04_190550.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 112570 ; propagations 467527220 ; nodes non rapporté ; temps de résolution 235.7 s (non déterministe)
- Durée de l'exécution : 484.3 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:05 — bench3_stag15_s05

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s05_190553.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 48817 ; propagations 234309898 ; nodes non rapporté ; temps de résolution 114.5 s (non déterministe)
- Durée de l'exécution : 349.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:06 — bench3_stag15_s06

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s06_190623.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 67151 ; propagations 319410608 ; nodes non rapporté ; temps de résolution 159.5 s (non déterministe)
- Durée de l'exécution : 394.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:06 — bench3_stag15_s07

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s07_190626.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 52** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63965 ; propagations 281508326 ; nodes non rapporté ; temps de résolution 140.4 s (non déterministe)
- Durée de l'exécution : 375.8 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:06 — bench3_stag15_s08

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s08_190633.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 67955 ; propagations 302375771 ; nodes non rapporté ; temps de résolution 147.3 s (non déterministe)
- Durée de l'exécution : 384.8 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:06 — bench3_stag15_s09

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s09_190644.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 71746 ; propagations 298970724 ; nodes non rapporté ; temps de résolution 144.7 s (non déterministe)
- Durée de l'exécution : 380.1 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:07 — bench3_stag15_s10

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s10_190704.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 33** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52330 ; propagations 236122936 ; nodes non rapporté ; temps de résolution 120.4 s (non déterministe)
- Durée de l'exécution : 355.5 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:07 — bench3_stag15_s11

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s11_190710.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 60757 ; propagations 276710927 ; nodes non rapporté ; temps de résolution 138.1 s (non déterministe)
- Durée de l'exécution : 371.8 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:07 — bench3_stag15_s12

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s12_190731.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 85110 ; propagations 398299027 ; nodes non rapporté ; temps de résolution 197.2 s (non déterministe)
- Durée de l'exécution : 424.8 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:07 — bench3_stag15_s13

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s13_190735.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 80053 ; propagations 354884380 ; nodes non rapporté ; temps de résolution 178.3 s (non déterministe)
- Durée de l'exécution : 412.2 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:07 — bench3_stag15_s14

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s14_190744.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 88** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 87399 ; propagations 399283246 ; nodes non rapporté ; temps de résolution 197.7 s (non déterministe)
- Durée de l'exécution : 423.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:07 — bench3_stag15_s15

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s15_190751.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52734 ; propagations 228761563 ; nodes non rapporté ; temps de résolution 115.5 s (non déterministe)
- Durée de l'exécution : 348.9 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:08 — bench3_stag15_s16

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s16_190811.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 94417 ; propagations 429995934 ; nodes non rapporté ; temps de résolution 208.5 s (non déterministe)
- Durée de l'exécution : 431.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:08 — bench3_stag15_s17

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s17_190830.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 49617 ; propagations 222101256 ; nodes non rapporté ; temps de résolution 112.7 s (non déterministe)
- Durée de l'exécution : 341.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:10 — bench3_stag15_s18

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s18_191044.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 49380 ; propagations 227795908 ; nodes non rapporté ; temps de résolution 105.0 s (non déterministe)
- Durée de l'exécution : 309.2 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:11 — bench3_stag15_s19

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s19_191134.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69485 ; propagations 297197700 ; nodes non rapporté ; temps de résolution 131.7 s (non déterministe)
- Durée de l'exécution : 325.1 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:11 — bench3_stag15_s20

Comparaison des seuils de stagnation sur bench_3 : stagnation 15, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag15_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag15_s20_191143.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 92471 ; propagations 432050119 ; nodes non rapporté ; temps de résolution 188.6 s (non déterministe)
- Durée de l'exécution : 378.8 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s00

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s00_184926.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 114722 ; propagations 519922835 ; nodes non rapporté ; temps de résolution 267.9 s (non déterministe)
- Durée de l'exécution : 513.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s01

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s01_184926.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 150732 ; propagations 657991716 ; nodes non rapporté ; temps de résolution 339.9 s (non déterministe)
- Durée de l'exécution : 609.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s02

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s02_184926.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 145342 ; propagations 645834742 ; nodes non rapporté ; temps de résolution 327.8 s (non déterministe)
- Durée de l'exécution : 590.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s03

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s03_184926.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 107710 ; propagations 486124039 ; nodes non rapporté ; temps de résolution 245.5 s (non déterministe)
- Durée de l'exécution : 499.3 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s04

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s04_184926.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 170514 ; propagations 720383435 ; nodes non rapporté ; temps de résolution 365.4 s (non déterministe)
- Durée de l'exécution : 626.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s05

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s05_184926.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 122993 ; propagations 559716590 ; nodes non rapporté ; temps de résolution 278.0 s (non déterministe)
- Durée de l'exécution : 530.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s06

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s06_184926.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 113466 ; propagations 534867002 ; nodes non rapporté ; temps de résolution 268.5 s (non déterministe)
- Durée de l'exécution : 514.5 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s07

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s07_184926.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 52** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 121780 ; propagations 511339034 ; nodes non rapporté ; temps de résolution 258.8 s (non déterministe)
- Durée de l'exécution : 505.2 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s08

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s08_184926.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 155467 ; propagations 686958218 ; nodes non rapporté ; temps de résolution 346.9 s (non déterministe)
- Durée de l'exécution : 609.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s09

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s09_184926.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 107088 ; propagations 458082943 ; nodes non rapporté ; temps de résolution 226.2 s (non déterministe)
- Durée de l'exécution : 470.9 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s10

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s10_184926.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 132256 ; propagations 579036790 ; nodes non rapporté ; temps de résolution 293.0 s (non déterministe)
- Durée de l'exécution : 546.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s11

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s11_184926.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 148141 ; propagations 641810946 ; nodes non rapporté ; temps de résolution 321.4 s (non déterministe)
- Durée de l'exécution : 582.0 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s12

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s12_184926.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 123131 ; propagations 564621476 ; nodes non rapporté ; temps de résolution 281.4 s (non déterministe)
- Durée de l'exécution : 535.1 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s13

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s13_184926.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 133292 ; propagations 587586863 ; nodes non rapporté ; temps de résolution 298.5 s (non déterministe)
- Durée de l'exécution : 552.8 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s14

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s14_184925.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 88** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 108844 ; propagations 493212714 ; nodes non rapporté ; temps de résolution 249.9 s (non déterministe)
- Durée de l'exécution : 489.9 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s15

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s15_184926.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 125707 ; propagations 542060760 ; nodes non rapporté ; temps de résolution 274.7 s (non déterministe)
- Durée de l'exécution : 527.2 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s16

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s16_184925.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 138401 ; propagations 632772954 ; nodes non rapporté ; temps de résolution 317.1 s (non déterministe)
- Durée de l'exécution : 570.2 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s17

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s17_184925.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 96087 ; propagations 428140381 ; nodes non rapporté ; temps de résolution 217.1 s (non déterministe)
- Durée de l'exécution : 462.0 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s18

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s18_184926.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 118441 ; propagations 537460942 ; nodes non rapporté ; temps de résolution 264.0 s (non déterministe)
- Durée de l'exécution : 517.1 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:49 — bench3_stag3_s19

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s19_184926.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 4 restart(s)
- **Effort cumulé du solveur** : 554 appels ; failures 142769 ; propagations 617286972 ; nodes non rapporté ; temps de résolution 310.1 s (non déterministe)
- Durée de l'exécution : 571.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:57 — bench3_stag3_s20

Comparaison des seuils de stagnation sur bench_3 : stagnation 3, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag3_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag3_s20_185709.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 47** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 134397 ; propagations 579662031 ; nodes non rapporté ; temps de résolution 296.1 s (non déterministe)
- Durée de l'exécution : 556.5 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:57 — bench3_stag5_s00

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s00_185718.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 95663 ; propagations 432032160 ; nodes non rapporté ; temps de résolution 222.9 s (non déterministe)
- Durée de l'exécution : 466.9 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:57 — bench3_stag5_s01

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s01_185736.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 39** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 96735 ; propagations 399321057 ; nodes non rapporté ; temps de résolution 207.6 s (non déterministe)
- Durée de l'exécution : 458.3 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:57 — bench3_stag5_s02

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s02_185746.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 78780 ; propagations 345922746 ; nodes non rapporté ; temps de résolution 173.2 s (non déterministe)
- Durée de l'exécution : 416.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:57 — bench3_stag5_s03

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s03_185753.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 111737 ; propagations 509372806 ; nodes non rapporté ; temps de résolution 258.1 s (non déterministe)
- Durée de l'exécution : 509.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s04

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s04_185800.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 151486 ; propagations 637618484 ; nodes non rapporté ; temps de résolution 329.7 s (non déterministe)
- Durée de l'exécution : 590.0 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s05

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s05_185801.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 98465 ; propagations 438230946 ; nodes non rapporté ; temps de résolution 219.0 s (non déterministe)
- Durée de l'exécution : 470.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s06

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s06_185804.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 94317 ; propagations 435649902 ; nodes non rapporté ; temps de résolution 221.2 s (non déterministe)
- Durée de l'exécution : 464.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s07

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s07_185815.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 52** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 80033 ; propagations 342852309 ; nodes non rapporté ; temps de résolution 173.6 s (non déterministe)
- Durée de l'exécution : 419.0 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s08

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s08_185818.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 67955 ; propagations 302375771 ; nodes non rapporté ; temps de résolution 149.3 s (non déterministe)
- Durée de l'exécution : 387.2 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s09

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s09_185822.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 89200 ; propagations 379214600 ; nodes non rapporté ; temps de résolution 190.1 s (non déterministe)
- Durée de l'exécution : 434.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s10

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s10_185833.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 105094 ; propagations 461158689 ; nodes non rapporté ; temps de résolution 236.7 s (non déterministe)
- Durée de l'exécution : 489.7 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s11

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s11_185840.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 51** (faisable) ; 26 générations, 3 restart(s)
- **Effort cumulé du solveur** : 537 appels ; failures 136145 ; propagations 607480416 ; nodes non rapporté ; temps de résolution 308.8 s (non déterministe)
- Durée de l'exécution : 569.9 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s12

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s12_185857.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 116388 ; propagations 536837978 ; nodes non rapporté ; temps de résolution 267.5 s (non déterministe)
- Durée de l'exécution : 517.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:58 — bench3_stag5_s13

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s13_185858.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 117256 ; propagations 515756431 ; nodes non rapporté ; temps de résolution 260.7 s (non déterministe)
- Durée de l'exécution : 511.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:59 — bench3_stag5_s14

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s14_185909.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 88** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 98755 ; propagations 447793022 ; nodes non rapporté ; temps de résolution 229.4 s (non déterministe)
- Durée de l'exécution : 473.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:59 — bench3_stag5_s15

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s15_185918.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 103198 ; propagations 435767142 ; nodes non rapporté ; temps de résolution 219.8 s (non déterministe)
- Durée de l'exécution : 470.6 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:59 — bench3_stag5_s16

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s16_185937.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 121930 ; propagations 553222119 ; nodes non rapporté ; temps de résolution 281.9 s (non déterministe)
- Durée de l'exécution : 532.5 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:59 — bench3_stag5_s17

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s17_185937.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 75603 ; propagations 338748926 ; nodes non rapporté ; temps de résolution 172.0 s (non déterministe)
- Durée de l'exécution : 414.5 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 18:59 — bench3_stag5_s18

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s18_185954.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 98899 ; propagations 432869807 ; nodes non rapporté ; temps de résolution 216.7 s (non déterministe)
- Durée de l'exécution : 469.1 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:04 — bench3_stag5_s19

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s19_190444.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 2 restart(s)
- **Effort cumulé du solveur** : 520 appels ; failures 119198 ; propagations 521662189 ; nodes non rapporté ; temps de résolution 267.9 s (non déterministe)
- Durée de l'exécution : 521.3 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## 2026-11-26 19:04 — bench3_stag5_s20

Comparaison des seuils de stagnation sur bench_3 : stagnation 5, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_stagnation/bench3_stag5_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_stag5_s20_190446.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 105099 ; propagations 475029604 ; nodes non rapporté ; temps de résolution 240.8 s (non déterministe)
- Durée de l'exécution : 482.4 s ; commit `f9376a7dbd6984b86138e4e045ca102d1a2bb52f`

## Synthese - Seuil de stagnation sur bench_3

- 63 nouvelles executions et 21 references reutilisees.
- Toutes les solutions finales sont faisables et sans violation quasi stricte.
- Aucun optimum atteint (optimum documente : 16).
- Seuil 10 : meilleur cout moyen (41.2857).
- Seuil 15 : effort solveur minimal.
- Seuil 3 : 68.7 % plus de propagations que le seuil 10.
- Les redemarrages frequents ne procurent pas de gain observable.
- Seuil 10 conserve comme reference.
- Rapport : experiments/analysis/bench3_stagnation.md.
- Script : experiments/analysis/analyze_bench3_stagnation.py.

## 2026-11-26 19:33 — bench3_dt10_s00

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s00_193344.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 73438 ; propagations 325403676 ; nodes non rapporté ; temps de résolution 171.9 s (non déterministe)
- Durée de l'exécution : 415.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:33 — bench3_dt10_s01

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s01_193346.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 44420 ; propagations 192093915 ; nodes non rapporté ; temps de résolution 99.2 s (non déterministe)
- Durée de l'exécution : 342.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:33 — bench3_dt10_s02

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s02_193351.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 61738 ; propagations 275871246 ; nodes non rapporté ; temps de résolution 139.9 s (non déterministe)
- Durée de l'exécution : 384.5 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:33 — bench3_dt10_s03

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s03_193352.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 80075 ; propagations 364838837 ; nodes non rapporté ; temps de résolution 189.4 s (non déterministe)
- Durée de l'exécution : 441.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:33 — bench3_dt10_s04

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s04_193352.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 112814 ; propagations 493630359 ; nodes non rapporté ; temps de résolution 249.6 s (non déterministe)
- Durée de l'exécution : 498.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:34 — bench3_dt10_s05

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s05_193403.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 69460 ; propagations 318486737 ; nodes non rapporté ; temps de résolution 161.6 s (non déterministe)
- Durée de l'exécution : 412.7 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:34 — bench3_dt10_s06

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s06_193413.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 76704 ; propagations 356005195 ; nodes non rapporté ; temps de résolution 181.1 s (non déterministe)
- Durée de l'exécution : 431.3 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:34 — bench3_dt10_s07

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s07_193417.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 52** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63965 ; propagations 281508326 ; nodes non rapporté ; temps de résolution 143.4 s (non déterministe)
- Durée de l'exécution : 386.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:34 — bench3_dt10_s08

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s08_193428.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 68874 ; propagations 306984797 ; nodes non rapporté ; temps de résolution 153.4 s (non déterministe)
- Durée de l'exécution : 396.5 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:34 — bench3_dt10_s09

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s09_193444.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 71746 ; propagations 298970724 ; nodes non rapporté ; temps de résolution 148.6 s (non déterministe)
- Durée de l'exécution : 390.9 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:34 — bench3_dt10_s10

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s10_193451.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 33** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52330 ; propagations 236122936 ; nodes non rapporté ; temps de résolution 122.6 s (non déterministe)
- Durée de l'exécution : 364.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:35 — bench3_dt10_s11

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s11_193505.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 77860 ; propagations 351567128 ; nodes non rapporté ; temps de résolution 175.8 s (non déterministe)
- Durée de l'exécution : 422.7 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:35 — bench3_dt10_s12

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s12_193519.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000033** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 91362 ; propagations 453155038 ; nodes non rapporté ; temps de résolution 214.1 s (non déterministe)
- Durée de l'exécution : 458.9 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:35 — bench3_dt10_s13

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s13_193523.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 98947 ; propagations 435310094 ; nodes non rapporté ; temps de résolution 217.7 s (non déterministe)
- Durée de l'exécution : 462.8 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:35 — bench3_dt10_s14

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s14_193531.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 88** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 87399 ; propagations 399283246 ; nodes non rapporté ; temps de résolution 202.8 s (non déterministe)
- Durée de l'exécution : 438.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:35 — bench3_dt10_s15

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s15_193534.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 75211 ; propagations 329094570 ; nodes non rapporté ; temps de résolution 163.9 s (non déterministe)
- Durée de l'exécution : 410.7 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:35 — bench3_dt10_s16

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s16_193543.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 94417 ; propagations 429995934 ; nodes non rapporté ; temps de résolution 215.3 s (non déterministe)
- Durée de l'exécution : 446.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:35 — bench3_dt10_s17

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s17_193546.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 58269 ; propagations 259728250 ; nodes non rapporté ; temps de résolution 132.8 s (non déterministe)
- Durée de l'exécution : 378.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:39 — bench3_dt10_s18

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s18_193930.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 72584 ; propagations 326350251 ; nodes non rapporté ; temps de résolution 142.9 s (non déterministe)
- Durée de l'exécution : 348.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:39 — bench3_dt10_s19

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s19_193938.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69485 ; propagations 297197700 ; nodes non rapporté ; temps de résolution 134.4 s (non déterministe)
- Durée de l'exécution : 329.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:40 — bench3_dt10_s20

Comparaison des budgets deterministes sur bench_3 : budget 10.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt10_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt10_s20_194017.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 92471 ; propagations 432050119 ; nodes non rapporté ; temps de résolution 185.3 s (non déterministe)
- Durée de l'exécution : 372.8 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s00

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s00_192057.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 63274 ; propagations 289236349 ; nodes non rapporté ; temps de résolution 146.9 s (non déterministe)
- Durée de l'exécution : 399.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s01

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s01_192057.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 32** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 60151 ; propagations 295739071 ; nodes non rapporté ; temps de résolution 149.1 s (non déterministe)
- Durée de l'exécution : 392.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s02

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s02_192057.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 60992 ; propagations 284110194 ; nodes non rapporté ; temps de résolution 145.2 s (non déterministe)
- Durée de l'exécution : 395.8 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s03

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s03_192057.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52622 ; propagations 242818803 ; nodes non rapporté ; temps de résolution 123.4 s (non déterministe)
- Durée de l'exécution : 364.7 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s04

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s04_192057.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63891 ; propagations 289756932 ; nodes non rapporté ; temps de résolution 145.8 s (non déterministe)
- Durée de l'exécution : 389.9 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s05

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s05_192057.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000038** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 61285 ; propagations 303953731 ; nodes non rapporté ; temps de résolution 151.4 s (non déterministe)
- Durée de l'exécution : 402.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s06

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s06_192057.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 57744 ; propagations 288184350 ; nodes non rapporté ; temps de résolution 142.2 s (non déterministe)
- Durée de l'exécution : 385.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s07

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s07_192057.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 70669 ; propagations 334023524 ; nodes non rapporté ; temps de résolution 167.8 s (non déterministe)
- Durée de l'exécution : 413.1 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s08

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s08_192056.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 47** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 59354 ; propagations 293870044 ; nodes non rapporté ; temps de résolution 146.7 s (non déterministe)
- Durée de l'exécution : 389.7 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s09

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s09_192057.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 69458 ; propagations 301069697 ; nodes non rapporté ; temps de résolution 153.3 s (non déterministe)
- Durée de l'exécution : 404.5 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s10

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s10_192057.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 58241 ; propagations 282116809 ; nodes non rapporté ; temps de résolution 141.1 s (non déterministe)
- Durée de l'exécution : 385.1 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s11

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s11_192056.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 62894 ; propagations 276094428 ; nodes non rapporté ; temps de résolution 137.6 s (non déterministe)
- Durée de l'exécution : 389.9 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s12

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s12_192057.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 73409 ; propagations 346353330 ; nodes non rapporté ; temps de résolution 178.4 s (non déterministe)
- Durée de l'exécution : 429.3 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s13

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s13_192057.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 74214 ; propagations 332982406 ; nodes non rapporté ; temps de résolution 169.0 s (non déterministe)
- Durée de l'exécution : 412.5 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s14

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s14_192057.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 68805 ; propagations 315839426 ; nodes non rapporté ; temps de résolution 153.9 s (non déterministe)
- Durée de l'exécution : 397.3 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s15

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s15_192056.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 70063 ; propagations 333146932 ; nodes non rapporté ; temps de résolution 166.0 s (non déterministe)
- Durée de l'exécution : 418.9 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s16

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s16_192056.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 64147 ; propagations 284062434 ; nodes non rapporté ; temps de résolution 147.2 s (non déterministe)
- Durée de l'exécution : 389.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s17

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s17_192056.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 31** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 50421 ; propagations 249702895 ; nodes non rapporté ; temps de résolution 127.3 s (non déterministe)
- Durée de l'exécution : 370.5 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s18

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s18_192057.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 66779 ; propagations 308509446 ; nodes non rapporté ; temps de résolution 155.2 s (non déterministe)
- Durée de l'exécution : 406.2 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:20 — bench3_dt1_s19

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s19_192057.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 26** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 90436 ; propagations 417158284 ; nodes non rapporté ; temps de résolution 209.1 s (non déterministe)
- Durée de l'exécution : 460.9 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt1_s20

Comparaison des budgets deterministes sur bench_3 : budget 1.0, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt1_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt1_s20_192702.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000036** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69061 ; propagations 321078398 ; nodes non rapporté ; temps de résolution 160.4 s (non déterministe)
- Durée de l'exécution : 402.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s00

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s00_192708.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 70312 ; propagations 317635583 ; nodes non rapporté ; temps de résolution 162.5 s (non déterministe)
- Durée de l'exécution : 402.4 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s01

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s01_192723.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 44420 ; propagations 192093915 ; nodes non rapporté ; temps de résolution 98.6 s (non déterministe)
- Durée de l'exécution : 337.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s02

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s02_192723.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 61738 ; propagations 275871246 ; nodes non rapporté ; temps de résolution 138.3 s (non déterministe)
- Durée de l'exécution : 379.3 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s03

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s03_192726.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 79581 ; propagations 363254103 ; nodes non rapporté ; temps de résolution 187.4 s (non déterministe)
- Durée de l'exécution : 436.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s04

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s04_192727.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 32** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 110237 ; propagations 475731449 ; nodes non rapporté ; temps de résolution 242.5 s (non déterministe)
- Durée de l'exécution : 494.2 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s05

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s05_192727.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 69460 ; propagations 318486737 ; nodes non rapporté ; temps de résolution 161.8 s (non déterministe)
- Durée de l'exécution : 408.3 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s06

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s06_192728.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000030** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 56919 ; propagations 282421733 ; nodes non rapporté ; temps de résolution 141.2 s (non déterministe)
- Durée de l'exécution : 382.2 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s07

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s07_192731.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 52** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 62348 ; propagations 275878741 ; nodes non rapporté ; temps de résolution 138.4 s (non déterministe)
- Durée de l'exécution : 378.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s08

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s08_192734.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 67440 ; propagations 296690743 ; nodes non rapporté ; temps de résolution 147.4 s (non déterministe)
- Durée de l'exécution : 388.3 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s09

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s09_192736.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 91333 ; propagations 385673852 ; nodes non rapporté ; temps de résolution 199.2 s (non déterministe)
- Durée de l'exécution : 448.1 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s10

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s10_192738.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 33** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52330 ; propagations 236122936 ; nodes non rapporté ; temps de résolution 121.2 s (non déterministe)
- Durée de l'exécution : 360.2 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s11

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s11_192741.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63076 ; propagations 300708045 ; nodes non rapporté ; temps de résolution 149.9 s (non déterministe)
- Durée de l'exécution : 391.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s12

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s12_192743.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 47** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 94265 ; propagations 435572106 ; nodes non rapporté ; temps de résolution 218.4 s (non déterministe)
- Durée de l'exécution : 469.5 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s13

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s13_192745.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 98913 ; propagations 435194058 ; nodes non rapporté ; temps de résolution 228.1 s (non déterministe)
- Durée de l'exécution : 480.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s14

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s14_192751.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 88** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 87399 ; propagations 399283246 ; nodes non rapporté ; temps de résolution 208.1 s (non déterministe)
- Durée de l'exécution : 451.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s15

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s15_192751.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 75211 ; propagations 329094570 ; nodes non rapporté ; temps de résolution 167.4 s (non déterministe)
- Durée de l'exécution : 418.5 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:27 — bench3_dt2p5_s16

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s16_192756.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 81372 ; propagations 374169815 ; nodes non rapporté ; temps de résolution 189.4 s (non déterministe)
- Durée de l'exécution : 441.0 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:28 — bench3_dt2p5_s17

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s17_192808.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 57190 ; propagations 256034022 ; nodes non rapporté ; temps de résolution 131.4 s (non déterministe)
- Durée de l'exécution : 379.7 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:28 — bench3_dt2p5_s18

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s18_192839.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 71835 ; propagations 324568650 ; nodes non rapporté ; temps de résolution 161.9 s (non déterministe)
- Durée de l'exécution : 410.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:33 — bench3_dt2p5_s19

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s19_193301.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69485 ; propagations 297197700 ; nodes non rapporté ; temps de résolution 151.9 s (non déterministe)
- Durée de l'exécution : 395.6 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## 2026-11-26 19:33 — bench3_dt2p5_s20

Comparaison des budgets deterministes sur bench_3 : budget 2.5, voisinage 1, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_deterministic_time/bench3_dt2p5_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_dt2p5_s20_193339.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69854 ; propagations 320078029 ; nodes non rapporté ; temps de résolution 168.7 s (non déterministe)
- Durée de l'exécution : 411.3 s ; commit `16daf977ef0070f6a48d5394ac76696727f710fb`

## Synthese - Budget deterministe sur bench_3

- 63 nouvelles executions et 21 references reutilisees.
- Aucun optimum atteint (optimum documente : 16).
- Toutes les solutions finales sont faisables.
- Budget 5 : seul budget sans violation quasi stricte pour les 21 graines.
- Budget 1 : environ 10 % moins de propagations que le budget 5.
- Contrairement a bench_2, les budgets ne sont pas equivalents.
- Les differences par graine diminuent lorsque le budget augmente.
- Budget 5 conserve comme reference pour le voisinage 1.
- Rapport : experiments/analysis/bench3_deterministic_time.md.
- Script : experiments/analysis/analyze_bench3_deterministic_time.py.
- Comparaison par graine : experiments/analysis/compare_bench3_deterministic_time.py.

## 2026-11-26 20:46 — bench3_vois2_dt10_s00

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s00_204601.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1268490 ; propagations 8405530317 ; nodes non rapporté ; temps de résolution 3662.6 s (non déterministe)
- Durée de l'exécution : 3919.8 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:46 — bench3_vois2_dt10_s01

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s01_204632.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 1197562 ; propagations 8826409148 ; nodes non rapporté ; temps de résolution 3790.5 s (non déterministe)
- Durée de l'exécution : 4053.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s02

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s02_204708.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1213771 ; propagations 8032471587 ; nodes non rapporté ; temps de résolution 3558.3 s (non déterministe)
- Durée de l'exécution : 3811.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s03

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s03_204710.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 26** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1430636 ; propagations 8404576130 ; nodes non rapporté ; temps de résolution 3743.6 s (non déterministe)
- Durée de l'exécution : 3994.8 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s04

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s04_204719.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1240449 ; propagations 8329532634 ; nodes non rapporté ; temps de résolution 3608.0 s (non déterministe)
- Durée de l'exécution : 3861.4 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s05

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s05_204724.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 18** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1148425 ; propagations 7744386127 ; nodes non rapporté ; temps de résolution 3444.4 s (non déterministe)
- Durée de l'exécution : 3702.3 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s06

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s06_204726.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1347113 ; propagations 7591435430 ; nodes non rapporté ; temps de résolution 3493.5 s (non déterministe)
- Durée de l'exécution : 3748.2 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s07

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s07_204729.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1337058 ; propagations 7809865966 ; nodes non rapporté ; temps de résolution 3605.1 s (non déterministe)
- Durée de l'exécution : 3856.5 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s08

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s08_204736.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1114434 ; propagations 7761069096 ; nodes non rapporté ; temps de résolution 3394.2 s (non déterministe)
- Durée de l'exécution : 3649.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s09

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s09_204738.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1221399 ; propagations 7707163792 ; nodes non rapporté ; temps de résolution 3533.5 s (non déterministe)
- Durée de l'exécution : 3787.5 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s10

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s10_204738.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 17** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1227836 ; propagations 7961911657 ; nodes non rapporté ; temps de résolution 3530.1 s (non déterministe)
- Durée de l'exécution : 3784.1 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s11

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s11_204745.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1136651 ; propagations 8162247896 ; nodes non rapporté ; temps de résolution 3616.5 s (non déterministe)
- Durée de l'exécution : 3871.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:47 — bench3_vois2_dt10_s12

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s12_204757.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1110733 ; propagations 7981040876 ; nodes non rapporté ; temps de résolution 3430.1 s (non déterministe)
- Durée de l'exécution : 3686.2 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:48 — bench3_vois2_dt10_s13

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s13_204818.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1276441 ; propagations 8076757752 ; nodes non rapporté ; temps de résolution 3653.0 s (non déterministe)
- Durée de l'exécution : 3907.0 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:48 — bench3_vois2_dt10_s14

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s14_204848.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1497019 ; propagations 8888615061 ; nodes non rapporté ; temps de résolution 3877.5 s (non déterministe)
- Durée de l'exécution : 4125.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:49 — bench3_vois2_dt10_s15

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s15_204904.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1225986 ; propagations 8157126836 ; nodes non rapporté ; temps de résolution 3578.4 s (non déterministe)
- Durée de l'exécution : 3830.3 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:49 — bench3_vois2_dt10_s16

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s16_204940.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 18** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1271988 ; propagations 8783798146 ; nodes non rapporté ; temps de résolution 3727.2 s (non déterministe)
- Durée de l'exécution : 3974.0 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:50 — bench3_vois2_dt10_s17

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s17_205040.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 1382978 ; propagations 8882785919 ; nodes non rapporté ; temps de résolution 3938.0 s (non déterministe)
- Durée de l'exécution : 4194.3 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 21:03 — bench3_vois2_dt10_s18

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s18_210322.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 17** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1456890 ; propagations 8317241728 ; nodes non rapporté ; temps de résolution 3606.0 s (non déterministe)
- Durée de l'exécution : 3835.4 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 21:11 — bench3_vois2_dt10_s19

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s19_211154.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1240008 ; propagations 8606610265 ; nodes non rapporté ; temps de résolution 3380.6 s (non déterministe)
- Durée de l'exécution : 3601.6 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 21:48 — bench3_vois2_dt10_s20

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 10.0, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt10_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt10_s20_214827.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 1204982 ; propagations 8389209947 ; nodes non rapporté ; temps de résolution 2898.2 s (non déterministe)
- Durée de l'exécution : 3076.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s00

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s00_200735.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 13000090** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 329581 ; propagations 1385978699 ; nodes non rapporté ; temps de résolution 600.7 s (non déterministe)
- Durée de l'exécution : 844.2 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s01

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s01_200734.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 11000053** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 323776 ; propagations 1391681668 ; nodes non rapporté ; temps de résolution 592.5 s (non déterministe)
- Durée de l'exécution : 837.8 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s02

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s02_200734.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 7000063** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 327238 ; propagations 1365548103 ; nodes non rapporté ; temps de résolution 596.3 s (non déterministe)
- Durée de l'exécution : 838.4 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s03

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s03_200734.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27000108** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 283895 ; propagations 1473436585 ; nodes non rapporté ; temps de résolution 569.8 s (non déterministe)
- Durée de l'exécution : 811.6 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s04

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s04_200735.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 13000062** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 327978 ; propagations 1371658058 ; nodes non rapporté ; temps de résolution 576.2 s (non déterministe)
- Durée de l'exécution : 822.0 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s05

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s05_200735.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000048** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 329233 ; propagations 1370592727 ; nodes non rapporté ; temps de résolution 581.2 s (non déterministe)
- Durée de l'exécution : 824.8 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s06

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s06_200734.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 13000054** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 296234 ; propagations 1422939324 ; nodes non rapporté ; temps de résolution 572.1 s (non déterministe)
- Durée de l'exécution : 815.3 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s07

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s07_200735.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 11000038** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 360567 ; propagations 1315776851 ; nodes non rapporté ; temps de résolution 593.1 s (non déterministe)
- Durée de l'exécution : 835.3 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s08

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s08_200735.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000055** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 260901 ; propagations 1440933376 ; nodes non rapporté ; temps de résolution 556.0 s (non déterministe)
- Durée de l'exécution : 799.5 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s09

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s09_200734.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 13000048** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 319588 ; propagations 1291506052 ; nodes non rapporté ; temps de résolution 578.1 s (non déterministe)
- Durée de l'exécution : 823.6 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s10

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s10_200734.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000082** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 279779 ; propagations 1421852721 ; nodes non rapporté ; temps de résolution 573.5 s (non déterministe)
- Durée de l'exécution : 817.5 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s11

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s11_200734.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 11000047** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 268369 ; propagations 1425149897 ; nodes non rapporté ; temps de résolution 550.2 s (non déterministe)
- Durée de l'exécution : 796.8 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s12

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s12_200734.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20000083** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 365340 ; propagations 1405770003 ; nodes non rapporté ; temps de résolution 623.5 s (non déterministe)
- Durée de l'exécution : 872.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s13

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s13_200734.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000063** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 362842 ; propagations 1358656081 ; nodes non rapporté ; temps de résolution 605.0 s (non déterministe)
- Durée de l'exécution : 847.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s14

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s14_200734.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21000081** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 443202 ; propagations 1403364737 ; nodes non rapporté ; temps de résolution 663.6 s (non déterministe)
- Durée de l'exécution : 907.8 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s15

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s15_200735.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 10000074** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 361887 ; propagations 1353980980 ; nodes non rapporté ; temps de résolution 609.1 s (non déterministe)
- Durée de l'exécution : 853.4 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s16

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s16_200735.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 10000117** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 362221 ; propagations 1397660291 ; nodes non rapporté ; temps de résolution 607.8 s (non déterministe)
- Durée de l'exécution : 850.4 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s17

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s17_200735.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 4000056** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 387842 ; propagations 1357133564 ; nodes non rapporté ; temps de résolution 623.7 s (non déterministe)
- Durée de l'exécution : 867.6 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s18

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s18_200734.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 12000060** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 345963 ; propagations 1395177344 ; nodes non rapporté ; temps de résolution 608.9 s (non déterministe)
- Durée de l'exécution : 852.2 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:07 — bench3_vois2_dt1_s19

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s19_200734.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 19000053** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 285731 ; propagations 1453923077 ; nodes non rapporté ; temps de résolution 571.6 s (non déterministe)
- Durée de l'exécution : 815.4 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:20 — bench3_vois2_dt1_s20

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 1.0, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt1_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt1_s20_202052.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 14000062** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 284003 ; propagations 1450142638 ; nodes non rapporté ; temps de résolution 586.5 s (non déterministe)
- Durée de l'exécution : 836.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:20 — bench3_vois2_dt2p5_s00

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 0.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s00_202055.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 544279 ; propagations 3083522063 ; nodes non rapporté ; temps de résolution 1256.0 s (non déterministe)
- Durée de l'exécution : 1504.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s01

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 1.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s01_202107.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 629784 ; propagations 2901677503 ; nodes non rapporté ; temps de résolution 1311.7 s (non déterministe)
- Durée de l'exécution : 1559.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s02

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 2.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s02_202110.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 655993 ; propagations 3034809859 ; nodes non rapporté ; temps de résolution 1328.4 s (non déterministe)
- Durée de l'exécution : 1574.6 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s03

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 3.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s03_202111.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 25** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 709951 ; propagations 3010927035 ; nodes non rapporté ; temps de résolution 1339.1 s (non déterministe)
- Durée de l'exécution : 1586.3 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s04

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 4.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s04_202112.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 17** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 456347 ; propagations 2763660197 ; nodes non rapporté ; temps de résolution 1178.8 s (non déterministe)
- Durée de l'exécution : 1430.0 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s05

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 5.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s05_202118.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 810278 ; propagations 3019639605 ; nodes non rapporté ; temps de résolution 1328.0 s (non déterministe)
- Durée de l'exécution : 1576.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s06

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 6.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s06_202118.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 742874 ; propagations 2944235937 ; nodes non rapporté ; temps de résolution 1371.1 s (non déterministe)
- Durée de l'exécution : 1617.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s07

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 7.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s07_202121.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 99** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 618180 ; propagations 2969716423 ; nodes non rapporté ; temps de résolution 1300.3 s (non déterministe)
- Durée de l'exécution : 1547.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s08

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 8.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s08_202131.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 31** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 570775 ; propagations 3184564542 ; nodes non rapporté ; temps de résolution 1307.1 s (non déterministe)
- Durée de l'exécution : 1552.2 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s09

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 9.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s09_202133.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 639518 ; propagations 2990577156 ; nodes non rapporté ; temps de résolution 1308.4 s (non déterministe)
- Durée de l'exécution : 1554.8 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s10

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 10.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s10_202134.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 26** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 670615 ; propagations 2971634238 ; nodes non rapporté ; temps de résolution 1321.8 s (non déterministe)
- Durée de l'exécution : 1569.4 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s11

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 11.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s11_202140.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 39** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 695182 ; propagations 2951086896 ; nodes non rapporté ; temps de résolution 1291.9 s (non déterministe)
- Durée de l'exécution : 1538.0 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s12

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 12.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s12_202143.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000029** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 675537 ; propagations 2922523128 ; nodes non rapporté ; temps de résolution 1325.0 s (non déterministe)
- Durée de l'exécution : 1572.2 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s13

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 13.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s13_202146.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 20** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 527226 ; propagations 2876375290 ; nodes non rapporté ; temps de résolution 1236.6 s (non déterministe)
- Durée de l'exécution : 1484.5 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s14

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 14.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s14_202148.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000031** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 803083 ; propagations 3103219582 ; nodes non rapporté ; temps de résolution 1425.3 s (non déterministe)
- Durée de l'exécution : 1671.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:21 — bench3_vois2_dt2p5_s15

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 15.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s15_202149.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 607580 ; propagations 3173559704 ; nodes non rapporté ; temps de résolution 1297.4 s (non déterministe)
- Durée de l'exécution : 1547.6 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:22 — bench3_vois2_dt2p5_s16

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 16.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s16_202203.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 704276 ; propagations 3073132611 ; nodes non rapporté ; temps de résolution 1372.0 s (non déterministe)
- Durée de l'exécution : 1619.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:22 — bench3_vois2_dt2p5_s17

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 17.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s17_202208.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000038** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 842480 ; propagations 3073921199 ; nodes non rapporté ; temps de résolution 1462.2 s (non déterministe)
- Durée de l'exécution : 1711.1 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:22 — bench3_vois2_dt2p5_s18

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 18.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s18_202243.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 50** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 607949 ; propagations 3106425852 ; nodes non rapporté ; temps de résolution 1315.0 s (non déterministe)
- Durée de l'exécution : 1564.1 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:34 — bench3_vois2_dt2p5_s19

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 19.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s19_203450.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 7000058** (infaisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 738357 ; propagations 3140626411 ; nodes non rapporté ; temps de résolution 1456.5 s (non déterministe)
- Durée de l'exécution : 1710.9 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## 2026-11-26 20:45 — bench3_vois2_dt2p5_s20

Interaction voisinage-budget sur bench_3 : voisinage 2, budget deterministe 2.5, population 18, 26 generations, NR=6, NM=6, graine 20.

- Configuration : `experiments/config/bench3_voisinage_budget/bench3_vois2_dt2p5_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_vois2_dt2p5_s20_204504.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 6, NM = 6, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 586581 ; propagations 3036876306 ; nodes non rapporté ; temps de résolution 1350.9 s (non déterministe)
- Durée de l'exécution : 1609.7 s ; commit `96c603cc45b5bcc1a6198bdd354b20c7763a9b57`

## Synthese - Interaction voisinage-budget sur bench_3

- 63 nouvelles executions et 105 references reutilisees.
- Comparaison de huit combinaisons sur 21 graines.
- Aucun optimum atteint (optimum documente : 16).
- Interaction importante entre voisinage et budget.
- Voisinage 2, budget 1 : aucune solution sans violation quasi stricte.
- Voisinage 2, budget 5 : cout moyen de 23.1429.
- Voisinage 2, budget 10 : cout moyen de 20.7619.
- Budgets 5 et 10 avec voisinage 2 : 21/21 solutions sans violation.
- Le passage du budget 5 a 10 reduit le cout moyen de 10.29 %,
  mais augmente les propagations de 65.52 %.
- Voisinage 1 et budget 5 conserves pour les prochaines series.
- Rapport : experiments/analysis/bench3_neighborhood_budget.md.
- Script : experiments/analysis/analyze_bench3_neighborhood_budget.py.

## 2026-11-26 22:42 — bench3_nr3_nm12_s00

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 0.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s00_224244.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 55278 ; propagations 249086663 ; nodes non rapporté ; temps de résolution 119.8 s (non déterministe)
- Durée de l'exécution : 356.1 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s01

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 1.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s01_224244.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 47** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 53565 ; propagations 258610643 ; nodes non rapporté ; temps de résolution 128.9 s (non déterministe)
- Durée de l'exécution : 366.6 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s02

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 2.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s02_224245.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 56135 ; propagations 254823781 ; nodes non rapporté ; temps de résolution 125.5 s (non déterministe)
- Durée de l'exécution : 364.4 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s03

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 3.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s03_224244.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 49** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 79893 ; propagations 344010583 ; nodes non rapporté ; temps de résolution 173.8 s (non déterministe)
- Durée de l'exécution : 420.0 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s04

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 4.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s04_224245.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 70653 ; propagations 296966183 ; nodes non rapporté ; temps de résolution 150.5 s (non déterministe)
- Durée de l'exécution : 397.2 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s05

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 5.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s05_224244.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 51** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 87505 ; propagations 381620126 ; nodes non rapporté ; temps de résolution 193.4 s (non déterministe)
- Durée de l'exécution : 442.0 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s06

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 6.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s06_224245.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 62911 ; propagations 282433672 ; nodes non rapporté ; temps de résolution 138.9 s (non déterministe)
- Durée de l'exécution : 376.7 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s07

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 7.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s07_224244.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 59695 ; propagations 279789962 ; nodes non rapporté ; temps de résolution 135.1 s (non déterministe)
- Durée de l'exécution : 372.6 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s08

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 8.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s08_224244.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 59176 ; propagations 276024279 ; nodes non rapporté ; temps de résolution 140.8 s (non déterministe)
- Durée de l'exécution : 387.1 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s09

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 9.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s09_224244.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 58479 ; propagations 256483629 ; nodes non rapporté ; temps de résolution 125.1 s (non déterministe)
- Durée de l'exécution : 363.5 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s10

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 10.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s10_224244.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63714 ; propagations 289844552 ; nodes non rapporté ; temps de résolution 143.3 s (non déterministe)
- Durée de l'exécution : 383.0 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s11

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 11.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s11_224245.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 82592 ; propagations 356830900 ; nodes non rapporté ; temps de résolution 180.2 s (non déterministe)
- Durée de l'exécution : 425.1 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s12

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 12.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s12_224245.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 81676 ; propagations 352089837 ; nodes non rapporté ; temps de résolution 176.9 s (non déterministe)
- Durée de l'exécution : 423.3 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s13

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 13.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s13_224245.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 71941 ; propagations 303916201 ; nodes non rapporté ; temps de résolution 152.1 s (non déterministe)
- Durée de l'exécution : 389.2 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s14

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 14.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s14_224245.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 40** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 60647 ; propagations 277238550 ; nodes non rapporté ; temps de résolution 138.0 s (non déterministe)
- Durée de l'exécution : 374.8 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s15

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 15.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s15_224244.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52410 ; propagations 221204075 ; nodes non rapporté ; temps de résolution 109.5 s (non déterministe)
- Durée de l'exécution : 346.6 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s16

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 16.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s16_224245.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 59840 ; propagations 278177266 ; nodes non rapporté ; temps de résolution 137.5 s (non déterministe)
- Durée de l'exécution : 376.1 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s17

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 17.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s17_224244.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 50** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 85291 ; propagations 372107325 ; nodes non rapporté ; temps de résolution 186.5 s (non déterministe)
- Durée de l'exécution : 433.1 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s18

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 18.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s18_224245.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 57598 ; propagations 263783862 ; nodes non rapporté ; temps de résolution 129.6 s (non déterministe)
- Durée de l'exécution : 367.2 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:42 — bench3_nr3_nm12_s19

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 19.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s19_224244.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 60884 ; propagations 257562362 ; nodes non rapporté ; temps de résolution 124.8 s (non déterministe)
- Durée de l'exécution : 364.4 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr3_nm12_s20

Comparaison des ratios NR/NM sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 20.

- Configuration : `experiments/config/bench3_ratio/bench3_nr3_nm12_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr3_nm12_s20_224832.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 81675 ; propagations 363453118 ; nodes non rapporté ; temps de résolution 183.9 s (non déterministe)
- Durée de l'exécution : 430.4 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr8_nm2_s00

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 0.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s00_224842.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 77072 ; propagations 326575494 ; nodes non rapporté ; temps de résolution 166.1 s (non déterministe)
- Durée de l'exécution : 411.6 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr8_nm2_s01

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 1.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s01_224848.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 76984 ; propagations 354511060 ; nodes non rapporté ; temps de résolution 176.8 s (non déterministe)
- Durée de l'exécution : 415.6 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr8_nm2_s02

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 2.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s02_224850.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 119615 ; propagations 510229723 ; nodes non rapporté ; temps de résolution 263.3 s (non déterministe)
- Durée de l'exécution : 506.3 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr8_nm2_s03

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 3.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s03_224850.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 31** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 62779 ; propagations 269325325 ; nodes non rapporté ; temps de résolution 139.3 s (non déterministe)
- Durée de l'exécution : 378.5 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr8_nm2_s04

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 4.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s04_224852.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 85120 ; propagations 379077236 ; nodes non rapporté ; temps de résolution 185.1 s (non déterministe)
- Durée de l'exécution : 431.5 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr8_nm2_s05

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 5.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s05_224853.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 1000037** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 64143 ; propagations 301494023 ; nodes non rapporté ; temps de résolution 159.5 s (non déterministe)
- Durée de l'exécution : 405.8 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:48 — bench3_nr8_nm2_s06

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 6.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s06_224857.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 31** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 89722 ; propagations 422737182 ; nodes non rapporté ; temps de résolution 215.6 s (non déterministe)
- Durée de l'exécution : 451.9 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s07

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 7.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s07_224901.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 33** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 109432 ; propagations 497707989 ; nodes non rapporté ; temps de résolution 245.5 s (non déterministe)
- Durée de l'exécution : 489.7 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s08

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 8.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s08_224902.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 75366 ; propagations 345821228 ; nodes non rapporté ; temps de résolution 169.6 s (non déterministe)
- Durée de l'exécution : 416.4 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s09

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 9.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s09_224902.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 92427 ; propagations 408290666 ; nodes non rapporté ; temps de résolution 209.6 s (non déterministe)
- Durée de l'exécution : 455.9 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s10

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 10.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s10_224908.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 82085 ; propagations 379514909 ; nodes non rapporté ; temps de résolution 194.9 s (non déterministe)
- Durée de l'exécution : 441.5 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s11

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 11.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s11_224912.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 110038 ; propagations 477516919 ; nodes non rapporté ; temps de résolution 247.4 s (non déterministe)
- Durée de l'exécution : 488.2 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s12

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 12.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s12_224915.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 101876 ; propagations 479690932 ; nodes non rapporté ; temps de résolution 241.5 s (non déterministe)
- Durée de l'exécution : 482.7 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s13

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 13.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s13_224923.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 34** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 68630 ; propagations 341174753 ; nodes non rapporté ; temps de résolution 172.4 s (non déterministe)
- Durée de l'exécution : 408.3 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s14

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 14.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s14_224945.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 114388 ; propagations 486532440 ; nodes non rapporté ; temps de résolution 240.9 s (non déterministe)
- Durée de l'exécution : 481.8 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s15

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 15.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s15_224949.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 74380 ; propagations 314435200 ; nodes non rapporté ; temps de résolution 165.8 s (non déterministe)
- Durée de l'exécution : 410.0 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s16

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 16.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s16_224951.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63733 ; propagations 312934838 ; nodes non rapporté ; temps de résolution 155.3 s (non déterministe)
- Durée de l'exécution : 390.6 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:49 — bench3_nr8_nm2_s17

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 17.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s17_224958.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 75283 ; propagations 323608009 ; nodes non rapporté ; temps de résolution 162.9 s (non déterministe)
- Durée de l'exécution : 398.3 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:50 — bench3_nr8_nm2_s18

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 18.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s18_225007.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 21** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 66981 ; propagations 313652832 ; nodes non rapporté ; temps de résolution 158.9 s (non déterministe)
- Durée de l'exécution : 395.7 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:55 — bench3_nr8_nm2_s19

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 19.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s19_225510.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 43** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 101746 ; propagations 459599533 ; nodes non rapporté ; temps de résolution 201.0 s (non déterministe)
- Durée de l'exécution : 391.8 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## 2026-11-26 22:55 — bench3_nr8_nm2_s20

Comparaison des ratios NR/NM sur bench_3 : NR=8, NM=2, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 20.

- Configuration : `experiments/config/bench3_ratio/bench3_nr8_nm2_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_nr8_nm2_s20_225534.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 8, NM = 2, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 74928 ; propagations 338494844 ; nodes non rapporté ; temps de résolution 147.6 s (non déterministe)
- Durée de l'exécution : 330.2 s ; commit `91aa95633017c9c6cc8001da885f1e595be8c4cd`

## Synthese - Ratios NR/NM sur bench_3

- 42 nouvelles executions et 21 references reutilisees.
- Comparaison des ratios 3/12, 6/6 et 8/2.
- Budget nominal constant de 486 individus.
- Aucun optimum atteint.
- Toutes les solutions finales sont faisables.
- Ratio 3/12 : 21/21 solutions sans violation quasi stricte.
- Ratio 6/6 : 21/21 solutions sans violation quasi stricte.
- Ratio 8/2 : 20/21 solutions sans violation quasi stricte.
- Ratio 3/12 : reduction du cout moyen global de 8.77 %
  et des propagations de 12.48 % relativement au ratio 6/6.
- Ratio 3/12 retenu, en coherence avec bench_2.
- Rapport : experiments/analysis/bench3_ratio.md.
- Script : experiments/analysis/analyze_bench3_ratio.py.

## 2026-11-26 23:06 — bench3_validation_s00

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 0.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s00_230651.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 55278 ; propagations 249086663 ; nodes non rapporté ; temps de résolution 120.6 s (non déterministe)
- Durée de l'exécution : 358.1 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s01

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 1.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s01_230651.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 47** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 53565 ; propagations 258610643 ; nodes non rapporté ; temps de résolution 130.6 s (non déterministe)
- Durée de l'exécution : 370.3 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s02

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 2.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s02_230651.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 56135 ; propagations 254823781 ; nodes non rapporté ; temps de résolution 126.9 s (non déterministe)
- Durée de l'exécution : 366.6 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s03

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 3.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s03_230650.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 49** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 79893 ; propagations 344010583 ; nodes non rapporté ; temps de résolution 169.7 s (non déterministe)
- Durée de l'exécution : 411.1 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s04

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 4.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s04_230651.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 70653 ; propagations 296966183 ; nodes non rapporté ; temps de résolution 147.8 s (non déterministe)
- Durée de l'exécution : 386.6 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s05

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 5.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s05_230651.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 51** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 87505 ; propagations 381620126 ; nodes non rapporté ; temps de résolution 190.2 s (non déterministe)
- Durée de l'exécution : 429.5 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s06

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 6.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s06_230651.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 62911 ; propagations 282433672 ; nodes non rapporté ; temps de résolution 139.4 s (non déterministe)
- Durée de l'exécution : 377.8 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s07

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 7.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s07_230651.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 59695 ; propagations 279789962 ; nodes non rapporté ; temps de résolution 137.7 s (non déterministe)
- Durée de l'exécution : 377.4 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s08

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 8.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s08_230650.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 59176 ; propagations 276024279 ; nodes non rapporté ; temps de résolution 137.8 s (non déterministe)
- Durée de l'exécution : 376.7 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s09

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 9.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s09_230651.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 37** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 58479 ; propagations 256483629 ; nodes non rapporté ; temps de résolution 125.3 s (non déterministe)
- Durée de l'exécution : 364.0 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s10

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 10.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s10_230651.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 27** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63714 ; propagations 289844552 ; nodes non rapporté ; temps de résolution 142.4 s (non déterministe)
- Durée de l'exécution : 380.5 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s11

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 11.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s11_230650.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 23** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 82592 ; propagations 356830900 ; nodes non rapporté ; temps de résolution 178.4 s (non déterministe)
- Durée de l'exécution : 419.4 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s12

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 12.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s12_230651.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 29** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 81676 ; propagations 352089837 ; nodes non rapporté ; temps de résolution 172.7 s (non déterministe)
- Durée de l'exécution : 415.7 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s13

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 13.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s13_230651.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 41** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 71941 ; propagations 303916201 ; nodes non rapporté ; temps de résolution 152.8 s (non déterministe)
- Durée de l'exécution : 390.0 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s14

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 14.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s14_230651.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 40** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 60647 ; propagations 277238550 ; nodes non rapporté ; temps de résolution 139.9 s (non déterministe)
- Durée de l'exécution : 378.0 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s15

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 15.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s15_230650.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 46** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52410 ; propagations 221204075 ; nodes non rapporté ; temps de résolution 111.0 s (non déterministe)
- Durée de l'exécution : 350.4 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s16

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 16.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s16_230651.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 48** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 59840 ; propagations 278177266 ; nodes non rapporté ; temps de résolution 137.4 s (non déterministe)
- Durée de l'exécution : 376.4 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s17

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 17.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s17_230650.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 50** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 85291 ; propagations 372107325 ; nodes non rapporté ; temps de résolution 183.7 s (non déterministe)
- Durée de l'exécution : 434.1 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s18

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 18.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s18_230651.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 22** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 57598 ; propagations 263783862 ; nodes non rapporté ; temps de résolution 130.4 s (non déterministe)
- Durée de l'exécution : 370.2 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:06 — bench3_validation_s19

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 19.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s19_230651.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 60884 ; propagations 257562362 ; nodes non rapporté ; temps de résolution 125.8 s (non déterministe)
- Durée de l'exécution : 365.2 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## 2026-11-26 23:12 — bench3_validation_s20

Validation des strategies implicites sur bench_3 : NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 20.

- Configuration : `experiments/config/bench3_validation/bench3_validation_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_validation_s20_231242.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `shift_start`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 81675 ; propagations 363453118 ; nodes non rapporté ; temps de résolution 149.1 s (non déterministe)
- Durée de l'exécution : 331.9 s ; commit `27f6efe1212ea1dbf8715433d61bb95402c83fd9`

## Synthese - Validation des strategies sur bench_3

- 21 nouvelles executions et 21 references reutilisees.
- Comparaison des strategies implicites et explicites.
- Ratio NR/NM : 3/12.
- Equivalence observee pour les 21 graines.
- Aucune difference sur les indicateurs algorithmiques compares.
- Mesures temporelles et metadonnees exclues.
- Strategies explicites conservees pour les prochaines series.
- Rapport : experiments/analysis/bench3_validation.md.
- Script : experiments/analysis/analyze_bench3_validation.py.

## 2026-11-26 23:25 — bench3_mut_activity_s00

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 0.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s00_232553.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 33** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 70710 ; propagations 326504855 ; nodes non rapporté ; temps de résolution 157.5 s (non déterministe)
- Durée de l'exécution : 396.5 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:25 — bench3_mut_activity_s01

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 1.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s01_232554.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69979 ; propagations 311079398 ; nodes non rapporté ; temps de résolution 150.9 s (non déterministe)
- Durée de l'exécution : 391.2 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s02

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 2.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s02_232602.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 1000030** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 74412 ; propagations 333501769 ; nodes non rapporté ; temps de résolution 167.3 s (non déterministe)
- Durée de l'exécution : 406.7 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s03

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 3.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s03_232602.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 42** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 79072 ; propagations 359870675 ; nodes non rapporté ; temps de résolution 177.2 s (non déterministe)
- Durée de l'exécution : 415.5 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s04

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 4.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s04_232604.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 28** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 71558 ; propagations 316502777 ; nodes non rapporté ; temps de résolution 157.0 s (non déterministe)
- Durée de l'exécution : 396.1 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s05

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 5.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s05_232604.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 27** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 60795 ; propagations 279778421 ; nodes non rapporté ; temps de résolution 138.4 s (non déterministe)
- Durée de l'exécution : 377.9 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s06

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 6.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s06_232604.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 63613 ; propagations 289971688 ; nodes non rapporté ; temps de résolution 141.8 s (non déterministe)
- Durée de l'exécution : 380.6 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s07

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 7.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s07_232605.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 24** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 66260 ; propagations 294403020 ; nodes non rapporté ; temps de résolution 142.1 s (non déterministe)
- Durée de l'exécution : 381.1 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s08

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 8.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s08_232605.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 33** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 64650 ; propagations 303024917 ; nodes non rapporté ; temps de résolution 150.8 s (non déterministe)
- Durée de l'exécution : 389.0 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s09

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 9.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s09_232607.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 36** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 91816 ; propagations 397140875 ; nodes non rapporté ; temps de résolution 195.9 s (non déterministe)
- Durée de l'exécution : 440.8 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s10

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 10.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s10_232609.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 68045 ; propagations 304599477 ; nodes non rapporté ; temps de résolution 149.2 s (non déterministe)
- Durée de l'exécution : 389.9 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s11

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 11.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s11_232611.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 55** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 101574 ; propagations 453845516 ; nodes non rapporté ; temps de résolution 218.9 s (non déterministe)
- Durée de l'exécution : 458.9 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s12

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 12.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s12_232613.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 32** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 80706 ; propagations 362972682 ; nodes non rapporté ; temps de résolution 179.7 s (non déterministe)
- Durée de l'exécution : 417.3 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s13

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 13.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s13_232614.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 39** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 69663 ; propagations 296154503 ; nodes non rapporté ; temps de résolution 148.5 s (non déterministe)
- Durée de l'exécution : 388.4 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s14

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 14.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s14_232622.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 47** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 95070 ; propagations 412821245 ; nodes non rapporté ; temps de résolution 200.7 s (non déterministe)
- Durée de l'exécution : 435.3 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s15

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 15.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s15_232629.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 37** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 71868 ; propagations 303440442 ; nodes non rapporté ; temps de résolution 151.0 s (non déterministe)
- Durée de l'exécution : 389.7 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s16

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 16.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s16_232634.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 55** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 67512 ; propagations 292776595 ; nodes non rapporté ; temps de résolution 144.3 s (non déterministe)
- Durée de l'exécution : 382.6 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:26 — bench3_mut_activity_s17

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 17.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s17_232644.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 45** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 93323 ; propagations 424090317 ; nodes non rapporté ; temps de résolution 203.0 s (non déterministe)
- Durée de l'exécution : 442.1 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:27 — bench3_mut_activity_s18

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 18.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s18_232715.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 31** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 68284 ; propagations 315431926 ; nodes non rapporté ; temps de résolution 153.5 s (non déterministe)
- Durée de l'exécution : 385.8 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:31 — bench3_mut_activity_s19

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 19.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s19_233125.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 25** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 66030 ; propagations 295998050 ; nodes non rapporté ; temps de résolution 125.1 s (non déterministe)
- Durée de l'exécution : 314.9 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:32 — bench3_mut_activity_s20

Comparaison des operateurs de mutation sur bench_3 : mutation activity, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 20.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_activity_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_activity_s20_233223.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `activity`
- **Coût obtenu : 2000033** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 68060 ; propagations 334844673 ; nodes non rapporté ; temps de résolution 133.3 s (non déterministe)
- Durée de l'exécution : 314.6 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s00

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 0.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s00.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s00_232017.json`
- Instance : bench_3 ; graine 0 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 1000037** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 70527 ; propagations 327760679 ; nodes non rapporté ; temps de résolution 166.8 s (non déterministe)
- Durée de l'exécution : 417.6 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s01

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 1.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s01.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s01_232017.json`
- Instance : bench_3 ; graine 1 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 1000041** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 43282 ; propagations 211191104 ; nodes non rapporté ; temps de résolution 107.6 s (non déterministe)
- Durée de l'exécution : 345.8 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s02

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 2.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s02.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s02_232017.json`
- Instance : bench_3 ; graine 2 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 40** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 49175 ; propagations 222898298 ; nodes non rapporté ; temps de résolution 113.5 s (non déterministe)
- Durée de l'exécution : 353.4 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s03

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 3.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s03.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s03_232016.json`
- Instance : bench_3 ; graine 3 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 24** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 55767 ; propagations 250417923 ; nodes non rapporté ; temps de résolution 125.7 s (non déterministe)
- Durée de l'exécution : 365.0 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s04

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 4.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s04.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s04_232016.json`
- Instance : bench_3 ; graine 4 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 26** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 53446 ; propagations 236844862 ; nodes non rapporté ; temps de résolution 118.3 s (non déterministe)
- Durée de l'exécution : 355.7 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s05

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 5.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s05.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s05_232017.json`
- Instance : bench_3 ; graine 5 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 27** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 42977 ; propagations 195459995 ; nodes non rapporté ; temps de résolution 95.4 s (non déterministe)
- Durée de l'exécution : 333.9 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s06

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 6.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s06.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s06_232017.json`
- Instance : bench_3 ; graine 6 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 1000028** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 44711 ; propagations 224266782 ; nodes non rapporté ; temps de résolution 108.8 s (non déterministe)
- Durée de l'exécution : 347.0 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s07

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 7.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s07.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s07_232016.json`
- Instance : bench_3 ; graine 7 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 32** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 52302 ; propagations 227870772 ; nodes non rapporté ; temps de résolution 112.4 s (non déterministe)
- Durée de l'exécution : 349.3 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s08

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 8.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s08.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s08_232017.json`
- Instance : bench_3 ; graine 8 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 48** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 56135 ; propagations 266556817 ; nodes non rapporté ; temps de résolution 130.6 s (non déterministe)
- Durée de l'exécution : 375.8 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s09

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 9.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s09.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s09_232016.json`
- Instance : bench_3 ; graine 9 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 44** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 50153 ; propagations 222818908 ; nodes non rapporté ; temps de résolution 107.1 s (non déterministe)
- Durée de l'exécution : 345.0 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s10

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 10.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s10.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s10_232017.json`
- Instance : bench_3 ; graine 10 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 30** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 49153 ; propagations 215923609 ; nodes non rapporté ; temps de résolution 105.7 s (non déterministe)
- Durée de l'exécution : 346.0 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s11

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 11.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s11.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s11_232016.json`
- Instance : bench_3 ; graine 11 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 40** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 51825 ; propagations 237823899 ; nodes non rapporté ; temps de résolution 118.4 s (non déterministe)
- Durée de l'exécution : 356.3 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s12

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 12.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s12.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s12_232017.json`
- Instance : bench_3 ; graine 12 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 44707 ; propagations 216071842 ; nodes non rapporté ; temps de résolution 106.8 s (non déterministe)
- Durée de l'exécution : 343.7 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s13

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 13.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s13.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s13_232016.json`
- Instance : bench_3 ; graine 13 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 45** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 46850 ; propagations 200437842 ; nodes non rapporté ; temps de résolution 99.9 s (non déterministe)
- Durée de l'exécution : 336.1 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s14

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 14.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s14.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s14_232016.json`
- Instance : bench_3 ; graine 14 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 62001 ; propagations 266664745 ; nodes non rapporté ; temps de résolution 132.7 s (non déterministe)
- Durée de l'exécution : 372.1 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s15

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 15.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s15.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s15_232016.json`
- Instance : bench_3 ; graine 15 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 49** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 61260 ; propagations 268163466 ; nodes non rapporté ; temps de résolution 138.8 s (non déterministe)
- Durée de l'exécution : 387.0 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s16

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 16.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s16.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s16_232016.json`
- Instance : bench_3 ; graine 16 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 32** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 50135 ; propagations 230046281 ; nodes non rapporté ; temps de résolution 111.5 s (non déterministe)
- Durée de l'exécution : 351.7 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s17

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 17.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s17.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s17_232017.json`
- Instance : bench_3 ; graine 17 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 38** (faisable) ; 26 générations, 1 restart(s)
- **Effort cumulé du solveur** : 503 appels ; failures 47126 ; propagations 203469545 ; nodes non rapporté ; temps de résolution 101.5 s (non déterministe)
- Durée de l'exécution : 346.2 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s18

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 18.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s18.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s18_232016.json`
- Instance : bench_3 ; graine 18 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 35** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 41796 ; propagations 207937546 ; nodes non rapporté ; temps de résolution 98.5 s (non déterministe)
- Durée de l'exécution : 335.6 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:20 — bench3_mut_block_boundary_s19

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 19.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s19.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s19_232016.json`
- Instance : bench_3 ; graine 19 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 31** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 47133 ; propagations 207341422 ; nodes non rapporté ; temps de résolution 105.7 s (non déterministe)
- Durée de l'exécution : 348.1 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## 2026-11-26 23:25 — bench3_mut_block_boundary_s20

Comparaison des operateurs de mutation sur bench_3 : mutation block_boundary, NR=3, NM=12, population 18, 26 generations, voisinage 1, budget deterministe 5, graine 20.

- Configuration : `experiments/config/bench3_mutation/bench3_mut_block_boundary_s20.json`
- Résultats : `experiments/results/2026-11-26/bench3_mut_block_boundary_s20_232552.json`
- Instance : bench_3 ; graine 20 ; population 18, NR = 3, NM = 12, 26 générations
- Stratégies : crossover `uniform_gene` ; mutation `block_boundary`
- **Coût obtenu : 36** (faisable) ; 26 générations, 0 restart(s)
- **Effort cumulé du solveur** : 486 appels ; failures 41541 ; propagations 187525961 ; nodes non rapporté ; temps de résolution 94.5 s (non déterministe)
- Durée de l'exécution : 332.2 s ; commit `55a4b7e2092174a313780b75518ce62530bee892`

## Synthese - Operateurs de mutation sur bench_3

- 42 nouvelles executions et 21 references reutilisees.
- Comparaison de shift_start, block_boundary et activity.
- Aucun optimum atteint.
- Toutes les solutions finales sont faisables.
- Shift_start : 21/21 solutions sans violation quasi stricte.
- Block_boundary : 18/21 solutions sans violation quasi stricte.
- Activity : 19/21 solutions sans violation quasi stricte.
- Block_boundary reduit les propagations de 22.34 %
  et le temps solveur de 22.43 % relativement a shift_start.
- Activity augmente l'effort solveur.
- Shift_start conserve pour sa robustesse observee.
- Rapport : experiments/analysis/bench3_mutation.md.
- Script : experiments/analysis/analyze_bench3_mutation.py.
