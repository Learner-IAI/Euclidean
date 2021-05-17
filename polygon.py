import defh
from defh import pygame
from ABsqrt2 import ABsqrt2

class polygon:
    def __init__(self, points):
        self.points = points

    def draw(self):
        pygame.draw.polygon(defh.GLOBAL_SCREEN, (0, 0, 0),
                            list(map(lambda x: defh.to_screen((float(x[0]), float(x[1]))), self.points)))
