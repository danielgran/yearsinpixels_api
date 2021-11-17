import unittest

from yearsinpixels_api.RequestProcessor.Mapper.Mapper import Mapper


class MapperTest(unittest.TestCase):
    def setUp(self):
        self.mapper = Mapper()

    def test_is_there(self):
        self.assertIsNotNone(Mapper)

    def test_check_metadata(self):
        self.assertIsNotNone(self.mapper.queryobject)
