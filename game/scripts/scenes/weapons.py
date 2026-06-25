import pygame
import math
from game.config.cfg import COLOR_WEAPON


class BibleWeapon(pygame.sprite.Sprite):
    def __init__(self, index, total_books=1, rot_speed=0.05):
        super().__init__()
        self.image = pygame.Surface((20, 24))
        self.image.fill(COLOR_WEAPON)
        self.rect = self.image.get_rect()

        self.index = index
        self.total_books = total_books
        self.radius = 80.0
        self.rot_speed = rot_speed
        self.damage = 15
        self.recalculate_angle(index, total_books)

    def recalculate_angle(self, index, total_books):
        self.index = index
        self.total_books = total_books
        self.current_angle = (2 * math.pi / total_books) * index

    def update(self, player_rect):
        self.current_angle += self.rot_speed
        self.rect.centerx = player_rect.centerx + int(self.radius * math.cos(self.current_angle))
        self.rect.centery = player_rect.centery + int(self.radius * math.sin(self.current_angle))