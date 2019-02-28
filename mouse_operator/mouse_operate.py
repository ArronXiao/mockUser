# -*- coding: utf-8 -*-
import win32api, win32gui, win32con  # 导入win32api相关模块

self = 'SE_SogouExplorerFrame'  # 窗口的类名
hwnd = win32gui.FindWindow(self, None)  # 通过窗口类名获取窗口句柄
# send key
win32api.PostMessage(hwnd, win32con.WM_MOUSEMOVE, win32con.VK_F9, 0)  # 发送F9键
win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_F9, 0)
