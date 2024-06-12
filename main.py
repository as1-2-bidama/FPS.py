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
    game.run()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
    pygame.display.update()
pygame.quit()