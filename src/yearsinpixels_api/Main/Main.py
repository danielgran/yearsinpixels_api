from yearsinpixels_api.EndPoint.EndPoint import EndPoint
from yearsinpixels_api.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy
from yearsinpixels_api.Main.ConcreteFactory import ConcreteFactory
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_api.RequestQueue.RequestQueue import RequestQueue


def main():
    factory = ConcreteFactory()
    webhost = factory.CreateWebHost("localhost")
    setup_webhost(webhost)
    webhost.run()

def setup_webhost(webhost):
    expose_strategy = FlaskWebStrategy()
    data_request_queue = RequestQueue()

    graqh_ql_processor = GraphQLProcessor()

    data_request_queue.reqister_processor("/test", graqh_ql_processor)

    webhost.setup_expose_strategy(expose_strategy)

    test_endpoint = EndPoint("/test")
    test_endpoint.set_request_queue(request_queue=data_request_queue)

    webhost.add_endpoint(test_endpoint)

if __name__ == '__main__':
    main()