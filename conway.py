from random import random
from typing import List


class Conway():
    def __init__(self, width: int = 10, height: int = 10):
        self.ROWS: int = width  # number of rows in the grid
        self.COLUMNS: int = height  # number of columns in the grid

        self.ALIVE: bool = True  # state of an alive cell
        self.DEAD: bool = False  # state of a dead cell

        self.ALIVE_CELL: str = 'X'  # representation of an alive cell
        self.DEAD_CELL: str = '.'  # representation of a dead cell

        self.has_alive_cell: bool = False  # whether the grid has a cell alive or not
        self.has_changed: bool = True  # whether the grid has evoluate or not

        self.grid: List[List[bool]] = [[self.DEAD for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
        self.next_grid: List[List[bool]] = [[self.DEAD for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]

        self.initGrid()

    def __str__(self) -> str:
        res = ""
        for row in self.grid:
            for cell in row:
                if cell:
                    res += f"{self.ALIVE_CELL:>3}"
                else:
                    res += f"{self.DEAD_CELL:>3}"
            res += "\n"
        return res

    def initGrid(self) -> None:
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if random() < 0.2:
                    self.has_alive_cell = True
                    self.grid[i][j] = self.ALIVE

    def countCellNeighbours(self, cell_row: int, cell_col: int) -> int:
        count = 0

        # check up
        if cell_col != 0:
            count = count+1 if self.grid[cell_row-1][cell_col] != self.DEAD else count
            # check upleft
            if cell_col != 0:
                count = count+1 if self.grid[cell_row-1][cell_col-1] != self.DEAD else count
            #check upright
            if cell_col != self.ROWS-1:
                count = count+1 if self.grid[cell_row-1][cell_col+1] != self.DEAD else count

        # check down
        if cell_row != self.ROWS-1:
            count = count+1 if self.grid[cell_row+1][cell_col] != self.DEAD else count
            # check downleft
            if cell_col != 0:
                count = count+1 if self.grid[cell_row+1][cell_col-1] != self.DEAD else count
            # check downright
            if cell_col != self.COLUMNS-1:
                count = count+1 if self.grid[cell_row+1][cell_col+1] != self.DEAD else count

        # check left
        if cell_col != 0:
            count = count+1 if self.grid[cell_row][cell_col-1] != self.DEAD else count
        # check right
        if cell_col != self.COLUMNS-1:
            count = count+1 if self.grid[cell_row][cell_col+1] != self.DEAD else count

        return count

    def run(self) -> None:
        alive_neighbours: int

        self.has_alive_cell = False

        for row in range(0, self.ROWS):
            for col in range(0, self.COLUMNS):
                alive_neighbours = self.countCellNeighbours(row, col)

                if self.grid[row][col] != self.DEAD:
                    self.has_alive_cell = True

                    if alive_neighbours < 2 or alive_neighbours > 3:
                        self.next_grid[row][col] = self.DEAD
                    else:
                        self.next_grid[row][col] = self.ALIVE
                else:
                    if alive_neighbours != 3:
                        self.next_grid[row][col] = self.DEAD
                    else:
                        self.next_grid[row][col] = self.ALIVE

        self.has_changed = self.hasChanged()
        if self.has_changed:
            for row in range(0, self.ROWS):
                for col in range(0, self.COLUMNS):
                    self.grid[row][col] = self.next_grid[row][col]

    def hasChanged(self) -> bool:
        for row in range(0, self.ROWS):
            for col in range(0, self.COLUMNS):
                if self.grid[row][col] != self.next_grid[row][col]:
                    return True
        return False