import unittest

from cycles import count_redistributions_to_known_state, get_cycles_in_loop

input_registers = [0, 2, 7, 0]

problem_input = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

class TestRegistersClass(unittest.TestCase):
    def test_count_redistributions(self):
        self.assertEqual(5, count_redistributions_to_known_state(input_registers.copy()))

    def test_count_problem_set(self):
        self.assertEqual(3156, count_redistributions_to_known_state(problem_input.copy()))

    def test_count_cycles(self):
        self.assertEqual(4, get_cycles_in_loop(input_registers.copy()))

    def test_count_cycles_problem_set(self):
        self.assertEqual(1610, get_cycles_in_loop(problem_input.copy()))
