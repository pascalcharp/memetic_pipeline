"""Mémétique de référence contre témoin « redémarrages aléatoires » sur bench_2 (étape 10d).

Usage, depuis la racine du dépôt : python experiments/analysis/analyze_random_restarts.py [RÉPERTOIRE_DES_RÉSULTATS]
Rapport : experiments/analysis/bench2_temoin_redemarrages.md.
"""
import glob
import json
import sys
from statistics import mean, median

OPTIMUM = 38
SERIES = {"mémétique": "bench2_memetique_ref", "redémarrages aléatoires": "bench2_temoin_redemarrages"}
CHECKPOINTS = (2, 4, 6, 8, 10, 15, 20, 30, 40, 60, 80)
results_dir = sys.argv[1] if len(sys.argv) > 1 else "experiments/results"


def load(series: str) -> list[dict]:
    documents = [json.load(open(p)) for p in glob.glob(f"{results_dir}/**/{series}_s*.json", recursive=True)]
    return sorted(documents, key=lambda d: d["settings"]["master_seed"])


def first_hit(document: dict) -> int | None:
    return next((c["generation"] for c in document["cost_statistics"] if c["total_min"] <= OPTIMUM), None)


def quartiles(values: list[float]) -> str:
    values = sorted(values)
    n = len(values)
    q1, q3 = values[n // 4], values[(3 * n) // 4]
    return f"{median(values):.4g} [{q1:.4g} ; {q3:.4g}]"


rows = {}
for label, series in SERIES.items():
    documents = load(series)
    hits = [first_hit(d) for d in documents]
    effort = [d["solver_effort"] for d in documents]
    rows[label] = (documents, hits, effort)
    print(f"\n=== {label} ({series}) : {len(documents)} exécutions, git_dirty = {sorted({str(d['git_dirty']) for d in documents})}")
    print("  graine : génération du succès / meilleur coût final")
    print("  " + "  ".join(f"{d['settings']['master_seed']}:{h}/{d['best']['cost']['total']}" for d, h in zip(documents, hits)))
    reached = [h for h in hits if h is not None]
    print(f"  succès : {len(reached)}/{len(documents)}", end="")
    if reached:
        print(f" ; génération du succès min {min(reached)}, médiane {median(reached)}, max {max(reached)}")
    else:
        print()
    print("  taux de succès cumulé : " + "  ".join(f"G{g}={sum(1 for h in reached if h <= g)}" for g in CHECKPOINTS))
    finals = [d["best"]["cost"]["total"] for d in documents]
    print(f"  meilleur coût final : min {min(finals)}, médiane {median(finals)}, max {max(finals)}")
    for key in ("calls", "failures", "propagations", "deterministic_time", "solve_time_seconds"):
        print(f"  effort cumulé {key} (80 gén.) : médiane [Q1 ; Q3] = {quartiles([e[key] for e in effort])}")
    print(f"  restarts : moyenne {mean(d['restarts'] for d in documents):.2f}")
    per_call = [e["deterministic_time"] / e["calls"] for e in effort]
    print(f"  temps déterministe par appel : {quartiles(per_call)}")

# Coût moyen du meilleur, génération par génération, à quelques points
print("\n=== meilleur coût (médiane sur les graines) par génération")
for g in CHECKPOINTS:
    line = [f"G{g:>2}"]
    for label, (documents, _, _) in rows.items():
        line.append(f"{label} {median(d['cost_statistics'][g]['total_min'] for d in documents)}")
    print("  " + " | ".join(line))

# Vérification : le mémétique relancé redonne la série bench2_seuil du 23 novembre
seuil = sorted((json.load(open(p)) for p in glob.glob(f"{results_dir}/**/bench2_seuil_s*.json", recursive=True)),
               key=lambda d: d["settings"]["master_seed"])
if seuil:
    same = [a["cost_statistics"] == b["cost_statistics"] for a, b in zip(seuil, rows["mémétique"][0])]
    print(f"\nmémétique relancé identique à bench2_seuil (cost_statistics) : {sum(same)}/{len(same)}")
