import time
import random # Import random module
from .cell import Cell

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None, # Added default None for win
        seed=None, # Add seed parameter
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None: # Seed random if provided
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0) # Start breaking walls recursively
        self._reset_cells_visited() # Reset visited status for solving

    def _create_cells(self):
        for i in range(self._num_cols):
            col_cells = []
            for j in range(self._num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.025)

    def _break_entrance_and_exit(self):
        # Break top wall of the entrance cell
        entrance_cell = self._cells[0][0]
        entrance_cell.has_top_wall = False
        self._draw_cell(0, 0)

        # Break bottom wall of the exit cell
        exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
        exit_cell.has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        current_cell = self._cells[i][j]
        current_cell.visited = True
        while True:
            to_visit = []
            # Check neighbors
            # Left
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            # Right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            # Up
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            # Down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))

            if not to_visit:
                self._draw_cell(i, j)
                return

            # Pick a random direction
            next_i, next_j = random.choice(to_visit)
            next_cell = self._cells[next_i][next_j]

            # Knock down walls
            # Moving right
            if next_i == i + 1:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            # Moving left
            elif next_i == i - 1:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            # Moving down
            elif next_j == j + 1:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            # Moving up
            elif next_j == j - 1:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False

            # Recursively call for the next cell
            self._break_walls_r(next_i, next_j)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate()
        current_cell = self._cells[i][j]
        current_cell.visited = True

        # Check if we reached the end cell
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # Directions: (di, dj) -> (right, left, down, up)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for di, dj in directions:
            ni, nj = i + di, j + dj

            # Check bounds
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                next_cell = self._cells[ni][nj]
                
                # Check if not visited and no wall between cells
                can_move = False
                if di == 1 and not current_cell.has_right_wall and not next_cell.has_left_wall: # Moving right
                    can_move = True
                elif di == -1 and not current_cell.has_left_wall and not next_cell.has_right_wall: # Moving left
                    can_move = True
                elif dj == 1 and not current_cell.has_bottom_wall and not next_cell.has_top_wall: # Moving down
                    can_move = True
                elif dj == -1 and not current_cell.has_top_wall and not next_cell.has_bottom_wall: # Moving up
                    can_move = True

                if can_move and not next_cell.visited:
                    current_cell.draw_move(next_cell)
                    if self._solve_r(ni, nj):
                        return True
                    else:
                        # Undo the move visually
                        current_cell.draw_move(next_cell, undo=True)

        # If none of the directions lead to the solution
        return False
