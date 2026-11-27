"""Analyse comparative des budgets deterministes sur bench_3."""

import json
import statistics as st
from pathlib import Path


RESULTS = Path(__file__).resolve().parents[1] / "results"
OPTIMUM = 16
BUDGETS = (1.0, 2.5, 5.0, 10.0)


def load_results():
    groups = {v: [] for v in BUDGETS}

    for path in sorted(RESULTS.rglob("*.json")):
        if path.name.startswith(("bench3_pop18_", "bench3_dt")):
            data = json.loads(path.read_text())
            pop = data["settings"]["deterministic_time_units"]
            groups[pop].append(data)

    for pop, runs in groups.items():
        seeds = sorted(r["settings"]["master_seed"] for r in runs)
        if seeds != list(range(21)):
            raise ValueError(f"Budget {pop}: graines manquantes ou dupliquees")

    return groups


def analyze(pop, runs):
    costs = [r["best"]["cost"]["total"] for r in runs]
    breakdowns = [r["best"]["cost"] for r in runs]

    feasible_costs = [
        c["total"] for c in breakdowns
        if c["is_feasible"]
    ]

    clean_costs = [
        c["total"] for c in breakdowns
        if c["is_feasible"] and c["quasi_hard_cells"] == 0
    ]

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

    print(f"\n===== BUDGET DETERMINISTE {pop} =====")

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


    print("\n--- QUALITE DES SOLUTIONS FINALES ---")

    print("Solutions faisables :", len(feasible_costs))
    print("Taux de faisabilite :", round(
        100 * len(feasible_costs) / len(runs), 2
    ))

    print("Solutions faisables sans violation quasi stricte :",
          len(clean_costs))

    print("Taux de solutions sans violation (%) :", round(
        100 * len(clean_costs) / len(runs), 2
    ))

    print("Cout minimum global :", min(costs))
    print("Cout maximum global :", max(costs))

    for key in (
        "quasi_hard_cells",
        "coverage_violations",
        "structural_violations",
        "under_coverage_cost",
        "over_coverage_cost",
        "penalty_cost",
    ):
        values = [c[key] for c in breakdowns]
        print(key, "moyenne :", round(st.mean(values), 4))

    if clean_costs:
        print("Couts sans violation :")
        print("  Moyenne :", round(st.mean(clean_costs), 4))
        print("  Mediane :", st.median(clean_costs))
        print("  Minimum :", min(clean_costs))
        print("  Maximum :", max(clean_costs))
        print("  Ecart-type :", round(st.pstdev(clean_costs), 4))
        print("  Ecart absolu moyen a l'optimum :", round(
            st.mean(clean_costs) - OPTIMUM, 4
        ))
        print("  Ecart relatif moyen (%) :", round(
            100 * (st.mean(clean_costs) - OPTIMUM) / OPTIMUM, 2
        ))
    else:
        print("Aucune solution sans violation.")

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
    for pop, runs in load_results().items():
        analyze(pop, runs)


if __name__ == "__main__":
    main()
