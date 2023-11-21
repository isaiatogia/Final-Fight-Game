# import modules
import pygame
from pygame import mixer


# initialize modules
pygame.init()
mixer.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game") # name displayed atop game window

# set framerate
clock = pygame.time.Clock()
FPS = 60

#define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# load music
pygame.mixer.music.load("../Fight Game OG/assets/audio/music.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

# load background image
bg_image = pygame.image.load("../My Game/assets/images/background/Forest.png").convert_alpha()

# load font
victory_font = pygame.font.Font("../My Game/assets/fonts/Canterbury.ttf", 100)
count_font = pygame.font.Font("../My Game/assets/fonts/Canterbury.ttf", 80)
score_font = pygame.font.Font("../My Game/assets/fonts/Canterbury.ttf", 30)

# load victory image
victory_1 = victory_font.render("Knight 1 Wins", True, (255, 0, 0))
victory_2 = victory_font.render("Knight 2 Wins", True, (255, 0, 0))

# function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT)) #scale image to screen dimensions
    screen.blit(scaled_bg, (0, 0))

# function for drawing fighter health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, BLACK, (x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, (x, y, 400, 30))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 30))

# game loop
run = True
while run:

    # limit FPS
    clock.tick(FPS)

    # draw background
    draw_bg()

    # draw text
    draw_text("Knight 1: ", score_font, RED, 20, 60)
    draw_text("Knight 2: ", score_font, RED, 580, 60)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # update display
    pygame.display.update()

# exit pygame
pygame.quit()