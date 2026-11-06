import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchCaseInsensitive(unittest.TestCase):
    def test_lowercase_keyword_finds_title(self):
        dvd = DigitalVideoDisc("The Lion King")
        result = search_by_title([dvd], "lion")
        self.assertEqual(result, [dvd])


if __name__ == "__main__":
    unittest.main()
