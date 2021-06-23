# Programming Exercises Chapter 2
# Choose which function to run at the bottom

# Modify the average function to find the the average of three numbers
def average():
    print("\nThis function calculates the average of two numbers.")
    n1, n2, n3 = eval(input("Enter three numbers seperated by commas: "))
    average = (n1 + n2 + n3) / 3
    print("The average of",n1,"+",n2,"+",n3,"is: ", average)

# Modify the FtoC function to use a loop to get a temperature from
# the user five times and print each one
def FtoC():
    print ("This program converts temperature from celsius to fahrenheit")
    # eval() is used when the input is a number, it turns the string "32" into the number 32
    for i in range(5):
        celsius = eval(input("\nEnter the temperature in Celsius: "))
        fahrenheit = 9/5 * celsius + 32
        print (celsius, "Celsius converts to: ", fahrenheit, "Fahrenheit")

# Modify the FtoC function to print a table of celsius temperatures and their 
# fahrenheit equivalents for every 10 degrees from 0C to 100C
def FtoCMod():
    print ("This program converts temperature from celsius to fahrenheit")
    # eval() is used when the input is a number, it turns the string "32" into the number 32
    celsius = 0
    for i in range(11):
        fahrenheit = 9/5 * celsius + 32
        print (celsius, "Celsius converts to: ", fahrenheit, "Fahrenheit")
        celsius = celsius + 10






#Choose what to run
#average()
#FtoC()
FtoCMod()