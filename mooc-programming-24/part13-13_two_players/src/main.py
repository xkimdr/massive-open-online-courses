# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x1 = 100
y1 = 100

x2 = 300
y2 = 300


xm = 640 - robot.get_width()
ym = 480 - robot.get_height()

keys = {
    "up": False,
    "down": False,
    "left": False,
    "right": False,
    "w": False,
    "s": False,
    "a": False,
    "d": False,
}

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys["up"] = True
            if event.key == pygame.K_DOWN:
                keys["down"] = True
            if event.key == pygame.K_LEFT:
                keys["left"] = True
            if event.key == pygame.K_RIGHT:
                keys["right"] = True
            if event.key == pygame.K_w:
                keys["w"] = True
            if event.key == pygame.K_s:
                keys["s"] = True
            if event.key == pygame.K_a:
                keys["a"] = True
            if event.key == pygame.K_d:
                keys["d"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys["up"] = False
            if event.key == pygame.K_DOWN:
                keys["down"] = False
            if event.key == pygame.K_LEFT:
                keys["left"] = False
            if event.key == pygame.K_RIGHT:
                keys["right"] = False
            if event.key == pygame.K_w:
                keys["w"] = False
            if event.key == pygame.K_s:
                keys["s"] = False
            if event.key == pygame.K_a:
                keys["a"] = False
            if event.key == pygame.K_d:
                keys["d"] = False

    if keys["up"]:
        y2 -= 2
    if keys["down"]:
        y2 += 2
    if keys["left"]:
        x2 -= 2
    if keys["right"]:
        x2 += 2

    if x2 < 0:
        x2 = 0
    elif x2 > xm:
        x2 = xm

    if y2 < 0:
        y2 = 0
    elif y2 > ym:
        y2 = ym

    if keys["w"]:
        y1 -= 2
    if keys["s"]:
        y1 += 2
    if keys["a"]:
        x1 -= 2
    if keys["d"]:
        x1 += 2

    if x1 < 0:
        x1 = 0
    elif x1 > xm:
        x1 = xm

    if y1 < 0:
        y1 = 0
    elif y1 > ym:
        y1 = ym

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)
