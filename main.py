# Author: Samuel Rudqvist
#
# A program to cover some basics of Python
#
# Change Log:
#           (20210623): Added the Fahrenheit to Celsius converter



# Fahrenheit to Celsius converter
def FtoC():
    print ("This program converts temperature from celsius to fahrenheit\n")
    celsius = eval(input("Enter the temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32
    print (celsius, "Celsius, converts to: ", fahrenheit, "Fahrenheit")

