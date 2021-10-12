class HTMLHeader:
    def __init__(self, dictionary=None):
        if dictionary is None:
            dictionary = dict()
        self.items = dictionary

    def add_item(self, item):
        if item[0] in self.items.keys():
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
