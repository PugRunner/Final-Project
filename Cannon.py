import pygame

class Cannon:

    def __init__(self, x, y, width, height, angle, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.angle = angle
        self.color = color

        self.rect = pygame.draw.line((x, y), (x+width, y+height))

    def display(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)