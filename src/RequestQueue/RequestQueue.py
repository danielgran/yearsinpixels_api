import uuid


class RequestQueue:

    ingoing_queue = None
    outgoing_queue = None

    def __init__(self):
        self.ingoing_queue = {}
        self.outgoing_queue = {}

    def __len__(self):
        return len(self.ingoing_queue)

    def add_incoming_request(self, incoming_request):
        guid = str(uuid.uuid4())
        self.ingoing_queue[guid] = incoming_request
        return guid # todo would it not be better to have it return an request object to then await some state in the webstrategy to return?

    def add_processor(self, processor):
        pass

