import argparse
import os
import sys

import pygame as pg
from loguru import logger as log

os.environ["SDL_VIDEO_CENTERED"] = "1"


class App:
    def __init__(self):
        self.is_running = True
        self._display_surf = None
        self.size = self.weight, self.height = 1280, 1024

    def init(self):
        pg.init()
        self._display_surf = pg.display.set_mode(self.size, pg.HWSURFACE | pg.DOUBLEBUF)
        self.is_running = True

    def event(self, event):
        if event.type == pg.QUIT:
            self.is_running = False

    def loop(self):
        pass

    def render(self):
        pass

    def cleanup(self):
        pg.quit()

    def execute(self):
        if self.init() == False:
            self.is_running = False

        while self.is_running:
            for event in pg.event.get():
                self.event(event)
            self.loop()
            self.render()
        self.cleanup()

    pg.quit()


if __name__ == "__main__":
    theApp = App()
    theApp.execute()
