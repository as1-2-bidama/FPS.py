import pygame
import time
from root import Root
start = time.time()  # 現在時刻（処理開始前）を取得

root = Root()
clock = pygame.time.Clock()
run = root.run_bool
fps = 60

while run == True:
    clock.tick(fps)
    run = root.run()
    end = time.time()  # 現在時刻（処理完了後）を取得
    time_diff = end - start  # 処理完了後の時刻から処理開始前の時刻を減算する
    print(time_diff)  # 処理にかかった時間データを使用
pygame.quit()