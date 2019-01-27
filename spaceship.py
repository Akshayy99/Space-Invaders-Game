import pygame
import sys
import random
import time
from pygame.locals import *
from missile1 import *
from missile2 import *
from alien import *

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


class Spaceship():

    def __init__(self, gameDisplay):
        self.ship = pygame.image.load("shipp.png")
        self.ship = pygame.transform.scale(self.ship, (100, 100))

        self.rect = self.ship.get_rect()

        self.rect.bottom = gameDisplay.bottom
        self.rect.centerx = gameDisplay.centerx

        self.change_x = 0
        self.missil1 = []
        self.missil2 = []
        self.score = 0

    def display(self):
        gameDisplay.blit(self.ship, (self.posx, self.posy))

    def event_handler(self, event):
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                self.change_x = -block_size
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                self.change_x = block_size
            elif event.key == K_s:
                self.missil1.append(Missile1(self.rect.centerx, self.rect.top))
            elif event.key == K_SPACE:
                self.missil2.append(Missile2(self.rect.centerx, self.rect.top))

        elif event.type == pygame.KEYUP:
            if event.key in (K_RIGHT, K_d, K_LEFT, K_a):
                self.change_x = 0

    def update_event(self):

        self.rect.x += self.change_x
        if self.rect.x > dis_width - 100:
            self.rect.x = dis_width - 100
        if self.rect.x < 0:
            self.rect.x = 0

        for miss1 in self.missil1:
            miss1.update()

        for m in range(len(self.missil1) - 1, -1, -1):
            if not self.missil1[m].active:
                del self.missil1[m]

        for miss2 in self.missil2:
            miss2.update()

        for m in range(len(self.missil2) - 1, -1, -1):
            if not self.missil2[m].active:
                del self.missil2[m]

    def display(self, screen):
        screen.blit(self.ship, self.rect.topleft)

        for miss1 in self.missil1:
            miss1.draw(screen)
        for miss2 in self.missil2:
            miss2.draw(screen)

    def Missile1_collision(self, alien_list):
        for miss1 in self.missil1:
            for a in alien_list:
                end = time.time()
                if pygame.sprite.collide_circle(miss1, a):
                    miss1.active = False
                    a.life += 5
                    a.image = pygame.image.load("alien2.png")
                    a.image = pygame.transform.scale(a.image, (100, 100))

    def Missile2_collision(self, alien_list):
        global score
        for miss2 in self.missil2:
            for a in alien_list:
                end = time.time()
                if pygame.sprite.collide_circle(miss2, a):
                    miss2.active = False
                    a.active = 0
                    self.score += 1
