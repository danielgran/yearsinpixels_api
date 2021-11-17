from yearsinpixels_api.EndPoint.SocketStrategy.WebStrategy import WebStrategy


class ConcreteTestStrategy(WebStrategy):

    def __init__(self):
        self.running = False
        self.callback = None

    def is_running(self):
        return self.running

    def setup_service(self, request_callback):
        self.callback = request_callback

    def run(self):
        self.running = True

    def simulate_request(self, path, header, body):
        if self.callback:
            self.callback(path, header, body)
