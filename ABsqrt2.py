from fractions import *


class ABsqrt2:
    def __init__(self, a, b):
        self._a = Fraction(a)
        self._b = Fraction(b)

    def __neg__(self):
        return ABsqrt2(-self._a, -self._b)

    def __add__(self, other):
        return ABsqrt2(self._a + other._a, self._b + other._b)

    def __sub__(self, other):
        return ABsqrt2(self._a - other._a, self._b - other._b)

    def __mul__(self, other):
        if type(other) == type(self):
            return ABsqrt2(self._a * other.a + 2 * self._b * other._b, self._a * other._b + self._b * other._a)
        else:
            return ABsqrt2(self._a * other, self._b * other)

    def __truediv__(self, other):
        if type(other) == type(self):
            return ABsqrt2((self._a * other.a - 2 * self._b * other._b) / (other._a * other._a - 2 * other._b * other._b),
                           (-self._a * other._b + self._b * other._a) / (other._a * other._a - 2 * other._b * other._b))
        else:
            return ABsqrt2(self._a / other, self._b / other)

    def __float__(self):
        return float(self._a) + 2**0.5 * float(self._b)
