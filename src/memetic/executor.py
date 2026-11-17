"""Exécution des lots (décision D7) : le moteur traite chaque lot par ``executor.map``.

Aucun parallélisme dans le POC : ``SequentialExecutor`` est la seule implémentation. L'interface permet d'ajouter
plus tard une version par fils ou asynchrone sans toucher au moteur. Pour que le résultat ne dépende pas de l'ordre
d'exécution, chaque tâche reçoit tout ce dont elle a besoin, dont sa propre graine (D7) ; elle ne partage ni
générateur aléatoire ni état modifiable avec les autres.
"""

from abc import ABC, abstractmethod
from collections.abc import Callable, Sequence


class Executor(ABC):
    """Applique une tâche à chaque élément d'un lot et rend les résultats dans l'ordre du lot."""

    @abstractmethod
    def map[T, R](self, task: Callable[[T], R], items: Sequence[T]) -> list[R]:
        """``[task(item) for item in items]``, dans l'ordre de ``items``, quel que soit l'ordre d'exécution."""


class SequentialExecutor(Executor):
    """Exécute les tâches une à une, dans le fil courant."""

    def map[T, R](self, task: Callable[[T], R], items: Sequence[T]) -> list[R]:
        return [task(item) for item in items]
