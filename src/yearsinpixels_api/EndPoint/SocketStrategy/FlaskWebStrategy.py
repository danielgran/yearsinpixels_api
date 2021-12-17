from flask import Flask, request, Response

from yearsinpixels_api.EndPoint.SocketStrategy.WebStrategy import WebStrategy
from yearsinpixels_api.Request.HTMLHeader import HTMLHeader
from yearsinpixels_api.Request.Request import Request


class FlaskWebStrategy(WebStrategy):

    def __init__(self):
        # The request callback is the method processed further by the webhost. Flask Strategy just handles getting the data
        self.request_callback = None
        self.flask_app = None
        self.running = False
        self.flask_app = Flask("yip_backend")

    def is_running(self):
        return self.running

    def setup_service(self, request_callback):
        self.request_callback = request_callback
        self.flask_app.add_url_rule("/<path:path>", view_func=self.catch_options, methods=['OPTIONS'])
        self.flask_app.add_url_rule("/", view_func=self.catch_all_route , defaults={'path': ''})
        self.flask_app.add_url_rule("/<path:path>", view_func=self.catch_all_route, methods=['GET', 'POST'])

    def run(self):
        self.running = True
        self.flask_app.run(host="localhost", port=5555)

    def catch_options(self, path):
        return_headers = {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*', 'X-Stupid': 'No'}

        return '', 200, return_headers



    async def catch_all_route(self, path):
        backend_request = Request(request.path)

        backend_request.body = request.get_json()
        backend_request.header = HTMLHeader(dict(request.headers))
        backend_request.request_cookies = request.cookies.to_dict()
        backend_request.arguments = request.args.to_dict()

        response = self.request_callback(backend_request)


        return str(response.body), 200, {'Access-Control-Allow-Origin': '*', 'Content-Type': 'application/json'}
