from src.EndPoint.WebHost import WebHost


class ConcreteFactory:
    @staticmethod
    def CreateWebHost(hostname):
        return WebHost(hostname)
