class Cell:

    def __init__(self, row, column):
        self.row = row
        self.column = column


    def get_neighbors(self):
         for i in range(self.row-1, self.row+2):
            for j in range(self.column-1, self.column+2):
                yield Cell(i,j)