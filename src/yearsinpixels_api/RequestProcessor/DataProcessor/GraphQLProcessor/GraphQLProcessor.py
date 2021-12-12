from datetime import date
from pathlib import Path

from ariadne import make_executable_schema, graphql_sync, ObjectType, load_schema_from_path

from yearsinpixels_api.Request.Response import Response
from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.User import User
from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria


class GraphQLProcessor(DataProcessor):

    def __init__(self):
        self.mappers = dict()
        self.query = ObjectType("Query")
        self.query.set_field("user", self.resolve_user)
        self.query.set_field("days", self.resolve_days)

        self.mutation = ObjectType("Mutation")
        self.mutation.set_field("register", self.register)
        self.mutation.set_field("login", self.login)
        self.mutation.set_field("create_day", self.create_day)

        path = Path(__file__)
        path = path.parent.resolve()
        self.path = f"{path}/schema.graphql"

        self.update_schema()

    def update_schema(self):
        self.schema = make_executable_schema(
            load_schema_from_path(self.path),
            self.query,
            self.mutation
        )

    def process(self, request):
        # validate request header
        # google captcha
        response = Response(request)

        success, result = graphql_sync(
            data=request.body,
            schema=self.schema,
            debug=__debug__
        )

        return_string = str(result)
        response.body = return_string

        return response

    def set_mapper(self, business_class, user_mapper):
        self.mappers[business_class] = user_mapper

    def resolve_user(self, obj, info, user_guid):
        user = self.mappers[User].find(Criteria.matches("guid", user_guid))
        return user

    def resolve_days(self, obj, info, user_guid):
        user_from_database = self.mappers[User].find(Criteria.matches("guid", user_guid))
        days = self.mappers[Day].find_all_from_user(Criteria.matches("id_user", user_from_database.id))
        moods = self.mappers[Mood].find_all()
        for day in days:
            mood1_for_day = next(mood for mood in moods if day.id_mood1 == mood.id)
            day.mood1 = mood1_for_day
        return days

    def register(self, obj, info, email, password):
        result = {
            "success": True,
            'text': ""
        }

    def login(self, obj, info, email, password):
        # jwt must contain guid of user

        login_result = {
            'success': True,
            'message': '',
            'jwt': ''

        }

    def create_day(self, obj, info, user_guid, day):
        user = self.mappers[User].find(Criteria.matches("guid", user_guid))
        if user is None:
            return {
                "success": False,
                "text": "Invalid user_guid."
            }

        try:
            title = day['title']
            notes = day['notes']
            date_of_day = date(day['date']['year'], day['date']['month'], day['date']['day'])
            id_mood1 = day['id_mood1']
            day = Day()
            day.id_user = user.id
            day.date = date_of_day
            day.title = title
            day.notes = notes
            day.id_mood1 = id_mood1
        except Exception:
            return {
                "success": False,
                'text': "Error parsing data."
            }

        self.mappers[Day].add(day)
        return {
            "success": True,
            'text': ""
        }
