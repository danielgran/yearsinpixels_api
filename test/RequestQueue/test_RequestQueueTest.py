import unittest

from src.Request.RawRequest import RawRequest
from src.RequestQueue.RequestQueue import RequestQueue


class RequestQueueTest(unittest.TestCase):
    def setUp(self):
        self.requestQueue = RequestQueue()

    def test_is_there(self):
        self.assertIsNotNone(self.requestQueue)

    def test_add_ingoing_request(self):
        id = self.requestQueue.add_incoming_request(RawRequest("/examplepath"))
        self.assertIsNotNone(id)
