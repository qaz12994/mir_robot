import matplotlib.pyplot as plt

from Node import PolygonFiller, PolygonPadding
from Node.PathPlanner.NoPlan import plan

if __name__ == '__main__':
    x = [0.5, 9.5, 9.5, 12.5, 12.5, 22.5, 22.5, 8.5, 8.5, 9.5, 9.5, 22.5, 22.5, 9.5, 9.5, 8.5, 8.5, 0.5, 0.5, 3.5,
         3.5, 0.5]
    y = [0.5, 0.5, 2.5, 2.5, 0.5, 0.5, 7.5, 7.5, 10.5, 10.5, 8.5, 8.5, 13.5, 13.5, 11.5, 11.5, 13.5, 13.5, 8.5, 8.5,
         2.5, 2.5]

    gap = 0.5

    padding_area = PolygonPadding.padding((x, y), 0.45)

    points = PolygonFiller.fill(padding_area, gap)

    psx, psy, psin = points

    px, py = plan(points)

    x.append(x[0])
    y.append(y[0])

    plt.plot(x, y)
    plt.scatter(px, py)
    plt.show()
    print(psin)
