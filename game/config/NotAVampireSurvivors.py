import pygame

from game.config.cfg import *
from game.scripts.scenes.mainMenu import MainMenu

pygame.init()
clock = pygame.time.Clock()

# Game window
displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Not A Vampire Survivors")

isGameRunning = True

mainMenu = MainMenu(displaySurface)

while isGameRunning:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False


    mainMenu.run()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()