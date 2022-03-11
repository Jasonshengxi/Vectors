from math import sqrt


class Vec2:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
        elif len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        else:
            raise ValueError("Invalid Quantity of input: " + str(len(args)))

    def __add__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x + other.x, self.y + other.y)
        elif type(other) in [list, tuple]:
            return Vec2(self.x + other[0], self.y + other[1])
        else:
            raise TypeError("Vec2 can only add with Vec2, list, tuple")

    def __radd__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x + other.x, self.y + other.y)
        elif type(other) in [list, tuple]:
            return [self.x + other[0], self.y + other[1]]
        else:
            raise TypeError("Vec2 can only add with Vec2, list, tuple")

    def __sub__(self, other):
        if type(other) == Vec2:
            return Vec2(self.x - other.x, self.y - other.y)
        elif type(other) in [list, tuple]:
            return Vec2(self.x - other[0], self.y - other[1])
        else:
            raise TypeError("Vec2 can only subtract with Vec2, list, tuple")

    def __rsub__(self, other):
        if type(other) == Vec2:
            return Vec2(other.x - self.x, other.y - self.y)
        elif type(other) in [list, tuple]:
            return [other[0] - self.x, other[1] - self.y]
        else:
            raise TypeError("Vec2 can only subtract with Vec2, list, tuple")

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vec2(self.x * other, self.y * other)
        if type(other) == Vec2:
            return self.x * other.x + self.y * other.y
        elif type(other) in [list, tuple]:
            return self.x * other[0] + self.y * other[1]
        else:
            raise TypeError(f"Vec2 can only multiply with Vec2, list, tuple, int, float")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in [int, float]:
            return self.__mul__(1 / other)
        else:
            raise TypeError(f"Vec2 can only divide with int, float")

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def __neg__(self):
        return Vec2(-self.x, -self.y)

    def __str__(self):
        return f"Vec2({self.x}, {self.y})"

    def dist_sq(self):
        return self.x * self.x + self.y * self.y

    def to_list(self):
        return [self.x, self.y]
