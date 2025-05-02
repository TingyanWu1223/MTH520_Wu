# matplotlib_intro.py
"""Python Essentials: Intro to Matplotlib.
<Name>Tingyan
<Class> Mth520
<Date>5.2.2025
"""

import numpy as np
from matplotlib import pyplot as plt

# Problem 1
def var_of_means(n):
    """ Create an (n x n) array of values randomly sampled from the standard
    normal distribution. Compute the mean of each row of the array. Return the
    variance of these means.

    Parameters:
        n (int): The number of rows and columns in the matrix.

    Returns:
        (float) The variance of the means of each row.
    """
    A = np.random.randn(n, n)
    row_means = np.mean(A, axis=1)
    return np.var(row_means)

def prob1():
    """ Create an array of the results of var_of_means() with inputs
    n = 100, 200, ..., 1000. Plot and show the resulting array.
    """
    ns = np.arange(100, 1001, 100)          # n = 100, 200, ..., 1000
    results = np.array([var_of_means(n) for n in ns])

    plt.plot(ns, results, marker='o')
    plt.title("Variance of Row Means vs. n")
    plt.xlabel("n (size of matrix)")
    plt.ylabel("Variance of row means")
    plt.grid(True)
    plt.show()


# Problem 2
def prob2():
    """ Plot the functions sin(x), cos(x), and arctan(x) on the domain
    [-2pi, 2pi]. Make sure the domain is refined enough to produce a figure
    with good resolution.
    """
    x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)

    plt.plot(x, np.sin(x), label="sin(x)")
    plt.plot(x, np.cos(x), label="cos(x)")
    plt.plot(x, np.arctan(x), label="arctan(x)")

    plt.title("Plot of sin(x), cos(x), and arctan(x)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()


# Problem 3
def prob3():
    """ Plot the curve f(x) = 1/(x-1) on the domain [-2,6].
        1. Split the domain so that the curve looks discontinuous.
        2. Plot both curves with a thick, dashed magenta line.
        3. Set the range of the x-axis to [-2,6] and the range of the
           y-axis to [-6,6].
    """
    x1 = np.linspace(-2, 0.99, 500)
    x2 = np.linspace(1.01, 6, 500)

    y1 = 1 / (x1 - 1)
    y2 = 1 / (x2 - 1)

    plt.plot(x1, y1, 'm--', lw=4, label="f(x) = 1 / (x - 1)")
    plt.plot(x2, y2, 'm--', lw=4)

    plt.xlim(-2, 6)
    plt.ylim(-6, 6)

    plt.title("Plot of f(x) = 1 / (x - 1)")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.show()


# Problem 4
def prob4():
    """ Plot the functions sin(x), sin(2x), 2sin(x), and 2sin(2x) on the
    domain [0, 2pi], each in a separate subplot of a single figure.
        1. Arrange the plots in a 2 x 2 grid of subplots.
        2. Set the limits of each subplot to [0, 2pi]x[-2, 2].
        3. Give each subplot an appropriate title.
        4. Give the overall figure a title.
        5. Use the following line colors and styles.
              sin(x): green solid line.
             sin(2x): red dashed line.
             2sin(x): blue dashed line.
            2sin(2x): magenta dotted line.
    """
    x = np.linspace(0, 2 * np.pi, 1000)

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))

    axes[0, 0].plot(x, np.sin(x), 'g-')
    axes[0, 0].set_title("sin(x)")
    axes[0, 0].axis([0, 2 * np.pi, -2, 2])

    axes[0, 1].plot(x, np.sin(2 * x), 'r--')
    axes[0, 1].set_title("sin(2x)")
    axes[0, 1].axis([0, 2 * np.pi, -2, 2])

    axes[1, 0].plot(x, 2 * np.sin(x), 'b--')
    axes[1, 0].set_title("2sin(x)")
    axes[1, 0].axis([0, 2 * np.pi, -2, 2])

    axes[1, 1].plot(x, 2 * np.sin(2 * x), 'm:')
    axes[1, 1].set_title("2sin(2x)")
    axes[1, 1].axis([0, 2 * np.pi, -2, 2])

    fig.suptitle("Variations of sin(x) on [0, 2π]", fontsize=16)

    fig.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


# Problem 5
def prob5():
    """ Visualize the data in FARS.npy. Use np.load() to load the data, then
    create a single figure with two subplots:
        1. A scatter plot of longitudes against latitudes. Because of the
            large number of data points, use black pixel markers (use "k,"
            as the third argument to plt.plot()). Label both axes.
        2. A histogram of the hours of the day, with one bin per hour.
            Label and set the limits of the x-axis.
    """
    data = np.load("FARS.npy")
    
    hours = data[:, 0]
    longitudes = data[:, 1]
    latitudes = data[:, 2]

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    axes[0].plot(longitudes, latitudes, "k,", markersize=1)
    axes[0].set_xlabel("Longitude")
    axes[0].set_ylabel("Latitude")
    axes[0].set_title("Crash Locations")
    axes[0].set_aspect("equal")

    axes[1].hist(hours, bins=np.arange(25) - 0.5, edgecolor='black')
    axes[1].set_xlim(-0.5, 23.5)
    axes[1].set_xticks(range(24))
    axes[1].set_xlabel("Hour of Day (0–23)")
    axes[1].set_ylabel("Number of Crashes")
    axes[1].set_title("Crashes by Hour")

    fig.suptitle("FARS Traffic Crash Data Visualization (2010–2014)", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()


# Problem 6
def prob6():
    """ Plot the function g(x,y) = sin(x)sin(y)/xy on the domain
    [-2pi, 2pi]x[-2pi, 2pi].
        1. Create 2 subplots: one with a heat map of g, and one with a contour
            map of g. Choose an appropriate number of level curves, or specify
            the curves yourself.
        2. Set the limits of each subplot to [-2pi, 2pi]x[-2pi, 2pi].
        3. Choose a non-default color scheme.
        4. Include a color scale bar for each subplot.
    """
    x = np.linspace(-2*np.pi, 2*np.pi, 400)
    y = np.linspace(-2*np.pi, 2*np.pi, 400)
    X, Y = np.meshgrid(x, y)

    with np.errstate(divide='ignore', invalid='ignore'):
        G = (np.sin(X) * np.sin(Y)) / (X * Y)
        G[np.isnan(G)] = 0

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    heat = ax1.imshow(G, extent=[-2*np.pi, 2*np.pi, -2*np.pi, 2*np.pi],
                      origin='lower', cmap='viridis', aspect='equal')
    ax1.set_title("Heat Map of g(x, y)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("y")
    fig.colorbar(heat, ax=ax1)

    contour = ax2.contourf(X, Y, G, levels=20, cmap='plasma')
    ax2.set_title("Contour Map of g(x, y)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("y")
    ax2.set_aspect('equal')
    fig.colorbar(contour, ax=ax2)

    fig.suptitle("Visualization of g(x, y) = sin(x)·sin(y) / (x·y)", fontsize=14)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    prob1()
    prob2()
    prob3()
    prob4()
    prob5()
    prob6()