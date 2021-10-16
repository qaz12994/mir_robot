import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from Node.Painter import colormap

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # Make data.
    Y, X = np.mgrid[-5:5:0.01, -5:5:0.01]
    # Z = norm.pdf(np.sqrt(X ** 2 + Y ** 2), scale=0.5)
    Z = np.exp(-X ** 2 - Y ** 2)
    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=colormap,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()
