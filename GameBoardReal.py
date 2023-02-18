import pygame
import sys
from pygame.locals import *

# pygame:
# https://ryanstutorials.net/pygame-tutorial/pygame-shapes.php

class GameBoardReal():

    def __init__(self, gb_config):
        self.gbConfig = gb_config
        self.win = None
        self.fpsClock = pygame.time.Clock()

    def init(self):
        pygame.display.set_caption(self.gbConfig.title)
        self.win = pygame.display.set_mode((self.gbConfig.win_w, self.gbConfig.win_h))

    def start(self):

        # get into an endless loop
        done = False

        while not done:

            # handle events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            # call the updater to do some update
            if self.gbConfig.updater:
                self.gbConfig.updater.update(self.gbConfig.data)

            # re-render
            self.draw_backgroud()
            self.draw_foreground()

            pygame.display.update()
            # tick the timer for next iteration
            self.fpsClock.tick(self.gbConfig.fps)

    def draw_backgroud(self):
        self.win.fill(self.gbConfig.bg_color)

        # draw the horizontal line
        y = self.gbConfig.data.ground_y
        pygame.draw.line(self.win, self.gbConfig.data.BLACK, (0, y), (self.gbConfig.data.w, y), 3)

        # draw a tree
        x = self.gbConfig.data.w*0.8
        self.draw_tree(x)

    def draw_tree(self, x):
        # always start from ground_y
        y = self.gbConfig.data.ground_y
        x1 = x - 5
        x2 = x + 5
        y1  = y - 60
        # trunk
        pygame.draw.polygon(self.win, (0, 125, 0), ((x1, y), (x2, y), (x, y1)))
        # first layer
        y = y1 + 3
        x1 = x - 30
        x2 = x + 30
        y1 = y - 30
        pygame.draw.polygon(self.win, (0, 200, 0), ((x1, y), (x2, y), (x, y1)))
        # second layer
        y = y1 + 3
        x1 = x - 20
        x2 = x + 20
        y1 = y - 20
        pygame.draw.polygon(self.win, (0, 200, 0), ((x1, y), (x2, y), (x, y1)))

    def draw_foreground(self):
        y = self.gbConfig.data.vir_y
        x = self.gbConfig.data.vir_x
        r = self.gbConfig.data.vir_r
        pygame.draw.circle(self.win, (255,0,0), (x,y), r)