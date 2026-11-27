"""Mémétique contre CP-SAT seul sur bench_3, à effort égal (étape 10g).

Usage, depuis la racine du dépôt :

    python -m experiments.analysis.analyze_bench3_cpsat_alone

Lit les résultats du témoin CP-SAT seul (``run_cpsat_alone`` : toutes les solutions intermédiaires, chacune avec
l'effort dépensé jusqu'à elle) et ceux des configurations du mémétique sur bench_3 (séries de Mély, 21 graines
chacune). Pour chaque configuration du mémétique, on prend son effort médian (propagations cumulées, temps de
résolution cumulé) et on regarde le meilleur coût que CP-SAT seul avait trouvé **avec le même effort**.

Les propagations ne dépendent pas de la machine ; le temps de résolution, si (les séries de Mély n'ont pas tourné
sur la même machine que le témoin). On donne les deux.
"""

import json
import statistics
from collections import defaultdict
from collections.abc import Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from experiments.drivers.run_cpsat_alone import CpSatAloneResultKeys
from src.config import ProjectPaths


class AnalysisConstants:
    """Constantes de l'analyse."""

    INSTANCE: str = "bench_3"
    OPTIMUM: int = 16
    CPSAT_PREFIX: str = "bench3_cpsat_"
    RESULTS_GLOB: str = "**/*.json"

    # Configurations recommandées par la synthèse de Mély (synthese_bench2_bench3.md, section 15).
    ECONOMY_LABEL: str = "mémétique économique"
    QUALITY_LABEL: str = "mémétique qualité"

    # Champs du fichier de résultats du mémétique.
    SETTINGS: str = "settings"
    STRATEGIES: str = "strategies"
    BEST: str = "best"
    COST: str = "cost"
    TOTAL: str = "total"
    SOLVER_EFFORT: str = "solver_effort"
    PROPAGATIONS: str = "propagations"
    SOLVE_TIME: str = "solve_time_seconds"
    SEED: str = "master_seed"

    # Champs de settings qui identifient une configuration (la graine exceptée).
    CONFIG_FIELDS: tuple[str, ...] = (
        "population_size", "generations", "crossover_count", "mutation_count", "neighborhood_size",
        "deterministic_time_units", "stagnation_generations", "initial_local_search",
    )
    MUTATION_ROLE: str = "mutation"
    NAME: str = "name"
    MILLION: float = 1e6
    # Nom de la statistique finale de MiniZinc qui correspond à chaque champ d'effort d'une solution.
    FINAL_STAT_NAMES: dict[str, str] = {
        CpSatAloneResultKeys.PROPAGATIONS: "propagations",
        CpSatAloneResultKeys.SOLVE_TIME_SECONDS: "solveTime",
    }
    RUN_ENDED_MARK: str = " (fin du run)"


@dataclass(frozen=True)
class MemeticGroup:
    """Les exécutions (une par graine) d'une configuration du mémétique."""

    key: tuple[Any, ...]
    runs: list[dict[str, Any]]

    def median_cost(self) -> float:
        return statistics.median(run[AnalysisConstants.BEST][AnalysisConstants.COST][AnalysisConstants.TOTAL]
                                 for run in self.runs)

    def costs(self) -> list[int]:
        return [run[AnalysisConstants.BEST][AnalysisConstants.COST][AnalysisConstants.TOTAL] for run in self.runs]

    def median_effort(self, field: str) -> float:
        return statistics.median(run[AnalysisConstants.SOLVER_EFFORT][field] for run in self.runs)


def result_files(root: Path = ProjectPaths.EXPERIMENT_RESULTS_DIR) -> list[Path]:
    return sorted(root.glob(AnalysisConstants.RESULTS_GLOB))


def load_cpsat_runs(paths: Sequence[Path]) -> list[dict[str, Any]]:
    """Les résolutions « CP-SAT seul » sur bench_3."""
    runs = []
    for path in paths:
        if path.name.startswith(AnalysisConstants.CPSAT_PREFIX):
            runs.append(json.loads(path.read_text(encoding="utf-8")))
    return runs


def memetic_key(document: dict[str, Any]) -> tuple[Any, ...]:
    settings = document[AnalysisConstants.SETTINGS]
    mutation = document[AnalysisConstants.STRATEGIES][AnalysisConstants.MUTATION_ROLE][AnalysisConstants.NAME]
    return tuple(settings[field] for field in AnalysisConstants.CONFIG_FIELDS) + (mutation,)


def load_memetic_groups(paths: Sequence[Path]) -> dict[tuple[Any, ...], MemeticGroup]:
    """Les configurations du mémétique sur bench_3, une exécution par graine.

    Certaines configurations ont été refaites dans plusieurs séries de Mély (même réglage, résultats identiques,
    vérifié par sa série de validation) : on garde la première exécution de chaque graine.
    """
    by_key: dict[tuple[Any, ...], dict[int, dict[str, Any]]] = defaultdict(dict)
    for path in paths:
        document = json.loads(path.read_text(encoding="utf-8"))
        if document.get("instance") != AnalysisConstants.INSTANCE or AnalysisConstants.SETTINGS not in document:
            continue
        seed = document[AnalysisConstants.SETTINGS][AnalysisConstants.SEED]
        by_key[memetic_key(document)].setdefault(seed, document)
    return {key: MemeticGroup(key, list(runs.values())) for key, runs in by_key.items()}


def best_at_effort(solutions: Sequence[dict[str, Any]], field: str, effort: float) -> int | None:
    """Le meilleur coût trouvé par CP-SAT avec au plus ``effort`` ; ``None`` s'il n'avait encore rien trouvé."""
    best = None
    for point in solutions:
        if point[field] is not None and point[field] <= effort:
            best = point[CpSatAloneResultKeys.OBJECTIVE]
    return best


def effort_to_reach(solutions: Sequence[dict[str, Any]], field: str, cost: float) -> float | None:
    """L'effort au moment où CP-SAT trouve pour la première fois un coût ≤ ``cost`` ; ``None`` s'il n'y arrive pas."""
    for point in solutions:
        if point[CpSatAloneResultKeys.OBJECTIVE] <= cost:
            return point[field]
    return None


def describe(key: tuple[Any, ...]) -> str:
    population, generations, nr, nm, neighborhood, units, stagnation, initial_ls, mutation = key
    return (f"pop {population}, {generations} gén., NR/NM {nr}/{nm}, voisinage {neighborhood}, budget {units:g}, "
            f"stagnation {stagnation}, RL initiale {initial_ls}, {mutation}")


def run_ended_mark(run: dict[str, Any], field: str, effort: float) -> str:
    """Une marque quand le run de CP-SAT s'est arrêté (limite atteinte) avant l'effort comparé : son coût est alors
    celui de la fin du run, et il pourrait encore baisser avec plus d'effort."""
    final_effort = run[CpSatAloneResultKeys.FINAL_STATISTICS][AnalysisConstants.FINAL_STAT_NAMES[field]]
    return AnalysisConstants.RUN_ENDED_MARK if final_effort < effort else ""


def cost_text(cost: float | None) -> str:
    if cost is None:
        return "aucune solution"
    return f"{cost:g}"


def print_cpsat_summary(runs: Sequence[dict[str, Any]]) -> None:
    keys = CpSatAloneResultKeys
    print("## CP-SAT seul (1 thread)\n")
    print("| Modèle | Graine | Meilleur coût | Prouvé | Solutions | Propagations finales (M) | solveTime final (s) |")
    print("|---|---:|---:|---|---:|---:|---:|")
    for run in sorted(runs, key=lambda r: (r[keys.MODEL], r[keys.SEED])):
        final = run[keys.FINAL_STATISTICS]
        print(f"| {run[keys.MODEL]} | {run[keys.SEED]} | {cost_text(run[keys.BEST_OBJECTIVE])} | "
              f"{run[keys.PROVEN_OPTIMAL]} | {len(run[keys.SOLUTIONS])} | "
              f"{final['propagations'] / AnalysisConstants.MILLION:.0f} | {final['solveTime']:.0f} |")
    print()


def print_comparison(groups: dict[tuple[Any, ...], MemeticGroup], runs: Sequence[dict[str, Any]], field: str,
                     cpsat_field: str, unit: str) -> None:
    keys = CpSatAloneResultKeys
    models = sorted({run[keys.MODEL] for run in runs})
    print(f"## À effort égal : {unit}\n")
    header = "| Configuration du mémétique | Coût médian (min) | Effort médian | " + " | ".join(
        f"CP-SAT {model} au même effort (par graine)" for model in models) + " |"
    print(header)
    print("|---|---:|---:|" + "---|" * len(models))
    for group in sorted(groups.values(), key=lambda g: g.median_effort(field)):
        effort = group.median_effort(field)
        cells = []
        for model in models:
            model_runs = sorted((r for r in runs if r[keys.MODEL] == model), key=lambda r: r[keys.SEED])
            cells.append(", ".join(cost_text(best_at_effort(r[keys.SOLUTIONS], cpsat_field, effort))
                                   + run_ended_mark(r, cpsat_field, effort) for r in model_runs))
        scaled = effort / AnalysisConstants.MILLION if field == AnalysisConstants.PROPAGATIONS else effort
        print(f"| {describe(group.key)} | {group.median_cost():g} ({min(group.costs())}) | {scaled:.0f} | "
              + " | ".join(cells) + " |")
    print()


def print_effort_to_reach(groups: dict[tuple[Any, ...], MemeticGroup], runs: Sequence[dict[str, Any]]) -> None:
    keys = CpSatAloneResultKeys
    print("## Effort de CP-SAT seul pour atteindre le coût médian du mémétique\n")
    print("| Configuration | Coût médian | Effort médian du mémétique (M propagations) | "
          "CP-SAT : propagations pour l'atteindre (M), par graine |")
    print("|---|---:|---:|---|")
    for group in sorted(groups.values(), key=lambda g: g.median_cost()):
        target = group.median_cost()
        cells = []
        for run in sorted(runs, key=lambda r: (r[keys.MODEL], r[keys.SEED])):
            reached = effort_to_reach(run[keys.SOLUTIONS], keys.PROPAGATIONS, target)
            text = "jamais" if reached is None else f"{reached / AnalysisConstants.MILLION:.0f}"
            cells.append(f"{run[keys.MODEL]}/s{run[keys.SEED]} : {text}")
        print(f"| {describe(group.key)} | {target:g} | "
              f"{group.median_effort(AnalysisConstants.PROPAGATIONS) / AnalysisConstants.MILLION:.0f} | "
              + " ; ".join(cells) + " |")
    print()


def main() -> None:
    paths = result_files()
    cpsat_runs = load_cpsat_runs(paths)
    groups = load_memetic_groups(paths)
    print_cpsat_summary(cpsat_runs)
    print_comparison(groups, cpsat_runs, AnalysisConstants.PROPAGATIONS, CpSatAloneResultKeys.PROPAGATIONS,
                     "propagations (millions, indépendantes de la machine)")
    print_comparison(groups, cpsat_runs, AnalysisConstants.SOLVE_TIME, CpSatAloneResultKeys.SOLVE_TIME_SECONDS,
                     "temps de résolution cumulé (s, dépend de la machine)")
    print_effort_to_reach(groups, cpsat_runs)


if __name__ == "__main__":
    main()
