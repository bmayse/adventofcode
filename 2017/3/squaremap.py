import itertools

from square import Square


class SquareMap:

    x_prime = 7
    y_prime = 13

    def __init__(self):
        self.squares_by_prime = {}
        self.squares_by_id = {}
        self.last_square = Square(0, 0, 0, 0)

    def add(self, square):
        self.squares_by_prime[self.get_prime_key(square.x, square.y)] = square
        self.squares_by_id[square.id] = square
        self.last_square = square

    def get_by_coordinates(self, x, y):
        return self.squares_by_prime[self.get_prime_key(x, y)]

    def get_by_id(self, id):
        return self.squares_by_id[id]

    def get_prime_key(self, x, y):
        return self.x_prime * x + self.y_prime * y

    def get_neighbors(self, x, y):
        neighbors = []
        for x_neighbor_index, y_neighbor_index in itertools.product(range(x - 1, x + 2), range(y - 1, y + 2)):
            key = self.get_prime_key(x_neighbor_index, y_neighbor_index)
            if key in self.squares_by_prime and key != self.get_prime_key(x, y):
                neighbors.append(self.squares_by_prime[key])
        return neighbors
