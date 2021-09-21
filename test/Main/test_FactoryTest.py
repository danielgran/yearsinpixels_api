import unittest

from Main.ConcreteFactory import ConcreteFactory

class FactoryUtility:

    @staticmethod
    def create_factory():
        return ConcreteFactory()


class FactoryTest(unittest.TestCase):

    def test_isthere(self):
        self.assertTrue(ConcreteFactory)

    def test_create_factory(self):
        factory = FactoryUtility.create_factory()
        self.assertTrue(factory)

