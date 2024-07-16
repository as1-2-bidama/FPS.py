import pygame
import math
import copy
from setting import *

class Calculation:
    def __init__(self):        
        self.vision_woll_ = []
        for i in range(len(angle_list)):
            self.vision_woll_.append([None])
        self.player_pos = pygame.math.Vector2(150,150)
        self.before_pos = self.player_pos
    def vision(self,angle):
        vision_woll = copy.deepcopy(self.vision_woll_)
        for look_angle in angle_list: #視点の線分と交点、3Dviewを描写
            for woll_num in range(len(woll_list)):
                self.player_dir = pygame.math.Vector2(math.cos(angle+look_angle)*50+self.player_pos.x,math.sin(angle+look_angle)*50+self.player_pos.y)
                hitpos = self.intersection(woll_num,"vision")
                if hitpos != None:
                    long = self.measure_long(hitpos)
                    if vision_woll[angle_list.index(look_angle)][0] != None:
                        if vision_woll[angle_list.index(look_angle)][1] > long:
                            vision_woll[angle_list.index(look_angle)] = [1,long]
                    else:
                        vision_woll[angle_list.index(look_angle)] = [1,long]
            if vision_woll[angle_list.index(look_angle)][0] == None:
                if angle_list.index(look_angle) == 0:
                    vision_woll[angle_list.index(look_angle)] = [None,50]
                else:
                    vision_woll[angle_list.index(look_angle)] = [None,vision_woll[angle_list.index(look_angle) - 1][1]]
        return vision_woll
    def move(self,key,angle):
        self.before_pos = self.player_pos
        if "d" in key:
            self.player_pos = pygame.math.Vector2(math.cos(angle+1.6)+self.player_pos.x,math.sin(angle+1.6)+self.player_pos.y)
        if "a" in key:
            self.player_pos = pygame.math.Vector2(math.cos(angle+1.6)*-1+self.player_pos.x,math.sin(angle+1.6)*-1+self.player_pos.y)
        if "w" in key:
            self.player_pos = pygame.math.Vector2(math.cos(angle)*1+self.player_pos.x,math.sin(angle)*1+self.player_pos.y)
        if "s" in key:
            self.player_pos = pygame.math.Vector2(math.cos(angle)*-1+self.player_pos.x,math.sin(angle)*-1+self.player_pos.y)
        for woll_num in range(len(woll_list)):
            can = self.intersection(woll_num,"can_move")
            if can != None:
                self.player_pos = copy.deepcopy(self.before_pos)
                break
        return angle,self.player_pos
    def intersection(self,woll_num,mode):
        if mode == "can_move":
            r1_way = self.before_pos
        elif mode == "vision":
            r1_way = self.player_dir
        r1_pos = self.player_pos
        r2_way = woll_list[woll_num][1]
        r2_pos = woll_list[woll_num][0]
        if (r1_way.x - r1_pos.x) == 0:
            a1 = float('inf')
            b1 = float('inf')
        else:
            a1 = (r1_way.y - r1_pos.y) / (r1_way.x - r1_pos.x)#視線の傾き
        if (r2_way[0] - r2_pos[0]) == 0:
            a2 = float('inf')
            b2 = float('inf')
        else:
            a2 = (r2_way[1] - r2_pos[1]) / (r2_way[0] - r2_pos[0])#壁の傾き
        b1 = r1_way.y - a1*r1_way.x
        b2 = r2_way[1] - a2*r2_way[0]
        if (a2 - a1) == 0:
            return None
        else:
            if a1 == float('inf') or a2 == float('inf'):
                x = r1_pos.x
            else: 
                x = (b2 - b1) / (a1 - a2)
            y = a1 * x + b1
            hitpos = pygame.math.Vector2(x,y)
            if hitpos.x > min(r1_way.x,r1_pos.x) and hitpos.x < max(r1_way.x,r1_pos.x) and hitpos.x > min(r2_way[0],r2_pos[0]) and hitpos.x < max(r2_pos[0],r2_way[0]):
                return hitpos
            else:
                return None
        # if mode == "can_move":
        #     r1_way = self.before_pos
        # elif mode == "vision":
        #     r1_way = self.player_dir
        # if r1_way.x == self.player_pos.x:
        #     a1 = float('inf')
        #     b1 = 0
        # else:
        #     a1 = (r1_way.y - self.player_pos.y) / (r1_way.x - self.player_pos.x)#視線の傾き
        #     b1 = r1_way.y - a1*r1_way.x
        # if woll_list[woll_num][1][0] == woll_list[woll_num][0][0]:
        #     a2 = float('inf')
        #     b2 = 0
        # else:
        #     a2 = (woll_list[woll_num][1][1] - woll_list[woll_num][0][1]) / (woll_list[woll_num][1][0] - woll_list[woll_num][0][0])#壁の傾き
        #     b2 = woll_list[woll_num][1][1] - a2*woll_list[woll_num][1][0]
        # if mode == "can_move":
        #     if self.before_pos != self.player_pos:
        #         print(self.before_pos,self.player_pos)
        #     print(a1,a2)
        # if abs(a2) == abs(a1):
        #     if mode == "can_move":
        #         print("a")
        #     return True
        # else:
        #     if mode == "can_mode":
        #         if a1 == float('inf') or a2 == float('inf'):
        #             x = self.player_pos.x
        #         else: 
        #             x = (b2 - b1) / (a1 - a2)
        #         y = a1 * x + b1
        #         hitpos = pygame.math.Vector2(x,y)
        #         # print(hitpos)
        #         # return hitpos
        #         if hitpos.x > min(self.player_pos.x,r1_way.x) and hitpos.x < max(r1_way.x,self.player_pos.x) and hitpos.x > min(woll_list[woll_num][0][0],woll_list[woll_num][1][0]) and hitpos.x < max(woll_list[woll_num][0][0],woll_list[woll_num][1][0]):
        #             print("b")
        #             return False
        #         else:
        #             print("c")
        #             return True
        #     elif mode == "vision":
        #         if a1 == float('inf') or a2 == float('inf'):
        #             x = self.player_pos.x
        #         else: 
        #             x = (b2 - b1) / (a1 - a2)
        #         y = a1 * x + b1
        #         hitpos = pygame.math.Vector2(x,y)
        #         if hitpos.x > min(self.player_pos.x,r1_way.x) and hitpos.x < max(r1_way.x,self.player_pos.x) and hitpos.x > min(woll_list[woll_num][0][0],woll_list[woll_num][1][0]) and hitpos.x < max(woll_list[woll_num][0][0],woll_list[woll_num][1][0]):
        #             return hitpos
        #         else:
        #             return True
    def measure_long(self,hitpos): #自機と壁との距離を計算
        long = math.sqrt((hitpos.x - self.player_pos.x)**2 + (hitpos.y - self.player_pos.y)**2)
        return long