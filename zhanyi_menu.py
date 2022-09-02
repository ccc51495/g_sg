#coding:utf-8

import pygame
import pickle
from PIL import Image
import sys

DEFAULT_SIZE = [1000,800]
color = (237,237,237)
screen = pygame.display.set_mode(DEFAULT_SIZE)
screen.fill(color)
ButtonDict = {}

class Button():
    def __init__(self,vertex,image_position,button_name):
        self.vertex = vertex
        
        
        self.paint = pygame.image.load(image_position).convert_alpha()
        self.paint = pygame.transform.scale(self.paint,(180,100))
        ButtonDict[button_name] = [self.vertex,(self.vertex[0] + 180,self.vertex[1] + 110)]
        screen.blit(self.paint,self.vertex)

def button_a_click():
    print(1)

def button_b_click():
    print(2)

def button_c_click():
    pass
    
def button_d_click():
    pass

def button_e_click():
    pass

def button_f_click():
    pass

def button_g_click():
    pass

def button_return_click():
    
    print(1)


# ButtonDict = {'button1':[(40,40),(140,110)],'button2':[(40,120),(140,190)]}

def Button_click(x,y):
    for mykey in ButtonDict.keys():
        if x in range(ButtonDict[mykey][0][0],ButtonDict[mykey][1][0]) \
            and y in range(ButtonDict[mykey][0][1],ButtonDict[mykey][1][1]):
            return mykey


def zhanyi_main():
    
    pygame.init()
    pygame.mixer.init()
    
    a = Button((20,20),"image/a1.bmp","a")
    b = Button((20,130),"image/a2.bmp","b")
    c = Button((20,240),"image/a3.bmp","c")
    d = Button((20,350),"image/a4.bmp","d")
    e = Button((20,460),"image/a5.bmp","e")
    f = Button((20,570),"image/a6.bmp","f")
    g = Button((20,680),"image/a7.bmp","g")
    r = Button((800,20),"image/0.bmp","return")


    # a:战役 b:传奇 c:点将台 d:征服

    # ButtonDict["a"] = [(40,40),(140,110)]
    # ButtonDict["b"] = [(40,120),(140,190)]
    # ButtonDict["c"] = [(40,200),(140,270)]
    # ButtonDict["d"] = [(40,280),(140,350)]
    
    
    
    pygame.display.flip()

    while True:
        x,y = pygame.mouse.get_pos()
        MyActiveC = Button_click(x,y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if MyActiveC:
                if event.type == pygame.KEYDOWN:
                    print(MyActiveC)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    exec("button_{}_click()".format(MyActiveC))
                elif event.type == pygame.MOUSEMOTION:
                    pass
                elif event.type == pygame.MOUSEBUTTONUP:
                    pass
        pygame.display.update()
        

if __name__ == "__main__":
    zhanyi_main()