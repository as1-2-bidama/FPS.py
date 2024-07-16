import pygame
import math
from setting import *

class Draw:
    def __init__(self):
        self.screen = pygame.display.set_mode(screen)
        pygame.display.set_caption("FPM")
    def draw(self,vision_woll,player_pos,player_angle):
        self.screen.fill(color_list["white"])
        num = 0
        # print(vision_woll)
        # for i in vision_woll:
        #     if i[0] != True:
        #             pygame.draw.line(screen, color_list["black"], (((screen[0]/len(angle_list)) * num),300), (((screen[0]/len(angle_list)) * num),230-(50/i[1])*40),int((screen[0]/len(angle_list))))
        #             pygame.draw.line(screen, color_list["black"], (((screen[0]/len(angle_list)) * num),300), (((screen[0]/len(angle_list)) * num),370+(50/i[1])*40),int((screen[0]/len(angle_list))))
        #     num += 1
        player_dir = pygame.math.Vector2(math.cos(player_angle)*50+player_pos[1].x,math.sin(player_angle)*50+player_pos[1].y)
        pygame.draw.line(self.screen,color_list["blue"],(player_pos[1].x,player_pos[1].y),(player_dir),2)
        pygame.draw.circle(self.screen,color_list["red"],(player_pos[1]),5)
        print(player_pos[1])
        for i in range(len(woll_list)):
            pygame.draw.line(self.screen, color_list["black"], woll_list[i][0], woll_list[i][1], 10)
        pygame.display.update()