from pathlib import Path

from ariadne import make_executable_schema, graphql_sync, ObjectType, load_schema_from_path

from yearsinpixels_api.Request.Response import Response
from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from yearsinpixels_business.Entity.User import User
from yearsinpixels_data.QueryObject.Criteria.Criteria import Criteria


class GraphQLProcessor(DataProcessor):

    def __init__(self):
        self.mappers = dict()
        self.query = ObjectType("Query")
        self.query.set_field("user", self.resolve_user)

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


    def resolve_user(self, obj, info, guid):
        user = self.mappers[User].find(Criteria.matches("guid", guid))
        return user

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

    def create_day(self, ob, info, day):
        return {
            "success": True,
            'text': ""
        }

