"""
    PROJECT    : Outer billiards visualization project.
    FILE       : point.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : The 2d-point class implementation module.
    LAST UPDATE: 18.05.2021.
"""

from ABsqrtN import *


'''
    The 2d-point representation class.
    
    Fields:
        x, y (numbers): Any numbers (floats or Fractions)
                        representing the point coordinates.
    
    Methods:
        __init__(x, y, n_for_sqrt): The constructor.
        __add__(other),
        __sub__(other),
        __mul__(other),
        __truediv__(other): Standard arithmetic operators
                            (addition, subtraction, multiplication and division).
        __iter__(): Iterate the point (needed for the tuple cast mostly).
        is_right_of(other): Check the vector is 'more to the right' than the other.
        reflect_about(other): Reflect the point about the other one. 
'''
class point:
    '''
        The point class constructor.
        Arguments:
            x, y (numbers): Any numbers (floats or Fractions or ABsqrtN-s)
                            representing the point coordinates.
            n_for_sqrt (int): The number under the radical for ABsqrtN-points.
    '''
    def __init__(self, x, y, n_for_sqrt=0):
        if type(x) == tuple:
            self.x = ABsqrtN(n_for_sqrt, x[0])
            self.y = ABsqrtN(n_for_sqrt, x[1])
        else:
            self.x = ABsqrtN(n_for_sqrt, x)
            self.y = ABsqrtN(n_for_sqrt, y)
    # End of '__init__' function

    '''
        Addition (+) operator.
        Arguments:
            other (point): The vector to sum with.
        Returns:
            (point) The sum of two vectors.
    '''
    def __add__(self, other):
        return point(self.x + other.x, self.y + other.y)
    # End of '__add__' function

    '''
        Subtraction (-) operator.
        Arguments:
            other (point): The vector to subtract.
        Returns:
            (point) The difference of two vectors.
    '''
    def __sub__(self, other):
        return point(self.x - other.x, self.y - other.y)
    # End of '__sub__' function

    '''
        Multiplication (*) operator.
        Arguments:
            other (point or number): The point to find dot product with or
                                     the number to multiply by.
        Returns:
            (number or point) The dot product of two vectors or a vector multiplied by a scalar.
    '''
    def __mul__(self, other):
        if type(other) == type(self):
            return self.x * other.x + self.y * other.y
        return point(self.x * other, self.y * other)
    # End of '__mul__' function

    '''
        Division (/) operator.
        Arguments:
            other (number): The number to divide by.
        Returns:
            (point) The vector divided by a scalar.
    '''
    def __truediv__(self, other):
        return point(self.x / other, self.y / other)
    # End of '__truediv__' function

    '''
        Iterate the point (needed for the tuple cast mostly).
        Arguments: None.
        Yields: 
            (number) The point coordinate.
    '''
    def __iter__(self):
        yield self.x
        yield self.y
    # End of '__iter__' function

    '''
        Check if the vector is 'more to the right' than the other one.
        Arguments:
            other (point): The vector to compare with.
        Returns:
            (int)  1 if the 'self' is righter;
                   0 if they are collinear;
                  -1 otherwise.  
    '''
    def is_right_of(self, other):
        det = self.x * other.y - self.y * other.x
        return 0 if float(det) == 0 else -float(det) / abs(float(det))
    # End of 'is_right_of' function

    '''
        Reflect the point about the other point.
        Arguments:
            other (point): The point to reflect about.
        Returns:
            (point) The reflected point.
    '''
    def reflect_about(self, other):
        return self + (other - self) * 2
    # End of 'reflect_about' function
# End of 'point' class

# END OF 'point.py' FILE
