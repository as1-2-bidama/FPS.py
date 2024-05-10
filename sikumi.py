import pygame
import sys
from pygame.locals import *
import math

def main(): #main
    screen_height = 640
    screen_width = 1000
    Green = (0,255,0)
    Red = (255,0,0)
    Blue = (0,0,255)
    Black = (0,0,0)
    White = (255,255,255)
    yellow = (255,0,255)
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("GAME")                          # タイトルバーに表示する文字
    mouse = pygame.math.Vector2(150,150)
    player_angle = 0
    player_dir = pygame.math.Vector2(50,-75)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while (1):
        pygame.mouse.set_pos([screen_width/2,screen_height/2])
        clock.tick(60)
        screen.fill(White)                                    # 画面を白色に塗りつぶし
        player_angle = Imput(mouse,player_angle)
        Draw(screen,Blue,Red,Green,Black,yellow,mouse,player_dir,player_angle,screen_width,screen_height)

        # イベント処理


def Draw(screen,Blue,Red,Green,Black,yellow,mouse,player_dir,player_angle,screen_width,screen_height): #描画の処理
    col_list = [Black,Blue,Red,Green,yellow]
    ver = ""
    angle_list = [-0.52,-0.48,-0.44,-0.40,-0.36,-0.32,-0.28,-0.24,-0.20,-0.16,-0.12,-0.08,-0.04,0,0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52]
    woll_list = [[(80,80),(240,80)],[(240,80),(160,240)],[(160,240),(80,80)],[(300,300),(100,300)]]
    for i in range(len(woll_list)): #壁の線分を描写
        # pygame.draw.aaline(screen, Black, woll_list[i][0], woll_list[i][1], 10)   # 直線の描画
        ver = Intersection_Vertical(player_angle,mouse,woll_list,i,ver)

    for woll_num in range(len(woll_list)): #視点の線分と交点、3Dviewを描写
        for angle in angle_list:
            player_dir,hitpos = Keisan(player_angle,mouse,angle,woll_list,woll_num)
            # pygame.draw.line(screen, yellow, (mouse.x,mouse.y), (player_dir.x,player_dir.y))
            if hitpos != None:

                    # pygame.draw.circle(screen, yellow, (hitpos.x,hitpos.y),5)
                    if ver == True:
                        angle = 0
                        player_dir,hitpos = Keisan(player_angle,mouse,angle,woll_list,woll_num)
                        long = TDview()
                    else:
                        long = TDview(mouse,hitpos)
                    pygame.draw.line(screen, Black, (((screen_width/len(angle_list)) * angle_list.index(angle)),300), (((screen_width/len(angle_list)) * angle_list.index(angle)),230-(50/long)*40),int((screen_width/len(angle_list))))
                    pygame.draw.line(screen, Black, (((screen_width/len(angle_list)) * angle_list.index(angle)),300), (((screen_width/len(angle_list)) * angle_list.index(angle)),370+(50/long)*40),int((screen_width/len(angle_list))))
    # pygame.draw.circle(screen, Black, (mouse.x,mouse.y), 10)
    pygame.display.update()                                 # 画面を更新
        
def Imput(mouse,player_angle): #入力の処理
    for event in pygame.event.get():
        if event.type == QUIT:                              # 閉じるボタンが押されたら終了
            pygame.quit()                                   # Pygameの終了(画面閉じられる)
            sys.exit()
    mouse_move = pygame.mouse.get_rel()
    if mouse_move[0] < 0:
        player_angle -= 0.05
    elif mouse_move[0] > 0:
        player_angle += 0.05
    key_pressed = pygame.key.get_pressed()
    if key_pressed[pygame.K_RIGHT]:
        player_angle += 0.1
    elif key_pressed[pygame.K_LEFT]:
        player_angle -= 0.1
    if key_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if key_pressed[pygame.K_d]:
        mouse.x,mouse.y = pygame.math.Vector2(math.cos(player_angle+1.6)+mouse.x,math.sin(player_angle+1.6)+mouse.y)
    if key_pressed[pygame.K_a]:
        mouse.x,mouse.y = pygame.math.Vector2(math.cos(player_angle+1.6)*-1+mouse.x,math.sin(player_angle+1.6)*-1+mouse.y)
    if key_pressed[pygame.K_w]:
        mouse.x,mouse.y = pygame.math.Vector2(math.cos(player_angle)*2+mouse.x,math.sin(player_angle)*2+mouse.y)
    if key_pressed[pygame.K_s]:
        mouse.x,mouse.y = pygame.math.Vector2(math.cos(player_angle)*-2+mouse.x,math.sin(player_angle)*-2+mouse.y)
    return player_angle

def Keisan(player_angle,mouse,angle,woll_list,woll_num): #視線のベクトルを計算
    player_dir = pygame.math.Vector2(math.cos(player_angle+angle)*50+mouse.x,math.sin(player_angle+angle)*50+mouse.y)
    hitpos = Intersection(mouse,player_dir,woll_list,woll_num)
    return player_dir,hitpos

def Intersection(mouse,player_dir,woll_list,woll_num): #視線の線分と壁の線分の交点を計算
    r1_way = player_dir
    r1_pos = mouse
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
        hitpos = None
        return hitpos
    else:
        if a1 == float('inf') or a2 == float('inf'):
            x = r1_pos.x
        else: 
            x = (b2 - b1) / (a1 - a2)
        y = a1 * x + b1
        hitpos = pygame.math.Vector2(x,y)
        if hitpos.x > min(mouse.x,player_dir.x) and hitpos.x < max(mouse.x,player_dir.x) and hitpos.x > min(r2_way[0],r2_pos[0]) and hitpos.x < max(r2_pos[0],r2_way[0]):
            return hitpos
        else:
            return None

def Intersection_Vertical(player_angle,mouse,woll_list,i,ver): #視線のアングル０と壁の垂直を計算
    r1_way = pygame.math.Vector2(math.cos(player_angle)*50+mouse.x,math.sin(player_angle)*50+mouse.y)
    r1_pos = mouse
    r2_way = woll_list[i][1]
    r2_pos = woll_list[i][0]
    if (r1_way.x - r1_pos.x) == 0:
        a1 = float('inf')
    else:
        a1 = (r1_way.y - r1_pos.y) / (r1_way.x - r1_pos.x)#視線の傾き
    if (r2_way[0] - r2_pos[0]) == 0:
        a2 = float('inf')
    else:
        a2 = (r2_way[1] - r2_pos[1]) / (r2_way[0] - r2_pos[0])#壁の傾き
    if a1 * a2 == -1 or ver == True:
        ver = True
    else:
        ver = False
    return ver
    
def TDview(mouse,hitpos): #自機と壁との距離を計算
    a = math.sqrt((hitpos.x - mouse.x)**2 + (hitpos.y - mouse.y)**2)
    print(a)
    return a


if __name__ == "__main__":
    main()