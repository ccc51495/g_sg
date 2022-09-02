#coding:utf-8

import pygame
import sys
import pickle
from PIL import Image



color = (237,237,237)
screen = pygame.display.set_mode((1000,800))
screen.fill(color)


class Jiangjun():
    number = 0
    def __init__(self,name,picture):
        
        self.name = name
        self.img = pygame.image.load(picture).convert_alpha()
        self.img = pygame.transform.scale(self.img,(40,60))
        x = self.number % 15
        y = (self.number - x)/ 15
        screen.blit(self.img,(40+x*50,40+y*70))
        
        self.number += 1

    def add_new(self,name,picture):
        
        self.name = name
        self.img = pygame.image.load(picture).convert_alpha()
        self.img = pygame.transform.scale(self.img,(40,60))
        x = self.number % 15
        y = (self.number - x)/ 15
        screen.blit(self.img,(40+x*50,40+y*70))
        
        self.number += 1
    



def jiang_main():
    pygame.init()
    pygame.mixer.init()
    
    pygame.display.flip()

    number_01 = Jiangjun("曹操","picture/曹操.bmp")
    number_02 = number_01.add_new('郭嘉','picture/郭嘉.bmp')
    number_03 = number_01.add_new('许褚','picture/许褚.bmp')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

if __name__ == "__main__":
    
    
    
    jiang_main()