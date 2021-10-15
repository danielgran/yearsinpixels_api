import unittest
import uuid

from src.EndPoint.EndPoint import EndPoint
from src.EndPoint.SocketStrategy.ConcreteTestStrategy import ConcreteTestStrategy
from src.Main.ConcreteFactory import ConcreteFactory
from src.Request.RawRequest import RawRequest
from src.RequestQueue.RequestQueue import RequestQueue


class WebHostUtility:

    @staticmethod
    def create_factory():
        return ConcreteFactory()

    @staticmethod
    def create_webhost():
        hostname = "localhost"
        webhost = WebHostUtility.create_factory().CreateWebHost(hostname)
        endpoint = EndPoint("/examplepath")
        request_queue = RequestQueue()
        endpoint.set_request_queue(request_queue)
        webhost.add_endpoint(endpoint)
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

    def test_setup_expose_strategy(self):
        webhost = WebHostUtility.create_webhost()
        testStrategy = ConcreteTestStrategy()
        webhost.setup_expose_strategy(testStrategy)
        self.assertTrue(webhost.exposeStrategy, "Webhost does not have an exposeStrategy")

    def test_run_host(self):
        webhost = WebHostUtility.create_webhost()
        testStrategy = ConcreteTestStrategy()
        webhost.setup_expose_strategy(testStrategy)
        webhost.run()

    def test_handle_request(self):
        webhost = WebHostUtility.create_webhost()
        teststrategy = ConcreteTestStrategy()
        webhost.setup_expose_strategy(teststrategy)
        request = RawRequest("/examplepath")
        guid = webhost.handle_request(request)

        self.assertEqual(type(guid), type("some_string"))


        request.path = "/thisshouldnotwork"
        self.assertRaises(Exception, webhost.handle_request, request)



