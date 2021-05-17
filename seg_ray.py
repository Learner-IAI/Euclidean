"""
    PROJECT    : Outer billiards visualization project.
    FILE       : seg_ray.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : The segment class implementation module.
    LAST UPDATE: 17.05.2021.
"""

from point import *
from render import *


'''
    The segment representation class.
    
    Fields:
        p1, p2 (point): The edges of the segment.
    
    Methods:
        __init__(self, p1, p2): The constructor.
        draw(rnd, color): Draw the segment.
'''
class segment:
    '''
        The segment class constructor.
        Arguments:
            p1, p2 (point): The edges of the segment.
    '''
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    # End of '__init__' function

    '''
        Draw the segment.
        Arguments:
            rnd (render): The rendering context.
            color (tuple): 3-component RGB color.
        Returns: None.
    '''
    def draw(self, rnd, color):
        rnd.draw_segment(self.p1, self.p2, color)
    # End of 'draw' function
# End of 'segment' class

'''
    The ray representation class.

    Fields:
        p1, p2 (point): The vertex and some point on the ray.

    Methods:
        __init__(self, p1, p2): The constructor.
        draw(rnd, color): Draw the ray.
'''
class ray:
    '''
        The ray class constructor.
        Arguments:
            p1, p2 (point): The vertex and some point on the ray.
    '''
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    # End of '__init__' function

    '''
        Draw the ray.
        Arguments:
            rnd (render): The rendering context.
            color (tuple): 3-component RGB color.
        Returns: None.
    '''
    def draw(self, rnd, color):
        rnd.draw_ray(self.p1, self.p2, color)
    # End of 'draw' function
# End of 'ray' class

# END OF 'seg_ray.py' FILE
