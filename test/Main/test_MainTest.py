import unittest

from src.Main import Main


class MainTest(unittest.TestCase):


    def test_isthere(self):
        self.assertTrue(Main)
