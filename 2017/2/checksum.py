import itertools


def line_to_number_array(line):
    return list(int(number) for number in line.split())


def list_lines_with_processor(input, process_line):
    return list(process_line(line) for line in input.splitlines())


def get_max_difference(numbers):
    if len(numbers) == 0: return 0
    minimum = min(element for element in numbers)
    maximum = max(element for element in numbers)
    return maximum - minimum


def get_only_divisible_result(numbers):
    if len(numbers) == 0: return 0
    for x,y in itertools.permutations(numbers, 2):
        result = x / y
        if result == x//y and result != 1:
            return result


def get_sum_of_line_evaluations(input, evaluate_line):
    number_grid = list_lines_with_processor(input, line_to_number_array)
    line_evaluations = list(evaluate_line(line) for line in number_grid)
    return sum(line_evaluations)


