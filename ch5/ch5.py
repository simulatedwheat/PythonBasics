# Chapter 5 Sequences: Strings, Lists, and Files.

def username():
    print("This function generates usernames.")
    # Get users first and last name
    fname = input("Enter your first name: ").lower()
    lname = input("Enter your last name: ").lower()
    # Concatenate first letter from fname and up to 7 in lastname
    uname = fname[0] + lname[:7]
    # Output the username
    print("Your username is:", uname)

def month():
    print("This function outputs an abbreviated month based on number input.")
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    n = int(input("Enter a month number (1-12): "))
    # Compute starting position of month n in months
    pos = (n-1) * 3
    # Grab the appropriate slice from months
    monthAbbrev = months[pos:pos+3]
    print("The month abbreviation is", monthAbbrev +".")

def monthList():
    print("This function prints the month name abbreviated.")
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    n = int(input("Enter a month nomber (1-12): "))
    print("The month abbreviation is", months[n-1]+".")

def text2Numbers():
    print("This function converts a textual characters into\na sequence of numbers representing the Unicode encoding.")
    # Get the message to encode
    message = input("Enter a message to encode: ")
    print("\nHere are the Unicode codes:")
    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")
    print()     # blank line before prompt


def numbers2Text():
    print("This function converts a string of Unicode numbers\nto the string that it represents\n")
    inString = input("Enter the ecoded message: ")
    # Loop through each substring and build the Unicode message
    message = ""
    for numStr in inString.split():
        codeNum = int(numStr)            # convert digits to a number
        message = message + chr(codeNum)    # concatenate character to message
    print("\nThe decoded message is:", message)
    # 83 116 114 105 110 103 115 32 97 114 101 32 70 117 110 33

def squares():
    # The squares of the first 100 real numbers
    squares = []
    for x in range(1,101):
        squares.append(x*x)
    print(squares)

def numbers2Text2():
    print("This function converts a string of Unicode numbers\nto the string that it represents\n")
    inString = input("Enter a Unicode-encoded string: ")

    chars = []
    for numStr in inString.split():
        codeNum = int(numStr)
        chars.append(chr(codeNum))
    message = "".join(chars)
    print("The decoded message is:", message)

# What to run
#username()
#month()
#monthList()
#text2Numbers()
#numbers2Text()
#squares()
numbers2Text2()