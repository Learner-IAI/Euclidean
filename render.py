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
        static GLOBAL_W, GLOBAL_H (float): Global field sizes. 
        screen (Surface): The screen to render to.
        draw(): The drawing callback.
        
    Methods:
        __init__(sw, sh, draw): The constructor.
        to_screen(xy): Convert local point coordinates to pixel coordinates.
        run(rnd): Run the main program loop.

        draw_segment(p1, p2, color): Draw the segment.
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
        pygame.init()

        pygame.display.set_caption("Outer billiard by AD1")
        icon = pygame.image.load("pent.png")
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode([sw, sh])
        self.draw = draw
    # End of '__init__' function

    '''
        Convert local point coordinates to pixel coordinates.
        Arguments:
            xy (tuple): The point coordinates.
        Returns:
            (tuple) Two integers representing the coordinates of the resulting pixel. 
    '''
    def to_screen(self, xy):
        return (int((float(xy[0]) + render.GLOBAL_W / 2) / render.GLOBAL_W * self.screen.get_width()),
                int((float(-xy[1]) + render.GLOBAL_H / 2) / render.GLOBAL_H * self.screen.get_height()))
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

    '''
        Draw the line segment.
        Arguments:
            p1, p2 (point): The edges of the segment.
            color (tuple): 3-component RGB color to draw with.
        Returns: None.
    '''
    def draw_segment(self, p1, p2, color=(0, 0, 0)):
        pygame.draw.line(self.screen, color, self.to_screen(tuple(p1)), self.to_screen(tuple(p2)))
    # End of 'draw_segment' function
# End of 'render' class

# END OF 'render.py' FILE
