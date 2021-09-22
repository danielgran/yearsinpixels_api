import os

import unittest

from src.Request.Request import Request


class RequestUtility:
    @staticmethod
    def create_request():
        return Request("/examplepath")


class RequestTest(unittest.TestCase):

    def test_creation(self):
        request = RequestUtility.create_request()
        self.assertTrue(request)

    def test_set_header(self):
        request = RequestUtility.create_request()
        request.header = {'server': "cloudflare"}
        self.assertTrue(request.header['server'])
        self.assertFalse(request.header.get('shouldNotExist'), "Request has flag that should not exist")

    def test_set_body(self):
        request = RequestUtility.create_request()
        request.body = "checkBody"
        self.assertTrue(request.body)

    def test_requestpath(self):
        request = RequestUtility.create_request()
        self.assertTrue(request.path)
