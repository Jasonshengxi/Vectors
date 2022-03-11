from math import sqrt
from numpy import array, linalg


def det(matrix):
    return linalg.det(array(matrix))


class Vec:
    def __init__(self, n, *args):
        self.n = n
        if len(args) == n:
            self.v = []
            for val in args:
                self.v.append(val)
        elif len(args) == 1:
            self.v = list(args[0])

    def copy(self):
        return Vec(self.n, self.v.copy())

    def list_add(self, other):
        result = []
        if type(other) == Vec and other.n == self.n:
            for i in range(self.n):
                result.append(self.v[i] + other.v[i])
        elif type(other) in [list, tuple]:
            for i in range(self.n):
                result.append(self.v[i] + other[i])
        else:
            raise TypeError(f"Vec{self.n} can only add with Vec{self.n}, list, tuple")
        return result

    def list_sub(self, other):
        result = []
        if type(other) == Vec and other.n == self.n:
            for i in range(self.n):
                result.append(self.v[i] - other.v[i])
        elif type(other) in [list, tuple]:
            for i in range(self.n):
                result.append(self.v[i] - other[i])
        else:
            raise TypeError(f"Vec{self.n} can only subtract with Vec{self.n}, list, tuple")
        return result

    def __add__(self, other):
        return Vec(self.n, self.list_add(other))

    def __radd__(self, other):
        result = self.list_add(other)
        if type(other) == Vec:
            return Vec(self.n, result)
        elif type(other) in [list, tuple]:
            return result

    def __sub__(self, other):
        return Vec(self.n, self.list_sub(other))

    def __rsub__(self, other):
        result = self.list_sub(other)
        if type(other) == Vec:
            return Vec(self.n, result)
        elif type(other) in [list, tuple]:
            return result

    def __mul__(self, other):
        if type(other) in [int, float]:
            result = []
            for i in range(self.n):
                result.append(self.v[i] * other)
            return Vec(self.n, result)
        else:
            result = 0
            if type(other) == Vec:
                for i in range(self.n):
                    result += self.v[i] * other.v[i]
            elif type(other) in [list, tuple]:
                for i in range(self.n):
                    result += self.v[i] * other[i]
            else:
                raise TypeError(f"Vec{self.n} can only multiply with Vec{self.n}, list, tuple, int, float")
            return result

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) in [int, float]:
            return self.__mul__(1 / other)
        else:
            raise TypeError(f"Vec{self.n} can only divide with int, float")
    
    def __abs__(self):
        return sqrt(self.__mul__(self))

    def __neg__(self):
        return Vec(self.n, list(map(lambda x: -x, self.v)))

    def __str__(self):
        string = f"Vec{self.n}("
        for i in range(self.n - 1):
            string += str(self.v[i])
            string += ", "
        string += str(self.v[self.n - 1])
        string += ")"
        return string

    def dist_sq(self):
        return self.__mul__(self)

    def cross(self, others):
        if len(others) != self.n - 2:
            raise ValueError(f"Quantity of other is not correct. Should be {self.n - 2}. Is {len(others)}")
        for other in others:
            if type(other) != Vec or other.n != self.n:
                raise TypeError(f"Vec{self.n} can only cross product with a list of {self.n - 2} Vec{self.n}")

        result = []
        for dimension in range(self.n):
            matrix = []
            row = []
            for i in range(self.n):
                if i == dimension:
                    continue
                row.append(self.v[i])
            matrix.append(row)
            for index in range(self.n - 2):
                row = []
                for i in range(self.n):
                    if i == dimension:
                        continue
                    row.append(others[index].v[i])
                matrix.append(row)
            result.append(det(matrix))
        print(result)
        return Vec(self.n, result)

    def to_list(self):
        return self.v.copy()

