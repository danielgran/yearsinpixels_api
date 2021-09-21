import unittest

from Request.Request import Request
from RequestQueue.RequestQueue import RequestQueue


class RequestQueueTest(unittest.TestCase):

    def test_nothing(self):
        self.assertTrue(True)

    def test_creation(self):
        requestQueue = RequestQueue()

    def test_add_ingoing_request(self):
        requestQueue = RequestQueue()
        id = requestQueue.add_incoming_request(Request())

        self.assertTrue(id)


