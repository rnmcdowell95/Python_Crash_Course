#Ryan McDowell
#Practicing detecting items hitting the edge of the screen.
#11/5/2021

import sys

import pygame

class RainDrops:
    """A class to simulate raindrops falling."""

    def __init__(self):
        """Initiliazes the raindrops class."""
         pygame.init()
        #self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (800, 640))
        pygame.display.set_caption("Alien Invasion")