"""Mémétique contre témoin fort, recherche locale itérée (1+1), sur bench_2 (étape 10e).

Usage, depuis la racine du dépôt : python experiments/analysis/analyze_iterated_local_search.py
Rapport : experiments/analysis/bench2_ils.md.

Séries comparées (21 graines chacune, mêmes graines, même LocalSolver, même mutation) :
    - bench2_memetique_pop18 : population 18, 26 générations, NR = NM = 6 (486 à 520 appels) ;
    - bench2_ils : population 1, NR = 0, NM = 1, enfant gardé s'il n'est pas pire, 519 générations (520 appels).

Bench_2 est saturé (le mémétique atteint l'optimum 38 dans 21 cas sur 21) : on compare donc le meilleur coût à chaque
nombre d'appels cumulés au LocalSolver, et l'effort avant d'atteindre 38. Une exécution qui n'atteint pas 38 est
censurée : son effort avant 38 est « plus que le budget ». Le test de Wilcoxon apparié (rangs signés, loi exacte)
compare les deux séries graine par graine ; une paire de deux exécutions censurées est une égalité, écartée.
"""

import json
from pathlib import Path
from statistics import median

RESULTS = Path(__file__).resolve().parents[1] / "results"
OPTIMUM = 38
SEEDS = list(range(21))
SERIES = {"mémétique": "bench2_memetique_pop18", "témoin": "bench2_ils"}
CALL_CHECKPOINTS = (18, 50, 72, 100, 150, 200, 300, 400, 486, 520)
SUCCESS_CHECKPOINTS = (100, 200, 520)
EFFORT_FIELDS = ("calls", "propagations", "deterministic_time")
# Un coût de 2 000 000 ou plus signale une violation de « au moins 1 » (pénalité du modèle assoupli).
INFEASIBLE_THRESHOLD = 1_000_000


def load(series: str) -> list[dict]:
    runs = [json.loads(p.read_text()) for p in sorted(RESULTS.rglob(f"{series}_s*.json"))]
    runs.sort(key=lambda r: r["settings"]["master_seed"])
    if [r["settings"]["master_seed"] for r in runs] != SEEDS:
        raise ValueError(f"{series} : graines manquantes ou dupliquées")
    return runs


def trajectory(run: dict) -> list[tuple[dict, int]]:
    """Par génération : effort cumulé (appels, propagations, temps déterministe) et meilleur coût de la population."""
    cumulative = {field: 0 for field in EFFORT_FIELDS}
    points = []
    for effort, cost in zip(run["solver_effort_by_generation"], run["cost_statistics"]):
        for field in EFFORT_FIELDS:
            cumulative[field] += effort[field] or 0
        points.append((dict(cumulative), cost["total_min"]))
    return points


def best_at(points: list[tuple[dict, int]], calls: int) -> int | None:
    """Meilleur coût après au plus ``calls`` appels ; ``None`` avant la fin de la génération 0."""
    best = None
    for effort, cost in points:
        if effort["calls"] > calls:
            break
        best = cost if best is None else min(best, cost)
    return best


def effort_to_optimum(points: list[tuple[dict, int]]) -> dict | None:
    """Effort cumulé à la fin de la première génération où 38 est atteint ; ``None`` si jamais (censuré)."""
    return next((effort for effort, cost in points if cost <= OPTIMUM), None)


def quartiles(values: list[float]) -> tuple[float, float, float]:
    ordered = sorted(values)
    n = len(ordered)
    return ordered[n // 4], median(ordered), ordered[(3 * n) // 4]


def wilcoxon_signed_rank(differences: list[float]) -> tuple[float, float, int]:
    """Statistique W+ et valeur p bilatérale exacte du test des rangs signés ; les différences nulles sont écartées.

    Loi exacte sous H0 par programmation dynamique sur les rangs (rangs moyens pour les égalités, doublés pour
    rester entiers).
    """
    nonzero = [d for d in differences if d != 0]
    n = len(nonzero)
    if n == 0:
        return 0.0, 1.0, 0
    ordered = sorted(range(n), key=lambda i: abs(nonzero[i]))
    ranks = [0.0] * n
    position = 0
    while position < n:
        end = position
        while end + 1 < n and abs(nonzero[ordered[end + 1]]) == abs(nonzero[ordered[position]]):
            end += 1
        average = (position + end) / 2 + 1
        for k in range(position, end + 1):
            ranks[ordered[k]] = average
        position = end + 1
    doubled = [int(round(2 * r)) for r in ranks]
    w_plus = sum(r for r, d in zip(doubled, nonzero) if d > 0)
    counts = {0: 1}
    for r in doubled:
        updated = dict(counts)
        for total, count in counts.items():
            updated[total + r] = updated.get(total + r, 0) + count
        counts = updated
    total_count = 2 ** n
    mean = sum(doubled) / 2
    deviation = abs(w_plus - mean)
    extreme = sum(count for total, count in counts.items() if abs(total - mean) >= deviation)
    return w_plus / 2, min(1.0, extreme / total_count), n


def main() -> None:
    runs = {label: load(series) for label, series in SERIES.items()}
    points = {label: [trajectory(r) for r in series_runs] for label, series_runs in runs.items()}

    print("=== Provenance")
    for label, series_runs in runs.items():
        commits = sorted({r["git_commit"][:7] for r in series_runs})
        dirty = sorted({str(r["git_dirty"]) for r in series_runs})
        budgets = [p[-1][0]["calls"] for p in points[label]]
        print(f"  {label} : commit {commits}, git_dirty {dirty}, appels totaux min {min(budgets)} max {max(budgets)}")

    print("\n=== Meilleur coût en fonction des appels cumulés : Q1 / médiane / Q3 sur 21 graines")
    print(f"  {'appels':>6} | {'mémétique':>22} | {'témoin':>30}")
    for calls in CALL_CHECKPOINTS:
        cells = []
        for label in SERIES:
            values = [best_at(p, calls) for p in points[label]]
            values = [v for v in values if v is not None]
            q1, q2, q3 = quartiles(values)
            cells.append(f"{q1:,.0f} / {q2:,.0f} / {q3:,.0f}".replace(",", " "))
        print(f"  {calls:>6} | {cells[0]:>22} | {cells[1]:>30}")

    print("\n=== Effort avant d'atteindre 38 (exécutions censurées exclues des quartiles)")
    reached = {label: [effort_to_optimum(p) for p in points[label]] for label in SERIES}
    for label in SERIES:
        hits = [e for e in reached[label] if e is not None]
        print(f"  {label} : {len(hits)}/21 atteignent 38")
        for field in EFFORT_FIELDS:
            if hits:
                q1, q2, q3 = quartiles([e[field] for e in hits])
                print(f"    {field} : médiane {q2:.4g} [Q1 {q1:.4g} ; Q3 {q3:.4g}]")
        rates = "  ".join(f"≤{c} appels : {sum(1 for e in hits if e['calls'] <= c)}/21" for c in SUCCESS_CHECKPOINTS)
        print(f"    taux de succès : {rates}")

    print("\n=== Test de Wilcoxon apparié (témoin moins mémétique), censure au-delà du budget")
    for field in EFFORT_FIELDS:
        differences = []
        for m_effort, t_effort, m_points, t_points in zip(reached["mémétique"], reached["témoin"],
                                                           points["mémétique"], points["témoin"]):
            censored = max(m_points[-1][0][field], t_points[-1][0][field]) * 2
            m_value = m_effort[field] if m_effort is not None else censored
            t_value = t_effort[field] if t_effort is not None else censored
            differences.append(t_value - m_value)
        w_plus, p_value, n = wilcoxon_signed_rank(differences)
        positive = sum(1 for d in differences if d > 0)
        print(f"  {field} : {positive}/{n} paires où le témoin dépense plus ; W+ = {w_plus} ; p = {p_value:.2g}")

    print("\n=== Faisabilité et diversité")
    for label, series_runs in runs.items():
        first_feasible = [next((c["generation"] for c in r["cost_statistics"] if c["feasible_count"] > 0), None)
                          for r in series_runs]
        known = [g for g in first_feasible if g is not None]
        print(f"  {label} : première génération faisable médiane {median(known) if known else '—'} "
              f"(jamais : {first_feasible.count(None)})")
        totals: dict[str, list[int]] = {}
        for r in series_runs:
            for rate in r["feasibility_rates"]:
                origin = rate["origin"]
                count, before, after = totals.get(origin, [0, 0, 0])
                totals[origin] = [count + rate["count"], before + rate["feasible_before"], after + rate["feasible_after"]]
        for origin, (count, before, after) in totals.items():
            print(f"    {origin} : {count} individus ; faisables avant {before / count:.1%} → après {after / count:.1%}")
        final_diversity = [r["diversity"][-1] for r in series_runs]
        for field in ("genotypic_diversity", "distinct_costs"):
            print(f"    {field} finale (médiane) : {median(d[field] for d in final_diversity):.3g}")
        finals = [r["best"]["cost"]["total"] for r in series_runs]
        print(f"    meilleur coût final : min {min(finals)}, médiane {median(finals)}, max {max(finals)} ; "
              f"infaisables {sum(1 for f in finals if f >= INFEASIBLE_THRESHOLD)}")


if __name__ == "__main__":
    main()
