#coding:utf-8

import pygame
import pickle
from PIL import Image
import sys

class JButton():
    def __init__(self,vertex,mouse_image_filename):
        self.vertex = vertex                        #鼠标顶点
        img = Image.open(mouse_image_filename)      #获取宽度，高度
        self.width,self.height = img.size
        self.mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()

    def set_position(self):                         #设置位置
        screen.

