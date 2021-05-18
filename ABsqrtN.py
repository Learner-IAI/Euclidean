"""
    PROJECT    : Outer billiards visualization project.
    FILE       : ABsqrtN.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : This module contains one class
                 to represent the numbers of the form a + sqrt(2) * b.
    LAST UPDATE: 18.05.2021.
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
                            (addition, subtraction, multiplication and division)

        __float__(): Cast to the floating point number.
        __int__(): Cast to the integer.
        __lt__(other): 'less than' comparation operator.
        __gt__(other): 'greater than' comparation operator.
'''
class ABsqrtN:
    '''
        The ABsqrtN constructor.
        Arguments:
            N (int): The number to be under the radical
            a, b (numbers): Any rational numbers.
    '''
    def __init__(self, N, a=None, b=None):
        if type(N) is type(self):
            self.N = N.N
            self._a = N._a
            self._b = N._b
        else:
            if a is None:
                self.N = 0
                self._a = Fraction(N)
                self._b = Fraction(0)
            else:
                if type(a) is type(self):
                    self.N = a.N
                    self._a = a._a
                    self._b = a._b
                else:
                    self.N = N
                    self._a = Fraction(a)
                    if b is None:
                        self._b = Fraction(0)
                    else:
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
        other = ABsqrtN(other)
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
        other = ABsqrtN(other)
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
            return ABsqrtN(self.N, self._a * other._a + self.N * self._b * other._b,
                           self._a * other._b + self._b * other._a)
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
            return ABsqrtN(self.N, (self._a * other._a - self.N * self._b * other._b) / denom,
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

    '''
        Cast to the integer.
        Arguments: None.
        Returns:
            (int) The approximate integer value of the representing number.
    '''
    def __int__(self):
        return int(float(self))
    # End of '__int__' function
    
    '''
    	'less than' comparation operator.
    	Argements:
    		other (ABsqrtN): Number to compare with.
    	Returns:
    		(bool) True if self < other, False otherwise.
    '''
    def __lt__(self, other):
    	return float(self) < float(other)
    # End of '__lt__' function
    
    '''
    	'greater than' comparation operator.
    	Argements:
    		other (ABsqrtN): Number to compare with.
    	Returns:
    		(bool) True if self > other, False otherwise.
    '''
    def __gt__(self, other):
    	return float(self) > float(other)
    # End of '__gt__' function
# End of 'ABsqrtN' class

# END OF 'ABsqrtN.py' FILE
