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
            
            
        # Bland's Rule
        self.N = list(range(self.n))
        self.B = list(range(self.n, self.n + self.m))
        
        #problem2
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

        # Objective row (row 0): value at origin = 0, then c coefficients
        D[0, 1:n+1] = c

        # Constraint rows (rows 1..m)
        D[1:, 0]        = b
        D[1:, 1:n+1]   = A
        D[1:, n+1:]    = np.eye(m)

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
            if a_ij > 0:
                ratio = self.dictionary[i, 0] / a_ij
                ratios.append((ratio, i))

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
        j = self._pivot_col()
        if j is None:
            return

        try:
            i = self._pivot_row(j)
        except ValueError:
            raise ValueError("Unbounded")

        D = self.dictionary

        piv = D[i, j]
        D[i, :] /= piv
        for r in range(D.shape[0]):
            if r != i:
                D[r, :] -= D[r, j] * D[i, :]

        varlist = self.N + self.B
        enter_idx = j - 1 
        leave_idx = self.n + (i - 1)
        
        varlist[enter_idx], varlist[leave_idx] = varlist[leave_idx], varlist[enter_idx]
 
        self.N = varlist[:self.n]
        self.B = varlist[self.n:]

        self.dictionary = D

    # Problem 5
    def solve(self):
        """Solve the linear optimization problem.

        Returns:
            (float) The minimum value of the objective function.
            (dict): The basic variables and their values.
            (dict): The nonbasic variables and their values.
        """
        while True:
            j = self._pivot_col()
            if j is None:
                break
            try:
                self.pivot()
            except ValueError:
                raise ValueError("Unbounded")

        D = self.dictionary
        raw_obj = D[0, 0]
        opt_value = round(-float(raw_obj), 10)

        basic_vars = {}
        for row in range(1, self.m + 1):
            var_idx = self.B[row-1]
            val = D[row, 0]
            basic_vars[var_idx] = round(float(val), 10)

        nonbasic_vars = { var: 0.0 for var in self.N }

        return opt_value, basic_vars, nonbasic_vars

# Problem 6
def prob6(filename='productMix.npz'):
    """Solve the product mix problem for the data in 'productMix.npz'.

    Parameters:
        filename (str): the path to the data file.

    Returns:
        ((n,) ndarray): the number of units that should be produced for each product.
    """
    raise NotImplementedError("Problem 6 Incomplete")
