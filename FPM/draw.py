import pygame
import math
from setting import *
import time

class Draw:
    def __init__(self):
        self.screen = pygame.display.set_mode(screen,pygame.FULLSCREEN)
        pygame.display.set_caption("FPM")
        self.start_time = time.time()
        self.time = time.time()
        self.font2 = pygame.font.Font("font/NikkyouSans-mLKax.ttf", 60)
        self.clear_text = self.font2.render("Clear!",True,(255,255,255))
        self.title_text1 = self.font2.render("[780,660]をめざせ！FPS迷路",True,(255,255,255))
        self.title_text2 = self.font2.render("Enterでスタート",True,(255,255,255))
        self.title_text3 = self.font2.render("WASDで移動 ←→で視点操作",True,(255,255,255))
        self.clear_rect = self.clear_text.get_rect(center = (screen[0]/2,screen[1]/2))
        self.title_text1_rect = self.title_text1.get_rect(center = (screen[0]/2,screen[1]/2 - 20))
        self.title_text2_rect = self.title_text2.get_rect(center = (screen[0]/2,screen[1]/2 + 40))
        self.title_text3_rect = self.title_text3.get_rect(center = (screen[0]/2,screen[1]/2 + 100))
    def draw_game(self,vision_woll,player_pos):
        self.time = time.time()
        time_text = self.font2.render(str(int(self.time - self.start_time)),True,(255,255,255))
        pos_text = self.font2.render(str(player_pos),True,(255,255,255))
        time_rect = time_text.get_rect(center = (screen[0]/2,80))
        pos_rect = pos_text.get_rect(center = (screen[0]/2,screen[1]-100))
        self.screen.fill(color_list["blue"])
        num = 0
        for i in vision_woll:
            if i[0] == 1:
                pygame.draw.line(self.screen, color_list["gray"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 - 10)-(100/i[1])*30),int((screen[0]/len(angle_list))))
                pygame.draw.line(self.screen, color_list["gray"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 + 10)+(100/i[1])*30),int((screen[0]/len(angle_list))))
            elif i[0] != 1:
                pygame.draw.line(self.screen, color_list["black"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 - 10)-(100/i[1])*30),int((screen[0]/len(angle_list))))
                pygame.draw.line(self.screen, color_list["black"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 + 10)+(100/i[1])*30),int((screen[0]/len(angle_list))))
            num += 1
        self.screen.blit(time_text,time_rect)
        self.screen.blit(pos_text,pos_rect)
        pygame.display.update()
    def draw_title(self):
        self.screen.fill(color_list["blue"])
        self.screen.blit(self.title_text1,self.title_text1_rect)
        self.screen.blit(self.title_text2,self.title_text2_rect)
        self.screen.blit(self.title_text3,self.title_text3_rect)
        self.start_time = time.time()
        pygame.display.update()
    def draw_result(self):
        self.screen.fill(color_list["blue"])
        self.screen.blit(self.clear_text,self.clear_rect)
        self.clear_time = self.font2.render(str(int(self.time - self.start_time))+ "秒でクリアしました！",True,(255,255,255))
        self.clear_time_rect = self.clear_time.get_rect(center = (screen[0]/2,screen[1]/2 + 60))
        self.screen.blit(self.clear_time,self.clear_time_rect)
        pygame.display.update()