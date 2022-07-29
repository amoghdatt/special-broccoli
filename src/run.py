import sys
sys.path.append("..")
from src.store import Store
from src.cart import Cart
import itertools

if __name__ == '__main__':
    cart = Cart()
    print('Enter cart items....')
    cart_items = list(itertools.takewhile(lambda x: x.strip() != 'quit', sys.stdin))

    for desired_cart_item in cart_items:
        Store.build_cart(cart, desired_cart_item)

    Store.bill(cart)