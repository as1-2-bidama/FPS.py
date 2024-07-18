import pygame
from setting import *

class Title:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.image_title_txt = pygame.image.load("image/title_text.png")
        self.image_title_txt = pygame.transform.scale(self.image_title_txt,(screen_width/3*2,screen_height/3))
        pygame.mixer_music.load("Merrily_POP.mp3")
        pygame.mixer_music.play(-1)
        self.start_button_x = screen_width/10
        self.start_button_y = screen_height/10
        self.seen_num = 0
        self.run_bool = True
    def input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    x,y = pygame.mouse.get_pos()
                    if (((self.start_button_x*4)+self.start_button_x*2) > x) and (x > (self.start_button_x*4)) and ((self.start_button_y*7) < y) and (y < (self.start_button_y*7+self.start_button_y*2)):
                        self.seen_num = 1
                        pygame.mixer_music.pause()
                        print("a")
    def run(self):
        self.screen.fill(color_list["white"])
        self.screen.blit(self.image_title_txt, (screen_width/6,screen_height/10))
        pygame.draw.rect(self.screen,color_list["blue"],(self.start_button_x*4,self.start_button_y*7,self.start_button_x*2,self.start_button_y*2),0)
        self.input()
        return self.seen_num,self.run_bool