import unittest
from unittest.mock import MagicMock

from yearsinpixels_api.EndPoint.EndPoint import EndPoint
from yearsinpixels_api.Request.Request import Request
from yearsinpixels_api.Request.Response import Response
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_api.RequestQueue.RequestQueue import RequestQueue


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

    def test_failsafe_process_request(self):
        request = Request("/examplepath")
        self.assertRaises(Exception, self.endpoint.process_request, request, "The Endpoint should raise an error.")

    def test_process_request(self):
        request = Request("/examplepath")
        request_queue = RequestQueue()

        request_queue.get_response = MagicMock()
        self.endpoint.set_request_queue(request_queue)

        self.endpoint.process_request(request)

        self.assertTrue(request_queue.get_response.called)

    def test_no_open_request(self):
        request_queue = RequestQueue()
        self.endpoint.set_request_queue(request_queue)

        iterations = 213
        for i in range(iterations):
            self.endpoint.process_request(Request(f"/{i}"))

        self.assertEqual(self.endpoint.get_no_open_requests(), iterations)
