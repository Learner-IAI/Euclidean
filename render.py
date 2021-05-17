"""
    PROJECT    : Outer billiards visualization project.
    FILE       : render.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Render abstract entity implementation module.
    LAST UPDATE: 17.05.2021.
"""

import pygame

'''
    Render entity representation class.

    Fields:
        screen (Surface): The screen to render to.
        draw(): The drawing callback.
        
    Methods:
        __init__(sw, sh, draw): The constructor.
        to_screen(xy): Convert local point coordinates to pixel coordinates.
        run(rnd): Run the main program loop.
'''
class render:
    # Global screen sizes (in local coordinate system)
    GLOBAL_W = 8
    GLOBAL_H = 8

    '''
         The render class constructor.
         Arguments:
            sw, sh (int): Screen sizes in pixels.
            draw(rnd): The drawing callback.
    '''
    def __init__(self, sw, sh, draw):
        self.screen = pygame.display.set_mode([sw, sh])
        self.draw = draw

        pygame.init()
        pygame.display.set_caption("Outer billiard by AD1")
    # End of '__init__' function

    '''
        Convert local point coordinates to pixel coordinates.
        Arguments:
            xy (tuple): The point coordinates.
        Returns:
            (tuple) Two integers representing the coordinates of the resulting pixel. 
    '''
    def to_screen(self, xy):
        return (int((xy[0] + render.GLOBAL_W / 2) / render.GLOBAL_W * self.screen.get_width()),
                int((-xy[1] + render.GLOBAL_H / 2) / render.GLOBAL_H * self.screen.get_height()))
    # End of 'to_screen' function

    '''
        Run the main program loop.
        Arguments: None.
        Returns: None.
    '''
    def run(self):
        running = True
        while running:
            # Process the quit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Draw stuff
            self.screen.fill((255, 255, 255))
            self.draw(self)

            # Flip the display
            pygame.display.flip()
        pygame.quit()
    # End of 'run' function
# End of 'render' class

# END OF 'render.py' FILE
