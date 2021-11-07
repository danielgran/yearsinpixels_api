from ariadne.constants import PLAYGROUND_HTML

from src.Request.Response import Response
from src.RequestProcessor.DataProcessor.DataProcessor import DataProcessor


class GraphQLProcessor(DataProcessor):

    def process(self, request):
        # temporary
        html = PLAYGROUND_HTML

        response = Response(request)

        response.body = "Mock"

        return response
        # end temporary

