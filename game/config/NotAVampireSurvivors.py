import pygame

from game.config.cfg import *
from game.scripts.scenes.mainMenu import MainMenu

pygame.init()
clock = pygame.time.Clock()

# Game window
displaySurface = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Not A Vampire Survivors")

isGameRunning = True

mainMenu = MainMenu(displaySurface)

clock.tick(60)

while isGameRunning:
    mainMenu.run()


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False

pygame.quit()