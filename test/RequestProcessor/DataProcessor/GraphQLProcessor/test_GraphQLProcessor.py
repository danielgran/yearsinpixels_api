import unittest

from yearsinpixels_api.Request.Request import Request
from yearsinpixels_api.Request.Response import Response
from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor


class GraphQLProcessorTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(GraphQLProcessor)

    def test_is_data_processor(self):
        self.assertTrue(issubclass(GraphQLProcessor, DataProcessor))

    def test_creation(self):
        graphql_processor = GraphQLProcessor()
        self.assertTrue(graphql_processor.schema)
        self.assertTrue(graphql_processor.query)
        self.assertTrue(graphql_processor.mutation)

    def test_proper_process(self):
        graphql_processor = GraphQLProcessor()
        request = Request("/test")
        request.body = {'query': 'mutation {\n    register(email: "some.user@mail.de")\n}'}
        response = graphql_processor.process(request)
        self.assertTrue(isinstance(response, Response))
