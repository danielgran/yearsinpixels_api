# Accepts the http request directly and sends it to specific endpoint method
from src.EndPoint.EndPoint import EndPoint


class WebHost:

    endpoints = {}
    exposeStrategy = None

    def __init__(self, host):
        self.host = host

    def setup_expose_strategy(self, strategy):
        self.exposeStrategy = strategy
        self.exposeStrategy.setup_service(self.handle_request)

    def run(self):
        self.exposeStrategy.run()


    def add_endpoint(self, endpoint):
        self.endpoints[endpoint.path] = endpoint

    def remove_endpoint(self, path):
        if self.endpoints.get(path):
            self.endpoints.pop(path)

    def handle_request(self, request):
        if self.endpoints.get(request.path):
            self.endpoints.get(request.path).process_request(request)
        else:
            raise Exception(f"No Endpoint with the responsiblilty '{request.path}'")







