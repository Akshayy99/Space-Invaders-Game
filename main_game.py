import pygame
import sys
import random
import time
from pygame.locals import *
from spaceship import *
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
score = 0


class Game_SPACE_INVADERS():

    def __init__(self):
        pygame.init()
        dis_width = 800
        dis_height = 800
        self.gameDisplay = pygame.display.set_mode([dis_width, dis_height])
        pygame.mouse.set_visible(0)
        pygame.display.set_caption('Space Invaders')

        self.spaceship = Spaceship(self.gameDisplay.get_rect())

        self.aliens = []

        xpos = random.randint(1, 7) * 100
        ypos = random.randint(1, 2) * 100
        start = time.time()
        self.aliens.append(Alien(xpos, ypos, start))

    def gameLoop(self):
        global begin
        gameExit = False

        while not gameExit:
            clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        gameExit = True
                self.spaceship.event_handler(event)

            self.spaceship.update_event()

            self.spaceship.Missile1_collision(self.aliens)

            for i in range(len(self.aliens)-1, -1, -1):
                if not self.aliens[i].active:
                    del self.aliens[i]

            self.spaceship.Missile2_collision(self.aliens)

            for i in range(len(self.aliens)-1, -1, -1):
                end = time.time()
                if not self.aliens[i].active:
                    del self.aliens[i]
                elif end - self.aliens[i].start > self.aliens[i].life:
                    del self.aliens[i]

            self.gameDisplay.fill((white))
            self.spaceship.display(self.gameDisplay)

            end = time.time()
            if end - begin > 10:
                xpos = random.randint(1, 7) * 100
                ypos = random.randint(1, 2) * 100
                start = time.time()
                self.aliens.append(Alien(xpos, ypos, start))
                begin = time.time()

            for alien in self.aliens:
                alien.draw(self.gameDisplay)

            pygame.display.update()

            # display score
            text = 'Score: ' + str(self.spaceship.score)
            font = pygame.font.SysFont('arial', 30)
            text = font.render(text, True, black)
            self.gameDisplay.blit(text, (20, 20))

            pygame.display.update()

        pygame.quit()

Game_SPACE_INVADERS().gameLoop()
