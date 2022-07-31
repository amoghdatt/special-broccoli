from src.constants import CONST_IMPORTED
from src.enums import ItemNameToCategory
import re


class CartService:

    @staticmethod
    def fetch_item(desired_item):
        item_details = desired_item.split(' ')
        quantity = item_details[0].strip()
        price = item_details[-1].strip()
        is_imported = CONST_IMPORTED in item_details
        name = re.match(r"(.*)(?=at)", desired_item[1:]).group().strip()

        return {
            'name':name,
            'is_imported':is_imported,
            'price':float(price),
            'category':ItemNameToCategory.ITEM.value[name],
            'quantity':int(quantity)
        }