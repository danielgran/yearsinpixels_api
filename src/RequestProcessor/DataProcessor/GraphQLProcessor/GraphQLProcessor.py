import json
import os
from pathlib import Path

from ariadne.constants import PLAYGROUND_HTML
from ariadne import QueryType, gql, make_executable_schema, graphql_sync, ObjectType, load_schema_from_path, snake_case_fallback_resolvers
from ariadne.asgi import GraphQL

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
            debug=True
        )

        rs = str(result)

        response.body = rs;

        return response

def register_user(obj, info, email):
    return {
        "success": True
    }