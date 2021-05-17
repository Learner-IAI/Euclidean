"""
    PROJECT    : Outer billiards visualization project.
    FILE       : main.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Main executable file of the project.
    LAST UPDATE: 17.05.2021.
"""

from render import *
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

    POLYGON = polygon.regular(5)
    BILLIARD = billiard(POLYGON)
    BILLIARD.build_bound(1)
# End of 'init' function


'''
    Main drawing callback.
    Arguments:
        rnd (render): The rendering context.
    Returns: None.
'''
def draw(rnd):
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
