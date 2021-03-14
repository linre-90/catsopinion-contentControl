import configparser


class ConfigHandler:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("config.ini")

    def read_series(self):
        series_list = []
        index = 0
        for i in self.config["SERIES"]:
            series_list.insert(index, self.config.get("SERIES", i))
            index += 1
        return series_list
