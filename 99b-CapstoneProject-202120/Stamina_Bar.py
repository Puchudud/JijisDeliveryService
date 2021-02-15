import pygame
import sys
import time
import math

class Stamina:
    def __init__(self, screen, width, height, speed):
        self.screen = screen
        self.width = width
        self.height = height
        self.speed = speed
        self.BLACK = pygame.Color("Black")
        self.font1 = pygame.font.Font(None, 28)
        self.caption1 = self.font1.render("Stamina", True, self.BLACK)
        self.time = 0
        self.time_delayer = 0

    def draw(self):
        pygame.draw.rect(self.screen, (0, 204, 0), (40, 700, self.width, self.height))
        self.screen.blit(self.caption1, (45, 670))



    def drain(self):
        if self.time_delayer % 7 == 0:
            self.time = self.time + 1
            if self.time % 2 == 0:
                self.width = self.width - 1
        self.time_delayer = self.time_delayer + 1