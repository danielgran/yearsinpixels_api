from Entity.User import User

from src.EndPoint.EndPoint import EndPoint
from src.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy
from src.Main.ConcreteFactory import ConcreteFactory
from src.RequestQueue.RequestQueue import RequestQueue


def main():
    fac = ConcreteFactory()
    webhost = fac.CreateWebHost("localhost")
    setup_webhost(webhost)



    webhost.run()



def setup_webhost(webhost):
    expose_strategy = FlaskWebStrategy()

    request_queue = RequestQueue()

    webhost.setup_expose_strategy(expose_strategy)

    test_endpoint = EndPoint("/test")
    test_endpoint.set_request_queue(request_queue=request_queue)
    webhost.add_endpoint(test_endpoint)


if __name__ == '__main__':
    main()
