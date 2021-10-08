import uuid


class RequestQueue:

    ingoing_queue = {}
    outgoing_queue = {}

    def __init__(self):
        pass

    def __len__(self):
        return len(self.ingoing_queue)

    def add_incoming_request(self, incoming_request):
        guid = str(uuid.uuid4())
        self.ingoing_queue[guid] = incoming_request
        return guid

    def add_processor(self, processor):
        pass

