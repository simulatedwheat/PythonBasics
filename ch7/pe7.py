# Chapter 7 Programming Exercises

import math

###
### Number 1
###
def salaries():
    print("Calculate weekly salary, overtime pays 50% extra")
    try:
        h = float(input("How many hours? "))
        r = float(input("What is the hourly salary? "))
        if h > 40:
            over = h-40
            overSal = over * r * 1.5
            total = (40*r) + overSal
        else:
            total = h * r
        print("This week your salary is", total)

    except ValueError:
        print("Invalid Input.")
    except:
        print("Something Went Wrong.")

###
### Number 5
###

def BMI():
    print("Calculate BMI")
    try:
        weight = float(input("Weight in lbs: "))
        height = float(input("Height in inches: "))
        bmi = weight * 720 / height ** 2
        if bmi >= 19 and bmi <= 25:
            print("Your BMI is:", bmi, "Which is within the healthy range (19-25)")
        elif bmi < 19:
            print("Your BMI is:", bmi, "You are too skinny!")
        else:
            print("Your BMI is:", bmi, "You fat fuck!")
    except ValueError:
        print("Invalid Input")
    except:
        print("Something went wrong...")

###
### Number 6
###

def speedTicket():
    print("Calculate your ticket.")
    try:
        ticket = 50
        speed = int(input("Your speed in mph: "))
        limit = int(input("Enter the speed limit: "))
        if speed <= limit:
            print("The speed was within the speed limit.")
        if speed >= limit + 5:
            over = speed - limit
            plus = over * 5
            ticket = ticket + plus
        if speed >= 90:
            ticket = ticket + 200
            print("Damn you fast")
        print(ticket)
    except ValueError:
        print("Incorrect Input")
    except:
        print("Something went wrong...")


### What to run ###
#salaries()
#BMI()
speedTicket()