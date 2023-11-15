import pygame
import sys

#Initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600

#colors #use google = color picker for RGB tuples
BLUE = (0, 0, 255)
BROWN = (240, 215, 125)

#creat the screen # https://www.pygame.org/docs/ref/pygame.html
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Background with Sandy Brown Bottom")

#MAin Loop

running = True #set flag to True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #fill screen with blue
    screen.fill(BLUE)

    #add sandy bottom
    rectangle_height = 100
    pygame.draw.rect(screen, BROWN, (0, screen_height-rectangle_height, screen_width, rectangle_height))

    #update the display
    pygame.display.flip()

pygame.quit()