import unittest

from src.RequestProcessor.QueryObject.Criteria.Criteria import Criteria


@unittest.skip
class CriteriaTest(unittest.TestCase):
    @staticmethod
    def check_metadata(test, criteria):
        test.assertIsNotNone(criteria.operator)
        test.assertIsNotNone(criteria.field)
        test.assertIsNotNone(criteria.value)

    def setUp(self):
        self.criteria = Criteria()

    def test_is_there(self):
        self.assertIsNotNone(Criteria)

    def test_attributes(self):
        self.check_metadata(self, self.criteria)

    def test_static_matches(self):
        match_criteria = Criteria.matches("value", "field")
        self.check_metadata(self, match_criteria)
        sql = match_criteria.generateSQL()
        self.assertIsNotNone(sql)
