import unittest
from abc import ABC

from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.DataResolver.DataResolver import DataResolver
from yearsinpixels_data.Gateway.TestGateway import TestGateway
from yearsinpixels_data.Mapper.UserMapper import UserMapper


class DataResolverTest(unittest.TestCase):
    def setUp(self):
        gateway = TestGateway()
        usermapper = UserMapper(gateway)
        self.resolver = DataResolver(usermapper)

    def test_is_there(self):
        self.assertIsNotNone(DataResolver)

    def test_member_variables(self):
        self.assertIsNotNone(self.resolver.mapper)

    def test_existant_resolve_methods(self):
        self.assertIsNotNone(self.resolver.resolve_data)

    def test_abstraction(self):
        self.assertTrue(issubclass(DataResolver, ABC))
