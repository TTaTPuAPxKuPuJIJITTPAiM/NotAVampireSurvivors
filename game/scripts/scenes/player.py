import pygame
from game.config.cfg import COLOR_PLAYER


class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((32, 32), pygame.SRCALPHA)
        pygame.draw.circle(self.image, COLOR_PLAYER, (16, 16), 16)
        self.rect = self.image.get_rect(center=(width // 2, height // 2))

        self.world_x = 0.0
        self.world_y = 0.0
        self.speed = 4.0
        self.hp = 100

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        dx, dy = 0.0, 0.0

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  dx -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: dx += 1
        if keys[pygame.K_w] or keys[pygame.K_UP]:    dy -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:  dy += 1

        if dx != 0 and dy != 0:
            dx *= 0.7071
            dy *= 0.7071

        self.world_x += dx * self.speed
        self.world_y += dy * self.speed