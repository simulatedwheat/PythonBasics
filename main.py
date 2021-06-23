# Author: Samuel Rudqvist
#
# A program to cover some basics of Python
#
# Change Log:
#           (20210623): Added the FtoC(), chaos(), evaluate(), average(), forLoop()
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


def average():
    print("\nThis function calculates the average of two numbers.")
    n1, n2 = eval(input("Enter two numbers seperated by a comma: "))
    average = (n1 + n2) / 2
    print("The average of",n1,"+",n2,"is: ", average)
    n3 = eval(input("Enter a number: "))
    n4 = eval(input("Enter a number: "))
    average2 = (n3 + n4) / 2
    print("The average of",n3,"+",n4,"is: ", average2)

def forLoop():
    # Definate loop, executes 10 times (0-9)
    for num in range(10):
        print(num)
    
def futureValue():
    print("This function calculates a future value on an investement over x ammount of years.")
    startVal = eval(input("Enter the starting value: "))
    years = eval(input("Enter the ammount of years you will be saving: "))
    interest = eval(input("Enter the interest rate: "))

    for i in range(years):
        startVal = startVal * (1 + interest)
    print("\nThe total value after", years, "years will be:", startVal)

    





# Choose what to run
#FtoC()
#chaos()
#evaluate()
#average()
#forLoop()
futureValue()