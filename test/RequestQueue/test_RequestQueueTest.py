import unittest

from src.Request.Request import Request
from src.RequestQueue.RequestQueue import RequestQueue


class RequestQueueTest(unittest.TestCase):

    def test_creation(self):
        requestQueue = RequestQueue()
        self.assertTrue(requestQueue)

    def test_add_ingoing_request(self):
        requestQueue = RequestQueue()
        id = requestQueue.add_incoming_request(Request("/examplepath"))
        self.assertTrue(id)






