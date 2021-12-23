class Response:
    def __init__(self, request):
        self._request = request
        self.body = ""
        self.code = 0

    @property
    def request(self):
        return self._request

    def __repr__(self):
        return self.body
