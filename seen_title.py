import pygame
from setting import *

class Title:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.image_title_txt = pygame.image.load("image/title_text.png")
        self.seen_num = 0
    def run(self):
        self.screen.fill(color_list["white"])
        self.screen.blit(self.image_title_txt, (0,0))
        return self.seen_num