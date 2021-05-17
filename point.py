"""
    PROJECT    : Outer billiards visualization project.
    FILE       : point.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : The 2d-point class implementation module.
    LAST UPDATE: 17.05.2021.
"""


'''
    The 2d-point representation class.
    
    Fields:
        x, y (numbers): Any numbers (floats or Fractions)
                        representing the point coordinates.
    
    Methods:
        __init__(x, y): The constructor.
        __add__(other),
        __sub__(other),
        __mul__(other),
        __truediv__(other): Standard arithmetic operators
                            (addition, subtraction, multiplication and division).
        __tuple__(): Cast to the tuple.
        is_right_of(other): Check the vector is 'more to the right' than the other.
        reflect_about(other): Reflect the point about the other one. 
'''
class point:
    '''
        The point class constructor.
        Arguments:
            x, y (numbers): Any numbers (floats or Fractions)
                            representing the point coordinates.
    '''
    def __init__(self, x, y=None):
        if type(x) == tuple:
            self.x = x[0]
            self.y = x[1]
        else:
            self.x = x
            self.y = y
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
        Cast point to the tuple.
        Arguments: None.
        Returns:
            (tuple) The (x, y) tuple.
    '''
    def __tuple__(self):
        return (self.x, self.y)
    # End of '__tuple__' function

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
        return 0 if det == 0 else -det / abs(det)
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


'''
    Find the 'most right' point in the array
      from the perspective of some particular point.
    Arguments:
        pnt (point): The point from which to look.
        points (point[]): The array of points to find the 'most right' one in.
    Returns:
        (point or NoneType): The rightest points from the array or
                             None if there was no one particular rightest point. 
'''
def rightest(pnt, points):
    res = points[0]
    for p in points[1:]:
        if (p - pnt).is_right_of(pnt - res) > 0:
            res = p
    for p in points:
        if p is not res and (p - pnt).is_right_of(pnt - res) == 0:
            return None
    return res
# End of 'rightest' function

# END OF 'point.py' FILE
