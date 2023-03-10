from math import sqrt, inf
from heapq import heappush, heappop
import time


class JPS:
    """
        Luokka, joka sisältää Jump point search -algoritmin
    """

    def __init__(self):
        pass

    def solve(self, start, end, map):
        """
            Ratkaisee aloituspisteestä reitin lopetuspisteeseen
        """
        start_time = time.time()

        if map[start[0]][start[1]] == "@":
            return -1, [], -1, []

        self._map = map
        self._end = end

        heap = []
        heappush(heap, (self._heuristic(start, end), start[0], start[1]))

        self.m_length = len(map)
        self.m_width = len(map[0])
        self._parents = [[None for _ in range(self.m_width)]
                         for _ in range(self.m_length)]

        self.distances = [[inf for _ in range(self.m_width)]
                          for _ in range(self.m_length)]
        self.distances[start[0]][start[1]] = 0

        straight_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        diagonal_moves = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

        while heap:
            node = heappop(heap)

            if self.distances[end[0]][end[1]] != inf:
                total_time = time.time() - start_time
                path = self._construct_path(end, start, [end])
                visited = [(x, y) for x, row in enumerate(self.distances)
                           for y, val in enumerate(row) if val != inf]
                return self.distances[end[0]][end[1]], path, total_time, visited

            current_pos = (node[1], node[2])
            for move in straight_moves:
                if n := self._move_straight(current_pos, move):
                    f_score = self.distances[n[0]
                                             ][n[1]] + self._heuristic(n, end)
                    heappush(heap, (f_score, n[0], n[1]))

            for move in diagonal_moves:
                if n := self._move_diagonally(current_pos, move):
                    f_score = self.distances[n[0]
                                             ][n[1]] + self._heuristic(n, end)
                    heappush(heap, (f_score, n[0], n[1]))

        return -1, [], -1, []

    def _move_straight(self, current_pos, dir):
        """
            Etsii hyppäykselle sopivaa pistettä suoraa reittiä pitkin
        """
        node = list(current_pos)
        distance = self.distances[node[0]][node[1]]
        while True:
            node[0] += dir[0]
            node[1] += dir[1]
            distance += 1

            if (node[0] >= self.m_length or node[1] >= self.m_width or
                    node[0] < 0 or node[1] < 0 or
                    self._map[node[0]][node[1]] == "@"):
                return None

            if (self.distances[node[0]][node[1]] != inf and
                    distance > self.distances[node[0]][node[1]]):
                return None

            self._parents[node[0]][node[1]] = (
                node[0] - dir[0],
                node[1] - dir[1]
            )

            self.distances[node[0]][node[1]] = distance

            if tuple(node) == self._end:
                self.distances[node[0]][node[1]] = distance
                return node

            # liikutaan x akselilla
            if dir[0] == 0:
                if (((node[0] + 1) < self.m_length) and
                    (node[1] - dir[1] >= 0) and
                        (node[1] - dir[1] < self.m_width)):
                    if (self._map[node[0]+1][node[1]-dir[1]] == "@"):
                        return node

                if ((node[0] - 1 >= 0) and
                        (node[1] - dir[1] >= 0) and
                        (node[1] - dir[1] < self.m_width)):
                    if (self._map[node[0]-1][node[1]-dir[1]] == "@"):
                        return node
            else:
                if ((node[1] + 1) < self.m_width and
                        (node[0] - dir[0] >= 0) and
                        (node[0] - dir[0] < self.m_length)):
                    if (self._map[node[0]-dir[0]][node[1]+1] == "@"):
                        return node

                if ((node[1] - 1 >= 0) and
                        (node[0] - dir[0] >= 0) and
                        (node[0] - dir[0] < self.m_length)):
                    if (self._map[node[0]-dir[0]][node[1]-1] == "@"):
                        return node

    def _move_diagonally(self, current_pos, dir):
        """
            Etsii hyppäykselle sopivaa kohtaa viistosti
        """
        sqrt_2 = sqrt(2)
        node = list(current_pos)
        distance = self.distances[node[0]][node[1]]

        while True:
            node[0] += dir[0]
            node[1] += dir[1]
            distance += sqrt_2
            if (node[0] >= self.m_length or node[1] >= self.m_width or
                    node[0] < 0 or node[1] < 0 or
                    self._map[node[0]][node[1]] == "@"):
                return None

            if (self._map[node[0]-dir[0]][node[1]] == "@" or
                    self._map[node[0]][node[1]-dir[1]] == "@"):
                return None

            if (self.distances[node[0]][node[1]] != inf and
                    distance >= self.distances[node[0]][node[1]]):
                return None

            self.distances[node[0]][node[1]] = distance

            self._parents[node[0]][node[1]] = (
                node[0] - dir[0],
                node[1] - dir[1]
            )

            if tuple(node) == self._end:
                self.distances[node[0]][node[1]] = distance
                return node

            if self._move_straight(node, (dir[0], 0)):
                return node
            if self._move_straight(node, (0, dir[1])):
                return node

    def _heuristic(self, start, end):
        """
            A* algoritmin käyttämä heuristiikkafunktio,
            laskee "oktiilisen" pituuden
        """
        y_dist = abs(start[0] - end[0])
        x_dist = abs(start[1] - end[1])
        return y_dist + x_dist + (sqrt(2)-2)*min(y_dist, x_dist)

        # return max(abs(start[0]-end[0]), abs(start[1]-end[1]))

    def _construct_path(self, start, end, path):
        """
            Luo ratkaistun reitin
        """

        while start != end:
            path.append(self._parents[start[0]][start[1]])
            start = self._parents[start[0]][start[1]]

        return path
