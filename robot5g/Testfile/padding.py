from itertools import cycle, islice

import matplotlib.pyplot as plt
import numpy as np

from Utils.Vector import vector
from Utils.Inpolygon import inpolygon

if __name__ == '__main__':
    # x = [0, 1, 1, 0]
    # y = [0, 0, 1, 1]
    pad_size = 0.45

    x = [0.5, 9.5, 9.5, 12.5, 12.5, 22.5, 22.5, 8.5, 8.5, 9.5, 9.5, 22.5, 22.5, 9.5, 9.5, 8.5, 8.5, 0.5, 0.5, 3.5,
         3.5, 0.5]
    y = [0.5, 0.5, 2.5, 2.5, 0.5, 0.5, 7.5, 7.5, 10.5, 10.5, 8.5, 8.5, 13.5, 13.5, 11.5, 11.5, 13.5, 13.5, 8.5, 8.5,
         2.5, 2.5]



    x_pre = islice(cycle(x), 1, 1 + len(x))
    y_pre = islice(cycle(y), 1, 1 + len(y))
    x_next = islice(cycle(x), len(x) - 1, 2 * len(x) - 1)
    y_next = islice(cycle(y), len(y) - 1, 2 * len(x) - 1)

    px = []
    py = []
    inin = lambda p: inpolygon(p[0], p[1], x, y)

    for xp, yp, xx, yy, xn, yn in zip(x_pre, y_pre, x, y, x_next, y_next):
        point = np.array([xx, yy])
        v1 = vector.from_point(xp, yp, xx, yy)
        v2 = vector.from_point(xx, yy, xn, yn)
        meta = v1.unit_vector() + v2.unit_vector()

        # if vector.cos(to_mid, meta.normal_vector_x()) > 0:
        #     angular_bisector = meta.normal_vector_x().unit_vector()
        # else:
        #     angular_bisector = meta.normal_vector_y().unit_vector()

        if inin(point + pad_size * meta.normal_vector_x().unit_vector().v):
            angular_bisector = meta.normal_vector_x().unit_vector()
        else:
            angular_bisector = meta.normal_vector_y().unit_vector()

        pad = pad_size / vector.sin(v1, angular_bisector)
        pad_point = point + pad * angular_bisector.v
        px.append(pad_point[0])
        py.append(pad_point[1])

    x.append(x[0])
    y.append(y[0])
    px.append(px[0])
    py.append(py[0])
    plt.plot(x, y)
    plt.plot(px, py)
    plt.savefig('padding')
    plt.show()
