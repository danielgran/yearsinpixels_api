import unittest

from src.Request.Request import Request
from src.Request.Response import Response
from src.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from src.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor


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
        response = graphql_processor.process(Request("Test"))
        self.assertTrue(isinstance(response, Response))

