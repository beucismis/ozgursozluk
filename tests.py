import unittest

from ozgursozluk.scraper import EksiSozluk


es = EksiSozluk()
topic = es.get_topic("linux--32084")
entry = es.get_entry(1)


class TestTopic(unittest.TestCase):
    def test_topic_id(self):
        self.assertEqual(topic.id, 32084)

    def test_topic_title(self):
        self.assertEqual(topic.title, "linux")

    def test_topic_path(self):
        self.assertEqual(topic.path, "linux--32084")


class TestEntry(unittest.TestCase):
    def test_topic_id(self):
        self.assertEqual(entry.topic_id, 31782)

    def test_topic_title(self):
        self.assertEqual(entry.topic_title, "pena")

    def test_topic_path(self):
        self.assertEqual(entry.topic_path, "pena--31782")

    def test_entry_author(self):
        self.assertEqual(entry.author, "ssg")

    def test_entry_datetime(self):
        self.assertEqual(entry.datetime, "15.02.1999")


if __name__ == "__main__":
    unittest.main()
