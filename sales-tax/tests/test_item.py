import unittest
import sys
sys.path.append("..")
from src.item import Item

class TestItem(unittest.TestCase):
    
    item = Item('test_name', False, 11.00, 'Music')

    def test_that_created_item_has_expected_name(self):
        self.assertEqual(self.item.name, 'test_name')