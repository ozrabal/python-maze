import unittest
from src.maze import Maze

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
        num_cols = 50
        num_rows = 40
        m1 = Maze(0, 0, num_rows, num_cols, 5, 5)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_single(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_reset_cells_visited(self):
        num_cols = 5
        num_rows = 5
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        # Check initial state after __init__ calls _reset_cells_visited
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)
        
        # Manually set some cells to visited
        m1._cells[0][0].visited = True
        m1._cells[2][3].visited = True
        m1._cells[4][4].visited = True

        # Call the method to reset
        m1._reset_cells_visited()

        # Check if all cells are reset to not visited
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
