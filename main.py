# Author: Samuel Rudqvist
#
# A program to cover some basics of Python
#
# Change Log:
#           (20210623): Added the Fahrenheit to Celsius converter
#           (20210623): Added the chaos function
#
#
#



# Fahrenheit to Celsius converter
def FtoC():
    print ("This program converts temperature from celsius to fahrenheit\n")
    # eval() is used when the input is a number, it turns the string "32" into the number 32
    celsius = eval(input("Enter the temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print (celsius, "Celsius converts to: ", fahrenheit, "Fahrenheit")

# A chaotic function
def chaos():
    print ("\nThis program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)

# Uses eval() to find the answers from mathematical expressions.
def evaluate():
    print("\nThis function evaluates the math expression from the user input.")
    ans = eval(input("Enter an expression: "))
    print("Answer:", ans)

# Choose what to run
#FtoC()
#chaos()
evaluate()