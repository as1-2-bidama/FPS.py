import pygame
from setting import *

class Result:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.seen_num = 3
    def run(self):
        return self.seen_num