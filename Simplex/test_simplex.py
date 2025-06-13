"""Unit testing file for the Simplex lab"""

import simplex
import numpy as np

def test_simplex():
    """
    Write at least one unit test for problem 5, the simplex solver.
    """
    c = np.array([1.0])
    A = np.array([[1.0]])
    b = np.array([5.0])
    solver = simplex.SimplexSolver(c, A, b)
    opt, basic_vars, nonbasic_vars = solver.solve()
    assert opt == 0.0
    assert basic_vars == {1: 5.0}
    assert nonbasic_vars == {0: 0.0}

def test_simplex_example():
    # Sets up the values for the simplex problem.
    c = np.array([-3, -2])
    b = np.array([2, 5, 7])
    A = np.array([[1, -1], [3, 1], [4, 3]])

    # Runs the simplex solver.
    solver = simplex.SimplexSolver(c, A, b)
    sol = solver.solve()
    print(sol)
    # Checks if it returned the correct value
    assert sol[0] == -5.2, "Incorrect result from the simplex method"
