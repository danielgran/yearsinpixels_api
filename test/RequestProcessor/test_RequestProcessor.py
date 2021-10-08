import unittest

from src.RequestProcessor.RequestProcessor import RequestProcessor


class TestRequestProcessor(unittest.TestCase):

    def test_is_there(self):
        self.assertIsNotNone(RequestProcessor)
        self.assertIsNotNone(RequestProcessor.process)

