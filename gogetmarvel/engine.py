import hashlib
import requests
import json
from datetime import datetime

VERSION = "v1"

class Engine(object):
    """
    This is the parent class for other classes that interact with the
    Marvel API.
    """

    _resource = ""
    base_url = "http://gateway.marvel.com/{}/public/".format(VERSION)

    def __init__(self, public_key, private_key):
        """
        This is the initialization of the Marvel API. Each instance
        of the engine requires a Public key, and Private key provided
        by Marvel dev.

        Parameters:
            public_key: Public key provided by marvel
            private_key: Private key provided by marvel
        """

        self.public_key = public_key
        self.private_key = private_key

        self.methods = []
        self.parameters = []

    def get_timestamp(self):
        """
        Returns the datetime right now used as a salt for the hashstring
        sent to the Marvel API.
        Example:
            "2016-07-2807:32:21"
        """
        return datetime.now().strftime("%Y-%m-%d%H:%M:%S")

    def get_hashstring(self, ts):
        """
        Parameters:
            ts (timestamp): A timestamp of the current time
        Returns a hashstring of the format:
            md5(timestamp + private_key + public_key)
        This hashstring follows the specifications provided by Marvel.
        """
        hash_string = "{}{}{}".format(ts, self.private_key, self.public_key)
        return hashlib.md5(hash_string.encode('utf-8')).hexdigest()

    def get_auth(self, ts, hash):
        """
        Parameters:
            ts (timestamp): A timestamp of the current time
            hash: md5 encrypted string used by Marvel to authenticate
        Returns:
            A constructed string that is used in the URL being sent to
            Marvel.
        """
        return "ts={}&apikey={}&hash={}".format(ts,self.public_key,hash)

    def is_valid_method(self, test_method):
        """
        Returns true or false based on if the method is in the list of
        methods.
        """
        return True if test_method in self.methods else False

    def go_get(self, id=None, method=None, parameter=None):
        """
        This function is the main connector between the other functions.
        Its purpose is to retrive json data from the Marvel API.

        Parameters:
            id (int): id can refer to comic id, series id or event id
            method (string): Additional methods to get more details about
                            a comic, series or event.
        Returns:
            json data
        """

        if method and not self.is_valid_method(method):
            return -1

        url = "{}{}".format(self.base_url, self._resource)


        ts = self.get_timestamp()
        hash = self.get_hashstring(ts)


        auth_string = self.get_auth(ts, hash)


        if id:
            url = "{}/{}".format(url, id) # Since id exists appending id
            if method:
                url = "{}/{}".format(url, method)


        url = "{}?{}".format(url, auth_string)

        if parameter:
            url += parameter

        return json.loads(requests.get(url).text)

