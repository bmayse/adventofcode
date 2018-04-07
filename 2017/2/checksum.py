import itertools


def line_to_number_array(line):
    return (int(number) for number in line.split())


def list_lines_with_processor(input, process_line):
    return (process_line(line) for line in input.splitlines())


def get_max_difference(numbers):
    number_list = list(element for element in numbers)
    if len(number_list) == 0: return 0
    minimum = min(number_list)
    maximum = max(number_list)
    return maximum - minimum


def get_only_divisible_result(numbers):
    for x,y in itertools.permutations(numbers, 2):
        result = x / y
        if result == x//y and result != 1:
            return result
    return 0


def get_sum_of_line_evaluations(input, evaluate_line):
    number_grid_generator = list_lines_with_processor(input, line_to_number_array)
    line_evaluations = list(evaluate_line(line) for line in number_grid_generator)
    return sum(line_evaluations)


