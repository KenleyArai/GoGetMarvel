import profig

from gogetmarvel.comic import Comic
from gogetmarvel.engine import Engine

cfg  = profig.Config('gogetmarvel/config.cfg')
cfg.sync()

class Marvel(object):
    """
    Main marvel object connects the engine to its children.
    """

    def __init__(self, private_key=None, public_key=None):
        """
        Entry point of the marvel class.
        Requires the API key and secret provided by marvel
        developer.
        """

        if not private_key or not public_key:
            self.public_key = cfg['auth.public_key']
            self.private_key = cfg['auth.private_key']
        else:
            self.public_key = public_key
            self.private_key = private_key

        self.engine = Engine(self.public_key, self.private_key)
        self.query_comic = Comic(self.engine)
