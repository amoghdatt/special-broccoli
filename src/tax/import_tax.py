from src.tax.tax import Tax
from src.enums import TaxRate
from src.constants import CONST_DEFAULT
from src.tax.helpers.tax_helper import round_tax_amount


class ImportTax(Tax):

    DEFAULT_TAX_RATE = TaxRate.IMPORT_TAX.value[CONST_DEFAULT]

    def compute(self, item):
        if item.is_imported:
            price = item.price
            category = item.category
            tax =  price * TaxRate.IMPORT_TAX.value.get(category,
                                    self.DEFAULT_TAX_RATE)

            return round_tax_amount(tax) 

        return 0
