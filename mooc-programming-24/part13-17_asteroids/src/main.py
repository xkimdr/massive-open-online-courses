# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
rw = robot.get_width()
rh = robot.get_height()

xm = 640 - rw
ym = 480 - rh

x = randint(0, xm)
y = ym

clock = pygame.time.Clock()

left = False
right = False

c = 0

rock = pygame.image.load("rock.png")
rkw = rock.get_width()
rkh = rock.get_height()

rkym = 480 - rkh

rocks = [[randint(0, xm), (randint(-50, -2) * rkh)] for _ in range(0, 10)]

game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False

    if not game_over:

        if left:
            x -= 5
        if right:
            x += 5
        if x < 0:
            x = 0
        if x > xm:
            x = xm

        for l in rocks:
            l[1] += 1
            if ym - rkh <= l[1] <= rkym and x - rkw <= l[0] <= x + rw:
                c += 1
                l[0] = randint(0, xm)
                l[1] = randint(-50, -2) * rkh
            elif l[1] == rkym:
                game_over = True
                break

    window.fill((0, 0, 0))
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {c}", True, (255, 0, 0))
    window.blit(text, (xm - 80, 10))
    window.blit(robot, (x, y))
    for l in rocks:
        window.blit(rock, (l[0], l[1]))
    if game_over:
        gf = pygame.font.SysFont("Arial", 40)
        gt = gf.render(f"GAME OVER", True, (255, 0, 0))
        window.blit(gt, (320 - gt.get_width() / 2, 240 - gt.get_height() / 2))
    pygame.display.flip()

    clock.tick(60)
