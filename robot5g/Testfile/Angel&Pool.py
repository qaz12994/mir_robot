from Utils import timeit
from Utils.Vector import angle
from multiprocessing import Pool
if __name__ == '__main__':
    # x = list(range(25881))
    # y = list(range(25881))
    x = list(range(999))*999
    y = list(range(999))*999
    x_next = x.copy()
    y_next = y.copy()
    x_next.append(x_next.pop(0))
    y_next.append(y_next.pop(0))
    with timeit(), Pool() as p:
        p.starmap(angle, zip(x, y, x_next, y_next))

    with timeit():
        list(map(angle, x, y, x_next, y_next))
