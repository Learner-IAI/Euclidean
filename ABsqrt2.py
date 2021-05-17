"""
    PROJECT    : Outer billiards visualization project.
    FILE       : ABsqrt2.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : This module contains one class
                 to represent the numbers of the form a + sqrt(2) * b.
    LAST UPDATE: 17.05.2021.
"""

from fractions import *


'''
    Number of the form a + sqrt(2) * b representation class.

    Fields:
        _a, _b (Fraction): Rational coefficients representing the a and b.
        
    Methods:
        __init__(a, b): The constructor
        __neg__(): Unary minus operator.
        __add__(other),
        __sub__(other),
        __mul__(other),
        __truediv__(other): Standard arithmetic operators 
                            (addition, subtraction, multiplication and division).
        __float__(): Cast to the floating point number.
'''
class ABsqrt2:
    '''
        The ABsqrt2 constructor.
        Arguments:
            a, b (numbers): Any rational numbers.
    '''
    def __init__(self, a, b):
        self._a = Fraction(a)
        self._b = Fraction(b)
    # End of '__init__' function

    '''
        Unary minus operator.
        Arguments: None.
        Returns:
            (ABsqrt2) Negated number.
    '''
    def __neg__(self):
        return ABsqrt2(-self._a, -self._b)
    # End of '__neg__' function

    '''
        Addition (+) operator.
        Arguments:
            other (ABsqrt2): The number to sum with.
        Returns:
            (ABsqrt2) The sum of two numbers.
    '''
    def __add__(self, other):
        return ABsqrt2(self._a + other._a, self._b + other._b)
    # End of '__add__' function

    '''
        Subtraction (-) operator.
        Arguments:
            other (ABsqrt2): The number to subtract.
        Returns:
            (ABsqrt2) The difference of two numbers.
    '''
    def __sub__(self, other):
        return ABsqrt2(self._a - other._a, self._b - other._b)
    # End of '__sub__' function

    '''
        Multiplication (*) operator.
        Arguments:
            other (ABsqrt2): The number to multiply with.
        Returns:
            (ABsqrt2) The product of two numbers.
    '''
    def __mul__(self, other):
        if type(other) == type(self):
            return ABsqrt2(self._a * other.a + 2 * self._b * other._b, self._a * other._b + self._b * other._a)
        else:
            return ABsqrt2(self._a * other, self._b * other)
    # End of '__mul__' function

    '''
        Division (/) operator.
        Arguments:
            other (ABsqrt2): The nonzero number to divide on.
        Returns:
            (ABsqrt2) The quotient of two numbers.
    '''
    def __truediv__(self, other):
        if type(other) == type(self):
            return ABsqrt2((self._a * other.a - 2 * self._b * other._b) / (other._a * other._a - 2 * other._b * other._b),
                           (-self._a * other._b + self._b * other._a) / (other._a * other._a - 2 * other._b * other._b))
        else:
            return ABsqrt2(self._a / other, self._b / other)
    # End of '__truediv__' function

    '''
        Cast to the floating point number.
        Arguments: None.
        Returns:
            (float) The approximate value of the representing number.
    '''
    def __float__(self):
        return float(self._a) + 2**0.5 * float(self._b)
    # End of '__float__' function
# End of 'ABsqrt2' class

# END OF 'ABsqrt2.py' FILE
