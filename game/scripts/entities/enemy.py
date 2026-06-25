import pygame
import math
from game.config.cfg import COLOR_ENEMY


class Enemy(pygame.sprite.Sprite):
    def __init__(self, world_x, world_y):
        super().__init__()
        self.image = pygame.Surface((24, 24), pygame.SRCALPHA)
        pygame.draw.rect(self.image, COLOR_ENEMY, (0, 0, 24, 24))
        self.rect = self.image.get_rect()

        self.world_x = float(world_x)
        self.world_y = float(world_y)
        self.speed = 2.0
        self.hp = 30

    def update(self, player_world_x, player_world_y, player_rect):
        dx = player_world_x - self.world_x
        dy = player_world_y - self.world_y
        distance = math.hypot(dx, dy)

        if distance > 0:
            self.world_x += (dx / distance) * self.speed
            self.world_y += (dy / distance) * self.speed

        self.rect.centerx = int(self.world_x - player_world_x + player_rect.centerx)
        self.rect.centery = int(self.world_y - player_world_y + player_rect.centery)