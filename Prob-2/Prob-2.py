# Module 2
#   Programming Assignment 3
#     Prob-2.py

# YOUR NAME

def example():
    print("\nExample Output")
   # section 1
    x = 5
    # print x and its type
    print("x", x, "is a", type(x))

    # section 2
    print()
    x = float(x)
    print("x", x, "is a", type(x))

def studentCode():
    print("\nJeremy's Output")

    # section 1
    x = 5
    print("x", x, "is a", type(x))

    # section 2
    print()
    y = 3.14
    y = float(y)
    print("y", y, "is a", type(y))

    #section 3
    print()
    z = "a string"
    z = str(z)
    print("z", z, "is a", type(z))

    

    # print the values for x, y, and z and their types each on a separate line

    print()
    # section 2
    # convert y to an int and print

    y = 9.99
    # convert y to an int and print
    y=int(y)
    print(y)
    print("y", y, "is a", type(y))


    z = "12.34"
    # print z and its type
    
    # use eval() to convert z to a number and print its value and type
    print()
    eval(z)
    z=float(z)
    print("z", z, "is a", type(z))
    print()

example()
studentCode()