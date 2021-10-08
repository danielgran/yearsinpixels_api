from flask import Flask, request

from src.EndPoint.SocketStrategy.WebStrategy import WebStrategy


class FlaskWebStrategy(WebStrategy):

    request_callback = None
    flask_app = None
    is_running = False


    def __init__(self):
        self.flask_app = Flask("yip_backend")


    def is_running(self):
        return self.is_running


    def setup_service(self, request_callback):
        self.request_callback = request_callback
        self.flask_app.add_url_rule("/", view_func=self.catch_all_route, defaults={'path': ''})
        self.flask_app.add_url_rule("/<path:path>", view_func=self.catch_all_route)


    def open_service(self):
        self.flask_app.run(host="localhost", port=8080)


    def catch_all_route(self, path):
        request_path = path

        self.request_callback(None)


        return request_path

