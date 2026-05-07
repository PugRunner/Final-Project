# imports
import pygame
import math
from Cannon import Cannon
from Cannon_Ball import Cannon_Ball
from Power_Bar import Power_Bar
from Target import Target

# screen dimensions
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

# colors
BACKGROUND_COLOR = (0, 0, 0)
CANNON_COLOR = (100, 100, 100)
CANNON_X = 50
CANNON_Y = 500

# Frame update per second
FPS = 30

# Cannon Ball stuff
CANNON_BALL_COLOR = (255, 255, 255) 
CANNON_BALL_RADIUS = 7
CANNON_BALL_DX = 0.01
CANNON_BALL_DY = 0.15

# Power Bar stuff
POWER_BAR_WIDTH = 30
POWER_BAR_HEIGHT = 80
POWER_BAR_COLOR = (255, 255, 255) 

# target stuff
TARGET_COLOR = 'red'
TARGET_RADIUS = 20

SCORE_COLOR = (255, 255, 0)

pygame.init()


# font
font = pygame.font.SysFont('arial', 22)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong by Duncan")

clock = pygame.time.Clock()


def main():
    running = True
    cannon_fired = False

    x_speed = 3
    y_speed = -2

    power = False
    r_x = 0
    r_y = 0

    y_speed_factor = 15
    x_speed_factor = 0

    points = 0
    scored = False

    cannon_fired = False

    mistake = 0

    # (self, x, y, width, height, angle, color)
    cannon = Cannon(CANNON_X, CANNON_Y, 30, 45, CANNON_COLOR)

    # (self, x, y, color, radius, dx, dy)
    cannon_ball = Cannon_Ball(CANNON_X, CANNON_Y, CANNON_BALL_COLOR, CANNON_BALL_RADIUS, screen)

    # (self, x, y, width, height, color):
    power_bar = Power_Bar(10, SCREEN_HEIGHT - POWER_BAR_HEIGHT, POWER_BAR_WIDTH, POWER_BAR_HEIGHT, POWER_BAR_COLOR)

    # self, min_x, max_x, min_y, max_y, radius, color, point
    target = Target(200, SCREEN_WIDTH, 200, SCREEN_HEIGHT, TARGET_RADIUS, TARGET_COLOR, points, screen)

    while running:
        screen.fill(BACKGROUND_COLOR)

        score_text = f"{points}"
        score_surface = font.render(score_text, True, SCORE_COLOR)
        screen.blit(score_surface, (SCREEN_WIDTH // 2, 20))


        (x,y) = pygame.mouse.get_pos()
        # math time to get radians
        # need this weird y stuff to put it in right quadrant, before it was in 4 now in 1; i think
        y = SCREEN_HEIGHT - y
        y *= -1

        radius = math.sqrt(x ** 2 + y ** 2)

        cos_radians = math.acos(x/radius)
        sin_radians = math.asin(y/radius)

        # things to display
        cannon.display(screen, cos_radians, sin_radians)
        cannon_ball.display(screen)
        power_bar.display(screen)
        target.display(screen)
        

        after_cannon_fired = cannon_ball.update(screen, cannon_fired, x_speed, y_speed)
        if cannon_fired:
            x_speed = x_speed - CANNON_BALL_DX
            y_speed = y_speed + CANNON_BALL_DY

        if after_cannon_fired == True:
            x_speed = 0
            y_speed = 0
            cannon_ball = Cannon_Ball(CANNON_X, CANNON_Y, CANNON_BALL_COLOR, CANNON_BALL_RADIUS, screen)
            mistake += 1
            cannon_fired = False




        # Event handleing: check for all events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN and cannon_fired == False:
                if event.button == 1: # 1 is the Left Mouse Button
                    cannon_fired = True
                    y_speed = sin_radians * y_speed_factor
                    x_speed = (1-cos_radians) * x_speed_factor

                if event.button == 3: # 3 is right mouse 
                    (r_x,r_y) = pygame.mouse.get_pos()
                    power = True

                    x_speed_factor = power_bar.update(screen, r_x, r_y, power)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    cannon = Cannon(CANNON_X, CANNON_Y, 30, 45, CANNON_COLOR)
                    cannon_ball = Cannon_Ball(CANNON_X, CANNON_Y, CANNON_BALL_COLOR, CANNON_BALL_RADIUS, screen)
                    power_bar = Power_Bar(10, SCREEN_HEIGHT - POWER_BAR_HEIGHT, POWER_BAR_WIDTH, POWER_BAR_HEIGHT, POWER_BAR_COLOR)
                    target = Target(200, SCREEN_WIDTH, 200, SCREEN_HEIGHT, TARGET_RADIUS, TARGET_COLOR, 0, screen)

                    cannon_fired = False
                    power = False
                    x_speed = 0
                    y_speed = 0
                

        if (pygame.Rect.colliderect(target.getRect(), cannon_ball.getRect())):
                scored = target.hit()

        if scored:
                points += 1
                scored = False
                mistake = 0

        if mistake == 4: # need to do 1 more than intended due to cannon ball going through target
             points = 0


        pygame.display.update()
        clock.tick(FPS)



if __name__ == "__main__":
    main()
    pygame.quit()
