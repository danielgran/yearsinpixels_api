import unittest

from src.Request.Request import Request
from src.Request.Response import Response


class ResponseTest(unittest.TestCase):

    def setUp(self):
        self.response = Response(Request("/example"))

    def test_is_there(self):
        self.assertIsNotNone(self.response)

    def test_metadata(self):
        self.assertIsNotNone(self.response.request)
