class WebHost:
    def __init__(self, host):
        self.host = host
        self.endpoints = {}
        self.exposeStrategy = None

    def setup_expose_strategy(self, strategy):
        self.exposeStrategy = strategy
        self.exposeStrategy.setup_service(self.handle_request)

    def run(self):
        self.exposeStrategy.run()

    def add_endpoint(self, endpoint):
        if endpoint.path in self.endpoints.keys():
            raise Exception("Endpoint already exists.")
        self.endpoints[endpoint.path] = endpoint

    def has_endpoint(self, path):
        if path in self.endpoints.keys():
            return True
        return False

    def remove_endpoint(self, path):
        if self.has_endpoint(path):
            self.endpoints.pop(path)
        else:
            raise Exception("Endpoint does not exist.")

    def handle_request(self, request):
        if self.endpoints.get(request.path):
            response = self.endpoints.get(request.path).process_request(request)
            return str(response)
        else:
            raise Exception(f"No Endpoint with the responsiblilty '{request.path}'")
