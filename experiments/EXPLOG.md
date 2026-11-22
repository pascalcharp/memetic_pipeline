# Journal des expériences

Une entrée par exécution de `python -m src.drivers.run_experiment`, ajoutée automatiquement. Les fichiers de résultats complets sont dans `experiments/results/<date>/`.

## 2026-11-22 15:16 — integration_bench1

Configuration de base : les réglages de la 9-intégration sur bench_1 (6 individus, NR = 2, NM = 2, 4 générations, stagnation d'une génération, graine 7). Sert de référence pour vérifier que le pipeline d'expériences fonctionne ; la 9-intégration y atteint l'optimum 94 avec un restart.

- Configuration : `experiments/config/integration_bench1.json`
- Résultats : `experiments/results/2026-11-22/integration_bench1_151611.json`
- Instance : bench_1 ; graine 7 ; population 6, NR = 2, NM = 2, 4 générations
- **Coût obtenu : 94** (faisable) ; 4 générations, 1 restart(s)
- **Effort cumulé du solveur** : 35 appels ; failures 118 ; propagations 237945 ; nodes non rapporté ; temps de résolution 0.2 s (non déterministe)
- Durée de l'exécution : 12.7 s ; commit `f3c2f3caeb7240689ee386c32eacd7522159f196`
