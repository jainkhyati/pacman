import pygame
from Settings import *
import math
#from vector import Vector2

screen = pygame.display.set_mode((448, 560))

#loading images of pacman
pacman_right = pygame.image.load('pacman_right.png')#images taken from http://www.free-extras.com/search/1/pacman+facing+left.htm
pacman_left = pygame.image.load('pacman_left.png')
pacman_down = pygame.image.load('pacman_down.png')
pacman_up = pygame.image.load('pacman_up.png')


class Pacman(object):
    def __init__(self):
       self.position = pygame.math.Vector2(STARTPOS_X, STARTPOS_Y)
        #velocity stuff will go here
       self.velocity = pygame.math.Vector2(-VELOCITY, 0)
       self.color = YELLOW
       self.pacman = pacman_left


    def update_pacman(self):
        self.position += self.velocity
        screen.blit(self.pacman, self.position)


    def wants_left(self):
        self.pacman = pacman_left
        self.velocity = pygame.math.Vector2(-VELOCITY, 0)


    def wants_right(self):
        self.pacman = pacman_right
        self.velocity = pygame.math.Vector2(VELOCITY, 0)


    def wants_down(self):
        self.pacman = pacman_down
        self.velocity = pygame.math.Vector2(0, VELOCITY)


    def wants_up(self):
        self.pacman = pacman_up
        self.velocity = pygame.math.Vector2(0, -VELOCITY)



        



