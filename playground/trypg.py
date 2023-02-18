import pygame, sys, random

from pygame.locals import *

pygame.init()

BACKGROUND_COLOR = (255, 255, 255)

FPS = 60
fpsClock = pygame.time.Clock()

WIN_WIDTH = 800
WIN_HEIGHT = 600

WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

pygame.display.set_caption('Abgame')


def run():
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        WINDOW.fill(BACKGROUND_COLOR)
        pygame.display.update()
        fpsClock.tick(FPS)

if __name__ == '__main__':
    run()
