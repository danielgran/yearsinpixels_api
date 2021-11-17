import unittest

from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor


class DataProcessorTest(unittest.TestCase):
    def setUp(self):
        self.dataprocessor = DataProcessor

    def test_is_there(self):
        self.assertIsNotNone(DataProcessor)

    def test_metadata(self):
        self.assertIsNotNone(self.dataprocessor.process)