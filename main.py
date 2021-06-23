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



# Choose what to run
FtoC()
chaos()