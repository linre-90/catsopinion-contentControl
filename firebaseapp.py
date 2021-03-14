import firebase_admin


class FirebaseWizard:
    def __init__(self):
        firebase_admin.initialize_app()
