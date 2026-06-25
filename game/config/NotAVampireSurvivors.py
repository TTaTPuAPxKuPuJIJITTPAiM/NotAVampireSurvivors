import pygame
import sys

from game.config.cfg import *
from game.scripts.scenes.mainMenu import MainMenu
from game.scripts.scenes.field import Level

pygame.init()

displaySurface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Not A Vampire Survivors")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

isGameRunning = True

mainMenu = MainMenu(displaySurface)
level = Level(displaySurface)

current_state = "MENU"
button_rect = pygame.Rect(864, 880, 192, 64)

upgrade_buttons = [
    {"rect": pygame.Rect(WINDOW_WIDTH // 2 - 275, 200, 550, 60), "text": "1. +1 библия", "id": 1},
    {"rect": pygame.Rect(WINDOW_WIDTH // 2 - 275, 300, 550, 60), "text": "2. +10% к скорости передвижения", "id": 2},
    {"rect": pygame.Rect(WINDOW_WIDTH // 2 - 275, 400, 550, 60), "text": "3. +10% к свкорость заклинания", "id": 3}
]


while isGameRunning:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isGameRunning = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_state == "MENU" and button_rect.collidepoint(event.pos):
                level.restart()
                current_state = "GAME"
            elif current_state == "LVLUP":
                for btn in upgrade_buttons:
                    if btn["rect"].collidepoint(event.pos):
                        level.apply_lvlup(btn["id"])
                        current_state = "GAME"
                        break

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if current_state == "GAME":
                    current_state = "MENU"
                else:
                    isGameRunning = False

    if current_state == "MENU":
        mainMenu.run()
    elif current_state == "GAME":
        status = level.update()
        if status == "LVLUP":
            current_state = "LVLUP"
    elif current_state == "LVLUP":
        overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        displaySurface.blit(overlay, (0, 0))

        title = font.render("Уровень повышен! Выберите усиление:", True, (255, 255, 255))
        displaySurface.blit(title, (WINDOW_WIDTH // 2 - 220, 120))

        for btn in upgrade_buttons:
            pygame.draw.rect(displaySurface, (50, 50, 50), btn["rect"])
            pygame.draw.rect(displaySurface, (255, 215, 0), btn["rect"], 2)
            btn_text = font.render(btn["text"], True, (255, 255, 255))
            displaySurface.blit(btn_text, (btn["rect"].x + 20, btn["rect"].y + 15))

    pygame.display.update()

pygame.quit()
sys.exit()