#Chapter 8 Loop Structures and Booleans

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
    



### What to run ###
#loopComparison()
#average()
#average2()
#average3()
#averageFileFor()
#averageFileWhile()
averageNested()