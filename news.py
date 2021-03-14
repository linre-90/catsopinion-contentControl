import firebase_admin
from firebase_admin import firestore
import confighandler as ch
import ast


class News:
    def __init__(self):
        self.database_entry = ch.ConfigHandler()
        pass

    def get_news(self):
        try:
            db = firestore.client()
            news_array = []
            for i in self.database_entry.news_collections():
                records = db.collection(i).stream()
                for record in records:
                    record_dict = record.to_dict()
                    record_dict["uid"] = record.id
                    news_array.append(record_dict)
            return news_array
        except Exception as e:
            return ["error", e]

    def insert_new(self, item, locale):
        if locale == "fi" or locale == "en":
            return self.insert_single(self.database_entry.get_single_news_collection(locale), item)

    def delete_one(self, item):
        try:
            item_dic = ast.literal_eval(item)
            if item_dic["locale"] == "fi":
                db = firestore.client()
                db.collection(self.database_entry.get_single_news_collection("fi")).document(item_dic["uid"]).delete()
            if item_dic["locale"] == "en":
                db = firestore.client()
                db.collection(self.database_entry.get_single_news_collection("en")).document(item_dic["uid"]).delete()
            return ["ok"]
        except Exception as e:
            return ["error", e]

    def insert_single(self, collection, item):
        try:
            db = firestore.client()
            db.collection(collection).add(item)
            return [""]
        except Exception as e:
            return ["error", e]
