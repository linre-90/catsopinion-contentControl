import confighandler as cfh


class Blog:
    def __init__(self):
        self.config_wizard = cfh.ConfigHandler()

    def get_series(self):
        return self.config_wizard.read_series()

    def save_blog_post(self, item, locale):
        print(locale)
        if locale == "fi":
            print("save to fi db", item)
        elif locale == "en":
            print("save to en db", item)
