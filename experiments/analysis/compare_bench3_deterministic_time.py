import json
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[1] / "results"

groups = {1.0: {}, 2.5: {}, 5.0: {}, 10.0: {}}

for path in RESULTS.rglob("*.json"):
    if not path.name.startswith(("bench3_pop18_", "bench3_dt")):
        continue

    run = json.loads(path.read_text())
    budget = run["settings"]["deterministic_time_units"]
    seed = run["settings"]["master_seed"]

    assert seed not in groups[budget], f"Doublon : {budget}, {seed}"
    groups[budget][seed] = run

for budget, runs in groups.items():
    assert sorted(runs) == list(range(21)), f"Graines invalides : {budget}"

fields = (
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

for budget in (1.0, 2.5, 10.0):
    print(f"\n===== BUDGET {budget} VS 5.0 =====")

    for field in fields:
        differences = sum(
            groups[budget][seed][field] != groups[5.0][seed][field]
            for seed in range(21)
        )
        print(f"{field} : {differences}/21 differences")

    for field in effort_fields:
        differences = sum(
            groups[budget][seed]["solver_effort"][field]
            != groups[5.0][seed]["solver_effort"][field]
            for seed in range(21)
        )
        print(f"solver_effort.{field} : {differences}/21 differences")
