#coding:utf-8
import os
import main_menu
import pygame
import easygui

get = easygui.multenterbox("城墙","设置",("x坐标","y坐标","城墙防御","城墙血量","国家"))
if get[0] != "" and get[1] != "" and get[2] != "" and get[3] != "" and get[4] != "":
    print(1)