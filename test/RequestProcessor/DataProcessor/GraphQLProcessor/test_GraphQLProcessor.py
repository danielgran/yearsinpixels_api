import unittest

from yearsinpixels_data.Gateway.TestGateway import TestGateway

from yearsinpixels_business.Entity.User import User
from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_data.Mapper.UserMapper import UserMapper


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

    def test_set_mapper(self):
        test_gateway = TestGateway()
        user_mapper = UserMapper(test_gateway)
        self.graphql_processor.set_mapper(User, user_mapper)
        self.assertTrue(user_mapper in self.graphql_processor.mappers.values())

    def test_existent_user_query(self):
        self.assertIsNotNone('user' in self.graphql_processor.query._resolvers.keys())

    def test_existent_mutation_register(self):
        self.assertIsNotNone('register' in self.graphql_processor.mutation._resolvers.keys())

    def test_existent_mutation_login(self):
        self.assertIsNotNone('login' in self.graphql_processor.mutation._resolvers.keys())

    def test_existent_mutation_create_day(self):
        self.assertIsNotNone('create_day' in self.graphql_processor.mutation._resolvers.keys())

    def test_resolve_user(self):
        test_gateway = TestGateway()
        user_mapper = UserMapper(test_gateway)
        user = User()
        user_mapper.add(user)
        self.graphql_processor.set_mapper(User, user_mapper)

        resolved_user = self.graphql_processor.resolve_user(None, None, user.guid)

        self.assertTrue(user == resolved_user)