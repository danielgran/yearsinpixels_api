from yearsinpixels_business.Entity.Day import Day
from yearsinpixels_business.Entity.Mood import Mood
from yearsinpixels_business.Entity.User import User

from yearsinpixels_data.Gateway.MySQLGateway import MySQLGateway

from yearsinpixels_api.EndPoint.EndPoint import EndPoint
from yearsinpixels_api.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy
from yearsinpixels_api.Main.ConcreteFactory import ConcreteFactory
from yearsinpixels_api.RequestProcessor.DataProcessor.GraphQLProcessor.GraphQLProcessor import GraphQLProcessor
from yearsinpixels_api.RequestQueue.RequestQueue import RequestQueue
from yearsinpixels_data.Mapper.DayMapper import DayMapper
from yearsinpixels_data.Mapper.MoodMapper import MoodMapper
from yearsinpixels_data.Mapper.UserMapper import UserMapper


def main():
    factory = ConcreteFactory()
    webhost = factory.CreateWebHost("localhost")
    setup_webhost(webhost)
    webhost.run()

def setup_webhost(webhost):
    expose_strategy = FlaskWebStrategy()
    data_request_queue = RequestQueue()

    graqh_ql_processor = GraphQLProcessor()

    mysql_gateway = MySQLGateway(username='root', password='somepass', database='yearsinpixels')
    mysql_gateway.connect()
    user_mapper = UserMapper(mysql_gateway)
    graqh_ql_processor.set_mapper(User, user_mapper)
    mood_mapper = MoodMapper(mysql_gateway)
    graqh_ql_processor.set_mapper(Mood, mood_mapper)
    day_mapper = DayMapper(mysql_gateway)
    graqh_ql_processor.set_mapper(Day, day_mapper)

    data_request_queue.reqister_processor("/api", graqh_ql_processor)

    webhost.setup_expose_strategy(expose_strategy)

    test_endpoint = EndPoint("/api")
    test_endpoint.set_request_queue(request_queue=data_request_queue)

    webhost.add_endpoint(test_endpoint)

if __name__ == '__main__':
    main()
