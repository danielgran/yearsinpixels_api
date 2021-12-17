import unittest

from yearsinpixels_api.EndPoint.SocketStrategy.FlaskWebStrategy import FlaskWebStrategy


class TestFlaskStrategy(unittest.TestCase):
    def setUp(self):
        self.strategy = FlaskWebStrategy()

    def test_isThere(self):
        self.assertIsNotNone(FlaskWebStrategy)

    def test_setup_service(self):
        self.strategy.setup_service(None)
        self.assertTrue(self.strategy.is_running)

    def test_open_service(self):
        self.strategy.setup_service(None)
        self.assertIsNotNone(self.strategy.run)

    def test_cors_policy_endpoint(self):
        self.strategy.setup_service(None)
        return_from_options = self.strategy.catch_options(None)
        self.assertEqual(return_from_options, ('', 200, {'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Headers': '*'}))
