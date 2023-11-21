# import pygame module
import pygame

# initialize pygame module
pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game") # name displayed atop game window

# set framerate
clock = pygame.time.Clock()
FPS = 60

# load background image
bg_image = pygame.image.load("../My Game/assets/images/background/Forest.png").convert_alpha()

# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scale image to screen dimensions
    screen.blit(scaled_bg, (0, 0))

# game loop
run = True
while run:

    # limit FPS
    clock.tick(FPS)

    # draw background
    draw_bg()

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

# exit pygame
pygame.quit()