import pygame

class Cannon_Ball:
    
    def __init__(self, x, y, color, radius, screen):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius

        self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


    def display(self, screen):
        self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, screen, cannon_fired, x_speed, y_speed):
        after_cannon_fired = False

        if cannon_fired:
            if x_speed > 0:
                self.x = self.x + x_speed
            self.y = self.y + y_speed


            self.ball = pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


        if self.x >= 900 or self.y >= 600:
                after_cannon_fired = True
                return after_cannon_fired



    def getRect(self):
        ball_as_rect = pygame.Rect(self.ball)
        return ball_as_rect
