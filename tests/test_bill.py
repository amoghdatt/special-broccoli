import unittest
import unittest.mock
import sys
import io
sys.path.append("..")
from src.bill import Bill

class TestBill(unittest.TestCase):


    class FakeItemClass:

        def __init__(self, name, price) -> None:
            self.name = name
            self.price = price

    class FakeCartItemClass(FakeItemClass):

        def __init__(self, item, quantity) -> None:
            self.item = item
            self.quantity = quantity

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_whether_bill_is_being_printed(self, mock_stdout):

        item1 = self.FakeItemClass('test item', 60)
        item2 = self.FakeItemClass('test item second', 70)

        bill_items = [
            [self.FakeCartItemClass(item1, 2), 60.50],
            [self.FakeCartItemClass(item2, 3), 70.95]
        ]

        bill =  Bill(bill_items, 5, 130)
        bill.print()

        res = mock_stdout.getvalue()
        self.assertEqual(res, '2 test item: 60.50\n3 test item second: 70.95\nSales Taxes: 5.00\nTotal: 130.00')

