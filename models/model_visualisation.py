#!/usr/bin/python3
import pygame
import math
from queue import PriorityQueue

# Set up the game window
WIDTH = 800
WIN = pygame.display.set_mode(size=(WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# Define some colors to be used during visualisation
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)


class Spot:
    """
    A class to represent a grid spot.

    Attributes:
        row (int): The row position of the spot in the grid.
        col (int): The column position of the spot in the grid.
        x (int): The x-coordinate of the spot on the screen.
        y (int): The y-coordinate of the spot on the screen.
        color (tuple): The RGB color of the spot.
        neighbors (list): A list of the spot's neighboring spots.
        width (int): The width of the spot.
        total_rows (int): The total number of rows in the grid.
    """

    def __init__(self, row, col, width, total_rows):
        """
        Initializes a new grid spot.

        Args:
            row (int): The row position of the spot in the grid.
            col (int): The column position of the spot in the grid.
            width (int): The width of the spot.
            total_rows (int): The total number of rows in the grid.
        """
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        """
        Gets the position of the spot in the grid.

        Returns:
            tuple: A tuple containing the row and column position of the spot.
        """
        return self.row, self.col

    def is_closed(self):
        """
        Returns whether the spot has been visited.

        Returns:
            bool: True if the spot has been visited, False otherwise.
        """
        return self.color == RED

    def is_open(self):
        """
        Returns whether the spot is open.

        Returns:
            bool: True if the spot is open, False otherwise.
        """
        return self.color == GREEN

    def is_barrier(self):
        """
        Returns whether the spot is a barrier.

        Returns:
            bool: True if the spot is a barrier, False otherwise.
        """
        return self.color == BLACK

    def is_start(self):
        """
        Returns whether the spot is the starting point.

        Returns:
            bool: True if the spot is the starting point, False otherwise.
        """
        return self.color == ORANGE

    def is_end(self):
        """
        Returns whether the spot is the target point.

        Returns:
            bool: True if the spot is the target point, False otherwise.
        """
        return self.color == TURQUOISE

    def reset(self):
        """
        Resets the color of the spot to white.
        """
        self.color = WHITE

    def make_closed(self):
        """
        Resets the color of the spot to red.
        """
        self.color = RED

    def make_open(self):
        """
        Resets the color of the spot to green.
        """
        self.color = GREEN

    def make_barrier(self):
        """
        Resets the color of the spot to black.
        """
        self.color = BLACK

    def make_end(self):
        """
        Resets the color of the spot to turquoise.
        """
        self.color = TURQUOISE

    def make_path(self):
        """
        Resets the color of the spot to purple.
        """
        self.color = PURPLE

    def make_start(self):
        """
        Resets the color of the spot to orange.
        """
        self.color = ORANGE

    def draw(self, win):
        """
        Draw a rectangle on a given window with a given color.

        Args:
            win (pygame.Surface): The window to draw on.
        """
        pygame.draw.rect(
            win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        self.neighbors = []
        # MOVE DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row + 1][self.col])

        # MOVE UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier():
            self.neighbors.append(grid[self.row - 1][self.col])

        # MOVE RIGHT
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col + 1])

        # MOVE LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier():
            self.neighbors.append(grid[self.row][self.col - 1])

    def __lt__(self, other):
        return False


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col
