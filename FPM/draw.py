import pygame
import math
from setting import *

class Draw:
    def __init__(self):
        self.screen = pygame.display.set_mode(screen)
        pygame.display.set_caption("FPM")
    def draw(self,vision_woll,player_pos,player_angle,angle):
        self.screen.fill(color_list["blue"])
        num = 0
        for i in vision_woll:
            if i[0] == 1:
                pygame.draw.line(self.screen, color_list["gray"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 - 10)-(40/i[1])*20),int((screen[0]/len(angle_list))))
                pygame.draw.line(self.screen, color_list["gray"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 + 10)+(40/i[1])*20),int((screen[0]/len(angle_list))))
            elif i[0] != 1:
                pygame.draw.line(self.screen, color_list["black"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 - 10)-(40/i[1])*20),int((screen[0]/len(angle_list))))
                pygame.draw.line(self.screen, color_list["black"], (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),screen[1]/2), (((screen[0]/len(angle_list)) + num*screen[0]/len(angle_list)),(screen[1]/2 + 10)+(40/i[1])*20),int((screen[0]/len(angle_list))))
            num += 1
        player_dir = pygame.math.Vector2(math.cos(player_angle)*50+player_pos[1].x,math.sin(player_angle)*50+player_pos[1].y)
        for look_angle in angle_list:
            player_dir = pygame.math.Vector2(math.cos(angle+look_angle)*50+player_pos[1].x,math.sin(angle+look_angle)*50+player_pos[1].y)
            pygame.draw.line(self.screen,color_list["blue"],(player_pos[1].x,player_pos[1].y),(player_dir),2)
        pygame.draw.circle(self.screen,color_list["red"],(player_pos[1]),5)
        for i in range(len(woll_list)):
            pygame.draw.line(self.screen, color_list["black"], woll_list[i][0], woll_list[i][1], 1)
        pygame.display.update()