class Request:
    def __init__(self, path=None):

        if path is None:
            raise Exception("Path can not be None.")
        else:
            self.path = path

        self.header = dict()
        self.request_cookies = dict()
        self.arguments = dict()
