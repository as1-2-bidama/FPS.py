import pygame
from draw import Draw
from input import Input
from allmath import Calculation
from setting import *

class Root:
    def __init__(self):
        pygame.init()
        self.draw = Draw()
        self.input = Input()
        self.calculation = Calculation()
        self.run_bool = True
    def run(self):
        self.run_bool,key = self.input.input_key(self.run_bool)
        mouse_dir = self.input.input_mouse()
        player_pos = self.calculation.move(key,mouse_dir)
        vision_woll = None #self.calculation.vision(mouse_dir)
        self.draw.draw(vision_woll,player_pos,mouse_dir)
        pygame.mouse.set_pos([screen[0]/2,screen[1]/2])
        return self.run_bool