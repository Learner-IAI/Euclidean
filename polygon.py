"""
    PROJECT    : Outer billiards visualization project.
    FILE       : polygon.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : The polygon class implementation module.
    LAST UPDATE: 17.05.2021.
"""

import defh
from defh import pygame
from ABsqrt2 import ABsqrt2


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
# End of 'polygon' class

# END OF 'polygon.py' FILE
