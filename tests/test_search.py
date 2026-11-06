import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title


class TestSearch(unittest.TestCase):
    def setUp(self):
        self.lion_king = DigitalVideoDisc("The Lion King", "Animation")
        self.star_wars = DigitalVideoDisc("Star Wars", "Science Fiction")
        self.items = [self.lion_king, self.star_wars]

    def test_search_by_title_returns_matching_dvd(self):
        result = search_by_title(self.items, "Lion")
        self.assertEqual(result, [self.lion_king])

    def test_search_by_category_returns_matching_dvd(self):
        result = search_by_category(self.items, "Animation")
        self.assertEqual(result, [self.lion_king])

    def test_lowercase_keyword_finds_title(self):
        dvd = DigitalVideoDisc("The Lion King", "Animation")
        result = search_by_title([dvd], "lion")
        self.assertEqual(result, [dvd])
        
if __name__ == "__main__":
    unittest.main()
