import unittest

from ozgursozluk.api import Eksi


eksi = Eksi()
result_1 = eksi.search_topic("linux")
result_2 = eksi.get_entry("6934605")


class TestTopic(unittest.TestCase):
    def test_id(self):
        self.assertEqual(result_1.id, "32084")

    def test_title(self):
        self.assertEqual(result_1.title, "linux")

    def test_permalink(self):
        self.assertEqual(result_1.permalink, "https://eksisozluk.com/linux--32084")


class TestEntry(unittest.TestCase):
    def test_title(self):
        self.assertEqual(result_2.title, "debian")

    def test_content(self):
        for entry in result_2.entrys:
            self.assertEqual(entry.content, "en iyi dağıtımdır.")

    def test_author(self):
        for entry in result_2.entrys:
            self.assertEqual(entry.author, "carmack")

    def test_datetime(self):
        for entry in result_2.entrys:
            self.assertEqual(entry.datetime, "22.02.2005 04:18")

    def test_permalink(self):
        for entry in result_2.entrys:
            self.assertEqual(entry.permalink, "https://eksisozluk.com/entry/6934605")


if __name__ == "__main__":
    unittest.main()
