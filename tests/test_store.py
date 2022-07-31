import unittest
import unittest.mock
import io
import sys
sys.path.append("..")
from src.store import Store
from src.cart import Cart


class TestStore(unittest.TestCase):


    def test_that_cart_is_successfully_built_from_desired_items(self):
        desired_items = ['1 imported box of chocolates at 10.00']

        res = Store().build_cart(desired_items)

        self.assertIsInstance(res, Cart)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_that_invoice_is_successfully_printed(self, mock_stdout):
        sample_desired_item = ['1 imported box of chocolates at 10.00']

        cart = Store().build_cart(sample_desired_item)
        Store().invoice(cart)

        res = mock_stdout.getvalue()
        self.assertEqual(res, '1 imported box of chocolates: 10.50\nSales Taxes: 0.50\nTotal: 10.50')







