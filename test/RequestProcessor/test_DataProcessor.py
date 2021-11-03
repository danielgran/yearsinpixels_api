import unittest

from src.RequestProcessor.DataProcessor import DataProcessor


class DataProcessorTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DataProcessor)

    def test_is_processor(self):
        self.assertIsNotNone(DataProcessor.process)