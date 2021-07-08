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
            print("Damn you're fast")
        print(ticket)
    except ValueError:
        print("Incorrect Input")
    except:
        print("Something went wrong...")

###
### Number 11, 12, 13
###
def leap(year):
    year = int(year)
    try:
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    except:
        print("Something Went Wrong")
    
def validateDate(date):
    try:
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        numDay = ["31","28","31","30","31","30","31","31","30","31","30","31"]
        numMonth = ["1","2","3","4","5","6","7","8","9","10","11","12"]
        numMonth2 = ["01","02","03","04","05","06","07","08","09","10","11","12"]
        m31 = ["01","03","05","07","08","10","12"]
        date = date.split("/")
        if date[0] == "02" and date[1] > "28":
            if date[1] == "29":
                if leap(date[2]):
                    print("Date is valid")
                    return True
                else:  
                    return False, print("Date invalid")
            elif date[1] > "29":
                return False, print(months[date], "Does not have more than 29 days")
        if date[1] == "31":
            print("31 days")
            date = int(date[0]) -1
            index = numMonth2[date]
            if index in m31:
                print("Date is valid")
                return True
            else:
                print(months[date], "Does not have 31 days")
                return False
        if date[1] < "31":
            return True
    except:
        print("Something Went Wrong")

def countDays():
    try:
        date = input("Enter a date (mm/dd/yyyy): ")
        year = date.split("/")[2]
        month = date.split("/")[0]
        day = date.split("/")[1]
        dayNum = 0
        if validateDate(date):
            day = int(day)
            month = int(month)
            year = int(year)
            #dayNum = dayNum + 31(month - 1) + day
            month2 = month -1
            dayNum = dayNum + 31 * month2 + day
            if leap(year):
                print("It's a leap year.")
                dayNum = dayNum + 1
            else:
                print("not a leap")
            if month > 2:
                dayNum = dayNum - (4 * month +23)//10
                print()
            print("The number of days so far in", year, "is", dayNum)
    except:
        print("Something Went Wrong")

### What to run ###
#salaries()
#BMI()
#speedTicket()
#validateDate("04/31/2020")
countDays()
#leap()