import os


class FileReader:
    """
        Luokka, joka lukee karttoja tiedostoista
    """

    def __init__(self):
        pass

    def read_map_names(self):
        """
            Palauttaa karttojen nimet
        """
        names = []
        for file in os.listdir("data"):
            if ".scen" in file:
                continue
            names.append(file.split(".")[0])
        return names

    def read_map(self, name):
        """
            Lukee tietyn kartan tietodostosta
        """
        file_path = f"data/{name}.map"
        with open(file_path, encoding="utf-8") as f:
            map = []
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i < 4:
                    continue
                map.append(list(line.strip()))
            return map

    def read_maps(self):
        """
            Lukee kaikki kartat kansiosta
        """
        maps = []
        # scens = []
        for file in os.listdir("data"):
            file_path = "data/" + file
            if ".scen" in file:
                continue
            with open(file_path, encoding="utf-8") as f:
                map = []
                lines = f.readlines()
                for i, line in enumerate(lines):
                    if i < 4:
                        continue

                    map.append(list(line.strip()))
                maps.append(map)

        return maps

    def read_scen(self, name):
        """
            Lukee scen tiedostot testausta varten
        """
        file_path = f"data/{name}.map.scen"
        with open(file_path, encoding="utf-8") as f:
            scen = []
            lines = f.readlines()
            for i, line in enumerate(lines):
                if i == 0:
                    continue
                scen.append(line.split())
            return scen
