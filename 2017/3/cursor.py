from mode import Mode


class Cursor:
    def __init__(self, mode, x, y, max_degree):
        self.mode = mode
        self.x = x
        self.y = y
        self.max_degree = max_degree
        self.id = 1

    def move_cursor(self):
        if self.mode == Mode.build_y:
            self.handle_positive_y()
        elif self.mode == Mode.reduce_x:
            self.handle_negative_x()
        elif self.mode == Mode.reduce_y:
            self.handle_negative_y()
        else:
            self.handle_positive_x()
        self.id += 1

    def handle_positive_x(self):
        if self.x == self.max_degree:
            self.mode = Mode.build_y
            self.max_degree += 1
        self.x += 1

    def handle_negative_y(self):
        if abs(self.y) == self.max_degree:
            self.mode = Mode.build_x
            self.x += 1
        else:
            self.y -= 1

    def handle_negative_x(self):
        if abs(self.x) == self.max_degree:
            self.mode = Mode.reduce_y
            self.y -= 1
        else:
            self.x -= 1

    def handle_positive_y(self):
        if self.y == self.max_degree:
            self.mode = Mode.reduce_x
            self.x -= 1
        else:
            self.y += 1
