import pygame
from fighter import Fighter

pygame.init()

#create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Street Kombat") #name displayed atop game window

#set framerate
clock = pygame.time.Clock()
FPS = 60

#load background image
bg_image = pygame.image.load("../Street Kombat/assets/images/background/background.jpg").convert_alpha()

#functino for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scale image to screen dimensions
    screen.blit(scaled_bg, (0, 0))


#create two instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)

#game loop
run = True
while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #event handler #close game when clicking "x"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    #update display
    pygame.display.update()

#exit pygame
pygame.quit()