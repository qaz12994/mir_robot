import sys

import numpy as np
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # pg.plot(x=[0, 1, 2, 3], y=[4, 5, 9, 6])
    pg.image(np.arange(3600).reshape((60, 60)))
    status = app.exec_()
    sys.exit(status)
