# Chapter 6 Defining Functions
import graphics
import math

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
    # Get and draw three vertices