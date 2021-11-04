from src.RequestProcessor.QueryObject.Criteria.Criteria import Criteria


class MatchCriteria(Criteria):
    def __init__(self, field, value):
        super(MatchCriteria, self).__init__(field, value)

    def generate_SQL(self):
        return f"{self.field} = {self.value}";
