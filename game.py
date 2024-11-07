import pygame
import sys
from display_resolution import get_screen_infos, scaled_down
from constants import *

class Game:
    def __init__(self):
        pygame.init()

        self.screen_infos = get_screen_infos(DEVELOPMENT_RESOLUTION)
        self.screen = pygame.display.set_mode((self.screen_infos["width"], self.screen_infos["height"]), pygame.SCALED + pygame.FULLSCREEN + pygame.NOFRAME)
        pygame.display.set_caption("To Change")
        self.clock = pygame.time.Clock()
        self.ICON = None
        # pygame.display.set_icon(self.ICON)

    def main_menu(self):
        pass

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(FPS)


Game().run()