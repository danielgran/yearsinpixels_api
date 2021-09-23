import inspect
import unittest

from src.EndPoint.SocketStrategy.WebStrategy import WebStrategy


class TestWebStrategy(unittest.TestCase):

    def test_isThereAndAbstract(self):
        self.assertTrue(inspect.isabstract(WebStrategy), "There is no abstract strategy class")