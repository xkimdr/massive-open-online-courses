# WRITE YOUR SOLUTION HERE:

import pygame
import math
from datetime import datetime

pygame.init()

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    date = datetime.now()
    pygame.display.set_caption(date.strftime("%H:%M:%S"))
    pygame.draw.circle(window, (255, 0, 9), (320, 240), 200, 5)
    pygame.draw.circle(window, (255, 0, 9), (320, 240), 10)
    sa = date.second * math.pi / 30
    pygame.draw.line(
        window,
        (0, 0, 255),
        (320, 240),
        (320 + 180 * math.sin(sa), 240 - 180 * math.cos(sa)),
        1,
    )
    ma = date.minute * math.pi / 30
    pygame.draw.line(
        window,
        (0, 0, 255),
        (320, 240),
        (320 + 180 * math.sin(ma), 240 - 180 * math.cos(ma)),
        3,
    )
    ha = date.hour * math.pi / 6
    pygame.draw.line(
        window,
        (0, 0, 255),
        (320, 240),
        (320 + 180 * math.sin(ha), 240 - 180 * math.cos(ha)),
        5,
    )
    pygame.display.flip()

    clock.tick(60)
