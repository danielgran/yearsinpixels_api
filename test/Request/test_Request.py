import unittest

from yearsinpixels_api.Request.Request import Request


class RequestTest(unittest.TestCase):
    def setUp(self):
        self.request = Request("/examplepath")

    def test_is_there(self):
        self.assertTrue(self.request)

    def test_creation(self):
        self.assertRaises(Exception, Request, None)

    def test_metadata(self):
        self.assertIsNotNone(self.request.path)
        self.assertIsNotNone(self.request.header)
        self.assertIsNotNone(self.request.arguments)
        self.assertIsNotNone(self.request.request_cookies)

    def test_set_header(self):
        self.request.header = {'server': "cloudflare"}
        self.assertIsNotNone(self.request.header['server'])
        self.assertFalse(self.request.header.get('shouldNotExist'), "Request has flag that should not exist")

    def test_set_body(self):
        self.request.body = "checkBody"
        self.assertIsNotNone(self.request.body)

    def test_requestPath(self):
        self.assertIsNotNone(self.request.path)
