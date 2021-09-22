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
        webhost = WebHostUtility.create_factory().CreateWebHost(hostname)
        webhost.add_endpoint(EndPoint("/examplepath"))
        return webhost

    @staticmethod
    def sample_header():
        return {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "sec-gpc": "1",
            "upgrade-insecure-requests": "1"
        }


class TestWebHost(unittest.TestCase):

    def test_isthere(self):
        webhost = WebHostUtility.create_factory().CreateWebHost("localhost")
        self.assertTrue(webhost)

    def test_addEndpoint(self):
        webhost = WebHostUtility.create_webhost()
        self.assertTrue(webhost.endpoints["/examplepath"])

    def test_add_duplicate_endpoint(self):
        webhost = WebHostUtility.create_webhost()
        webhost.add_endpoint(EndPoint("/examplepath"))
        if len(webhost.endpoints) > 1:
            self.assertTrue(False, "Endoint names should be unique!")

        print(webhost.endpoints)

    def test_remove_endpoint(self):
        webhost = WebHostUtility.create_webhost()
        webhost.remove_endpoint("/examplepath")
        self.assertTrue(len(webhost.endpoints) == 0, 'Endpoint did not get removed');
        webhost.remove_endpoint("/thisEndpointDoesNotExist")

    def test_handle_request(self):
        webhost = WebHostUtility.create_webhost()
        webhost.handle_request("/examplepath", WebHostUtility.sample_header(), "request_body")
        # test the queue behavior

