import pygame,sys
from pygame.locals import * # 导入pygame库中的一些常量


WINDOW_WIDTH=640
WINDOW_HEIGHT=480
FPS=60


pygame.init()

FPS_CLOCK = pygame.time.Clock() #获取 时钟
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

BASIC_FONT = pygame.font.Font('freesansbold.ttf', 18)

pygame.display.set_caption('MyGame')         #设置标题

background = pygame.image.load('bg.jpg')
plane_img = pygame.image.load("plane.png")
class Plane(pygame.sprite.Sprite):
    def __init__(self, plane_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane_img
        self.rect = self.image.get_rect()
        self.rect.midbottom = init_pos
        self.speed = 10

    def update(self, current_time, rate=60):
        #更新动画帧
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = ( frame_x, frame_y, self.frame_width, self.frame_height )
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame
    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= WINDOW_HEIGHT - self.rect.height:
            self.rect.top = WINDOW_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def moveRight(self):
        if self.rect.left >= WINDOW_WIDTH - self.rect.width:
            self.rect.left = WINDOW_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed

def gamequit():         #定义游戏退出函数
    pygame.quit()       #游戏退出
    sys.exit()          #系统进程退出
player_pos = [100, 100]

plane = Plane(plane_img,player_pos)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:      #如果是退出事件则直接退出
                gamequit()
        elif event.type == KEYDOWN: #如果是键盘事件则打印对应的键盘字符
            if event.key == K_LEFT:
                plane.moveLeft()
                print("左")
            elif event.key == K_RIGHT:
                plane.moveRight()
                print("右")
            elif event.key == K_UP:
                plane.moveUp()
                print("上")
            elif event.key == K_DOWN:
                plane.moveDown()
                print("下")
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_w] or key_pressed[K_UP]:
        plane.moveUp()
    if key_pressed[K_s] or key_pressed[K_DOWN]:
        plane.moveDown()
    if key_pressed[K_a] or key_pressed[K_LEFT]:
        plane.moveLeft()
    if key_pressed[K_d] or key_pressed[K_RIGHT]:
        plane.moveRight()
    DISPLAY_SURF.blit(background, (0, 0))
    FPS_CLOCK.tick(FPS)
    DISPLAY_SURF.blit(plane.image,plane.rect)
    pygame.display.update()
