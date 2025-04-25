# numpy_intro.py
"""Python Essentials: Intro to NumPy.
<Name> Tingyan Wu
<Class> MTH 520
<Date> 2025.4.24
"""

import numpy as np


def prob1():
    """ Define the matrices A and B as arrays. Return the matrix product AB. """
    A =np.array([[3, -1, 4], [1,5, -9]])
    B =np.array([[2,6,-5,3],[5,-8,9,7],[9,-3,-2,-3]])
    product=np.dot(A,B)
    return product

def prob2():
    """ Define the matrix A as an array. Return the matrix -A^3 + 9A^2 - 15A. """
    A = np.array([[3, 1, 4],[1, 5, 9],[-5, 3, 1]])
    
    A2 = A @ A       
    A3 = A2 @ A      
    
    result = -A3 + 9 * A2 - 15 * A
    return result


def prob3():
    """ Define the matrices A and B as arrays using the functions presented in
    this section of the manual (not np.array()). Calculate the matrix product ABA,
    change its data type to np.int64, and return it.
    """
    A = np.triu(np.ones((7, 7), dtype=np.int64))
    B = -1 * np.ones((7, 7), dtype=np.int64)
    B += 6 * np.triu(np.ones((7, 7), dtype=np.int64))

    ABA = A @ B @ A
    return ABA


def prob4(A):
    """ Make a copy of 'A' and use fancy indexing to set all negative entries of
    the copy to 0. Return the resulting array.

    Example:
        >>> A = np.array([-3,-1,3])
        >>> prob4(A)
        array([0, 0, 3])
    """
    A_copy = A.copy()           
    A_copy[A_copy < 0] = 0      
    return A_copy

    

def prob5():
    """ Define the matrices A, B, and C as arrays. Use NumPy's stacking functions
    to create and return the block matrix:
                                | 0 A^T I |
                                | A  0  0 |
                                | B  0  C |
    where I is the 3x3 identity matrix and each 0 is a matrix of all zeros
    of the appropriate size.
    """
    A = np.array([[0, 2, 4],[1, 3, 5]])
    
    B = np.array([[3, 0, 0],[3, 3, 0],[3, 3, 3]])
    
    C = np.diag([-2, -2, -2])  
    
    AT = A.T                  
    I = np.eye(3, dtype=int)  

    
    zero_M33 = np.zeros((3, 3), dtype=int)
    zero_M32 = np.zeros((3, 2), dtype=int)
    zero_M22 = np.zeros((2, 2), dtype=int)
    zero_M23 = np.zeros((2, 3), dtype=int)


    top_row    = np.hstack([zero_M33, AT, I])
    middle_row = np.hstack([A, zero_M22, zero_M23])
    bottom_row = np.hstack([B, zero_M32, C])

    
    block = np.vstack([top_row, middle_row, bottom_row])

    return block
    


def prob6(A):
    """ Divide each row of 'A' by the row sum and return the resulting array.
    Use array broadcasting and the axis argument instead of a loop.

    Example:
        >>> A = np.array([[1,1,0],[0,1,0],[1,1,1]])
        >>> prob6(A)
        array([[ 0.5       ,  0.5       ,  0.        ],
               [ 0.        ,  1.        ,  0.        ],
               [ 0.33333333,  0.33333333,  0.33333333]])
    """
    row_sums = A.sum(axis=1, keepdims=True)
    return A / row_sums 
    


def prob7():
    """ Given the array stored in grid.npy, return the greatest product of four
    adjacent numbers in the same direction (up, down, left, right, or
    diagonally) in the grid. Use slicing, as specified in the manual.
    """
    raise NotImplementedError("Problem 7 Incomplete")


if __name__ == "__main__":
    print(prob1())
    
    print(prob2())
    
    
    print(prob3())
   
    A = np.array([-3,-1,3])
    print(prob4(A))
    
    print(prob5())
    
    A = np.array([[1,1,0],[0,1,0],[1,1,1]])
    print(prob6(A))