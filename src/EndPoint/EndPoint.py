import time


class EndPoint:

    creation = time.time()
    request_queue = None

    def __init__(self, path):
        self.path = path

    pass

    def process_request(self, request):
        if self.request_queue is None:
            raise Exception("No request queue found.")
        else:
            self.request_queue.add_incoming_request(request)

    def set_request_queue(self, request_queue):
        self.request_queue = request_queue

    def has_request_queue(self):
        if self.request_queue is not None:
            return True
        else:
            return False


    def get_no_open_requests(self):
        return len(self.request_queue)
