from src.cart_item import CartItem


class Cart:

    def __init__(self) -> None:
        self.cart_items = []

    def add_item(self, item, quantity):

        new_cart_item = CartItem(item, quantity)
        self.cart_items.append(new_cart_item)

    def get_items(self):
        return self.cart_items
