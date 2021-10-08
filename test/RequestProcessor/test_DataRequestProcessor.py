import unittest

from src.Request.DataRequest import DataRequest
from src.RequestProcessor.DataRequestProcessor import DataRequestProcessor


class TestDataRequestProcessor(unittest.TestCase):
    def test_is_there(self):
        self.assertIsNotNone(DataRequestProcessor)

    def test_process_data(self):
        drp = DataRequestProcessor()
        rq = DataRequest()
        drp.process(rq)