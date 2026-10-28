# Le problème : confection d'horaires de travail

Ce document décrit le problème que l'algorithme mémétique doit résoudre. La référence formelle est le modèle MiniZinc [`src/model/horaire.mzn`](../src/model/horaire.mzn). En cas de doute, c'est lui qui fait foi.

---

## 1. En bref

On dispose d'une équipe d'**employés interchangeables** et d'une journée découpée en **périodes de 15 minutes**. Chaque employé fait **un quart de travail** dont la structure est imposée : il commence, prend une pause, dîne, prend une seconde pause et termine, avec une **activité** entre chaque jalon.

Pour chaque période et chaque activité, l'instance donne une **demande**, c'est-à-dire le nombre d'employés souhaité. Il faut choisir les quarts et les activités pour que la couverture colle au mieux à la demande. Le **coût** à minimiser pénalise chaque employé de trop (sur-couverture) et chaque employé manquant (sous-couverture).

---

## 2. Les données d'une instance

Les instances sont dans [`data/`](../data), au format JSON. MiniZinc les lit directement.

| Champ | Type | Signification |
|---|---|---|
| `NB_EMPLOYES` | entier | Nombre d'employés |
| `NB_ACTIVITES` | entier | Nombre d'activités différentes |
| `NB_PERIODES` | entier | Nombre de périodes de 15 min de la journée |
| `demande` | `NB_PERIODES` × `NB_ACTIVITES` | Nombre d'employés souhaité sur l'activité *a* à la période *p* |
| `surcout` | `NB_PERIODES` × `NB_ACTIVITES` | Coût de **chaque** employé en trop sur l'activité *a* à la période *p* |
| `souscout` | `NB_PERIODES` × `NB_ACTIVITES` | Coût de **chaque** employé manquant sur l'activité *a* à la période *p* |

**Attention à l'indexation.** Dans le modèle, les périodes, les activités et les employés sont numérotés **à partir de 1**. Dans le JSON, les tableaux sont des listes Python indexées à partir de 0 : `demande[0][0]` du JSON correspond à `demande[1, 1]` dans MiniZinc.

Extrait de `bench_2.json` (4 employés, 2 activités, 28 périodes) :

```json
{
    "NB_EMPLOYES": 4,
    "NB_ACTIVITES": 2,
    "NB_PERIODES": 28,
    "demande":  [[0, 1], [0, 1], ...],
    "surcout":  [[...], ...],
    "souscout": [[...], ...]
}
```

### La plage utile

Le modèle ignore les périodes du début et de la fin de journée où toutes les données sont nulles (demande, sur-coût et sous-coût, pour toutes les activités). Ce qui reste est la **plage utile** :

- `MIN_PERIODES` : première période dont les données ne sont pas toutes nulles ;
- `MAX_PERIODES` : dernière période dont les données ne sont pas toutes nulles.

Les quarts sont placés dans cette plage. Dans les cinq instances fournies, la plage utile couvre toute la journée (de 1 à `NB_PERIODES`).

---

## 3. Ce qu'il faut décider : le quart de chaque employé

Pour chaque employé *e*, on choisit **cinq jalons** (des numéros de période) et **quatre activités** :

```text
debut ─ activité 1 ─ pause1 ─ activité 2 ─ diner (4 périodes) ─ activité 3 ─ pause2 ─ activité 4 ─ fin
```

| Variable du modèle | Signification |
|---|---|
| `debut[e]` | Première période travaillée |
| `pause1[e]` | Période de la première pause (dure 1 période) |
| `diner[e]` | Première période du dîner (dure 4 périodes : `diner` à `diner + 3`) |
| `pause2[e]` | Période de la seconde pause (dure 1 période) |
| `fin[e]` | Dernière période travaillée (**incluse**) |
| `activites[e, 1..4]` | Activité faite dans chacun des quatre blocs |

Les quatre activités ne sont **pas** forcément différentes : un employé peut faire la même activité avant et après sa pause. Il ne change d'activité qu'aux pauses et au dîner.

Périodes occupées par chaque bloc d'activité (bornes incluses) :

| Bloc | De | À |
|---|---|---|
| Activité 1 | `debut` | `pause1 - 1` |
| Activité 2 | `pause1 + 1` | `diner - 1` |
| Activité 3 | `diner + 4` | `pause2 - 1` |
| Activité 4 | `pause2 + 1` | `fin` |

---

## 4. Les règles d'un quart (contraintes structurelles)

Un quart est **structurellement faisable** s'il respecte toutes les règles suivantes. Côté Python, les constantes correspondantes sont dans [`src/model/shift_rules.py`](../src/model/shift_rules.py).

### 4.1 Durées

| Règle | Valeur | Constante |
|---|---|---|
| Pause | 1 période (15 min) | `ShiftStructure.BREAK_DURATION` |
| Dîner | 4 périodes (1 h) | `ShiftStructure.LUNCH_DURATION` |
| Bloc d'activité minimal | 4 périodes (1 h) | `ShiftStructure.MIN_ACTIVITY_DURATION` |
| Heures rémunérées par quart | 6 à 8 h (dîner non rémunéré, pauses rémunérées) | `ShiftStructure.MIN_PAID_HOURS`, `MAX_PAID_HOURS` |

### 4.2 Durée du quart

Comme les deux bornes sont incluses, un quart de *N* périodes a un écart `fin - debut` de *N* − 1. Pour 6 à 8 h rémunérées, plus 1 h de dîner :

```text
27 ≤ fin - debut ≤ 35        (27 = 6×4 + 4 − 1,   35 = 8×4 + 4 − 1)
```

Constantes : `ShiftStructure.MIN_SHIFT_SPAN`, `MAX_SHIFT_SPAN`.

### 4.3 Écarts minimaux entre jalons

Chaque bloc doit durer au moins 4 périodes. Il faut aussi compter la pause ou le dîner qui le précède :

| Contrainte | Écart minimal | Raison | Constante |
|---|---|---|---|
| `pause1 - debut ≥ 4` | 4 | bloc 1 | `ShiftGaps.START_TO_BREAK1` |
| `diner - pause1 ≥ 5` | 1 + 4 | pause + bloc 2 | `ShiftGaps.BREAK1_TO_LUNCH` |
| `pause2 - diner ≥ 8` | 4 + 4 | dîner + bloc 3 | `ShiftGaps.LUNCH_TO_BREAK2` |
| `fin - pause2 ≥ 4` | 4 | bloc 4 | `ShiftGaps.BREAK2_TO_END` |

### 4.4 Fenêtres de chaque jalon

Avant lui, chaque jalon doit laisser la place aux écarts qui le précèdent. Après lui, il doit laisser la place à ceux qui le suivent. On en tire une fenêtre dans la plage utile :

| Jalon | Au plus tôt | Au plus tard |
|---|---|---|
| `debut` | `MIN_PERIODES` | `MAX_PERIODES − 27` |
| `pause1` | `MIN_PERIODES + 4` | `MAX_PERIODES − 17` (17 = 5 + 8 + 4) |
| `diner` | `MIN_PERIODES + 9` (9 = 4 + 5) | `MAX_PERIODES − 12` (12 = 8 + 4) |
| `pause2` | `MIN_PERIODES + 17` (17 = 4 + 5 + 8) | `MAX_PERIODES − 4` |
| `fin` | `MIN_PERIODES + 27` | `MAX_PERIODES` |

Constantes : `WindowOffsets` (par exemple `BREAK1_LATEST_BEFORE_LAST = 17`).

---

## 5. La couverture

`total[p, a]` est le nombre d'employés qui font l'activité *a* à la période *p*. Un employé compte pour l'activité de son bloc en cours. Il ne compte pour **aucune** activité pendant ses pauses, son dîner et en dehors de son quart.

**Contrainte dure** : à toute période où une activité a une demande positive, **au moins un** employé doit y être affecté.

```text
pour tout p, a :   demande[p, a] > 0   ⇒   total[p, a] ≥ 1
```

---

## 6. Le coût à minimiser

```text
cout_total = Σ (sur p, a)   max(0, demande[p, a] − total[p, a]) × souscout[p, a]     (employés manquants)
                          + max(0, total[p, a] − demande[p, a]) × surcout[p, a]      (employés en trop)
```

**Un sous-coût de 1 000 000 sert de pénalité quasi dure.** Dans les instances fournies, il n'apparaît que là où la demande est positive. Il signale une période et une activité où manquer d'employés est pratiquement interdit, sans l'être formellement. Une solution qui laisse un tel trou a donc un coût de l'ordre du million : on la repère d'un coup d'œil.

---

## 7. Exemple : la solution optimale de `bench_1`

`bench_1` : 3 employés, 1 activité, 32 périodes. CP-SAT prouve que le coût optimal est **94**.

Légende : `1` = activité 1, `P` = pause, `D` = dîner, `.` = hors quart.

```text
Période    12345678901234567890123456789012
Employé 1  1111P1111DDDD111111P11111111....
Employé 2  ...1111P1111DDDD11111111P111111.
Employé 3  ....1111P111111DDDD111111P111111
Demande    11111111111111112222111121111111
```

| Employé | debut | pause1 | diner | pause2 | fin | fin − debut |
|---|---|---|---|---|---|---|
| 1 | 1 | 5 | 10 | 20 | 28 | 27 |
| 2 | 4 | 8 | 13 | 25 | 31 | 27 |
| 3 | 5 | 9 | 16 | 26 | 32 | 27 |

Dans cette solution, la demande n'est jamais sous-couverte. Le coût de 94 vient entièrement de la sur-couverture. Par exemple, aux périodes 6 et 7, trois employés travaillent pour une demande de 1, soit 2 employés de trop × sur-coût 8 = 16 par période.

---

## 8. Les instances fournies

| Instance | Employés | Activités | Périodes | Remarque |
|---|---|---|---|---|
| `bench_1` | 3 | 1 | 32 | Optimum 94, prouvé en moins d'une seconde |
| `bench_2` | 4 | 2 | 28 | |
| `bench_3` | 6 | 3 | 48 | |
| `bench_4` | 8 | 4 | 44 | |
| `bench_5` | 8 | 5 | 48 | **Difficile** : environ 1 min (médiane) pour une première solution avec CP-SAT à 8 workers |

---

## 9. Particularités à garder en tête

- **Symétrie.** Les employés sont interchangeables : permuter deux horaires donne une solution équivalente, de même coût. Ça compte pour l'algorithme génétique, puisque croiser « employé par employé » deux parents équivalents mais permutés peut être destructeur (décision D3 du [`TODO.md`](../TODO.md)). Le modèle MiniZinc contient une contrainte de bris de symétrie, mais elle est **désactivée** (en commentaire).
- **Faisabilité difficile.** Sur les grosses instances, la contrainte « au moins un employé si demande > 0 » rend même la recherche d'une première solution coûteuse. Générer des individus initiaux faisables (étape 6) ne sera donc pas trivial.
- **Deux sorties dans le modèle.** `horaire.mzn` imprime les variables au format JSON, puis une grille « employé × période » où 0 signifie « aucune activité » (hors quart, pause ou dîner). Contrairement à l'exemple ci-dessus, cette grille ne distingue pas la pause du dîner.
