class Response:
    def __init__(self, request):
        self._request = request

    @property
    def request(self):
        return self._request
