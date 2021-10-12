import unittest

from src.Request.HTMLHeader import HTMLHeader


class test_HTMLHeader(unittest.TestCase):

    def test_is_there(self):
        self.assertIsNotNone(HTMLHeader)

    def test_add_item(self):
        header = HTMLHeader()
        header.add_item(("some", "thing"))
        self.assertRaises(Exception, header.add_item, ("some", "as"))
        self.assertEqual(header.get_content("some"), "thing")

    def test_remove_item(self):
        header = HTMLHeader()
        header.add_item(("some", "thing"))
        header.remove_item("some")
        self.assertRaises(Exception, header.remove_item, "not_there")

    def test_get_content(self):
        header = HTMLHeader()
        header.add_item(("some", "header"))
        self.assertEqual(header.get_content("some"), "header")

    def test_new_from_dict(self):
        header_mock = {'Host': 'localhost:8080', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Upgrade-Insecure-Requests': '1', 'Cookie': 'Webstorm-ef1f44d4=7fd8ddd3-93b4-4beb-bdea-b421d50c90ed', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15', 'Accept-Language': 'en-gb', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'keep-alive'}
        header = HTMLHeader(header_mock)
        self.assertEqual(header_mock, header.items)