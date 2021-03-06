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

def click():
    print("Opens a window which gets the pixels where you click 10 times")
    win = GraphWin("Click Me!")
    for i in range(10):
        pixel = win.getMouse()
        print("You clicked at:", pixel.getX(), pixel.getY())

def triangle():
    print("This function will let the user draw a triangle by clicking")
    win = GraphWin("Draw a Triangle")
    win.setCoords(0.0, 0.0, 10.0, 10.0)
    message = Text(Point(5, 0.5), "Click on three points")
    message.draw(win)
    # Get and draw three vertices of a triangle
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    # Use polygon object to draw the triangle
    # The polygon class can draw any multi-sided, closed shape, it accepts any
    # number of points and connects them in the order given
    triangle = Polygon(p1,p2,p3)
    triangle.setFill("peachpuff")
    triangle.setOutline("cyan")
    triangle.setWidth(2)
    triangle.draw(win)
    # Wait for another click to exit
    message.setText("Click anywhere to quit")   # uses the same point as the message in the beginning
    win.getMouse()

def clickNType():
    win = GraphWin("Click and type", 400, 400)
    for i in range(10):
        pt = win.getMouse()
        key = win.getKey()
        label = Text(pt, key)
        label.draw(win)

def tempConverter():
    win = GraphWin("Celsius Converter", 400,300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    # Draw the interface
    Text(Point(1,3),"    Celsius Temperature:").draw(win)
    Text(Point(1,1), "Fahrenheit Temperature:").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25,1), "")
    outputText.draw(win)
    button = Text(Point(1.5,2.0), "Convert It")
    button.draw(win)
    Rectangle(Point(1,1.5), Point(2,2.5)).draw(win)
    # Wait for a mouse click
    win.getMouse()
    # Convert input
    celsius = float(inputText.getText())
    fahrenheit = 9.0/5.0 * celsius + 32
    # Display the output and change button
    outputText.setText(round(fahrenheit,2))
    button.setText("Quit")
    # Wait for click then quit
    win.getMouse()
    win.close()

def animation():
    win = GraphWin("Animation example", 400, 250, autoflush=False)
    p1 = win.getMouse()
    p1.draw(win)
    p2 = win.getMouse()
    p2.draw(win)
    p3 = win.getMouse()
    p3.draw(win)
    for i in range(1000):
        triangle = Polygon(p1,p2,p3)
        triangle.setFill("peachpuff")
        triangle.setOutline("cyan")
        triangle.setWidth(2)
        triangle.draw(win)
        update(2)
        triangle = Polygon(p1,p2,p3)
        triangle.setFill("cyan")
        triangle.setOutline("peachpuff")
        triangle.setWidth(2)
        triangle.draw(win)
        update(2)

# What to run
#investmentChart()
#ticTacToe()
#investmentChart2()
#click()
#triangle()
#clickNType()
#tempConverter()
animation()

#root.mainloop()
