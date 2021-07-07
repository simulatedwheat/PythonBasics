# Chapter 7 Decision Structures
import math

def quadractic():
    print("This function finds the real solutions to a quadratic\n")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    

    discrim = b * b - 4 * a * c
    if discrim < 0:
        print("\nThe equation has no real roots")
    elif a == 0:
        print("Coefficient a can not be 0")
    elif discrim == 0:
        root = -b/(2*a)
        print("\nThere is a double root at",root)
    else:
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2*a)
        root2 = (-b - discRoot) / (2*a)
        print("\nThe solutions are: ", root1, root2)

# Using try and except for error handling
def quadractic1():
    print("This function finds the real solutions to a quadratic\n")
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2*a)
        root2 = (-b - discRoot) / (2*a)
        print("\nThe solutions are: ", root1, root2)
    except ValueError as excObj:
        if str(excObj) == "math domain error":
            print("\nNo real roots")
        else: 
            print("Invalid coefficient given")
    except:
        print("Something went wrong")

# Algorithm to find max value
def maxN():
    n = int(input("How many numbers are there? "))

    # Set max to be the first value
    maxVal = float(input("Enter a number >> "))
    # Compares the n-1 successive values
    for i in range(n-1):
        x = float(input("Enter a number >> "))
        if x > maxVal:
            maxVal = x
    print("The largest value is", maxVal)


## What to run ##
#quadractic()
#quadractic1()
maxN()