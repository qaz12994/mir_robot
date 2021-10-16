import time

import matplotlib.pyplot as plt
import numpy as np
from drawnow import drawnow

# from Node.PANITER import colormap

## test data
gap = 0.2
error = 0
step = gap - error
# step = 1 - (gap * error)/100
edge = 1.5

y, x = np.mgrid[-edge:edge:step, -edge:edge:step]
x = x.flatten()
y = y.flatten()
data = - (x ** 2 + y ** 2) * 10
plt.ion()


# fig = plt.figure()
# plt.show()

def make_fig():
    plt.scatter(xx, yy, c=dd, vmin=-40, vmax=-1, s=300, cmap='RdYlBu_r')  # I think you meant this
    plt.colorbar()



xx, yy, dd = [], [], []
# sc = plt.scatter(xx, yy, c=dd, vmin=-40, vmax=-1, s=300)
# plt.colorbar(sc)
# plt.show()

for _x, _y, _d in zip(x, y, data):
    s = time.time()
    xx.append(_x)
    yy.append(_y)
    dd.append(_d)
    # fig.clear()
    # sc = plt.scatter(xx, yy, c=dd, vmin=-40, vmax=-1, s=300)
    # plt.pause(0.1)
    # # plt.colorbar(sc)
    # plt.show()
    drawnow(make_fig)
    print(time.time() - s)

plt.waitforbuttonpress()
