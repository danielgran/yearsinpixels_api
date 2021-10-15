import time


class EndPoint:
    def __init__(self, path):
        self.creation = time.time()
        self.request_queue = None
        self.path = path

    def process_request(self, request):
        if self.request_queue is None:
            raise Exception("No request queue found.")
        else:
            return self.request_queue.add_incoming_request(request)

    def set_request_queue(self, request_queue):
        self.request_queue = request_queue

    def has_request_queue(self):
        if self.request_queue is None:
            return False
        return True

    def get_no_open_requests(self) :
        return len(self.request_queue)
