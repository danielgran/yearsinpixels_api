import unittest

from yearsinpixels_api.Request.HTMLHeader import HTMLHeader
from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_business.Entity.User import User
from yearsinpixels_data.Gateway.TestGateway import TestGateway
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

    def test_validate_token_with_user(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2d1aWQiOiIxNzc0Mzc1NC01MTkyLTQyM2YtYTVhYi0xNzk3ZmI2NzQwODEiLCJleHBpcmVzIjoxNjQwMzU3OTA3fQ.0Jsnw3k44U6jNiqwFhgtePX_KXR_euzbCLkP1bzfqM8"
        user_guid = "17743754-5192-423f-a5ab-1797fb674081"
        header = HTMLHeader()
        header.items["Authorization"] = "Bearer " + token
        context = {
            "request_header": header
        }

        class info_context:
            def __init__(self, context):
                self.context = context

        self.graphql_processor.validate_token_with_user(info_context(context), user_guid)
