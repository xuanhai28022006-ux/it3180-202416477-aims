import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class CartSortingTests(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.aladdin = DigitalVideoDisc("Aladdin", cost=18.99)
        self.lion_king = DigitalVideoDisc("The Lion King", cost=19.95)
        self.star_wars = DigitalVideoDisc("Star Wars", cost=24.95)

        self.cart.items = [
            self.star_wars,
            self.lion_king,
            self.aladdin,
        ]

    def test_sort_by_title(self):
        result = self.cart.sort_by_title()
        self.assertEqual(
            [dvd.title for dvd in result],
            ["Aladdin", "Star Wars", "The Lion King"],
        )

    def test_sort_by_cost(self):
        result = self.cart.sort_by_cost()
        self.assertEqual(
            [dvd.cost for dvd in result],
            [18.99, 19.95, 24.95],
        )


if __name__ == "__main__":
    unittest.main()
