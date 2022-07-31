import re
from src.item import Item
from src.handlers.invoice_handler import InvoiceHandler
from src.handlers.cart_handler import CartHandler


class Store:

    @classmethod
    def build_cart(cls, desired_items):
        return CartHandler().prepare_cart(desired_items)

    @classmethod
    def invoice(cls, cart):
        InvoiceHandler().generate_invoice(cart)
