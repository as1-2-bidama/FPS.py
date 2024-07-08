import pygame
import sys
from pygame.locals import *
import math

def main(): #main
    angle_list = [-0.52,-0.48,-0.44,-0.40,-0.36,-0.32,-0.28,-0.24,-0.20,-0.16,-0.12,-0.08,-0.04,0,0.04,0.08,0.12,0.16,0.20,0.24,0.28,0.32,0.36,0.40,0.44,0.48,0.52]
    woll_list = [[(80,80),(240,80)],[(240,80),(160,240)],[(160,240),(80,80)],[(300,300),(100,300)]]
    screen_height = 640
    screen_width = 1000
    Green = (0,255,0)
    Red = (255,0,0)
    Blue = (0,0,255)
    Black = (0,0,0)
    White = (255,255,255)
    yellow = (255,0,255)
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))                # 大きさ600*500の画面を生成
    pygame.display.set_caption("GAME")                          # タイトルバーに表示する文字
    player = pygame.math.Vector2(150,150)
    player_angle = 0
    player_dir = pygame.math.Vector2(50,-75)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while (1):
        pygame.mouse.set_pos([screen_width/2,screen_height/2])
        clock.tick(60)
        screen.fill(White)                                    # 画面を白色に塗りつぶし
        player_angle,player_after,flags = Imput(player,player_angle,woll_list,angle_list)
        Draw(screen,Blue,Red,Green,Black,yellow,player,player_angle,screen_width,angle_list,woll_list)

        # イベント処理


def Draw(screen,Blue,Red,Green,Black,yellow,player,player_angle,screen_width,angle_list,woll_list): #描画の処理
    col_list = [Black,Blue,Red,Green,yellow]
    ver = ""

    for i in range(len(woll_list)): #壁の線分と視線の並行を計算
        ver = Intersection_Vertical(player_angle,player,woll_list,i,ver)

    for woll_num in range(len(woll_list)): #視点の線分と交点、3Dviewを描写
        for angle in angle_list:
            hitpos = Keisan(player_angle,player,angle,woll_list,woll_num)
            if hitpos != None:
                    if ver == True:
                        angle = 0
                        hitpos = Keisan(player_angle,player,angle,woll_list,woll_num)
                        if hitpos == None:
                            long = 0.1
                        else:
                            long = TDview(player,hitpos)
                    else:
                        long = TDview(player,hitpos)

                    pygame.draw.line(screen, Black, (((screen_width/len(angle_list)) * angle_list.index(angle)),300), (((screen_width/len(angle_list)) * angle_list.index(angle)),230-(50/long)*40),int((screen_width/len(angle_list))))
                    pygame.draw.line(screen, Black, (((screen_width/len(angle_list)) * angle_list.index(angle)),300), (((screen_width/len(angle_list)) * angle_list.index(angle)),370+(50/long)*40),int((screen_width/len(angle_list))))
    pygame.display.update()                                 # 画面を更新
        
def Imput(player,player_angle,woll_list,angle_list): #入力の処理
    player_after = pygame.math.Vector2()
    player_dir_flags = []
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
    if key_pressed[pygame.K_a]:
        player_after.x,player_after.y = pygame.math.Vector2(math.cos(player_angle+1.6)+player.x,math.sin(player_angle+1.6)+player.y)
        angle = 1.6
        for woll_num in range(len(woll_list)):
            hitpos = Keisan_move(player_angle,player,angle,woll_list,woll_num)
            if hitpos == None:
                player = player_after
            else:
                long = TDview(player,hitpos)
                if long > 2.5:
                    player = player_after
        player_dir_flags.append("Left")
    if key_pressed[pygame.K_d]:
        player_after.x,player_after.y = pygame.math.Vector2(math.cos(player_angle+1.6)*-1+player.x,math.sin(player_angle+1.6)*-1+player.y)
        angle = -1.6
        for woll_num in range(len(woll_list)):
            hitpos = Keisan_move(player_angle,player,angle,woll_list,woll_num)
            if hitpos == None:
                player = player_after
            else:
                long = TDview(player,hitpos)
                if long > 2.5:
                    player = player_after
        player_dir_flags.append("Right")
    if key_pressed[pygame.K_w]:
        player_after.x,player_after.y = pygame.math.Vector2(math.cos(player_angle)*2+player.x,math.sin(player_angle)*2+player.y)
        angle = 0
        hitpos = []
        for woll_num in range(len(woll_list)):
            hitpos.append(Keisan_move(player_angle,player,angle,woll_list,woll_num))
        if int not in hitpos:
            player = player_after
        else:
            hitpos = [i for i in hitpos if type(i) == int]
            long = TDview(player,hitpos)
            if long > 2.5:
                player = player_after
        player_dir_flags.append("Foward")
    if key_pressed[pygame.K_s]:
        player_after.x,player_after.y = pygame.math.Vector2(math.cos(player_angle)*-2+player.x,math.sin(player_angle)*-2+player.y)
        player_dir_flags.append("Back")
    return player_angle,player_after,player_dir_flags

def Keisan(player_angle,player,angle,woll_list,woll_num): #視線のベクトルを計算
    player_dir = pygame.math.Vector2(math.cos(player_angle+angle)*50+player.x,math.sin(player_angle+angle)*50+player.y)
    hitpos = Intersection(player,player_dir,woll_list,woll_num)
    return hitpos

def Intersection(player,player_dir,woll_list,woll_num): #視線の線分と壁の線分の交点を計算
    r1_way = player_dir
    r1_pos = player
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
        if hitpos.x > min(player.x,player_dir.x) and hitpos.x < max(player.x,player_dir.x) and hitpos.x > min(r2_way[0],r2_pos[0]) and hitpos.x < max(r2_pos[0],r2_way[0]):
            return hitpos
        else:
            return None

def Intersection_Vertical(player_angle,player,woll_list,i,ver): #視線のアングル０と壁の垂直を計算
    r1_way = pygame.math.Vector2(math.cos(player_angle)*50+player.x,math.sin(player_angle)*50+player.y)
    r1_pos = player
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

def Intersection_Ve(player_angle,player): #視線のアングル０と壁の垂直を計算
    r1_way = pygame.math.Vector2(math.cos(player_angle)*50+player.x,math.sin(player_angle)*50+player.y)
    r1_pos = player
    if (r1_way.x - r1_pos.x) == 0:
        a1 = float('inf')
    else:
        a1 = (r1_way.y - r1_pos.y) / (r1_way.x - r1_pos.x)#視線の傾き
    
    
def TDview(player,hitpos): #自機と壁との距離を計算
    a = math.sqrt((hitpos.x - player.x)**2 + (hitpos.y - player.y)**2)
    print(a)
    return a

def Keisan_move(player_angle,player,angle,woll_list,woll_num): #視線のベクトルを計算
    player_dir = pygame.math.Vector2(math.cos(player_angle+angle)*50+player.x,math.sin(player_angle+angle)*50+player.y)
    hitpos = Intersection(player,player_dir,woll_list,woll_num)
    return hitpos
if __name__ == "__main__":
    main()