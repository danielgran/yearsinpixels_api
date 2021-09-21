import unittest

from EndPoint.EndPoint import EndPoint
from Main.ConcreteFactory import ConcreteFactory


class WebHostUtility:

    @staticmethod
    def create_factory():
        return ConcreteFactory()

    @staticmethod
    def create_webhost():
        hostname = "localhost"
        return WebHostUtility.create_factory().CreateWebHost(hostname);


class TestWebHost(unittest.TestCase):

    def test_isthere(self):
        webhost = WebHostUtility.create_webhost()
        self.assertTrue(webhost)

    def test_addEndpoint(self):
        webhost = WebHostUtility.create_webhost()
        webhost.add_endpoint(EndPoint("/examplepath"))
        self.assertTrue(webhost.endpoints["/examplepath"])

    def test_add_duplicate_endpoint(self):
        webhost = WebHostUtility.create_webhost()
        webhost.add_endpoint(EndPoint("/examplepath"))
        webhost.add_endpoint(EndPoint("/examplepath"))
        if len(webhost.endpoints) > 1:
            self.assertTrue(False, "Endoint names should be unique!")

        print(webhost.endpoints)

    def test_remove_endpoint(self):
        webhost = WebHostUtility.create_webhost()
        webhost.add_endpoint(EndPoint("/examplepath"))
        webhost.remove_endpoint("/examplepath")
        self.assertTrue(len(webhost.endpoints) == 0, 'Endpoint did not get removed');
        webhost.remove_endpoint("/thisEndpointDoesNotExist")


