import pygame
from setting import *

class Gamemode:
    def __init__(self):
        self.seen_num = 3
        self.run_bool = True
    def run(self):
        return self.seen_num,self.run_bool