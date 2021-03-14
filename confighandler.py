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

    def news_collections(self):
        series_list = []
        index = 0
        for i in self.config["DBNEWSCOLLECTIONS"]:
            series_list.insert(index, self.config.get("DBNEWSCOLLECTIONS", i))
            index += 1
        return series_list

    def get_single_news_collection(self, locale):
        if locale == "fi":
            return self.config.get("DBNEWSCOLLECTIONS", "newsfi")
        elif locale == "en":
            return self.config.get("DBNEWSCOLLECTIONS", "newsen")

    def get_message_collection(self):
        return self.config.get("DBMESSAGECOLLECTIONS", "messages")
