import unittest

from src.RequestProcessor.GraphQLDataProcessorStrategy.AriadneStrategy import AriadneStrategy


class test_AriadneStrategy(unittest.TestCase):

    def test_is_there(self):
        self.assertIsNotNone(AriadneStrategy)



