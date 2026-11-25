"""Validation de l'architecture configurable sur bench_2."""

import json
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"


def load(pattern):
    groups = {}

    for path in RESULTS.rglob(pattern):
        data = json.loads(path.read_text())
        seed = data["settings"]["master_seed"]

        if seed in groups:
            raise ValueError(f"Graine dupliquee : {seed}")

        groups[seed] = data

    if sorted(groups) != list(range(21)):
        raise ValueError("Graines manquantes")

    return groups


def main():
    old = load("bench2_nr3_nm12_s*.json")
    new = load("bench2_validation_s*.json")

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

    differences = {field: [] for field in fields}

    for field in effort_fields:
        differences[f"solver_effort.{field}"] = []

    identical = 0

    for seed in range(21):
        a, b = old[seed], new[seed]
        same = True

        for field in fields:
            if a[field] != b[field]:
                differences[field].append(seed)
                same = False

        for field in effort_fields:
            if a["solver_effort"][field] != b["solver_effort"][field]:
                differences[f"solver_effort.{field}"].append(seed)
                same = False

        if same:
            identical += 1

    print("\n===== VALIDATION DES STRATEGIES =====")
    print("Executions comparees : 21")
    print("Executions identiques :", identical, "/ 21")

    print("\n--- DIFFERENCES ---")

    for field, seeds in differences.items():
        print(f"{field} : {len(seeds)} difference(s)")
        if seeds:
            print("  Graines :", seeds)

    print("\n--- PERFORMANCE ---")

    for name, runs in (("Ancien", old), ("Nouveau", new)):
        print(name)
        print("  Optimums :", sum(
            r["best"]["cost"]["total"] == 38
            for r in runs.values()
        ))
        print("  Commits :", sorted({
            r["git_commit"] for r in runs.values()
        }))
        print("  Git dirty :", {r["git_dirty"] for r in runs.values()})
        print("  Python :", {r["python_version"] for r in runs.values()})
        print("  Paquets :", {
            json.dumps(r["packages"], sort_keys=True)
            for r in runs.values()
        })


if __name__ == "__main__":
    main()
