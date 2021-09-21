import unittest

from RequestQueue.RequestQueue import RequestQueue


class RequestQueueTest(unittest.TestCase):

    def test_nothing(self):
        self.assertTrue(True)

    def test_creation(self):
        requestQueue = RequestQueue()

    def test_add_ingoing_request(self):
        requestQueue = RequestQueue()
        requestQueue.add_incoming_reqeuest(Request)

