# Programming exercises chapter 8

def fibonachi():
    n = int(input("Enter the nth number you want (negative number to quit): "))
    n1, n2 = 1, 1
    count = 0
    if n < 0:
        quit()

    while n >= 0:
        if n == 0:
            print("Invalid Input")
        elif n == 1:
            print(n1)
        else:
            while count < n:
                print(n1)
                nth = n1 + n2
                # Update values
                n1 = n2
                n2 = nth
                count += 1
        n = int(input("Enter the nth number you want (negative to quit): "))
        n1, n2 = 1, 1
        count = 0
       
    



####
####
fibonachi()