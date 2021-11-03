class Criteria:
    def __init__(self, a,b):
        self.operator = ""
        self.field = ""
        self.value = ""

    def generateSQL(self):
        pass

    @staticmethod
    def matches(field, value):
        from src.RequestProcessor.QueryObject.Criteria.MatchCriteria import MatchCriteria
        match_criteria = MatchCriteria(field, value)
        return match_criteria


