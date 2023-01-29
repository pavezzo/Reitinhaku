from math import sqrt, inf
from heapq import heappush, heappop

class Dijkstra:
    def __init__(self):
        self.distance = inf
        self.path = []
    
    def solve(self, start, end, map):
        length = len(map)
        width = len(map[0])

        distances = [[inf for _ in range(width)] for _ in range(length)]
        distances[start[0]][start[1]] = 0
    
        parents = [[None for _ in range(width)] for _ in range(length)]
        handled = {}

        heap = []
        heappush(heap, (0, start[0], start[1]))

        moves = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]
    
        while heap:
            node = heappop(heap)
        
            if (node[1], node[2]) in handled or map[node[1]][node[2]] != ".":
                continue
            elif (node[1], node[2]) == end:
                self.path = self._construct_path(end, start, parents, [end])
                self.path.reverse()
                return node[0], self.path

            handled[(node[1], node[2])] = True
        
            for i, move in enumerate(moves):
                next = (node[1]+move[0], node[2]+move[1])
                if next[0] < 0 or next[0] >= width or next[1] < 0 or next[1] >= length:
                    continue
            
                if i > 3 and (map[node[1]][next[1]] != "." or map[next[0]][node[2]] != "."):
                    continue
                
                if map[next[0]][next[1]] == ".":
                    current_distance = distances[next[0]][next[1]]
                    new_distance = 0
                    if i < 4:
                        new_distance = distances[node[1]][node[2]] + 1
                    else:
                        new_distance = distances[node[1]][node[2]] + sqrt(2)
                    if new_distance < current_distance or current_distance == inf: 
                        distances[next[0]][next[1]] = new_distance
                        parents[next[0]][next[1]] = (node[1], node[2])
                        if i < 4:
                            heappush(heap, (node[0]+1, next[0], next[1]))
                        else:
                            heappush(heap, (node[0]+sqrt(2), next[0], next[1]))

        return 0, []


    def _construct_path(self, start, end, parents, path):
        if start == end:
            return path

        path.append(parents[start[0]][start[1]])
        self._construct_path(parents[start[0]][start[1]], end, parents, path)
        return path
