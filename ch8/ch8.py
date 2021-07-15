#Chapter 8 Loop Structures and Booleans

from graphics import *

def loopComparison():
    print("Both these loops will give the same output.")
    # The while loop needs i to be initialized
    # The for loop does not
    i = 0
    # While Loop
    while i <= 10:
        print(i)
        # i needs to get larger or the loop will just print
        # out 0's for eternity, becoming an indefinite loop
        i = i +1
    # For Loop
    for i in range(11):
        print(i)

# Annoying use of a while loop since the user always has
# to say yes to add another number
def average():
    total = 0.0
    count = 0
    moreData = "yes"
    # Check the first input character for y or n
    while moreData[0] == "y":
        x = float(input("Enter a number: "))
        total = total + x
        count = count + 1
        moreData = input("Do you want to add more numbers? (yes/no): ").lower()
    print("The average of the numbers is:",total / count)

# Uses a sentinel to determine wether to keep going or not
# Still not good since it does not support negative numbers
def average2():
    total = 0.0
    count = 0
    x = float(input("Enter a number (negative to quit): "))
    while x >= 0:
        total = total + x
        count = count + 1
        x = float(input("Enter a number (negative to quit): "))
    print("The average of the numbers is:",total / count)
    
def average3():
    total = 0.0
    count = 0
    xStr = input("Enter a number hit <Enter> to quit. >>> ")
    while xStr != "":
        x = float(xStr)
        total = total + x
        count = count + 1
        xStr = input("Enter a number hit <Enter> to quit. >>> ")
    print("The average of the numbers is:",total / count)
    
def averageFileFor():
    fileName = input("Enter a file name with numbers on each line: ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    for line in infile:
        total = total + float(line)
        count = count + 1
    print("The average of the numbers is:",total / count)

def averageFileWhile():
    fileName = input("Enter a file name with numbers on each line: ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        total = total + float(line)
        count = count + 1
        line = infile.readline()
    print("The average of the numbers is:",total / count)
    
def averageNested():
    fileName = input("Enter a file name with numbers on each line: ")
    infile = open(fileName, 'r')
    total = 0.0
    count = 0
    line = infile.readline()
    while line != "":
        for xStr in line.split(","):
            total = total + float(xStr)
            count = count + 1
        line = infile.readline()
    print("The average of the numbers is:",total / count)
    
# Event driven, keyboard- driven color changing window
def event_loop():
    win = GraphWin("Color Window", 500, 500)
    # Event Loop: handle key presses until user presses q key
    while True:
        key = win.getKey()
        if key == "q":
            break           # exit loop
        # Process the key
        if key == "r":
            win.setBackground("red")
        elif key == "w":
            win.setBackground("white")
        elif key == "g":
            win.setBackground("green")
        elif key == "b":
            win.setBackground("black")
    # Exit program
    win.close()

def event_loop_2():
    win = GraphWin("Click and Type", 500, 500)
    while True:
        key = win.checkKey()
        if key == "q":
            break
        if key:
            handleKey(key, win)
        pt = win.checkMouse()
        if pt:
            handleClick(pt, win)
def handleKey(k, win):
    if k == "w":
        win.setBackground("white")
    elif k == "r":
        win.setBackground("red")
    elif k == "b":
        win.setBackground("black")
    elif k == "g":
        win.setBackground("green")
def handleClick(pt, win):
    pass

def event_loop_3():
    win = GraphWin("Click and Type", 500, 500)
    while True:
        key = win.checkKey()
        if key == "q":
            break
        if key:
            handleKey2(key, win)
        pt = win.checkMouse()
        if pt:
            handleClick2(pt, win)
def handleClick2(pt, win):
    # Create an entry for the user to type in
    entry = Entry(pt, 10)
    entry.draw(win)
    # Go Modal: loop until user hits Enter key
    while True:
        key = win.getKey()
        if key == "Return": break
    # Undraw the entry and create and draw text obj
    entry.undraw()
    typed = entry.getText()
    Text(pt, typed).draw(win)
    # Clear (ignore) any mouse click that occured during the text entry
    win.checkMouse()
def handleKey2(k, win):
    if k == "w":
        win.setBackground("white")
    elif k == "r":
        win.setBackground("red")
    elif k == "b":
        win.setBackground("black")
    elif k == "g":
        win.setBackground("green")


### What to run ###
#loopComparison()
#average()
#average2()
#average3()
#averageFileFor()
#averageFileWhile()
#averageNested()
#event_loop()
#event_loop_2()
event_loop_3()