"""
    PROJECT    : Outer billiards visualization project.
    FILE       : polygon.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : The polygon class implementation module.
    LAST UPDATE: 17.05.2021.
"""

from math import pi, sin, cos

import defh
from defh import pygame
from ABsqrtN import ABsqrtN


'''
    The polygon representation class.
    
    Fields:
        points (tuple[]): The array of the (x, y)-tuples
                          representing each vertex coordinates.
    
    Methods:
        __init__(points): The constructor.
        draw(): Draw the polygon on the screen. 
'''
class polygon:
    '''
        The polygon class constructor.
        Arguments:
            points (tuple[]): The array of the coordinates of the vertices.
    '''
    def __init__(self, points):
        self.points = points
    # End of '__init__' function

    '''
        Draw the polygon on the screen.
        Arguments: None.
        Returns: None.
    '''
    def draw(self):
        pygame.draw.polygon(defh.GLOBAL_SCREEN, (0, 0, 0),
                            list(map(lambda x: defh.to_screen((float(x[0]), float(x[1]))), self.points)))

    '''
        Create a regular polygon of a given number of vertices and side of the length 1.
        Arguments:
            n (int): The number of polygon vertices.
        Returns:
            (polygon) A regular polygon with n vertices.
    '''
    @staticmethod
    def regular(n):
        if n == 3:
            return polygon([(0, ABsqrtN(3, 0, 1 / 3)),
                            (1 / 2, -ABsqrtN(3, 0, 1 / 6)),
                            (-1 / 2, -ABsqrtN(3, 0, 1 / 6))])
        elif n == 4:
            return polygon([(1 / 2, 1 / 2),
                            (1 / 2, -1 / 2),
                            (-1 / 2, -1 / 2),
                            (-1 / 2, 1 / 2)])
        elif n == 6:
            return polygon([(1, 0),
                            (1 / 2, -ABsqrtN(3, 0, 1 / 2)),
                            (-1 / 2, -ABsqrtN(3, 0, 1 / 2)),
                            (-1, 0),
                            (-1 / 2, ABsqrtN(3, 0, 1 / 2)),
                            (1 / 2, ABsqrtN(3, 0, 1 / 2))])
        elif n == 8:
            return polygon([(1 / 2,  ABsqrtN(2, 1, 1) / 2),
                            (ABsqrtN(2, 1, 1) / 2,  1 / 2),
                            (ABsqrtN(2, 1, 1) / 2, -1 / 2),
                            (1 / 2, -ABsqrtN(2, 1, 1) / 2),

                            (-1 / 2, -ABsqrtN(2, 1, 1) / 2),
                            (-ABsqrtN(2, 1, 1) / 2, -1 / 2),
                            (-ABsqrtN(2, 1, 1) / 2, 1 / 2),
                            (-1 / 2,  ABsqrtN(2, 1, 1) / 2)])
        else:
            mul = 2 * sin(pi / n)
            return polygon([(cos(2 * pi / n * i) / mul, sin(2 * pi / n * i) / mul) for i in range(0, n)])
    # End of 'regular' function
# End of 'polygon' class

# END OF 'polygon.py' FILE
