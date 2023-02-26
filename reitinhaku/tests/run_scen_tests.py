from reitinhaku.algorithms.dijkstra import Dijkstra
from reitinhaku.algorithms.jps import JPS
from reitinhaku.utils.filereader import FileReader
from math import floor

if __name__ == "__main__":
    fr = FileReader()
    # map = fr.read_map("Berlin_0_256")
    # scens = fr.read_scen("Berlin_0_256")
    map = fr.read_map("Berlin_0_1024")
    scens = fr.read_scen("Berlin_0_1024")
    dijkstra = Dijkstra()
    jps = JPS()

    for i, s in enumerate(scens):
        start = (int(s[5]), int(s[4]))
        end = (int(s[7]), int(s[6]))
        expected = float(s[8])
        distance_d, _, _ = dijkstra.solve(start, end, map)
        distance_j, _, _ = jps.solve(start, end, map)

        if (floor(distance_d*100000000)/100000000.0) != (floor(distance_j*100000000)/100000000.0):
            print(s)
            print(f"dijkstra: {distance_d}")
            print(f"jps: {distance_j}")
