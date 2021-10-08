import unittest

from src.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy


class TestFlaskStrategy(unittest.TestCase):

    def test_isThere(self):
        self.assertIsNotNone(FlaskWebStrategy)





