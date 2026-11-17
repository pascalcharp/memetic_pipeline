"""Tests de l'exécution des lots (src/memetic/executor.py) — scaffold commun de la semaine du 16 novembre."""

import unittest

from src.memetic.executor import Executor, SequentialExecutor

ITEMS: tuple[int, ...] = (3, 1, 2)


class TestSequentialExecutor(unittest.TestCase):

    def test_givenInterface_whenInstantiated_thenRaisesTypeError(self) -> None:
        with self.assertRaises(TypeError):
            Executor()  # type: ignore[abstract]

    def test_givenTaskAndItems_whenMap_thenResultsAreInTheOrderOfTheItems(self) -> None:
        self.assertEqual(SequentialExecutor().map(lambda item: item * item, ITEMS), [item * item for item in ITEMS])

    def test_givenEmptyBatch_whenMap_thenReturnsEmptyList(self) -> None:
        self.assertEqual(SequentialExecutor().map(lambda item: item, ()), [])

    def test_givenTask_whenMap_thenEachItemIsProcessedOnce(self) -> None:
        processed: list[int] = []
        SequentialExecutor().map(processed.append, ITEMS)
        self.assertEqual(processed, list(ITEMS))


if __name__ == "__main__":
    unittest.main()
