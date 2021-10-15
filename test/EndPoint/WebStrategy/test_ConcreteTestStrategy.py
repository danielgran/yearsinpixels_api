import unittest

from src.EndPoint.SocketStrategy.ConcreteTestStrategy import ConcreteTestStrategy


class Utility:
    @staticmethod
    def create_test_strategy():
        strategy = ConcreteTestStrategy()
        return strategy

    @staticmethod
    def create_callback():
        callback_object = CallbackTest()

        return callback_object


class CallbackTest:
    success = False
    path = None
    header = None
    body = None

    def callback(self, path, header, body):
        self.success = True
        self.path = path
        self.header = header
        self.body = body


class TestStrategies(unittest.TestCase):

    def setUp(self):
        self.strategy = Utility.create_test_strategy()
        self.callback_test_object = Utility.create_callback()
        self.strategy.setup_service(self.callback_test_object.callback)

    def test_isThere(self):
        self.assertTrue(self.strategy)

    def test_callback(self):
        self.strategy.simulate_request("/doesalsonotmatter", "doesntmatter", "doesntmatter")
        self.assertTrue(self.callback_test_object.success)

    def test_service_status(self):
        self.strategy.run()
        self.assertTrue(self.strategy.is_running())

    def test_simulate_request(self):
        self.strategy.simulate_request("/examplepath", "headertest", "bodytest")

        # The callback class has these temporary strings which now are checked if changed successfully
        self.assertTrue(self.callback_test_object.path == "/examplepath")
        self.assertTrue(self.callback_test_object.header == "headertest")
        self.assertTrue(self.callback_test_object.body == "bodytest")
