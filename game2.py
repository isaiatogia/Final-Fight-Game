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
    screen.blit(text, (screen_width/2-text.get_width()/2, screen_height/8-text.get_height()/2))

def draw_fishes(surf):
    #Load our fish tiles onto our surface
    green_fish = pygame.image.load("assets/sprites/green_fish.png").convert()
    orange_fish = pygame.image.load("assets/sprites/orange_fish.png").convert()
    puffer_fish = pygame.image.load("assets/sprites/puffer_fish.png").convert()

    #set colorkey
    green_fish.set_colorkey((0, 0, 0))
    orange_fish.set_colorkey((0, 0, 0))
    puffer_fish.set_colorkey((0, 0, 0))

    #distribute our green fish on the screen randomly
    for _ in range(5):
        x = random.randint(0, screen_width-tile_size)
        y = random.randint(0, screen_height-tile_size*2)
        surf.blit(green_fish, (x, y))

    # distribute our orange fish on the screen randomly
    for _ in range(4):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(0, screen_height - tile_size * 2)
        surf.blit(orange_fish, (x, y))

    # distribute our puffer fish on the screen randomly
    for _ in range(3):
        x = random.randint(0, screen_width - tile_size)
        y = random.randint(0, screen_height - tile_size * 2)
        surf.blit(puffer_fish, (x, y))

#Main loop
running = True
background = screen.copy()
draw_background(background) #draw background first
draw_fishes((background)) #draw fish on background

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
