import unittest

from src.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy


class TestFlaskStrategy(unittest.TestCase):

    def test_isThere(self):
        self.assertIsNotNone(FlaskWebStrategy)

    def test_setup_service(self):
        fws = FlaskWebStrategy()
        fws.setup_service(None)
        self.assertTrue(fws.is_running)

    def test_open_service(self):
        fws = FlaskWebStrategy()
        fws.setup_service(None)
        self.assertIsNotNone(fws.run)
