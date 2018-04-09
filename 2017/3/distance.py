from cursor import Cursor
from square import Square
from squaremap import SquareMap
from mode import Mode


def build_until_square_satisfies_criteria(end, check, calculate):
    squares = SquareMap()
    cursor = Cursor(mode=Mode.build_x, x=0, y=0, max_degree=0)
    square: Square
    while cursor.id == 1 or not check(square, end):
        square = Square(id=cursor.id, x=cursor.x, y=cursor.y, data=calculate(squares, cursor.x, cursor.y))
        squares.add(square)
        cursor.move_cursor()
    return squares


def is_end_id(square, end):
    return square.id == end


def has_passed_max_data(square, maximum):
    return square.data > maximum


def calculate_distance(squares, x, y):
    return abs(x) + abs(y)


def calculate_neighbors(squares, x, y):
    if x == 0 and y == 0:
        return 1
    return sum(square.data for square in squares.get_neighbors(x, y))


def manhattan_distance(id):
    squares = build_until_square_satisfies_criteria(id, is_end_id, calculate_distance)
    square = squares.get_by_id(id)
    return square.data


def neighbor_distance(end_value):
    squares = build_until_square_satisfies_criteria(end_value, has_passed_max_data, calculate_neighbors)
    square = squares.last_square
    return square.data
