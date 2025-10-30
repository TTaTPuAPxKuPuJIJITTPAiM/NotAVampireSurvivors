import pygame

from game.config.cfg import *

class MainMenu:
    def __init__(self, displaySurface):
        self.bgimage = pygame.image.load(ASSETS_PATH + "mainmenu.png").convert()

        self.button_play = pygame.image.load(ASSETS_PATH + "Play_button.png").convert()

        self.displaySurface = displaySurface


    def update(self):
        pygame.display.update()

    def draw(self):
        self.displaySurface.blit(self.bgimage, (0, 0))

        self.displaySurface.blit(self.button_play, (864, 880))

    def run(self):
        self.update()
        self.draw()