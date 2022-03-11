from math import sqrt
from numpy import array, linalg


def det(matrix):
    return linalg.det(array(matrix))


class Vec3:
    def __init__(self, *args):
        if len(args) == 1:
            self.x = args[0][0]
            self.y = args[0][1]
            self.z = args[0][2]
        elif len(args) == 3:
            self.x = args[0]
            self.y = args[1]
            self.z = args[2]
        else:
            raise ValueError("Invalid Quantity of input: " + str(len(args)))

    def __add__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif type(other) in [list, tuple]:
            return Vec3(self.x + other[0], self.y + other[1], self.z + other[2])
        else:
            raise TypeError("Vec3 can only add with Vec3, list, tuple")

    def __radd__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif type(other) in [list, tuple]:
            return [self.x + other[0], self.y + other[1], self.z + other[2]]
        else:
            raise TypeError("Vec3 can only add with Vec3, list, tuple")

    def __sub__(self, other):
        if type(other) == Vec3:
            return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif type(other) in [list, tuple]:
            return Vec3(self.x - other[0], self.y - other[1], self.z - other[2])
        else:
            raise TypeError("Vec3 can only subtract with Vec3, list, tuple")

    def __rsub__(self, other):
        if type(other) == Vec3:
            return Vec3(other.x - self.x, other.y - self.y, other.z - self.z)
        elif type(other) in [list, tuple]:
            return [other[0] - self.x, other[1] - self.y, other[2] - self.z]
        else:
            raise TypeError("Vec3 can only subtract with Vec3, list, tuple")

    def __mul__(self, other):
        if type(other) in [int, float]:
            return Vec3(self.x * other, self.y * other, self.z * other)
        if type(other) == Vec3:
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) in [list, tuple]:
            return self.x * other[0] + self.y * other[1] + self.z * other[2]
        else:
            raise TypeError(f"Vec3 can only multiply with Vec3, list, tuple, int, float")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in [int, float]:
            return self.__mul__(1 / other)
        else:
            raise TypeError(f"Vec3 can only divide with int, float")

    def __abs__(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z)

    def __neg__(self):
        return Vec3(-self.x, -self.y, -self.z)

    def __str__(self):
        return f"Vec3({self.x}, {self.y}, {self.z})"

    def dist_sq(self):
        return self.x * self.x + self.y * self.y + self.z * self.z

    def cross(self, other):
        return Vec3(
            det([[self.y, self.z], [other.y, other.z]]),
            -det([[self.x, self.z], [other.x, other.z]]),
            det([[self.x, self.y], [other.x, other.y]]),
        )

    def to_list(self):
        return [self.x, self.y, self.z]
