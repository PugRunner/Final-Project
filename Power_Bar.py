import pygame
import math

class Power_Bar:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

        self.rect = pygame.Rect(x, y, width, self.height)

    def display(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)

    def update(self, screen, x, y, power):
        if power:
            height = 600 - y
            self.rect = pygame.Rect(self.x, y, self.width, height)
            pygame.draw.rect(screen, 'orange', self.rect)

            return math.cbrt(600 - y) * 4