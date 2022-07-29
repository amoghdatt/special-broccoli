import unittest
import sys
sys.path.append("..")
from src.tax.helpers.tax_helper import round_tax_amount

class TestTaxHelper(unittest.TestCase):

    def test_that_tax_amount_is_rounded_to_the_nearest_zero_point_zero_five(self):
        res = round_tax_amount(0.4877)

        self.assertEqual(res, 0.5)


    def test_that_tax_amount_is_rounded_to_the_nearest_zero_point_zero_five_2(self):
        res = round_tax_amount(1.6500000000000001)

        self.assertEqual(res, 1.65)