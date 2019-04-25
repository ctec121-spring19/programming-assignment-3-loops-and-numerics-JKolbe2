# Module 2
#   Programming Assignment 3
#     Prob-4.py

# YOUR NAME
from random import *
def main():
    print("\nJeremy's Output")

    # write code that will sum the numbers between 15 and 30 inclusive
    # and print the sum
    sum = 0
    for i in range(15, 31):
        sum = sum + i
        print(i)
        print("----")
        print(sum)

    # sum the numbers in the sequence [2, 4, 7, 9, 12, 14, 17, 19]
    # and print the sum
    sum = 0
    for i in [2, 4, 7, 9, 12, 14, 17, 19]:
        sum = sum + i
        print(i)
        print("----")
        print(sum)

    # use the randrange() function to sum 5 randomly generated numbers 
    # between 1 and 99 inclusive.
    # Print each random number on a line. 
    # Print the sum on the last line
    sum=0
    for i in range(5):
        num=randrange(1,100)
        print(num)



main()
