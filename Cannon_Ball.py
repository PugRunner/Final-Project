import pygame

class Cannon_Ball:
    
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius


    def display(self, screen):
        self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, screen, cannon_fired, x_speed, y_speed):
        if cannon_fired:
            if x_speed > 0:
                self.x = self.x + x_speed
            self.y = self.y + y_speed


            self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
