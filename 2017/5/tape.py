from Node import Node


def traverse_input_standard_step(filename):
    return run_tape(build_tape(filename), increment)


def traverse_input_converge_to_three_step(filename):
    return run_tape(build_tape(filename), decrement_if_large)


def increment(value):
    return value + 1


def decrement_if_large(value):
    if value > 2:
        return value - 1
    return value + 1


def read_file(filename):
    with open(filename) as file:
        for line in file:
            yield line


def build_tape(filename):
    prev, root = None, None
    for number in read_file(filename):
        if root is None:
            root = Node(int(number), None, None)
            prev = root
        else:
            cur = Node(int(number), prev, None)
            prev.right = cur
            prev = cur
    return root


def run_tape(cur, value_operation):
    iterations = 0
    while cur is not None:
        iterations += 1
        cur = cur.apply_then_find_next_node(cur.value, value_operation)
    return iterations




