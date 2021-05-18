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
        Calculate the intersection with other segment (treating segments as lines).
        Arguments:
            other (segment): The segment to calculate intersection with.
        Returns:
            (point or NoneType) The intersection point or None if no such exists.
    '''
    def intersect(self, other):
        x1 = self.p1.x; x2 = self.p2.x
        x3 = other.p1.x; x4 = other.p2.x
        y1 = self.p1.y; y2 = self.p2.y
        y3 = other.p1.y; y4 = other.p2.y

        det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if det == 0:
            return None
        split_pnt = point(((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / det,
                          ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / det)
    # End of 'intersect' function

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
        while (abs(float(self.p2.x)) < render.GLOBAL_W / 2 and
               abs(float(self.p2.y)) < render.GLOBAL_H / 2):
            self.p2 += p2 - p1
    # End of '__init__' function

    '''
        Draw the ray.
        Arguments:
            rnd (render): The rendering context.
            color (tuple): 3-component RGB color.
        Returns: None.
    '''
    def draw(self, rnd, color):
        rnd.draw_segment(self.p1, self.p2, color)
    # End of 'draw' function
# End of 'ray' class

# END OF 'seg_ray.py' FILE
