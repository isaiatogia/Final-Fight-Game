import pygame
import sys
import random

#import all our necessary files
from fish import Fish, fishes
from background import draw_background
from game_parameters import *
from player import Player

#Initialize pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Adding a player fish")

#clock object
clock = pygame.time.Clock() #allows us to set the frames per second

#Main loop
running = True
background = screen.copy()
draw_background(background)

#draw fish on the screen
for _ in range(10):
    fishes.add(Fish(random.randint(screen_width, screen_width * 2), random.randint(tile_size, screen_height - tile_size)))

#draw player fish
player = Player(screen_width/2, screen_height/2)

#load new font to keep score
score = 0
score_font = pygame.font.Font("../assets/fonts/28 Days Later.ttf", 48)

#load a sound to our game
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        #control our player fish with arrow kys
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("You pressed the key up key")
                player.move_up()
            if event.key == pygame.K_DOWN:
                print("You pressed the key down key")
                player.move_down()
            if event.key == pygame.K_RIGHT:
                print("You pressed the key right key")
                player.move_right()
            if event.key == pygame.K_LEFT:
                print("You pressed the key left key")
                player.move_left()

    #draw the background
    screen.blit(background, (0,0))

    #update fish position
    fishes.update()

    #update player fish
    player.update()

    #check for collisions between player and fish - use group collision method
    result = pygame.sprite.spritecollide(player, fishes, True)
    #print(result)
    if result: #if run into green fish
        pygame.mixer.Sound.play(chomp)
        score += len(result) #add one to the len of list
        # for x in result:
        #     score += 1
        #draw more green fish on the screen
        for _ in range(len(result)):
            fishes.add(Fish(random.randint(screen_width, screen_width * 2),
                            random.randint(tile_size, screen_height - tile_size)))

    #check if fish have left the screen
    for fish in fishes:  # loop through our fish in the sprite group
        if fish.rect.x < -fish.rect.width:
            fishes.remove(fish)
            fishes.add(Fish(random.randint(screen_width, screen_width + 50),
                            random.randint(tile_size, screen_height - tile_size)))


    # draw game objects
    fishes.draw(screen)
    player.draw(screen)

    text = score_font.render(f"{score}", True, (255, 29, 0))
    screen.blit(text, (screen_width - text.get_width()/2 - 15, 0))

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

pygame.quit()
sys.exit
