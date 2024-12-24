# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()

for i in range(1, 11):
    window.blit(robot, (10 + width * i, 100))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
