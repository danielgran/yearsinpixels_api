import unittest
from unittest.mock import MagicMock

from src.Request.Request import Request
from src.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from src.RequestQueue.RequestQueue import RequestQueue


class RequestQueueTest(unittest.TestCase):
    def setUp(self):
        self.requestQueue = RequestQueue()

    def test_is_there(self):
        self.assertIsNotNone(self.requestQueue)

    def test_add_ingoing_request(self):
        id = self.requestQueue.add_incoming_request(Request("/examplepath"))
        self.assertIsNotNone(id)

    def test_register_processor(self):
        g = GraphQLProcessor()
        self.requestQueue.reqister_processor("/examplepath", g)
        self.assertTrue(self.requestQueue.processors.get("/examplepath"))


    def test_notify_request_processor(self):
        g = GraphQLProcessor()

        g.process = MagicMock(return_value = ":-)")

        self.requestQueue.reqister_processor("/examplepath", g)

        self.requestQueue.add_incoming_request(Request("/examplepath"))

        g.process.assert_called()
