from firebase_admin import firestore
import confighandler as conf


class Message:
    def __init__(self):
        self.conf_reader = conf.ConfigHandler()

    def get_messages(self):
        try:
            db = firestore.client()
            records_array = []
            records = db.collection(self.conf_reader.get_message_collection()).stream()
            for record in records:
                record_dict = record.to_dict()
                record_dict["uid"] = record.id
                records_array.append(record_dict)
            return records_array
        except Exception as e:
            return ["error", e]

    def delete_message_from_db(self, uid):
        try:
            db = firestore.client()
            db.collection(self.conf_reader.get_message_collection()).document(uid).delete()
            return ["ok"]
        except Exception as e:
            return ["error", e]
