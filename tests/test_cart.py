import unittest
from aims.cart import Cart


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()

        for _ in range(20):
            self.assertTrue(cart.add_dvd(None))

        self.assertFalse(cart.add_dvd(None))
        self.assertEqual(len(cart.items), 20)


if __name__ == "__main__":
    unittest.main()