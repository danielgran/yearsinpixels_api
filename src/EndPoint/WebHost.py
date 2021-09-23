# Accepts the http request directly and sends it to specific endpoint method
from src.EndPoint.EndPoint import EndPoint


class WebHost:

    endpoints = {}
    exposeStrategy = None

    def __init__(self, host):
        self.host = host

    def setup_expose_strategy(self, strategy):
        self.exposeStrategy = strategy
        strategy.open_service(self.handle_request)

    def add_endpoint(self, endpoint):
        self.endpoints[endpoint.path] = endpoint

    def remove_endpoint(self, path):
        if self.endpoints.get(path):
            self.endpoints.pop(path)

