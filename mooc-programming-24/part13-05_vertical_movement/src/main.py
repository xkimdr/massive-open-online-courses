# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

y = 0
v = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (0, y))
    pygame.display.flip()

    y += v
    if y == 480 - robot.get_height() or v == -1 and y == 0:
        v = -v
    clock.tick(60)
