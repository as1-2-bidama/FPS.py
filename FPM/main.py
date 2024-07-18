import pygame
import time
from root import Root

root = Root()
clock = pygame.time.Clock()
run = root.run_bool
fps = 60

while run == True:
    clock.tick(fps)
    run = root.run()
pygame.quit()