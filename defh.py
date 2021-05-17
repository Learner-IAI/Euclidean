"""
    PROJECT    : Outer billiards visualization project.
    FILE       : defh.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : The universal 'include' file.
    LAST UPDATE: 17.05.2021.
"""

import pygame


# Global screen surface variable (None by default)
GLOBAL_SCREEN = None


'''
    Convert local point coordinates to pixel coordinates.
    Arguments:
        xy (tuple): The point coordinates.
        w, h (float): Window sizes in local coordinate system (5x5 by default).
        screen (Surface): The pygame object to draw to (sets to GLOBAL_SCREEN by default).
    Returns:
        (tuple) Two integers representing the coordinates of the resulting pixel. 
'''
def to_screen(xy, w=5, h=5, screen=None):
    if not screen:
        screen = GLOBAL_SCREEN
    return (int((xy[0] + w / 2) / w * screen.get_width()), int((-xy[1] + h / 2) / h * screen.get_height()))
# End of 'to_screen' function

# END OF 'defh.py' FILE
