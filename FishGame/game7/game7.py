import pygame
import sys
import random

#import all our necessary files
from game_parameters import *
from fish import Fish, fishes
from enemy import enemies
from background import draw_background, add_fish, add_enemies
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
add_fish(10)

#draw enemies on the screen
add_enemies(5)

#draw player fish
player = Player(screen_width/2, screen_height/2)

#load new font to keep score
score = 0
score_font = pygame.font.Font("../assets/fonts/28 Days Later.ttf", 48)

#load a sound to our game
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")

#add alternate and game over
life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0, 0, 0))

#set the number of lives
lives = NUM_LIVES

while lives > 0:
    for event in pygame.event.get():
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

    #update enemy position
    enemies.update()

    #update player fish
    player.update()

    #check for collisions between player and fish - use group collision method
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result: #if run into green fish
        #play chomp sound
        pygame.mixer.Sound.play(chomp)
        score += len(result)
        #draw more green fish on the screen
        add_fish(len(result))

    #check if player collides with enemy fish
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        #play hurt sound
        pygame.mixer.Sound.play(hurt) #update to another sound
        #placeholder for losing lives
        lives -= len(result)
        #draw more enemy fish on the screen
        add_enemies(len(result))

    #check if any fish have left the screen
    for fish in fishes:  # loop through our fish in the sprite group
        if fish.rect.x < -fish.rect.width: #use the tile size
            fishes.remove(fish) #remove the fish from the sprite group
            add_fish(1)

    #check if any enemy left the screen
    for enemy in enemies:  # loop through our fish in the sprite group
        if enemy.rect.x < -enemy.rect.width: #use the tile size
            enemies.remove(enemy) #remove the fish from the sprite group
            add_enemies(1)

    # draw game objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    # color and location of score count
    text = score_font.render(f"{score}", True, (255, 29, 0))
    screen.blit(text, (screen_width-tile_size,0))

    #draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*tile_size, screen_height-tile_size))

    # update the display
    pygame.display.flip()

    # limit the frame rate
    clock.tick(60)

#create new background when game over
screen.blit(background, (0, 0))

#show game over message
message = score_font.render("GAME OVER", True, (0, 0, 0))
screen.blit(message, (screen_width/2 - message.get_width()/2, screen_height/2))

#show final score
score_text = score_font.render(f"Score: {score}", True, (0, 0, 0))
screen.blit(score_text, (screen_width/2 - score_text.get_width()/2, screen_height/2 +score_text.get_height()))

#update display
pygame.display.flip()

#play game over sound effect
pygame.mixer.Sound.play(bubbles)

#wait for user to exit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Quit game
            pygame.quit()
            sys.exit()

