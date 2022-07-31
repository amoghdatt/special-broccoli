import sys
sys.path.append("..")
from src.life_grid import LifeGrid
import itertools
from src.cell import Cell

if __name__ == '__main__':
    print('Enter seed data....')
    seed_data = list(itertools.takewhile(lambda x: x.strip() != 'quit', sys.stdin))
    seed_data_dict = dict()

    for data in seed_data:
        x, y = data.split(',')
        seed_data_dict[data.strip()] = Cell(int(x), int(y))
        
    
    life_grid = LifeGrid(seed_data_dict)
    life_grid.tick()
    life_grid.print_survivors()