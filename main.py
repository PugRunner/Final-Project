# imports
import pygame
import math
from Cannon import Cannon

# screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# colors
BACKGROUND_COLOR = (0, 0, 0)
CANNON_COLOR = (100, 100, 100)

# Frame update per second
FPS = 30

pygame.init()


# font
font = pygame.font.SysFont('arial', 22)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong by Duncan")

clock = pygame.time.Clock()


def main():
    running = True

    # (self, x, y, width, height, angle, color)
    cannon = Cannon(50, 500, 30, 45, CANNON_COLOR)

    while running:
        screen.fill(BACKGROUND_COLOR)

        (x,y) = pygame.mouse.get_pos()
        # math time to get degrees
        # radians = math.atan(y/x)
        radius = math.sqrt(x ** 2 + y ** 2)

        cos_radians = math.acos(x/radius)
        sin_radians = math.asin(y/radius)

        # things to display
        cannon.display(screen, cos_radians, sin_radians)

        pygame.display.update()
        clock.tick(FPS)

        # Event handleing: check for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



if __name__ == "__main__":
    main()
    pygame.quit()
