from ui.ui import UI
from algorithms.dijkstra import Dijkstra
import filereader

if __name__ == "__main__":
    maps = filereader.read_maps()
    #map = [["." for _ in range(10)] for _ in range(10)]
    #map[5][0] = "@"
    #map[5][1] = "@"
    #map[5][2] = "@"
    #dijkstra = Dijkstra()
    #distance, path = dijkstra.solve((0, 0), (9, 0), map)
    
    ui = UI(maps[0], (136, 17), (157, 35))
    ui.start()
