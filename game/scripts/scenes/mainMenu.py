import pygame

from game.config.cfg import *

class MainMenu():
    def __init__(self, displaySurface):
        self.bgimage = pygame.image.load(ASSETS_PATH + "mainmenu.png").convert()
        # self.bgimage = pygame.transform.scale(self.bgimage,(WINDOW_WIDTH, WINDOW_WIDTH))

        self.displaySurface = displaySurface


    def update(self):
        pass

    def draw(self):
        self.displaySurface.blit(self.bgimage, (0, 0))

    def run(self):
        #self.update()
        self.draw()