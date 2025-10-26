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

button_surface = pygame.Surface((192, 64))
font = pygame.font.Font(None, 24)
text = font.render("Play", True, (0, 0, 0))
text_rect = text.get_rect(center=(button_surface.get_width() // 2, button_surface.get_height() / 2))
button_rect = pygame.Rect(864, 880, 192, 64)

while isGameRunning:
    mainMenu.run()

    button_surface.blit(text, text_rect)

    displaySurface.blit(button_surface, (button_rect.x, button_rect.y))





    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                print("Button clicked!")

    pygame.display.update()


pygame.quit()