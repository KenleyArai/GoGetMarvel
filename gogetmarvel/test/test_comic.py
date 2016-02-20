import unittest
import profig

from gogetmarvel.comic import Comic
from gogetmarvel.engine import Engine

cfg  = profig.Config('config.cfg')
cfg.sync()

public_key = cfg['auth.public_key']
private_key = cfg['auth.private_key']

test_engine = Engine(public_key, private_key)
test_comic = Comic(test_engine)

class TestComic(unittest.TestCase):

    def test_go_get(self):
        testing_go_get = test_comic.go_get()
        self.assertEqual(testing_go_get["code"],200)

    def test_go_get_id(self):
        testing_go_get = test_comic.go_get(id=400)
        self.assertEqual(testing_go_get["code"],200)

    def test_go_get_method(self):
        testing_go_get = test_comic.go_get(id=400,method='events')
        test_comic.go_get_week("thisWeek")
        self.assertEqual(testing_go_get["code"],200)

    def test_go_get_param(self):
        testing_go_get = test_comic.go_get_week("thisWeek")
        self.assertEqual(testing_go_get["code"],200)
