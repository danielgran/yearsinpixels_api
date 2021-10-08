from src.EndPoint.SocketStrategy.WebStrategy import WebStrategy


class ConcreteTestStrategy(WebStrategy):

    isrunning = False
    callback = None

    def is_running(self):
        return self.isrunning

    def open_service(self, request_callback):
        self.isrunning = True
        self.callback = request_callback

    def simulate_request(self, path, header, body):
        if self.callback:
            self.callback(path, header, body)

    def __init__(self):
        pass
