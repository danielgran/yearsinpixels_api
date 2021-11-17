import uuid


class RequestQueue:
    def __init__(self):
        self.ingoing_queue = dict()
        self.response_queue = dict()
        self.processors = dict()

    def __len__(self):
        return len(self.ingoing_queue)

    def add_incoming_request(self, incoming_request):
        guid = str(uuid.uuid4())
        incoming_request.guid = guid
        self.ingoing_queue[guid] = incoming_request
        self.notify_processor(incoming_request)
        return incoming_request.guid

    def reqister_processor(self, path, processor):
        self.processors[path] = processor

    def notify_processor(self, request):
        if self.processors.get(request.path):
            self.response_queue[request.guid] = self.processors.get(request.path).process(request)

    def get_response(self, request_id):
        response = self.response_queue.get(request_id)
        return response
