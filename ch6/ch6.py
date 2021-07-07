# Chapter 6 Defining Functions
from graphics import *
import math


# Triangle with support functions
def square(x):
    return x**2

def distance(p1,p2):
    dist = math.sqrt(square(p2.getX() - p1.getX() 
            + square(p2.getY() - p1.getY())))
    return dist

def triangle():
    win = GraphWin("Draw a triangle")
    win.setCoords(0.0,0.0,10.0,10.0)
    message = Text(Point(5,0.5), "Click on three points")
    message.draw(win)
    # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    # Use polygon objects to draw the triangle
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("red2")
    triangle.setOutline("black")
    triangle.setWidth(2)
    triangle.draw(win)
    # Calculate the perimeter of the triangle
    perim = distance(p1,p2) + distance(p2,p3) + distance(p1, p3)
    message.setText("The perimeter is: {0:0.2f}".format(perim))
    # Wait for another click to exit
    win.getMouse()
    win.close()


# Happy Birthday 
def happy():
    return "Happy Birthday to you!\n"
def verseFor(person):
    lyrics = happy()*2 + "Happy Birthday, dear " + person + ".\n" + happy()
    return lyrics
def song():
    for person in ["Nikki", "Tommy", "Mick", "Vince"]:
        print(verseFor(person))

# Writes it to a file instead
def song2():
    outf = open("happybirthday.txt", "w")
    for person in ["Nikki", "Tommy", "Mick", "Vince"]:
        print(verseFor(person), file=outf)
    outf.close()

# useSumDiff
def sumDiff(x,y):
    sum = x + y
    diff = x - y
    return sum, diff
def useSumDiff():
    num1,num2 = input("Enter two numbers (num1, num2): ").split(",")
    s, d = sumDiff(float(num1), float(num2))
    print("The sum is:", s, "and the difference is", d)


def addInterest(balances, rate):
    for i in range(len(balances)):
        balances[i] = balances[i] * (1 + rate)

def test():
    amounts = [1000,2000,3000,4000] 
    rate = 0.05
    addInterest(amounts, rate)
    print(amounts)

####
####
#### Future Value
def createLabeledWindow():
    window = GraphWin("Investment Growth Chart", 320, 240)
    window.setBackground("white")
    window.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), "0.0K").draw(window)
    Text(Point(-1, 2500), "2.5K").draw(window)
    Text(Point(-1, 5000), "5.0K").draw(window)
    Text(Point(-1, 7500), "7.5K").draw(window)
    Text(Point(-1, 10000), "10.0K").draw(window)
    return window

def drawBar(window, year, height):
    bar = Rectangle(Point(year,0), Point(year+1, height))
    bar.setWidth(2)
    bar.setFill("green")
    bar.draw(window)

def futureVal():
    print("This program plots the growth of a 10 year investment.")
    startVal = float(input("Enter the initial investment: "))
    interest = float(input("Enter the apr (interest): "))
    win = createLabeledWindow()
    drawBar(win, 0, startVal)
    for year in range(1,11):
        startVal = startVal * (1 + interest)
        drawBar(win, year, startVal)
    input("Press <ENTER> to Quit")
    win.close()

    


# What to run
#triangle()
#song()
#song2()
#useSumDiff()
#test()
futureVal()
