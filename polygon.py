"""
    PROJECT    : Outer billiards visualization project.
    FILE       : polygon.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : The polygon class implementation module.
    LAST UPDATE: 17.05.2021.
"""

from math import pi, sin, cos

from render import *
from ABsqrtN import ABsqrtN
from point import *


'''
    The polygon representation class.
    
    Fields:
        points (point[]): The array of the (x, y)-tuples
                          representing each vertex coordinates.
    
    Methods:
        __init__(points): The constructor.
        draw(color): Draw the polygon on the screen.
        static regular(n): Create the regular polygon with n vertices.
'''
class polygon:
    '''
        The polygon class constructor.
        Arguments:
            points (tuple[]): The array of the coordinates of the vertices.
            n_for_sqrt (int): The number under the radical for ABsqrtN-polygons.
    '''
    def __init__(self, points, n_for_sqrt=0):
        self.points = [point(xy[0], xy[1], n_for_sqrt) for xy in points]
    # End of '__init__' function

    '''
        Draw the polygon on the screen.
        Arguments:
            rnd (render): The rendering context to draw in.
            color (tuple): 3-component RGB color to draw with.
        Returns: None.
    '''
    def draw(self, rnd, color):
        pygame.draw.polygon(rnd.screen, color,
                            list(map(lambda p: rnd.to_screen((float(p.x), float(p.y))), self.points)))
    # End of 'draw' function

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
            return polygon([(ABsqrtN(3, 0), ABsqrtN(3, 0, 1 / 3)),
                            (ABsqrtN(3, 1 / 2), -ABsqrtN(3, 0, 1 / 6)),
                            (ABsqrtN(3, -1 / 2), -ABsqrtN(3, 0, 1 / 6))], 3)
        elif n == 4:
            return polygon([(ABsqrtN(2, 1 / 2), ABsqrtN(2, 1 / 2)),
                            (ABsqrtN(2, 1 / 2), ABsqrtN(2, -1 / 2)),
                            (ABsqrtN(2, -1 / 2), ABsqrtN(2, -1 / 2)),
                            (ABsqrtN(2, -1 / 2), ABsqrtN(2, 1 / 2))], 2)
        elif n == 6:
            return polygon([(ABsqrtN(3, 1), ABsqrtN(3, 0)),
                            (ABsqrtN(3, 1 / 2), -ABsqrtN(3, 0, 1 / 2)),
                            (ABsqrtN(3, -1 / 2), -ABsqrtN(3, 0, 1 / 2)),
                            (ABsqrtN(3, -1), ABsqrtN(3, 0)),
                            (ABsqrtN(3, -1 / 2), ABsqrtN(3, 0, 1 / 2)),
                            (ABsqrtN(3, 1 / 2), ABsqrtN(3, 0, 1 / 2))], 3)
        elif n == 8:
            return polygon([(ABsqrtN(2, 1 / 2),  ABsqrtN(2, 1, 1) / 2),
                            (ABsqrtN(2, 1, 1) / 2,  ABsqrtN(2, 1 / 2)),
                            (ABsqrtN(2, 1, 1) / 2, ABsqrtN(2, -1 / 2)),
                            (ABsqrtN(2, 1 / 2), -ABsqrtN(2, 1, 1) / 2),

                            (ABsqrtN(2, -1 / 2), -ABsqrtN(2, 1, 1) / 2),
                            (-ABsqrtN(2, 1, 1) / 2, ABsqrtN(2, -1 / 2)),
                            (-ABsqrtN(2, 1, 1) / 2, ABsqrtN(2, 1 / 2)),
                            (ABsqrtN(2, -1 / 2),  ABsqrtN(2, 1, 1) / 2)], 2)
        else:
            mul = 2 * sin(pi / n)
            return polygon([(cos(-2 * pi / n * i) / mul, sin(-2 * pi / n * i) / mul) for i in range(0, n)])
    # End of 'regular' function
# End of 'polygon' class

# END OF 'polygon.py' FILE
