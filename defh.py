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
# Global screen sizes (in local coordinate system)
GLOBAL_W = 8
GLOBAL_H = 8


'''
    Convert local point coordinates to pixel coordinates.
    Arguments:
        xy (tuple): The point coordinates.
        screen (Surface): The pygame object to draw to (sets to GLOBAL_SCREEN by default).
    Returns:
        (tuple) Two integers representing the coordinates of the resulting pixel. 
'''
def to_screen(xy, screen=None):
    if not screen:
        screen = GLOBAL_SCREEN
    return (int((xy[0] + GLOBAL_W / 2) / GLOBAL_W * screen.get_width()),
            int((-xy[1] + GLOBAL_H / 2) / GLOBAL_H * screen.get_height()))
# End of 'to_screen' function

# END OF 'defh.py' FILE
