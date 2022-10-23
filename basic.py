# coding: utf-8
from concurrent.futures.process import _ThreadWakeup
import nntplib
from turtle import width
import pygame
from pygame.locals import *
import sys
import os



def load_image(foldername,filename,colorkey = None):
    try:
        image = pygame.image.load(os.path.join(foldername,filename))
    except pygame.error as message:
        print ,"Cannot load image:",filename
        raise SystemExit
    image = image.convert()
    if colorkey != None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey,RLEACCEL)
    return image,image.get_rect()

#使い方　mobImg,mobRect = load_image("image","metamon.png",colorkey=-1)

SCR_RECT = Rect(0,0,1536,864) #PCの解像度に合わせること推奨
#SCR_WIDTH,SCR_HEIGHT = 1536,864

#スプライト(背景とは別に動く画像のこと)
class MySprite(pygame.sprite.Sprite): #オリジナルスプライト作成時，スプライトクラスを継承している
    def __init__(self,foldername,filename,x,y,vx,vy):
        pygame.sprite.Sprite.__init__(self,self.containers) #スプライトクラスの__init__()（コンストラクタ）を呼び出している
        self.image = pygame.image.load(os.path.join(foldername,filename)).convert_alpha()
        self.image = pygame.transform.scale(self.image,(100,100))
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x,y,width,height)
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect.move_ip(self.vx,self.vy)
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        self.rect = self.rect.clamp(SCR_RECT) #画面からはみ出ないようにする
    """
    def draw(self,screen):
        screen.blit(self.image,self.rect)
    """

def main():
    #pygame初期化
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"Basic")
    backImg = pygame.image.load(os.path.join("image","3Dblock.png")).convert() #背景画像
    
    #スプライトグループを作成してスプライトクラスに割り当て
    group = pygame.sprite.RenderUpdates()
    MySprite.containers = group
    
    #スプライト作成
    metamon1 = MySprite("image","metamon.png",0,0,2,2)
    metamon2 = MySprite("image","metamon.png",10,10,5,5)
    metamon3 = MySprite("image","metamon.png",320,240,-2,3)
    """
    #スプライトグループを作成してスプライトを追加
    group = pygame.sprite.RenderUpdates()
    group.add(metamon1)
    group.add(metamon2)
    group.add(metamon3)
    """
    """
    #text
    sysfont = pygame.font.SysFont(None,80) #(フォント名，サイズ)

    sysfont.set_bold(True) #太文字
    sysfont.set_italic(True) #斜体
    sysfont.set_underline(True) #アンダーライン

    hellow1 = sysfont.render("Hellow,world!",False,(0,0,0)) #(文字列，アンチエイリアシング，文字の色，背景色)
    hellow2 = sysfont.render("Hellow,world!",True,(0,0,0))
    hellow3 = sysfont.render("Hellow,world!",True,(255,0,0),(255,255,0))
    """
    """
    #画像
    backImg = pygame.image.load(os.path.join("image","3Dblock.png")).convert()
    mobImg = pygame.image.load(os.path.join("image","metamon.png")).convert_alpha() #画像の透明色を透明に描画
    mobImg = pygame.transform.scale(mobImg,(100,100))
    mobImg_rect = mobImg.get_rect()
    mobImg_rect.center = (320,240)
    #mob2Img = pygame.image.load(os.path.join("image","metamon.jpg")).convert()
    #colorkey = mob2Img.get_at((0,0)) #左上に色を透明色に指定
    #mob2Img.set_colorkey(colorkey,RLEACCEL)
    """
    """
    #マウスイベント
    cur_pos =(0,0)
    mob_pos = []
    """
    
    #アニメーション
    #vx = vy = 2 #移動ピクセル
    #vx = vy = 120 #1秒間の移動ピクセル
    clock = pygame.time.Clock()
    
    """ 
    #キーイベント
    kvx = kvy = 5
    """
    """ 
    #サウンドをロード
    hit_sound = pygame.mixer.Sound(os.path.join("sound","hit.wav"))
    hit_sound.set_volume(0.3) #音量
    """
     
    #BGM
    pygame.mixer.music.load(os.path.join("bgm","retroparty.mp3"))
    pygame.mixer.music.set_volume(0.3) #音量
    pygame.mixer.music.play(-1) #-1でループ再生
    
    """
    #汚れたRect
    background = pygame.Surface(SCR_RECT.size)
    background.fill((0,0,255))
    screen.blit(background,(0,0))
    screen.blit(backImg,(0,0))
    pygame.display.update()
    """

    #フルスクリーン
    fullscreen_flag = False
    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        screen.blit(backImg,(0,0))
        
        """
        #text
        screen.blit(hellow1,(20,50)) #(座標)
        screen.blit(hellow2,(20,150))
        screen.blit(hellow3,(20,250))
        """
        """
        #図形の描画
        pygame.draw.rect(screen,(255,255,0),Rect(10,10,300,200))#第4引数 線の太さ
        #screen.fill((255,255,0),Rect(10,10,300,200))の方が描画速度が速い
        pygame.draw.circle(screen,(255,0,0),(320,240),100)
        pygame.draw.ellipse(screen,(255,0,255),(400,300,200,100))
        pygame.draw.line(screen,(255,255,255),(0,0),(640,480)) #第5引数 線の太さ
        """
        """
        #画像
        screen.blit(backImg,(0,0))
        #screen.blit(mobImg,(100,100))
        #screen.blit(mob2Img,(200,200))
        #screen.blit(mobImg,mobImg_rect)
        """
        """
        #マウスイベント(pygame.mouse)
        mouse_pressed = pygame.mouse.get_pressed()
        if mouse_pressed[0]: #左クリック
            x,y = pygame.mouse.get_pos()
            x -= mobImg.get_width()/2
            y -= mobImg.get_height()/2
            mob_pos.append((x,y))

        x,y = pygame.mouse.get_pos()
        x -= mobImg.get_width()/2
        y -= mobImg.get_height()/2
        cur_pos = (x,y)

        screen.blit(mobImg,cur_pos)
        for i,j in mob_pos:
            screen.blit(mobImg,(i,j))

        #マウスボタンを押した/離したの瞬間を検出したい場合はイベントハンドラ、
        #マウスボタンが押された状態かを検出したい場合は pygame.mouseを使うとよい
        """
        
        """
        #アニメーション
        #clock.tick(60) #60fps
        time_passed = clock.tick(60) #60fpsで全開からの経過時間を返す
        time_passed_seconds = time_passed/1000.0 #ミリ秒を秒に変換
        #mobImg_rect.move_ip(vx,vy)
        mobImg_rect.x += vx * time_passed_seconds
        mobImg_rect.y += vy * time_passed_seconds
        if mobImg_rect.left < 0 or mobImg_rect.right > SCR_WIDTH:
            hit_sound.play() #サウンド再生
            vx = -vx
        if mobImg_rect.top < 0 or mobImg_rect.bottom > SCR_HEIGHT:
            hit_sound.play()
            vy = -vy
        screen.blit(mobImg,mobImg_rect)
        """
        """
        #キーイベント(pygame.mouse)
        pressed_keys = pygame.key.get_pressed() #押されているキー
        if pressed_keys[K_a]:
            mobImg_rect.move_ip(-kvx,0)
        if pressed_keys[K_d]:
            mobImg_rect.move_ip(kvx,0)
        if pressed_keys[K_w]:
            mobImg_rect.move_ip(0,-kvy)
        if pressed_keys[K_s]:
            mobImg_rect.move_ip(0,kvy)
        screen.blit(mobImg,mobImg_rect)
        """
        """
        #スプライトの更新・描画
        metamon1.update()
        metamon2.update()
        metamon3.update()

        metamon1.draw(screen)
        metamon2.draw(screen)
        metamon3.draw(screen)
        """
        #screen上のスプライトを背景で消去
        #group.clear(screen,background)

        #スプライトグループの更新・描画
        group.update()
        group.draw(screen)
        #print ,metamon1.rect
        #enderUpdateのdraw()は変化があった部分の短形(dirty rect)を返す
        #dirty_rects = group.draw(screen)
        #print ,dirty_rects

        pygame.display.update()

        #終了処理
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            #キーイベント(イベントハンドル)
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                elif event.key == K_F2:
                    fullscreen_flag = not fullscreen_flag
                    if fullscreen_flag:
                        #screen = pygame.display.set_mode(SCR_RECT.size,FULLSCREEN,32)
                        screen = pygame.display.set_mode(SCR_RECT.size,DOUBLEBUF|HWSURFACE|FULLSCREEN) #高速化
                    else:
                        screen = pygame.display.set_mode(SCR_RECT.size,0,32)
                        
                """
                if event.key == K_LEFT:
                    mobImg_rect.move_ip(-kvx,0)
                if event.key == K_RIGHT:
                    mobImg_rect.move_ip(kvx,0)
                if event.key == K_UP:
                    mobImg_rect.move_ip(0,-kvy)
                if event.key == K_DOWN:
                    mobImg_rect.move_ip(0,kvy)
                """
            """
            #マウスイベント(イベントハンドラ)
            if event.type == MOUSEBUTTONDOWN and event.button == 1: 
                #buttonの1は左クリック,2は中クリック,3は右クリック
                x, y = event.pos
                x -= mobImg.get_width()/2
                y -= mobImg.get_height()/2
                mob_pos.append((x,y))
            if event.type == MOUSEMOTION:
                #relはカーソルの移動距離を表す
                x, y = event.pos
                x -= mobImg.get_width()/2
                y -= mobImg.get_height()/2
                cur_pos = (x,y)

            screen.blit(mobImg,cur_pos)
            for i,j in mob_pos:
                screen.blit(mobImg,(i,j))
            """
if __name__ == "__main__": #実行時に__name__に__main__の文字列が代入される
    main()