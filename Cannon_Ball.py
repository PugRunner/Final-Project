import pygame

class Cannon_Ball:
    
    def __init__(self, x, y, color, radius, x_speed, y_speed, dx, dy):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.dx = dx
        self.dy = dy


    def display(self, screen):
        self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, screen, cannon_fired):
        if cannon_fired:
            self.x = self.x + self.x_speed
            self.y = self.y + self.y_speed

            self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)