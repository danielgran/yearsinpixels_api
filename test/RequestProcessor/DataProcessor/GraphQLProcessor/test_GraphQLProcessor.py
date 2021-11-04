import unittest

from src.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from src.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor


class GraphQLProcessorTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(GraphQLProcessor)

    def test_is_data_processor(self):
        self.assertTrue(issubclass(GraphQLProcessor, DataProcessor))
