from flask import Flask, request

from src.EndPoint.SocketStrategy.WebStrategy import WebStrategy
from src.Request.HTMLHeader import HTMLHeader
from src.Request.Request import Request


class FlaskWebStrategy(WebStrategy):

    def __init__(self):
        self.request_callback = None
        self.flask_app = None
        self.running = False
        self.flask_app = Flask("yip_backend")

    def is_running(self):
        return self.running

    def setup_service(self, request_callback):
        self.request_callback = request_callback
        self.flask_app.add_url_rule("/", view_func=self.catch_all_route , defaults={'path': ''})
        self.flask_app.add_url_rule("/<path:path>", view_func=self.catch_all_route)

    def run(self):
        self.running = True
        self.flask_app.run(host="localhost", port=8080)

    async def catch_all_route(self, path):
        backend_request = Request(request.path)

        backend_request.body = request.get_json()
        backend_request.header = HTMLHeader(dict(request.headers))
        backend_request.request_cookies = request.cookies.to_dict()
        backend_request.arguments = request.args.to_dict()

        req_guid = self.request_callback(backend_request)

        return req_guid
