from Entity.User import User

from src.EndPoint.EndPoint import EndPoint
from src.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy
from src.Main.ConcreteFactory import ConcreteFactory


def main():
    fac = ConcreteFactory()
    webhost = fac.CreateWebHost("localhost")
    setup_webhost(webhost)

    expose_strat = FlaskWebStrategy()
    expose_strat.setup_service(tmp)

    webhost.setup_expose_strategy(expose_strat)


def tmp():
    return "hi"


def setup_webhost(webhost):
    test_endpoint = EndPoint("/test")
    webhost.add_endpoint(test_endpoint)




if __name__ == '__main__':
    main()
