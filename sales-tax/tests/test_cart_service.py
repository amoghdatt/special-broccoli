import unittest
import sys
sys.path.append("..")
from src.services.cart_service import CartService

class TestCartService(unittest.TestCase):

    def test_whether_desired_item_is_fetched(self):
        desired_item = '1 imported bottle of perfume at 47.50'

        expected = {
            'name':'bottle of perfume',
            'is_imported':'imported',
            'price':47.50,
            'category':'Cosmetics',
            'quantity':1

        }

        result = CartService.fetch_item(desired_item)

        self.assertDictEqual(result, expected)

    def test_whether_desired_item_is_fetched_2(self):
        desired_item = '1 bottle of imported perfume at 47.50'

        expected = {
            'name':'bottle of perfume',
            'is_imported':'imported',
            'price':47.50,
            'category':'Cosmetics',
            'quantity':1

        }

        result = CartService.fetch_item(desired_item)

        self.assertDictEqual(result, expected)
