import hashlib
import requests
from datetime import datetime
from gogetmarvel.engine import Engine


VERSION = "v1"

class Comic(Engine):
    _resource = "comics"

    def __init__(self, eng):
        self.public_key = eng.public_key
        self.private_key = eng.private_key
        self.methods = ['characters', 'creators', 'events', 'stories']
        self.parameters = ['dateDescriptor']

    def go_get_week(self, week):
        """
        Parameters:
            week (str): Valid options are "nextWeek", "thisWeek", and "lastWeek"
        Returns:
            json data of the selected week
        """
        p = "&dateDescriptor=" + week
        return self.go_get(parameter=p)
