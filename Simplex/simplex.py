"""Volume 2: Simplex

<Name>
<Date>
<Class>
"""

import numpy as np

# Problems 1-6
class SimplexSolver(object):
    """Class for solving the standard linear optimization problem

                        minimize        c^Tx
                        subject to      Ax <= b
                                         x >= 0
    via the Simplex algorithm.
    """
    # Problem 1
    def __init__(self, c, A, b):
        """Check for feasibility and initialize the dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.

        Raises:
            ValueError: if the given system is infeasible at the origin.
        """
        self.c = np.asarray(c, dtype=float)
        self.A = np.asarray(A, dtype=float)
        self.b = np.asarray(b, dtype=float)
        
        self.m, self.n = self.A.shape
        
        if self.c.size != self.n:
            raise ValueError(f"c must have length {self.n}, but has length {self.c.size}")
        if self.b.size != self.m:
            raise ValueError(f"b must have length {self.m}, but has length {self.b.size}")

        if np.any(self.b < 0):
            raise ValueError("Infeasible at origin: some entries of b are negative")
            
        self.N = list(range(self.n))
        self.B = list(range(self.n, self.n + self.m))
        
        self.dictionary = self._generatedictionary(self.c, self.A, self.b)


    # Problem 2
    def _generatedictionary(self, c, A, b):
        """Generate the initial dictionary.

        Parameters:
            c ((n,) ndarray): The coefficients of the objective function.
            A ((m,n) ndarray): The constraint coefficients matrix.
            b ((m,) ndarray): The constraint vector.
        """
        m, n = A.shape
        D = np.zeros((m + 1, n + m + 1))
        D[0, 1:n+1] = c
        D[1:, 0] = b
        D[1:, 1:n+1] = A
        D[1:, n+1: ]= np.eye(m)

        return D


    # Problem 3a
    def _pivot_col(self):
        """Return the column index of the next pivot column.
        """
        for j in range(1, self.dictionary.shape[1]):
            if self.dictionary[0, j] < 0:
                return j
        return None

    # Problem 3b
    def _pivot_row(self, index):
        """Determine the row index of the next pivot row using the ratio test
        (Bland's Rule).
        """
        ratios = []
        for i in range(1, self.m + 1):
            a_ij = self.dictionary[i, index]
            if a_ij < 0:
                ratio = -self.dictionary[i, 0] / a_ij
                if ratio >= 0:
                    ratios.append((ratio, i))
        if not ratios:
            return None
        min_ratio = min(ratios, key=lambda x: x[0])[0]
        eps = 1e-8
        candidates = [i for (r, i) in ratios if abs(r - min_ratio) < eps]
        best_row = min(candidates, key=lambda i: self.B[i-1])
        return best_row

   # Problem 4
    def pivot(self):
        """Select the column and row to pivot on. Reduce the column to a
        negative elementary vector.
        """
        return NotImplementedError("Problem 4 Incomplete")

    # Problem 5
    def solve(self):
        """Solve the linear optimization problem.

        Returns:
            (float) The minimum value of the objective function.
            (dict): The basic variables and their values.
            (dict): The nonbasic variables and their values.
        """
        raise NotImplementedError("Problem 5 Incomplete")

    # Problem 6
    def prob6(filename='productMix.npz'):
        """Solve the product mix problem for the data in 'productMix.npz'.

        Parameters:
            filename (str): the path to the data file.

        Returns:
            ((n,) ndarray): the number of units that should be produced for each product.
        """
        raise NotImplementedError("Problem 6 Incomplete")

