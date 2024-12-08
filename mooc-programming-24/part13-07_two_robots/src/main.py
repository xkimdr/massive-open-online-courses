# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x1 = 0
x2 = 0
v1 = 1
v2 = 2
xm = 640 - robot.get_width()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (x1, 100))
    window.blit(robot, (x2, 200))
    pygame.display.flip()

    x1 += v1
    x2 += v2

    if x1 == xm or v1 == -1 and x1 == 0:
        v1 = -v1
    if x2 == xm or v2 == -2 and x2 == 0:
        v2 = -v2

    clock.tick(60)
