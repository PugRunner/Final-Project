import pygame
import random

class Target:

    def __init__(self, min_x, max_x, min_y, max_y, radius, color):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y
        self.color = color
        self.radius = radius

        self.x = random.randint(min_x, max_x)
        self.y = random.randint(min_y, max_y)

        

    def display(self, screen):
        self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def getRect(self):
        ball_as_rect = pygame.Rect(self.ball)
        return ball_as_rect
    def hit(self):
        self.horizontal_factor *= -1

    def rest(self): # put ball in middle of screen
        self.horizontal_factor *= -1
        self.x = self.max_x // 2
        self.y = self.max_y // 2