import unittest

from src.Main.ConcreteFactory import ConcreteFactory


class FactoryTest(unittest.TestCase):


    def test_isthere(self):
        self.assertIsNotNone(ConcreteFactory)

    def test_create_factory(self):
        self.assertIsNotNone(ConcreteFactory.CreateWebHost("localhost"))
