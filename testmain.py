#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import image_handle.image_grey
# scrapy_screen.scrapy_screen_all()
# position = photo_match.matchImg("./scrapy_photo/2018_12_25_16_30_17.png","./scrapy_photo/target.png")
# x,y = position['result']
# print("result: x: " + str(x) + " y: " + str(y))
# print(position)
#
# #
# position2 = photo_match.matchImg("./scrapy_photo/2018_12_25_16_14_17.png","./scrapy_photo/target2.png")
# x,y = position2['result']
# print("result: x: " + str(x) + " y: " + str(y))
# print(position2)
image_handle.image_grey.image_grey_operate("./scrapy_photo/2018_12_25_16_30_17.png")
print("你好")
