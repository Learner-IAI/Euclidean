import pygame

import defh
from polygon import *

if __name__ == '__main__':
    pygame.init()

    # Set up the drawing window
    defh.GLOBAL_SCREEN = pygame.display.set_mode([500, 500])

    # Run until the user asks to quit
    points = [( ABsqrt2(1, 0) / 2,  ABsqrt2(1, 1) / 2),
              ( ABsqrt2(1, 1) / 2,  ABsqrt2(1, 0) / 2),
              ( ABsqrt2(1, 1) / 2, -ABsqrt2(1, 0) / 2),
              ( ABsqrt2(1, 0) / 2, -ABsqrt2(1, 1) / 2),

              (-ABsqrt2(1, 0) / 2, -ABsqrt2(1, 1) / 2),
              (-ABsqrt2(1, 1) / 2, -ABsqrt2(1, 0) / 2),
              (-ABsqrt2(1, 1) / 2,  ABsqrt2(1, 0) / 2),
              (-ABsqrt2(1, 0) / 2,  ABsqrt2(1, 1) / 2)]

    running = True
    while running:
        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        defh.GLOBAL_SCREEN.fill((255, 255, 255))

        # Draw the polygon
        p = polygon(points)
        p.draw()

        # Flip the display
        pygame.display.flip()
    pygame.quit()
