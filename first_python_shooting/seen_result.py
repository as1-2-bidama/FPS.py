import pygame
from setting import *

class Result:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.seen_num = 3
        self.run_bool = True
    def run(self):
        self.screen.fill(color_list["white"])
        return self.seen_num,self.run_bool