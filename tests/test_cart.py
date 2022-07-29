import unittest
import sys
sys.path.append("..")
from src.cart import Cart
from src.cart_item import CartItem

class TestCart(unittest.TestCase):

    class fakeItemClass:

        def __init__(self, name) -> None:
            self.name = name

    def test_whether_item_was_successfully_added_to_cart(self):
        test_cart = Cart()
        test_item = self.fakeItemClass('SAMPLE_ITEM')

        test_cart.add_item(test_item, 1)

        self.assertEqual(len(test_cart.get_items()),1)

    def test_that_added_cart_item_was_of_cartItem_instance(self):
        test_cart = Cart()
        test_item = self.fakeItemClass('SAMPLE_ITEM')

        test_cart.add_item(test_item, 1)

        self.assertIsInstance(test_cart.get_items()[0], CartItem)