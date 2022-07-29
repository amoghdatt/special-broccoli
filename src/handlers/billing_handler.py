from src.services.tax_service import TaxService
from src.bill import Bill


class BillingHandler:

    def __init__(self):
        self.tax_service = TaxService()

    def get_billing_details(self, cart_items):
        total_sales_tax = 0
        bill_details = []
        total_cart_value = 0
        for cart_item in cart_items:
            item = cart_item.item
            quantity = cart_item.quantity

            tax_for_current_item = self.tax_service.compute_tax(
                item) * quantity

            total_value_of_item_with_tax = tax_for_current_item + item.price

            bill_details.append([cart_item, total_value_of_item_with_tax])

            total_sales_tax += tax_for_current_item
            total_cart_value += total_value_of_item_with_tax

        return total_sales_tax, total_cart_value, bill_details

    def generate_bill(self, cart):
        items_in_cart = cart.get_items()

        total_sales_tax, total_cart_value, bill_details = self.get_billing_details(items_in_cart)
        return Bill(bill_details, total_sales_tax, total_cart_value)
