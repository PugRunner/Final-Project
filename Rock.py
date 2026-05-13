import pygame
import random

class Rock:

    def __init__(self, min_x, max_x, min_y, max_y, width, height, color):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.width = width
        self.height = height
        self.color = color

        self.x = random.randint(min_x, max_x)
        self.y = random.randint(min_y, max_y) 

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def display(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)

    def getRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return self.rect

    def hit(self):
        rock_hit = True
        return rock_hit