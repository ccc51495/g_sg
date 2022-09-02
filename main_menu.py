#coding:utf-8

import pygame
import pickle
from PIL import Image
import sys
import os

background = (237,237,237)
black = (0,0,0)
green = (0,255,0)
blue = (0,0,255)
sand = (255,235,205)
red = (255,0,0)
DEFAULT_SIZE = [1000,800]

screen = pygame.display.set_mode(DEFAULT_SIZE)
screen.fill(background)

ButtonDict1 = {}#主菜单
ButtonDict2 = {}#战役菜单
ButtonDict3 = {}#战役菜单1-
ButtonDict4 = {}#战役菜单2-
ButtonDict5 = {}#战役菜单3-
ButtonDict6 = {}#战役菜单4-
ButtonDict7 = {}#战役菜单5-
ButtonDict8 = {}#战役菜单6-
ButtonDict9 = {}#战役菜单7-
ButtonDict10 = {}#将军菜单

class Map():
    def draw_map(self,screen,width,height):
        screen.fill(background)
        width += 1
        height += 1
        for i in range(width):
            pygame.draw.line(screen,black,[20,20+i*30],[20+height*30 - 30,20+i*30])
        for i in range(height):
            pygame.draw.line(screen,black,[20+i*30,20],[20+i*30,20+width*30 - 30])

    def draw_tree(self,screen,x,y):
        pygame.draw.rect(screen,green,([21+x*30,21+y*30],[29,29]))

    def draw_river(self,screen,x,y):
        pygame.draw.rect(screen,blue,([21+x*30,21+y*30],[29,29]))

    def draw_sand(self,screen,x,y):
        pygame.draw.rect(screen,sand,([21+x*30,21+y*30],[29,29]))

    def draw_mountain(self,screen,x,y):
        pygame.draw.rect(screen,red,([21+x*30,21+y*30],[29,29]))

    

    def main(self,width,height):
        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("??")
        draw_map(screen,width,height)
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                


class Button():
    global ButtonDict1
    ButtonDict1 = {}
    def __init__(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(100,70))
        ButtonDict1[button_name] = [self.vertex,(self.vertex[0] + 100,self.vertex[1] + 70)]
        screen.blit(self.paint,self.vertex)

    def add_new(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(100,70))
        ButtonDict1[button_name] = [self.vertex,(self.vertex[0] + 100,self.vertex[1] + 70)]
        screen.blit(self.paint,self.vertex)

    def button_a_click(self):
        screen.fill(background)
        zhanyi_main()

    def button_b_click(self):
        print(5)

    def button_c_click(self):
        screen.fill(background)
        jiang_main()
    
    def button_d_click(self):
        pass

    def button_quit_click(self):
        pygame.quit()
        sys.exit()


class zhanyi(Button):
    global ButtonDict2
    ButtonDict2 = {}
    def __init__(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(180,100))
        ButtonDict2[button_name] = [self.vertex,(self.vertex[0] + 180,self.vertex[1] + 100)]
        screen.blit(self.paint,self.vertex)

    def add_new(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(180,100))
        ButtonDict2[button_name] = [self.vertex,(self.vertex[0] + 180,self.vertex[1] + 100)]
        screen.blit(self.paint,self.vertex)

    def button_a_click(self):
        screen.fill(background)
        zhanyi_1_main()

    def button_b_click(self):
        print(2)

    def button_c_click(self):
        pass
        
    def button_d_click(self):
        pass

    def button_e_click(self):
        pass

    def button_f_click(self):
        pass

    def button_g_click(self):
        pass

    def button_return_click(self):
        screen.fill(background)
        menu_main()
        
class Jiangjun(Button):
    global ButtonDict10
    number = 0
    ButtonDict10 = {}
    def __init__(self,name,picture,button_name):
        
        self.name = name
        self.img = pygame.image.load(picture).convert_alpha()
        self.img = pygame.transform.scale(self.img,(40,60))
        x = self.number % 15
        y = (self.number - x)/ 15
        screen.blit(self.img,(40+x*50,40+y*70))
        ButtonDict10[button_name] = [(40+x*50,40+y*70),(80+x*50,100+y*70)]
        self.number += 1

    def add_new(self,name,picture,button_name):
        
        self.name = name
        self.img = pygame.image.load(picture).convert_alpha()
        self.img = pygame.transform.scale(self.img,(40,60))
        x = self.number % 15
        y = (self.number - x)/ 15
        screen.blit(self.img,(40+x*50,40+y*70))
        ButtonDict10[button_name] = [(40+x*50,40+y*70),(80+x*50,100+y*70)]
        self.number += 1


class zhanyi1(Button):#战役界面1
    global ButtonDict3
    ButtonDict3 = {}
    def __init__(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(180,50))
        ButtonDict3[button_name] = [self.vertex,(self.vertex[0] + 180,self.vertex[1] + 50)]
        screen.blit(self.paint,self.vertex)

    def add_new(self,vertex,image_position,button_name):
        self.vertex = vertex
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(180,50))
        ButtonDict3[button_name] = [self.vertex,(self.vertex[0] + 180,self.vertex[1] + 50)]
        screen.blit(self.paint,self.vertex)
    
    def button_a_click(self):
        height0 = 20
        width0 = 20
        # maplist = [[Map_information() for i in range(height0)] for j in range(width0)]
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

    def button_b_click(self):
        pass

    def button_c_click(self):
        pass

    def button_d_click(self):
        pass

    def button_return_click(self):
        screen.fill(background)
        zhanyi_main()

# ButtonDict = {'button1':[(40,40),(140,110)],'button2':[(40,120),(140,190)]}

def Button_click1(x,y):#主菜单
    for mykey in ButtonDict1.keys():
        if x in range(ButtonDict1[mykey][0][0],ButtonDict1[mykey][1][0]) \
            and y in range(ButtonDict1[mykey][0][1],ButtonDict1[mykey][1][1]):
            return mykey
            
def Button_click2(x,y):#战役菜单
    for mykey in ButtonDict2.keys():
        if x in range(ButtonDict2[mykey][0][0],ButtonDict2[mykey][1][0]) \
            and y in range(ButtonDict2[mykey][0][1],ButtonDict2[mykey][1][1]):
            return mykey

def Button_click3(x,y):#战役1菜单
    for mykey in ButtonDict3.keys():
        if x in range(ButtonDict3[mykey][0][0],ButtonDict3[mykey][1][0]) \
            and y in range(ButtonDict3[mykey][0][1],ButtonDict3[mykey][1][1]):
            return mykey

def menu_main():

    pygame.init()
    pygame.mixer.init()
    screen.fill(background)
    
    a = Button((40,40),"image/2.bmp","a")
    b = a.add_new((40,120),"image/3.bmp","b")
    c = a.add_new((40,200),"image/4.bmp","c")
    d = a.add_new((40,280),"image/5.bmp","d")
    e = a.add_new((600,40),"image/1.bmp","quit")
    pygame.display.flip()

    while True:
        x,y = pygame.mouse.get_pos()
        MyActiveC = Button_click1(x,y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if MyActiveC:
                if event.type == pygame.KEYDOWN:
                    print(MyActiveC)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    exec("a.button_{}_click()".format(MyActiveC))
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
        pygame.display.update()
        
def jiang_main():
    pygame.init()
    pygame.mixer.init()
    
    pygame.display.flip()

    number_01 = Jiangjun("曹操","picture/曹操.bmp","001")
    number_02 = number_01.add_new('郭嘉','picture/郭嘉.bmp',"002")
    number_03 = number_01.add_new('许褚','picture/许褚.bmp',"003")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

def zhanyi_main():
    
    pygame.init()
    pygame.mixer.init()
    
    a = zhanyi((20,20),"image/a1.bmp","a")
    b = a.add_new((20,130),"image/a2.bmp","b")
    c = a.add_new((20,240),"image/a3.bmp","c")
    d = a.add_new((20,350),"image/a4.bmp","d")
    e = a.add_new((20,460),"image/a5.bmp","e")
    f = a.add_new((20,570),"image/a6.bmp","f")
    g = a.add_new((20,680),"image/a7.bmp","g")
    r = a.add_new((800,20),"image/0.bmp","return")

    
    pygame.display.flip()

    while True:
        x,y = pygame.mouse.get_pos()
        MyActiveC = Button_click2(x,y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if MyActiveC:
                
                if event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    exec("a.button_{}_click()".format(MyActiveC))
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
        pygame.display.update()

def zhanyi_1_main():
    pygame.init()
    pygame.mixer.init()
    
    a = zhanyi1((20,20),"image/a11.bmp","a")
    b = a.add_new((20,80),"image/a12.bmp","b")
    c = a.add_new((20,140),"image/a13.bmp","c")
    d = a.add_new((20,200),"image/a14.bmp","d")
    r = a.add_new((800,20),"image/0.bmp","return")
    pygame.display.flip()

    while True:
        x,y = pygame.mouse.get_pos()
        MyActiveC = Button_click3(x,y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if MyActiveC:
                
                if event.type == pygame.KEYDOWN:
                    pass
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    exec("a.button_{}_click()".format(MyActiveC))
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
        pygame.display.update()


if __name__ == "__main__":
    menu_main()