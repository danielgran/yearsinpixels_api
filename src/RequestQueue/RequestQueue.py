import uuid


class RequestQueue:
    def __init__(self):
        self.ingoing_queue = dict()
        self.outgoing_queue = dict()
        self.processors = dict()

    def __len__(self):
        return len(self.ingoing_queue)

    def add_incoming_request(self, incoming_request):
        guid = str(uuid.uuid4())
        self.ingoing_queue[guid] = incoming_request
        self.notify_processor(incoming_request)
        return guid # todo would it not be better to have it return an request object to then await some state in the webstrategy to return?

    def reqister_processor(self, path, processor):
        self.processors[path] = processor

    def notify_processor(self, request):
        if (self.processors.get(request.path)):
            self.processors.get(request.path).process(request)
