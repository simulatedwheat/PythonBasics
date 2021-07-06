# Programming Exercises Chapter 5
from tabulate import tabulate

# Converted to use string formatting.
def dateConvert():
    # Get the date
    dateStr = input("Enter a date(mm/dd/yyyy): ")
    # Split in to components
    monthStr, dayStr, yearStr = dateStr.split("/")
    # convert monthStr to month names
    months = ["January", "February", "March", "April", "May", 
                "June", "July", "August", "September", "October",
                 "November", "December"]
    monthStr = months[int(monthStr)-1]
    # Output result in format: month, day, year
    print("The converted date is: {0} {1}, {2}".format(monthStr,dayStr,yearStr))


def quizScore():
    score = int(input("Enter your score as an integer between 0 and 5: "))
    gt = "Your grade is: "
    if score == 5:
        print("{} A".format(gt))
    elif score == 4:
        print("{} B".format(gt))
    elif score == 3:
        print("{} C".format(gt))
    elif score == 2:
        print("{} D".format(gt))
    elif score == 1 or 0:
        print("{} F".format(gt))
    else: 
        print("Make sure to input your score as an integer between 0 and 5.")

def quizScore2():
    score = int(input("Enter your score as an integer between 0 and 100: "))
    gt = "Your grade is: "
    if score >= 90:
        print("{} A".format(gt))
    elif score >= 80 and score < 90:
        print("{} B".format(gt))
    elif score >= 70 and score < 80:
        print("{} C".format(gt))
    elif score >= 60 and score < 70:
        print("{} D".format(gt))
    elif score < 60:
        print("{} F".format(gt))
    else: 
        print("Make sure to input your score as an integer between 0 and 5.")


def acronym():
    str = input("Enter the phrase you want to make an acronym of: ")
    blank = []
    acro = str[0].upper()       # Gets the first letter, adds it to the acronym and makes it uppercase
    pos = 0
    
    # Adds the indexes of the blank spaces
    for i in range(len(str)):
        if str[i] == ' ':
            blank.append(i)
    # Gets the characters after the blanks, makes them upper case and adds them to the acronym
    for pos in range(len(blank)):
        index = blank[pos]
        c = str[index + 1].upper()
        acro += c
    print("The acronym is:",acro)

# Works for both #5 and #6
def nameNumber():
    name = input("Enter your first name: ").lower()
    alph = ['a','b','c','d','e','f','g','h','i',
            'j','k','l','m','n','o','p','q','r',
            's','t','u','v','w','x','y','z']
    # Set initial value to 0
    number = 0
    # loop through the length of the name, set c to the index of each letter
    # check to see that it is in the alphabet set the number's value and add
    # it to number
    for i in range(len(name)):
        c = name[i]
        if c in alph:
            num = alph.index(c) + 1
            number += num
    print(number)

def caesarCipher():
    print("CaesarCipher")
    message = input("Enter the message to encode: ").lower()
    key = int(input("Enter the key (int): "))
    encoded = []
    newStr = ""
#97 to 122
    for i in range(len(message)):
        c = message[i]
        uni = ord(c)
        # If input is z set value to 96
        if uni == 122:
            uni = 96
        encoding = uni + key
        newC = chr(encoding)
        newStr += newC
        encoded.append(encoding)
    print(encoded)
    print(newStr)

def countWords():
    print("A function that counts the words in a sentence.")
    sentence = input("Enter a sentence: ")
    counter = 0
    for i in range(len(sentence)):
        c = sentence[i]
        blank = ord(c)
        # Check if character is a blank space
        if blank == 32:
            counter += 1
        # Check if character is a period
        if blank == 46:
            counter += 1
            break       # break out of the loop
    print(counter)

def avgWordL():
    print("This function calculates the average word length\nof words in a sentence.")
    print("The sentence has to end with a period.")
    sentence = input("Enter a sentence: ")
    counter = 0
    length = []
    wordL = 0
    lSum = 0
    for i in range(len(sentence)):
        c = sentence[i]
        blank = ord(c)
        if blank != 32 and blank != 46:
            wordL += 1
        # Check if character is a blank space
        if blank == 32:
            counter += 1
            length.append(wordL)
            wordL = 0
        # Check if character is a period
        if blank == 46:
            counter += 1
            length.append(wordL)
            wordL = 0
            break       # break out of the loop
    # Loop through the list and calculate the average.
    for i in range (0, len(length)):
        lSum = lSum + length[i]
    average = lSum / counter
    print("\nThe average length of the words in the sentence is:",average,"\n")
    
def chaos():
    # don't forget to put on top
    # from tabulate import tabulate
    print ("\nThis program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    y = float(input("Enter another number between 0 and 1: "))
    sX = x
    sY = y
    index = 0
    list = []
    for i in range(10):
        innerList = []
        index += 1
        x = 3.9 * x * (1-x)
        y = 3.9 * y * (1-y)
        innerList.append(index)
        innerList.append(x)
        innerList.append(y)
        list.append(innerList)
        print(innerList)
    print(tabulate(list, headers = ["index", sX, sY]))



# What to run
#dateConvert()
#quizScore()
#quizScore2()
#acronym()
#nameNumber()
#caesarCipher()
#countWords()
#avgWordL()
chaos()