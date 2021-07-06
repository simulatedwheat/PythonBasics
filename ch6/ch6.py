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
# What to run
#triangle()
#song()
song2()