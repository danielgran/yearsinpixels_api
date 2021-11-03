import unittest

from src.RequestProcessor.QueryObject.Criteria.MatchCriteria import MatchCriteria


class MatchCriteriaTest(unittest.TestCase):
    def setUp(self):
        self.criteria = MatchCriteria("field", "value")

    def test_is_there(self):
        self.assertIsNotNone(MatchCriteria)
        self.assertIsNotNone(self.criteria)

    def test_generate_sql(self):
        sql = self.criteria.generate_SQL()
        self.assertTrue(isinstance(sql, str))
