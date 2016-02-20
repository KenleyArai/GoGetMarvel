


class Marvel(object):

    def __init__(self, api_key, secret):
        """
        Entry point of the marvel class.
        Requires the API key and secret provided by marvel
        developer.
        """

        if not api_key or not secret:
            print("API key or Secret is None")
            raise ValueError

        self.api_key = api_key
        self.secret = secret

