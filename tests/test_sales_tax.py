import unittest
import sys
sys.path.append("..")
from src.tax.sales_tax import SalesTax

class TestSalesTax(unittest.TestCase):

    class FakeItemClass:

        def __init__(self, name, price, category, is_imported) -> None:
            self.name = name
            self.price = price 
            self.is_imported = is_imported
            self.category = category

    def test_sales_tax_calculation_when_category_is_food(self):
        item = self.FakeItemClass('test', 80, 'Food', True)
        computed_tax = SalesTax().compute(item)

        self.assertEqual(computed_tax, 0)

    def test_sales_tax_calculation_when_category_is_books(self):
        item = self.FakeItemClass('test book', 10, 'Book', True)
        computed_tax = SalesTax().compute(item)

        self.assertEqual(computed_tax, 0)


    def test_sales_tax_calculation_when_category_is_medicine(self):
        item = self.FakeItemClass('test medicine', 9.75, 'Medicine', True)
        computed_tax = SalesTax().compute(item)

        self.assertEqual(computed_tax, 0)

    def test_sales_tax_calculation_when_category_is_any(self):
        item = self.FakeItemClass('test music', 5, 'Music', True)
        computed_tax = SalesTax().compute(item)

        self.assertEqual(computed_tax, 0.5)



