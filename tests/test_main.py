import unittest
from src.app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_root(self):
        resp = self.app.get('/')
        assert b'Hello World!' in resp.data

if __name__ == '__main__':
    unittest.main()
