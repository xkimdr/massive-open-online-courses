# WRITE YOUR SOLUTION HERE:


import pygame
from random import randint

pygame.init()

wx = 640
wy = 480
window = pygame.display.set_mode((wx, wy))

ball = pygame.image.load("ball.png")
bx = ball.get_width()
by = ball.get_height()

xm = wx - bx
ym = wy - by

vx = 2
vy = 2

x = randint(0, xm)
y = randint(0, ym)

angle = 1

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    x += vx
    y += vy

    if y >= ym or vy < 0 and y <= 0:
        vy = -vy
    if x >= xm or vx < 0 and x <= 0:
        vx = -vx

    clock.tick(60)
