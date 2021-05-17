"""
    PROJECT    : Outer billiards visualization project.
    FILE       : billiard.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Main billiard interface class implementation module.
    LAST UPDATE: 17.05.2021.
"""

from polygon import *


'''
    Outer billiard interface representation class.
    
    Fields:
        plg (polygon): The generative polygon.
        
    Methods:
        __init__(plg): The constructor.
'''
class billiard:
    '''
        The billiard class constructor.
        Arguments:
            plg (polygon): The polygon for the billiard.
    '''
    def __init__(self, plg):
        self.plg = plg
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
# End of 'billiard' class

# END OF 'billiard.py' FILE
