import unittest
from math import sqrt
from algorithms.dijkstra import Dijkstra
from algorithms.jps import JPS


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.dijkstra = Dijkstra()
        self.jps = JPS()
        self.map = [["." for _ in range(10)] for _ in range(10)]

    def test_straigth_down(self):
        distance, path, _, _ = self.dijkstra.solve((0, 0), (9, 0), self.map)
        self.assertEqual(distance, 9)

        distance, path, _, _ = self.jps.solve((0, 0), (9, 0), self.map)
        self.assertEqual(distance, 9)

    def test_diagonal(self):
        distance, path, _, _ = self.dijkstra.solve((0, 0), (9, 9), self.map)
        self.assertAlmostEqual(distance, 9*sqrt(2))

        distance, path, _, _ = self.jps.solve((0, 0), (9, 9), self.map)
        self.assertAlmostEqual(distance, 9*sqrt(2))

    def test_no_path(self):
        map = [[".", ".", ".", "."],
               [".", ".", ".", "."],
               ["@", "@", "@", "@"],
               [".", ".", ".", "."]]

        distance, path, _, _ = self.dijkstra.solve((0, 0), (3, 3), map)
        self.assertEqual(distance, -1)
        self.assertEqual(path, [])

        distance, path, _, _ = self.jps.solve((0, 0), (3, 3), map)
        self.assertEqual(distance, -1)
        self.assertEqual(path, [])

    def test_illegal_start(self):
        map = self.map[:]
        map[0][0] = "@"

        distance, path, _, _ = self.dijkstra.solve((0, 0), (3, 3), map)
        self.assertEqual(distance, -1)
        self.assertEqual(path, [])

        distance, path, _, _ = self.jps.solve((0, 0), (3, 3), map)
        self.assertEqual(distance, -1)
        self.assertEqual(path, [])
