import unittest
from unittest.mock import MagicMock

from yearsinpixels_api.Request.Request import Request
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_api.RequestQueue.RequestQueue import RequestQueue


class RequestQueueTest(unittest.TestCase):
    def setUp(self):
        self.requestQueue = RequestQueue()

    def test_is_there(self):
        self.assertIsNotNone(self.requestQueue)

    def test_add_ingoing_request(self):
        id = self.requestQueue.add_incoming_request(Request("/examplepath"))
        self.assertIsNotNone(id)

    def test_register_processor(self):
        graphql_processor = GraphQLProcessor()
        self.requestQueue.reqister_processor("/examplepath", graphql_processor)

        self.assertTrue(self.requestQueue.processors.get("/examplepath"))

    def test_notify_request_processor(self):
        graphql_processor = GraphQLProcessor()
        graphql_processor.process = MagicMock()

        self.requestQueue.reqister_processor("/examplepath", graphql_processor)
        self.requestQueue.add_incoming_request(Request("/examplepath"))
        self.assertTrue(graphql_processor.process.called, "Request Processor did not get called.")

    def test_get_request_response(self):
        graphql_processor = GraphQLProcessor()
        self.requestQueue.reqister_processor("/examplepath", graphql_processor)
        request = Request("/examplepath")
        # mock
        graphql_processor.process = MagicMock(return_value = "Edsger Dijkstra")

        request_id = self.requestQueue.add_incoming_request(request)
        response = self.requestQueue.get_response(request_id)

        self.assertTrue(response == "Edsger Dijkstra", "Request response was not right.")