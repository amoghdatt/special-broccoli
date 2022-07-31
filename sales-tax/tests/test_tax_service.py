import unittest
import sys
sys.path.append("..")
from src.item import Item
from src.services.tax_service import TaxService

class TestTaxService(unittest.TestCase):

    def test_total_sales_tax_for_an_imported_non_exempted_item(self):
        item = Item('Dua Lipa', True, 11.00, 'Music')
        computed_tax = TaxService().compute_tax(item)

        self.assertEqual(computed_tax, 1.6500000000000001)

    def test_total_sales_tax_for_an_imported_exempted_item(self):
        item = Item('eye drops', True, 9.75 , 'Medicine')
        computed_tax = TaxService().compute_tax(item)

        self.assertEqual(computed_tax, 0.5)

    def test_total_sales_tax_for_a_non_imported_exempted_item(self):
        item = Item('Headache pill', False, 111.11 , 'Medicine')
        computed_tax = TaxService().compute_tax(item)

        self.assertEqual(computed_tax, 0)

    def test_total_sales_tax_for_a_non_imported_non_exempted_item(self):
        item = Item('Dua Lipa', False, 111.11 , 'Music')
        computed_tax = TaxService().compute_tax(item)

        self.assertEqual(computed_tax, 11.15)




