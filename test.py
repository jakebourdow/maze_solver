import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0,0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_break_entrance_and_exit_large(self):
        has_top_wall = False
        has_bottom_wall = False
        m1 = Maze(0, 0, 12, 16, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[15][11].has_bottom_wall,
            False
        )

    def test_break_entrance_and_exit_small(self):
        has_top_wall = False
        has_bottom_wall = False
        m1 = Maze(0, 0, 1, 1, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1._cells[0][0].has_bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()