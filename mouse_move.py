import os
import time
import ctypes
import random


class Cursor(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]


def random_mouse_move_windows(interval: int = 30, duration: int = 8):
    cur = Cursor()
    ctypes.windll.user32.GetCursorPos(ctypes.byref(cur))

    max_width = ctypes.windll.user32.GetSystemMetrics(0)
    max_height = ctypes.windll.user32.GetSystemMetrics(1)

    x_move = max_width // 100
    y_move = max_height // 100

    next_x = cur.x
    next_y = cur.y

    for i in range(duration * 60 * 30 // interval):
        next_x = max(
            min(next_x + random.randint(-x_move, x_move), max_width), 0)
        next_y = max(
            min(next_y + random.randint(-y_move, y_move), max_height), 0)
        ctypes.windll.user32.SetCursorPos(next_x, next_y)
        ctypes.windll.user32.mouse_event(0x0008, next_x, next_y, 0, 0)
        ctypes.windll.user32.mouse_event(0x0010, next_x, next_y, 0, 0)
        print(f'current pos = x:{next_x} y:{next_y}')
        time.sleep(interval)


if os.name == 'nt':
    random_mouse_move_windows()
