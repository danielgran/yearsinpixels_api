import unittest

from src.EndPoint.EndPoint import EndPoint
from src.Request.RawRequest import RawRequest
from src.RequestQueue.RequestQueue import RequestQueue


class TestEndpoint(unittest.TestCase):

    def setUp(self):
        self.endpoint = EndPoint("/test")

    def test_creation(self):
        self.assertTrue(self.endpoint)

    def test_metadata(self):
        self.assertTrue(self.endpoint.path)
        self.assertTrue(self.endpoint.creation)

    def test_set_request_queue(self):
        self.endpoint.set_request_queue(RequestQueue())
        self.assertTrue(self.endpoint.has_request_queue())

    def test_process_request(self):
        request = RawRequest("/examplepath")

        self.assertRaises(Exception, self.endpoint.process_request, request)

        request_queue = RequestQueue()
        self.endpoint.set_request_queue(request_queue)
        guid = self.endpoint.process_request(request)

        self.assertEqual(type(guid), type("some_string"))
        self.assertEqual(self.endpoint.get_no_open_requests(), 1)

    def test_no_open_request(self):
        request_queue = RequestQueue()
        self.endpoint.set_request_queue(request_queue)

        iterations = 213
        for i in range(iterations):
            self.endpoint.process_request(RawRequest(f"/{i}"))

        self.assertEqual(self.endpoint.get_no_open_requests(), iterations)
