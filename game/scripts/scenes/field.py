import pygame
import math
import random

from game.scripts.scenes.weapons import BibleWeapon
from game.scripts.scenes.player import Player
from game.scripts.entities.enemy import Enemy
from game.config.cfg import *
from game.scripts.entities.Exp import Exp


class Level:
    def __init__(self, display_surface):
        self.displaySurface = display_surface
        self.width = display_surface.get_width()
        self.height = display_surface.get_height()
        self.font = pygame.font.SysFont(None, 36)

        self.score = 0
        self.exp = 0
        self.num_books = 1
        self.bible_rot_speed = 0.05
        self.time_elapsed = 0.0

        self.player = Player(self.width, self.height)
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.enemy_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.Group()
        self.gem_group = pygame.sprite.Group()

        self.spawn_timer = 0
        self.spawn_cooldown = 45
        self.restart()

    def restart(self):
        self.score = 0
        self.exp = 0
        self.num_books = 1
        self.bible_rot_speed = 0.05
        self.spawn_timer = 0
        self.time_elapsed = 0.0

        self.player = Player(self.width, self.height)
        self.player_group = pygame.sprite.GroupSingle(self.player)
        self.enemy_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.Group()
        self.gem_group = pygame.sprite.Group()

        self.weapon_group.add(BibleWeapon(0, self.num_books, self.bible_rot_speed))

    def _spawn_enemies(self):
        self.spawn_timer += 1
        current_cooldown = max(15, self.spawn_cooldown - int(self.time_elapsed // 30) * 5)
        if self.spawn_timer >= current_cooldown:
            self.spawn_timer = 0
            angle = random.uniform(0, 2 * math.pi)
            spawn_radius = max(self.width, self.height) * 0.7
            spawn_world_x = self.player.world_x + spawn_radius * math.cos(angle)
            spawn_world_y = self.player.world_y + spawn_radius * math.sin(angle)
            self.enemy_group.add(Enemy(spawn_world_x, spawn_world_y))

    def _handle_collisions(self):
        hits = pygame.sprite.groupcollide(self.enemy_group, self.weapon_group, False, False)
        for enemy, weapons in hits.items():
            for weapon in weapons:
                enemy.hp -= weapon.damage
            if enemy.hp <= 0:
                self.gem_group.add(Exp(enemy.world_x, enemy.world_y))
                enemy.kill()
                self.score += 10

        gem_hits = pygame.sprite.spritecollide(self.player, self.gem_group, True)
        if gem_hits:
            self.exp += len(gem_hits)

        damage_hits = pygame.sprite.spritecollide(self.player, self.enemy_group, False)
        if damage_hits:
            self.player.hp -= len(damage_hits) * 0.5
            if self.player.hp <= 0:
                self.restart()

    def _draw_grid(self):
        grid_size = 64
        start_x = int(-self.player.world_x % grid_size)
        start_y = int(-self.player.world_y % grid_size)
        for x in range(start_x, self.width, grid_size):
            pygame.draw.line(self.displaySurface, COLOR_GRID, (x, 0), (x, self.height))
        for y in range(start_y, self.height, grid_size):
            pygame.draw.line(self.displaySurface, COLOR_GRID, (0, y), (self.width, y))

    def _draw_ui(self):
        pygame.draw.rect(self.displaySurface, (50, 50, 50), (0, 0, self.width, 15))
        exp_width = int((self.exp / 10) * self.width)
        pygame.draw.rect(self.displaySurface, COLOR_EXP, (0, 0, exp_width, 15))

        score_text = self.font.render(f"Счет: {self.score}", True, COLOR_TEXT)
        self.displaySurface.blit(score_text, (20, 30))

        minutes = int(self.time_elapsed) // 60
        seconds = int(self.time_elapsed) % 60
        time_string = f"{minutes:02d}:{seconds:02d}"
        time_text = self.font.render(time_string, True, COLOR_TEXT)
        time_rect = time_text.get_rect(center=(self.width // 2, 40))
        self.displaySurface.blit(time_text, time_rect)

        if self.player.hp > 0:
            bar_width = 40
            bar_height = 6
            bar_x = self.player.rect.centerx - (bar_width // 2)
            bar_y = self.player.rect.top - 12
            pygame.draw.rect(self.displaySurface, (200, 50, 50), (bar_x, bar_y, bar_width, bar_height))
            current_hp_width = int((max(0, self.player.hp) / 100) * bar_width)
            pygame.draw.rect(self.displaySurface, (50, 255, 50), (bar_x, bar_y, current_hp_width, bar_height))

    def apply_lvlup(self, choice):
        if choice == 1:
            self.num_books += 1
            self.weapon_group.empty()
            for i in range(self.num_books):
                self.weapon_group.add(BibleWeapon(i, self.num_books, self.bible_rot_speed))
        elif choice == 2:
            self.player.speed += self.player.speed * 0.10
        elif choice == 3:
            self.bible_rot_speed += self.bible_rot_speed * 0.10
            for weapon in self.weapon_group:
                weapon.rot_speed = self.bible_rot_speed

    def update(self):
        self.time_elapsed += 1 / 60

        self.player_group.update()
        self.weapon_group.update(self.player.rect)
        self.enemy_group.update(self.player.world_x, self.player.world_y, self.player.rect)
        self.gem_group.update(self.player.world_x, self.player.world_y, self.player.rect)

        self._spawn_enemies()
        self._handle_collisions()

        self.displaySurface.fill(COLOR_BG)
        self._draw_grid()

        self.gem_group.draw(self.displaySurface)
        self.enemy_group.draw(self.displaySurface)
        self.weapon_group.draw(self.displaySurface)
        self.player_group.draw(self.displaySurface)

        self._draw_ui()

        if self.exp >= 10:
            self.exp = 0
            return "LVLUP"
        return "GAME"