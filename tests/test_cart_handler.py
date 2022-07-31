import unittest
import sys
sys.path.append("..")
from src.handlers.cart_handler import CartHandler
from src.item import Item

class TestCartHandler(unittest.TestCase):

    def test_that_cart_is_returned_when_desired_items_are_given(self):

        desired_items = [
            '1 imported box of chocolates at 10.00',
            '1 imported bottle of perfume at 47.50'
        ]

        

        result = CartHandler().prepare_cart(desired_items).get_items()

        for i in range(len(result)):
            self.assertEqual(result[i].quantity, 1)
            self.assertIsInstance(result[i].item, Item)

