import unittest

from tape import traverse_input_standard_step, traverse_input_converge_to_three_step

class TestTapeClass(unittest.TestCase):
    def test_tape_small(self):
        self.assertEqual(5, traverse_input_standard_step("small_input.txt"))

    def test_tape_big(self):
        self.assertEqual(358309, traverse_input_standard_step("input.txt"))

    def test_tape_small_converge(self):
        self.assertEqual(10, traverse_input_converge_to_three_step("small_input.txt"))

    def test_tape_large_converge(self):
        self.assertEqual(28178177, traverse_input_converge_to_three_step("input.txt"))
