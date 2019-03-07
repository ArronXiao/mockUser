# -*- coding: utf-8 -*-
import win32gui
import win32api
import sys
import time

import win32clipboard as w
import win32con

hwnd_title = dict()


def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        print"************************"
        info = u'title: ' + win32gui.GetWindowText(hwnd).decode("gbk") + u'   类名:  ' + win32gui.GetClassName(hwnd)
        hwnd_title.update({hwnd: info})
        if win32gui.GetWindowText(hwnd).decode("gbk") == u'胡强力':
            active_window(hwnd)


def get_child_windows(parent):
    '''
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    print"--------------- parent", parent
    hwndChildList = []
    # win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)
    return hwndChildList


def active_window(hwnd):
    print"--------------- 激活窗口： ", hwnd
    win32gui.SetForegroundWindow(hwnd)
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(39, 61))
    time.sleep(1)
    # win32api.PostMessage(hwnd, win32con.WM_LBUTTONDOWN, 0, win32api.MAKELONG(39, 61))
    # win32api.PostMessage(hwnd, win32con.WM_LBUTTONUP, 0, win32api.MAKELONG(39, 61))
    # win32gui.SendMessage(hwnd, win32con.WM_SETTEXT, 0, u"我真实日了够了哟".encode("gbk"))
    for num in range(1, 1000):
        mySendMessage(hwnd, "this is a test message! " + str(num))
        time.sleep(0.1)


def test():
    qqhd = 0x00151A28
    # qqhd = 0x001004B4
    active_window(qqhd)


def testForChinse(messageStr):
    hwnd = 0x001004B4
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    for msg in messageStr:
        myBytes = bytearray(msg.encode("gbk"))
        print myBytes[0], myBytes[1]
        win32api.SendMessage(hwnd, win32con.WM_CHAR, myBytes[0], 1)
        win32api.SendMessage(hwnd, win32con.WM_CHAR, myBytes[1], 1)

def testForChinseForEnd(messageStr):
    hwnd = 0x001A1A96
    # hwnd = 0x001004B4
    # win32gui.SetForegroundWindow(hwnd)
    for msg in messageStr:
        myBytes = bytearray(msg.encode("gbk"))
        for num in range(0, len(myBytes)):
            win32api.SendMessage(hwnd, win32con.WM_CHAR, myBytes[num], 1)
    #不知道为啥这么操蛋，需要使用postMessage,在这里send是不行的，总算是实现了后台的enter
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def mySendMessage(hwnd, message):
    sendText = message;
    for letter in sendText:
        win32api.SendMessage(hwnd, win32con.WM_CHAR, ord(letter), 1)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


# 设置剪贴板文本
def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


def getHwndByTitle(title):
    print("")


# win32gui.EnumWindows(get_all_hwnd, 0)
#
# for h, t in hwnd_title.items():
#     if t is not "":
#         print h,"            ",t.encode("utf-8")
# setText(u"你好啊")
# qqhd = 0x00151A28
# # qqhd = 0x001004B4
# active_window(qqhd)
# win32gui.SendMessage(qqhd,258,22,0)
# win32gui.SendMessage(qqhd,770,0,0)
testForChinseForEnd(u"这是一条很不容易的数据哟 难得")