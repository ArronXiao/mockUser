#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
from PIL import Image
def image_grey_operate(src):
    img = Image.open(src)
    Img = img.convert('L')
    Img.save("./scrapy_photo/2018_12_25_16_30_17_1.png")
    threshold = 200
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    photo = Img.point(table, "1")
    photo.save("./scrapy_photo/2018_12_25_16_30_17_2.png")

