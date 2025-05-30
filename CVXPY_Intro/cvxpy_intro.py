# cvxpy_intro.py
"""Volume 2: Intro to CVXPY.
<Name>
<Class>
<Date>
"""

import numpy as np
import cvxpy as cp

def prob1():
    """Solve the following convex optimization problem:

    minimize        2x + y + 3z
    subject to      x  + 2y         <= 3
                         y   - 4z   <= 1
                    2x + 10y + 3z   >= 12
                    x               >= 0
                          y         >= 0
                                z   >= 0

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    # Variable vector: [x, y, z]
    x = cp.Variable(3, nonneg=True)

    # Objective coefficients
    c = np.array([2, 1, 3])
    objective = cp.Minimize(c @ x)

    # Constraints
    constraints = [
        x[0] + 2*x[1] <= 3,
        x[1] - 4*x[2] <= 1,
        2*x[0] + 10*x[1] + 3*x[2] >= 12,
    ]

    # Formulate and solve the problem
    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()

    # Return the solution and objective value
    return x.value, optimal_value


# Problem 2
def l1Min(A, b):
    """Calculate the solution to the optimization problem

        minimize    ||x||_1
        subject to  Ax = b

    Parameters:
        A ((m,n) ndarray)
        b ((m, ) ndarray)

    Returns:
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n)
    objective = cp.Minimize(cp.norm(x, 1))
    constraints = [A @ x == b]
    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()
    return x.value, optimal_value


# Problem 3
def prob3():
    """Solve the transportation problem by converting the last equality constraint
    into inequality constraints.

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """

    x = cp.Variable(6, nonneg=True)

    c = np.array([4, 7, 6, 8, 8, 9])

    objective = cp.Minimize(c @ x)

    constraints = [
        x[0] + x[1] <= 7,     
        x[2] + x[3] <= 2,      
        x[4] + x[5] <= 4,     
        x[0] + x[2] + x[4] >= 5,  
        x[1] + x[3] + x[5] >= 8,  
    ]

    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()

    return x.value, optimal_value


# Problem 4
def prob4():
    """Find the minimizer and minimum of

    g(x,y,z) = (3/2)x^2 + 2xy + xz + 2y^2 + 2yz + (3/2)z^2 + 3x + z

    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    Q = np.array([
        [3, 2, 1],
        [2, 4, 2],
        [1, 2, 3]
    ])
    r = np.array([3, 0, 1])
    x = cp.Variable(3)
    objective = cp.Minimize(0.5 * cp.quad_form(x, Q) + r @ x)
    prob = cp.Problem(objective)
    optimal_value = prob.solve()
    return x.value, optimal_value


# Problem 5
def prob5(A, b):
    """Calculate the solution to the optimization problem
        minimize    ||Ax - b||_2
        subject to  ||x||_1 == 1
                    x >= 0
    Parameters:
        A ((m,n), ndarray)
        b ((m,), ndarray)
        
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """
    n = A.shape[1]
    x = cp.Variable(n, nonneg=True)
    objective = cp.Minimize(cp.norm(A @ x - b, 2))
    constraints = [cp.sum(x) == 1]
    prob = cp.Problem(objective, constraints)
    optimal_value = prob.solve()
    return x.value, optimal_value


# Problem 6
def prob6():
    """Solve the college student food problem. Read the data in the file 
    food.npy to create a convex optimization problem. The first column is 
    the price, second is the number of servings, and the rest contain
    nutritional information. Use cvxpy to find the minimizer and primal 
    objective.
    
    Returns (in order):
        The optimizer x (ndarray)
        The optimal value (float)
    """	 
    raise NotImplementedError("Problem 6 Incomplete")
    
if __name__ == "__main__":
    #prob1
    x_opt, obj_val = prob1()
    print("Optimal x:", x_opt)
    print("Optimal value:", obj_val)
    
    #prob2
    A = np.array([
        [1, 2, 1, 1],
        [0, 3, -2, -1]
    ])
    b = np.array([7, 4])
    x_opt, obj_val = l1Min(A, b)
    print("Optimal x:", x_opt)
    print("Optimal value:", obj_val)
    
    #prob3
    x_opt, obj_val = prob3()
    print("Optimal x:", x_opt)
    print("Optimal value:", obj_val)
    
    #prob4
    x_opt, obj_val = prob4()
    print("Optimal x:", x_opt)
    print("Optimal value:", obj_val)
    
    #prob5
    A = np.array([[1, 2, 1, 1], [0, 3, -2, -1]])
    b = np.array([7, 4])
    x_opt, obj_val = prob5(A, b)
    print("Optimal x:", x_opt)
    print("Optimal value:", obj_val)