# -*- coding: utf-8 -*-
import win32gui
import win32api
import sys
import time

import win32con

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        print"************************"
        info = u'title: ' + win32gui.GetWindowText(hwnd).decode("gbk") + u'   类名:  ' + win32gui.GetClassName(hwnd)
        hwnd_title.update({hwnd: info})
        if win32gui.GetWindowText(hwnd).decode("gbk") == u'丰声':
            active_window(hwnd)

def get_child_windows(parent):
    '''
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    print"--------------- parent",parent
    hwndChildList = []
    # win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList

def active_window(hwnd):
    print"--------------- 激活窗口： ", hwnd
    # win32gui.SetForegroundWindow(hwnd)
    # win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(39, 61))
    time.sleep(1)
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, win32api.MAKELONG(39, 61))
    win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(39, 61))

def getHwndByTitle(title):
    print("")

win32gui.EnumWindows(get_all_hwnd, 0)

for h, t in hwnd_title.items():
    if t is not "":
        print h,"            ",t.encode("utf-8")