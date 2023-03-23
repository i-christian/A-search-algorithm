#!/usr/bin/python3
import unittest
from unittest.mock import MagicMock
from models.a_star_algorithm import algorithm
from models.model_visualisation import Spot


class TestSpot(unittest.TestCase):
    def test_get_pos(self):
        spot = Spot(3, 4, 10, 20)
        self.assertEqual(spot.get_pos(), (3, 4))

    def test_is_closed(self):
        spot = Spot(3, 4, 10, 20)
        spot.color = (255, 0, 0)
        self.assertTrue(spot.is_closed())
        spot.color = (0, 255, 0)
        self.assertFalse(spot.is_closed())

    def test_is_open(self):
        spot = Spot(3, 4, 10, 20)
        spot.color = (0, 255, 0)
        self.assertTrue(spot.is_open())
        spot.color = (255, 0, 0)
        self.assertFalse(spot.is_open())

    def test_is_barrier(self):
        spot = Spot(3, 4, 10, 20)
        spot.color = (0, 0, 0)
        self.assertTrue(spot.is_barrier())
        spot.color = (255, 255, 255)
        self.assertFalse(spot.is_barrier())


class TestAlgorithm(unittest.TestCase):
    def setUp(self):
        pygame = MagicMock()
        pygame.event.get.return_value = []
        self.grid = [[Spot(j, i, 10, 20) for i in range(20)]
                     for j in range(20)]
        self.start = self.grid[5][5]
        self.end = self.grid[15][15]

    def test_algorithm(self):
        result = algorithm(lambda: None, self.grid, self.start, self.end)
        self.assertFalse(result)

    def test_algorithm_no_path(self):
        for i in range(6, 16):
            self.grid[i][10].color = (0, 0, 0)  # Make a barrier
        result = algorithm(lambda: None, self.grid, self.start, self.end)
        self.assertFalse(result)

    def test_unsolvable_maze(self):
        self.grid[5][6].color = (0, 0, 0)  # Make a barrier
        self.grid[5][7].color = (0, 0, 0)  # Make a barrier
        self.grid[5][8].color = (0, 0, 0)  # Make a barrier
        self.grid[5][9].color = (0, 0, 0)  # Make a barrier
        result = algorithm(lambda: None, self.grid, self.start, self.end)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
