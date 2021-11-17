import unittest

from yearsinpixels_api.Main import Main


class MainTest(unittest.TestCase):

    def test_isthere(self):
        self.assertTrue(Main)

    def test_main(self):
        self.assertIsNotNone(Main.main)
