import re
from src.item import Item
from src.handlers.invoice_handler import InvoiceHandler
from src.constants import CONST_IMPORTED
from src.enums import ItemNameToCategory


class Store:

    @classmethod
    def build_cart(cls, cart, desired_item):

        item, quantity = cls.fetch_desired_item(desired_item)
        cart.add_item(item, quantity)

    @classmethod
    def invoice(cls, cart):
        InvoiceHandler().generate_invoice(cart)

    @staticmethod
    def fetch_desired_item(desired_item):
        item_details = desired_item.split(' ')
        quantity = item_details[0].strip()
        price = item_details[-1].strip()
        is_imported = CONST_IMPORTED in item_details
        name = re.match(r"(.*)(?=at)", desired_item[1:]).group().strip()

        return Item(name, is_imported, float(price), ItemNameToCategory.ITEM.value[name]), int(quantity)
