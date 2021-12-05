from pathlib import Path

from ariadne import make_executable_schema, graphql_sync, ObjectType, load_schema_from_path

from yearsinpixels_api.Request.Response import Response
from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor
from yearsinpixels_business.Entity.User import User


class GraphQLProcessor(DataProcessor):

    def __init__(self):
        self.resolvers = dict()

        self.query = ObjectType("Query")
        self.mutation = ObjectType("Mutation")
        self.mutation.set_field("register", register_user)
        self.query.set_field("user", resolve_user)

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

    def add_resolver(self, business_class, resolver):
        self.resolvers[business_class] = resolver


def resolve_strr(obj, info):
    return "IT WORKS"

def register_user(ob, info, email, password):
    return {
        "success": True
    }


def resolve_user(obj, info, guid):
    user = User()
    user.email = "dads"
    return user
