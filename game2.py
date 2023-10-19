import pygame
import sys
import random

#Initialize pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

#creat the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Using blit to draw tiles")

#Load Game Font
custom_font = pygame.font.Font("assets/fonts/28 Days Later.ttf", 128)

def draw_background(screen):
    #Load our tiles from the assets folder
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()

    #make PNGs transparent
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    #fill the screen with water
    for x in range(0, screen_width, tile_size):
        for y in range(0, screen_height, tile_size):
            screen.blit(water, (x,y))

    #draw a sandy bottom
    for x in range(0, screen_width, tile_size):
        screen.blit(sand, (x, screen_height-tile_size))

    #place the seagrass randomly along the bottom
    for _ in range(7):
        x = random.randint(0, screen_width)
        screen.blit(seagrass, (x, screen_height-tile_size*2+10))

    #draw the text
    text = custom_font.render("Chomp", True, (255, 29, 0))
    screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/2-text.get_height()/2))

#Main loop
running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #draw the background
    screen.blit(background, (0,0))

    # update the display
    pygame.display.flip()

#quite pygame
pygame.quit()
