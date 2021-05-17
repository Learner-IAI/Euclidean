import pygame


GLOBAL_SCREEN = None


def to_screen(xy, w=5, h=5, screen=None):
    if not screen:
        screen = GLOBAL_SCREEN
    return ((xy[0] + w / 2) / w * screen.get_width(), (-xy[1] + h / 2) / h * screen.get_height())
