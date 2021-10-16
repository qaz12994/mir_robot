"""
本程式目的：
1. 執行已建立任務
2. 掃描製作地圖
"""
from time import sleep

from drawnow import drawnow
from matplotlib import pyplot as plt

from Config.colorbar import *
from Node import DataSaver, Painter
from Node.Painter import colormap
from Robot import Status
from Robot.Mission import queue
from Robot.Status import state
from Sensors.u2063xa.lib import device
from Utils import timeit, root_path
from Utils.Alert import PLAY_mission_completed
from Utils.Map2d import signal_map
from Utils.Statistical import min_error as function

# list of data
x, y, data = [], [], []

# 即時繪圖
def make_fig():
    plt.scatter(x, y, c=data, vmin=vmin, vmax=vmax, s=300, cmap=colormap)


def crawl(mission_id, gap):
    # init
    Measuring = True

    # set mission
    state.setReady()
    queue.DELETE()
    queue.POST(mission_id)
    sleep(1)
    # 計算測量時間、初始化儀控
    with timeit(), device() as sensor:  # init sensor
        # run
        while Measuring:
            power = sensor.read_power()
            bot = Status.GET()
            if bot.Success():
                bot_y, bot_x = bot.position()
                y.append(bot_y)
                x.append(bot_x)
                data.append(power)
                Measuring = bot.state_id() == state.Executing
                print(f'({x[-1]:.3f}, {y[-1]:.3f}): {data[-1]:.3f}')
                drawnow(make_fig)  # 即時繪圖

    # 警告任務完成
    PLAY_mission_completed()

    # 建立熱圖用2d陣列
    map2d = signal_map.map2darray(y, x, data, gap, error_function=function)

    # 建立儲存資料夾
    path = root_path()

    # 繪製熱圖
    Painter.heatmap(path, map2d)

    # 儲存檔案
    DataSaver.map(path, map2d)  # 2d陣列
    DataSaver.map_original_data(path, y, x, data)  # 原始x, y, data資料
    plt.waitforbuttonpress()


if __name__ == '__main__':
    from Robot.Mission import GET

    # 取得任務列表
    missions = GET()
    dict_mission = {m.name(): m.guid() for m in missions.array()}
    mission_ID = None
    # 詢問要執行何任務
    while mission_ID is None:
        try:
            mission_ID = dict_mission[input('mission name: ')]
        except KeyError:
            print('No Such Mission!')
    # 執行任務
    crawl(mission_ID, 0.1)
