import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearch(unittest.TestCase):
    def test_search_by_title_returns_matching_dvd(self):
        lion_king = DigitalVideoDisc("The Lion King")
        star_wars = DigitalVideoDisc("Star Wars")

        result = search_by_title([lion_king, star_wars], "Lion")

        self.assertEqual(result, [lion_king])


if __name__ == "__main__":
    unittest.main()
