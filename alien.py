import pygame
import sys
import random
import time
from pygame.locals import *
from spaceship import *
from missile1 import *
from missile2 import *

clock = pygame.time.Clock()
begin = time.time()

dis_width = 800
dis_height = 800
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 155, 0)
FPS = 60

block_size = 15
score = 0


class Alien():

    def __init__(self, x, y, start):
        self.image = pygame.image.load("alien1.png")
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.active = True
        self.time = 1
        self.life = 8
        self.start = start

    def draw(self, display):
        display.blit(self.image, self.rect.topleft)

    def life(self):
        self.time += 1

    def time(self):
        return self.time / 60
