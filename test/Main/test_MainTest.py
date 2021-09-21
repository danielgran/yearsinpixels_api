import unittest

import Main.Main


class MainTest(unittest.TestCase):


    def test_isthere(self):
        self.assertTrue(Main.Main.main)
