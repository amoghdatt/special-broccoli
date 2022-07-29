from src.enums.tax import ApplicableTaxes


class TaxService:

    def compute_tax(self,item):
        total_sales_tax = 0.0

        for tax in ApplicableTaxes:
            total_sales_tax += tax.value.compute(item)

        return total_sales_tax
