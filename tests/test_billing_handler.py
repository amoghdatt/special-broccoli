import sys
sys.path.append("..")
import unittest
import io
import unittest.mock
from src.cart import Cart
from src.item import Item
from src.handlers.billing_handler import BillingHandler

class TestBillingHandler(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tax_calculation_for_non_imported_exempted_and_non_exempted_items(self, mock_stdout):
        handler = BillingHandler()
        cart = Cart()
        cart.add_item(Item('book', False, 12.49, 'Book'), 1)
        cart.add_item(Item('music CD', False, 14.99, 'Music'), 1)
        cart.add_item(Item('chocolate bar', False, 0.85, 'Food'), 1)

        bill = handler.generate_bill(cart)
        bill.print()
        res = mock_stdout.getvalue()
        expected = '1 book: 12.49\n1 music CD: 16.49\n1 chocolate bar: 0.85\nSales Taxes: 1.50\nTotal: 29.83'

        self.assertEqual(res, expected)


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tax_calculation_for_imported_exempted_and_non_exempted_items(self, mock_stdout):
        handler = BillingHandler()
        cart = Cart()
        cart.add_item(Item('imported box of chocolates', True, 10.00, 'Food'), 1)
        cart.add_item(Item('imported bottle of perfume', True, 47.50, 'Cosmetics'), 1)

        bill = handler.generate_bill(cart)
        bill.print()
        res = mock_stdout.getvalue()
        expected = '1 imported box of chocolates: 10.50\n1 imported bottle of perfume: 54.65\nSales Taxes: 7.65\nTotal: 65.15'

        self.assertEqual(res, expected)


    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tax_calculation_for_imported_exempted_and_non_exempted_items_2(self, mock_stdout):
        handler = BillingHandler()
        cart = Cart()
        cart.add_item(Item('imported bottle of perfume', True, 27.99, 'Cosmetics'), 1)
        cart.add_item(Item('bottle of perfume', False, 18.99, 'Cosmetics'), 1)
        cart.add_item(Item('packet of headache pills', False, 9.75, 'Medicine'), 1)
        cart.add_item(Item('box of imported chocolates', True, 11.25, 'Food'), 1)

        bill = handler.generate_bill(cart)
        bill.print()
        res = mock_stdout.getvalue()
        expected = '1 imported bottle of perfume: 32.19\n1 bottle of perfume: 20.89\n1 packet of headache pills: 9.75\n1 box of imported chocolates: 11.85\nSales Taxes: 6.70\nTotal: 74.68'

        self.assertEqual(res, expected)




