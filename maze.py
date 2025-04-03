import time
from cell import Cell
import random

class Maze():
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None,
        ):
        if seed:
            random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()
        
        
    def _create_cells(self):
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                col.append(Cell(self._win))
            self._cells.append(col)

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[self._num_cols-1][self._num_rows-1].has_bottom_wall = False
        self._draw_cell(0, 0)
        self._draw_cell(self._num_cols-1, self._num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))

            if len(to_visit) == 0:
                self._draw_cell(i,j)
                return
            dir_index = random.randrange(len(to_visit))
            next_index = to_visit[dir_index]

            if next_index[0] == i+1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False 
            if next_index[0] == i-1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            if next_index[1] == j-1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
            if next_index[1] == j+1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
           
            self._break_walls_r(next_index[0],next_index[1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
                
    def solve(self):
        i, j = 0, 0
        output = self._solve_r(i, j)
        if output:
            return True
        return False
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self._num_cols-1][self._num_rows-1]:
            return True
        
        if (
            i +1 < self._num_cols and 
            self._cells[i+1][j].visited == False and 
            self._cells[i][j].has_right_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i+1][j])
            output = self._solve_r(i+1, j)
            if output:
                return True
            self._cells[i][j].draw_move(self._cells[i+1][j], undo = True)
        if (
            i - 1 >= 0 and
            self._cells[i-1][j].visited == False and
            self._cells[i][j].has_left_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i-1][j])
            output = self._solve_r(i-1, j)
            if output:
                return True
            self._cells[i][j].draw_move(self._cells[i-1][j], undo = True)
        
        if (
            j + 1 < self._num_rows and
            self._cells[i][j+1].visited == False and
            self._cells[i][j].has_bottom_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j+1])
            output = self._solve_r(i, j+1)
            if output:
                return True
            self._cells[i][j].draw_move(self._cells[i][j+1], undo = True)
            
        if (
            j - 1 >= 0 and
            self._cells[i][j-1].visited == False and
            self._cells[i][j].has_top_wall == False
        ):
            self._cells[i][j].draw_move(self._cells[i][j-1])
            output = self._solve_r(i, j-1)
            if output:
                return True
            
            self._cells[i][j].draw_move(self._cells[i][j-1], undo = True)

        return False
