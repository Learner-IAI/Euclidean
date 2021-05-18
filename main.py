"""
    PROJECT    : Outer billiards visualization project.
    FILE       : main.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Main executable file of the project.
    LAST UPDATE: 18.05.2021.
"""

from render import *
import pygame
from billiard import *

# Global variables
POLYGON = None
BILLIARD = None


'''
    Init some upper-level logic.
    Arguments: None.
    Returns: None.
'''
def init():
    global POLYGON
    global BILLIARD

    POLYGON = polygon.regular(8)
    BILLIARD = billiard(POLYGON)
    BILLIARD.build_bound(1, rnd)
# End of 'init' function


'''
    Main drawing callback.
    Arguments:
        rnd (render): The rendering context.
    Returns: None.
'''
def draw(rnd):
    seg = segment(point(0, 3, 2), point(1, 3, 2))
    seg.draw(rnd, (0, 0, 255))
    refl = BILLIARD.transform(seg)
    if type(refl) == segment:
        refl.draw(rnd, (255, 0, 0))
    elif type(refl) == list:
        for s in refl:
            s.draw(rnd, (255, 0, 0))
    else:
        print(refl)

    BILLIARD.draw_polygon(rnd)
    BILLIARD.draw_bound(rnd)
# End of 'draw' function


# Main executable block
if __name__ == '__main__':
    rnd = render(500, 500, draw)
    init()

    rnd.run()
# End of main executable block

# END OF 'main.py' FILE
