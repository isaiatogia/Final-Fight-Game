#a pygame sprite class for a player fish

import pygame
from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        #TODO: turn the fish in the opposite direction
        self.forward_image = pygame.image.load("../assets/sprites/orange_fish.png").convert()
        self.forward_image.set_colorkey((0, 0, 0))
        self.reverse_image = pygame.transform.flip(self.forward_image, True, False)
        self.image = self.forward_image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.y_speed = -1*PLAYER_SPEED

    def move_down(self):
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.x_speed = -1*PLAYER_SPEED
        self.image = self.reverse_image

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.forward_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        #TODO: need to check if player fish went off the screen
        self.x += self.x_speed
        self.y += self.y_speed
        if self.x > screen_width - tile_size:
            self.x = screen_width - tile_size
        if self.x < 0:
            self.x = 0
        if self.y > screen_height - 2*tile_size:
            self.y = screen_height - 2*tile_size
        if self.y < 0:
            self.y = 0
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, surf):
        surf.blit(self.image, self.rect)


