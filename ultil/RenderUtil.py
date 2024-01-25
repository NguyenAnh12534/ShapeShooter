import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

SCREEN = pygame.display.set_mode((300, 300));

# Define FPS
FPS = 60

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def handleExitEvent():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

def render():
    handleExitEvent()
    SCREEN.fill(BLACK)
    pygame.display.update()
    clock.tick(FPS)