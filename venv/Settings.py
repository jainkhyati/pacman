import pygame
#colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0,0,0)

#directions
UP = pygame.math.Vector2(0, -1)
DOWN = pygame.math.Vector2(0, 1)

#coordinates (in pixels)
STARTPOS_X = 224
STARTPOS_Y = 400
WIDTH = 448
HEIGHT = 560

#velocities
VELOCITY = 0.06
#grid for clarity during coding - to be deleted later


#sizes
CELL_SIZE = 16 #since cells are 16*16

#notes
#1. we may have four different images of pacman
#   facing different sides according to the velocity.
#2. 