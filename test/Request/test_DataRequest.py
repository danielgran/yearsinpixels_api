import unittest

from src.Request.DataRequest import DataRequest


class TestDataRequest(unittest.TestCase):


    def test_is_there(self):
        self.assertIsNotNone(DataRequest)
