# Chapter 4 Objects and Graphics
# an input is needed at the end of the program to keep the window up
from graphics import *
def windows():
    win = GraphWin()

    p1 = Point(50,60)
    p1.draw(win)
    p2 = Point(60,60)
    p2.draw(win)


    win2 = GraphWin('shapes')
    center = Point(100,100)

    circle = Circle(center, 50)                             # center point and radius
    circle.setFill('red')                                   # fills the circle with color
    circle.draw(win2)                                       # draws the circle to the canvas

    label = Text(center, "Red Circle")
    label.draw(win2)

    rectangle = Rectangle(Point(30,30), Point(70,70))       # upper left, bottom right?
    rectangle.draw(win2)

    line = Line(Point(20,30), Point(180, 165))              # start and end
    line.draw(win2)

    oval = Oval(Point(20,150), Point(180, 199))
    oval.draw(win2)


    # Creating two eyes using the clone method
    win3 = GraphWin("eyes")
    leftEye = Circle(Point(80,50), 5)                       # creates a circle with radius 5
    leftEye.setFill('yellow')                               # fills with yellow
    leftEye.setOutline('red')                               # set the outline to red
    rightEye = leftEye.clone()                              # clones the leftEye 
    rightEye.move(20,0)                                     # moves the clone 20px to the right
    leftEye.draw(win3)
    rightEye.draw(win3)


    close = input("Exit program by hitting enter: ")


def investmentChart():

    print("This program plots the growth of a ten year investment")
    startVal = float(input("Enter the initial inestment: "))
    interest = float(input("Enter the interest: "))

    # Create the graphics window
    win = GraphWin("Investment Growth Chart", 320, 240)
    win.setBackground("white")       # set the background of the window to white
    # Labels
    Text(Point(20,230), "0.0K").draw(win)
    Text(Point(20,180), "2.5K").draw(win)
    Text(Point(20,130), "5.0K").draw(win)
    Text(Point(20,80), "7.5K").draw(win)
    Text(Point(20,30), "10.0K").draw(win)
    # Draw Bars
    for year in range(1,11):
        # Claculate the value for the next year
        startVal = startVal * (1 + interest)
        # Draw the bar for this value
        x11 = year * 25 + 40
        height = startVal *0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill("green")
        bar.setWidth(2)              # set the width of the outlining on the bars to 2px       
        bar.draw(win)
    input("Press <Enter> to quit")
    win.close()

def ticTacToe():
    print("This program makes a window using setCoords")
    win = GraphWin("Tic Tac Toe")
    # Set coordinates to go from 0,0 in the lower left
    # to 3,3 in the upper right
    win.setCoords(0.0, 0.0, 3.0, 3.0)
    # Draw vertical lines
    Line(Point(1,0), Point(1,3)).draw(win)
    Line(Point(2,0), Point(2,3)).draw(win)
    # Draw horizontal lines
    Line(Point(0,1), Point(3,1)).draw(win)    
    Line(Point(0,2), Point(3,2)).draw(win)    
    input("Press <Enter> to quit")
    win.close()


def investmentChart2():
    print("This program graphs the investment chart but it is scalable")
    startVal = float(input("Enter the initial investment: "))
    interest = float(input("Enter the interest: "))
    # Create the graphics window
    win = GraphWin("Investment Growth Chart", 600, 500)
    win.setBackground("white")
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1,0), '0.0K').draw(win)
    Text(Point(-1,2500), '2.5K').draw(win)
    Text(Point(-1,5000), '5.0K').draw(win)
    Text(Point(-1,7500), '7.5K').draw(win)
    Text(Point(-1,10000), '10.0K').draw(win)
    # Draw bar for initial investment
    bar = Rectangle(Point(0,0), Point(1, startVal))
    bar.setFill("green")
    bar.setWidth(2)
    bar.draw(win)
    # Draw bars for subsequent years
    for year in range(1,11):
        startVal = startVal * (1+interest)
        bar = Rectangle(Point(year, 0), Point(year+1, startVal))
        bar.setFill("green")
        bar.setWidth(2)
        bar.draw(win)
    input("Press <Enter> to quit")
    win.close()

# What to run
#investmentChart()
#ticTacToe()
investmentChart2()

#root.mainloop()
