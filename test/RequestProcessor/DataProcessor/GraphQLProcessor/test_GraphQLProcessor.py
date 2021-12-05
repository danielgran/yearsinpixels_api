import unittest

from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.DataResolver.UserResolver import UserResolver
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_business.Entity.User import User


class GraphQLProcessorTest(unittest.TestCase):
    def setUp(self):
        self.graphql_processor = GraphQLProcessor()

    def test_is_there(self):
        self.assertIsNotNone(GraphQLProcessor)

    def test_is_data_processor(self):
        self.assertTrue(issubclass(GraphQLProcessor, DataProcessor))

    def test_creation(self):
        self.assertTrue(self.graphql_processor.schema)
        self.assertTrue(self.graphql_processor.query)
        self.assertTrue(self.graphql_processor.mutation)

    def test_update_schema(self):
        self.graphql_processor.update_schema()

    def test_existent_resolver_list(self):
        self.assertIsNotNone(self.graphql_processor.resolvers)

    def test_add_resolver(self):
        user_resolver = UserResolver()
        self.graphql_processor.add_resolver(User, user_resolver)
        self.assertTrue(user_resolver in self.graphql_processor.resolvers.values())
