import os

def read_maps():
    maps = []
    scens = []
    for file in os.listdir("data"):
        file_path = "data/" + file
        if ".scen" in file:
            continue
        with open(file_path) as f:
            map = []
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i < 4:
                    continue

                map.append(list(line.strip()))
            maps.append(map)

    return maps
