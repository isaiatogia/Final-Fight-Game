# create a pygame sprite class for a fish

import pygame
import random

MIN_SPEED = 0.5
MAX_SPEED = 3

class Fish1(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image2 = pygame.image.load("../assets/sprites/puffer_fish.png").convert()
        self.image2.set_colorkey((0, 0, 0))
        self.image2 = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update(self):
        #update the x position of the fish
        self.x -= self.speed  # fish is moving left
        self.rect.x = self.x

    def draw(self, surf):
        surf.blit(self.image2, self.rect)


fishes = pygame.sprite.Group()