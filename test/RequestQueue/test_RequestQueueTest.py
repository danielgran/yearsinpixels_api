import unittest

from src.Request.RawRequest import RawRequest
from src.RequestQueue.RequestQueue import RequestQueue


class RequestQueueTest(unittest.TestCase):

    def test_creation(self):
        requestQueue = RequestQueue()
        self.assertIsNotNone(requestQueue)

    def test_add_ingoing_request(self):
        requestQueue = RequestQueue()
        id = requestQueue.add_incoming_request(RawRequest("/examplepath"))
        self.assertTrue(id)






