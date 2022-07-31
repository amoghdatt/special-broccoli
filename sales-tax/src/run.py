import sys
sys.path.append("..")
from src.store import Store
import itertools

if __name__ == '__main__':
    print('Enter cart items....')
    desired_cart_items = list(itertools.takewhile(lambda x: x.strip() != 'quit', sys.stdin))


    cart = Store().build_cart(desired_cart_items)
    Store.invoice(cart)