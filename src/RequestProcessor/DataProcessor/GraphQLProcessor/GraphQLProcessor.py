from pathlib import Path

from ariadne import make_executable_schema, graphql_sync, ObjectType, load_schema_from_path

from src.Request.Response import Response
from src.RequestProcessor.DataProcessor.DataProcessor import DataProcessor


class GraphQLProcessor(DataProcessor):

    def __init__(self):
        self.query = ObjectType("Query")
        self.mutation = ObjectType("Mutation")
        self.mutation.set_field("register", register_user)

        path = Path(__file__)
        path = path.parent.resolve()
        path = f"{path}/schema.graphql"

        self.schema = make_executable_schema(
            load_schema_from_path(path)
        )

    def process(self, request):
        response = Response(request)

        success, result = graphql_sync(
            data=request.body,
            schema=self.schema,
            debug=__debug__
        )

        return_string = str(result)
        response.body = return_string

        return response

# Thats BL
def register_user(obj, info, email):
    return {
        "success": True
    }
