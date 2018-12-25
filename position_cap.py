
# -*- coding: utf-8 -*-
import win32gui, win32api, win32con
import window_cap
# 获取鼠标当前位置的坐标
win32api.GetCursorPos()
# 将鼠标移动到坐标处
# win32api.SetCursorPos((200, 200))
# # 左点击
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 200, 200, 0, 0)
# win32api.mouse_event(win32con.MUOSEEVENTF_LEFTUP, 200, 200, 0, 0)
# # 获取窗口句柄
# win32gui.FindWindow(None, 'qq')
# win32gui.FindWindow('TXGuiFoundation', None)
# 通过坐标获取窗口句柄
# hw = win32api.fin(win32api.GetCursorPos())
classname = "MainForm"
title = "丰声".decode("utf-8")
hwnd = win32gui.FindWindow(classname, title)

# 获取窗口classname
print(str(win32gui.GetClassName(hwnd)))
# # 获取窗口坐标
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
# 获取窗口标题
print("left: " + str(left) + " top: " + str(top) + " right: " + str(right) + " bottom: " + str(bottom))

hwndlist = []
hwndlist.append(hwnd)
window_cap.pprint(window_cap.demo_child_windows(hwndlist))