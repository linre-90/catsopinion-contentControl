import firebase_admin


class Message:
    def __init__(self):
        pass

    def get_messages(self):
        dummy_messages = [
            {"uid": "123", "headline": "asdasd", "date": "12/3/2021",
             "message": "test messagedasdajsdkjasdaksjhdkasjdalsjdhlaksjdhalksjdhalskjdhalsjdhaksjdhlasjdhalksjhdklasjhdjhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",
             "name": "", "type": "question", "email": ""},
            {"uid": "321", "headline": "dsadsa", "date": "10/3/2021", "message": "test message", "name": "",
             "type": "question", "email": "asd@asd.com"},
            {"uid": "777", "headline": "teststststs", "date": "11/3/2021", "message": "test message", "name": "",
             "type": "question", "email": ""}
        ]
        return dummy_messages
