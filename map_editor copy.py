#coding:utf-8

import pygame
import sys
import os
import easygui
import xlrd
from PIL import Image,ImageDraw



background = (237,237,237)
black = (0,0,0)
green = (0,255,0)#tree
blue = (0,0,255)#river
sand = (255,235,205)#sand
red = (255,0,0)#mountain
ice = (50,200,180)#ice
grey = (190,190,190)#small mountain
DEFAULT_SIZE = [1000,800]

h0 = 0
w0 = 0



maplist = []
ButtonDict1 = {}

class Map_information():
    def __init__(self):
        self.landform = 0 #0 平原 1 森林 2 河流 3 沙漠 4 高山 5 雪地 6 丘陵
        self.buildings = 0 #0 空地 1 城墙 2 防御建筑：箭楼 3 防御建筑：石墙 4 关隘 5 防御建筑：投石台
        self.buildings_hp = 0
        self.buildings_defend = 0
        self.buildings_attack = 0
        self.buildings_country = ""
        self.soldiers = 0 #0 空地 1 步卒 2 骑手 3 弓手 4 器械
        self.general = 0
        self.soldiers_hp = 0
        self.soldiers_defend = 0
        self.soldiers_attack = 0
        self.soldiers_type = 0 
        # 1 农夫 2 轻步兵 3 重步兵 4 近卫军 5 青州军 6 藤甲军 7 蛮族军 8 黄巾军 9 山越勇士 10 大戟士
        # 1 轻骑兵 2 重骑兵 3 铁骑兵 4 虎豹骑 5 象兵 6 战车 
        # 1 征召弓手 2 熟练弓手 3 精锐弓手 4 弩手 5 乌丸骑手 6 匈奴骑手 7 白马义从 8 诸葛连弩
        # 1 冲车 2 井栏 3 霹雳车
        self.soldiers_ship = 0 # 0 走舸 1 艨艟 2 楼船 3 斗舰
        self.soldiers_strength = 0  # 移動
        self.soldiers_experience = 0    # 當前經驗
        self.soldiers_level = 0 # 當前等級
        self.soldiers_will = 0  # 當前士氣
        self.soldiers_attackrange = 0   # 攻擊範圍
        self.soldiers_country = ""


def Button_click1(x,y):
    for mykey in ButtonDict1.keys():
        if x in range(ButtonDict1[mykey][0][0],ButtonDict1[mykey][1][0]) \
            and y in range(ButtonDict1[mykey][0][1],ButtonDict1[mykey][1][1]):
            return mykey

def Button_click(x,y):
    if x in range(20,20 + h0*30) and y in range(20,20 + w0*30):
        return int((x-20)/30),int((y-20)/30)

class Button():
    global ButtonDict1,maplist
    ButtonDict1 = {}
    mode = -1
    def __init__(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(40,20))
        ButtonDict1[button_name] = [self.vertex,(self.vertex[0] + 40,self.vertex[1] + 20)]
        screen.blit(self.paint,self.vertex)

    def add_new(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(40,20))
        ButtonDict1[button_name] = [self.vertex,(self.vertex[0] + 40,self.vertex[1] + 20)]
        screen.blit(self.paint,self.vertex)

    def button_a_click(self):
        self.mode = 1

    def button_b_click(self):
        self.mode = 2

    def button_c_click(self):
        self.mode = 3
    
    def button_d_click(self):
        self.mode = 4

    def button_e_click(self):
        self.mode = 5

    def button_f_click(self):
        self.mode = 6

    def button_g_click(self):
        self.mode = -1
        easygui.buttonbox("选择建筑","建筑",("城墙","箭楼","石墙","关隘","投石台"))

    def button_clear_click(self):
        self.mode = 0
        

def map_size(height0,width0):
    global h0,w0,screen
    screen = pygame.display.set_mode(DEFAULT_SIZE)
    surface = pygame.surface.Surface(DEFAULT_SIZE)

    screen.fill(background)

    a = Button((940,40),"image/m1.bmp","a")
    b = a.add_new((940,70),"image/m3.bmp","b")
    c = a.add_new((940,100),"image/m4.bmp","c")
    d = a.add_new((940,130),"image/m2.bmp","d")
    e = a.add_new((940,160),"image/m6.bmp","e")
    f = a.add_new((940,190),"image/m7.bmp","f")
    g = a.add_new((940,220),"image/m8.bmp","g")
    h = a.add_new((940,250),"image/m9.bmp","h")
    clear = a.add_new((940,400),"image/m5.bmp","clear")
    maplist = [[Map_information() for i in range(height0)] for j in range(width0)]
   

    width = width0 + 1
    height = height0 + 1
    for i in range(width):
        pygame.draw.line(screen,black,[20,20+i*30],[20+height*30 - 30,20+i*30])
    for i in range(height):
        pygame.draw.line(screen,black,[20+i*30,20],[20+i*30,20+width*30 - 30])
    pygame.display.flip()
    while True:
        x,y = pygame.mouse.get_pos()
        MyActiveC = Button_click1(x,y)
        MyActiveD = Button_click(x,y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if MyActiveC:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    exec("a.button_{}_click()".format(MyActiveC))
            if MyActiveD:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if a.mode == 1:
                        draw_tree(screen,MyActiveD[0],MyActiveD[1])
                        maplist[MyActiveD[1]][MyActiveD[0]].landform = 1
              
                      
                    elif a.mode == 2:
                        draw_river(screen,MyActiveD[0],MyActiveD[1])
                        maplist[MyActiveD[1]][MyActiveD[0]].landform = 2
                    
                        
                    elif a.mode == 3:
                        draw_sand(screen,MyActiveD[0],MyActiveD[1])
                        maplist[MyActiveD[1]][MyActiveD[0]].landform = 3
                        
                        
                    elif a.mode == 4:
                        draw_mountain(screen,MyActiveD[0],MyActiveD[1])
                        maplist[MyActiveD[1]][MyActiveD[0]].landform = 4
                      
                       
                    elif a.mode == 5:
                        draw_ice(screen,MyActiveD[0],MyActiveD[1])
                        maplist[MyActiveD[1]][MyActiveD[0]].landform = 5

                    elif a.mode == 6:
                        draw_smallmountain(screen,MyActiveD[0],MyActiveD[1])
                        maplist[MyActiveD[1]][MyActiveD[0]].landform = 6
                   
                       
                    elif a.mode == 0:
                        draw_white(screen,MyActiveD[0],MyActiveD[1])
                        maplist[MyActiveD[1]][MyActiveD[0]].landform = 0
                        
        pygame.display.update()
        

def draw_tree(screen,x,y):
    pygame.draw.rect(screen,green,([21+x*30,21+y*30],[29,29]))

def draw_river(screen,x,y):
    pygame.draw.rect(screen,blue,([21+x*30,21+y*30],[29,29]))

def draw_sand(screen,x,y):
    pygame.draw.rect(screen,sand,([21+x*30,21+y*30],[29,29]))

def draw_mountain(screen,x,y):
    pygame.draw.rect(screen,red,([21+x*30,21+y*30],[29,29]))

def draw_ice(screen,x,y):
    pygame.draw.rect(screen,ice,([21+x*30,21+y*30],[29,29]))

def draw_smallmountain(screen,x,y):
    pygame.draw.rect(screen,grey,([21+x*30,21+y*30],[29,29]))

def draw_white(screen,x,y):
    pygame.draw.rect(screen,background,([21+x*30,21+y*30],[29,29]))



def map_set_size():
    fields = ('*长度','*宽度')
    msg = '请输入长度和宽度'
    title = '地图大小设置'
    start = easygui.multenterbox(msg,title,fields)
    if start == None:
        return -1
    else:
        map_size(int(start[0]),int(start[1]))
            

if __name__ == "__main__":
    map_set_size()

