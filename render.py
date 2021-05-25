"""
    PROJECT    : Outer billiards visualization project.
    FILE       : render.py
    AUTHOR     : Andrey Dmitrenko.
    PURPOSE    : Render abstract entity implementation module.
    LAST UPDATE: 19.05.2021.
"""

import pygame


'''
    Coordinate system representation class.
    
    Fields:
        cx, cy (float): Relative center position.
        w, h (float): The field sizes.
        sw, sh (int): Actual screen sizes in pixels.
        
    Methods:
        __init__(cx, cy, w, h, sw, sh): The constructor.
        to_screen(xy): Convert local point coordinates to pixel coordinates.
'''
class cor_sys:
    '''
        The coordinate system class constructor.
        Arguments:
            cx, cy (float): Relative center position.
            w, h (float): The field sizes.
            sw, sh (int): Actual screen sizes in pixels.
    '''
    def __init__(self, cx, cy, w, h, sw, sh):
        self.cx = cx
        self.cy = cy

        self.w = w
        self.h = h

        self.sw = sw
        self.sh = sh
    # End of '__init__' function

    '''
        Convert local point coordinates to pixel coordinates.
        Arguments:
            xy (tuple): The point coordinates.
        Returns:
            (tuple) Two integers representing the coordinates of the resulting pixel. 
    '''
    def to_screen(self, xy):
        return (int(((float(xy[0]) + self.cx) + self.w / 2) / self.w * self.sw),
                int(((float(-(xy[1] + self.cy))) + self.h / 2) / self.h * self.sh))
    # End of 'to_screen' function
# End of 'cor_sys' class


'''
    Render entity representation class.

    Fields:
        screen (Surface): The screen to render to.
        cs (cor_sys): The coordinate system to work with.
        draw(): The drawing callback.
        
    Methods:
        __init__(sw, sh, draw): The constructor.
        run(rnd): Run the main program loop.

        draw_segment(p1, p2, color): Draw the segment.
'''
class render:
    '''
         The render class constructor.
         Arguments:
            sw, sh (int): Screen sizes in pixels.
            draw(rnd): The drawing callback.
    '''
    def __init__(self, cs, draw):
        pygame.init()

        pygame.display.set_caption("Outer billiard by AD1")
        icon = pygame.image.load("pent.png")
        pygame.display.set_icon(icon)

        self.screen = pygame.display.set_mode([cs.sw, cs.sh])
        self.cs = cs
        self.draw = draw
    # End of '__init__' function

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
        pygame.draw.line(self.screen, color, self.cs.to_screen(tuple(p1)), self.cs.to_screen(tuple(p2)))
    # End of 'draw_segment' function
# End of 'render' class

# END OF 'render.py' FILE
