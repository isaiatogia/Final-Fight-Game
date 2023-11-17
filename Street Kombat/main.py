import pygame

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Kombat") #name displayed atop game window

#load background image
bg_image = pygame.image.load("../Street Kombat/assets/images/background/The Pit II.png").convert_alpha()
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scale image to screen dimensions
    screen.blit(scaled_bg, (0, 0))

#game loop
run = True
while run:

    #draw background
    draw_bg()

    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

#exit pygame
pygame.quit()