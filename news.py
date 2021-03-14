import firebase_admin


class News:
    def __init__(self):
        pass

    def get_news(self):
        return ["test news 1", "test news 2"]

    def insert_new(self, item, locale):
        if locale == "fi":
            print("fi db", item)
        elif locale == "en":
            print("en db", item)

    def delete_one(self, item):
        print(item)
