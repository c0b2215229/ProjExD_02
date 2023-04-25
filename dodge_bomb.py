import random
import sys

import pygame as pg

delta = { # 練習4
        pg.K_UP: (0, -1),
        pg.K_DOWN: (0, +1),
        pg.K_LEFT: (-1, 0),
        pg.K_RIGHT: (+1, 0)
    }
accs = [a for a in range(1, 11)]

def check_bound(scr_rct: pg.Rect,obj_rct:pg.Rect) -> tuple[bool, bool]: # 練習5
    """
    オブジェクトが画面内or画面外を判定し、真理値タプルを返す関数
    引数1：画面SurfaceのRect
    引数2：こうかとん、または、爆弾Surface
    戻り値：横方向、縦方向のはみだし判定結果（画面内：True、画面概：False)
    """
    yoko, tate = True, True # 練習5
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right: # 練習5
        yoko = False # 練習5
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom: # 練習5
        tate = False # 練習5
    return yoko, tate # 練習5

def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((1600, 900))
    clock = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex01/fig/3.png")
    kkc_img = pg.image.load("ex01/fig/8.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    kk_rct = kk_img.get_rect() # 練習4
    kk_rct.center = 900, 400 # 練習4

    bb_img = pg.Surface((20, 20)) # 練習１
    pg.draw.circle(bb_img, (255, 0, 0),(10, 10), 10) # 練習1
    bb_img.set_colorkey((0, 0, 0)) # 練習１
    x, y = random.randint(0,1600), random.randint(0, 900) # 練習2
    # screen.blit(bb_img, [x, y]) # 練習2
    screen.blit(bb_img,[x, y]) # 練習2
    vx, vy = +1, +1 # 練習3
    bb_rct = bb_img.get_rect() # 練習3
    bb_rct.center = x, y # 練習3
    bb_imgs = []
    kk_lst = { # 演習1
        (0, -1):pg.transform.rotozoom(kk_img,0,1),
        (+1, -1):pg.transform.rotozoom(kk_img,45,1),
        (+1, 0):pg.transform.rotozoom(kk_img,90,1),
        (+1, +1):pg.transform.rotozoom(kk_img,135,1),
        (0, +1):pg.transform.rotozoom(kk_img,180,1),
        (-1, +1):pg.transform.rotozoom(kk_img,225,1),
        (-1, 0):pg.transform.rotozoom(kk_img,270,1),
        (-1, -1):pg.transform.rotozoom(kk_img,315,1)
    }
    tmr = 0

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        tmr += 1
        key_lst = pg.key.get_pressed() #練習4
        for k, mv in delta.items(): # 練習4
            if key_lst[k]: # 練習4
                kk_rct.move_ip(mv) # 練習4 
        
        if check_bound(screen.get_rect(),kk_rct) != (True, True):
            for k, mv in delta.items(): # 練習5
                if key_lst[k]: # 練習5
                    kk_rct.move_ip(-mv[0],-mv[1]) # 練習5

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, kk_rct) # 練習4
        bb_rct.move_ip(vx, vy) # 練習3
        yoko, tate = check_bound(screen.get_rect(),bb_rct) # 練習5
        if not yoko: # 横方向にはみ出ていたら　# 練習5
            vx *= -1 # 練習5
        if not tate: # 縦方向にはみ出ていたら　# 練習5
            vy *= -1 # 練習5
        screen.blit(bb_img, bb_rct) # 練習3
        for r in range(1, 11): # 演習2
            bb_img = pg.Surface((20*r,20*r)) # 演習2
            pg.draw.circle(bb_img,(255, 0, 0), (10*r, 10*r), 10*r) # 演習2
            bb_img.set_colorkey((0,0,0))
            bb_imgs.append(bb_img) # 演習2
        bb_img = bb_imgs[min(tmr//1000, 9)] #演習2
        
        if kk_rct.colliderect(bb_rct): # 練習6
            return  # 練習6
        

        pg.display.update()
        clock.tick(1000)



if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()