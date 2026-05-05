import pygame
import math

class Cannon:

    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def display(self, screen, cos_radians, sin_radians):
        # make it look smoother, make it rotate in a circle
        x_length = math.cos(cos_radians)
        y_length = math.sin(sin_radians)
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x + x_length * 100, self.y + y_length * 100), width=40)
        
