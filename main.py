#import pygame
#import math
#from vector import Vector2
#from Settings import *
from pacman import *
#import random

# initialize
pygame.init()

# create screen
screen = pygame.display.set_mode((448, 560))
# for background image - creating variable to store img
background = pygame.image.load('background.png') #image taken from https://www.codeproject.com/Articles/520783/Pacman-Multiplayer

# title and icon
pygame.display.set_caption("Pac Man")
icon = pygame.image.load('pacmanicon.png')
pygame.display.set_icon(icon)

#create player
player = Pacman()

#game loop
running = True
while running:
    screen.fill(BLACK)
    #background image
    screen.blit(background, (0, 32))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # other events - keystrokes fall here
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.wants_left()
            elif event.key == pygame.K_RIGHT:
                player.wants_right()
            elif event.key == pygame.K_DOWN:
                player.wants_down()
            elif event.key == pygame.K_UP:
                player.wants_up()

    player.update_pacman()
    pygame.display.update()


pygame.quit()