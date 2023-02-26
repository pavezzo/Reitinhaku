from reitinhaku.algorithms.jps import JPS
from reitinhaku.algorithms.dijkstra import Dijkstra
from reitinhaku.utils.filereader import FileReader


def run_perfomance_test(iterations, map, start, end):
    dijkstra_times = []
    jps_times = []

    for i in range(iterations):
        _, _, time = dijkstra.solve(start, end, map)
        dijkstra_times.append(time)

    d_avg = sum(dijkstra_times) / len(dijkstra_times)
    print(f"Dijkstra took on average: {d_avg} seconds")

    for i in range(iterations):
        _, _, time = jps.solve(start, end, map)
        jps_times.append(time)

    j_avg = sum(jps_times) / len(jps_times)
    print(f"JPS took on average: {j_avg} seconds")


if __name__ == "__main__":
    fr = FileReader()
    jps = JPS()
    dijkstra = Dijkstra()

    maps = ["Berlin_0_256", "Boston_0_512", "Berlin_0_1024"]
    coords = [[(228, 252), (0, 0)], [(5, 268), (478, 27)],
              [(36, 8), (1016, 977)]]
    iterations = 100

    for i, m in enumerate(maps):
        map = fr.read_map(m)
        print("Starting test {i}")
        print(f"Map size: {len(map)}x{len(map[0])}")
        print(f"Running {iterations} iterations")
        run_perfomance_test(iterations, map, coords[i][0], coords[i][1])
