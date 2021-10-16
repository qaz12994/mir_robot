"""
本程式目的：
1. 新建任務(control.py)
2. 執行任務(crawler.py)
"""
import control
import crawler
from Node.PathPlanner.CoverageCost_Lai import plan
from Node import PolygonFiller, MissionPoster, PolygonPadding

import sys
sys.path.append('~/mir_robot_ws/src/mir_robot/robot5g')

if __name__ == '__main__':
    gap = 0.15

    # 圈出可以走的範圍
    area = control.circle()

    # 內縮
    padding_area = PolygonPadding.padding(area, 0.45)

    # 將內縮好的地圖切割
    points = PolygonFiller.fill(padding_area, gap)

    # 路徑規劃
    path = plan(points)

    missionID = MissionPoster.post(path)

    crawler.crawl(missionID, gap)
