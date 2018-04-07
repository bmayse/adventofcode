import unittest

from checksum import line_to_number_array, list_lines_with_processor, get_sum_of_line_evaluations, \
    get_max_difference, get_only_divisible_result


single_line = "1 22 456     2"
single_line_result = [1, 22, 456, 2]

multi_line = "1 22 43 \n 77 \n   \n 22 33 44"
multi_line_result = [[1, 22, 43], [77], [], [22, 33, 44]]

single_line_with_divisibility_result = [7, 13, 28, 12]

multi_line_with_divisibility = "7   13 28   12 \n \n    7  13 5 31   25 6"


class TestChecksumFunctions(unittest.TestCase):
    def test_line_to_number_array(self):
        self.assertEqual(single_line_result, list(line_to_number_array(single_line)))

    def test_line_to_number_array_empty(self):
        self.assertEqual([], list(line_to_number_array("")))

    def test_list_lines_with_processor_ensure_provided_processor_used(self):
        self.assertEqual(["a", "a", "a", "a"], list(list_lines_with_processor(multi_line, test_sublist_generator)))

    def test_get_max_difference(self):
        self.assertEqual(455, get_max_difference(single_line_result))

    def test_get_max_difference_empty_line(self):
        self.assertEqual(0, get_max_difference([]))

    def test_get_only_divisible_result(self):
        self.assertEqual(4, get_only_divisible_result(single_line_with_divisibility_result))

    def test_max_difference_multiple_lines(self):
        self.assertEqual(64, get_sum_of_line_evaluations(multi_line, get_max_difference))

    def test_only_divisible_result_multiple_lines(self):
        self.assertEqual(9, get_sum_of_line_evaluations(multi_line_with_divisibility, get_only_divisible_result))


def test_sublist_generator(line):
    return "a"