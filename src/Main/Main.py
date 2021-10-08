from Entity.User import User

from src.EndPoint.EndPoint import EndPoint
from src.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy
from src.Main.ConcreteFactory import ConcreteFactory


def main():
    fac = ConcreteFactory()
    webhost = fac.CreateWebHost("localhost")
    setup_webhost(webhost)



    webhost.run()


def tmp():
    return "hi"


def setup_webhost(webhost):
    expose_strategy = FlaskWebStrategy()
    expose_strategy.setup_service(tmp)
    webhost.setup_expose_strategy(expose_strategy)

    test_endpoint = EndPoint("/test")
    webhost.add_endpoint(test_endpoint)


if __name__ == '__main__':
    main()
