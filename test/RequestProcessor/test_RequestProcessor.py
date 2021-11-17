import unittest

from yearsinpixels_api.RequestProcessor.RequestProcessor import RequestProcessor


class TestRequestProcessor(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(RequestProcessor)

    def test_process(self):
        self.assertIsNotNone(RequestProcessor.process)
