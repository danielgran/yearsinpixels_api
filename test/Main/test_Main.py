import unittest

import test
from yearsinpixels_api.Main import Main

@unittest.skipIf(test.disable_mysql_testcase,
                 "MySQL support will not work on this system. Use the 'yearsinpixels_data.Gateway.TestGateway' package.")
class MainTest(unittest.TestCase):

    def test_isthere(self):
        self.assertTrue(Main)

    def test_main(self):
        self.assertIsNotNone(Main.main)
