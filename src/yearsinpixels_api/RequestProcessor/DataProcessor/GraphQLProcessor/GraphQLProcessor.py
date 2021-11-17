from pathlib import Path

from ariadne import make_executable_schema, graphql_sync, ObjectType, load_schema_from_path
from flask import Flask, _app_ctx_stack
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session

from yearsinpixels_api.Request.Response import Response
from yearsinpixels_api.RequestProcessor.DataProcessor.DataProcessor import DataProcessor

engine = create_engine("mysql://root:somepass@127.0.0.1/yearsinpixels")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

app = Flask(__name__)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)

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
        users = app.session.query(User).all()

        users = users



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

def get_users(obj):
    pass


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String)