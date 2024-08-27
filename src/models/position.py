from math import sqrt


class Position:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def length(self):
        z = sqrt(self.x * self.x + self.y * self.y)
        return z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"<Position({self.x}, {self.y})>"

    def __hash__(self):
        return hash((self.x, self.y))

