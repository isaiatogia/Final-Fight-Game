import pygame
import sys

from game_parameters import *
from background import draw_background #import draw background function

#initialize pygame
pygame.init()

#creat the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Learning to get event types")

#Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("You pressed the key up key")
            if event.key == pygame.K_DOWN:
                print("You pressed the key down key")


    # draw the background
    screen.blit(background, (0,0))

    # update the display
    pygame.display.flip()

pygame.quit()
sys.exit
