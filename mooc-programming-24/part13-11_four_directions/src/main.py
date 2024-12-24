# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 320 - robot.get_width()
y = 240 - robot.get_height()

keys = {"up": False, "down": False, "left": False, "right": False}

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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys["up"] = False
            if event.key == pygame.K_DOWN:
                keys["down"] = False
            if event.key == pygame.K_LEFT:
                keys["left"] = False
            if event.key == pygame.K_RIGHT:
                keys["right"] = False

    if keys["up"]:
        y -= 2
    if keys["down"]:
        y += 2
    if keys["left"]:
        x -= 2
    if keys["right"]:
        x += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
