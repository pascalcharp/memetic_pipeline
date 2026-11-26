import json
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"

groups = {
    "explicit": {},
    "implicit": {},
}

for path in sorted(RESULTS.rglob("*.json")):
    if path.name.startswith("bench3_nr3_nm12_s"):
        group = "explicit"
    elif path.name.startswith("bench3_validation_s"):
        group = "implicit"
    else:
        continue

    run = json.loads(path.read_text())
    seed = run["settings"]["master_seed"]

    assert seed not in groups[group], f"Doublon : {group}, {seed}"
    groups[group][seed] = run

for group, runs in groups.items():
    assert sorted(runs) == list(range(21)), (
        f"Graines invalides : {group}"
    )

fields = (
    "settings",
    "best",
    "generations",
    "restarts",
    "cost_statistics",
    "diversity",
    "feasibility_rates",
)

effort_fields = (
    "calls",
    "nodes",
    "failures",
    "propagations",
)

different_seeds = set()

print("===== VALIDATION DES STRATEGIES SUR BENCH_3 =====")
print("Comparaison de 21 paires d'executions\n")

for field in fields:
    differences = [
        seed for seed in range(21)
        if groups["explicit"][seed][field]
        != groups["implicit"][seed][field]
    ]

    different_seeds.update(differences)

    print(f"{field} : {len(differences)}/21 differences")

    if differences:
        print("  Graines :", differences)

for field in effort_fields:
    differences = [
        seed for seed in range(21)
        if groups["explicit"][seed]["solver_effort"][field]
        != groups["implicit"][seed]["solver_effort"][field]
    ]

    different_seeds.update(differences)

    print(f"solver_effort.{field} : {len(differences)}/21 differences")

    if differences:
        print("  Graines :", differences)

print("\n--- REPRODUCTIBILITE ---")

for group, runs in groups.items():
    print(group)
    print("  Commits :", sorted({r["git_commit"] for r in runs.values()})
          if all("git_commit" in r for r in runs.values())
          else "Voir les metadonnees des resultats")

print("\n--- CONCLUSION ---")
print("Paires identiques :", 21 - len(different_seeds), "/ 21")
print("Paires differentes :", len(different_seeds), "/ 21")

if not different_seeds:
    print("Validation reussie : equivalence sur les champs compares.")
else:
    print("Des differences doivent etre analysees.")
