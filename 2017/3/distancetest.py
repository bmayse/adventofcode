import unittest

from distance import manhattan_distance, neighbor_distance


class TestDistanceFunctions(unittest.TestCase):

    def test_manhattan_distance_base(self):
        self.assertEqual(0, manhattan_distance(1))

    def test_manhattan_distance_corner(self):
        self.assertEqual(4, manhattan_distance(13))

    def test_manhattan_distance_straight(self):
        self.assertEqual(2, manhattan_distance(23))

    def test_manhattan_distance_far(self):
        self.assertEqual(31, manhattan_distance(1024))

    def test_neighbors_base(self):
        self.assertEqual(1, neighbor_distance(0))

    def test_neighbors_early(self):
        self.assertEqual(2, neighbor_distance(1))

    def test_neighbors_far(self):
        self.assertEqual(369601, neighbor_distance(368078))
