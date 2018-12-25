#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import datetime

from PIL import ImageGrab

import file_manager.file_util
import info.screen_info

path = "./scrapy_photo"
file_manager.file_util.mkdir(path)

def scrapy_screen_all():
    # 参数说明
    # 第一个参数 开始截图的x坐标
    # 第二个参数 开始截图的y坐标
    # 第三个参数 结束截图的x坐标
    # 第四个参数 结束截图的y坐标
    screen = info.screen_info.Screen()
    bbox = (0, 0, screen.get_screen_width(), screen.get_screen_height())
    im = ImageGrab.grab(bbox)
    # 参数 保存截图文件的路径
    now_time = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    save_path = path + "/" + now_time + '.png'
    im.save(save_path.decode('utf-8').encode('gbk'))

def scrapy_screen(x_start,y_start,x_end,y_end, name):
    bbox = (x_start, y_start, x_end, y_end)
    im = ImageGrab.grab(bbox)
    # 参数 保存截图文件的路径
    im.save(path + str(name) + '.png')



