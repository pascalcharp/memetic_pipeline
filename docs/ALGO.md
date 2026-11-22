```Text
Memetic(NR, NM):

    Initialiser population P

    while not terminé(P):

        for j in NR:
            Parents = SelectParent(P)
            Enfants = Recombine(Parents)
            Enfants = SolveurLocal(Enfants)
            Evaluer(Enfants)
            P = P + Enfants

        for j  in NM:
            i = SelectMutable(P)
            Mute(i)
            i = SolveurLocal(i)
            Evaluer(i)
            P = P + {i}
        P = SelectPop(P)
        if (P a convergé)
            P = Restart(P)
   ```

## Correspondance avec le code

Le moteur est `Memetic` (`src/memetic/engine.py`) ; une exécution est décrite par une `MemeticConfig` (`src/memetic/config.py`), et `build_block_memetic_config` (`src/memetic/assembly.py`) en assemble une avec les vrais composants.

| Pseudo-code | Interface (rôle dans `MemeticConfig`) | Implémentation de l'assemblage de référence |
|---|---|---|
| `Initialiser population P` | `PopulationInitializer` (`initializer`) | `RandomBlockInitializer`, avec ou sans `LocalSolver` |
| `terminé(P)` | `TerminationCriterion` (`termination`) | `GenerationLimit` |
| `SelectParent(P)` | `ParentSelector` (`parent_selector`) | `TournamentSelector` |
| `Recombine(Parents)` | `Crossover` (`crossover`) | `UniformGeneCrossover` |
| `SelectMutable(P)` | `MutableSelector` (`mutable_selector`) | `UniformMutableSelector` |
| `Mute(i)` | `Mutation` (`mutation`) | `ShiftStartMutation` |
| `SolveurLocal(...)` | `LocalSolver` (`local_solver`) | `MiniZincLocalSolver` : CP-SAT, modèle assoupli `horaire_assoupli.mzn` |
| `Evaluer(...)` | `CostEvaluator` (`evaluator`) | `CostEvaluator` |
| `SelectPop(P)` | `SurvivorSelector` (`survivor_selector`) | `PlusSurvivorSelector` ((μ+λ) sans doublons) |
| `P a convergé` | `ConvergenceCriterion` (`convergence`) | `StagnationCriterion` |
| `Restart(P)` | `RestartPolicy` (`restart`) | `EliteRestart` (élite distincte et réinitialisation) |

## Écarts assumés avec le pseudo-code

- **Traitement par lots (D7)** : les boucles `for j in NR` et `for j in NM` ne sont pas faites une itération à la fois. Les `NR × 2` parents sont tirés d'un coup dans P, puis NR tâches indépendantes produisent les enfants, et P = P + enfants à la fin du lot. Même chose pour les NM individus à muter, tirés dans P qui contient déjà les enfants du lot NR. Les tâches passent par un `Executor` et reçoivent chacune leur graine (`derive_task_seeds`) : le résultat ne dépend pas de l'ordre d'exécution, ce qui prépare un futur parallélisme.
- **Évaluation avant et après** : chaque enfant est évalué avant la recherche locale (coût avant) et après (coût après), pour mesurer l'apport du solveur.
- **Observation (D8)** : le moteur émet des événements (`RunStarted`, `LocalSearchDone`, `IndividualCreated`, `GenerationEnded`, `Converged`, `Restarted`, `RunEnded`) vers un `ObservationHub`. Les recherches locales de l'initialisation et du restart sont aussi publiées, pour que la charge du solveur (D10) soit comptée partout.
