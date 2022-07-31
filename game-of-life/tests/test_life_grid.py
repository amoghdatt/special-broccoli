import unittest
import sys
sys.path.append("..")
from src.cell import Cell
from src.life_grid import LifeGrid


class TestLifeGrid(unittest.TestCase):

    def test_next_generation_survivors_for_block_pattern(self):
        
        seed_data = {'1, 1':Cell(1, 1), '1, 2':Cell(1, 2), '2, 1':Cell(2, 1), '2, 2':Cell(2, 2)}

        expected = ['1, 1', '1, 2', '2, 1', '2, 2']
        life_grid = LifeGrid(seed_data)
        life_grid.tick()

        result = list(life_grid.get_survivors())


        self.assertEqual(expected, result)

    
    def test_next_generation_survivors_for_boat_pattern(self):
        
        seed_data = {'0, 1': Cell(0, 1), '1, 0': Cell(1, 0), '2, 1': Cell(2, 1), '0, 2':Cell(0, 2), '1, 2':Cell(1, 2)}
     
        expected = ['0, 1', '1, 0', '2, 1', '0, 2', '1, 2']

        life_grid = LifeGrid(seed_data)
        life_grid.tick()

        result = list(life_grid.get_survivors())

        self.assertEqual(expected, result)


    def test_next_generation_survivors_for_blinker_pattern(self):
        
        seed_data = {'1, 1': Cell(1, 1), '1, 0':Cell(1, 0), '1, 2':Cell(1, 2)}
     
        expected = ['1, 1', '0, 1', '2, 1']
        life_grid = LifeGrid(seed_data)
        life_grid.tick()

        LifeGrid(seed_data)

        result = list(life_grid.get_survivors())

        self.assertEqual(result, expected)

    
    def test_next_generation_survivors_for_toad_pattern(self):
        
        seed_data = {
            '1, 1': Cell(1, 1), 
        '1, 2': Cell(1, 2), 
        '1, 3': Cell(1, 3), 
        '2, 2': Cell(2, 2), 
        '2, 3': Cell(2, 3), 
        '2, 4': Cell(2, 4)}
     

        expected = ['0, 2', '1, 1', '1, 4', '2, 1', '2, 4', '3, 3']

        life_grid = LifeGrid(seed_data)
        life_grid.tick()

        result = list(life_grid.get_survivors())

        self.assertCountEqual(expected, result)