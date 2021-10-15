import unittest
import uuid

from src.EndPoint.EndPoint import EndPoint
from src.Request.RawRequest import RawRequest
from src.RequestQueue.RequestQueue import RequestQueue


class TestEndpointUtility:
    @staticmethod
    def create_endpoint():
        return EndPoint("/test")

class TestEndpoint(unittest.TestCase):

    def test_creation(self):
        endpoint = TestEndpointUtility.create_endpoint()
        self.assertTrue(endpoint)

    def test_metadata(self):
        endpoint = TestEndpointUtility.create_endpoint()
        self.assertTrue(endpoint.path)
        self.assertTrue(endpoint.creation)

    def test_set_request_queue(self):
        endpoint = TestEndpointUtility.create_endpoint()
        endpoint.set_request_queue(RequestQueue())
        self.assertTrue(endpoint.has_request_queue())

    def test_process_request(self):
        endpoint = EndPoint("/test")
        request = RawRequest("/examplepath")
        self.assertRaises(Exception, endpoint.process_request, request)

        request_queue = RequestQueue()
        endpoint.set_request_queue(request_queue)
        guid = endpoint.process_request(request)

        self.assertEqual(type(guid), type("some_string"))

        self.assertEqual(endpoint.get_no_open_requests(), 1, msg="Should be 1")

    def test_no_open_request(self):
        endpoint = EndPoint("/test")
        request_queue = RequestQueue()
        endpoint.set_request_queue(request_queue)



        iterations = 21
        for i in range(iterations):
            endpoint.process_request(RawRequest(f"/{i}"))
            if i == 20:
                i = i

        print(endpoint.get_no_open_requests())

        self.assertEqual(endpoint.get_no_open_requests(), iterations, msg=f"Should be {iterations}")
