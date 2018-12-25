#!/usr/bin/python2.6
# -*- coding: utf-8 -*-
import wx
from win32api import GetSystemMetrics
import win32con

# os.makedirs('d:/z/z/z/z')
# os.rename("d:/zz.bmp" , "d:/z/z/z/z/z.bmp")

class Screen():
    def __init__(self):
        print ""

    def get_screen_width(self):
        return GetSystemMetrics(win32con.SM_CXSCREEN)

    def get_screen_height(self):
        return GetSystemMetrics(win32con.SM_CYSCREEN)
