from abc import ABC


class DataResolver(ABC):

    def __init__(self, mapper):
        self.mapper = mapper

    def resolve_data(self):
        pass
