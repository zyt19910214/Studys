# coding: utf-8
import pygame
from pygame.locals import * # 导入pygame库中的一些常量
from pygame.math import *
from sys import exit # 导入sys库中的exit函数
#from gameobjects.vector2 import Vector2
from math import *
# 定义窗口的分辨率
SCREEN_WIDTH = 603
SCREEN_HEIGHT = 603
# 初始化游戏
pygame.init()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT], 0, 32)
# 初始化一个用于显示的窗口
pygame.display.set_caption('LOL')
# 设置窗口标题 #加载并转换图像
background = pygame.image.load("background.jpg").convert()
# 加载图片资源
major_cursor = pygame.image.load("major.png").convert_alpha()
mouse_cursor = pygame.image.load("cursor.png").convert_alpha()
fire_cursor = pygame.image.load("fire.png").convert_alpha()
boom_cursor = pygame.image.load("boom.png").convert_alpha()
major_pos_new = major_pos_old = (20.0, 550.0)
mouse_pos = (300.0, 300.0)
sunflower_pos = (35, 420)
bullets = []
def load_image(file, width=None, number=None):
    try:
        surface = pygame.image.load(file).convert_alpha()
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    if width == None: return surface
    height = surface.get_height()

    return [surface.subsurface(
        Rect((i * width, 0), (width, height)) ) for i in range(number)] # 返回切片后的图片列表，按帧控制显示

class SunFlower(pygame.sprite.Sprite):
    _rate = 100
    _width = 82
    _height = 77
    _number = 18
    _life = 100
    images = []
    def __init__(self):
        self.order = 0
        pygame.sprite.Sprite.__init__(self)
        if len(self.images) == 0:
            self.images = load_image("sunflower.png", self._width, self._number)
        self.image = self.images[self.order]
        self.rect = Rect(0, 0, self._width, self._height)
        self.life = self._life
        self.passed_time = 0

    def update(self, passed_time):
        self.passed_time += passed_time
        self.order = ( self.passed_time // self._rate ) % self._number
        if self.order == 0 and self.passed_time > self._rate:
            self.passed_time = 0

        return self.images[self.order]

if __name__ == '__main__':
    sunflower = SunFlower()
    clock = pygame.time.Clock()
    screen.blit(major_cursor, major_pos_old) # 主角
    # #游戏主循环
    while True:
        screen.blit(background, (0,0)) # 背景
        #  major_pos_old = straight_move(major_pos_old, major_pos_new)
        for event in pygame.event.get(): #接收到退出事件后退出程序
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            major_pos_new = major_pos_old
                            bullet_pos = (major_pos_old[0], major_pos_old[1])
                            vector_direction = Vector2.from_points(bullet_pos, pygame.mouse.get_pos())
                            vector_direction.normalize()
                            bullets.append([bullet_pos, vector_direction]) # 添加子弹位置及方向
                    elif index == 1:
                        pass
                    elif index == 2:
                        major_pos_new = pygame.mouse.get_pos()
        time_passed = clock.tick()
        for bullet in bullets:
            print(bullet[0][0], bullet[0][1])
            if (int(bullet[0][0]) in range(20, 70)) and (int(bullet[0][1]) in range(410, 460)):
                sunflower.life -= 10
                bullets.remove(bullet)
            elif (bullet[0][0] > 0 and bullet[0][0] < 603) and (bullet[0][1] > 0 or bullet[0][1] < 603):
                bullet[0] += bullet[1] * time_passed * 0.5 # 设置子弹按帧移动
                screen.blit(fire_cursor, bullet[0])
            else:
                bullets.remove(bullet)
        vector_to_new = Vector2(major_pos_old, major_pos_new)
        vector_to_new.normalize()
        major_pos_old += vector_to_new * time_passed * 0.1
        vector_mouse = Vector2(major_pos_old, pygame.mouse.get_pos())
        vector_mouse.normalize()
        # print(degrees(acos(vector_mouse[0])))
        if vector_mouse[1] >= 0:
            derection = -1
        else: derection = 1
        if vector_mouse[0] >= 0:
            major_sufurce = major_cursor
        else: major_sufurce = pygame.transform.flip(major_cursor, False, True) # 根据Y轴翻转

        major_cursor_ratation = pygame.transform.rotate(major_sufurce, derection * degrees(acos(vector_mouse[0]))) # 设置偏移角度
        screen.blit(major_cursor_ratation, (major_pos_old[0]-30, major_pos_old[1]-15))
        if sunflower.life > 0:
            img = sunflower.update(time_passed)
            screen.blit(img, sunflower_pos)
            my_font = pygame.font.SysFont("arial", 15) # 设置血量
            text_surface = my_font.render(str(sunflower.life), True, (255,0,0))
            screen.blit(text_surface, (sunflower_pos[0]+25, sunflower_pos[1]-15))
        else:
            screen.blit(boom_cursor, sunflower_pos)
            screen.blit(mouse_cursor, pygame.mouse.get_pos())
            pygame.mouse.set_visible(False) # 设置鼠标不可见
            pygame.display.update() #刷新画面