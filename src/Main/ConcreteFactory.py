from src.EndPoint.WebHost import WebHost


class ConcreteFactory:

    def __init__(self):
        pass

    @staticmethod
    def CreateWebHost(hostname):
        return WebHost(hostname)
