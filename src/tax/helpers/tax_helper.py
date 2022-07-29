from src.constants import CONST_PRECISION
from src.constants import CONST_CEIL
import math

def round_tax_amount(tax_amount):
    cieled_amount =  math.ceil(tax_amount*CONST_CEIL)/CONST_CEIL
    return round(cieled_amount, CONST_PRECISION)