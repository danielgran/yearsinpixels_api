from abc import ABC, abstractmethod

from yearsinpixels_api.Request.Response import Response


class RequestProcessor(ABC):
    @abstractmethod
    def process(self, request) -> Response:
        pass
