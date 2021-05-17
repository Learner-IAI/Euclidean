"""
    PROJECT    : Outer billiards visualization project.
    FILE       : main.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Main executable file of the project.
    LAST UPDATE: 17.05.2021.
"""

from polygon import *


# Main executable block
if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("Outer billiard by AD1")
    defh.GLOBAL_SCREEN = pygame.display.set_mode([500, 500])

    # Main program loop
    running = True
    while running:
        # Process the quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        defh.GLOBAL_SCREEN.fill((255, 255, 255))

        # Draw stuff
        p = polygon.regular(12)
        p.draw()

        # Flip the display
        pygame.display.flip()
    pygame.quit()
# End of main executable block

# END OF 'main.py' FILE
