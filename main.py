"""
    PROJECT    : Outer billiards visualization project.
    FILE       : main.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Main executable file of the project.
    LAST UPDATE: 17.05.2021.
"""

from render import *
from billiard import *


'''
    Main drawing callback.
    Arguments:
        rnd (render): The rendering context to dra.
    Returns: None.
'''
def draw(rnd):
    p = polygon.regular(12)
    blrd = billiard(p)
    p.draw(rnd, (0, 0, 0))
# End of 'draw' function


# Main executable block
if __name__ == '__main__':
    rnd = render(500, 500, draw)
    rnd.run()
# End of main executable block

# END OF 'main.py' FILE
