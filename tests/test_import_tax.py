import unittest
import sys
sys.path.append("..")
from src.tax.import_tax import ImportTax

class TestImportTax(unittest.TestCase):

    class FakeItemClass:

        def __init__(self, name, price, category, is_imported) -> None:
            self.name = name
            self.price = price 
            self.is_imported = is_imported
            self.category = category

    def test_import_tax_calculation_for_imported_item_when_category_is_food(self):
        item = self.FakeItemClass('test', 80, 'Food', True)
        computed_tax = ImportTax().compute(item)

        self.assertEqual(computed_tax, 4)

    def test_import_tax_calculation_for_imported_item_when_category_is_books(self):
        item = self.FakeItemClass('test book', 10, 'Book', True)
        computed_tax = ImportTax().compute(item)

        self.assertEqual(computed_tax, 0.5)


    def test_import_tax_calculation_for_imported_item_when_category_is_medicine(self):
        item = self.FakeItemClass('test medicine', 9.75, 'Medicine', True)
        computed_tax = ImportTax().compute(item)

        self.assertEqual(computed_tax, 0.5)

    def test_import_tax_calculation_for_imported_item_when_category_is_any(self):
        item = self.FakeItemClass('test music', 5, 'Music', True)
        computed_tax = ImportTax().compute(item)

        self.assertEqual(computed_tax, 0.25)

    def test_import_tax_calculation_for_non_imported_item_when_category_is_any(self):
        item = self.FakeItemClass('test music', 5, 'Music', False)
        computed_tax = ImportTax().compute(item)

        self.assertEqual(computed_tax, 0)



