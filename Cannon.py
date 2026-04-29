import pygame
import math

class Cannon:

    def __init__(self, x, y, width, height, angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.color = color

    def display(self, screen):
        x_length = math.cos(math.radians(self.angle))
        y_length = math.sin(math.radians(self.angle))
        print(x_length)
        print(y_length)
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + x_length * 100, self.y - y_length * 100), width=40)