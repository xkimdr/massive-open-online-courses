# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

x = 0
y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0] - robot.get_width() / 2
            y = event.pos[1] - robot.get_height() / 2
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
