import yaml


class TrelloSetting:
    def __init__(self):
        self.settings = yaml.load(open('./settings.yaml', 'r'), Loader=yaml.FullLoader)

    @property
    def api_key(self):
        return self.settings["api_key"]

    @property
    def api_secret(self):
        return self.settings["api_secret"]


settings = TrelloSetting()
