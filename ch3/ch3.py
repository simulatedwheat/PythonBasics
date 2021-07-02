# Chapter 3

import math


def changeCounter():
    print("Change Counter\n")
    print("Enter the count of each coin type: ")
    quarters = eval(input("Quarters: "))
    # Using int instead of eval ensures the user can't enter anything that is not an integer.
    dimes = int(input("Dimes: "))
    nickels = int(input("Nickels: "))
    pennies = int(input("Pennies: "))
    total = .25*quarters + .10*dimes + .05*nickels + .01*pennies
    print("\nThe total value of your change is ${0:0.2f}".format(total))

# pq-formeln
# import math required for this
# Crashes if there are no real roots...
def quadratic():
    print("This function finds the real solutions to a quadratic\n")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discRoot = math.sqrt(b * b - 4 * a * c)
    root1 = (-b + discRoot) / (2*a)
    root2 = (-b - discRoot) / (2*a)
    print("\nThe solutions are: ", root1, root2)

def factorial():
    n = int(input("Enter a whole number: "))
    fact = 1
    # starts at user input (n) and steps down (-1) to but not including 1 
    for factor in range(n, 1, -1):
        fact = fact * factor
    print("The factorial of", n, "is", fact)





# Choose what to run
changeCounter()
#quadratic()
#factorial()