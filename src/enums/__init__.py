from enum import Enum
from src.constants import CONST_DEFAULT


class Category(Enum):
    FOOD = 'Food'
    BOOK = 'Book'
    MEDICINE = 'Medicine'
    MUSIC_CD = 'Music'
    COSMETICS = 'Cosmetics'


class TaxRate(Enum):

    SALES_TAX = {
        Category.FOOD.value: 0,
        Category.MEDICINE.value: 0,
        Category.BOOK.value: 0,
        CONST_DEFAULT: 0.1
    }

    IMPORT_TAX = {CONST_DEFAULT: 0.05}


class ItemNameToCategory(Enum):
    ITEM = {
        'book': Category.BOOK.value,
        'music CD': Category.MUSIC_CD.value,
        'chocolate bar': Category.FOOD.value,
        'box of chocolates': Category.FOOD.value,
        'bottle of perfume':Category.COSMETICS.value,
        'packet of headache pills': Category.MEDICINE.value
    }
