from concurrent.futures.process import _ThreadWakeup
import nntplib
from turtle import width
import pygame
from pygame.locals import *
import sys

from basic import load_image,load_sound

SCR_RECT = Rect(0,0,640,768)
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image,self.rect = load_image("paddle.png")
        self.rect.bottom = SCR_RECT.bottom
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0] #マウスのx座標
        self.rect.clamp_ip(SCR_RECT)

class Ball(pygame.sprite.Sprite):
    speed = 5
    def __init__(self,paddle,blocks):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image,self.rect = load_image("metamon.png")
        self.dx = self.dy = 0
        self.paddle = paddle
        self.blocks = blocks
        self.update = self.start
    def start(self): #self.updateにself.startが格納されている状態でself.update()を呼び出すとself.start()が呼び出される
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = self.speed
            self.dy = -self.speed
            self.update = self.move
    def move(self):
        self.rect.centerx += self.dx
        self.rect.centery += self.dy
        #壁との反射
        if self.rect.left < SCR_RECT.left:
            self.rect.left = SCR_RECT.left
            self.dx = -self.dx
        if self.rect.right > SCR_RECT.right:
            self.rect.right = SCR_RECT.right
            self.dx = -self.dx
        if self.rect.top < SCR_RECT.top:
            self.rect.top = SCR_RECT.top
            self.dy = -self.dy
        #パドルとの反射
        if self.rect.colliderect(self.paddle.rect) and self.dy > 0: #A.colliderect(B) AとBの矩形範囲が衝突していたらTrueを返す
            self.dy = -self.dy
            self.paddle_sound.play()
        #ボールの落下
        if self.rect.top > SCR_RECT.bottom:
            self.update = self.start
            self.fall_sound.play()
        #壁の破壊
        block_collided = pygame.sprite.spritecollide(self,self.blocks,True)
        if block_collided:
            oldrect = self.rect
            for block in block_collided:
                if oldrect.left < block.rect.left < oldrect.right < block.rect.right:
                    self.rect.right = block.rect.left
                    self.dx = -self.dx
                if block.rect.left < oldrect.left < block.rect.right < oldrect.right:
                    self.rect.left = block.rect.right
                    self.dx = -self.dx
                if oldrect.top < block.rect.top < oldrect.bottom < block.rect.bottom:
                    self.rect.bottom = block.rect.top
                    self.dy = -self.dy
                if block.rect.top < oldrect.top < block.rect.bottom < oldrect.bottom:
                    self.rect.top = block.rect.bottom
                    self.dy = -self.dy
                self.block_sound.play()
                
            
class Block(pygame.sprite.Sprite):
    def __init__(self,filename,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.image,self.rect = load_image(filename)
        self.rect.left = SCR_RECT.left + x*self.rect.width
        self.rect.top = SCR_RECT.top + y*self.rect.height

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"Break Block")

    all = pygame.sprite.RenderUpdates()
    blocks = pygame.sprite.Group()
    Paddle.containers = all
    Ball.containers = all
    Block.containers = all,blocks
    Ball.paddle_sound = load_sound("paddle_hit.mp3")
    Ball.block_sound = load_sound("block_hit.mp3")
    Ball.fall_sound = load_sound("fall_hit.wav")

    paddle = Paddle()
    for x in range(0,10):
        for y in range(1,6):
            if y == 1:
                Block("block_red.png",x,y)
            if y == 2:
                Block("block_purple.png",x,y)
            if y == 3:
                Block("block_yellow.png",x,y)
            if y == 4:
                Block("block_green.png",x,y)
            if y == 5:
                Block("block_blue.png",x,y)
    Ball(paddle,blocks)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        screen.fill((0,0,0))
        all.update()
        all.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

if __name__ == "__main__": #実行時に__name__に__main__の文字列が代入される
    main()