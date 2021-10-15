class RawRequest:
    def __init__(self, path=None):
        self.path = path
        self.header = {}
        self.body = ""
