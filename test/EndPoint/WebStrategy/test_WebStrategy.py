import inspect
import unittest

from src.EndPoint.SocketStrategy.WebStrategy import WebStrategy


class TestWebStrategy(unittest.TestCase):

    def test_isThereAndAbstract(self):
        self.assertTrue(inspect.isabstract(WebStrategy), "There is no abstract strategy class")

    def test_is_there_a_setup(self):
        self.assertIsNotNone(WebStrategy.setup_service)

    def test_is_there_a_run(self):
        self.assertIsNotNone(WebStrategy.run)

    def test_is_there_a_is_running(self):
        self.assertIsNotNone(WebStrategy.is_running)
