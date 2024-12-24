# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()


x = randint(0, 640 - rw)
y = randint(0, 480 - rh)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx = event.pos[0]
            my = event.pos[1]
            if x <= mx <= x + rw and y <= my <= y + rh:
                x = randint(0, 640 - rw)
                y = randint(0, 480 - rh)
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
