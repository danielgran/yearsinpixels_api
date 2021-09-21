# Accepts the http request and adds it to the request queue

class WebHost:

    endpoints = {}

    def __init__(self, host):
        self.host = host

    def add_endpoint(self, endpoint):
        self.endpoints[endpoint.path] = endpoint

    def remove_endpoint(self, path):
        if self.endpoints.get(path):
            self.endpoints.pop(path)
