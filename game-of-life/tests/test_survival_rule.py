import unittest
import sys
sys.path.append("..")
from src.rules.survival_rule import SurvivalRule
from src.cell import Cell

class TestSurvivalRule(unittest.TestCase):

    def test_next_generation_survivors_for_block_pattern(self):
        
        current_survivors = {'1, 1': Cell(1, 1), '1, 2': Cell(1, 2), '2, 1':Cell(2, 1), '2, 2':Cell(2, 2)}
        potential_survivors = dict()

        SurvivalRule().apply(potential_survivors, current_survivors)

        self.assertEqual(len(potential_survivors.keys()), 4)

    
    def test_next_generation_survivors_for_boat_pattern(self):
        
        current_survivors = {'0, 1': Cell(0, 1), '1, 0': Cell(1, 0), '2, 1': Cell(2, 1), '0, 2':Cell(0, 2), '1, 2':Cell(1, 2)}
        potential_survivors = dict()

        SurvivalRule().apply(potential_survivors, current_survivors)

        self.assertEqual(len(potential_survivors.keys()), 5)


    def test_next_generation_survivors_for_blinker_pattern(self):
        
        current_survivors = {'1, 1': Cell(1, 1), '1, 0':Cell(1, 0), '1, 2':Cell(1, 2)}
        potential_survivors = dict()

        expected = ['1, 1']

        SurvivalRule().apply(potential_survivors, current_survivors)

        result = [survivor for survivor in potential_survivors.keys()]

        self.assertEqual(result, expected)

    
    def test_next_generation_survivors_for_toad_pattern(self):
        
        current_survivors = {
            '1, 1': Cell(1, 1), 
        '1, 2': Cell(1, 2), 
        '1, 3': Cell(1, 3), 
        '2, 2': Cell(2, 2), 
        '2, 3': Cell(2, 3), 
        '2, 4': Cell(2, 4)}
        potential_survivors = dict()

        expected = ['1, 1','2, 4']

        SurvivalRule().apply(potential_survivors, current_survivors)

        result = [survivor for survivor in potential_survivors.keys()]

        self.assertEqual(expected, result)


