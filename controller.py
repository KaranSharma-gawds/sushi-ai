import win32con, win32api
from coordinates import Coordinates
import time
def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print('left clicked')
    time.sleep(0.1)

def left_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    print('left down')

def left_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    time.sleep(0.1)
    print('left up')

def mousePos(cord):
    win32api.SetCursorPos((Coordinates.x_pad+cord[0], Coordinates.y_pad+cord[1]))

def mouse_click(cord):
    mousePos(cord)
    time.sleep(0.1)
    left_click()
def getCords():
    x,y = win32api.GetCursorPos()
    x = x - Coordinates.x_pad
    y = y - Coordinates.y_pad
    return (x,y)
