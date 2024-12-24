# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

cx = 320 - robot.get_width() / 2
cy = 240 - robot.get_height() / 2
r = 150
j = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))

    for i in range(0, 10):
        angle = i * math.pi / 5 + j
        x = cx + r * math.cos(angle)
        y = cy - r * math.sin(angle)
        window.blit(robot, (x, y))

    pygame.display.flip()

    j -= 0.01
    clock.tick(60)
