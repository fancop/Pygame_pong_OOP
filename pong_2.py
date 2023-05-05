from typing import Any
import pygame 
import sys
from random import randint

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Game:
    def __init__(self):
        pygame.init()
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        screen_info = pygame.display.Info()
        self.screen_width = screen_info.current_w
        self.screen_height = screen_info.current_h
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height),
            pygame.FULLSCREEN
        )
        self.rect = self.screen.get_rect()
        player_1 = Paddle(
            self.rect.width * 0.1,
            self.rect.centery,
            self.rect.width * 0.005,
            self.rect.height * 0.1,
            WHITE,
            pygame.K_w,
            pygame.K_s
        )
        player_2 = Paddle(
            self.rect.width * 0.9,
            self.rect.centery,
            self.rect.width * 0.005,
            self.rect.height * 0.1,
            WHITE,
            pygame.K_UP,
            pygame.K_DOWN
        )
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(player_1)
        self.all_sprites.add(player_2)

    def main_loop(self):
        game = True
        while game:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                game = False

            self.screen.fill((BLACK))
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()


class Paddle(pygame.sprite.Sprite):
    def __init__(
            self,
            center_x: int,
            center_y: int,
            width: int,
            height: int,
            color: tuple,
            key_up,
            key_down
    ):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((color))
        self.rect = self.image.get_rect()
        self.rect.centerx = center_x
        self.rect.centery = center_y
        self.key_up = key_up
        self.key_down = key_down
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.key_up]:
            self.rect.y -= 5
        elif keys[self.key_down]:
            self.rect.y += 5

game = Game()
game.main_loop()
pygame.quit()
sys.exit()