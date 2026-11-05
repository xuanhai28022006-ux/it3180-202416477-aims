import unittest
from types import SimpleNamespace

from aims.cart import Cart


class TestDiscount(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        self.cart.items = [SimpleNamespace(cost=100)]

    def test_twenty_percent_discount(self):
        self.assertEqual(self.cart.total_cost_with_discount(20), 80)

    def test_reject_discount_over_100_percent(self):
        with self.assertRaises(ValueError):
            self.cart.total_cost_with_discount(150)