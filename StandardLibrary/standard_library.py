# standard_library.py
"""Python Essentials: The Standard Library.
<Name>
<Class>
<Date>
"""

from math import sqrt


# Problem 1
def prob1(L):
    """Return the minimum, maximum, and average of the entries of L
    (in that order, separated by a comma).
    """
    minL = min(L)
    maxL = max(L)
    avgL = sum(L) / len(L)
    return minL, maxL, avgL


# Problem 2
def prob2():
    """Determine which Python objects are mutable and which are immutable.
    Test integers, strings, lists, tuples, and sets. Print your results.
    """
    # int
    a = 10
    old_id = id(a)
    a = a + 1
    if id(a) == old_id:
        print("int: mutable")
    else:
        print("int: immutable")

    # str
    s = "hello"
    old_id = id(s)
    s = s + "!"
    if id(s) == old_id:
        print("str: mutable")
    else:
        print("str: immutable")

    # list
    lst = [1, 2, 3]
    lst_id = id(lst)
    lst.append(4)
    if id(lst) == lst_id:
        print("list: mutable")
    else:
        print("list: immutable")

    # tuple
    t = (1, 2, 3)
    old_id = id(t)
    t = t + (4,)
    if id(t) == old_id:
        print("tuple: mutable")
    else:
        print("tuple: immutable")

    # set
    st = {1, 2, 3}
    st_id = id(st)
    st.add(4)
    if id(st) == st_id:
        print("set: mutable")
    else:
        print("set: immutable")


# Problem 3
def hypot(a, b):
    """Calculate and return the length of the hypotenuse of a right triangle.
    Do not use any functions other than sum(), product() and sqrt() that are
    imported from your 'calculator' module.

    Parameters:
        a: the length one of the sides of the triangle.
        b: the length the other non-hypotenuse side of the triangle.
    Returns:
        The length of the triangle's hypotenuse.
    """
    from calculator import sum, product, sqrt
    
    return sqrt(sum(product(a, a), product(b, b)))


# Problem 4
def power_set(A):
    """Use itertools to compute the power set of A.

    Parameters:
        A (iterable): a str, list, set, tuple, or other iterable collection.

    Returns:
        (list(sets)): The power set of A as a list of sets.
    """
    from itertools import combinations

    result = []
    for i in range(len(A) + 1):
        for subset in combinations(A, i):
            result.append(set(subset))
    return result


# Problem 5: Implement shut the box.
def shut_the_box(player, timelimit):
    """Play a single game of shut the box."""
    raise NotImplementedError("Problem 5 Incomplete")


if __name__ == "__main__":
    print(prob1([1,2,3,4,5]))
    prob2()
    print(hypot(3, 4))
    print(power_set("ABC"))