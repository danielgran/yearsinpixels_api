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
        request.body = {'query': 'mutation {\n    register(email: "daniel.gran")\n}'}

        request_id = self.requestQueue.add_incoming_request(request)
        response = self.requestQueue.get_response(request_id)

        self.assertIsNotNone(response, "Response None after processing")
