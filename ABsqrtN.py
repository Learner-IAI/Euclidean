"""
    PROJECT    : Outer billiards visualization project.
    FILE       : ABsqrtN.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : This module contains one class
                 to represent the numbers of the form a + sqrt(2) * b.
    LAST UPDATE: 17.05.2021.
"""

from fractions import *


'''
    Number of the form a + sqrt(N) * b representation class.

    Fields:
        N (int): The whole number under the radical.
        _a, _b (Fraction): Rational coefficients representing the a and b.
        
    Methods:
        __init__(N, a, b): The constructor
        __neg__(): Unary minus operator.
        __add__(other),
        __sub__(other),
        __mul__(other),
        __truediv__(other): Standard arithmetic operators 
                            (addition, subtraction, multiplication and division).
        __float__(): Cast to the floating point number.
'''
class ABsqrtN:
    '''
        The ABsqrtN constructor.
        Arguments:
            N (int): The number to be under the radical
            a, b (numbers): Any rational numbers.
    '''
    def __init__(self, N, a, b):
        self.N = N
        self._a = Fraction(a)
        self._b = Fraction(b)
    # End of '__init__' function

    '''
        Unary minus operator.
        Arguments: None.
        Returns:
            (ABsqrtN) Negated number.
    '''
    def __neg__(self):
        return ABsqrtN(self.N, -self._a, -self._b)
    # End of '__neg__' function

    '''
        Addition (+) operator.
        Arguments:
            other (ABsqrtN): The number to sum with.
        Returns:
            (ABsqrtN) The sum of two numbers.
    '''
    def __add__(self, other):
        return ABsqrtN(self.N, self._a + other._a, self._b + other._b)
    # End of '__add__' function

    '''
        Subtraction (-) operator.
        Arguments:
            other (ABsqrtN): The number to subtract.
        Returns:
            (ABsqrtN) The difference of two numbers.
    '''
    def __sub__(self, other):
        return ABsqrtN(self.N, self._a - other._a, self._b - other._b)
    # End of '__sub__' function

    '''
        Multiplication (*) operator.
        Arguments:
            other (ABsqrtN): The number to multiply with.
        Returns:
            (ABsqrtN) The product of two numbers.
    '''
    def __mul__(self, other):
        if type(other) == type(self):
            return ABsqrtN(self.N, self._a * other.a + self.N * self._b * other._b, self._a * other._b + self._b * other._a)
        else:
            return ABsqrtN(self.N, self._a * other, self._b * other)
    # End of '__mul__' function

    '''
        Division (/) operator.
        Arguments:
            other (ABsqrtN): The nonzero number to divide on.
        Returns:
            (ABsqrtN) The quotient of two numbers.
    '''
    def __truediv__(self, other):
        if type(other) == type(self):
            denom = other._a * other._a - self.N * other._b * other._b
            return ABsqrtN(self.N, (self._a * other.a - self.N * self._b * other._b) / denom,
                                   (-self._a * other._b + self._b * other._a) / denom)
        else:
            return ABsqrtN(self.N, self._a / other, self._b / other)
    # End of '__truediv__' function

    '''
        Cast to the floating point number.
        Arguments: None.
        Returns:
            (float) The approximate value of the representing number.
    '''
    def __float__(self):
        return float(self._a) + self.N**0.5 * float(self._b)
    # End of '__float__' function
# End of 'ABsqrtN' class

# END OF 'ABsqrtN.py' FILE
