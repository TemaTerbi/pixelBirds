import sys
import pygame
from pygame import *

# Create a const variables for game
WIDTH = 1000
HEIGHT = 500
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


# Function which init game and screen for game
def run():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pixel Birds")
    clock = pygame.time.Clock()
    screen.fill(BLUE)
    pygame.display.flip()

    # Cycle for game event
    game_running = True
    while game_running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == QUIT:
                return sys.exit()


run()
