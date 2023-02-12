from math import sqrt, inf
from heapq import heappush, heappop


class JPS:
    """
        Luokka, joka sisältää Jump point search -algoritmin
    """
    def __init__(self):
        pass

    def solve(self, start, end, map):
        """
            Ratkaisee aloituspisteestä reitin lopetuspisteeseen,
            ei toimi vielä kaikissa tapauksissa.
        """
        
        self.map = map
        self.end = end

        heap = []
        heappush(heap, (self._heuristic(start, end), start[0], start[1]))

        self.m_length = len(map)
        self.m_width = len(map[0])

        self.distances = [[inf for _ in range(self.m_width)]
                          for _ in range(self.m_length)]
        self.distances[start[0]][start[1]] = 0

        straight_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        diagonal_moves = [(-1, -1), (1, 1), (1, -1), (-1, 1)]

        while heap:
            node = heappop(heap)
            # print(f"current node: {node}")
            if self.distances[end[0]][end[1]] != inf:
                return self.distances[end[0]][end[1]]

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

    def _move_straight(self, current_pos, dir, mark_distances=True):
        """
            Etsii hyppäykselle sopivaa pistettä suoraa reittiä pitkin
        """
        node = list(current_pos)
        distance = self.distances[node[0]][node[1]]
        while True:
            node[0] += dir[0]
            node[1] += dir[1]
            distance += 1
            # print(f"straight: {node}")
            if (node[0] >= self.m_length or node[1] >= self.m_width or
                    node[0] < 0 or node[1] < 0 or
                    self.map[node[0]][node[1]] == "@"):
                return None
            if self.distances[node[0]][node[1]] != inf:
                return None
            if mark_distances:
                self.distances[node[0]][node[1]] = distance

            if tuple(node) == self.end:
                self.distances[node[0]][node[1]] = distance
                # print("straightly found it!")
                return node

            # liikutaan x akselilla
            if dir[0] == 0:
                if (((node[0] + 1) < self.m_length) and
                        (node[1] - dir[1] >= 0) and
                        (node[1] - dir[1] < self.m_width)):
                    if (self.map[node[0]+1][node[1]-dir[1]] == "@"):
                        # print(f"jump point: {node}")
                        return node

                if ((node[0] - 1 >= 0) and
                        (node[1] - dir[1] >= 0) and
                        (node[1] - dir[1] < self.m_width)):
                    if (self.map[node[0]-1][node[1]-dir[1]] == "@"):
                        # print(f"jump point: {node}")
                        return node
            else:
                if ((node[1] + 1) < self.m_width and
                        (node[0] - dir[0] >= 0) and
                        (node[0] - dir[0] < self.m_length)):
                    if (self.map[node[0]-dir[0]][node[1]+1] == "@"):
                        # print(f"jump point: {node}")
                        return node

                if ((node[1] - 1 >= 0) and
                        (node[0] - dir[0] >= 0) and
                        (node[0] - dir[0] < self.m_length)):
                    if (self.map[node[0]-dir[0]][node[1]-1] == "@"):
                        # print(f"jump point: {node}")
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
            # print(f"diagonally: {node}")
            if (node[0] >= self.m_length or node[1] >= self.m_width or
                    node[0] < 0 or node[1] < 0 or
                    self.map[node[0]][node[1]] == "@"):
                return None

            if self.distances[node[0]][node[1]] != inf:
                return None
            self.distances[node[0]][node[1]] = distance

            if tuple(node) == self.end:
                self.distances[node[0]][node[1]] = distance
                # print("diagonally found it!")
                return node

            if self._move_straight(node, (dir[0], 0), False):
                return node
            if self._move_straight(node, (0, dir[1]), False):
                return node

    def _heuristic(self, start, end):
        """
            A* algoritmin käyttämä heuristiikkafunktio,
            laskee diagonaalisen pituuden
        """
        return max(abs(start[0]-end[0]), abs(start[1]-end[1]))
