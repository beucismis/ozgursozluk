import unittest

from ozgursozluk.api import Eksi


eksi = Eksi()
topic = eksi.search_topic("linux")


class TestTopic(unittest.TestCase):
    def test_id(self):
        self.assertEqual(topic.id, "32084")

    def test_title(self):
        self.assertEqual(topic.title, "linux")

    def test_permalink(self):
        self.assertEqual(topic.permalink, "https://eksisozluk.com/linux--32084")


if __name__ == "__main__":
    unittest.main()
