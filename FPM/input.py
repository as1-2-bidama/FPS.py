import pygame

class Input:
    def __init__(self):
        self.mouse_dir = 90
    def input_key(self,run_bool):
        self.key = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run_bool = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run_bool = False
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.key.append("a")
        if key[pygame.K_w]:
            self.key.append("w")
        if key[pygame.K_d]:
            self.key.append("d")
        if key[pygame.K_s]:
            self.key.append("s") 
        return run_bool,self.key
    def input_mouse(self):
        mouse_move = pygame.mouse.get_rel()
        if mouse_move[0] < 0:
            self.mouse_dir += mouse_move[0]/500
        elif mouse_move[0] > 0:
            self.mouse_dir += mouse_move[0]/500
        return self.mouse_dir