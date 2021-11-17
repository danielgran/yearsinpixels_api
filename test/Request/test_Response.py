import unittest

from yearsinpixels_api.Request.Request import Request
from yearsinpixels_api.Request.Response import Response


class ResponseTest(unittest.TestCase):

    def setUp(self):
        self.response = Response(Request("/example"))
        self.response.body = ":-)"

    def test_is_there(self):
        self.assertIsNotNone(self.response)

    def test_metadata(self):
        self.assertIsNotNone(self.response.request)
        self.assertIsNotNone(self.response.body)

    def test_toString(self):
        self.assertEqual(str(self.response), ":-)")