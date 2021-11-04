import unittest

from src.RequestProcessor.DataProcessor.DataProcessor import DataProcessor


class DataProcessorTest(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DataProcessor)