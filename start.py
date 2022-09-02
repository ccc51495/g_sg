#coding:utf-8

import pygame
import Game
import sys
import easygui as g

map1=[]
map2=[]
n=0
zhanghao=0
zhanghao_list=[]


#登录界面
def login(zhanghao_list):
    global n,map1,map2,zhanghao
    fields = ('name:','password')
    msg = '请输入用户名和密码'
    title='login'
    yonghu = g.multpasswordbox(msg,title,fields)

    if yonghu == None:
        return -1 #'取消登录'
    elif yonghu == ["",""]:
        button_choices = g.buttonbox("以游客身份登录",'无账号登录',choices=("确定","注册"))
        if button_choices == "确定":
            return 2
        elif button_choices == "注册":
            return 1
    else:
        list1 = []
        with open ('user/zhanghao.txt','r',encoding="utf-8") as ZhangHao:
            for each_line in ZhangHao:
                (zhang_hao,huanhang) = each_line.split('\n')
                list1.append(zhang_hao)

        list2 = []
        with open ('user/mima.txt','r',encoding="utf-8") as MiMa:
            for each_line in MiMa:
                (mi_ma,huanhang) = each_line.split('\n')
                list2.append(mi_ma)


        for x in list1:
            if x == str(yonghu[0]) and list2[list1.index(x)] == str(yonghu[1]):
                g.msgbox(str(yonghu[0]) + 'welcome',ok_button='开始')
                zhanghao = list1.index(x)
                return 2
                break
            elif x == str(yonghu[0]) and list2[list1.index(x)] != str(yonghu[1]):
                g.msgbox("用户名或密码错误",ok_button="确定")
                return 0
                break

        if str(yonghu[0]) not in list1:
            g.msgbox("用户名或密码错误",ok_button="确定")
            return 0
            

def zhuce():
    values = []


if __name__ == "__main__":

    x = 0
    while x == 0:
        x = login(zhanghao_list)
    if x == 2:
        Game.main(20,20)