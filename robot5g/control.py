"""
本程式目的：
1. 使用搖桿控制Mir100
2. 踩點圈出可走範圍
"""
import sys
import webbrowser

import pyautogui
import pygame
from drawnow import drawnow
from matplotlib import pyplot as plt
# 可更換搖桿模組
from Config.controller.GameSir_G3s import config
# 不同電腦的滑鼠的位置
from Config.web_joy_position import GET_joy_position
from Robot import Address
from Robot.Status import GET
from Robot.Status.state import joystick_control
from Utils.Alert import PLAY_select

# 取得滑鼠位置
web_joy = GET_joy_position()
y, x = [], []


# 初始化搖桿
def init_joy() -> 'pygame.joystick.JoystickType':
    pygame.init()
    pygame.joystick.init()
    last = pygame.joystick.get_count() - 1  # return搖桿的數量
    try:
        # 創建新的搖桿
        joysticks = pygame.joystick.Joystick(last)
        joysticks.init()
        return joysticks
    except pygame.error:
        print('No Joysticks!!!')
        sys.exit()


def make_fig():
    plt.plot(x, y)


def circle():
    # region
    # init
    clock = pygame.time.Clock()
    gameExit = False
    joystick = init_joy()
    x.clear()
    y.clear()

    # open control panel
    joystick_control()
    webbrowser.open(Address)  # 開啟網頁
    pyautogui.moveTo(web_joy)  # 將滑鼠移動到初始位置
    # endregion
    # loop
    while not gameExit:
        pygame.event.get()
        """
        this is very important!
        put this function in loop
        """
        pyautogui.mouseDown()
        dx, dy = 0, 0
        clock.tick(60)  # 運行速度不超過60幀

        # start: end of catching the point
        gameExit = joystick.get_button(config['exit'])

        # select point
        if joystick.get_button(config['select']):
            py, px = GET().position()
            y.append(py)
            x.append(px)
            PLAY_select()
            drawnow(make_fig)
            print(px, py)

        # button
        # get_button(button) -> bool
        for button, (wx, wy) in config['button'].items():
            dx += joystick.get_button(button) * wx
            dy += joystick.get_button(button) * wy

        # HAT
        # get_hat(hat_number) -> x, y
        for hat, (wx, wy) in config['hat'].items():
            hat_x, hat_y = joystick.get_hat(0)
            dx += hat_x * wx
            dy += hat_y * wy

        # AXIS
        # get_axis(axis_number) -> float
        for axis, (wx, wy) in config['axis'].items():
            dx += joystick.get_axis(axis) * wx
            dy += joystick.get_axis(axis) * wy

        # normalize
        rate = max(dx, dy, 1)
        scale = rate if rate > 100 else 100
        dx = dx / scale * 60
        dy = dy / scale * 60

        # drag Mouse pointer
        pyautogui.dragTo(web_joy.x + dx, web_joy.y + dy, mouseDownUp=False)

    pyautogui.mouseUp()
    pygame.quit()
    return x, y


if __name__ == '__main__':
    xx, yy, = circle()
    print(xx)
    print(yy)
