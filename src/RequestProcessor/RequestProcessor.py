from abc import ABC, abstractmethod

from src.Request.Response import Response


class RequestProcessor(ABC):
    @abstractmethod
    def process(self, request) -> Response:
        pass
