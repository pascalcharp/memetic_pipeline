# Comment faire ?

Guide pratique pour utiliser et modifier le pipeline. Chaque section dit **quels fichiers modifier**, **quelle interface dériver** et donne **au moins un exemple**. Tous les exemples de code ont été exécutés sur `bench_1` le 22 novembre 2026.

Pour savoir ce qui existe déjà avant d'écrire une nouvelle stratégie : [`AVAILABLE_STRATEGIES.md`](AVAILABLE_STRATEGIES.md).

1. [Je veux lancer une expérience](#1-je-veux-lancer-une-expérience)
2. [Je veux faire rouler la boucle mémétique depuis Python](#2-je-veux-faire-rouler-la-boucle-mémétique-depuis-python)
3. [Je veux modifier la probabilité de crossover](#3-je-veux-modifier-la-probabilité-de-crossover)
4. [Je veux modifier la probabilité de mutation](#4-je-veux-modifier-la-probabilité-de-mutation)
5. [Je veux créer un nouveau crossover](#5-je-veux-créer-un-nouveau-crossover)
6. [Je veux créer un nouvel opérateur de mutation](#6-je-veux-créer-un-nouvel-opérateur-de-mutation)
7. [Je veux modifier la stratégie de sélection de la population](#7-je-veux-modifier-la-stratégie-de-sélection-de-la-population)
8. [Je veux une autre stratégie de redémarrage](#8-je-veux-une-autre-stratégie-de-redémarrage)
9. [Je veux modifier les options de CP-SAT pour ma prochaine expérience](#9-je-veux-modifier-les-options-de-cp-sat-pour-ma-prochaine-expérience)
10. [Je veux essayer la boucle avec un autre solveur sur MiniZinc](#10-je-veux-essayer-la-boucle-avec-un-autre-solveur-sur-minizinc)
11. [Je veux modifier l'encodage des génomes](#11-je-veux-modifier-lencodage-des-génomes)

---

## 0. Le principe : tout passe par `MemeticConfig`

Le moteur `Memetic` (`src/memetic/engine.py`) ne connaît que des **interfaces**. Une exécution est entièrement décrite par une `MemeticConfig` (`src/memetic/config.py`) : un objet par rôle du pseudo-code (initialiseur, sélecteurs, croisement, mutation, `LocalSolver`, évaluateur, sélection des survivants, convergence, restart, arrêt) et les paramètres scalaires (taille de la population, NR, NM, graine maître). La correspondance entre le pseudo-code et ces rôles est dans [`ALGO.md`](ALGO.md).

`build_block_memetic_config(instance, settings, dispatcher)` (`src/memetic/assembly.py`) construit la **configuration de référence**, avec les vrais composants. Ses paramètres numériques sont dans `AssemblySettings`, et leurs valeurs par défaut dans `AssemblyDefaults`.

Pour brancher un composant à vous, deux façons de faire :

- **Pour un essai** : partir de la configuration de référence et remplacer un rôle avec `dataclasses.replace`. Rien à modifier dans le dépôt, sauf votre nouvelle classe.

  ```python
  import dataclasses
  config = dataclasses.replace(build_block_memetic_config(instance, settings), crossover=MonCroisement())
  ```

- **Pour un choix durable** : modifier `build_block_memetic_config` (et ajouter un champ à `AssemblySettings` et une valeur par défaut à `AssemblyDefaults` si le composant a des paramètres). Les tests `tests/test_integration.py` (classe `TestAssembly`) vérifient les composants de l'assemblage : à mettre à jour avec lui.

**Attention aux objets partagés.** Dans la configuration de référence, le même `LocalSolver` sert au moteur **et** à l'initialiseur, et le même initialiseur et le même évaluateur servent au restart (`EliteRestart`). Si vous remplacez le `LocalSolver`, remplacez aussi l'initialiseur et le restart (voir la [section 10](#10-je-veux-essayer-la-boucle-avec-un-autre-solveur-sur-minizinc)).

**Règles communes à toute nouvelle classe** (détail dans [`CLAUDE.md`](../CLAUDE.md)) :
- classe documentée, annotations de type, aucun nombre magique : les constantes vont dans une classe de constantes (par exemple `OperatorDefaults`) ou une constante de classe ;
- exceptions sur mesure, avec leurs gabarits de messages dans la classe `...Messages` du module (espaces réservés nommés, jamais de f-strings) ;
- **ne jamais modifier les entrées** (génomes, individus, populations) : rendre de nouveaux objets (D7) ;
- **tout l'aléa vient du `random.Random` reçu** en argument : jamais le module `random` global, sinon la reproductibilité est perdue ;
- des tests `unittest` dans le fichier de tests du module (`tests/test_operators.py`, `tests/test_population.py`, etc.) : cas nominaux et cas limites.

---

## 1. Je veux lancer une expérience

**Fichiers** : un fichier de configuration à créer dans `experiments/config/` ; aucun code à modifier.

**Où sont les choses.** `src/` est le **cœur** (modèle, algorithme génétique, mémétique, observabilité). `experiments/` contient ce qui sert à l'**exploiter** :

| Chemin | Contenu |
|---|---|
| `experiments/drivers/` | scripts de pilotage, dont `run_experiment.py` |
| `experiments/analysis/` | scripts d'analyse des résultats (à venir, étape 10b) |
| `experiments/config/` | configurations JSON des expériences |
| `experiments/results/<AAAA-MM-JJ>/` | fichiers de résultats JSON, un répertoire par jour (versionnés) |
| `experiments/EXPLOG.md` | journal des expériences : une entrée par exécution, ajoutée automatiquement |

**1. Écrire la configuration**, par exemple `experiments/config/mon_essai.json`. Le nom du fichier, sans extension, devient le nom de l'expérience :

```json
{
  "description": "Ce que l'expérience cherche à montrer, en une ou deux phrases.",
  "instance": "bench_3",
  "settings": {"population_size": 10, "crossover_count": 3, "mutation_count": 2, "generations": 20, "master_seed": 1}
}
```

| Clé | Obligatoire | Contenu |
|---|---|---|
| `description` | oui | texte lisible, recopié dans les résultats et dans `EXPLOG.md` |
| `instance` | oui | nom d'un fichier de `data/` sans extension (`bench_1` … `bench_5`) |
| `settings` | non | paramètres de l'assemblage de référence (`AssemblySettings`) ; les champs absents gardent leur valeur par défaut |

Paramètres de `settings` et valeurs par défaut (`AssemblyDefaults`, `src/memetic/assembly.py`) :

| Paramètre | Type | Défaut | Rôle |
|---|---|---|---|
| `population_size` | entier | 6 | taille de la population |
| `crossover_count` | entier | 2 | NR : croisements par génération |
| `mutation_count` | entier | 2 | NM : mutations par génération |
| `generations` | entier | 5 | nombre de générations (critère d'arrêt) |
| `master_seed` | entier | 0 | graine maître, d'où dérivent toutes les graines (D7) |
| `tournament_size` | entier | 2 | taille du tournoi (sélection des parents et des mutables) |
| `stagnation_generations` | entier | 10 | générations sans amélioration avant un restart |
| `elite_count` | entier | 1 | individus gardés au restart |
| `neighborhood_size` | entier | 1 | employés libérés par la recherche locale |
| `deterministic_time_units` | réel | 5.0 | budget de CP-SAT par appel (limite déterministe) |
| `initial_local_search` | booléen | `true` | passer aussi les individus initiaux et ceux du restart par le `LocalSolver` |

Une clé inconnue, une clé obligatoire absente, une valeur du mauvais type ou une instance introuvable sont refusées **avant toute exécution** (`InvalidExperimentConfigError`, avec le chemin et la clé en cause dans le message). Les domaines (par exemple une taille au moins 1) sont vérifiés à la construction du moteur.

**2. Commiter le code.** `git_dirty` vaut `true` si la copie de travail a des modifications non commitées au lancement (hors `experiments/results/` et `EXPLOG.md`). Le résultat ne peut alors pas être reproduit à partir du seul commit noté, et l'entrée d'`EXPLOG.md` le signale en gras.

**3. Lancer**, depuis la racine du dépôt :

```bash
python -m experiments.drivers.run_experiment experiments/config/mon_essai.json
```

Toujours avec `python -m` et depuis la racine : `python experiments/drivers/run_experiment.py` échoue (`ModuleNotFoundError: No module named 'src'`), car les imports partent de la racine. Dans PyCharm, le répertoire de travail de la configuration d'exécution doit être la racine.

| Paramètre | Rôle | Par défaut |
|---|---|---|
| `CONFIG` (obligatoire) | le fichier de configuration | — |
| `--results-dir` | le répertoire du fichier de résultats, créé au besoin | `experiments/results/<AAAA-MM-JJ>/`, la date du lancement |
| `--log` | le journal des expériences, créé avec son en-tête s'il n'existe pas | `experiments/EXPLOG.md` |

Pour un essai qu'on ne veut pas garder, envoyer les résultats et le journal ailleurs : `--results-dir /tmp/essai --log /tmp/essai/EXPLOG.md`.

À la fin, le script affiche une ligne de résumé :

```text
Coût obtenu : 94 ; effort cumulé du solveur : 35 appels. Résultats : experiments/results/2026-11-22/integration_bench1_151611.json
```

En cas d'erreur (configuration refusée, fichier de résultats déjà présent), il s'arrête avec l'exception et un code de sortie non nul, sans écrire de fichier de résultats ni d'entrée au journal.

**4. Ce qui est produit.**

- **Le fichier de résultats** `<nom de l'expérience>_<HHMMSS>.json`, jamais écrasé (`ResultsFileExistsError` si le nom existe déjà). Il contient :
  - la configuration complète (`description`, `config_path`, `instance`, `settings` avec les valeurs par défaut appliquées) ;
  - la provenance : `started_at`, `duration_seconds`, `git_commit`, `git_dirty`, versions de Python et des paquets ;
  - `best` : le coût décomposé (`cost`, dont `total` et `is_feasible`) et l'horaire (`schedule`) du meilleur individu ;
  - `generations` et `restarts` ;
  - `solver_effort` : l'effort cumulé du solveur (D10 : appels, échecs, propagations, temps de résolution), initialisation et restarts compris ;
  - `feasibility_rates` : taux de faisabilité cumulés avant et après la recherche locale, par origine (initialisation, croisement, mutation, restart) et par opérateur ;
  - `cost_statistics` et `diversity` : une entrée par génération.
- **Une entrée dans `EXPLOG.md`** : description, chemins de la configuration et des résultats, coût obtenu, effort cumulé du solveur, durée, commit et état de la copie de travail.

**5. Commiter les résultats et le journal** avec un message qui dit ce que l'expérience montre. Les résultats sont versionnés : c'est ce qui permet de citer une expérience dans le rapport.

**Reproductibilité** : même configuration et même commit ⇒ même résultat, car CP-SAT tourne en monothread sous limite déterministe. Le temps de résolution (`solve_time`) varie d'une machine à l'autre ; pour comparer l'effort, utiliser les appels et les propagations.

**Depuis Docker.** Monter le dépôt pour que les résultats et le journal arrivent sur la machine hôte :

```bash
docker run --rm -v "$PWD":/app memetic-pipeline python -m experiments.drivers.run_experiment experiments/config/mon_essai.json
```

L'image ne contient pas Git : `git_commit` y vaut `inconnu` et `git_dirty`, `null`. L'heure est celle du conteneur (UTC), ce qui change le répertoire du jour et le nom du fichier. Pour une expérience à citer, lancer plutôt en local.

**Ce que `run_experiment` ne fait pas (encore).** Il utilise toujours l'assemblage de référence (`build_block_memetic_config`) : on ne choisit pas les opérateurs, l'encodage ou le solveur dans la configuration (prévu à l'étape 10, via le registre). Pour essayer un autre composant, passer par Python ([section 2](#2-je-veux-faire-rouler-la-boucle-mémétique-depuis-python), puis sections 3 à 11) ; pour un choix durable, modifier `build_block_memetic_config` ([section 0](#0-le-principe--tout-passe-par-memeticconfig)), et `run_experiment` en profite.

---

## 2. Je veux faire rouler la boucle mémétique depuis Python

**Fichiers** : aucun à modifier.

Pour une expérience à citer (configuration JSON, résultats versionnés, entrée d'`EXPLOG.md`), passer par `run_experiment` : [section 1](#1-je-veux-lancer-une-expérience). Cette section-ci lance le moteur depuis Python, pour un essai ou pour brancher un composant à vous.

Depuis la racine du dépôt (les imports partent de `src.`) :

```python
from src.config import ProjectPaths
from src.memetic.assembly import AssemblySettings, build_block_memetic_config
from src.memetic.engine import Memetic
from src.utils.io import load_instance

instance = load_instance(ProjectPaths.DATA_DIR / "bench_1.json")
settings = AssemblySettings(generations=4, master_seed=7, stagnation_generations=1)
result = Memetic(build_block_memetic_config(instance, settings)).run()
print(result.best.cost.total, result.generations, result.restarts)   # 94 4 1
```

`result` est un `MemeticResult` : `best` (le meilleur individu : `best.genome`, `best.horaire`, `best.cost`), `population` (la population finale), `generations` et `restarts`.

**Paramètres** (`AssemblySettings`) : `population_size`, `crossover_count` (NR), `mutation_count` (NM), `generations`, `master_seed`, `tournament_size`, `stagnation_generations`, `elite_count`, `neighborhood_size` (employés libérés par la recherche locale), `deterministic_time_units` (budget de CP-SAT par appel), `initial_local_search` (passer aussi les individus initiaux par le `LocalSolver`).

**Reproductibilité** : même graine maître et mêmes paramètres ⇒ même résultat, à condition que CP-SAT reste en monothread sous limite déterministe (le cas de l'assemblage de référence).

**Exécution mesurée, avec les résultats sur disque.** Le troisième argument de `build_block_memetic_config` est un `ObservationHub` (`src/observability/hub.py`) : des **collecteurs** calculent des mesures à partir des événements du moteur, des **destinations** les écrivent. `RunDirectory` crée `results/<expérience>/<run_id>/` (ignoré par Git).

```python
import dataclasses
from src.observability.collectors import (
    CostStatisticsCollector, DiversityCollector, FeasibilityRateCollector, RecordNames, SolverEffortCollector,
)
from src.observability.hub import ObservationHub
from src.observability.logging_config import configure_logging
from src.observability.run_directory import RunDirectory
from src.observability.sinks import CsvSink, JsonlSink

run = RunDirectory.create("premier-essai")
run.write_config(seed=settings.master_seed, parameters=dataclasses.asdict(settings))
configure_logging(run_log=run.run_log_path)
hub = ObservationHub(
    collectors=(CostStatisticsCollector(), DiversityCollector(instance.period_count),
                FeasibilityRateCollector(), SolverEffortCollector()),
    sinks=(JsonlSink(run.events_path), CsvSink(run.generations_path, RecordNames.COST_STATISTICS)),
)
result = Memetic(build_block_memetic_config(instance, settings, hub)).run()
```

Le répertoire contient alors `config.json` (paramètres, graine, commit Git, versions), `events.jsonl` (tous les enregistrements), `generations.csv` (statistiques du coût, une ligne par génération) et `run.log`. Le moteur ferme le hub à la fin de `run`. Les collecteurs disponibles et leurs champs sont documentés dans `src/observability/collectors.py`.

---

## 3. Je veux modifier la probabilité de crossover

**À savoir d'abord** : le moteur n'a **pas** de probabilité de croisement. Il suit le pseudo-code (`for j in NR`) : à chaque génération, il fait exactement **NR croisements** (`crossover_count`), chacun sur `parent_count()` parents tirés par le `ParentSelector`, et chacun produit deux enfants avec `UniformGeneCrossover`. Avec une population de μ individus, 2·NR/μ joue le rôle d'un « taux de croisement » : le nombre d'enfants produits par individu et par génération.

**Option A : changer NR.** Aucun fichier à modifier :

```python
settings = AssemblySettings(crossover_count=4)          # 4 croisements, 8 enfants par génération
```

Pour changer la valeur par défaut : `AssemblyDefaults.CROSSOVER_COUNT` dans `src/memetic/assembly.py`. NR peut être nul (pas de croisement), mais pas en même temps que NM (`MemeticConfig.validate`).

**Option B : une vraie probabilité p_c.** Envelopper le croisement dans un `Crossover` qui ne recombine qu'avec la probabilité p_c, et rend sinon des copies des parents.

- **Fichier** : `src/ga/operators.py` (avec ses tests dans `tests/test_operators.py`) ; la probabilité par défaut va dans `OperatorDefaults`.
- **Interface** : `Crossover[G]`.

```python
class ProbabilisticBlockCrossover(Crossover[BlockGenome]):
    """Applique ``inner`` avec la probabilité ``probability`` ; sinon, rend des copies des parents."""

    def __init__(self, inner: Crossover[BlockGenome], probability: float) -> None:
        self.inner = inner
        self.probability = probability

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def parent_count(self) -> int:
        return self.inner.parent_count()

    def recombine(self, parents: Sequence[BlockGenome], rng: random.Random) -> tuple[BlockGenome, ...]:
        if rng.random() < self.probability:
            return self.inner.recombine(parents, rng)
        return tuple(parents)

config = dataclasses.replace(
    build_block_memetic_config(instance, settings),
    crossover=ProbabilisticBlockCrossover(UniformGeneCrossover(), probability=0.8),
)
```

Deux conséquences à connaître :
- les copies passent quand même par le `LocalSolver` : la charge du solveur ne baisse pas avec p_c ;
- dans les événements, l'opérateur s'appelle `ProbabilisticBlockCrossover` (le nom de la classe du croisement de la configuration).

---

## 4. Je veux modifier la probabilité de mutation

**À savoir d'abord** : comme pour le croisement, il n'y a pas de probabilité de mutation dans le moteur. À chaque génération, il fait exactement **NM mutations** (`mutation_count`) : le `MutableSelector` tire NM individus, et chacun est muté une fois. NM/μ joue le rôle d'un taux de mutation par individu et par génération. De plus, les opérateurs de mutation existants modifient **un seul gène** (un seul employé) par appel.

**Option A : changer NM** :

```python
settings = AssemblySettings(mutation_count=4)
```

Valeur par défaut : `AssemblyDefaults.MUTATION_COUNT` dans `src/memetic/assembly.py`.

**Option B : changer l'intensité d'une mutation.** Les amplitudes sont des constantes de `OperatorDefaults` (`src/ga/operators.py`) : `MIN_SHIFT_AMPLITUDE` et `MAX_SHIFT_AMPLITUDE` pour `ShiftStartMutation`, `MIN_BOUNDARY_TRANSFER` et `MAX_BOUNDARY_TRANSFER` pour `BlockBoundaryMutation`. Les modifier change tous les usages : les tests de `tests/test_operators.py` doivent rester verts.

**Option C : une vraie probabilité p_m.**
- *Par individu* : même patron que le croisement probabiliste de la section 3, avec l'interface `Mutation[G]` :

  ```python
  class ProbabilisticBlockMutation(Mutation[BlockGenome]):
      """Applique ``inner`` avec la probabilité ``probability`` ; sinon, rend le génome inchangé."""

      def __init__(self, inner: Mutation[BlockGenome], probability: float) -> None:
          self.inner = inner
          self.probability = probability

      @classmethod
      def encoding_type(cls) -> type[Encoding[BlockGenome]]:
          return BlockEncoding

      def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
          if rng.random() < self.probability:
              return self.inner.mutate(genome, rng)
          return genome
  ```

- *Par gène* (chaque employé muté avec la probabilité p_m) : écrire un nouvel opérateur qui parcourt les gènes et tire, pour chacun, `rng.random() < p_m` (voir la [section 6](#6-je-veux-créer-un-nouvel-opérateur-de-mutation) pour la structure d'un opérateur).

---

## 5. Je veux créer un nouveau crossover

**Fichiers** :
- `src/ga/operators.py` : la nouvelle classe, ses constantes dans `OperatorDefaults`, ses éventuelles exceptions (dérivées de `OperatorError`) et leurs messages dans `OperatorMessages` ;
- `tests/test_operators.py` : ses tests ;
- pour l'adopter durablement : `build_block_memetic_config` dans `src/memetic/assembly.py`.

**Interface** : `Crossover[G]` (`src/ga/operators.py`), avec trois méthodes :

| Méthode | Contrat |
|---|---|
| `encoding_type()` (méthode de classe) | le type d'encodage dont l'opérateur manipule les génomes ; `MemeticConfig.validate` refuse un opérateur incompatible avec l'encodage (`IncompatibleOperatorError`) |
| `parent_count()` | le nombre de parents attendus ; le moteur tire `NR × parent_count()` parents par génération |
| `recombine(parents, rng)` | rend un tuple d'enfants (autant qu'on veut) ; lève `WrongParentCountError` si `len(parents) != parent_count()` ; ne modifie pas les parents |

Avec `BlockEncoding`, un génome est un tuple de `BlockGene`, un par employé ; un gène est un quart complet (début et quatre blocs d'activité). Échanger des gènes entiers garde chaque quart faisable.

**Exemple : croisement à un point sur les gènes.**

```python
class OnePointGeneCrossover(Crossover[BlockGenome]):
    """Croisement à un point : les employés avant le point viennent d'un parent, ceux d'après de l'autre.
    Rend deux enfants complémentaires. Chaque quart reste faisable."""

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def parent_count(self) -> int:
        return OperatorDefaults.CROSSOVER_PARENT_COUNT

    def recombine(self, parents: Sequence[BlockGenome], rng: random.Random) -> tuple[BlockGenome, ...]:
        if len(parents) != self.parent_count():
            raise WrongParentCountError(OperatorMessages.WRONG_PARENT_COUNT.format(
                operator=type(self).__name__, expected=self.parent_count(), found=len(parents)
            ))
        first, second = parents
        cut = rng.randint(0, len(first))
        return first[:cut] + second[cut:], second[:cut] + first[cut:]
```

Pour l'essayer :

```python
config = dataclasses.replace(build_block_memetic_config(instance, settings), crossover=OnePointGeneCrossover())
result = Memetic(config).run()
```

**Tests à écrire au minimum** (voir ceux de `UniformGeneCrossover` dans `tests/test_operators.py`) : enfants structurellement faisables (`FeasibilityChecker(instance).violations(encoding.decode(enfant)) == []`), parents non modifiés, même graine ⇒ mêmes enfants, mauvais nombre de parents ⇒ `WrongParentCountError`, cas limites (parents identiques, un seul employé).

---

## 6. Je veux créer un nouvel opérateur de mutation

**Fichiers** : les mêmes que pour un croisement : `src/ga/operators.py`, `tests/test_operators.py`, et `src/memetic/assembly.py` pour l'adopter durablement.

**Interface** : `Mutation[G]` (`src/ga/operators.py`) :

| Méthode | Contrat |
|---|---|
| `encoding_type()` (méthode de classe) | le type d'encodage manipulé |
| `mutate(genome, rng)` | rend un **nouveau** génome ; ne modifie pas `genome` ; un génome vide est une erreur d'appel (`EmptyGenomeError`) |

Si l'opérateur a besoin de l'instance (plage utile, nombre d'activités), il la reçoit à la construction, comme `ShiftStartMutation(instance)`. Un opérateur peut produire un génome infaisable (D6) : le `LocalSolver` le réparera, mais mieux vaut l'éviter.

**Exemple : échanger les activités de deux blocs d'un même quart.** Les durées et les jalons ne changent pas, donc le quart reste faisable.

```python
class BlockActivitySwapMutation(Mutation[BlockGenome]):
    """Échange les activités de deux blocs du quart d'un employé tiré au hasard ; les durées sont conservées.
    Sans effet si les deux blocs tirés ont la même activité (toujours le cas avec une seule activité)."""

    BLOCKS_SWAPPED: int = 2

    @classmethod
    def encoding_type(cls) -> type[Encoding[BlockGenome]]:
        return BlockEncoding

    def mutate(self, genome: BlockGenome, rng: random.Random) -> BlockGenome:
        if len(genome) == 0:
            raise EmptyGenomeError(OperatorMessages.EMPTY_GENOME.format(operator=type(self).__name__))
        index = rng.randrange(len(genome))
        gene = genome[index]
        first, second = rng.sample(range(len(gene.blocks)), self.BLOCKS_SWAPPED)
        blocks = list(gene.blocks)
        blocks[first] = ActivityBlock(activity=gene.blocks[second].activity, duration=gene.blocks[first].duration)
        blocks[second] = ActivityBlock(activity=gene.blocks[first].activity, duration=gene.blocks[second].duration)
        mutated = list(genome)
        mutated[index] = BlockGene(start=gene.start, blocks=tuple(blocks))
        return tuple(mutated)

config = dataclasses.replace(build_block_memetic_config(instance, settings), mutation=BlockActivitySwapMutation())
```

**À éviter** : une mutation qui échange les quarts de deux employés. Les employés sont interchangeables : l'horaire, donc le coût, ne change pas.

**Tests à écrire au minimum** : génome muté structurellement faisable, entrée non modifiée, même graine ⇒ même résultat, génome vide ⇒ `EmptyGenomeError`, cas limites (une seule activité, quart en bordure de la plage utile, blocs à la durée minimale).

---

## 7. Je veux modifier la stratégie de sélection de la population

Trois rôles de la configuration sont des sélections :

| Rôle (`MemeticConfig`) | Ligne du pseudo-code | Interface | Fichier | Implémentation de référence |
|---|---|---|---|---|
| `survivor_selector` | `P = SelectPop(P)` | `SurvivorSelector[G]` | `src/ga/population.py` | `PlusSurvivorSelector` : (μ+λ) sans doublons ; variante `DeathPenaltySurvivorSelector` (les faisables d'abord) |
| `parent_selector` | `Parents = SelectParent(P)` | `ParentSelector[G]` | `src/ga/selection.py` | `TournamentSelector(size)` |
| `mutable_selector` | `i = SelectMutable(P)` | `MutableSelector[G]` | `src/ga/selection.py` | `UniformMutableSelector` |

**Pour changer de stratégie existante**, aucune classe à écrire :

```python
from src.ga.population import DeathPenaltySurvivorSelector
config = dataclasses.replace(build_block_memetic_config(instance, settings),
                             survivor_selector=DeathPenaltySurvivorSelector())
settings = AssemblySettings(tournament_size=4)          # pression de sélection des parents
```

**Pour une nouvelle stratégie de `SelectPop`** : dériver `SurvivorSelector[G]` dans `src/ga/population.py`, tests dans `tests/test_population.py`. Une seule méthode, `select(population, size, rng)`, qui rend `size` survivants. Contrat :
- appeler `check_selectable(population, size)` (`src/ga/selection.py`) en premier : taille invalide, population vide et individu non évalué lèvent les exceptions communes ;
- rendre **exactement** `size` individus (le moteur et les collecteurs supposent une population de taille fixe) ;
- ne pas modifier `population` ;
- **garder le meilleur individu** : sans élitisme, le coût du meilleur peut remonter, et `test_givenRun_whenFinished_thenBestCostNeverIncreases` (`tests/test_integration.py`) échouera.

**Exemple : tournoi élitiste.**

```python
class ElitistTournamentSurvivorSelector[G](SurvivorSelector[G]):
    """Garde le meilleur individu, puis remplit la population par tournois de ``tournament_size`` (avec remise)."""

    def __init__(self, tournament_size: int) -> None:
        self.tournament_size = tournament_size

    def select(self, population: Sequence[Individu[G]], size: int, rng: random.Random) -> tuple[Individu[G], ...]:
        check_selectable(population, size)
        best = min(population, key=lambda individu: individu.cost.total)
        survivors = [best]
        while len(survivors) < size:
            contenders = [rng.choice(population) for _ in range(self.tournament_size)]
            survivors.append(min(contenders, key=lambda individu: individu.cost.total))
        return tuple(survivors)

config = dataclasses.replace(build_block_memetic_config(instance, settings),
                             survivor_selector=ElitistTournamentSurvivorSelector(tournament_size=3))
```

Ce sélecteur accepte les doublons, contrairement à `PlusSurvivorSelector` : la diversité baisse plus vite. Le `DiversityCollector` permet de le mesurer.

**Pour un nouveau sélecteur de parents ou d'individus à muter** : dériver `ParentSelector[G]` ou `MutableSelector[G]` dans `src/ga/selection.py`, tests dans `tests/test_selection.py`. Même méthode `select(population, count, rng)`, qui tire `count` individus **avec remise** en un seul appel (le moteur tire tous les parents d'une génération d'un coup, D7), après `check_selectable`.

---

## 8. Je veux une autre stratégie de redémarrage

Le redémarrage met en jeu deux rôles :

| Rôle (`MemeticConfig`) | Ligne du pseudo-code | Interface | Implémentation de référence |
|---|---|---|---|
| `convergence` | `if (P a convergé)` | `ConvergenceCriterion[G]` | `StagnationCriterion(generations)` : le meilleur coût n'a pas baissé depuis G générations |
| `restart` | `P = Restart(P)` | `RestartPolicy[G]` | `EliteRestart(initializer, evaluator, elite_count)` : garde jusqu'à k meilleurs individus distincts, régénère le reste |

**Fichiers** : `src/ga/population.py` (classe, constantes dans `PopulationDefaults`, exceptions dérivées de `PopulationError`), `tests/test_population.py`, et `src/memetic/assembly.py` pour l'adopter durablement.

**Interface `RestartPolicy[G]`** : une méthode, `restart(population, rng)`, qui rend un `RestartResult(elite, newcomers, searches)` :
- `elite` : les individus gardés, tels quels ;
- `newcomers` : les nouveaux individus, **évalués** (`individu.with_cost(evaluator.evaluate(individu.horaire))`) ;
- `searches` : les recherches locales faites pour obtenir les nouveaux. Si vous utilisez un `PopulationInitializer`, transmettez `InitializationResult.searches` : le moteur publie un `LocalSearchDone` pour chacune, et la charge du solveur (D10) est comptée. Les oublier fausse les mesures de l'étape 10 ;
- `len(elite) + len(newcomers)` doit égaler `len(population)` ; ne pas modifier `population`.

Le moteur émet ensuite un `IndividualCreated` (origine `RESTART`) par nouvel individu, appelle `convergence.reset()` et utilise `result.population` (l'élite, puis les nouveaux).

**Exemple : garder la meilleure moitié.**

```python
class PartialRestart[G](RestartPolicy[G]):
    """Garde la fraction ``kept_fraction`` des meilleurs individus (au moins un) et régénère le reste."""

    def __init__(self, initializer: PopulationInitializer[G], evaluator: CostEvaluator, kept_fraction: float) -> None:
        self.initializer = initializer
        self.evaluator = evaluator
        self.kept_fraction = kept_fraction

    def restart(self, population: Sequence[Individu[G]], rng: random.Random) -> RestartResult[G]:
        ranked = sorted(population, key=lambda individu: individu.cost.total)
        kept_count = max(1, int(len(ranked) * self.kept_fraction))
        elite = tuple(ranked[:kept_count])
        initialization = self.initializer.initialize(len(population) - kept_count, rng)
        newcomers = tuple(
            individu.with_cost(self.evaluator.evaluate(individu.horaire)) for individu in initialization.individuals
        )
        return RestartResult(elite=elite, newcomers=newcomers, searches=initialization.searches)

base = build_block_memetic_config(instance, settings)
config = dataclasses.replace(base, restart=PartialRestart(base.initializer, base.evaluator, kept_fraction=0.5))
```

Dans une version durable, le `1` et le `0.5` deviennent des constantes de `PopulationDefaults`, et `kept_fraction` est validé à la construction (exception dérivée de `PopulationError`). Attention aussi au cas `kept_count == len(population)` : `initialize` refuse une taille nulle (`InvalidPopulationSizeError`), il faut alors rendre `RestartResult(elite=elite, newcomers=())` sans l'appeler, comme le fait `EliteRestart`.

**Pour changer quand on redémarre** : `AssemblySettings(stagnation_generations=...)`, ou une nouvelle `ConvergenceCriterion[G]` (par exemple sur la diversité). Elle a deux méthodes : `has_converged(population)`, appelée une fois par génération après `SelectPop`, et `reset()`, appelée après chaque restart pour oublier l'historique.

---

## 9. Je veux modifier les options de CP-SAT pour ma prochaine expérience

Les options d'une résolution sont dans `SolverOptions` (`src/memetic/solver.py`) : `limit` (limite d'effort), `seed` et `threads`. `CpSatAdapter.solver_arguments` les traduit en arguments pour MiniZinc.

**Le budget par appel** : aucun fichier à modifier.

```python
settings = AssemblySettings(deterministic_time_units=2.0)
```

L'unité est le temps déterministe de CP-SAT (`max_deterministic_time`) : environ une seconde de calcul, mais reproductible.

**La graine, le nombre de threads ou une limite en temps mural** : l'assemblage de référence ne construit que `SolverOptions(limit=DeterministicTimeLimit(...))`. Modifier cette ligne dans `build_block_memetic_config` (ou construire votre propre `MiniZincLocalSolver`, voir la [section 10](#10-je-veux-essayer-la-boucle-avec-un-autre-solveur-sur-minizinc)) :

```python
from src.memetic.solver import CpSatAdapter, DeterministicTimeLimit, ModelVariants, SolverOptions, WallTimeLimit

options = SolverOptions(limit=DeterministicTimeLimit(2.0), seed=3, threads=1)
adapter = CpSatAdapter(options, model=ModelVariants.RELAXED)
```

- `threads > 1` ou `WallTimeLimit(seconds)` rendent les résultats **non reproductibles** (D7, D10) : deux exécutions de même graine diffèrent, et les tests de reproductibilité ne s'appliquent plus.
- `model=ModelVariants.REFERENCE` résout le modèle original, à couverture dure (D12) : un sous-problème qui viole « au moins un employé par activité » devient insatisfiable.

**Un autre paramètre de CP-SAT** (n'importe quel champ de `SatParameters`, par exemple `linearization_level`) : dériver `CpSatAdapter` et ajouter le paramètre à la liste `--params` que construit `solver_arguments`.

- **Fichier** : `src/memetic/solver.py` (le nom du paramètre en constante dans `CpSatFlags`), tests dans `tests/test_solver.py`.
- **Exemple** :

```python
class TunedCpSatAdapter(CpSatAdapter):
    """CP-SAT avec des paramètres ``SatParameters`` supplémentaires (nom → valeur)."""

    def __init__(self, extra_parameters: dict[str, Any], options: SolverOptions = SolverOptions(),
                 model: ModelVariant = ModelVariants.RELAXED) -> None:
        super().__init__(options=options, model=model)
        self.extra_parameters = extra_parameters

    def solver_arguments(self) -> dict[str, Any]:
        arguments = super().solver_arguments()
        extra = CpSatFlags.PARAMETER_SEPARATOR.join(
            CpSatFlags.PARAMETER_TEMPLATE.format(name=name, value=value) for name, value in self.extra_parameters.items()
        )
        arguments[CpSatFlags.FZN_FLAGS_OPTION] += CpSatFlags.PARAMETER_SEPARATOR + extra
        return arguments

adapter = TunedCpSatAdapter({"linearization_level": 2}, SolverOptions(limit=DeterministicTimeLimit(2.0), seed=3))
adapter.solver_arguments()
# {'processes': 1, 'fzn-flags': '--params random_seed:3,max_deterministic_time:2.0,linearization_level:2'}
```

Puis brancher `adapter` dans un `MiniZincLocalSolver`, comme à la section 10.

---

## 10. Je veux essayer la boucle avec un autre solveur sur MiniZinc

**Fichiers** : `src/memetic/solver.py` (le nouvel adaptateur ; l'identifiant du solveur en constante dans `SolverIds`, les mots-clés de minizinc-python dans `MiniZincPythonArguments`), tests dans `tests/test_solver.py`, et `src/memetic/assembly.py` pour l'adopter durablement.

**Interface** : `SolverAdapter` (`src/memetic/solver.py`). La résolution elle-même (`solve`) est commune à tous les solveurs ; une sous-classe ne fournit que trois choses :

| Méthode | Rôle |
|---|---|
| `solver_id()` (méthode de classe) | l'identifiant du solveur dans MiniZinc (`minizinc --solvers` : `gecode`, `chuffed`, `highs`, …) ; s'il est absent, la construction lève `SolverNotAvailableError` |
| `supported_limits()` (méthode de classe) | les types de limites d'effort compris ; une autre limite lève `UnsupportedLimitError` à la construction |
| `solver_arguments()` | la traduction de `self.options` en arguments de `minizinc.Instance.solve` (`processes`, `time_limit`, `random_seed`, options propres au solveur) |

Gecode, Chuffed et HiGHS sont dans l'image Docker et dans le *bundle* MiniZinc.

**Exemple : Gecode.**

```python
from datetime import timedelta

class GecodeAdapter(SolverAdapter):
    """Adaptateur pour Gecode : temps mural seulement (résultats non reproductibles)."""

    @classmethod
    def solver_id(cls) -> str:
        return "gecode"                          # constante de SolverIds dans une version durable

    @classmethod
    def supported_limits(cls) -> tuple[type[EffortLimit], ...]:
        return (WallTimeLimit,)

    def solver_arguments(self) -> dict[str, Any]:
        return {
            MiniZincPythonArguments.THREADS: self.options.threads,
            MiniZincPythonArguments.TIME_LIMIT: timedelta(seconds=self.options.limit.seconds),
            "random_seed": self.options.seed,     # constante de MiniZincPythonArguments dans une version durable
        }
```

**Le brancher** : l'adaptateur va dans un `MiniZincLocalSolver`, et ce `LocalSolver` doit remplacer celui du moteur, de l'initialiseur **et** du restart (voir l'encadré « objets partagés » de la [section 1](#0-le-principe--tout-passe-par-memeticconfig)) :

```python
from src.ga.initialization import RandomBlockInitializer
from src.ga.population import EliteRestart
from src.memetic.local_search import MiniZincLocalSolver, RandomEmployeesNeighborhood

base = build_block_memetic_config(instance, settings)
adapter = GecodeAdapter(SolverOptions(limit=WallTimeLimit(2.0)), model=ModelVariants.RELAXED)
local_solver = MiniZincLocalSolver(instance, adapter, RandomEmployeesNeighborhood(instance, size=1), base.evaluator)
initializer = RandomBlockInitializer(instance, base.encoding, local_solver=local_solver)
config = dataclasses.replace(
    base,
    local_solver=local_solver,
    initializer=initializer,
    restart=EliteRestart(initializer, base.evaluator, settings.elite_count),
)
result = Memetic(config).run()
```

Points à vérifier pour un nouveau solveur :
- **reproductibilité** : seul CP-SAT a une limite déterministe dans le projet. Gecode accepte une limite en nombre d'échecs (`--fail`, prévue dans D10 sous le nom `FailureLimit`), qui serait reproductible : il faudrait l'ajouter comme nouvelle sous-classe d'`EffortLimit` ;
- **statistiques** : `failures`, `propagations` et `nodes` sont facultatives dans `SolverStatistics`, parce que tous les solveurs ne les rapportent pas. Les comparaisons de charge (D10) ne valent qu'entre exécutions du **même** solveur ;
- **statuts** : `SolverAdapter._outcome_of` traduit les statuts de minizinc-python. Un statut inattendu lève `SolverFailureError`.

---

## 11. Je veux modifier l'encodage des génomes

C'est la modification la plus profonde : l'encodage détermine le type `G` des génomes, et donc les opérateurs et l'initialiseur compatibles.

**Fichiers** :
- `src/ga/chromosome.py` : le nouvel encodage (et le type de son génome), tests dans `tests/test_chromosome.py` ;
- `src/ga/initialization.py` : un `PopulationInitializer[G]` qui produit des génomes du nouveau type, tests dans `tests/test_initialization.py` ;
- `src/ga/operators.py` : au moins un `Crossover[G]` et une `Mutation[G]` dont `encoding_type()` rend le nouvel encodage, tests dans `tests/test_operators.py` ;
- `src/memetic/assembly.py` : une nouvelle fonction d'assemblage (par exemple `build_direct_memetic_config`) qui rend une `MemeticConfig[G]` du nouveau type.

Le reste ne change pas : le moteur, la sélection, `SelectPop`, le restart, le `LocalSolver` et l'évaluation travaillent sur `Individu[G]` et sur le phénotype `Horaire`, quel que soit `G`.

**Interface** : `Encoding[G]` (`src/ga/chromosome.py`), deux méthodes, des **traductions pures et réciproques** (D6) :

| Méthode | Contrat |
|---|---|
| `encode(horaire)` | le génome qui représente `horaire` |
| `decode(genome)` | l'horaire représenté par `genome`, faisable ou non ; jamais d'exception pour un horaire infaisable |

Il faut `decode(encode(h)) == h` et `encode(decode(g)) == g`. Le moteur ré-encode chaque horaire rendu par le `LocalSolver` : une traduction qui perd de l'information casse cette boucle.

**Contraintes sur le type `G`** :
- le génome doit être **immuable et comparable** (tuples, *dataclasses* figées) : `PlusSurvivorSelector` élimine les doublons en comparant les individus ;
- le `DiversityCollector` compte les gènes avec `Counter(individu.genome)` : le génome doit être itérable, et ses éléments hachables.

**Exemple : l'encodage direct (le phénotype comme génome).**

```python
from src.model.horaire import Horaire, HoraireEmploye

# Génome de DirectEncoding : le quart de chaque employé (ses jalons et ses activités), dans l'ordre des employés.
type DirectGenome = tuple[HoraireEmploye, ...]

class DirectEncoding(Encoding[DirectGenome]):
    """Le génome est la liste des quarts de l'horaire : la traduction est l'identité."""

    def encode(self, horaire: Horaire) -> DirectGenome:
        return horaire.employees

    def decode(self, genome: DirectGenome) -> Horaire:
        return Horaire(employees=genome)
```

Ensuite, les opérateurs :

```python
class UniformShiftCrossover(Crossover[DirectGenome]):
    @classmethod
    def encoding_type(cls) -> type[Encoding[DirectGenome]]:
        return DirectEncoding
    ...
```

Un opérateur de `BlockEncoding` branché sur `DirectEncoding` est refusé par `MemeticConfig.validate` (`IncompatibleOperatorError`). Les variantes d'encodage à comparer sont prévues à l'étape 10 du [`TODO.md`](../TODO.md) (`DirectEncoding`, `SortedBlockEncoding`, D1 et D3).

---

*Une question manque ? Ajoutez une section en suivant le même plan : fichiers, interface, exemple exécuté, points de vigilance. Et mettez à jour la liste au début de ce document et la section « Comment faire ? » du [`README.md`](../README.md).*
