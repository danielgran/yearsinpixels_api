from ariadne.constants import PLAYGROUND_HTML

from src.RequestProcessor.DataProcessor.DataProcessor import DataProcessor


class GraphQLProcessor(DataProcessor):

    def process(self):
        # temporary
        html = PLAYGROUND_HTML
        return html
        # end temporary

