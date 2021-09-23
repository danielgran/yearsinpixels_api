import unittest

from src.EndPoint.EndPoint import EndPoint
from src.Request.Request import Request
from src.RequestQueue.RequestQueue import RequestQueue


class TestEndpointUtility:
    @staticmethod
    def create_endpoint():
        return EndPoint("/test")

class TestEndpoint(unittest.TestCase):

    def test_creation(self):
        endpoint = TestEndpointUtility.create_endpoint()
        self.assertTrue(endpoint)

    def test_getmetadata(self):
        endpoint = TestEndpointUtility.create_endpoint()
        self.assertTrue(endpoint.path)
        self.assertTrue(endpoint.creation)

    def test_set_request_queue(self):
        endpoint = TestEndpointUtility.create_endpoint()
        endpoint.set_request_queue(RequestQueue())
        self.assertTrue(endpoint.has_request_queue())

    def test_process_request(self):
        endpoint = TestEndpointUtility.create_endpoint()
        request = Request("/examplepath")
        self.assertRaises(Exception, endpoint.process_request, request)

        request_queue = RequestQueue()

        endpoint.set_request_queue(request_queue)
        endpoint.process_request(request)

        self.assertTrue(endpoint.get_no_open_requests() == 1)



