# Accepts the http request directly and sends it to specific endpoint method
from EndPoint.EndPoint import EndPoint


class WebHost:

    endpoints = {}

    def __init__(self, host):
        self.host = host

    def add_endpoint(self, endpoint):
        self.endpoints[endpoint.path] = endpoint

    def remove_endpoint(self, path):
        if self.endpoints.get(path):
            self.endpoints.pop(path)

    def handle_request(self, path, request_header, request_body):

        #

        if self.endpoints.get(path):


            EndPoint(self.endpoints.get(path))
        pass





