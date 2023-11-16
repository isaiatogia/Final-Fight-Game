import pygame

class Fighter():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))

    def move(self):
        SPEED = 10
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        #movement
        if key[pygame.K_a]:
            dx = -SPEED
        if key[pygame.K_d]:
            dx = SPEED

        #update player position
        self.rect.x += dx
        self.rect.x += dy

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)