import pygame
from setting import *
from seen_title import Title
from seen_diffc import Diffc
from seen_game import Gamemode
from seen_result import Result

class Game:
    def __init__(self):
        self.seen_list = ["title","diffc","gamemode","result"]
        self.seen_Title = Title()
        self.seen_Diffc = Diffc()
        self.seen_Game = Gamemode()
        self.seen_Result = Result()
        self.seen_num = 0
    def run(self):
        if self.seen_list[self.seen_num] == "title":
            self.seen_num = self.seen_Title.run()
        elif self.seen_list[self.seen_num] == "diffc":
            self.seen_num = self.seen_Diffc.run()
        elif self.seen_list[self.seen_num] == "gamemode":
            self.seen_num = self.seen_Game.run()
        elif self.seen_list[self.seen_num] == "result":
            self.seen_num = self.seen_Result.run()
            