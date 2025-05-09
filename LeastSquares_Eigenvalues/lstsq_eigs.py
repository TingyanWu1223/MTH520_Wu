# lstsq_eigs.py
"""Volume 1: Least Squares and Computing Eigenvalues.
<Name>Tingyan Wu
<Class>MTH 520
<Date>5.9
"""

import numpy as np
from cmath import sqrt
from scipy import linalg as la
from matplotlib import pyplot as plt


# Problem 1
def least_squares(A, b):
    """Calculate the least squares solutions to Ax = b by using the QR
    decomposition.

    Parameters:
        A ((m,n) ndarray): A matrix of rank n <= m.
        b ((m, ) ndarray): A vector of length m.

    Returns:
        x ((n, ) ndarray): The solution to the normal equations.
    """
    
    Q, R = la.qr(A, mode='economic')
    Qt_b = Q.T @ b
    x = la.solve_triangular(R, Qt_b)
    return x


# Problem 2
def line_fit():
    """Find the least squares line that relates the year to the housing price
    index for the data in housing.npy. Plot both the data points and the least
    squares line.
    """
    data = np.load("housing.npy")
    years = data[:, 0]
    prices = data[:, 1]
    
    A = np.column_stack((years, np.ones(len(years))))
    b = prices
    
    a, b_est = least_squares(A, b)
    
    x_fit = np.linspace(years.min(), years.max(), 100)
    y_fit = a * x_fit + b_est
    
    plt.figure(figsize=(10, 6))
    plt.scatter(years, prices, color='black', label="Data Points")
    plt.plot(x_fit, y_fit, color='tab:blue', linewidth=2, label="Least Squares Fit")
    plt.title("Housing Price Index (2000-2010)")
    plt.xlabel("Year (0 = 2000)")
    plt.ylabel("Price Index")
    plt.legend()
    plt.show()


# Problem 3
def polynomial_fit():
    """Find the least squares polynomials of degree 3, 6, 9, and 12 that relate
    the year to the housing price index for the data in housing.npy. Plot both
    the data points and the least squares polynomials in individual subplots.
    """
    
    data = np.load("housing.npy")
    years = data[:, 0]
    prices = data[:, 1]

    degrees = [3, 6, 9, 12]
    x_fit = np.linspace(years.min(), years.max(), 500)

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    axes = axes.flatten()

    for i, degree in enumerate(degrees):
        A = np.vander(years, degree + 1)
        
        coeffs = la.lstsq(A, prices)[0]
        
        y_fit = np.polyval(coeffs, x_fit)
        
        axes[i].scatter(years, prices, color='black', label='Data Points')
        axes[i].plot(x_fit, y_fit, linewidth=2, label=f"Degree {degree} Fit")
        axes[i].set_title(f"Polynomial Degree {degree}")
        axes[i].set_xlabel("Year (0 = 2000)")
        axes[i].set_ylabel("Price Index")
        axes[i].legend()

    plt.tight_layout()
    plt.show()


def plot_ellipse(a, b, c, d, e):
    """Plot an ellipse of the form ax^2 + bx + cxy + dy + ey^2 = 1."""
    theta = np.linspace(0, 2*np.pi, 200)
    cos_t, sin_t = np.cos(theta), np.sin(theta)
    A = a*(cos_t**2) + c*cos_t*sin_t + e*(sin_t**2)
    B = b*cos_t + d*sin_t
    r = (-B + np.sqrt(B**2 + 4*A)) / (2*A)

    plt.plot(r*cos_t, r*sin_t)
    plt.gca().set_aspect("equal", "datalim")

# Problem 4
def ellipse_fit():
    """Calculate the parameters for the ellipse that best fits the data in
    ellipse.npy. Plot the original data points and the ellipse together, using
    plot_ellipse() to plot the ellipse.
    """
    raise NotImplementedError("Problem 4 Incomplete")


# Problem 5
def power_method(A, N=20, tol=1e-12):
    """Compute the dominant eigenvalue of A and a corresponding eigenvector
    via the power method.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The maximum number of iterations.
        tol (float): The stopping tolerance.

    Returns:
        (float): The dominant eigenvalue of A.
        ((n,) ndarray): An eigenvector corresponding to the dominant
            eigenvalue of A.
    """
    raise NotImplementedError("Problem 5 Incomplete")


# Problem 6
def qr_algorithm(A, N=50, tol=1e-12):
    """Compute the eigenvalues of A via the QR algorithm.

    Parameters:
        A ((n,n) ndarray): A square matrix.
        N (int): The number of iterations to run the QR algorithm.
        tol (float): The threshold value for determining if a diagonal S_i
            block is 1x1 or 2x2.

    Returns:
        ((n,) ndarray): The eigenvalues of A.
    """
    raise NotImplementedError("Problem 6 Incomplete")
