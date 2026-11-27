"""Analyse comparative des ratios croisement-mutation sur bench_2."""

import json
import statistics as st
from pathlib import Path


RESULTS = Path(__file__).resolve().parents[1] / "results"
OPTIMUM = 38
RATIOS = ((3, 12), (6, 6), (8, 2))


def load_results():
    groups = {v: [] for v in RATIOS}

    for path in sorted(RESULTS.rglob("*.json")):
        if path.name.startswith(("bench2_pop18_", "bench2_nr")):
            data = json.loads(path.read_text())
            settings = data["settings"]
            v = (settings["crossover_count"], settings["mutation_count"])
            if 2 * v[0] + v[1] != 18:
                raise ValueError(f"Budget nominal incorrect : {path}")

            if settings["population_size"] != 18:
                raise ValueError(f"Population incorrecte : {path}")

            if settings["generations"] != 26:
                raise ValueError(f"Nombre de generations incorrect : {path}")

            groups[v].append(data)

    for v, runs in groups.items():
        seeds = sorted(r["settings"]["master_seed"] for r in runs)
        if seeds != list(range(21)):
            raise ValueError(
                f"Ratio NR={v[0]}, NM={v[1]} : graines manquantes ou dupliquees"
            )

    return groups


def analyze(v, runs):
    costs = [r["best"]["cost"]["total"] for r in runs]
    first_feasible = []
    first_optimum = []
    budgets = []
    feasibility = {}

    for run in runs:
        settings = run["settings"]
        stats = sorted(
            run["cost_statistics"],
            key=lambda x: x["generation"]
        )

        feasible = next(
            (x["generation"] for x in stats
             if x["feasible_count"] > 0),
            None
        )

        optimum = next(
            (x["generation"] for x in stats
             if x["total_min"] == OPTIMUM),
            None
        )

        if feasible is not None:
            first_feasible.append(feasible)

        if optimum is not None:
            first_optimum.append(optimum)
            budgets.append(
                settings["population_size"] + optimum * (
                    2 * settings["crossover_count"]
                    + settings["mutation_count"]
                )
            )

        for event in run["feasibility_rates"]:
            key = (event["origin"], event["operator"])
            acc = feasibility.setdefault(key, [0, 0, 0])
            acc[0] += event["count"]
            acc[1] += event["feasible_before"]
            acc[2] += event["feasible_after"]

    print(f"\n===== NR={v[0]}, NM={v[1]} =====")

    print("\n--- PERFORMANCE ---")
    print("Executions :", len(runs))
    print("Generations :", runs[0]["settings"]["generations"])
    print("Optimums :", costs.count(OPTIMUM))
    print("Taux de succes :", round(100 * costs.count(OPTIMUM) / len(runs), 2))
    print("Cout moyen :", round(st.mean(costs), 4))
    print("Cout median :", st.median(costs))
    print("Ecart-type :", round(st.pstdev(costs), 4))
    print("Restarts moyens :", round(st.mean(r["restarts"] for r in runs), 2))

    for key in ("calls", "propagations", "solve_time_seconds"):
        values = [r["solver_effort"][key] for r in runs]
        print(key, "moyenne :", round(st.mean(values), 4))

    print("\n--- CONVERGENCE ---")
    print("Executions realisables :", len(first_feasible))
    print("Executions optimales observees :", len(first_optimum))

    for name, values in (
        ("Premiere faisabilite", first_feasible),
        ("Premiere generation optimale", first_optimum),
        ("Budget nominal avant optimum", budgets),
    ):
        if values:
            print(name)
            print("  Moyenne :", round(st.mean(values), 2))
            print("  Mediane :", st.median(values))
            print("  Minimum :", min(values))
            print("  Maximum :", max(values))

    print("\n--- DIVERSITE ---")

    for key in ("genotypic_diversity", "phenotypic_diversity"):
        histories = [
            sorted(r["diversity"], key=lambda x: x["generation"])
            for r in runs
        ]
        initial = st.mean(h[0][key] for h in histories)
        final = st.mean(h[-1][key] for h in histories)
        print(key)
        print("  Initiale :", round(initial, 4))
        print("  Finale :", round(final, 4))

    print("\n--- RECHERCHE LOCALE ---")

    for (origin, operator), (count, before, after) in feasibility.items():
        if count:
            print(origin, operator)
            print("  Avant :", round(100 * before / count, 2), "%")
            print("  Apres :", round(100 * after / count, 2), "%")
            print("  Gain :", round(100 * (after - before) / count, 2), "pts")

    print("\n--- REPRODUCTIBILITE ---")
    print("Commits :", sorted({r["git_commit"] for r in runs}))
    print("Git dirty :", {r["git_dirty"] for r in runs})
    print("Python :", sorted({r["python_version"] for r in runs}))
    print("Paquets :", sorted({
        json.dumps(r["packages"], sort_keys=True) for r in runs
    }))


def main():
    for v, runs in load_results().items():
        analyze(v, runs)


if __name__ == "__main__":
    main()
