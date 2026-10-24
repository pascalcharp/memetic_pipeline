# TODO — Proof of concept : algorithme mémétique pour l'horaire

Légende :
- `[ ]` à faire · `[~]` en cours · `[x]` validé (tests verts)
- **(C)** Claude écrit · **(P)** Pascal écrit, Claude vérifie · **(C→P)** Claude scaffolde (signatures, docstrings, tests), Pascal implémente

Règle : une seule étape à la fois ; on ne passe à la suivante qu'une fois les tests verts (cas nominaux + cas limites).

---

## Décisions de conception à trancher (avant l'étape concernée)

- [ ] **D1 — Encodage du chromosome** (avant étape 3) : direct (par employé : `debut, pause1, diner, pause2, fin, activites[4]`) ou indirect / par paramètres ?
- [x] **D2 — Rôle de MiniZinc comme `SolveurLocal`** : recherche locale d'amélioration (on fixe une partie des gènes, le solveur ré-optimise le reste sous limite de temps). Solveur par défaut : CP-SAT. Les particularités de chaque solveur sont cachées derrière une classe d'indirection, pour pouvoir en changer (Gecode, Chuffed, HiGHS, …).
- [ ] **D3 — Symétrie entre employés** (avant étape 7) : les employés sont interchangeables ; un croisement « par employé » peut être destructeur. Normaliser (trier les employés) avant de croiser ?
- [ ] **D4 — Remplacement / convergence / restart** (avant étape 8) : élitisme (μ+λ) ? mesure de diversité ? quelle fraction conserver au restart ?

---

## Étape 0 — Infrastructure et environnement **(C)**
- [ ] Localisation de l'exécutable MiniZinc : variable d'environnement (ex. `MINIZINC_PATH`) avec repli sur une constante de configuration (`/Applications/MiniZincIDE.app/Contents/Resources/minizinc`) ; pas de dépendance au `PATH` (PyCharm ne le voit pas)
- [ ] Installer `requirements.txt` dans `.venv`
- [ ] Squelette `tests/` (unittest, découverte via `python -m unittest discover`)
- [ ] Test de fumée : MiniZinc + CP-SAT résolvent `horaire.mzn` sur `bench_1.json` depuis Python
- [ ] Dockerfile (Python 3.13 + MiniZinc + CP-SAT) : en second, le développement se fait d'abord en local dans PyCharm
- [ ] Harmoniser la structure réelle avec CLAUDE.md (`horaire.mzn` vs `schedule_model.mzn`, noms des instances `bench_*.json`)

## Étape 1 — Constantes du domaine **(C)**
- [ ] Classe(s) de constantes : 4 activités par quart, durées pause (1 période) / dîner (4 périodes), activité min. (4 périodes), durée de quart (27..35), décalages des fenêtres (`+4`, `-17`, `+9`, `-12`, …)
- [ ] Aucune valeur magique ailleurs dans le code ; tests vérifiant la cohérence avec `horaire.mzn`

## Étape 2 — Lecture des instances (`src/utils/io.py`) **(C)**
- [ ] Classe `Instance` (dataclass typée) : `NB_EMPLOYES`, `NB_ACTIVITES`, `NB_PERIODES`, `demande`, `surcout`, `souscout`
- [ ] Calcul de `MIN_PERIODES` / `MAX_PERIODES` et des fenêtres dérivées (mêmes formules que le modèle)
- [ ] Exceptions sur mesure (`InstanceError`, …) : fichier absent, champ manquant, dimensions incohérentes, valeurs négatives
- [ ] Tests : les 5 bench se chargent ; JSON malformés ; instance où aucun quart ne rentre (ex. trop peu de périodes)

## Étape 3 — Chromosome (`src/ga/chromosome.py`) **(C→P)**
- [ ] Trancher D1
- [ ] Classe `Chromosome` / `HoraireEmploye`
- [ ] Vérification de faisabilité structurelle (les contraintes de `horaire.mzn`) **(P)**
- [ ] Conversion vers la grille « employé × période → activité ou 0 » (même sémantique que la 2ᵉ sortie du modèle)
- [ ] Tests : horaires valides, chaque contrainte violée isolément, bornes exactes des fenêtres

## Étape 4 — Évaluation (fonction de coût) **(P)**
- [ ] Calcul de `total[p, a]` puis du coût sur/sous-couverture, identique à `cout_total`
- [ ] Traitement de la contrainte « au moins 1 employé si demande > 0 » (infaisable ou pénalité ?)
- [ ] Tests : cas calculés à la main + **validation croisée** avec le coût renvoyé par MiniZinc sur des solutions réelles

## Étape 5 — Interface MiniZinc (`src/memetic/local_search.py`) **(C→P)**
- [ ] Classe d'indirection `SolverAdapter` (interface) + `CpSatAdapter` : identifiant du solveur, options (threads, graine, limite de temps), traduction des statuts
- [ ] Résolution complète (référence / borne pour comparer le mémétique)
- [ ] `SolveurLocal(chromosome)` : fixer une partie des variables, résoudre sous limite de temps, reconstruire un `Chromosome`
- [ ] Gestion des erreurs MiniZinc (timeout, UNSAT, solveur absent) via exceptions sur mesure
- [ ] Tests : le résultat est faisable, son coût ≤ coût d'entrée, comportement en timeout / UNSAT

## Étape 6 — Initialisation de la population **(P)**
- [ ] Génération aléatoire d'individus structurellement faisables (graine contrôlée)
- [ ] Option : passer chaque individu initial au `SolveurLocal`
- [ ] Tests : taille, faisabilité de tous les individus, reproductibilité avec la même graine

## Étape 7 — Opérateurs génétiques (`src/ga/operators.py`) **(P)**
- [ ] Trancher D3
- [ ] `SelectParent` (ex. tournoi)
- [ ] `Recombine` (croisement préservant la faisabilité, ou suivi d'une réparation)
- [ ] `SelectMutable` et `Mute` (décaler un quart, une pause, changer une activité, …)
- [ ] Tests : faisabilité préservée, cas limites (population de 2, individus identiques, gènes en bordure de fenêtre)

## Étape 8 — Gestion de la population (`src/ga/population.py`) **(P)**
- [ ] Trancher D4
- [ ] `SelectPop` (remplacement), détection de convergence, `Restart`
- [ ] Tests : taille conservée, meilleur individu jamais perdu (si élitiste), convergence détectée sur population homogène

## Étape 9 — Boucle mémétique `Memetic(NR, NM)` **(P)**
- [ ] Assemblage selon le pseudo-code de CLAUDE.md ; critère `terminé(P)` (générations, temps, stagnation)
- [ ] Journalisation de l'historique (meilleur coût, coût moyen, diversité par génération)
- [ ] Tests : terminaison, coût du meilleur monotone non croissant, exécution complète sur `bench_1`

## Étape 10 — Driver et expériences (`src/drivers/`) **(C)**
- [ ] Point d'entrée CLI (instance, NR, NM, taille de population, graine, limite de temps)
- [ ] Campagne sur `bench_1` … `bench_5` : mémétique vs MiniZinc seul (coût, temps)
- [ ] Export des résultats (CSV/JSON)

## Étape 11 — Documentation **(C)**
- [ ] README : construction Docker, lancement des tests, lancement des expériences
- [ ] DEVLOG à jour
