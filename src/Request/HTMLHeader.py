class HTMLHeader:

    items = None

    def __init__(self, dict={}):
        self.items = dict

    def add_item(self, item):
        if self.items.get(item[0]):
            raise Exception("Header key already exists.")
        self.items[item[0]] = item[1]

    def remove_item(self, key):
        if self.items.get(key):
            self.items.pop(key)
        else:
            raise Exception("Key does not exist.")

    def get_content(self, key):
        if self.items.get(key):
            return self.items.get(key)
        raise Exception("Key does not exist.")
