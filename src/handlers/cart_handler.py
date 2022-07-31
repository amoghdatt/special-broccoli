from src.services.cart_service import CartService
from src.cart import Cart
from src.item import Item

class CartHandler:

    def __init__(self):
        self.cart_service = CartService

    def prepare_cart(self,desired_items):

        cart = Cart()
        for item in desired_items:
            fetched_item = CartService.fetch_item(item)
            quantity = fetched_item['quantity']
            del fetched_item['quantity']
            item = Item(**fetched_item)
            cart.add_item(item, quantity)
        
        return cart