#coding:utf-8

import pygame
import sys


pygame.init()
pygame.mixer.init()
size = width,height = 1000,800  #窗口大小

move = 50 #偏移量

color0 = (237,237,237)
color1 = (0,0,0)

# 关卡地图
def draw_map(screen,width,height):
    screen.fill(color0)
    width += 1
    height += 1
    for i in range(width):
        pygame.draw.line(screen,color1,[move,move+i*30],[move+width*30 - 30,move+i*30])
    for i in range(height):
        pygame.draw.line(screen,color1,[move+i*30,move],[move+i*30,move+height*30 - 30])
        # for j in range(N):
            # pygame.draw.rect(screen,color1,[i*30,j*30,30,30],1)


def main(width,height):
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("??")
    draw_map(screen,width,height)
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
if __name__ == "__main__":
    main(20,20)