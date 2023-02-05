import unittest
from math import sqrt
from algorithms.dijkstra import Dijkstra


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.dijkstra = Dijkstra()
        self.map = [["." for _ in range(10)] for _ in range(10)]

    def test_straigth_down(self):
        distance, path = self.dijkstra.solve((0, 0), (9, 0), self.map)
        self.assertEqual(distance, 9)

    def test_diagonal(self):
        distance, path = self.dijkstra.solve((0, 0), (9, 9), self.map)
        self.assertAlmostEqual(distance, 9*sqrt(2))

    def test_no_path(self):
        map = [[".", ".", ".", "."],
               [".", ".", ".", "."],
               ["@", "@", "@", "@"],
               [".", ".", ".", "."]]

        distance, path = self.dijkstra.solve((0, 0), (3, 3), map)
        self.assertEqual(distance, -1)
        self.assertEqual(path, [])
