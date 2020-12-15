import os
import sys
from pathlib import Path

import pygame

pygame.init()

screen = pygame.display.set_mode(
    size=(640, 480)
)

ballPosition = pygame.Vector2(0, 0)
ballVector = pygame.Vector2(1, 1)

clock = pygame.time.Clock()
p = Path(__file__).parent / r'assets\images\email icon.png'
print('p=', p)
surf = pygame.image.load(str(p))
surf = pygame.transform.scale(surf, (50, 50))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 0, 0))

    ballPosition += ballVector

    if ballPosition.x < 0 or ballPosition.x > screen.get_width():
        ballVector.x *= -1
    if ballPosition.y < 0 or ballPosition.y > screen.get_height():
        ballVector.y *= -1

    screen.blit(
        surf,
        ballPosition,
    )

    pygame.display.flip()
    clock.tick(120)
