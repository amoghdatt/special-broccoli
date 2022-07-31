from enum import Enum
from src.tax.import_tax import ImportTax
from src.tax.sales_tax import SalesTax


class ApplicableTaxes(Enum):

    IMPORT_TAX = ImportTax()
    SALES_TAX = SalesTax()
