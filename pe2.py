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
def CtoF():
    print ("This program converts temperature from celsius to fahrenheit")
    # eval() is used when the input is a number, it turns the string "32" into the number 32
    for i in range(5):
        celsius = eval(input("\nEnter the temperature in Celsius: "))
        fahrenheit = 9/5 * celsius + 32
        print (celsius, "Celsius converts to: ", fahrenheit, "Fahrenheit")

# Modify the FtoC function to print a table of celsius temperatures and their 
# fahrenheit equivalents for every 10 degrees from 0C to 100C
def CtoFMod():
    print ("This program converts temperature from celsius to fahrenheit")
    # eval() is used when the input is a number, it turns the string "32" into the number 32
    celsius = 0
    for i in range(11):
        fahrenheit = 9/5 * celsius + 32
        print (celsius, "Celsius converts to: ", fahrenheit, "Fahrenheit")
        celsius = celsius + 10

# Modify the futureValue function to include additional yearly investments
# The inputs will be ammount to invest every year, total years and the interest rate

def futureValue():
    print("This function calculates a future value on a yearly investment over time\n")
    yearlyInvest = eval(input("Enter the yearly investment value: "))
    years = eval(input("Enter the ammount of years you will be saving: "))
    print("Interest rate: 1% = 0.01, 100% = 1")
    interest = eval(input("Enter the interest rate: "))
    value = 0
    for i in range(years):
        value = value + yearlyInvest
        print("Just invested", yearlyInvest)
        print("Value =", value)
        value = value * (1 + interest)
    print("\nThe total value after", years, "years will be:", value)

# Write a program that converts fahrenheit to celsius
def FtoC():
    print("This function converts fahrenheit to celsius.")
    fahrenheit = eval(input("Enter the temperature in Fahrenheit: "))
    celsius = (fahrenheit -32) * 5/9
    print(fahrenheit, "Fahrenheit converts to: ", celsius, "Celsius")

def KilometertToMiles():
    print("This function converts kilometers to miles.")
    km = eval(input("Enter kilometers: "))
    miles = km / 1.609
    print(km, "kilometers converts to", miles, "miles")

def KGtoLBS():
    print("This function converts kilograms to pounds")
    kg = eval(input("Enter the weight in kilograms: "))
    lbs = kg * 2.2046
    print(kg, "kg converts to: ", lbs, "lbs")


#Choose what to run
#average()
#CtoF()
#CtoFMod()
#futureValue()
#FtoC()
#KilometertToMiles()
KGtoLBS()