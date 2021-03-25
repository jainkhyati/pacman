import pygame
from Settings import *
import math
#from vector import Vector2

screen = pygame.display.set_mode((448, 560))
pacman_right = pygame.image.load('pacman_right.png')#image taken from http://www.free-extras.com/search/1/pacman+facing+left.htm

class Pacman(object):
    def __init__(self):
       self.position = pygame.math.Vector2(STARTPOS_X, STARTPOS_Y)
        #velocity stuff will go here
        #self.velocity =
       self.color = YELLOW
       self.pacman = pacman_right

    def update_pacman(self):
        #self.position += self.velocity
        screen.blit(pacman_right, self.position)
        



