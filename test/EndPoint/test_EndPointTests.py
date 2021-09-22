import unittest

from src.EndPoint.EndPoint import EndPoint


class TestEndpointUtility:
    @staticmethod
    def create_endpoint():
        return EndPoint("/test")

class TestEndpoint(unittest.TestCase):

    def test_creation(self):
        endpoint = TestEndpointUtility.create_endpoint()
        self.assertTrue(endpoint)

    def test_getmetadata(self):
        endpoint = TestEndpointUtility.create_endpoint()
        self.assertTrue(endpoint.path)
        self.assertTrue(endpoint.creation)
