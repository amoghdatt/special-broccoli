import unittest
import sys
sys.path.append("..")
from src.cell import Cell

class TestCell(unittest.TestCase):

    def test_whether_cell_returns_all_its_neighbors_coordinates(self):
        
        cell = Cell(1, 1)
        expected = [
            '[0,0]',
            '[0,1]',
            '[0,2]',
            '[1,0]',
            '[1,1]',
            '[1,2]',
            '[2,0]',
            '[2,1]',
            '[2,2]'

        ]

        result = []

        for neighbor in cell.get_neighbors():
            result.append(f'[{neighbor.row},{neighbor.column}]')

        self.assertEqual(expected, result)

    
    def test_whether_cell_returns_all_its_neighbors_coordinates_2(self):
        
        cell = Cell(0, 1)
        expected = [
            '[-1,0]',
            '[-1,1]',
            '[-1,2]',
            '[0,0]',
            '[0,1]',
            '[0,2]',
            '[1,0]',
            '[1,1]',
            '[1,2]'

        ]

        result = []

        for neighbor in cell.get_neighbors():
            result.append(f'[{neighbor.row},{neighbor.column}]')

        self.assertEqual(expected, result)

    
    def test_whether_cell_returns_all_its_neighbors_coordinates_3(self):
        
        cell = Cell(0, 0)

        expected = [
            '[-1,-1]',
            '[-1,0]',
            '[-1,1]',
            '[0,-1]',
            '[0,0]',
            '[0,1]',
            '[1,-1]',
            '[1,0]',
            '[1,1]'

        ]

        result = []

        for neighbor in cell.get_neighbors():
            result.append(f'[{neighbor.row},{neighbor.column}]')

        self.assertEqual(expected, result)



