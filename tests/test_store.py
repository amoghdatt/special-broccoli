import unittest
import unittest.mock
import io
import sys
sys.path.append("..")
from src.store import Store
from src.cart import Cart


class TestStore(unittest.TestCase):

    def test_that_quantity_is_parsed_from_given_string(self):
        sample_desired_item = '1 imported box of chocolates at 10.00'
        item, quantity = Store().fetch_desired_item(sample_desired_item)

        self.assertEqual(quantity, 1)

    def test_that_item_name_is_parsed_from_given_string(self):
        sample_desired_item = '1 imported box of chocolates at 10.00'
        item, quantity = Store().fetch_desired_item(sample_desired_item)

        self.assertEqual(item.name, 'imported box of chocolates')

    def test_that_item_price_is_parsed_from_given_string(self):
        sample_desired_item = '1 imported box of chocolates at 10.00'
        item, quantity = Store().fetch_desired_item(sample_desired_item)

        self.assertEqual(item.price, 10.00)

    def test_whether_item_is_an_imported_item_from_given_string(self):
        sample_desired_item = '1 imported box of chocolates at 10.00'
        item, quantity = Store().fetch_desired_item(sample_desired_item)

        self.assertEqual(item.is_imported, True)

    def test_whether_item_category_is_determined_from_given_string(self):
        sample_desired_item = '1 imported box of chocolates at 10.00'
        item, quantity = Store().fetch_desired_item(sample_desired_item)

        self.assertEqual(item.category, 'Food')

    def test_that_desired_item_is_successfully_added_to_cart(self):
        cart = Cart()
        sample_desired_item = '1 imported box of chocolates at 10.00'

        Store().build_cart(cart, sample_desired_item)
        cart_items = cart.get_items()

        no_of_items = len(cart_items)
        quantity = cart_items[0].quantity
        name = cart_items[0].item.name
        price = cart_items[0].item.price
        is_imported = cart_items[0].item.is_imported
        category = cart_items[0].item.category

        self.assertListEqual([no_of_items, quantity, name, price, is_imported, category], [1,1,'imported box of chocolates',10.00, True, 'Food'])

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_that_invoice_is_successfully_printed(self, mock_stdout):
        cart = Cart()
        sample_desired_item = '1 imported box of chocolates at 10.00'

        Store.build_cart(cart, sample_desired_item)
        Store.invoice(cart)

        res = mock_stdout.getvalue()
        self.assertEqual(res, '1 imported box of chocolates: 10.50\nSales Taxes: 0.50\nTotal: 10.50')







