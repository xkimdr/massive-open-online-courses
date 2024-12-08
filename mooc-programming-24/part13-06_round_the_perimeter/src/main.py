# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
xm = 640 - robot.get_width()
ym = 480 - robot.get_height()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    if y == 0 and x < xm:
        x += 1
    elif y < ym and x == xm:
        y += 1
    elif y == ym and x > 0:
        x -= 1
    elif y > 0 and x == 0:
        y -= 1
    clock.tick(60)
