import pygame
from game import *
from setting import *

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("FPS.exe")
game = Game()
clock = pygame.time.Clock()
run = True
while run == True:
    clock.tick(fps)
    run = game.run()
    pygame.display.update()
pygame.quit()
#マウスクリックでフリーズ