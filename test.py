import unittest
from maze import Maze

class Tests(unittest.TestCase):

    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
                len(m1._cells),
                num_rows,
        )
        self.assertEqual(len(m1._cells[0]),
                         num_cols,
        )
    
    def test_maze_diff(self):
        num_cols = 25
        num_rows = 2
        m2 = Maze(10, 20, num_rows, num_cols, 12, 15)
        self.assertEqual(
                len(m2._cells),
                num_rows,
        )
        self.assertEqual(
                len(m2._cells[1]),
                num_cols,
        )
        self.assertEqual(
                m2._x1,
                10,
        )
        self.assertEqual(
                m2._cell_size_x,
                12,
        )
    
    def test_maze_entrance_exit(self):
        num_cols = 25
        num_rows = 25
        m3 = Maze(10, 20, num_rows, num_cols, 10, 10)
        self.assertEqual(
                m3._cells[0][0].has_top_wall,
                False,
        )
        self.assertEqual(
                m3._cells[num_cols-1][num_rows-1].has_bottom_wall,
                False,
        )
    def test_maze_reset(self):
        num_rows, num_cols = 10, 10
        m4 = Maze(10, 20, num_rows, num_cols, 10, 10)
        self.assertEqual(
                m4._cells[5][5].visited,
                False,
        )
        self.assertEqual(
                m4._cells[8][2].visited,
                False,
        )
                
        

if __name__ == "__main__":
    unittest.main()
