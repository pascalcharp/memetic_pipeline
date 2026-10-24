# DEVLOG

## 2026-10-23 — Planification initiale

**Fait**
- Lecture de CLAUDE.md, `docs/ALGO.md`, `src/model/horaire.mzn` et des instances `data/bench_1..5.json`.
- Rédaction du `TODO.md` : 12 étapes (0 à 11), du conteneur jusqu'aux expériences, avec répartition des rôles (Claude / Pascal).

**Constats**
- Instances : de 3 employés × 1 activité × 32 périodes (`bench_1`) à 8 employés × 5 activités × 48 périodes (`bench_5`).
- MiniZinc 2.10.0 est installé localement (`/Applications/MiniZincIDE.app/Contents/Resources/minizinc`), mais il n'est pas dans le `PATH`, ni dans celui de PyCharm. CP-SAT 9.15 est disponible et c'est le solveur par défaut. Pas encore de Dockerfile.

**Décision D2** : `SolveurLocal` = recherche locale d'amélioration avec CP-SAT par défaut, derrière une classe d'indirection pour pouvoir changer de solveur.
- Écarts avec la structure de CLAUDE.md : modèle nommé `horaire.mzn` (et non `schedule_model.mzn`), instances `bench_*.json`.
- `requirements.txt` existe, mais les paquets ne sont pas installés dans `.venv`.

**Décisions en suspens** : D1, D3, D4 (voir `TODO.md`).
