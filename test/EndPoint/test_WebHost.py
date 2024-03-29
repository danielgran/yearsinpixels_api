import unittest
from unittest.mock import MagicMock

from yearsinpixels_api.EndPoint.EndPoint import EndPoint
from yearsinpixels_api.EndPoint.SocketStrategy.ConcreteTestStrategy import ConcreteTestStrategy
from yearsinpixels_api.EndPoint.WebHost import WebHost
from yearsinpixels_api.Request.Request import Request
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_api.RequestQueue.RequestQueue import RequestQueue


class WebHostUtility:
    @staticmethod
    def create_webhost():
        hostname = "localhost"
        webhost = WebHost(hostname)
        endpoint = EndPoint("/examplepath")
        request_queue = RequestQueue()
        test_processor = GraphQLProcessor()
        request_queue.reqister_processor("/examplepath", test_processor)
        endpoint.set_request_queue(request_queue)
        webhost.add_endpoint(endpoint)
        return webhost

    @staticmethod
    def setup_webhost_test_strategy(webhost):
        testStrategy = ConcreteTestStrategy()
        webhost.setup_expose_strategy(testStrategy)

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
    def setUp(self):
        self.webhost = WebHostUtility.create_webhost()

    def test_is_there(self):
        self.assertTrue(self.webhost)

    def test_addEndpoint(self):
        self.webhost.add_endpoint(EndPoint("/newlyaddedendpoint"))
        self.assertTrue("/newlyaddedendpoint" in self.webhost.endpoints.keys())
        self.assertRaises(Exception, self.webhost.add_endpoint, EndPoint("/newlyaddedendpoint"))

    def test_has_endpoint(self):
        self.assertTrue(self.webhost.has_endpoint("/examplepath"))

    def test_remove_endpoint(self):
        self.webhost.remove_endpoint("/examplepath")
        self.assertTrue(len(self.webhost.endpoints) == 0, 'Endpoint did not get removed');
        self.assertRaises(Exception, self.webhost.remove_endpoint, "/thisEndpointDoesNotExist")

    def test_setup_expose_strategy(self):
        WebHostUtility.setup_webhost_test_strategy(self.webhost)
        self.assertIsNotNone(self.webhost.exposeStrategy, "Webhost does not have an exposeStrategy")

    def test_run_host(self):
        WebHostUtility.setup_webhost_test_strategy(self.webhost)
        self.webhost.run()

    def test_handle_request(self):
        WebHostUtility.setup_webhost_test_strategy(self.webhost)
        request = Request("/examplepath")

        self.webhost.endpoints.get(request.path).process_request = MagicMock()

        self.webhost.handle_request(request)
        self.assertTrue(self.webhost.endpoints.get(request.path).process_request.called)

    def test_handle_request_with_unknown_path(self):
        WebHostUtility.setup_webhost_test_strategy(self.webhost)
        request = Request("/examplepath")
        self.assertRaises(Exception, self.webhost.handle_request, request)
