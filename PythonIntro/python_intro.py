# python_intro.py
"""Python Essentials: Introduction to Python.
<Name> Tingyan Wu
<Class> MTH 520
<Date>
"""


# Problem 1 (write code below)
def print_hello():
    print("Hello, world!")

       
# Problem 2
def sphere_volume(r):
    """ Return the volume of the sphere of radius 'r'.
    Use 3.14159 for pi in your computation.
    """
    v = (4/3) * 3.14159 * r**3
    return v


# Problem 3
def isolate(a, b, c, d, e):
    """ Print the arguments separated by spaces, but print 5 spaces on either
    side of b.
    """
   # print("a","    b","     c","d","e")
    print(a,"     ", b, "     ",c,d,e)
     
# Problem 4
def first_half(my_string):
    """ Return the first half of the string 'my_string'. Exclude the
    middle character if there are an odd number of characters.

    Examples:
        >>> first_half("python")
        'pyt'
        >>> first_half("ipython")
        'ipy'
    """
    my_string_len=len(my_string)
    midd=my_string_len//2
    result = my_string[:midd]
    print(result)
    #return result

def backward(my_string):
    """ Return the reverse of the string 'my_string'.

    Examples:
        >>> backward("python")
        'nohtyp'
        >>> backward("ipython")
        'nohtypi'
    """
    a=my_string[::-1]
    
    return a

# Problem 5
def list_ops():
    """ Define a list with the entries "bear", "ant", "cat", and "dog".
    Perform the following operations on the list:
        - Append "eagle".
        - Replace the entry at index 2 with "fox".
        - Remove (or pop) the entry at index 1.
        - Sort the list in reverse alphabetical order.
        - Replace "eagle" with "hawk".
        - Add the string "hunter" to the last entry in the list.
    Return the resulting list.

    Examples:
        >>> list_ops()
        ['fox', 'hawk', 'dog', 'bearhunter']
    """
    animals=["bear","ant","cat","dog"]
    animals.append("eagle")
    animals[2]=("fox")
    animals.remove(animals[1])
    animals.sort(reverse=True)
    animals[1]="hawk"
    animals[len(animals)-1]=animals[len(animals)-1]+"hunter"
    return animals
    
    
    
# Problem 6
def pig_latin(word):
    """ Translate the string 'word' into Pig Latin, and return the new word.

    Examples:
        >>> pig_latin("apple")
        'applehay'
        >>> pig_latin("banana")
        'ananabay'
    """
    if word[0] in ["a", "e", "i", "o", "u"]:
        return word+"hay"
    else:
        return word[1:]+word[0]+"ay"


# Problem 7
def palindrome():
    """ Find and retun the largest panindromic number made from the product
    of two 3-digit numbers.
    """
    max = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if str(product) == str(product)[::-1]:
                if product > max:
                    max = product
    return max

# Problem 8
def alt_harmonic(n):
    """ Return the partial sum of the first n terms of the alternating
    harmonic series, which approximates ln(2).
    """
    answer = 0
    for i in range(1, n+1):
        answer = answer + ((-1)**(i+1))/i
    return answer
if __name__ == "__main__":
    print_hello()
    radius = 3
    print("radius: ", sphere_volume(radius))
    
    isolate(1,2,3,4,5)
    
    first_half("Hello,Chengdu")
    
    print(backward("Hello,Chengdu"))
    print(list_ops())
    print(pig_latin("banana"))
    print(palindrome())
    print(alt_harmonic(500000))