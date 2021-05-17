"""
    PROJECT    : Outer billiards visualization project.
    FILE       : billiard.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Main billiard interface class implementation module.
    LAST UPDATE: 17.05.2021.
"""

from polygon import *
from seg_ray import *


'''
    Outer billiard interface representation class.
    
    Fields:
        plg (polygon): The generative polygon.
        _bound_iter (int): Current boundary iteration.
        bound (array[]): The boundary elements array (rays and segments).
        
    Methods:
        __init__(plg): The constructor.
        transform(p): Transform the point by the billiard.
        
        draw_polygon(rnd, color): Draw the generative polygon.
        
        build_bound(n): Build the billiard boundary after the n-th iteration.
        draw_bound(rnd , color): Draw the evaluated boundary.
'''
class billiard:
    '''
        The billiard class constructor.
        Arguments:
            plg (polygon): The polygon for the billiard.
    '''
    def __init__(self, plg):
        self.plg = plg
        self.bound = []
        self._bound_iter = 0
    # End of '__init__' function

    '''
        Transform the point by the billiard.
        Arguments:
            p (point): The point to transform.
        Returns:
            (point) The transformed point. 
    '''
    def transform(self, p):
        return p.reflect_about(rightest(p, self.plg.points))
    # End of 'transform' function

    '''
        Draw the generative polygon.
        Arguments:
            rnd (render): The rendering context.
            color (tuple): 3-component RGB color.
        Returns: None.
    '''
    def draw_polygon(self, rnd, color=(0, 0, 0)):
        self.plg.draw(rnd, color)
    # End of 'draw_polygon' function

    '''
        Build the billiard boundary after the n-th iteration.
        Arguments:
            n (int): Number of iterations to build boundary for.
        Returns: None.
    '''
    def build_bound(self, n):
        if self._bound_iter >= n:
            return
        self._bound_iter = n
        for i in range(len(self.plg.points)):
            self.bound.append(ray(self.plg.points[i], self.plg.points[(i - 1) % len(self.plg.points)]))
    # End of 'build_bound' function

    '''
        Draw the evaluated boundary.
        Arguments:
            rnd (render): The rendering context.
            color (tuple): 3-component RGB color.
        Returns: None.
    '''
    def draw_bound(self, rnd, color=(0, 0, 0)):
        for elem in self.bound:
            elem.draw(rnd, color)
    # End of 'draw_bound' function
# End of 'billiard' class

# END OF 'billiard.py' FILE
