from abc import ABC, abstractmethod


class WebStrategy(ABC):

    def __init__(self):
        self.request_callback = None

    @abstractmethod
    def setup_service(self, request_callback):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def is_running(self):
        pass
