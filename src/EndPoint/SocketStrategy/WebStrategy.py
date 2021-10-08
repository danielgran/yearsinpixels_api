from abc import ABC, abstractmethod


class WebStrategy(ABC):

    request_callback = None

    @abstractmethod
    def setup_service(self, request_callback):
        pass

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def is_running(self):
        pass
