# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

ym = 480 - robot.get_height()
xm = 650 - robot.get_width()

clock = pygame.time.Clock()

pos = [[randint(0, xm), randint(-10000, -50), 0, 1] for _ in range(0, 100)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for t in pos:
        window.blit(robot, (t[0], t[1]))

    pygame.display.flip()

    for t in pos:
        t[0] += t[2]
        t[1] += t[3]

        if t[1] >= ym:
            t[3] = 0
            if t[0] < xm / 2:
                t[2] = -1
            else:
                t[2] = 1

    clock.tick(60)
