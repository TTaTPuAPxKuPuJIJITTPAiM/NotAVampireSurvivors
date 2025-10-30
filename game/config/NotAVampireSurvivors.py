import pygame

from game.config.cfg import *
from game.scripts.scenes.mainMenu import MainMenu
from game.scripts.scenes.level import Level

pygame.init()

clock = pygame.time.Clock()

# Game window
displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Not A Vampire Survivors")

isGameRunning = True



mainMenu = MainMenu(displaySurface)
level = Level(displaySurface)

mainMenu.run()

button_rect = pygame.Rect(864, 880, 192, 64)

clock.tick(60)

while isGameRunning:






    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                level.run()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isGameRunning = False
                pygame.quit()
                exit()

    pygame.display.update()

