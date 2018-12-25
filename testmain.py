#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import info.compute_info
import scrapy_screen
import win32com
import photo_match
# scrapy_screen.scrapy_screen_all()
position = photo_match.matchImg("./scrapy_photo/2018_12_25_16_30_17.png","./scrapy_photo/target.png")
x,y = position['result']
print("result: x: " + str(x) + " y: " + str(y))
print(position)

#
# position2 = photo_match.matchImg("./scrapy_photo/2018_12_25_16_14_17.png","./scrapy_photo/target2.png")
# x,y = position2['result']
# print("result: x: " + str(x) + " y: " + str(y))
# print(position2)

print("你好")
