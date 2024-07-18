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
        pygame.mouse.set_visible(False)
        self.run_bool = True
        self.mode = 1
    def run(self):
        self.run_bool,key = self.input.input_key(self.run_bool)
        if self.mode == 1:
            self.mode = self.calculation.move(key,0,self.mode)
            self.draw.draw_title()
        elif self.mode == 2:
            mouse_dir = self.input.input_mouse()
            player_pos = self.calculation.move(key,mouse_dir,self.mode)
            self.mode = self.calculation.if_clear()
            vision_woll = self.calculation.vision(mouse_dir)
            self.draw.draw_game(vision_woll,player_pos)
        elif self.mode == 3:
            self.mode = self.calculation.move(key,0,self.mode)
            self.draw.draw_result()
        pygame.mouse.set_pos([screen[0]/2,screen[1]/2])
        return self.run_bool