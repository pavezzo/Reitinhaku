import unittest
from math import sqrt
from algorithms.dijkstra import Dijkstra

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.dijkstra = Dijkstra()
        self.map = [["." for _ in range(10)] for _ in range(10)]        

    def testStraigthDown(self):
        distance, path = self.dijkstra.solve((0, 0), (9, 0), self.map)
        self.assertEqual(distance, 9)

    def testDiagonal(self):
        distance, path = self.dijkstra.solve((0, 0), (9, 9), self.map)
        self.assertAlmostEqual(distance, 9*sqrt(2))
