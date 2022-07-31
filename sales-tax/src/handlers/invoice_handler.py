from src.services.tax_service import TaxService
from src.invoice import Invoice


class InvoiceHandler:

    def __init__(self):
        self.compute_tax = TaxService().compute_tax

    def get_invoice_details(self, cart, invoice):

        if not cart:
            return invoice

        cart_item = cart.pop()
        item = cart_item.item
        quantity = cart_item.quantity 

        tax_for_current_item = self.compute_tax(
                item) * quantity

        total_value_of_item_with_tax = tax_for_current_item + item.price

        invoice.add_item_details([cart_item, total_value_of_item_with_tax])
        invoice.add_to_sales_tax(tax_for_current_item)
        invoice.add_to_total(total_value_of_item_with_tax)

        return self.get_invoice_details(cart, invoice)


        
    
    def generate_invoice(self, cart):
        items_in_cart = cart.get_items()
        items_in_cart.reverse()
        invoice = Invoice(item_details=[])

        self.get_invoice_details(items_in_cart, invoice)
        invoice.print()
