import pygame
import math
from game.config.cfg import COLOR_EXP

class Exp(pygame.sprite.Sprite):
    def __init__(self, world_x, world_y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(COLOR_EXP)
        self.rect = self.image.get_rect()
        self.world_x = world_x
        self.world_y = world_y

    def update(self, player_world_x, player_world_y, player_rect):
        dx = player_world_x - self.world_x
        dy = player_world_y - self.world_y
        distance = math.hypot(dx, dy)

        if distance < 100:
            self.world_x += (dx / distance) * 5.0
            self.world_y += (dy / distance) * 5.0

        self.rect.centerx = int(self.world_x - player_world_x + player_rect.centerx)
        self.rect.centery = int(self.world_y - player_world_y + player_rect.centery)