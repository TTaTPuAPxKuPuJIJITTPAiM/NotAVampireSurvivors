import pygame

from game.config.cfg import *

class Level:
    def __init__(self, displaySurface):
        self.displaySurface = displaySurface
        self.bg_level = pygame.image.load(ASSETS_PATH + "bg_level.png").convert()

    def update(self):
        pygame.display.update()

    def draw(self):
        self.displaySurface.blit(self.bg_level, (0,0))

    def run(self):
        self.update()
        self.draw()