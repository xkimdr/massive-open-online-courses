# WRITE YOUR SOLUTION HERE:

from random import choice
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")
height = robot.get_height()
width = robot.get_width()

for _ in range(1, 1001):
    window.blit(
        robot, (choice(range(0, 640 - width + 1)), choice(range(0, 480 - height + 1)))
    )

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
